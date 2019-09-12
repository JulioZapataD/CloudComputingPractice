import random as r
import math as m
import time as t
import json
import requests
from multiprocessing.pool import ThreadPool

def localDrawPoint(total):
	suma = 0
	for i in range(0, total):
		x= r.random()
		y= r.random()

		if (x*x + y*y) < 1.0:
			suma += 1

	return suma


def MonteCarloPi(total):
	p1 = ThreadPool(processes=1)
	p2 = ThreadPool(processes=2)
	p3 = ThreadPool(processes=3)

	it= int( total/3 )
	
	start= t.time()

	pr1 = p1.apply_async(localDrawPoint, (it,))
	pr2 = p2.apply_async(localDrawPoint, (it,))
	pr3 = p3.apply_async(localDrawPoint, (it,))

	suma1 = pr1.get()
	suma2 = pr2.get()
	suma3 = pr3.get()

	sum_total = suma1 + suma2 + suma3

	pi = (float(sum_total)/total) * 4.0

	end = t.time()

	print("local: pi=", pi, "tiempo de calculo", (end - start), "s" )

def drawPoint1():
	pto = requests.get('https://mc-proyecto1-cs.appspot.com/?t=1000000').json()['value']
	t.sleep(6)
	return pto

def drawPoint2():
	pto = requests.get('https://mc-proyecto2-cs.appspot.com/?t=1000000').json()['value']
	t.sleep(6)
	return pto

def drawPoint3():
	pto = requests.get('https://mc-proyecto3-cs.appspot.com/?t=1000000').json()['value']
	t.sleep(6)
	return pto

def MonteCarloPiCS(total):

	start= t.time()

	p1 = ThreadPool(processes=1)
	p2 = ThreadPool(processes=2)
	p3 = ThreadPool(processes=3)

	pr1 = p1.apply_async(drawPoint1)
	pr2 = p2.apply_async(drawPoint2)
	pr3 = p3.apply_async(drawPoint3)

	suma1 = pr1.get()
	suma2 = pr2.get()
	suma3 = pr3.get()

	sum_total = suma1 + suma2 + suma3

	pi = (float(sum_total)/total) * 4.0

	end = t.time()

	print("C/S: pi=", pi, "tiempo de calculo", (end - start), "s" ) 


MonteCarloPi(3000000)


MonteCarloPiCS(3000000)
