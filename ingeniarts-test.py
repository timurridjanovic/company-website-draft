import os
import webapp2
import jinja2
import hmac
import re
from string import letters
import time
import logging
import json

from google.appengine.ext import db
from google.appengine.api import memcache

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)



class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

   
               

class Index(Handler):
    def get(self):
        self.render("index.html")

class History(Index):
    def get(self):
	self.render("history.html")

class Contact(Index):
    def get(self):
	self.render("contact.html")

    def post(self):
	firstname = self.request.get("firstname")
	logging.error(firstname)

class News(Index):
    def get(self):
	self.render("news.html")

class Technology(Index):
    def get(self):
	self.render("technology.html")

class Partners(Index):
    def get(self):
	self.render("partners.html")



app = webapp2.WSGIApplication([('/', Index), ('/history', History), ('/contact', Contact), ('/news', News), ('/technology', Technology), ('/partners', Partners)], 
		debug=True)
