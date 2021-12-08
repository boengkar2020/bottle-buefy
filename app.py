import sys, os
sys.path.append(os.path.dirname(__file__))

from bottle import run, request, response, route, abort,default_app, static_file, mako_template, debug, redirect
import json, functools
from ast import literal_eval
#from models.session import *

PRODUCTION = False

if PRODUCTION :
    STATIC_PATH = '/your/absoulte/production/path/to/folder/static'
else:
    STATIC_PATH = './static'

if not PRODUCTION:
    debug(True)

app = application = default_app()

@route('/static/<filename:path>')
def send_file(filename):
    return static_file(filename,root=STATIC_PATH)

@route('/')
@route('/<page>')
def index(page = None):
    if not page:
        return mako_template('index.html')
    else:
        tpl = page + '.html'

        try:
            #return mako_template(tpl,user)
            return mako_template(tpl)
        except:
            return '<h1>Page not found</h1>'


if __name__ == '__main__':
    run(app,host='0.0.0.0',port=8000,reloader=True)
