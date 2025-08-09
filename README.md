Usage:

python3 port_scanner.py
" -----------------------------------------------------------------------
Sample Output:

Enter target IP or hostname: 192.168.0.1
Confirm scan (y/n)? y

[SECURITY NOTICE] This tool is for AUTHORIZED NETWORK TESTING ONLY
[+] Scanning 192.168.0.1 from port 1 to 1024
[+] Started at: 2025-08-02 08:46:53
[*] Using 0.5s timeout to prevent network congestion

 [OPEN] PORT 80 (http)
 [OPEN] PORT 443 (https)

[+] Scan Complete at: 2025-08-02 08:55:30
" -----------------------------------------------------------------------
Program Graph:

graph TD
    A[Start Scan] --> B{Authorization Check}
    B -->|Confirmed| C[Port Scanning]
    B -->|Denied| D[Abort]
    C --> E[Results]
    E --> F[Security Notice]

" -----------------------------------------------------------------------
Legal Disclaimer:

    "This tool is provided for educational and authorized security testing purposes only. The developers assume no liability for misuse. Unauthorized port scanning violates computer misuse laws in most jurisdictions and may result in severe legal penalties."