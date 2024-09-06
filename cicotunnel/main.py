import subprocess
import signal
import re
import sys
import requests
from colorama import Fore, Style, init

def main():
    init()

    if len(sys.argv) <= 1:
        print("Porta não informada.")
        sys.exit()

    port = sys.argv[1]
    server = "portuser@tunnel.cico.lol"  # Servidor padrão

    # Verifica se há um argumento para servidor remoto
    if len(sys.argv) > 2:
        if sys.argv[2] == '-r' and len(sys.argv) > 3:
            server = sys.argv[3]
        elif sys.argv[2] == '--remote' and len(sys.argv) > 3:
            server = sys.argv[3]
        else:
            print("Argumentos inválidos.")
            sys.exit()

    command = f"ssh -R 0:localhost:{port} -o ServerAliveInterval=60 -o ServerAliveCountMax=3 -o StrictHostKeyChecking=no {server}"
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    porta_alocada = None
    for line in iter(process.stdout.readline, b''):
        match = re.search(r"Allocated port (\d+) for remote forward to localhost:\d+", line.decode('utf-8'))
        if match:
            porta_alocada = int(match.group(1))
            break

    if porta_alocada:
        url = f"http://ip-api.com/json/{server.split('@')[-1]}"
        response = requests.get(url, verify=False)
        print(r"""
  ______            ______                   __
 / ___(_)______    /_  __/_ _____  ___  ___ / /
/ /__/ / __/ _ \    / / / // / _ \/ _ \/ -_) / 
\___/_/\__/\___/   /_/  \_,_/_//_/_//_/\__/_/  
                                               
""")
        link_text = "cicodevada"
        url = "https://github.com/cicodevada"

        print(Fore.CYAN + "CicoTunnel" + Style.RESET_ALL + " by " + Fore.CYAN + f"\033]8;;{url}\033\\{link_text}\033]8;;\033\\".ljust(30)+ Style.RESET_ALL)
        print("")
        print(Fore.GREEN + "Tunnel Status".ljust(30) + "Online" + Style.RESET_ALL)
        if response.status_code == 200:
            data = response.json()
            country = data.get('country')
            countryCode = data.get('countryCode')
            print("Region".ljust(30) + f"{country} ({countryCode})")
        else:
            print("Region".ljust(30) + "Failed to get info.")
        print("Forwarding".ljust(30) + f"http://localhost:{port} -> http://{server.split('@')[-1]}:{porta_alocada}")
        print("")
        print("")
        print("")
        print("(CTRL + C to quit)")
    else:
        print("Conexão não estabelecida.")
        process.terminate()

    process.wait()

    def handle_interrupt(sig, frame):
        process.terminate()

    signal.signal(signal.SIGINT, handle_interrupt)

if __name__ == "__main__":
    main()
