from flask import Flask,request
from flask.templating import render_template
from models import *
# 12. Import the models.py and other corresponding library which is going to be required.

# 1. Create an instance of flask and define it

# 2. Create a hello world with the route /test.
@app.route('/test')
def helloworld():
    return 'HelloWorl!'





# 4. Create a route / which will open up the landing page, but before this go to templates folder and add code inside the index.html 
#and its corresponding css at style.css.
@app.route('/')
def index():
    return render_template('index.html',query=Users.query.all())
@app.route('/student')
def student():
    return render_template('register.html')
@app.route('/d/<int:id>')
def d():
    return render_template('index.html',query=Users.query.all())
# 6. Create a route for register page

# 8. Create a route for login page
@app.route('/login')
def login():
    return render_template('login.html')

# 13. Create a registersuccess route which will get trigger when the user submits the data at register page (dont forget to check the action tag)
@app.route('/registersuccess',methods=['POST'])
def registerSuccess():
    if request.method == 'POST':
        id = request.form.get('id')
        name= request.form.get('name')
        email = request.form.get('email')
        entry = Users(id=id,name=name,email=email)
        db.session.add(entry)
        db.session.commit()

    return render_template('index.html',query=Users.query.all())



# 14. Create a loginsuccess route which will check if the users credential entered is correct or not and redirect them to dashboard.html by printing name on it.

# 3. Run your app file at port 8000 with debug option being true
if __name__=="__main__":
    app.run(debug=True)