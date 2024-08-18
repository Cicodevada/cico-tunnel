import subprocess
import signal
import re
import sys
from colorama import Fore, Style, init
init()
#Pegar Porta nos argumentos do comando
if len(sys.argv) <= 1:
    print("Porta não informada.")
    sys.exit()
else:
    port = sys.argv[1]

command = f"ssh -R 0:localhost:{port} -o ServerAliveInterval=60 -o ServerAliveCountMax=3 portuser@tunnel.cico.lol"
process = subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

#Caçar porta alocada pelo ssh auto
porta_alocada = None
for line in iter(process.stdout.readline, b''):
    match = re.search(r"Allocated port (\d+) for remote forward to localhost:80", line.decode('utf-8'))
    if match:
        porta_alocada = int(match.group(1))
        break

if porta_alocada:
    print(r"""

  ______            ______                   __
 / ___(_)______    /_  __/_ _____  ___  ___ / /
/ /__/ / __/ _ \    / / / // / _ \/ _ \/ -_) / 
\___/_/\__/\___/   /_/  \_,_/_//_/_//_/\__/_/  
                                               
""")
    link_text = "hugosantoslisboa"
    url = "https://github.com/hugosantoslisboa"

    print(Fore.CYAN + "CicoTunnel" + Style.RESET_ALL + " by " + Fore.CYAN + f"\033]8;;{url}\033\\{link_text}\033]8;;\033\\".ljust(30)+ Style.RESET_ALL)
    print("(CTRL + C to quit)")
    print("")
    print(Fore.GREEN + "Tunnel Status".ljust(30) + "Online" + Style.RESET_ALL)
    print("Region".ljust(30) + "Brasil (BR)")
    print("Forwarding".ljust(30) + f"http://localhost:{port} -> http://tunnel.cico.lol:{porta_alocada}")
else:
    print("Porta não encontrada.")
    process.terminate()
process.wait()
#Finalizar com CTRL+C
def handle_interrupt(sig, frame):
    process.terminate() 

signal.signal(signal.SIGINT, handle_interrupt)