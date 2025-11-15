import requests,re,os,threading,time
from user_agent import generate_user_agent
from colorama import Fore
from itertools import cycle
from typing import List
from concurrent.futures import ThreadPoolExecutor,as_completed





###Note: If you have only 5 session IDs or fewer, duplicate them in your sessions.txt file.
sessionids_file="sessions.txt"#session id's file name, you can change that here 
proxies_file="proxies.txt"#proxies file name, you can change that here 
time_out=4 #maximum time limit for proxy website requests 
proxy_check_urls=["https://www.google.com/",]#urls for proxy sites to check proxies






def logo():
    print(f"""
            {Fore.MAGENTA}TikTok{Fore.RESET}          {Fore.RED}V2.1{Fore.RESET}
 ____                       _       
|  _ \ ___ _ __   ___  _ __| |_ ___ 
| |_) / _ \ '_ \ / _ \| '__| __/ __|
|  _ <  __/ |_) | (_) | |  | |_\__ /
|_| \_\___| .__/ \___/|_|   \__|___/
          |_| <\> github.com/filza2""")

def read_lines_strip(path:str)->List[str]:
    try:
        with open(path,"r",encoding="utf-8") as f:lines=[line.strip() for line in f if line.strip()]
        return lines
    except FileNotFoundError:input("- Error The session id file is Not Found ...");exit()

def parse_proxy_line(line:str)->dict:
    if "@" in line:creds,host=line.split("@",1);proxy_url=f"http://{creds}@{host}"
    else:proxy_url=f"http://{line}"
    return {"http":proxy_url,"https":proxy_url}

def test_all_proxies(file_name=proxies_file):
    try:os.system('cls' if os.name=='nt'else'clear');logo();print('\n- Proxy Checking in progress this may take a while.\n')
    except:pass
    with open(file_name,"r",encoding="utf-8") as f:proxies=[line.strip() for line in f if line.strip()]
    working=[]
    lock=threading.Lock()
    def worker(p):
        if check_proxy_multi(p):
            with lock:working.append(p);print(f"\r {Fore.GREEN}Good{Fore.RESET} Proxy {p}",end="",flush=True)
        else:print(f"\r {Fore.RED}Bad{Fore.RESET} Proxy {p}",end="",flush=True)
    threads=[]
    for p in proxies:
        t=threading.Thread(target=worker,args=(p,),daemon=True)
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    print(f"\n- Proxy check Completed {Fore.RED}sucssfully{Fore.RESET} good proxies ratio : [{len(working)}/{len(proxies)}]")
    with open(file_name,"w",encoding="utf-8") as f:
        f.write("\n".join(working))
    print(f"- {file_name} has been updated with good proxies, and bad proxies have been {Fore.RED}deleted{Fore.RESET}")
    return working

def check_proxy_multi(proxy_line:str,required_success:int=1)->bool:#you can change required success, like 2 but this will take more time to check one proxy because it will be tested on {TEST_URLS} websites if more than 2 websites succeed this mean the proxy is good 
    proxies=parse_proxy_line(proxy_line)
    success=0
    for url in proxy_check_urls:
        try:
            r=requests.get(url,proxies=proxies,timeout=time_out)
            if r.status_code==200:success+=1
        except Exception:pass
        if success>=required_success:return True
    return False


