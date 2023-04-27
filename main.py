from flask import Flask, render_template,session,request
from student import Student
from flask_session import Session
from DBHandler import DBHandler
from note import Note
from datetime import date
import pymysql

app = Flask(__name__)


app.secret_key ="secretkey"
app.config['SESSION_TYPE']='filesystem'
app.config["SESSION_PERMANENT"]=False

Session(app)


@app.route('/')
def WelcomePage():
    return render_template('welcomePage.html')
    # return render_template("welcomePage.html")
    return render_template("registerStudent.html")

@app.route('/home')
def goHome():
    print(session['email'])
    if session["email"]!=None:
        return render_template("home.html")
    else:
        return render_template('registerStudent.html',msg='Login First')
    # if session!=None:
    #     return render_template("home.html")

@app.route('/register')
def register():
    return render_template('registerStudent.html')

    
@app.route('/registered', methods=["POST"])
def registered():
    name = request.form["name"]
    age = request.form["age"]
    email = request.form["email"]
    password = request.form["password"]
    notebook=request.form["notebook"]
    print(name,age,email,password,notebook)
    student = Student(name,age,email,password,notebook)
    #print(name, age, city, profession)
    db = DBHandler('localhost', 'root', 'password', 'students', 3307)
    isRegister = db.register_student(student)
    if isRegister:
        return render_template("/loginPage.html")
    else:
        return render_template("registerStudent.html", msg="Registration Failed! Try Again")

@app.route('/login')
def login():
    return render_template('loginPage.html')


@app.route('/loggedIn',methods=["POST"])
def loggedIn():
    # if session['email']!=None:
    # return render_template('registerStudent.html')
    email = request.form["email"]
    Xemail=email.split('@')
    if Xemail[1]!='pucit.edu.pk':
        return render_template('loginPage.html',msg='Email Not Correct!!')
    password = request.form["password"]
    print(email,password)
    db = DBHandler('localhost', 'root', 'password', 'students', 3307)
    isVerified = db.verify_student(email,password)
    if isVerified:
        session["id"] = isVerified[0][0]
        print(session["id"])
        session["email"] = isVerified[0][1]
        session["password"] = isVerified[0][2]
        session["name"] = isVerified[0][3]
        session["age"] = isVerified[0][4]
        session["notebook"] = isVerified[0][5]
        return render_template('home.html')
    else:
        return render_template('loginPage.html',msg='Login Failed! Try Again')

    # if pwd.isnumeric() == True:
    #     session["name"] = name
    #     session["pwd"] = pwd
    #     return render_template("second.html")
    # else:
    #     return render_template("first.html")

@app.route('/create')
def create():
    if session['email']!=None:
        return render_template('note.html')
    else:
        return render_template('welcomePage.html',msg='Login First')
        # contactList = ContactController.DisplayContact()
        # return render_template("contacts.html", ContactList=contactList)

@app.route('/createdNote',methods=["POST"])
def createdNote():
    if session['email']!=None:
        print('in session')
        title = request.form["title"]
        text = request.form["text"]
        dateToday=date.today()
        student_id=session["id"]
        note=Note(title,text,student_id,dateToday)
        db=DBHandler('localhost', 'root', 'password', 'students', 3307)
        isNote=db.createNote(note)
        return render_template('note.html',msg='Note Successfully Created!')
    else:
        return render_template('note.html',msg='Note Not Created')



@app.route('/show',methods=['GET'])
def show():
    if session['email']!=None:
        id=session["id"]
        name=session["name"]
        age=session["age"]
        email=session["email"]
        password=session["password"]
        notebook=session["notebook"]
        #student=Student(name,age,email,password,notebook)
        db=DBHandler('localhost', 'root', 'password', 'students', 3307)
        print(id)
        allNotes=db.showAllNotes(id)
        print(allNotes)
        if allNotes:
            return render_template('showAllNotes.html',AllNotes=allNotes)
        else:
            return render_template('showAllNotes.html',msg='No Note Found')
    else:
        return render_template('welcomePage.html',msg='Login First')


    # return render_template("loginPage.html", msg='Login First')

@app.route('/logout')
def logout():
    session.clear()

    # SESSION CAN BE CLEARED THIS WAY AS WELL!

    session["id"]=None
    session["name"]=None
    session["age"]=None
    session["email"]=None
    session["password"]=None
    session["notebook"]=None

    return render_template('loginPage.html')
    # contactList = ContactController.DisplayContact()
    # return render_template("contacts.html", ContactList=contactList)


# @app.route('/Search')
# def SearchContacts():


if __name__ == '__main__':
    app.run()
