from datetime import date , datetime
from decimal import Decimal
import jwt, uuid

def json_serialize(obj):
    if isinstance(obj,datetime):
        return obj.strftime("%Y-%m-%d %H:%M:%S")
    elif isinstance(obj,date):
        return obj.strftime("%Y-%m-%d")
    elif isinstance(obj,Decimal):
        return float(obj)
    raise TypeError ("Type {s} not serializable".format(s=type(obj)))

#change this value
TOP_SECRET = '001928nnadknillqeoqkqw_1283921'

def generate_token(data):
    if isinstance(data,dict):
        return jwt.encode(data,TOP_SECRET,algorithm='HS256').decode('utf-8')
    else:
        return jwt.encode({'data':data},TOP_SECRET,algorithm='HS256').decode('utf-8')

def generate_id(data):
    return str(uuid.uuid5(uuid.NAMESPACE_OID,data))

def first_letter(txt):
    return txt[0]