def main(proxies_file):
    try:os.system('cls' if os.name == 'nt' else 'clear');logo()
    except:pass
    print(f"""
1-[{Fore.RED}Plagiarism{Fore.RESET}]    2-[{Fore.RED}Under 13{Fore.RESET}]   3-[{Fore.RED}Hate Speech{Fore.RESET}]
4-[{Fore.RED}Suicide&Self Injure{Fore.RESET}]  
5-[{Fore.RED}Frauds&scams{Fore.RESET}]  6-[{Fore.RED}S*x{Fore.RESET}]        7-[{Fore.RED}Violence{Fore.RESET}]""")
    try:fl=int(input('\n >> '))
    except ValueError:
        print(f'- Enter numbers {Fore.RED}ONLY{Fore.RESET} ..\n')
        try:fl=int(input('\n >> '))
        except ValueError:exit("- You will not be successful in life never, thanks don't want to serve you")
    report_ids={1:910121,2:91015,3:9002,4:90061,5:9004,6:90086,7:90013}
    report_id=report_ids.get(fl)
    if not report_id:print(f"\n\n- {Fore.RED}Wrong{Fore.RESET} Entry Try again ..");return
    target=input('- Target username : ').replace('@','')
    try:
        try:proxies_auto=int(input("\n- Proxies source\n1- Auto proxy (will take some time)\n2- You have proxy file\n> "))
        except ValueError:
            print('- Enter numbers ONLY ..\n')
            try:proxies_auto=int(input(' > '))
            except ValueError:exit("- You will not be successful in life never, thanks don't want to serve you")
        if proxies_auto==1:
            try:
                urls=[
                    'https://api.proxyscrape.com/?request=getproxies&proxytype=https&timeout=10000&country=all&ssl=all&anonymity=all',
                    'https://api.proxyscrape.com/v2/?request=getproxies&protocol=https&timeout=10000&country=all&ssl=all&anonymity=all',
                    'https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=all&ssl=all&anonymity=all',
                    'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all',
                    'https://alexa.lr2b.com/proxylist.txt','http://olaf4snow.com/public/proxy.txt','https://api.openproxylist.xyz/http.txt',
                    'https://www.proxy-list.download/api/v1/get?type=http',
                    'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt',
                    'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt',
                    'https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt',
                    'https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/https.txt',
                    'https://raw.githubusercontent.com/RX4096/proxy-list/main/online/https.txt',
                    'https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt',
                    'https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt',
                    'https://raw.githubusercontent.com/hanwayTech/free-proxy-list/main/https.txt',
                    'https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/https/https.txt',
                    'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt',
                    'https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt',
                    'https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt',
                    'https://raw.githubusercontent.com/HyperBeats/proxy-list/main/http.txt',
                    'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt',
                    'https://raw.githubusercontent.com/hendrikbgr/Free-Proxy-Repo/master/proxy_list.txt'
                    ] #imported from https://github.com/Filza2/Proxy-Scraper , #you can always modify the urls here by removing or adding which will definitely affect the proxy check and download speed.
                os.system('cls' if os.name=='nt'else'clear');logo();print('\n')
                for url in urls:
                    try:r=requests.get(url).text
                    except:pass
                    for px in re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\:\d{1,5}\b",str(r)):
                        with open(f'proxies.txt','a') as p:p.write(str(px+'\n'))
                        print(f"\rDownloaded --> {px}",end="",flush=True)
                test_all_proxies(file_name=proxies_file)
            except PermissionError:pass;exit(f"\n\n- Automatic proxy download failed, We have a Permission Error, Please manually download the proxy list and save it to a file named {proxies_file} to proceed.")
            except Exception as e:pass;exit(f'\n\n- Automatic proxy download failed. Please manually download the proxy list and save it to a file named {proxies_file} to proceed.')
        else:pass
        id_info_bysessionid(sessionids_file,proxies_file,target,report_id)
    except Exception as e:input(f'- Error ---> {e} ..\n');main(proxies_file)
    except KeyboardInterrupt:exit()


