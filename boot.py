import os
from banner import banner
from colorama import Fore


banner.banner1()

def boot():    
    try:
        os.system("sudo fdisk -l")
        path = input(Fore.BLUE + "\n\nEnter path of OS: ")
        device = input(Fore.BLUE +"Enter device name: [/dev/sdXX]: ")
        os.system("clear")
        os.system("sudo dd if={} of={} bs=4M status=progress".format(path, device))
        banner.banner2()
    except:
        print(Fore.RED + "\nSome thing went wrong!..")
        boot();


boot();