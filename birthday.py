import webapp2, cgi

form="""
<form method="post">
    What's your birthday?
    <br>
    <lable>
        Month: <input type="text" name="month" value="%(month)s">
    </lable>
    
    <lable>
        Day: <input type="text" name="day" value="%(day)s">
    </lable>
    
    <lable>
        Year: <input type="text" name="year" value="%(year)s">
    </lable>
    
    <div style="color: red">%(error)s</div>
    
    <br>
    <br>
    <input type="submit">
</form>
"""

def escape_html(s):
    return cgi.escape(s, quote=True)

months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']
          
month_abbvs = dict((m[:3].lower(), m) for m in months)
          
def valid_month(month):
    if month:
        short_month = month[:3].lower()
        return month_abbvs.get(short_month)
        
def valid_day(day):
    if day and day.isdigit():
        day = int(day)
        if day in range(1,32):
            return day
            
def valid_year(year):
    if year and year.isdigit():
        year = int(year)
        if year in range(1900, 2021):
            return year                  

class BirthdayHandler(webapp2.RequestHandler):
    def write_form(self, error="", month="", day="", year=""):
        self.response.out.write(form % {"error": error,
                                        "month": escape_html(month),
                                        "day": escape_html(day),
                                        "year": escape_html(year)})

    def get(self):
        self.write_form()
        
    def post(self):
        user_month = self.request.get('month')
        user_day = self.request.get('day')
        user_year = self.request.get('year')
        
        month = valid_month(user_month)
        day = valid_day(user_day)
        year = valid_year(user_year)
        
        if not (month and day and year):
            self.write_form("That doesn't look valid to me, friend.",
                            user_month, user_day, user_year)
        else:
            self.redirect("/birthday/thanks")
        
class ThanksHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("Thanks! That's a totally valid day!")
        
          