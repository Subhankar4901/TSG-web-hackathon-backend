from . import app
from .models import User,Event,db
from flask import render_template,make_response,request,redirect,url_for,g
from .jwt import getToken, validateToken
import bcrypt
@app.route("/home")
def home():
    if g.user:
        return redirect(url_for("profile",usr=g.user.username))
    else:
        return render_template("home.html")
@app.route("/login", methods=["GET","POST"])
def login():
    if request.method=="POST":
        username=request.form.get("username")
        password=request.form.get("password")
        user=User.query.filter_by(username=username).first()
        if user is None:
            return render_template("login.html")
        else:
            if bcrypt.checkpw(password.encode("utf-8"),user.password.encode("utf-8")):
                mytoken=getToken(username)
                resp=make_response(redirect(url_for("profile",usr=username)))
                resp.set_cookie("session",mytoken,httponly=True)
                return resp
            else:
                return render_template("login.html")
    elif g.user:
        return redirect(url_for("profile",usr=g.user.username))
    else:
        return render_template("login.html")
@app.route("/signup",methods=["GET","POST"])
def signup():
    if request.method=="POST":
        username=request.form.get("username")
        email=request.form.get("email")
        password=request.form.get("password").encode("utf-8")
        if User.query.filter_by(username=username).first():
            return render_template("register.html",msg="Username already exists")
        elif User.query.filter_by(email=email).first():
            return render_template("register.html",msg="Email already exists")
        else:            
            user=User(username=username,email=email,password=bcrypt.hashpw(password,bcrypt.gensalt()).decode("utf-8"))
            db.session.add(user)
            db.session.commit()
            myToken=getToken(username)
            resp=make_response(redirect(url_for("profile",usr=username)))
            resp.set_cookie("session",myToken,httponly=True)
            return resp
    else:
        return render_template("register.html")
@app.route("/profile/<usr>", methods=["GET","POST"])
def profile(usr):
    if request.method=="POST":
        if g.user.username==usr and usr=="admin":
            event_name=request.form.get("event")
            new_event=Event(name=event_name)
            db.session.add(new_event)
            db.session.commit()
            return redirect(url_for("profile",usr=g.user.username))   
        else:
            return redirect(url_for("profile",usr=g.user.username))   
    elif g.user.username==usr:
        events=[]
        for event in g.user.events:
            events.append(event.name)
        return render_template("profile.html",events=events,user=g.user)
    else:
        return redirect(url_for("login"))
@app.route("/logout")
def logout():
    resp=make_response(redirect(url_for("home")))
    resp.delete_cookie("session")
    g.user=None
    return resp
@app.route("/events/<id>",methods=["GET","POST"])
def events(id):
    if id=="dashboard":
        cur_events=[]
        for event in Event.query.all():
            cur_events.append(event)
        return render_template("event-dashboard.html",events=cur_events)
    else:
        event=Event.query.filter_by(id=id).first()
        if request.method=="POST":
            if g.user:
                if not g.user in event.participants:
                    event.participants.append(g.user)
                    db.session.commit()
                    return redirect(url_for("profile",usr=g.user.username))
                return render_template("event.html",event=event,msg="You have already applied")
            else:
                return redirect(url_for("login"))
        else:
            return render_template("event.html",event=event,msg=None)
@app.before_request
def before():
    g.user=None
    token=request.cookies.get("session")
    val=validateToken(token)
    if not val==None:
        g.user=User.query.filter_by(username=val).first()
    