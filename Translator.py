import json
import urllib.parse
import urllib.request

def translate(content):

    # URL of translator
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

    head = {}
    head['User_Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

    Form_Data = {}
    Form_Data['i'] = content
    Form_Data['from'] = 'AUTO'
    Form_Data['to'] = 'AUTO'
    Form_Data['smartresult'] = 'dict'
    Form_Data['client'] = 'fanyideskweb'
    Form_Data['salt'] = '15326858088180'
    Form_Data['sign'] = '4805445cac590750301ad08319a79675'
    Form_Data['ts'] = '1532685808818'
    Form_Data['bv'] = '9deb57d53879cce82ff92bccf83a3e4c'
    Form_Data['doctype'] = 'json'
    Form_Data['version'] = '2.1'
    Form_Data['keyfrom'] = 'fanyi.web'
    Form_Data['action'] = 'FY_BY_REALTIME'
    Form_Data['typoResult'] = 'false'
    data = urllib.parse.urlencode(Form_Data).encode('utf-8')

    req = urllib.request.Request(url, data, head)
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    targe = json.loads(html)
    dic_result = targe["translateResult"][0][0]["tgt"]

    return dic_result
