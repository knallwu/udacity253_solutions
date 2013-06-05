import webapp2, cgi

form2="""
<form method="post">
    Type some text below and click the button to encode:
    <br>
    <textarea rows="10" cols="80" name="text">%(input_text)s</textarea>
    <br>
    <input type="submit" value="Encode">
</form>
"""        

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def escape_html(s):
    return cgi.escape(s, quote=True)
    
    
def rot13(s):
    encoded = []
    for i in s:
        if i not in letters:
            encoded.append(i)
        else:    
            init_pos = letters.index(i)
            if init_pos <= 25 :
                rot13_pos = init_pos + 13
                l = letters[rot13_pos]
                letter = l.lower()
                encoded.append(letter)
            else:
                rot13_pos = init_pos + 13
                if rot13_pos > 51:
                    rot13_pos = init_pos + 13 - 26
                letter = letters[rot13_pos]
                encoded.append(letter)
    return ''.join(encoded)

        
class Rot13Handler(webapp2.RequestHandler):
    def write_form2(self, input_text=""):
        self.response.out.write(form2 % {'input_text':input_text})
    
    def get(self):
        self.write_form2()
        
    def post(self):
        output_text = self.request.get('text')
        if output_text:
            input_text = rot13(output_text)
            self.write_form2(escape_html(input_text))