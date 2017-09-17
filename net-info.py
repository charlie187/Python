#!/usr/bin/python
import os
import subprocess
import time
import fcntl, socket, struct
import mechanize as browser
os.system('clear')

print 'Welcome to network-info\n'
print 'Your Gateway is: '
os.system("sleep 2")
cmnd = """route -n | grep "UG" | awk '{print $2}'
"""
os.system(cmnd)
print '\n'
print'Your Local IP adress is: '
os.system("sleep 1")
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print(s.getsockname()[0])
s.close()
print '\n'
print 'Your Public IP adress is: '
url = "https://duckduckgo.com/?q=whats+my+ip&ia=answer";
br = browser.Browser();
br.set_handle_robots(False);
br.set_handle_refresh(browser._http.HTTPRefreshProcessor(), max_time=1);
visit = br.open(url);
html = visit.read();
if("Your IP address is" in html):
 #found
 html=html.split("Your IP address is")[1].strip();
 html=html.split("in")[0].strip();
 print "%s"%html;
else:
 pass
print '\n'
print 'Your Wireless MAC adress is: '
def getHwAddr(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    info = fcntl.ioctl(s.fileno(), 0x8927,  struct.pack('256s', ifname[:15]))
    return ':'.join(['%02x' % ord(char) for char in info[18:24]])
print getHwAddr('wlan0')
print '\n'
print 'Your Wired MAC adress is: '
def getHwAddr(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    info = fcntl.ioctl(s.fileno(), 0x8927,  struct.pack('256s', ifname[:15]))
    return ':'.join(['%02x' % ord(char) for char in info[18:24]])
print getHwAddr('eth0')
print '\n'
print 'Up and Download Speed: '
	   #je kunt met curl programmas op github gebruiken als je curl site.com/program.py | python - doet
os.system ("curl -s  https://raw.githubusercontent.com/sivel/speedtest-cli/master/speedtest.py | python -")
