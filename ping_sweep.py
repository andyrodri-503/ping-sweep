#!/usr/bin/env python3

import subprocess
import ipaddress

def ping_once(ip):
    result = subprocess.run(
        ["ping", "-c", "1", str(ip)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    return result.returncode == 0

def sweep(network):
    net = ipaddress.ip_network(network, strict=False)

    for ip in net.hosts():
        up = ping_once(ip)
        print(ip, "UP" if up else "DOWN")

sweep("192.168.1.0/24")
