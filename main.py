from flask import Flask, request, redirect
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    template = jinja_env.get_template('signup.html')
    return template.render()

@app.route("/test", methods=['POST'])
def validation():
    first_name = request.form['username']
    passw = request.form['password']
    vpassw = request.form['vpassword']
    mail = request.form['email']
    fne = ''
    pwe = ''
    vpwe = ''
    me = ''
    idxm = 0
    idxp = 0

    for letter in first_name:
        if letter == " " or len(first_name) < 3 or len(first_name) > 20:
            fne = "not a valid username"

    for letter in passw:
        if letter == " " or len(passw) < 3 or len(passw) > 20:
            fne = "not a valid username"
    
    for letter in mail:
        if letter == "@":
            idxm +=1
        if letter == ".":
            idxp +=1

    if first_name == '':
        fne = 'not a valid username'
    if passw == '':
        pwe = 'not a valid password'
    if vpassw == '' or passw!=vpassw:
        vpwe = 'not valid or does not match'
    if mail == '' or idxm != 1 or idxp !=1:
        me = 'not a valid email'


    template = jinja_env.get_template('signup.html')

    if fne == pwe == vpwe == me:
        return redirect('/success?name={0}'.format(first_name))
    

    

    return template.render(name_error=fne, pw_error=pwe, vpw_error=vpwe, email_error=me, name=first_name, email=mail)

@app.route("/success")
def success():
    first_name = request.args.get('name')
    template = jinja_env.get_template('success.html')
    return template.render(name=first_name)

app.run()