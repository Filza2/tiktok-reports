try:import re;from time import sleep;from colorama import Fore;from requests import get,post
except Exception as e:print(f'[!] Download The Missing Module ! , {e}');exit()
error,done=0,0
print("""
            TikTok          V2
 ____                       _       
|  _ \ ___ _ __   ___  _ __| |_ ___ 
| |_) / _ \ '_ \ / _ \| '__| __/ __|
|  _ <  __/ |_) | (_) | |  | |_\__ /
|_| \_\___| .__/ \___/|_|   \__|___/
          |_| By @TweakPY - @vv1ck
          """)
print("""
1-[Self-Injury]\t\t2-[Plagiarism User]\t\t3-[Bad profile picutre]\n4-[Under 13]\t\t5-[else]""")
fl=int(input('>'))
if fl==1:report_id=90061
elif fl==2:report_id=910122
elif fl==3:report_id=910131
elif fl==4:report_id=91014
elif fl==5:report_id=9013
print("---------------------------------------------------------")
sessionid=input('[?] Enter Session id : ')
target=input('[?] Enter Target username : ')
slp=int(input('[?] Enter Sleep [5/10] : '))
print("---------------------------------------------------------")
rid=get(f'https://www.tiktok.com/@{target}',headers={
'Host': 'www.tiktok.com',
'Cookie': f'ttwid=1%7Cf1d9mI-3uCgb1W1ykT_ZvVGVVmxnggmGJ2TkBooEM1k%7C1661644523%7C102964ade11ca48ec226af6ebf7b674b7282c73affd87c87a209a43e7d50bb68; _abck=22E1C240F157DDF6067B25DFB9B821C1~-1~YAAQ5eRhXv0z76qCAQAAGxR54QgjtVxm3BwmbNsNvMg5PxPBKR5hu9S+ufq/XI5wOxRiMjWefWL8Aj0WO2n30bbHK+G7PSAeO3/plRIMYmhYKpmTExK//Z/7g4c0BGSG2DIjKXSDBMdpTwg+GVHcLPrYwnR+49aX/3ecT3fDPyulaMDzccSV2L64UpKMSWFXOIwidkuV4XvutbWyA687pqpmJx1q+vWyBoUQ3PmfNQBFuxhyVmwBjVRWNH8+TfVE6roGl6KJNw3rJlucYl+s8V5flZiOThkKv14WsTdeVt4aG4RwzUdzWYt7FYIPn7uxAxbp1Z7dRsbOf4B5jym2fwW79Q5ahsytbv7fXno8+1nQnIGwSVEuBfDp7KRWh0ZAX5+GTu9l9M5maQ==~-1~-1~-1; tt_csrf_token=NLIPKjMI-nbSZThQ8j7GKCRM5WbYhfW8b164; bm_sz=29169B1A00AF93E69A99EC87548A5BF1~YAAQ7eRhXmukQNOCAQAAFDVx4RBO2aK1snwE0si7+A9NXsWK4AMqJdKnUloLzLyehNfjAFJHIvADi90SqkRoXIRFcGysiopcTLM2MNbYcqqTyzoObd/M/wkr4j4is8m4Ny7dA943oCm0XG2aB/9tZ04dch04l1FVuY0eR3F6Lk1OBcWkjjTDfG58bx0kf57HCOeIFu6l9uPzcDW5Amc1HysA187WozFvL+zx1T/h2GUYRQmm508tKmlErJKFflYSZIOsG0oACB7WcQBWbWPVXdxZYKFyVIyTUsDlN3FRlvnbPR8=~3488048~4535876; __tea_cache_tokens_1988='+str('{%22_type_%22:%22default%22%2C%22user_unique_id%22:%227122424033622476290%22%2C%22timestamp%22:1661639613182}')+f'; msToken=0apSs85udSMKXsBSoIvwZaYjLeh663Wd_CqCrfpZ8Cxd1xieHCR8zLD3l83jE8_78MP6o-SEIgMNcAw5csP0vVXlKY6X5KG4EsP13PSdD0H6tWjat3Uo49aU7wNYNwCSFC0=; passport_csrf_token=13ece5f7e525190b87f121f3036fc2fa; passport_csrf_token_default=13ece5f7e525190b87f121f3036fc2fa; s_v_web_id=verify_l7chdt9a_7slNGyxb_mBhG_43Ss_8P7z_waU60HRLX7Az; odin_tt=9bc49ecc94c4d9859b8b1deb132bccfde523fe9b38750cc2082c83fe3a77df182990e999add6966efaa3cf1203380c5c6a493d952c75143b15e906167a7b1bad; cmpl_token=AgQQAPO_F-RO0rM0c6QIM104-LZ337Ba_4A0YMULRQ; sid_guard={sessionid}%7C1661640060%7C5184000%7CWed%2C+26-Oct-2022+22%3A41%3A00+GMT; uid_tt=45ac0a8230548d27c192f810cca59123e7516d2cb30dfe412bf79aa3373a7b35; uid_tt_ss=45ac0a8230548d27c192f810cca59123e7516d2cb30dfe412bf79aa3373a7b35; sid_tt={sessionid}; sessionid={sessionid}; sessionid_ss={sessionid}; sid_ucp_v1=1.0.0-KGQ5NTE4NmVjOTNmODFiNGRkOTc2MGMxYTVlOGI2ZWFlMGI2ZDQ2MjAKIAiBiIaAuKCnhWMQ_LqqmAYYswsgDDCuuqqYBjgEQOoHEAMaBm1hbGl2YSIgM2E4OWZjMDVmZmE5ZWIwMDE0NTU3ODM4ZTcwODE4ZTI; ssid_ucp_v1=1.0.0-KGQ5NTE4NmVjOTNmODFiNGRkOTc2MGMxYTVlOGI2ZWFlMGI2ZDQ2MjAKIAiBiIaAuKCnhWMQ_LqqmAYYswsgDDCuuqqYBjgEQOoHEAMaBm1hbGl2YSIgM2E4OWZjMDVmZmE5ZWIwMDE0NTU3ODM4ZTcwODE4ZTI; store-idc=alisg; store-country-code=sa; store-country-code-src=uid; tt-target-idc=alisg; passport_fe_beating_status=false; csrf_session_id=5d701bf19a877a2a4e1e3fa86f69af93; ak_bmsc=C447CEB3E0F85AFF614297D4481D403B~000000000000000000000000000000~YAAQ1O9hXklHBKuCAQAAF9Xf4RCNy5vrA6SlAzpy2T0io3QrPirE5nudeK5vLX/pmPsax5vf7ZNnFZ/cMgSoXlLDwIPoaj6LxFy+XXCc0wzrGjMG7n8Bx4ipNxrEFdsUoabIiNJO/EtgGAubERbYUSpjTShxLfndK4HjW3kmaeqrDol8DZ48n67TEFnHV5M9Hr8JXVwgMTrPBqPf9SReyq64j10WH5SonnHe3V+MEjWMChNhMO2uq8Hsle1UtGufVGI8Oze0eZ9cDKcsONFaly0XiwpqKkJ/vO8GoYY4dRbmomL0HyYEWpRUJQOUZp54JJetEnd/Qzo934v4XrAS1qd981DPeZH7Q7mC6zxXc6T6pAV8BD9EP7VYnHaYPd3ZQRbnELjvnY6wqA==; bm_sv=B8544CD5731378CBBE17F21AF892401D~YAAQ1u9hXkabypOCAQAAMm714RCX9cWClFBUzrQ9yamVsmMgw5PQKjFyo4MDb4AodaRlQzTI5r+OytdbZ/KlCOWqa4kK42qkhONCmz+QBFm9NLsNGYufflu6l+QexbTjHItkqSoLvfJRn73k41WjiPgeypTWJq0UitF9eRzj06xaRW286Gcm7N1gi6Q357Spmbj4euRQzM1JNA4l177RatieAEjYTLxOZ/liYRDxV+Yv2Wiv3qXS3SChxID73Vqd~1; msToken=0apSs85udSMKXsBSoIvwZaYjLeh663Wd_CqCrfpZ8Cxd1xieHCR8zLD3l83jE8_78MP6o-SEIgMNcAw5csP0vVXlKY6X5KG4EsP13PSdD0H6tWjat3Uo49aU7wNYNwCSFC0=',
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
'Accept-Encoding': 'gzip, deflate',
'Upgrade-Insecure-Requests': '1',
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'none',
'Sec-Fetch-User': '?1',
'Te': 'trailers'})
ID=str(re.findall('"authorId":"(.*?)",',rid.text)[0]).split(',')[0];usrid=str(re.findall('"uid":"(.*?)",',rid.text)[0])
url=f'https://www.tiktok.com/aweme/v1/aweme/feedback/?aid=1988&app_language=en&app_name=tiktok_web&browser_language=en&browser_name=Mozilla&browser_online=true&browser_platform=Linux%20x86_64&browser_version=5.0%20%28X11%29&channel=tiktok_web&cookie_enabled=true&current_region=SA&device_id=7122424033622476290&device_platform=web_pc&focus_state=true&from_page=user&history_len=9&is_fullscreen=false&is_page_visible=true&lang=ar&nickname=%D9%88%D9%83%D8%A7%D9%84%D8%A9%20%D8%B1%D9%88%D8%AD%20%D8%A7%D9%84%D8%B3%D9%81%D8%B1&object_id={ID}&os=linux&owner_id={ID}&priority_region=SA&reason={report_id}&referer=&region=SA&report_type=user&reporter_id={usrid}&root_referer=https%3A%2F%2Fwww.google.com%2F&screen_height=768&screen_width=1366&secUid=MS4wLjABAAAAjP4NJvV_yOYEMuNb4_Yjglfoy-EpDzHP88O5ARl85TM7PSU3WVWrK7xF3DHkekdi&target={ID}&tz_name=Asia%2FRiyadh&verifyFp=verify_l7chdt9a_7slNGyxb_mBhG_43Ss_8P7z_waU60HRLX7Az&webcast_language=ar&msToken=6Nus-3bKkLfqDRGOCLeUuVS0xzFGHfSsE7_AJzAE3WuStqC57DfGFsFdjIUCikUlV5KKVe0YFe7es_XDxbdB9iDb7hOnkrHjDATvY_Ie4CqyWQ7CByDKTUddTZhe4Ma7yWY=&X-Bogus=DFSzsIjubTsANSjSSBGe-GybrU2D&_signature=_02B4Z6wo0000199b9lQAAIDC3b9j.iAhcQ.fWvrAAJTl79'
head={
'Host': 'www.tiktok.com',
'Cookie': f'ttwid=1%7Cf1d9mI-3uCgb1W1ykT_ZvVGVVmxnggmGJ2TkBooEM1k%7C1661644523%7C102964ade11ca48ec226af6ebf7b674b7282c73affd87c87a209a43e7d50bb68; _abck=22E1C240F157DDF6067B25DFB9B821C1~-1~YAAQ5eRhXv0z76qCAQAAGxR54QgjtVxm3BwmbNsNvMg5PxPBKR5hu9S+ufq/XI5wOxRiMjWefWL8Aj0WO2n30bbHK+G7PSAeO3/plRIMYmhYKpmTExK//Z/7g4c0BGSG2DIjKXSDBMdpTwg+GVHcLPrYwnR+49aX/3ecT3fDPyulaMDzccSV2L64UpKMSWFXOIwidkuV4XvutbWyA687pqpmJx1q+vWyBoUQ3PmfNQBFuxhyVmwBjVRWNH8+TfVE6roGl6KJNw3rJlucYl+s8V5flZiOThkKv14WsTdeVt4aG4RwzUdzWYt7FYIPn7uxAxbp1Z7dRsbOf4B5jym2fwW79Q5ahsytbv7fXno8+1nQnIGwSVEuBfDp7KRWh0ZAX5+GTu9l9M5maQ==~-1~-1~-1; tt_csrf_token=NLIPKjMI-nbSZThQ8j7GKCRM5WbYhfW8b164; bm_sz=29169B1A00AF93E69A99EC87548A5BF1~YAAQ7eRhXmukQNOCAQAAFDVx4RBO2aK1snwE0si7+A9NXsWK4AMqJdKnUloLzLyehNfjAFJHIvADi90SqkRoXIRFcGysiopcTLM2MNbYcqqTyzoObd/M/wkr4j4is8m4Ny7dA943oCm0XG2aB/9tZ04dch04l1FVuY0eR3F6Lk1OBcWkjjTDfG58bx0kf57HCOeIFu6l9uPzcDW5Amc1HysA187WozFvL+zx1T/h2GUYRQmm508tKmlErJKFflYSZIOsG0oACB7WcQBWbWPVXdxZYKFyVIyTUsDlN3FRlvnbPR8=~3488048~4535876; __tea_cache_tokens_1988='+str('{%22_type_%22:%22default%22%2C%22user_unique_id%22:%227122424033622476290%22%2C%22timestamp%22:1661639613182}')+f'; msToken=6Nus-3bKkLfqDRGOCLeUuVS0xzFGHfSsE7_AJzAE3WuStqC57DfGFsFdjIUCikUlV5KKVe0YFe7es_XDxbdB9iDb7hOnkrHjDATvY_Ie4CqyWQ7CByDKTUddTZhe4Ma7yWY=; passport_csrf_token=13ece5f7e525190b87f121f3036fc2fa; passport_csrf_token_default=13ece5f7e525190b87f121f3036fc2fa; s_v_web_id=verify_l7chdt9a_7slNGyxb_mBhG_43Ss_8P7z_waU60HRLX7Az; odin_tt=57653a1c6306cd66ce3c4745f22992c803f4be0259edcac4a826b983cbf26a3f472938d0088cf44b8c8756427e0bd069cb26cd8ff3587e9974b2c242f15fcab690755fdbfc5a09131bb19b6b2d0b310b; cmpl_token=AgQQAPO_F-RO0rM0c6QIM104-LZ337Ba_4A0YMULRQ; sid_guard={sessionid}%7C1661640060%7C5184000%7CWed%2C+26-Oct-2022+22%3A41%3A00+GMT; uid_tt=45ac0a8230548d27c192f810cca59123e7516d2cb30dfe412bf79aa3373a7b35; uid_tt_ss=45ac0a8230548d27c192f810cca59123e7516d2cb30dfe412bf79aa3373a7b35; sid_tt={sessionid}; sessionid={sessionid}; sessionid_ss={sessionid}; sid_ucp_v1=1.0.0-KGQ5NTE4NmVjOTNmODFiNGRkOTc2MGMxYTVlOGI2ZWFlMGI2ZDQ2MjAKIAiBiIaAuKCnhWMQ_LqqmAYYswsgDDCuuqqYBjgEQOoHEAMaBm1hbGl2YSIgM2E4OWZjMDVmZmE5ZWIwMDE0NTU3ODM4ZTcwODE4ZTI; ssid_ucp_v1=1.0.0-KGQ5NTE4NmVjOTNmODFiNGRkOTc2MGMxYTVlOGI2ZWFlMGI2ZDQ2MjAKIAiBiIaAuKCnhWMQ_LqqmAYYswsgDDCuuqqYBjgEQOoHEAMaBm1hbGl2YSIgM2E4OWZjMDVmZmE5ZWIwMDE0NTU3ODM4ZTcwODE4ZTI; store-idc=alisg; store-country-code=sa; store-country-code-src=uid; tt-target-idc=alisg; passport_fe_beating_status=true; csrf_session_id=5d701bf19a877a2a4e1e3fa86f69af93; ak_bmsc=C447CEB3E0F85AFF614297D4481D403B~000000000000000000000000000000~YAAQ1O9hXklHBKuCAQAAF9Xf4RCNy5vrA6SlAzpy2T0io3QrPirE5nudeK5vLX/pmPsax5vf7ZNnFZ/cMgSoXlLDwIPoaj6LxFy+XXCc0wzrGjMG7n8Bx4ipNxrEFdsUoabIiNJO/EtgGAubERbYUSpjTShxLfndK4HjW3kmaeqrDol8DZ48n67TEFnHV5M9Hr8JXVwgMTrPBqPf9SReyq64j10WH5SonnHe3V+MEjWMChNhMO2uq8Hsle1UtGufVGI8Oze0eZ9cDKcsONFaly0XiwpqKkJ/vO8GoYY4dRbmomL0HyYEWpRUJQOUZp54JJetEnd/Qzo934v4XrAS1qd981DPeZH7Q7mC6zxXc6T6pAV8BD9EP7VYnHaYPd3ZQRbnELjvnY6wqA==; bm_sv=B8544CD5731378CBBE17F21AF892401D~YAAQT+9hXst0FtSCAQAAtibr4RDwi6umltC0Q/4nxqN+W2+H8jEqJiAM1UKq/WFRxvIWhD1cun7u+tsaokZUIFUtQ+BfD39WvB1UibsoZGFoWVjTKj4bK5EAwMu1QlH/12/pDUlhGiayqklz3tR7Z50CdBuzGqveSZ1+0zZm6huOffoPqGSwG9wceTQDSeLStHbo0q9U1uJ6k/nfDVNxu8euwA1o0E54chCfc6aWRX8Jo8WT4vwMtFAtkIsDIiHa~1; msToken=qGBWaC6AABYwCGW40MpO_ULzu3p1frMHAB2HusJhNaTTXidh2uPt3izjt9hj8Dwpa14bb3aqUr52_h3K_czyr7KjZhwsQIjRmMSPBAjTu6qfjDLCes5IQh7vysV_Z-FIjuw=',
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
'Accept': '*/*',
'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
'Accept-Encoding': 'gzip, deflate',
'Referer': f'https://www.tiktok.com/@{target}',
'Sec-Fetch-Dest': 'empty',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Site': 'same-origin',
'Te': 'trailers'}
print('\n')
while True:
	sleep(slp)
	req=post(url,headers=head)
	if 'Thanks for your feedback' in req.text:
		print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN}Done Report [{done}]{Fore.RESET} | {Fore.RED}Error Report [{error}]{Fore.RESET}',end=' ')
		done+=1
	elif 'Server is currently unavailable. Please try again later.' in req.text:
		print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN}Done Report [{done}]{Fore.RESET} | {Fore.RED}Error Report [{error}]{Fore.RESET}',end=' ')
		error+=1
	else:
		print(f'\n\t[{Fore.RED}!{Fore.RESET}] {Fore.RED}Error{Fore.RESET} sending report',req.text)
		exit("[!] Go to @TweakPY on Telegram and Tell filza this error to make the update of tool batter")
