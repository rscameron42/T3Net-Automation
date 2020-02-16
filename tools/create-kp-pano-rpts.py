#!/usr/bin/env python3
from __future__ import unicode_literals, print_function

# Open file for processing and place contents into variable "f"
with open("dc-rule-group.csv") as f:
    policies = f.read()

# Iterate through lines in CSV, assign fields to variables
for line in policies.splitlines():
    (rule,dc,tags,grp) = line.split(',')
    # Print rule ID section header
    print('### Group-' + grp + ' - ' + dc + ' Data Center - Policy name: "' + rule + '"')
    print('### Top Sources report commands')
    print('set shared reports "Grp-' + grp + ' ' + dc + ' ' + rule + ' Top Sources" type trsum sortby bytes group-by from aggregate-by [ src to ] values [ bytes bytes_sent bytes_received ]')
    print('set shared reports "Grp-' + grp + ' ' + dc + ' ' + rule + ' Top Sources" topn 100 topm 10 caption "Top Sources"')
    print('set shared reports "Grp-' + grp + ' ' + dc + ' ' + rule + ' Top Sources" query "(device-group eq ' + dc + ') and (rule eq \'' + rule + '\')"')
    print('set shared reports "Grp-' + grp + ' ' + dc + ' ' + rule + ' Top Sources" start-time "2019/09/01 00:01:00" end-time "2020/05/31 11:59:59')
    print('### Top Destinations report commands')
    print('set shared reports "Grp-' + grp + ' ' + dc + ' ' + rule + ' Top Destinations" type trsum sortby bytes group-by to aggregate-by [ from dst ] values [ bytes bytes_sent bytes_received ]')
    print('set shared reports "Grp-' + grp + ' ' + dc + ' ' + rule + ' Top Destinations" topn 100 topm 10 caption "Top Destinations"')
    print('set shared reports "Grp-' + grp + ' ' + dc + ' ' + rule + ' Top Destinations" query "(device-group eq ' + dc + ') and (rule eq \'' + rule + '\')"')
    print('set shared reports "Grp-' + grp + ' ' + dc + ' ' + rule + ' Top Destinations" start-time "2019/09/01 00:01:00" end-time "2020/05/31 11:59:59')
    print('### Top Applications report commands')
    print('set shared reports "Grp-' + grp + ' ' + dc + ' ' + rule + ' Top Applications" type trsum sortby bytes group-by app aggregate-by [ from to ] values [ bytes bytes_sent bytes_received ]')
    print('set shared reports "Grp-' + grp + ' ' + dc + ' ' + rule + ' Top Applications" topn 100 topm 10 caption "Top Applications"')
    print('set shared reports "Grp-' + grp + ' ' + dc + ' ' + rule + ' Top Applications" query "(device-group eq ' + dc + ') and (rule eq \'' + rule + '\')"')
    print('set shared reports "Grp-' + grp + ' ' + dc + ' ' + rule + ' Top Applications" start-time "2019/09/01 00:01:00" end-time "2020/05/31 11:59:59"')
    print('### Top Ports report commands')
    print('set shared reports "Grp-' + grp + ' ' + dc + ' ' + rule + ' Top Ports" type trsum sortby bytes group-by dport aggregate-by [ from to ] values [ bytes bytes_sent bytes_received ]')
    print('set shared reports "Grp-' + grp + ' ' + dc + ' ' + rule + ' Top Ports" topn 100 topm 10 caption "Top Ports"')
    print('set shared reports "Grp-' + grp + ' ' + dc + ' ' + rule + ' Top Ports" query "(device-group eq ' + dc + ') and (rule eq \'' + rule + '\')"')
    print('set shared reports "Grp-' + grp + ' ' + dc + ' ' + rule + ' Top Ports" start-time "2019/09/01 00:01:00" end-time "2020/05/31 11:59:59"')
    print('### Top Flows report commands')
    print('set shared reports "Grp-' + grp + ' ' + dc + ' ' + rule + ' Top Flows" type trsum sortby bytes aggregate-by [ from src to dst app ] values [ bytes bytes_sent bytes_received ]')
    print('set shared reports "Grp-' + grp + ' ' + dc + ' ' + rule + ' Top Flows" topn 100 topm 10 caption "Top Flows"')
    print('set shared reports "Grp-' + grp + ' ' + dc + ' ' + rule + ' Top Flows" query "(device-group eq ' + dc + ') and (rule eq \'' + rule + '\')"')
    print('set shared reports "Grp-' + grp + ' ' + dc + ' ' + rule + ' Top Flows" start-time "2019/09/01 00:01:00" end-time "2020/05/31 11:59:59"')
    print()
