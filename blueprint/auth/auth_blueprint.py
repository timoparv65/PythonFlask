#luotu 4.2.2016. Register/Login blueprint

from flask import Blueprint
from app.forms import LoginForm,RegisterForm
from app import db
from app.db_models import Users,Friends
from flask.ext.bcrypt import check_password_hash

auth = Blueprint('auth',__name__,template_folder='templates')



@app.route('/',methods=['GET','POST'])
def index():
    login = LoginForm()#login objekti
    if request.method == 'GET':
        return render_template('template_index.html',form=login,isLogged=False)
    else:
        #check if form data is valid
        if login.validate_on_submit():
            user = Users.query.filter_by(email=login.email.data)
            print(user)
            if (user.count() == 1) and (check_password_hash(user[0].passw,login.passw.data)):
                print(user[0])
                session['user_id'] = user[0].id
                session['isLogged'] = True
                print(session['user_id'])
                #Haetaan ystävät
                #tapa 1 listata ystävät
                friends = Friends.query.filter_by(user_id =user[0].id)
                print(friends)
                return render_template('template_user.html',isLogged=True,friends=friends)
            else:
                flash('Wrong email or password')
                return render_template('template_index.html',form=login,isLogged=False)
        #form data was not valid
        else:
            flash('Give proper information to email and password fields!')
            return render_template('template_index.html',form=login,isLogged=False)


@app.route('/register',methods=['GET','POST'])
def registerUser():
    form = RegisterForm()
    if request.method == 'GET':
        return render_template('template_register.html',form=form,isLogged=False)
    else:
        if form.validate_on_submit():
            user = Users(form.email.data,form.passw.data)
            try:
                db.session.add(user)
                db.session.commit()
            except:
                db.session.rollback()
                flash('Username allready in use')
                return render_template('template_register.html',form=form,isLogged=False)
            flash("Name {0} registered".format(form.email.data))
            return redirect('/')
        else:
            flash('Invalid email address or no password given')
            return render_template('template_register.html',form=form,isLogged=False)


@app.route('/logout')
def logout():
    #delete user session (clear all values)
    session.clear()
    return redirect('/')

