
import json
from django.http import HttpResponse

def json_data(code = 200,msg = "success",data = {}):
    resp = {
        'status':code,
        'data':data,
        'mag':msg
    }
    data = json.dumps(resp, ensure_ascii=False)

    return HttpResponse(data, content_type="application/json;charset = utf-8")