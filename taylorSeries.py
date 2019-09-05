import random as r
import math as m
import time as t
import json
import requests

def taylorSerie(n):
	start = t.time()
	ratio = 0.0

	for i in range(1,n+1):
		ratio += pow(-1,i+1)/(2*i-1)
	pi = ratio*4
	end = t.time()
	print("local pi:", pi, "time:", (end-start), "s")

def taylorSerieCS():
	inicio= t.time()
	pi = requests.get('http://www.cloudinf.appspot.com/').json()['value']*4
	fin = t.time()
	print("C/S pi:", pi, "time:", (fin-inicio), "s")


taylorSerie(1000000)
taylorSerieCS()