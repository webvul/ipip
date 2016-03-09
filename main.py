# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os

from ipip import IP
#from ipip import IPX

str_ip = sys.argv[1] if len(sys.argv) > 1 else '113.206.51.191'
print 'find address of ip[%s]:' % str_ip

IP.load(os.path.abspath("17monipdb.dat"))
print IP.find(str_ip.encode('utf-8'))

#IPX.load(os.path.abspath("17monipdb.datx"))
#print IPX.find("118.28.8.8")
