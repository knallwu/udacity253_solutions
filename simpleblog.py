import os
import webapp2
import jinja2
from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)
    
    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)
    
    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

def blog_key(name = 'defaut'):
    return db.Key.from_path('Blog', name)
        
class Blog(db.Model):
    subject = db.StringProperty(required = True)
    content = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)
    last_modified = db.DateTimeProperty(auto_now = True)
    
        
class NewPost(Handler):
    def render_post(self, subject="", content="", error=""):
        self.render("simpleblog_post.html", subject = subject, content = content, error = error)
    
    def get(self):
        self.render("simpleblog_post.html")
        
    def post(self):
        subject = self.request.get("subject")
        content = self.request.get("content")
        
        if subject and content:
            a = Blog(parent = blog_key(), subject = subject, content = content)
            a.put()
            self.redirect("/simpleblog/%s" % str(a.key().id()))
        else:
            error = "error!!"
            self.render_post(subject, content, error)

class MainPage(Handler):
    def get(self):
        posts = db.GqlQuery("SELECT * FROM Blog ORDER BY created DESC")
        self.render("simpleblog.html", posts = posts)

class SinglePost(Handler):
    def get(self, post_id):
        key = db.Key.from_path('Blog', int(post_id), parent=blog_key())
        post = db.get(key)
        
        if not post:
            self.response.out.write("""
                                    404! Page doesn't exist! 
                                    <a href="/simpleblog">Back Mainpage</a>""")
            return
        #self.response.out.write('hello')
        self.render("simpleblog_single.html", post = post)
