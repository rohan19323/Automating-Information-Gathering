import nmap
import sys
import time

nm_scan=nmap.PortScanner();
print("\nRunning")
nm_scanner=nm_scan.scan(sys.argv[1],'80',arguments='-O')

host="The host is: "+nm_scanner['scan'][sys.argv[1]]['status']['state']+".\n"
port="The port 80 is: "+nm_scanner['scan'][sys.argv[1]]['tcp'][80]['state']+".\n"
method="The method of scanning is: "+nm_scanner['scan'][sys.argv[1]]['tcp'][80]['reason']+".\n"
guess="There is %s percent chance that the target is running %s"%(nm_scanner['scan'][sys.argv[1]]['osmatch'][0]['accuracy'],nm_scanner['scan'][sys.argv[1]]['osmatch'][0]['name'])+".\n"
with open("%s.txt"%sys.argv[1],'w') as f:
	f.write(host+port+guess)

print("\nFinished")
