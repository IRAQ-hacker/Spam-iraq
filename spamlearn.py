#Author : ReKuShE
#YouTube : iraqhacker
#telegram : @iiwiw
#channel telegram : @Professional_school
#Thanks for using my tool, have a nice day 
import requests,uuid,secrets
from time import sleep
uid = uuid.uuid4()
r = requests.Session()
cookie = secrets.token_hex(8)*2
username = input('your user:')
password = input('your password:')
target = input('target:')
sle = int(input('sleep:'))
def login():
    global username
    global password
    url = 'https://www.instagram.com/accounts/login/ajax/'
    headers = {"user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36', 'x-csrftoken': 'missing', 'mid': cookie}
    data = {'username':username,
            'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(password),
            'queryParams': '{}',
            'optIntoOneTap': 'false',}
    req_login = r.post(url,headers=headers,data=data)
    if ("userId") in req_login.text:
        r.headers.update({'X-CSRFToken': req_login.cookies['csrftoken']})
        print('login True')
        url_id = 'https://www.instagram.com/{}/?__a=1'.format(target)
        req_id = r.get(url_id).json()
        user_id = str(req_id['logging_page_id'])
        idd = user_id.split('_')[1]
        done = 1
        while True:
            url_report = 'https://www.instagram.com/users/{}/report/'.format(idd)
            datas = {'source_name':'','reason_id':1,'frx_context':''} #spam
            report = r.post(url_report,data=datas)
            print('\033[0;31mdone spam \033[0;31mReKuShR {}'.format(done))
            sleep(sle)
            done += 1
            print("\033[0;96mYouTube : iraqhacker")
                 
    else:
        print('login false')
        print("\033[0;96m#Dev ReKuShE")
	
        exit()

login()

