if __name__ == "__main__":
    try:
        import requests
        import instagramy
        import colorama
        import cfonts
        import time
        import json
        import socket
        import subprocess
        import io
        import sys
        import pip
        import random
        import platform
    except:
        from requests import get
        from instagramy import InstagramUser
        from colorama.initialise import init
        from colorama.ansi import Fore
        from cfonts import render , cli
        from time import sleep
        from json import loads
        from socket import gethostbyname , gethostname
        from subprocess import call
        from random import choice
        from sys import exit
        from platform import system

    try:
        if pip.__version__ == str(pip.__version__):
            if platform.system() == "Linux":
                pass
            else:
                sys.exit(0)
        else:
            subprocess.call(["python3" , "-m" , "pip" , "install" , "--upgrade" , "pip"])
    except Exception as E:
        raise E

    C = [
        f"{colorama.ansi.Fore.WHITE}",
        f"{colorama.ansi.Fore.GREEN}",
        f"{colorama.ansi.Fore.CYAN}",
        f"{colorama.ansi.Fore.MAGENTA}",
        f"{colorama.ansi.Fore.YELLOW}",
        f"{colorama.ansi.Fore.RED}" 
    ]

    F = [
        "black" , "red" , "green" , "yellow" ,
        "blue" , "magenta" , "cyan" , "white" ,
        "gray"
    ]

    L_IP = socket.gethostbyname(socket.gethostname())
    RE_Q = requests.get("https://api.myip.com").content
    LOAD = json.loads(RE_Q)
    P_IP = LOAD["ip"]
    C_RY = LOAD["country"]

    H = f"""
             {random.choice(C) or random.choice(C) and random.choice(C)}.:--================--:.             
           :+**++================+***+:           
         .+*+-.                    .-**+.         
         +**.                   -++: .**+         
        .**=         {random.choice(C) or random.choice(C) and random.choice(C)}:-====-:   +**-  =**:        
        :**-      .=***+==+***=.      -**-        
        -**:     :+*+:      :+**:     :**-        
        -++:    .+++          +**.    :**-        
        -++:    :++-          -**:    :**-        
        -++:    .++=          +**.    :**-        
        :++:     :++=:      :++*:     :**-        
        :++:      .=+++====+++=.      -**-        
        .++-         {random.choice(C) or random.choice(C) and random.choice(C)}:--==--:         =**:        
         =++.                        .**+         
          =++-.                    .-**+.         
           :=+++====---==========++**+-           
              ::----=============--:.
        """

    def HeaderFunc():
        print(f"{H}")
        time.sleep(1.5)
    HeaderFunc()

    def MainScript():
        time.sleep(1.5)
        print(f"\n\n{C[1]}[{C[3]}Python Version{C[1]}] {C[0]}: {C[2]}{pip.__version__}")
        print(f"\n{C[1]}[{C[3]}Local IP{C[1]}] {C[0]}: {C[2]}{L_IP}")
        print(f"\n{C[1]}[{C[3]}Public IP{C[1]}] {C[0]}: {C[2]}{P_IP}")
        print(f"\n{C[1]}[{C[3]}Country{C[1]}] {C[0]}: {C[2]}{C_RY}")
        print(f"\n\n{C[0]}<=========================================================>\n"
                      f"\n\t\t\t{C[3]}Help"
                      f"\n{C[1]}help => {C[2]}Opening The Help Center\n"
                      f"\n\n\t\t\t{C[3]}Scripts"
                      f"\n{C[1]}scripts/set-username => {C[2]}Setting The Username For Getting Page Information"
                      f"\n\n\t\t\t{C[3]}Options"
                      f"\n{C[1]}options/version => {C[2]}Shows The Script's Version"
                      f"\n{C[1]}options/license => {C[2]}Shows The Script's License\n"
                      f"\n\n\t\t\t{C[3]}Commands"
                      f"\n{C[1]}show-banner => {C[2]}Shows The Script banner"
                      f"\n{C[1]}update-script => {C[2]}Download The Latest Update Of Script"
                      f"\n{C[1]}exit => {C[2]}Exit the Script"
                      f"\n{C[0]}"
                      f"\n<=========================================================>\n"
                )
        while True:
            INPUT = str(input(f"\n\n{C[1]}[{C[3]}~{C[1]}] {C[1]}({C[5]}Inst4Inf0{C[1]})--$ \n{C[2]}[~] >{C[0]} "))
            if str(INPUT) == "help" or str(INPUT) == "Help" or str(INPUT) == "HELP":
                print(f"\n\n{C[0]}<=========================================================>\n"
                      f"\n\t\t\t{C[3]}Help"
                      f"\n{C[1]}help => {C[2]}Opening The Help Center\n"
                      f"\n\n\t\t\t{C[3]}Scripts"
                      f"\n{C[1]}scripts/set-username => {C[2]}Setting The Username For Getting Page Information"
                      f"\n\n\t\t\t{C[3]}Options"
                      f"\n{C[1]}options/version => {C[2]}Shows The Script's Version"
                      f"\n{C[1]}options/license => {C[2]}Shows The Script's License\n"
                      f"\n\n\t\t\t{C[3]}Commands"
                      f"\n{C[1]}show-banner => {C[2]}Shows The Script banner"
                      f"\n{C[1]}update-script => {C[2]}Download The Latest Update Of Script"
                      f"\n{C[1]}exit => {C[2]}Exit the Script"
                      f"\n{C[0]}"
                      f"\n<=========================================================>\n"
                )
                continue
            elif str(INPUT) == "show-banner":
                HEADER = cfonts.render(text = "InstaInfo" , colors = [f"{random.choice(F)}" , f"{random.choice(F)}"] , align = "left")
                print(HEADER)
                continue
            elif str(INPUT) == "options/version":
                with io.open(file = "version.txt" , mode = "r") as V:
                    print(str(V.read(5)))
                    V.close()
                    continue
            elif str(INPUT) == "options/license":
                with io.open(file = "license.txt" , mode = "r") as L:
                    print(str(L.read(5055)))
                    L.close()
                    continue
            elif str(INPUT) == "exit" or str(INPUT) == "Exit" or str(INPUT) == "EXIT":
                last_input = str(input(f"{C[1]}[{C[3]}?{C[1]}] {C[0]}Do you want to save The Progress In log.txt ?"))
                if str(last_input) == "y" or str(last_input) == "Y" or str(last_input) == "yes" or str(last_input) == "Yes" or str(last_input) == "YES":
                    with io.open(file = r"{}".format("log/log.txt") , mode = "a" , encoding = "utf-8") as LOG:
                        LOG.write(f"Username : @{str(i.username)}\n")
                        LOG.write(f"Verified : {str(i.is_verified)}\n")
                        LOG.write(f"Private : {str(i.is_private)}\n")
                        LOG.write(f"Full name : {str(i.fullname)}\n")
                        LOG.write(f"Recently Joined Instagram : {str(i.is_joined_recently)}\n")
                        LOG.write(f"Follow Requested Other Pages : {str(i.has_requested_viewer)}\n")
                        LOG.write(f"Followers : {str(i.number_of_followers)}\n")
                        LOG.write(f"Followings : {str(i.number_of_followings)}\n")
                        LOG.write(f"Posts : {str(i.number_of_posts)}\n")
                        LOG.write(f"Website : {str(i.website)}\n")
                        LOG.write(f"Facebook Page : {str(i.connected_fb_page)}\n")
                        LOG.write(f"Country Blocked User : {str(i.has_country_block)}\n")
                        LOG.write(F"Blocked Any Instagram Users : {str(i.has_blocked_viewer)}\n")
                        LOG.write(f"Blocked By Other Users : {str(i.is_blocked_by_viewer)}\n")
                        LOG.write(f"Biography : {str(i.biography)}\n")
                        LOG.write(f"Profile Picture URL : {str(i.profile_picture_url)}")
                        LOG.write("\n\r\n\r")
                        LOG.close()
                        break
                elif str(last_input) == "n" or str(last_input) == "N" or str(last_input) == "no" or str(last_input) == "No" or str(last_input) == "NO":
                    break
            elif str(INPUT) == "update-script":
                try:
                    subprocess.call(["git" , "clone" , "https://github.com/shervin-glitch/InstaInfo"])
                    print("[+] The Script Directory is Cloned")
                except Exception as Err:
                    subprocess.call(["rm" , "-rf" , "InstaInfo"])
                    subprocess.call(["git" , "clone" , "https://github.com/shervin-glitch/InstaInfo"])
                    print("[+] The Script Directory is Cloned")
                    raise Err
                finally:
                    print("\n")
                continue
            elif str(INPUT) == "scripts/set-username":
                INPUT = str(input(f"\n\n{C[1]}[{C[3]}~{C[1]}] {C[1]}({C[5]}Inst4Inf0{C[1]})--$ \n{C[2]}[scripts/set-username] >{C[0]} "))
                i = instagramy.InstagramUser(INPUT)
                print(f"\n{C[1]}[{C[3]}Verified{C[1]}] {C[0]}: {C[2]}{str(i.is_verified)}")
                print(f"{C[1]}[{C[3]}Private{C[1]}] {C[0]}: {C[2]}{str(i.is_private)}")
                print(f"{C[1]}[{C[3]}Username{C[1]}] {C[0]}: {C[2]}@{str(INPUT)}")
                print(f"{C[1]}[{C[3]}Full name{C[1]}] {C[0]}: {C[2]}{str(i.fullname)}")
                print(f"{C[1]}[{C[3]}Recently Joined Instagram{C[1]}] {C[0]}: {C[2]}{str(i.is_joined_recently)}")
                print(f"{C[1]}[{C[3]}Follow Requested Other Pages{C[1]}] {C[0]}: {C[2]}{str(i.has_requested_viewer)}")
                print(f"{C[1]}[{C[3]}Followers{C[1]}] {C[0]}: {C[2]}{str(i.number_of_followers)}")
                print(f"{C[1]}[{C[3]}Followings{C[1]}] {C[0]}: {C[2]}{str(i.number_of_followings)}")
                print(f"{C[1]}[{C[3]}Posts{C[1]}] {C[0]}: {C[2]}{str(i.number_of_posts)}")
                print(f"{C[1]}[{C[3]}Website{C[1]}] {C[0]}: {C[2]}{str(i.website)}")
                print(f"{C[1]}[{C[3]}Facebook Page{C[1]}] {C[0]}: {C[2]}{str(i.connected_fb_page)}")
                print(f"{C[1]}[{C[3]}Country Blocked User{C[1]}] {C[0]}: {C[2]}{str(i.has_country_block)}")
                print(f"{C[1]}[{C[3]}Blocked Any Instagram Users{C[1]}] {C[0]}: {C[2]}{str(i.has_blocked_viewer)}")
                print(f"{C[1]}[{C[3]}Blocked By Other Users{C[1]}] {C[0]}: {C[2]}{str(i.is_blocked_by_viewer)}")
                print(f"{C[1]}[{C[3]}Biography{C[1]}] {C[0]}: {C[2]}{str(i.biography)}")
                print(f"{C[1]}[{C[3]}Profile Picture Url{C[1]}] {C[0]}: {C[2]}{str(i.profile_picture_url)}")
                continue
            else:
                print(f"{C[5]}[  !  ] Wrong Command")
                continue
    MainScript()
