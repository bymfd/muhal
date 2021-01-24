import requests
import zipfile
import os
import time, threading  # requeried run periodic
from swinlnk.swinlnk import SWinLnk  # requeried create startup application

# url for check version
kontrolurl = "https://raw.githubusercontent.com/bymfd/csautoupdate/main/ver"
# file to download url
dosyaurl = "https://github.com/bymfd/csautoupdate/blob/main/dosyalar.zip?raw=true"
# working directory
folder_path = os.path.dirname(os.path.realpath(__file__))

# try to make startup program static.exe file
# work only with admin right but not controlled
# first time execute admin rights
if os.path.exists("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp"):
    try:
        swl = SWinLnk()
        swl.create_lnk(folder_path + "\muhal.exe",
                       'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp\muhal.lnk')
    except:
        print("try to run admin")


# delete downloaded zip file
def temizlik():
    try:
        print("temizlik")
        os.remove("dosyalar.zip")
        return True
    except:

        print("silemedim abi")
        return False


def indir():
    # download dosyalar.zip
    try:
        r = requests.get(dosyaurl, allow_redirects=True)
        open('dosyalar.zip', 'wb').write(r.content)

        # extract zip
        with zipfile.ZipFile("dosyalar.zip", "r") as zip_ref:
            zip_ref.extractall()
            return True
    except:
        print("download or write dont work ")


# find net version
def netversionbul():
    try:
        r = requests.get(kontrolurl)
        netversion = r.text.strip()
        return netversion
    except:
        print("Connection failed")


# find local version number
def localversionbul():
    try:
        f = open("ver", "r")
        localversion = f.read().strip()
        return localversion
    except:
        print("read version fail")


#  change local file version with netversion
def localversiondegistir():
    temizlik()
    global netverison
    try:
        print(netversionbul())
        f = open("ver", "w")
        f.write(str(netversionbul()))
        f.close()
    except:
        print("Write error")


# compare local version and net version
def versionkarsilastir():
    if localversionbul() != netversionbul():
        # versions not same
        if indir():
            # downloaded file succesfully
            localversiondegistir()
    else:
        print("up to date")
    # work perioodic
    threading.Timer(10, versionkarsilastir).start()


# start every call
versionkarsilastir()
