import os
import sys
import socks
import socket
import requests
import platform

# Display banner
os.system("figlet QUANTUM-TOOL")
print ("A multi-purpose toolkit for beginner ethical hacker")

# Help menu 
if len(sys.argv) < 2 or sys.argv[1] == "-help":
	print( 
        '''
======================================= 
|           Reconnaissance            | 
======================================= 
-iplookup,      [-iplookup]                         simple ip info lookup
-portscan,      [-portscan target]                  simple nmap portscan
-nall,          [-nall target]                      nmap OS detection, version detection, script scanning, and traceroute scan
-dnsbr,         [-dnsbr target]                     nmap dns bruteforce
-vulnscan,      [-vulnscan]                         nmap vuln scanner
-dosscan,       [-dosscan]                          nmap dos scanner
-wti,           [-wti target]                       get a hosts ip address
-discover,      [-discover]                         scan for devices on your network
-online,        [-online target]                    check if a host is online (\033[33minclude http:// or https://\033[0m)
-whois,         [-whois target]                     who-is lookup
-dnsup,         [-dnsup target]                     dns-lookup
-ssls,          [-ssls target]                      run a ssl scan
-geoip,         [-geoip target]                     find the location of a ip address
-revip,         [-revip target]                     reverse ip lookup a target
-hostsr,        [-hostsr target]                    host search
-revdns,        [-revdns target]                    reverse dns 
-ddns,          [-ddns target]                      find shared dns
-sysinfo,       [-sysinfo]                          get detailed system information 

======================================= 
|           Web Attack                | 
======================================= 
-lfi            [-lfi]                                  check for lfi vuln within url 
-adminfind      [-adminfind]                            bruteforce to find open admin panel in a website
-urlcrazy       [-urlcrazy domain]                      Generate and test domain typos and variations
-ftpbr          [-ftpbr host userfile passfile]         Brute force against FTP servers
-waf,           [-waf target]                           web application firewall scanner
-dirb,          [-dirb target]                          run a directory bruteforce on a host (\033[33minclude http:// or https://\033[0m)
-pwnxss         [-pwnxss target]                        run a XSS check on url (include http or https)

======================================= 
|           Internal Attack           | 
======================================= 
-sniff          [-sniff interface]                      turn on interface for sniffing and save to pcap file
-revshell       [-revshell]                             start a listening reverse shell, if you want to deploy then copy client.py to your client machines

======================================= 
|          Social Engineering         | 
======================================= 
-cuteit         [-cuteit ip]                            IP obfuscator made to make a malicious ip a bit cuter
-trape          [-trape]                                People tracker on the Internet: Learn to track the world, to avoid being traced

======================================= 
|             Crypto                  | 
======================================= 
-passgen,       [-passgen]                              Simple password generator
-text2hash,     [-text2hash text hashtype]              convert certain text to different hash types 
-rot13,         [-rot13 encrypt/decrypt]                ROT13 encrypts and decrypts

======================================= 
|             Privacy                 | 
======================================= 
-wimip,         [-wimip]                                check your public ip address
-tor,           [-tor]                                  install and start tor service
-macchanger,    [-macchanger device]                    randomize your mac address
-faker,         [-faker]                                automatically generate fake identities for you

======================================= 
|             Stress test             | 
======================================= 
-hammer         [-hammer host port turbo]               hammer dos script

======================================= 
|             Hardening               | 
======================================= 
-harden,        [-harden]                               get hardening report provided by lynis
-upgrade,       [-upgrade]                              update and upgrade kali host

======================================= 
|             Windows                 | 
======================================= 
-wifidump       [-wifidump]                             open source tool to dump the wifi profiles and cleartext passwords of the connected access points on the Windows machine.

======================================= 
|            Clearing Tracks          | 
=======================================  
-clearwin       [-clearwin]                             Clearing log on Windows, Windows Server
-clearlinux     [-clearlinux]                           Clearing log on Linux, need PHP installed
        '''
    )
# exit if not pass any agruments
if len(sys.argv) < 2:
    sys.exit()

# Recon
if sys.argv[1] == "-iplookup":
    os.system("python3 modules/iplookup.py")

if sys.argv[1] == "-portscan":
    os.system("nmap {0}".format(sys.argv[2]))

if sys.argv[1] == "-nall":
    os.system("nmap -A {0}".format(sys.argv[2]))

if sys.argv[1] == "-dnsbr":
    os.system("nmap --script dns-brute {0}".format(sys.argv[2]))

if sys.argv[1] == "-vulnscan": 
    os.system("nmap -v --script vuln {0}".format(sys.argv[2]))

if sys.argv[1] == "-dosscan": 
    os.system("nmap -v --script dos {0}".format(sys.argv[2]))

if sys.argv[1] == "-wti":
    ip = socket.gethostbyname(sys.argv[2])
    print("Host: ", sys.argv[2])
    print("IP:   ", ip)

if sys.argv[1] == "-discover":
    os.system("netdiscover")
if sys.argv[1] == "-online":
	request = requests.get(sys.argv[2])
	http = request.status_code
	if http == 200:
		print("Server: [\033[32monline\033[0m]")
	else:
		print("Server: [\033[31moffline\033[0m]")

