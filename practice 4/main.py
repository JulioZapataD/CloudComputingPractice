import webapp2
import random as r
import math as m
import json




class MainPage(webapp2.RequestHandler):

    def get(self):
    	self.response.headers['Content-Type'] = 'application/json'
    	valor = 0
        total = int( self.request.get('t') )
        for i in range(0, total):
            x= r.random()
            y= r.random()
            if (x*x + y*y) < 1:
            	valor += 1
        res= {
		    'value': valor
		    }
        self.response.write(json.dumps(res))
    

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
