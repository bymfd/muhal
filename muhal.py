import requests
import zipfile
import os
import time ,threading
from swinlnk.swinlnk import SWinLnk
dir_path = os.path.dirname(os.path.realpath(__file__))
folder_path = (dir_path)
kontrolurl = "https://raw.githubusercontent.com/bymfd/csautoupdate/main/ver"
dosyaurl = "https://github.com/bymfd/csautoupdate/blob/main/dosyalar.zip?raw=true"

if os.path.exists("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp"):
    print("ass")
    try:
        swl = SWinLnk()
        swl.create_lnk(dir_path+"\muhal.exe", 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp\muhal.lnk')
    except:
        print("asss")
def temizlik():
    try:
        print("temizlik")
        os.remove("dosyalar.zip")
        return True
    except:
        return False
        print("silemedim abi")


def indir():
    # dosyalar.zipi inidr
    try:
        r = requests.get(dosyaurl, allow_redirects=True)
        open('dosyalar.zip', 'wb').write(r.content)

        # dosyaları olduğu klasöre çıkart
        with zipfile.ZipFile("dosyalar.zip", "r") as zip_ref:
            zip_ref.extractall()
            return True
    except:
        print("olmaadı be indiremedim ya da yazamadım ")




def netversionbul():

    try:
        r = requests.get(kontrolurl)
        netversion = r.text.strip()
        return netversion
    except:
        print("bağlanamadı")


def localversionbul():
    try:
        f = open("ver", "r")
        localversion = f.read().strip()
        return localversion
    except:
        print("okunamadı")


def localversiondegistir():
    temizlik()
    global netverison
    try:
        print(netversionbul())
        f = open("ver", "w")
        f.write(str(netversionbul()))
        f.close()
    except :
        print("www")


def versionkarsilastir():
    if localversionbul() != netversionbul():
        if indir():
            localversiondegistir()
    else:
        print("herşey güncel görünüyor")

    threading.Timer(10, versionkarsilastir).start()

versionkarsilastir()