if sys.argv[1] == "-whois":
    whois = requests.get("https://api.hackertarget.com/whois/?q=" + sys.argv[2]).content.decode("UTF-8")
    print(whois)

if sys.argv[1] == "-dnsup":
    os.system("curl https://api.hackertarget.com/dnslookup/?q={0}".format(sys.argv[2]))

if sys.argv[1] == "-ssls":
    os.system("sslscan {0}".format(sys.argv[2]))

if sys.argv[1] == "-geoip":
	os.system("curl https://api.hackertarget.com/geoip/?q={0}".format(sys.argv[2]))

if sys.argv[1] == "-revip":
	os.system("curl https://api.hackertarget.com/reverseiplookup/?q={0}".format(sys.argv[2]))

if sys.argv[1] == "-hostsr":
	os.system("curl https://api.hackertarget.com/hostsearch/?q={0}".format(sys.argv[2]))

if sys.argv[1] == "-revdns":
	os.system("curl https://api.hackertarget.com/reversedns/?q={0}".format(sys.argv[2]))

if sys.argv[1] == "-ddns":
	os.system("curl https://api.hackertarget.com/findshareddns/?q={0}".format(sys.argv[2]))

if sys.argv[1] == "-sysinfo": 
    os.system("python modules/sysinfo.py")

# web Attack 
if sys.argv[1] == "-lfi": 
    os.system("python3 modules/LFIChecker.py")

if sys.argv[1] == "-adminfind": 
    os.system("python3 modules/admin_finder/admin_finder.py")

if sys.argv[1] == "-urlcrazy": 
    os.system("urlcrazy {}".format(sys.argv[2]))

if sys.argv[1] == "-ftpbru": 
    os.system("python3 modules/ftpbrute.py {} {} {}".format(sys.argv[2], sys.argv[3], sys.argv[4]))

if sys.argv[1] == "-waf":
    os.system("wafw00f {0}".format(sys.argv[2]))

if sys.argv[1] == "-dirb":
    os.system("dirb {0}".format(sys.argv[2]))

if sys.argv[1] == "-pwnxss": 
    os.system("python3 modules/PwnXSS/pwnxss.py -u {}".format(sys.argv[2]))

# Internal
if sys.argv[1] == "-sniff": 
    os.system("python3 modules/sniff.py --iface {}".format(sys.argv[2]))

if sys.argv[1] == "-revshell":
    os.system("python3 modules/reverse_shell/server.py")

# Social Engineering
if sys.argv[1] == "-cuteit": 
    os.system("python modules/Cuteit/Cuteit.py {}".format(sys.argv[2]))

if sys.argv[1] == "-trape": 
    os.system("python2 modules/trape/trape.py")

# Crypto
if sys.argv[1] == "-passgen": 
    os.system("python3 modules/password_generator.py")
if sys.argv[1] == "-text2hash": 
    os.system("python modules/text2hash.py -t {} -T {}".format(sys.argv[2], sys.argv[3]))
if sys.argv[1] == "-rot13": 
    os.system("python3 modules/rot13.py {}".format(sys.argv[2]))

# Be Anonymous
if sys.argv[1] == "-wimip":
    public_ip = requests.get('http://ip.42.pl/raw').text
    print("Your public IP address is: " + public_ip)
    print("------------------------------------------")
    print("Your IP Information: ")
    print("------------------------------------------")
    whois = requests.get("https://api.hackertarget.com/whois/?q=" + public_ip).content.decode("UTF-8")
    print(whois)

if sys.argv[1] == "-tor": 
    os.system("python3 modules/tor.py")
    session = requests.session()
    session.proxies = {}
    session.proxies['http'] = 'socks5h://localhost:9050'
    session.proxies['https'] = 'socks5h://localhost:9050'
    r = session.get("http://httpbin.org/ip")
    print("Your New TOR Public IP Address: " + r.text)
    print("Please config your browser to connect with Tor network through SOCK5 localhost:9050")

if sys.argv[1] == "-macchanger":
    os.system("macchanger -r {0}".format(sys.argv[2]))

if sys.argv[1] == "-faker": 
    print("\n")
    print("Your new identity to fool someone: ")
    print("-----------------------------------")
    os.system("python3 modules/fakeidentity.py")
    print("-----------------------------------")

# Stress testing
if sys.argv[1] == "-hammer": 
    os.system("python3 modules/pyhammer.py -s {} -p {} -t {}".format(sys.argv[2], sys.argv[3], sys.argv[4]))

# Hardening 
if sys.argv[1] == "-harden": 
    os.system("sudo lynis audit system")
if sys.argv[1] == "-upgrade": 
    os.system("sudo apt update -y && sudo apt upgrade -y")
    os.system("sudo apt autoremove")

# Windows
if sys.argv[1] == "-wifidump":
    os.system("python modules/Windows/Wifi-Dumper/wifi_dumper.py")

# Clearing Tracks
if sys.argv[1] == "-clearwin":
    os.system("modules/Log-killer/logkiller.bat")
if sys.argv[1] == "-clearlinux": 
    os.system("php modules/Log-killer/cleartracks.php")