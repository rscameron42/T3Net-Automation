#!/usr/bin/env python3
from __future__ import unicode_literals, print_function
from ipaddress import *

# Open file for processing and place contents into variable "f"
with open("ip-ranges.txt") as f:
    ip_ranges_output = f.read()

# to calculate the total IPs in the all the elements processes, initialize
# the variable "total_ip" at zero.
total_ip = (0)
for line in ip_ranges_output.splitlines():
    if 'ip-range' in line:
        address_object = line.split()[4]
        ip_range = line.split()[6]
        ip_start = ip_range.split("-")[0]
        ip_end = ip_range.split("-")[1]
        ip_start_int = (int(IPv4Address(ip_start)))
        ip_end_int = (int(IPv4Address(ip_end)))
        print("{addr_obj:>35} ---> {qty:<9}".format(addr_obj=str(address_object), qty=str((ip_end_int + 1) - ip_start_int)))
    total_ip = total_ip + (((ip_end_int + 1) - ip_start_int))
print(('-' *50) + '\n' + (' ' *30) + 'Total ---> ' + str(total_ip))
