#!/usr/bin/python
#Developed by Caleb Watt and Ben Donnelly for USCC Western Regional 2013
#CYBER CYBER!!
import random
import os
import sys

bar = ['cyber', 'cloud', 'threat', 'analytics', 'infrastructure', 'software-as-a-service', 'virtualization', 'distributed', 'denial', 'critical', 'mission', 'mobile', 'platform', 'intensive', 'application', 'intelligence', 'architecture', 'data', 'gathering', 'information', 'system', 'end-user', 'support', 'cross', 'fault', 'security', 'BYOD', 'defense', 'license', 'multiplatform', 'integration', 'network', 'admin', 'reverse engineering', 'testing', 'product', 'global', 'password', 'management', 'research', 'development', 'root', 'software', 'hardware', 'kernel', 'exploit', 'proprietary', 'server', 'cyberbullying', 'VOiP', 'web-based', 'front-end', 'workflow', 'optimization', 'innovative', 'specialized', 'attack-vector', 'professional', 'leader', 'forensics', 'occupational', 'hashtag', 'social']

bzwd = len(bar) - 1

while(True):
	a = random.randint(0,bzwd)
	b = a
	while(b==a and b!=0):
		b = random.randint(0,bzwd)
	os.system("clear")
	print(bar[a] + " " + bar[b])
	print("Press enter for a new buzzword pair.")
	pyVersion = sys.version[0]
	if(int(pyVersion) < 3):
		xyz = raw_input()
	else:
		xyz = input()
