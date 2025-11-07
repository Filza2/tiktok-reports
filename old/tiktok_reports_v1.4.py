import requests,re,time
from colorama import Fore
error,done=0,0
print("""
            TikTok          V1.4
 ____                       _       
|  _ \ ___ _ __   ___  _ __| |_ ___ 
| |_) / _ \ '_ \ / _ \| '__| __/ __|
|  _ <  __/ |_) | (_) | |  | |_\__ /
|_| \_\___| .__/ \___/|_|   \__|___/
          |_| <\> @TweakPY - @vv1ck
          """)
print("""
1-[None]          2-[Plagiarism User]          3-[Plagiarism Me]\n4-[S*x]           5-[Self-Injury]              6-[Annoying]\n7-[Violence]      8-[Under 13]                 9-[Cruelty animaly] \n10-[Cheat&Scam]   11-[Terrorism]               12-[Hate Speech] \n13-[Child Abuse]  14-[Violent Content]         15-[Bad prof pic]\n16-[Cotent]       17-[suicide]                 18-[Plagiarism Famous user]\n19-[Hate Groups]  20-[Promotion Of Criminal Activities]""")
fl=int(input('>'))
if fl==1:report_id=311
elif fl==2:report_id=3143
elif fl==3:report_id=3131
elif fl==4:report_id=308
elif fl==5:report_id=3052
elif fl==6:report_id=310
elif fl==7:report_id=3072
elif fl==8:report_id=317
elif fl==9:report_id=304
elif fl==10:report_id=3024
elif fl==11:report_id=3011
elif fl==12:report_id=306
elif fl==13:report_id=3093
elif fl==14:report_id=303
elif fl==15:report_id=3141
elif fl==16:report_id=399
elif fl==17:report_id=3051
elif fl==18:report_id=3073
elif fl==19:report_id=3013
elif fl==20:report_id=3021
print("---------------------------------------------------------")
sessionid=input('[?] Enter Session id : ')
target=input('[?] Enter Username Target : ')
sleep=int(input('[?] Enter Sleep [5/10] : '))
print("*********************************************************")
head1={
    'Host': 'www.tiktok.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Te': 'trailers',
    'Connection': 'close',}
