from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
# flask.ext.sqlalchemy . . . this means that sqlalchemy was already installed in your app folders
from send_email import send_email
from sqlalchemy.sql import func

app=Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:shivani@123@localhost/App9'

class Data(db.Model):
    __tablename__="data"
    id = db.Column(db.Integer,primary_key=True)
    email_ = db.Column(db.String(120),unique=True)
    height_ = db.Column(db.Integer)

    def __init__(self,email_,height_):
        self.email_=email_
        self.height_=height_

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success',methods=['POST'])
def success():
    if request.method == 'POST':
        email = request.form["email_name"]
        height = request.form["height_name"]

        if db.session.query(Data).filter(Data.email_==email).count()==0:
            data = Data(email,height)
            db.session.add(data)
            db.session.commit()
            average_height = db.session.query(func.avg(Data.height_)).scalar()
            average_height = round(average_height,2)
            # round upto 2 decimal points
            count = db.session.query(Data.height_).count()
            send_email(email,height,average_height,count)
            return render_template('success.html')
        return render_template('index.html',text="Seems like we do have that mail<br> address already!")
if __name__ == '__main__':
    app.run(debug=True)
    # app.run(port=5001)
