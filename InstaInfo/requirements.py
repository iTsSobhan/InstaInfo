if __name__ == "__main__":
    import sys
    import subprocess

    def PackageManager(param = None , event = True):
        if param == None and event == True:
            try:
                import requests
            except:
                print(r"[-] requests Package is not Installed")
            try:
                import instagramy
            except:
                print(r"[-] instagramy package is not Installed")
            try:
                import colorama
            except:
                print(r"[-] colorama package is not Installed")
            try:
                import cfonts
            except:
                print(r"[-] cfonts package is not Installed")
            try:
                import socket
            except:
                print(r"[-] socket package is not Installed")

    PackageManager()

    def Installer(param = None , event = True):
        if param == None and event == True:
            while True:
                INPUT = str(input("[?] Do you want To Download and install Requirements ? (y/n) : "))
                if str(INPUT) == "y" or str(INPUT) == "Y" or str(INPUT) == "yes" or str(INPUT) == "Yes":
                    subprocess.call(["python3" , "-m" , "pip" , "install" , "--upgrade" , "pip"])
                    subprocess.call(["pip3" , "install" , "requests"]) and subprocess.call(["pip" , "install" , "requests"])
                    subprocess.call(["pip3" , "install" , "sockets"]) and subprocess.call(["pip" , "install" , "sockets"])
                    subprocess.call(["pip3" , "install" , "colorama"]) and subprocess.call(["pip" , "install" , "colorama"])
                    subprocess.call(["pip3" , "install" , "instagramy"]) and subprocess.call(["pip" , "install" , "instagramy"])
                    subprocess.call(["pip3" , "install" , "python-cfonts"]) and subprocess.call(["pip" , "install" , "python-cfonts"])
                    print(r"[+] Packages Successfully Installed")
                    break
                elif str(INPUT) == "n" or str(INPUT) == "N" or str(INPUT) == "no" or str(INPUT) == "No":
                    break
    Installer()
