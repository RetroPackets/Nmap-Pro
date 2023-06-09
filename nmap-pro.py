import socket
import threading
import os

cyan = "\033[1;36;40m"
green = "\033[1;32;40m"
red = "\033[1;31;40m"
Y = '\033[1;33;40m'


print(cyan +"""
   ▒█▄░▒█ █▀▄▀█ █▀▀█ █▀▀█ ░░ ▒█▀▀█ █▀▀█ █▀▀█ 
   ▒█▒█▒█ █░▀░█ █▄▄█ █░░█ ▀▀ ▒█▄▄█ █▄▄▀ █░░█ 
   ▒█░░▀█ ▀░░░▀ ▀░░▀ █▀▀▀ ░░ ▒█░░░ ▀░▀▀ ▀▀▀▀
------------------------------------------------
| CREATED BY : RetroPackets                    |
|     GITHUB : https://github.com/RetroPackets |
|  INSTAGRAM : @retropacketz                   |
------------------------------------------------""")
print ("")
print(
    f"{red}WARNING: This scan can take a while depending on your network speed"
)
print(f"{red}so have a cup of coffee and relax until finished 😎")
print(f"{cyan}")


target = input("""Target: """)  # scan local host
print("")
def port_scanner(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        print(f"""{green}[*] Port {port} is open""")
    except:
        pass


for port in range(1,10000):
    thread = threading.Thread(target =port_scanner, args=[port])
    thread.start()


print ("")
print(f"{Y}[*] Confirming Results For {target}", "With Nmap...")
print(f"{green}")
os.system(f"sudo nmap --top-ports 50 {target}")

print ("")
print(f"{Y}[*] Scanning Using TCP Protocols For: {target}")
print(f"{green}")
os.system(f"sudo nmap -sT {target}")



print ("")
print(f"{Y}[*] Scanning Using UDP Protocols For: {target}")
print(f"{green}")
os.system(f"sudo nmap -sU {target}")

print ("")
print(f"{Y}[*] Performing OS/Service Detection On: {target}")
print(f"{green}")
os.system(f"sudo nmap -A -T4 {target}")

print ("")
print(f"{Y}[*] Detecting Service/Daemon Versions For: {target}")
print(f"{green}")
os.system(f"sudo nmap -sV {target}")

print ("")
print(f"{Y}[*] Performing CVE Detection For: {target}")
print(f"{green}")
os.system(f"sudo nmap -Pn --script vuln {target}")

print ("")
print(f"{Y}[*] Detecting Malware Infections On Remote Hosts For: {target}")
print(f"{green}")
os.system(f"sudo nmap -sV --script=http-malware-host {target}")

print ("")
#print (Y +"")
#question = input("Would you like to run a dos attack on the target [y/n]: ")
#if question == ("y"):
#    print (green +"")
#    os.system("cd src/hammer && python torshammer.py -p 80 -r 5000 -t " + target)
#elif answer == ("n"):
#    print("Moving On...")



