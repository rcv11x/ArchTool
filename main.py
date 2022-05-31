from utils.colors import *
from utils.utils import Utils
import sys, time, distro
import os

utils = Utils()

def main():
    os.system("clear")
    print(f"""
        ╔═══════════════════════════════════════════════════════════════
        ║  
        ║    ░█▀▀█ █▀▀█ █▀▀ █░░█ ▒█▀▀█ █▀▀ █▀▀▄ ▀▀█▀▀ █▀▀ █▀▀ ▀▀█▀▀ 
        ║    ▒█▄▄█ █▄▄▀ █░░ █▀▀█ ▒█▄▄█ █▀▀ █░░█ ░░█░░ █▀▀ ▀▀█ ░░█░░ 
        ║    ▒█░▒█ ▀░▀▀ ▀▀▀ ▀░░▀ ▒█░░░ ▀▀▀ ▀░░▀ ░░▀░░ ▀▀▀ ▀▀▀ ░░▀░░
        ║   
        ║          Author: rec0veryyy / github.com/rec0veryyy     
        ║   
        ║   {cred}[1] {cpurple}Install BlackArch repo{cdefault}
        ║   {cred}[2] {cpurple}Install Hacking Tools (ex: gobuster crackmapexec){cdefault}
        ║   {cred}[0] {cdefault}Exit
        ║
        ╚═══════════════════════════════════════════════════════════════
        """)

    option = int(input(f"{utils.promp_style}"))

    if option == 1:
        InstallBlackArch()
    elif option == 2:
        InstallHackingTools()
    elif option == 0:
        exit
    else:
        print("[!] Elije una opcion valida")
        input();
        os.system("clear")
        main()
        

def InstallBlackArch():
    os.system("clear")
    print(f"-* {cblue}A continucacion se instalara el repo de arch{cdefault} *-\n")

    try:

        opt = input(f"{cred}[!] {cdefault}Proceder con la instalacion? [Y/n] ")

        if opt == "Y" or opt == "y":
            print(f"{cred}[!] {cgreen}Instalando Repo de BlackArch...{cdefault}")
            time.sleep(2)
            os.system("mkdir -p ~/repos; cd ~/repos")
            os.system("git clone https://aur.archlinux.org/paru-bin.git; cd ~/repos/paru-bin")
            os.system("makepkg -si")
            print("[!] ")

            os.system("mkdir -p ~/repos/; cd ~/repos/; git clone https://aur.archlinux.org/paru-bin.git; cd ~/repos/paru-bin/; makepkg -si; mkdir ~/repos/blackarch; cd ~/repos/blackarch/; curl -O https://blackarch.org/strap.sh; chmod +x strap.sh; sudo ./strap.sh");
        elif opt == "N" or opt == "n":
            main()
        else:
            print("\n~ Elije una opcion valida [Press Any key]")
            input();os.system("clear")
            InstallBlackArch()
    except:
        pass

def InstallHackingTools():
    print("[!] Instalacion de Herramientas\n\n")

    select_tool = str(input(">> "))

    os.system(f"sudo pacman -S {select_tool}")

    print(f"[!] Herramintas {select_tool} han sido descargadas/actualizadas") 
    #ex = os.system("sudo pacman -Sgg | grep blackarch | awk '{print $2}' > tools.txt")


if __name__ == '__main__':
    try:
        if distro.name() != "Ubuntu": # Change to Arch Linux
            sys.exit(1)
        else:
            main()
    except KeyboardInterrupt:
        print(f"\n\n{cred}[!]{cdefault}Saliendo")
        sys.exit(1)