req=requests.get(f'https://www.tiktok.com/@{target}?lang=en',headers=head1)
ID=re.findall('''"user":{"id":"(.*?)"''',req.text)[0]
url='https://www.tiktok.com/node/report/reasons_put?aid=1988&app_name=tiktok_web&device_platform=web_pc&device_id=6965670367281858049&region=SA&priority_region=SA&os=windows&referer=&root_referer=&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=ar&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0+(Windows)&browser_online=true&verifyFp=verify_1836fc1bf3f7deccde3944b94542fa17&app_language=ar&timezone_name=Asia%2FRiyadh&is_page_visible=true&focus_state=true&is_fullscreen=false&history_len=4'
head={
    'Cookie': f'tt_webid_v2=6965670367281858049; tt_webid=6965670367281858049; MONITOR_WEB_ID=6965670367281858049; _abck=DF7A347900A8D8FED81AFD5EE12008C7~-1~YAAQfDNWsm1IkCR6AQAAlkm1TAYdeigFmAycOmOWxft0YbRTSKOs7NaHScrsWmMKrgF0Q8MygS9PJYYIeXUipV02ajZtZQ60Qml5yYXInMgf/hmag4ZPfgVu5yWMJ/Y9kay1hOhykc0F5lr1aLuXGuw5hgipQF2Bbta01dwzFeNJ6lEDj8Qt6y1ycvgufkscePLNT1qAAcWYM6WnkuVrEKyIH1ueJFeN97XILjwXozkGhtQB22TwyrTs6qHeuI4AIXAOX4AR3mmLuIijdOm26JV7E+oseILjYmxVvs+bVa9t7dBnTLHv86SrtHIuse6pFR8ho8h4GZioLIGQIszbaVRuZYag0YS8gYQQXQ9rV4gHzl/JLiVUm13V22huRH3xDsLCHz+QCGa2zF8=~-1~-1~-1; ttwid=1%7CGgSBNxhEX3SRZ-8gRwj6trJuRqBn9FTPhb-bLV09ikY%7C1624784631%7Cf683a26c37bf889d5659b8b39f844ca3e5e8ef5d4068a1fd780b35d7ead43a5e; passport_csrf_token=f04fc476081a3d063b607f520e64780c; passport_csrf_token_default=f04fc476081a3d063b607f520e64780c; store-idc=alisg; store-country-code=kw; tt_csrf_token=9ABBszZbHK-ybQ4EmUNmO88d; R6kq3TV7=ANIltUx6AQAA0iR_0DT4isYyFe0wIvLcwlR2DLcu2HoxH_xr2S0UHDnko0X2|1|0|eb909f1c8b6476808c1eef972d934138938d3ff6; bm_sz=370278FCD4D299B700A745DEFAAB4B0D~YAAQfDNWsmxIkCR6AQAAlkm1TAw2bpWuOWe2G6NQNmzScG/m/xH6+Bem8m78w2/xA1Ha2lKE6MdNZ07JVFPoTVvp8FWL2M8G9QgMB02MBRYvrdTc2kD7ZUncdEr392PhTdcf6xJSYchBqThi7Bf/AYjoDGAEvd8b0LydfFMR4EUTIjS74FL0EOdqS8iz9UKW; ak_bmsc=B9040DAC3320D28FDD67A48B46D6575F~000000000000000000000000000000~YAAQfDNWsm5IkCR6AQAAlkm1TAy1aLYODh/mLGC2V6LsEt2XdGdRrZ1OjPijcPWKx5OQ76nFom4AOV76WA4wgozpx6RLYGtKMeuHKDvEe2K0MPj0XOxya3Ncidl3fWQH7st+H01osdxOq6hmZwppADsEaXXc6hca3gvnQIJGfoZI//q8Bu2eOIlpSUlPvESJu0uNEUk+KKrKHn/TlnhXGxyzrkxlFfP7CaL5FwddZlr7RFvevMCiymnHeOVMZaQbigbTb40hWSDiNjTBBb6MYEuqstefPomDVHa7gBUSw1e86/FJ7J8/GDfrH6v97vNyC/zCnho5zL6gl5Iyc1QHCp1nNdWrSzQ2pXHUwMNVUmizdgxM5B0aWHbTMcUMaKmndIyT5S2C8uwZ; csrf_session_id=df090d1141b540129aae2ff9154974e3; csrf_session_id=df090d1141b540129aae2ff9154974e3; bm_sv=5569F3C837EAA3EC3B3B9811A5D462D9~4u+GwfJaQ8rC17D45IxIXyOnJnYE1viTfbOgdfs3k0bp9EYRmgE8eFx928/JAVuP7MV2NDAAXHxkuORBxRVpAwI/dwnqOSrvCkLsimQ061YJb5gHtNIH3QMbwL+yTR9Q91H8lNAI2xKb/uUXKwXAbZO8vcqLAbKetV6VBxEwDFg=; s_v_web_id=verify_1836fc1bf3f7deccde3944b94542fa17; cmpl_token=AgQQAPOvF-RMpbCWRisot104-sqReLfT_4M0YP6syw; sid_guard={sessionid}%7C1624784625%7C5184000%7CThu%2C+26-Aug-2021+09%3A03%3A45+GMT; uid_tt=560c663051ee8ff8a3ff0068cf8eb4b98b29b305eedc84c15ca18d6869be8951; uid_tt_ss=560c663051ee8ff8a3ff0068cf8eb4b98b29b305eedc84c15ca18d6869be8951; sid_tt={sessionid}; sessionid={sessionid}; sessionid_ss={sessionid}; odin_tt=89e0ee29e1136ac2744696c6d6549510fb534ad7f9c0e511a6c6581a6b025c04f91814d3daecd456516c2ed276d5453767ceeda259ac65d2f139014dc96bdf438d81ad34e414f090f01f3d0b0d4d6ebc; passport_fe_beating_status=true',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/json',
    'Content-Length': '102',
    'Tt-Csrf-Token': '9ABBszZbHK-ybQ4EmUNmO88d',
    'X-Secsdk-Csrf-Token': '0001000000014ea713b3201bdb67f32cded9fd338566179a21daa4321f512da8c2c7b50bcdba168c6503d189e850',
    'Origin': 'https://www.tiktok.com',
    'Referer': f'https://www.tiktok.com/@{target}?lang=ar',
    'Te': 'trailers',
    'Connection': 'close'}
data={"reason":f'{int(report_id)}',"object_id":ID,"owner_id":ID,"report_type":"user"}
print(str(data))
while True:
    time.sleep(sleep)
    req=requests.post(url,json=data,headers=head)
    if '"statusCode":0,"errMsg":"نشكرك على ملاحظاتك"' in req.text:
        print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN}Done Report [{done}]{Fore.RESET} | {Fore.RED}Error Report [{error}]{Fore.RESET}')
        done+=1
    elif 'نأسف، الخادم غير متوفر حاليًا. يرجى المحاولة مرة أخرى' in req.text:
        print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN}Done Report [{done}]{Fore.RESET} | {Fore.RED}Error Report [{error}]{Fore.RESET}')
        error+=1
    else:
        print(f'\n\t[{Fore.RED}!] Error{Fore.RESET} sending report',req.text)
        exit("[!] Go to TweakPY on telegram and tell filza this error to make the update of tool batter")