def id_info_bysessionid(sessionids_file,proxies_file,target,report_id):
    try:
        with open(sessionids_file,"r",encoding="utf-8") as f:sessionid=f.readline().strip()
        if not sessionid:input("\n- Error The session id file is Empty ...");exit()
        else:pass
    except FileNotFoundError:input("- Error The session id file is Not Found ...");exit()
    info_r=requests.get(f'https://www.tiktok.com/@{target}?lang=en',headers={'Host': 'www.tiktok.com','Cookie': f'sessionid={sessionid}','User-Agent': generate_user_agent(),'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate, br','Upgrade-Insecure-Requests': '1','Sec-Fetch-Dest': 'document','Sec-Fetch-Mode': 'navigate','Sec-Fetch-Site': 'none','Sec-Fetch-User': '?1','Te': 'trailers',"Priority": "u=0, i"})
    try:target_ID=re.findall('''"user":{"id":"(.*?)"''',info_r.text)[0]
    except Exception as e:
        target_ID=input('\n- Error getting Target ID, however you can enter it manually : ')
        if target_ID:pass
        else:exit("\n- Try again later ")
    sessions=read_lines_strip(sessionids_file)
    proxies=read_lines_strip(proxies_file)
    if not sessions:print("\n\n- No sessions found in",sessionids_file);exit()
    if not proxies:print("\n\n- No proxies found in",proxies_file);exit()
    total_s=len(sessions)
    total_p=len(proxies)
    try:os.system('cls' if os.name=='nt'else'clear');logo();print('\n')
    except:pass
    print(f'- Session ID info getting in process this will take some time\n')
    print(f"- Sessions loaded: {total_s}")
    print(f"- Proxies  loaded: {total_p}\n");time.sleep(0.5)
    proxy_cycle=cycle(proxies)
    session_ids={}
    lock=threading.Lock()
    max_thread=min(300,(total_s))#max threads recommended 
    request_timeout=globals().get("time_out",5)
    RETRIES=3#proxy retries
    def worker(sessionid,proxy_line,idx,total):
        proxies_dict=parse_proxy_line(proxy_line)
        ID=None
        ms_token=None
        success=False
        for a in range(RETRIES):
            try:
                info_r2=requests.get(f'https://www.tiktok.com/@{target}?lang=en',headers={'Host': 'www.tiktok.com','Cookie': f'sessionid={sessionid}','User-Agent': generate_user_agent(),'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate, br','Upgrade-Insecure-Requests': '1','Sec-Fetch-Dest': 'document','Sec-Fetch-Mode': 'navigate','Sec-Fetch-Site': 'none','Sec-Fetch-User': '?1','Te': 'trailers',"Priority": "u=0, i"},proxies=proxies_dict,timeout=request_timeout)
                if info_r2.status_code==200:
                    try:
                        ID=re.findall('''"uid":"(.*?)"''',info_r2.text)[0]
                        if not ID:
                            sID=re.search(r'"uid":"(\d+)"', info_r2.text)
                            if sID:ID=sID.group(1)
                    except Exception as e:
                        pass;print(f'- Error getting ID for ---> : [{sessionid}],  {e}')
                        #print(e)
                        #ID=input('\n- Error getting Your ID, however you can enter it manually : ')
                        #if ID:pass
                        #else:exit("\n- Try again later ")
                    try:
                        ms_token=info_r2.cookies.get("msToken")
                        if not ms_token:
                            rce=info_r2.headers.get("Set-Cookie","")
                            m=re.search(r'msToken=([^;]+)',rce)
                            if m:ms_token=m.group(1)
                    except:ms_token=""
                    if ID and ms_token:
                        success=True
                        break
                else:
                    continue
            except Exception as e:
                print(f"[{idx}] Proxy error ({proxy_line})")
                continue
        with lock:
            if success and ID and ms_token:
                session_ids[sessionid]={
                    "id": ID,
                    "ms_token": ms_token,
                    "sessionid": sessionid}
                print(f"\r[{idx}{Fore.MAGENTA}/{Fore.RESET}{total}] [{Fore.GREEN}+{Fore.RESET}] session={sessionid[:12]} --> id={ID} | ms_token={ms_token[:12]} | proxy={proxy_line}")
            else:
                print(f"\r[{idx}{Fore.MAGENTA}/{Fore.RESET}{total}] [{Fore.RED}X{Fore.RESET}] {Fore.RED}Failed{Fore.RESET} all retries for session={sessionid[:12]} | proxy={proxy_line}")

    with ThreadPoolExecutor(max_workers=min(max_thread,total_s)) as ex:
        futures=[]
        for i,sessionid in enumerate(sessions,start=1):
            proxy_line=next(proxy_cycle)
            futures.append(ex.submit(worker,sessionid,proxy_line,i,total_s))
        for fut in as_completed(futures):
            try:fut.result()
            except Exception as e:print(f"[{Fore.RED}!{Fore.RESET}] worker error:  ", e)
    print(f"\n- Collected info for {len(session_ids)} sessions ")
    start_reports_attack(session_ids,proxies,target,target_ID,report_id)


