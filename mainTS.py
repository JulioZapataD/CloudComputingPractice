import webapp2
import random as r
import math as m
import json




class MainPage(webapp2.RequestHandler):

    def get(self):
    	self.response.headers['Content-Type'] = 'application/json'
    	valor = 0.0
    	for i in range(1,1000001):
            valor += pow(-1,i+1)/(2*i-1)
        res= {
		    'value': valor
		    }
        self.response.write(json.dumps(res))
    

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
