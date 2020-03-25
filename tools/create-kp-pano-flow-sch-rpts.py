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
    print('### Top Flows report commands')
    print('set shared reports "Grp-' + grp + ' ' + dc + ' ' + rule + ' Top Flows-scheduled" type trsum sortby bytes aggregate-by [ from src to dst app ] values [ bytes bytes_sent bytes_received ]')
    print('set shared reports "Grp-' + grp + ' ' + dc + ' ' + rule + ' Top Flows-scheduled" topn 100 topm 10 caption "Grp-' + grp + ' ' + dc + ' ' + rule + ' Top Flows - Scheduled"')
    print('set shared reports "Grp-' + grp + ' ' + dc + ' ' + rule + ' Top Flows-scheduled" query "(device-group eq ' + dc + ') and (rule eq \'' + rule + '\')"')
    print('set shared reports "Grp-' + grp + ' ' + dc + ' ' + rule + ' Top Flows-scheduled" period last-calendar-day frequency daily')
    print()
