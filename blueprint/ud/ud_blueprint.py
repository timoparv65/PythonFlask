#luotu 4.2.2016. Update/Delete blueprint

from flask import Blueprint,session,redirect,request,render_template,flash
from app.forms import FriendForm
from app import db
from app.db_models import Users,Friends
from werkzeug import secure_filename

#Create blueprint
#First argument is the name of the blueprint folder
#Second is always __name__ attribute
#Third parameter tells what folder contains your templates
ud = Blueprint('ud',__name__,template_folder='templates',url_prefix=('/app/'))

#when context is /app/delete
@ud.route('delete/<int:id>')
def delete(id):#kutsu selaimessa esim: http://localhost:3000/app/delete/2
    ##pass#ei tee mitään, voidaan käyttää testatessa
    return "Delete"

@ud.route('update')
def update():
    return "Update"


#Lisätty 4.2.2016
@ud.route('friends',methods=['GET','POST'])
def friends():
    form = FriendForm()
    if request.method == 'GET':
        return render_template('template_friends.html',form=form,isLogged=True)
    else:
        if form.validate_on_submit():
            print('friends from submit ok')
            temp = Friends(form.name.data,form.address.data,form.age.data,session['user_id'])
            
            # save the image if present
            if form.upload_file.data:
                filename = secure_filename(form.upload_file.data.filename)
                form.upload_file.data.save('app/static/images/' + filename)
                temp.filename = '/static/images/' + filename
            
            db.session.add(temp)
            db.session.commit()
            #2. tapa listata ystävät. Kts db_models.py
            user = Users.query.get(session['user_id'])
            print(user.friends)
            return render_template('template_user.html',isLogged=True,friends=user.friends)
        else:
            flash('Give proper values to all fields')
            return render_template('template_friends.html',form=form,isLogged=True)

def before_request():
    if not 'isLogged' in session:
        return redirect('/')

#tämä suoritetaan aina ennen minkään route:n suorittamista
ud.before_request(before_request)