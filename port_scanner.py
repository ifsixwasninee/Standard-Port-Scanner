# To be able to interact with the network & and call forth date/time timestaps in the scan.
import socket
from datetime import datetime

# Used to get target from user with validation
while True:
    target = input("Enter target IP or hostname: ").strip()
    if target:
        if target.lower() in ["localhost", "127.0.0.1"]:
            print("[!] Scanning localhost - ensure you have proper authorization")
            break
        elif target.count('.') == 3 and all(0 <= int(part) < 256 for part in target.split('.') if part.isdigit()):
            break
        else:
            print("[!] Invalid IP format. Use format: 192.168.1.1")
    else:
        print("[!] Target cannot be empty")

# Choose any "Target", and scan all open ports interacting with the IP between the range of 1-1024.
start_port = 1
end_port = 1024

# Confirms if you'd like to prceed with this network scan.
if input("\nConfirm scan (y/n)? ").lower() != 'y':
    print("[!] Scan cancelled by user")
    exit()

# Print data info2rmiung user When & Where the scan was initiated.
print("[SECURITY NOTICE] This tool is for AUTHORIZED NETWORK TESTING ONLY")
print(f"[+] Scanning {target} from port {start_port} to {end_port}")
print(f"[+] Started at: {datetime.now()}\n")
print("[*] Using 0.5s timeout to prevent network congestion\n")

# Before scanning the program translates the "target name" into an IP address, and if it fails the program will cease proicess.
try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("[-] Host could not be resolved.")
    exit()

# Loop through each port whilst also checking if it is open.
try:
    for port in range (start_port, end_port + 1):

# Opens a connection socket withh a halfsecond timeout.
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)

# Attempts to make a connection and if succesful, there is a wide open port for hackers and vulnerabilities.
        result = s.connect_ex((target_ip, port))
        if result == 0:
            try:
                 service = socket.getservbyport(port)
            except:
                 service ="Unknown"
            print(f" [OPEN] PORT {port} ({service})")

# Quickly closes ports therefore there are no hanging connections.
    s.close()

# If "Control C" is clicked the program will quick clean. Any other error, logged and the program continues.
except KeyboardInterrupt:
    print("\n[!] Scan aborted by User")
except Exception as e:
    print(f"[-] Error on port {port}: {e}")

# Final print out of a list of all open ports on the Network in question.
print(f"\n[+] Scan Complete at: {datetime.now()}")