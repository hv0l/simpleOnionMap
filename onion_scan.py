import sys
import subprocess
from stem.control import Controller
from getpass import getpass

def scan_onion(onion_address, scan_type):
    with Controller.from_port(port=9051) as controller:
        controller.authenticate()
        socks_port = controller.get_conf('SocksPort')

        if scan_type == '1':
            nmap_cmd = f'proxychains nmap -sS -PN -n -v {onion_address} -oX {onion_address}.xml'
        elif scan_type == '2':
            nmap_cmd = f'proxychains nmap -sT -PN -n -v {onion_address} -oX {onion_address}.xml'
        elif scan_type == '3':
            nmap_cmd = f'proxychains nmap -sT -A -PN -n -v {onion_address} -oX {onion_address}.xml'
        else:
            print('\033[91mInvalid scan type selected.\033[0m')
            sys.exit(1)

        process = subprocess.Popen(nmap_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

        open_ports_output = []

        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                if "open" in output:
                    open_ports_output.append(output.strip())
                sys.stdout.write("\r\033[93m" + output.strip() + "\033[0m")
                sys.stdout.flush()

        process.wait()

        print("\n\n\033[92mOpen ports:\033[0m")
        for port_output in open_ports_output:
            print(port_output)

if __name__ == '__main__':
    onion_address = input('\033[94mEnter the Onion URL: \033[0m').strip()

    print("\033[96mSelect a scan type:\033[0m")
    print("1. Stealth Scan (-sS)")
    print("2. Quick Scan (no options)")
    print("3. Comprehensive Scan (-A)")

    scan_type = input('\033[94mEnter the number for your scan choice: \033[0m').strip()
    scan_onion(onion_address, scan_type)
