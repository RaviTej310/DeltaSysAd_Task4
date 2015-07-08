#!/usr/bin/python

import re

file_name = "access.txt"

ip_codes = {}
status_code = {}
print "\nIP addresses - number of occurrences: \n"

regex = re.compile('(?:::1|[\d]{2,3}\.[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}[\s]\-)')
file1 = open("access.txt", "r")

for line in file1:
    ip_counts = regex.findall(line)
    for ip in ip_counts:
        try:
            ip_codes[ip.split('\n')[0]] += 1
        except Exception:
             ip_codes[ip.split('\n')[0]] = 1 
for ip_code in ip_codes:       
    print "%s %s" % (ip_code, ip_codes[ip_code])
print "\n"

print "Status codes - number of occurences:\n"

regex = re.compile('[\d]{3}[\s][\d]{3,5}')
file1 = open("access.txt", "r")

for line in file1:
    status_codes = regex.findall(line)
    for status in status_codes:
        try:
            status_code[status.split('\n')[0]] += 1
        except Exception:
             status_code[status.split('\n')[0]] = 1 
for code in status_code:       
    print "%s - %s" % (code, status_code[code])
print "\n"