#!/usr/bin/python
#Developed by Caleb Watt and Ben Donnelly for USCC Western Regional 2013
#CYBER THREAT-HUNT!!
import random
import os
import sys

buzzwords = ['cyber', 'cloud', 'threat', 'analytics', 'infrastructure', 'software-as-a-service', 'virtualization', 'distributed', 'denial', 'critical', 'mission', 'mobile', 'platform', 'intensive', 'application', 'intelligence', 'architecture', 'data', 'gathering', 'information', 'system', 'end-user', 'support', 'cross', 'fault', 'security', 'BYOD', 'defense', 'license', 'multiplatform', 'integration', 'network', 'admin', 'reverse engineering', 'testing', 'product', 'global', 'password', 'management', 'research', 'development', 'root', 'software', 'hardware', 'kernel', 'exploit', 'proprietary', 'server', 'cyberbullying', 'VOiP', 'web-based', 'front-end', 'workflow', 'optimization', 'innovative', 'specialized', 'attack-vector', 'professional', 'leader', 'forensics', 'occupational', 'hashtag', 'social', 'blockchain', 'GoLang', 'rust', 'machine-learning', 'deep-learning', 'tensor-flow', 'devops', 'containerization', 'in a docker container', 'ansible', 'serverless', 'fileless']


def getBuzzwords(maxWord):
	firstWord = random.randint(0,maxWord)
	secondWord = random.randint(0,maxWord)
	while(firstWord==secondWord):
		secondWord = random.randint(0,maxWord)
	buzzwordPair = buzzwords[firstWord] + " " + buzzwords[secondWord]
	return(buzzwordPair)

def clearScreen():
	if(sys.platform[:3]=='win'):
		os.system("cls")
	else:
		os.system("clear")

def printBuzzwords(wordString):
	print(wordString)
	print("Press enter for a new buzzword pair.")
	pyVersion = sys.version[0]
	if(int(pyVersion) < 3):
		keyPress = raw_input()
	else:
		keyPress = input()
		
while(True):
	clearScreen()	
	printBuzzwords(getBuzzwords(len(buzzwords) - 1))
