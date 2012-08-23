import os
import re
from string import letters

import webapp2
import jinja2

#from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)

def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)

class BaseHandler(webapp2.RequestHandler):
    def render(self, template, **kw):
        self.response.out.write(render_str(template, **kw))

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

class Home(BaseHandler):
    def get(self):
        self.render('home.html')

class Post(BaseHandler):
    def get(self):
        self.render('post')    

app = webapp2.WSGIApplication([('/', Home),
                               ('/post' , Post)],
                              debug=True)
