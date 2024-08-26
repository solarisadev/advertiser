import requests
import time
import threading
from colorama import Fore, Style

# Banner
banner = """
                                                                                                                                                        dddddddd                                                                                                                                                     
   SSSSSSSSSSSSSSS                  lllllll                                       iiii                                       AAA                        d::::::d                                                                      tttt            iiii                                                           
 SS:::::::::::::::S                 l:::::l                                      i::::i                                     A:::A                       d::::::d                                                                   ttt:::t           i::::i                                                          
S:::::SSSSSS::::::S                 l:::::l                                       iiii                                     A:::::A                      d::::::d                                                                   t:::::t            iiii                                                           
S:::::S     SSSSSSS                 l:::::l                                                                               A:::::::A                     d:::::d                                                                    t:::::t                                                                           
S:::::S               ooooooooooo    l::::l   aaaaaaaaaaaaa  rrrrr   rrrrrrrrr  iiiiiii     ssssssssss                   A:::::::::A            ddddddddd:::::dvvvvvvv           vvvvvvv eeeeeeeeeeee    rrrrr   rrrrrrrrr   ttttttt:::::ttttttt    iiiiiii     ssssssssss       eeeeeeeeeeee    rrrrr   rrrrrrrrr   
S:::::S             oo:::::::::::oo  l::::l   a::::::::::::a r::::rrr:::::::::r i:::::i   ss::::::::::s                 A:::::A:::::A         dd::::::::::::::d v:::::v         v:::::vee::::::::::::ee  r::::rrr:::::::::r  t:::::::::::::::::t    i:::::i   ss::::::::::s    ee::::::::::::ee  r::::rrr:::::::::r  
 S::::SSSS         o:::::::::::::::o l::::l   aaaaaaaaa:::::ar:::::::::::::::::r i::::i ss:::::::::::::s               A:::::A A:::::A       d::::::::::::::::d  v:::::v       v:::::ve::::::eeeee:::::eer:::::::::::::::::r t:::::::::::::::::t     i::::i ss:::::::::::::s  e::::::eeeee:::::eer:::::::::::::::::r 
  SS::::::SSSSS    o:::::ooooo:::::o l::::l            a::::arr::::::rrrrr::::::ri::::i s::::::ssss:::::s             A:::::A   A:::::A     d:::::::ddddd:::::d   v:::::v     v:::::ve::::::e     e:::::err::::::rrrrr::::::rtttttt:::::::tttttt     i::::i s::::::ssss:::::se::::::e     e:::::err::::::rrrrr::::::r
    SSS::::::::SS  o::::o     o::::o l::::l     aaaaaaa:::::a r:::::r     r:::::ri::::i  s:::::s  ssssss             A:::::A     A:::::A    d::::::d    d:::::d    v:::::v   v:::::v e:::::::eeeee::::::e r:::::r     r:::::r      t:::::t           i::::i  s:::::s  ssssss e:::::::eeeee::::::e r:::::r     r:::::r
       SSSSSS::::S o::::o     o::::o l::::l   aa::::::::::::a r:::::r     rrrrrrri::::i    s::::::s                 A:::::AAAAAAAAA:::::A   d:::::d     d:::::d     v:::::v v:::::v  e:::::::::::::::::e  r:::::r     rrrrrrr      t:::::t           i::::i    s::::::s      e:::::::::::::::::e  r:::::r     rrrrrrr
            S:::::So::::o     o::::o l::::l  a::::aaaa::::::a r:::::r            i::::i       s::::::s             A:::::::::::::::::::::A  d:::::d     d:::::d      v:::::v:::::v   e::::::eeeeeeeeeee   r:::::r                  t:::::t           i::::i       s::::::s   e::::::eeeeeeeeeee   r:::::r            
            S:::::So::::o     o::::o l::::l a::::a    a:::::a r:::::r            i::::i ssssss   s:::::s          A:::::AAAAAAAAAAAAA:::::A d:::::d     d:::::d       v:::::::::v    e:::::::e            r:::::r                  t:::::t    tttttt i::::i ssssss   s:::::s e:::::::e            r:::::r            
SSSSSSS     S:::::So:::::ooooo:::::ol::::::la::::a    a:::::a r:::::r           i::::::is:::::ssss::::::s        A:::::A             A:::::Ad::::::ddddd::::::dd       v:::::::v     e::::::::e           r:::::r                  t::::::tttt:::::ti::::::is:::::ssss::::::se::::::::e           r:::::r            
S::::::SSSSSS:::::So:::::::::::::::ol::::::la:::::aaaa::::::a r:::::r           i::::::is::::::::::::::s        A:::::A               A:::::Ad:::::::::::::::::d        v:::::v       e::::::::eeeeeeee   r:::::r                  tt::::::::::::::ti::::::is::::::::::::::s  e::::::::eeeeeeee   r:::::r            
S:::::::::::::::SS  oo:::::::::::oo l::::::l a::::::::::aa:::ar:::::r           i::::::i s:::::::::::ss        A:::::A                 A:::::Ad:::::::::ddd::::d         v:::v         ee:::::::::::::e   r:::::r                    tt:::::::::::tti::::::i s:::::::::::ss    ee:::::::::::::e   r:::::r            
 SSSSSSSSSSSSSSS      ooooooooooo   llllllll  aaaaaaaaaa  aaaarrrrrrr           iiiiiiii  sssssssssss         AAAAAAA                   AAAAAAAddddddddd   ddddd          vvv            eeeeeeeeeeeeee   rrrrrrr                      ttttttttttt  iiiiiiii  sssssssssss        eeeeeeeeeeeeee   rrrrrrr            
"""

# Print the banner in red
print(Fore.RED + banner + Style.RESET_ALL)

content = input("Enter the message content to send: ")
per_sec = int(input("Enter how many times to send the message per second: "))
duration = int(input("Enter for how many seconds to send the message: "))
target = input("Do you want to send the messages to (1) Only General, (2) Only Advertising, or (3) Both? Enter 1, 2, or 3: ")

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en,en-US;q=0.9',
    'authorization': 'Bearer 26048|BIAa2I3PYscIdL5FtXz8NYOTc0aNGPxx0EnZdqqr8bcac629',
    'origin': 'https://dash.sellauth.com',
    'priority': 'u=1, i',
    'referer': 'https://dash.sellauth.com/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera GX";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36' 
}

data = {
    "content": content
}

def send_messages(url, headers, data, per_sec, duration, channel_name):
    start_time = time.time()
    while time.time() - start_time < duration:
        for _ in range(per_sec):
            response = requests.post(url, headers=headers, json=data)
            if response.status_code == 200:
                print(f"[+] Message Sent to {channel_name}")
            else:
                print(f"[-] Failed to send message to {channel_name}: {response.status_code}")
            time.sleep(600)
    print(f"Finished sending messages to {channel_name}.")

urls = {
    "1": ("https://api-internal.sellauth.com/v1/chat/channels/1/messages", "General"),
    "2": ("https://api-internal.sellauth.com/v1/chat/channels/2/messages", "Advertising"),
}

selected_urls = []
if target == "1":
    selected_urls.append(urls["1"])
elif target == "2":
    selected_urls.append(urls["2"])
elif target == "3":
    selected_urls.append(urls["1"])
    selected_urls.append(urls["2"])
else:
    print("Invalid input. Exiting.")
    exit(1)

threads = []
for url, channel_name in selected_urls:
    thread = threading.Thread(target=send_messages, args=(url, headers, data, per_sec, duration, channel_name))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Finished sending messages to all selected channels.")
