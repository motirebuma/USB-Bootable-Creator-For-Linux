import os
from banner import banner
from colorama import Fore


banner.banner()

def boot():    
    try:
        os.system("sudo fdisk -l")
        path = input(Fore.BLUE + "\nEnter path of OS: ")
        device = input(Fore.BLUE +"Enter device name: [/dev/sdXX]: ")
        os.system("sudo dd if={} of={} bs=4M status=progress".format(path, device))

    except:
        print(Fore.RED + "\nSome thing went wrong!..")
        boot();


boot();