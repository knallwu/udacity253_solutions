import webapp2, cgi, re

form3 = """
<html>
  <head>
    <title>Sign UP</title>
    <style type="text/css">
      .lable {text-align: right}
      .error {color:red}
    </style>
  </head>

  <body>
    <h2>SignUp</h2>
    

    <form method="post">
      <table>
        <tr>
          <td class="lable">
            Username 
          </td>
          <td>
            <input type="text" name="username" value="%(username)s">
          </td>        
          <td class="error">
            <div style="color: red">%(er_user)s</div>
          </td>
        </tr>
    
        <tr>
          <td class="lable">
            Password 
          </td>
          <td>
            <input type="password" name="password" value="%(password)s">
          </td>        
          <td class="error">
            <div style="color: red">%(er_pw)s</div>
          </td>
        </tr>
    
        <tr>
          <td class="lable">
            Password again 
          </td>
          <td>
            <input type="password" name="verify" value="%(verify)s">
          </td>        
          <td class="error">
            <div style="color: red">%(er_verify)s</div>
          </td>
        </tr>
    
        <tr>
          <td class="lable">
            Email(Optional) 
          </td>
          <td>
            <input type="text" name="email" value="%(email)s">
          </td>        
          <td class="error">
            <div style="color: red">%(er_email)s</div>
          </td>
        </tr>
      
      </table>
      
      <input type="submit" value="Submit">
    
    </form>
  </body>
</html>
"""

form_welcome = """
<form>
    <h2>Welcome, %(username)s!</h2>
</form>
"""

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASS_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")

def valid_username(username):
    if USER_RE.match(username):
        return True
        
def valid_password(password):
    if PASS_RE.match(password):
        return True

def valid_email(email):
    if EMAIL_RE.match(email):
        return True
        

class SignupHandler(webapp2.RequestHandler):
    def write_form3(self, username="", er_user="",
                    password="", er_pw="",
                    verify="", er_verify="",
                    email="", er_email=""):
        self.response.out.write(form3 % {'username':username,
                                         'password':password,
                                         'verify':verify,
                                         'email':email,
                                         'er_user':er_user,
                                         'er_pw':er_pw,
                                         'er_verify':er_verify,
                                         'er_email':er_email
                                         })
                                         
    def get(self):
        self.write_form3()
        
    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')
        
        if not valid_username(username):
            self.write_form3(username, "Invalid username", "", "",
                             "", "", "", "")
        else:
            if not valid_password(password):
                self.write_form3(username, "", "", "Invalid password!",
                                 "", "", "", "")
            else:
                if not verify == password:
                    self.write_form3(username, "", "", "",
                                     "", "Passwork dosn't match!",
                                     "", "")
                                     
                else:
                    if email:
                        if not valid_email(email):
                            self.write_form3(username, "", password,"", 
                                         verify, "",
                                         email, "Invalid Email address!")
                        else:
                            self.redirect("/signup/welcome?username=" + username)
                    else:
                        self.redirect("/signup/welcome?username=" + username)
            
                
class WelcomeHandler(webapp2.RequestHandler):
    def write_form_welcome(self, username=""):
        self.response.out.write(form_welcome % {'username':username})
        
    def get(self):
        username = self.request.get('username')
        if valid_username(username):
            self.write_form_welcome(username = username)
        else:
            self.redirect("/signup")