import webapp2
import rot13, birthday, signup, ascii, simpleblog, play, hash_cookies_counter

form = """
<!DOCTYPE html>
<html>
  <title></title>
  
  <body>
    <h3>Here are some homeworks for learning Web Developement</h3>
    <form method="GET">
      <a href="/rot13">Rot13</a><br><br>
      <a href="/birthday">Birthday checker</a><br><br>
      <a href="/signup">User signup checker</a><br><br>
      <a href="/ascii">A simple ASCIIChan</a><br><br>
      <a href="/simpleblog">A shabby Blog Webapp</a><br><br>
      <a href="/cookies_counter">Basic Hashing cookies counter</a><br><br>
      <br>Looking for more?<a href="/">...</a>
    </form>
  
  <body>
</html>
"""

class IndexHandler(webapp2.RequestHandler):
    def write(self):
        self.response.out.write(form)
    def get(self):
        self.write()

 
app = webapp2.WSGIApplication([('/', IndexHandler),
                               ('/rot13', rot13.Rot13Handler), 
                               ('/birthday', birthday.BirthdayHandler),
                               ('/birthday/thanks', birthday.ThanksHandler),
                               ('/signup', signup.SignupHandler),
                               ('/signup/welcome', signup.WelcomeHandler),
                               ('/ascii', ascii.MainPage),
                               ('/simpleblog',simpleblog.MainPage),
                               ('/simpleblog/newpost', simpleblog.NewPost),
                               ('/simpleblog/([0-9]+)', simpleblog.SinglePost),
                               ('/cookies_counter', hash_cookies_counter.CookiesCounter),
                               
                               ('/play', play.Play),
                               
                              ],debug=True)