def start_reports_attack(session_ids,proxies,target,target_ID,report_id):
    total_s=len(session_ids)
    total_p=len(proxies)
    if not session_ids or not proxies:
        print("- Missing sessions or proxies.")
        return
    proxy_cycle=cycle(proxies)
    lock=threading.Lock()
    max_thread=min(300,(total_s))#max threads recommended 
    done=0
    error=0
    def worker(sessionid, info, proxy_line, idx, total):
        nonlocal done,error
        ID=info.get("id")
        ms_token=info.get("ms_token")
        MAX_PROXIES=15
        success=False
        for attempt,proxy_line in enumerate(proxies[:MAX_PROXIES],start=1):
            try:
                ok=REPORTS_Attack(
                    sessionid,
                    target,
                    target_ID,
                    ID,
                    ms_token,
                    idx,
                    total,
                    total_p,
                    proxy_line,
                    report_id)
                if ok==True:
                    success=True
                    print(f"\r[{idx}{Fore.MAGENTA}/{Fore.RESET}{total}] [{Fore.MAGENTA}/{Fore.RESET}] request sent {Fore.GREEN}sucssfully{Fore.RESET} via proxy {attempt}/{MAX_PROXIES} -> {proxy_line}")
                    break
            except Exception as e:
                print(f"\r[{idx}{Fore.MAGENTA}/{Fore.RESET}{total}] Proxy {Fore.RED}failed{Fore.RESET} ({attempt}/{MAX_PROXIES}) -> {proxy_line}")
                continue
        with lock:
            if success:done+=1
            else:
                error+=1
                print(f"\r[{idx}{Fore.MAGENTA}/{Fore.RESET}{total}] [X] All {MAX_PROXIES} proxies {Fore.RED}failed{Fore.RESET} for session {sessionid[:12]}")
                
    try:os.system('cls' if os.name=='nt'else'clear');logo();print('\n')
    except:pass
    with ThreadPoolExecutor(max_workers=max_thread) as ex:
        futures=[]
        for i,(sessionid,info) in enumerate(session_ids.items(),start=1):
            proxy_line=next(proxy_cycle)
            futures.append(ex.submit(worker,sessionid,info,proxy_line,i,total_s))
        for fut in as_completed(futures):
            try:
                fut.result()
            except Exception as e:
                print(f"[{Fore.RED}!{Fore.RESET}] worker error:", e)
    print(f"\n- Finished all threads. {Fore.GREEN}Done={done}{Fore.RESET} | {Fore.RED}Error={error}{Fore.RESET}")


def REPORTS_Attack(sessionid,target,target_ID,ID,ms_token,idx,total,total_p,proxy_line,report_id): 
    try:
        #print(sessionid,target,target_ID,ID,ms_token,idx,total,total_p,proxy_line,report_id)
        proxies_dict=parse_proxy_line(proxy_line)
        url=f'https://www.tiktok.com/aweme/v2/aweme/feedback/?WebIdLastTime=1762529639&aid=1988&app_language=en&app_name=tiktok_web&browser_language=en&channel=tiktok_web&object_id={int(target_ID)}&odinId={int(ID)}&owner_id={int(target_ID)}&reason={int(report_id)}&report_type=user&reporter_id={int(ID)}&target={int(target_ID)}'
        head={
            'Host': 'www.tiktok.com',
            'Cookie': f"sid_guard={sessionid}; sid_tt={sessionid}; sessionid={sessionid}; sessionid_ss={sessionid}; msToken={ms_token}",
            'User-Agent': generate_user_agent(),
            'Accept': '*/*',
            'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Referer': f'https://www.tiktok.com/@{target}',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'Priority': 'u=0',
            'Te': 'trailers'}
        r=requests.get(url,headers=head,proxies=proxies_dict,timeout=time_out)
        #print(r.text)
        if 'report_id' in r.text and r.json().get('report_id')!=0:
            print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN}Success{Fore.RESET} Report {Fore.RESET} | {sessionid[:12]}')
            return True
        elif r.json().get('status_code')==10:
            print(f'\r[{Fore.RED}-{Fore.RESET}] {Fore.RED}Failed{Fore.RESET} Report {Fore.RESET} | {sessionid[:12]}')
            return False
        elif 'report_id' not in r.text:
            print(f'\r[{Fore.RED}-{Fore.RESET}] {Fore.RED}Failed{Fore.RESET} Report {Fore.RESET} | {sessionid[:12]}')
            return False
        elif r.json().get('report_id')==0:
            print(f'\r[{Fore.RED}-{Fore.RESET}] {Fore.RED}Failed{Fore.RESET} Report {Fore.RESET} | {sessionid[:12]}')
            return False
        else:
            print(f'\n\t[{Fore.RED}!] Unable {Fore.RESET}to send report, unexpected response received :\n',r.text)
            exit("[!] please go to https://github.com/filza2 and tell filza about this error to make an update for the tool")
    
    except Exception as e:
        #print(e)
        return False



main(proxies_file)