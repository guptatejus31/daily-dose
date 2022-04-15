from flask import Flask, request, redirect
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///static/site.db'
db = SQLAlchemy(app)

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=False, nullable=False)
    password = db.Column(db.String(20), unique=False, nullable=False)
    para = db.Column(db.String(100), unique=False, nullable=False)

    def __repr__(self):
        return f"para : {self.para}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save', methods=["post"])
def save():
    para1 = request.form.get("para")
    uname = request.form.get("username")
    print(uname)
    user = Profile.query.filter_by(username=uname).first()
    print("user",user,"//","user.username","//para",para1,"//uname",uname )
    user.para = para1
    db.session.commit()
    return redirect("/")


@app.route('/login', methods=["POST"])
def profile():
    username = request.form.get("username")
    password = request.form.get("password")
    print(username,password)
    user = Profile.query.filter_by(username=username).first()
    if user is None :
        if username == "" and password == "root":
            profiles = Profile.query.all()
            print("profile")
            return render_template("database.html",profiles=profiles)
        elif username != '' and password != '':
            para = ""
            p = Profile(username=username, password=password, para=para)
            db.session.add(p)
            db.session.commit()
            print("comit")
            user = Profile.query.filter_by(username=username).first()
            return render_template("diary.html",user=user)
        else:
            print("prblm")
            return redirect('/')
    else:
        if password == user.password:
            return render_template("diary.html",user=user)
        else:
            return redirect("/")

if __name__ == '__main__':
    db.create_all()
    app.run()