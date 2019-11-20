import sys
import os

print ("Installing Tor")
os.system("sudo apt-get install tor")
print ("Starting Tor service")
os.system("sudo service tor start")
print ("Checking status....")
os.system("curl --socks5 localhost:9050 --socks5-hostname localhost:9050 -s https://check.torproject.org/ | cat | grep -m 1 Congratulations | xargs")