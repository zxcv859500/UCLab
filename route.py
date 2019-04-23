import subprocess
import shlex


def assign_static_ip(ip_address):
    subprocess.call(shlex.split("sudo ifconfig eth0 down"))
    subprocess.call(shlex.split("sudo ifconfig eth0 " + ip_address))
    subprocess.call(shlex.split("sudo ifconfig eth0 up"))
