import subprocess
import shlex
import re
import ipaddress


def valid_ip(address):
    try:
        ipaddress.ip_address(address)
        return True
    except:
        return False


def assign_static_ip(ip_address, subnetmask, gateway):
    if valid_ip(ip_address) is False:
        print("Unacceptable ip address")
        return None
    if valid_ip(subnetmask) is False:
        print("Unacceptable subnetmask")
        return None
    if valid_ip(gateway) is False:
        print("Unacceptable gateway")
        return None
    subprocess.call(shlex.split("sudo ifconfig eth0 down"))
    subprocess.call(shlex.split("sudo ifconfig eth0 {ip} netmask {sub} broadcast {gate}"
                                .format(ip=ip_address, sub=subnetmask, gate=gateway)))
    subprocess.call(shlex.split("sudo ifconfig eth0 up"))
