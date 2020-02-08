#!/usr/bin/env python3
from ipaddress import *


ip_range = '10.204.0.0-10.204.63.255'
ip_start = ip_range.split("-")[0]
ip_end = ip_range.split("-")[1]
ip_start_int = (int(IPv4Address(ip_start)))
ip_end_int = (int(IPv4Address(ip_end)))

print('\nThe dotted decimal IP range is from ' + ip_start + ' to ' + ip_end + '.')
print('The integer IP range is from ' + str(ip_start_int) + ' to ' + str(ip_end_int) + '.')
print('There are ' + str((ip_end_int + 1) - ip_start_int) + ' IP addresses in this range.\n')
