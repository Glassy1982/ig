from flask import Flask, render_template, url_for, request, session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect('host=ec2-52-0-155-79.compute-1.amazonaws.com user=ssukjbptgzsada password=dacde918826aac7e0ee3680078d5487e3a6808ba18cab5515f6a55c0e69fdc09 dbname=daq9525pn99tuo')
db = conn.cursor()


@app.route ('/')
def index():
    return render_template('index.html')


@app.route ('/formSuccess', methods=["POST"])
def formSuccess():
    
    if request.method=="POST":
       
        name = request.form.get('name')
        email = request.form.get('email')
        db.execute('INSERT INTO emails VALUES(default, %s, %s)', (name, email))
        db.execute("SELECT * FROM emails")
        conn.commit()
        mail = db.fetchall()
        
    return render_template('formSuccess.html', mail=mail)
    

@app.route ('/whyus')
def whyus():
    return render_template('whyus.html')


@app.route ('/about')
def about():
    return render_template('about.html')


@app.route ('/testimonials')
def testimonials():
    return render_template('testimonials.html')


@app.route ('/contact')
def contact():
    return render_template('contact.html')


@app.route ('/mealprep')
def mealprep():
    return render_template('mealprep.html')

if __name__ == "__main__":
    app.run()
