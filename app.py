import json 
from flask import Flask, render_template, request, flash, Response, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

from flask_wtf import FlaskForm
from sqlalchemy import create_engine
from wtforms import (
    SubmitField,
    HiddenField,
    StringField,
    IntegerField,
    SelectField
)
from wtforms.validators import InputRequired, NumberRange
from countries import countries
from datetime import date
#%%
#Querying DB 

import sqlite3

con = sqlite3.connect("database.sqlite")
#%%
app = Flask(__name__)

# Flask-WTF requires an enryption key - the string can be anything
app.config["SECRET_KEY"] = "super secret key"

# Flask-Bootstrap requires this line
Bootstrap(app)

# the name of the database; add path if necessary
db_name = "database.sqlite"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + db_name

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

# this variable, db, will be used for all SQLAlchemy commands
db = SQLAlchemy(app)
#%%
# each table in the database needs a class to be created for it
# db.Model is required - don't change it
# identify all columns by name and data type
class Entry(db.Model):
    __tablename__ = "entries"
    id = db.Column(db.Integer, primary_key=True)
    #trade profile
    tst1 = db.Column(db.String)
    tst2 = db.Column(db.String)
    tst3 = db.Column(db.String)
    tst4 = db.Column(db.String)
    tst5 = db.Column(db.String)
    tst6 = db.Column(db.String)
    tst7 = db.Column(db.String)
    tst8 = db.Column(db.String)

    #perf data
    tst9 = db.Column(db.String)
    tst10 = db.Column(db.String)
    tst11  = db.Column(db.String)
    tst12 = db.Column(db.String)
    tst13 = db.Column(db.String)
    
    #targets
    tst14 = db.Column(db.String)
    tst15 = db.Column(db.Integer)
    tst16 = db.Column(db.String)
    tst17 = db.Column(db.Integer)

    #rationale 
    tst18 = db.Column(db.String)
    tst19 = db.Column(db.String)
    tst20 = db.Column(db.String)
    tst21 = db.Column(db.String)
    tst22 = db.Column(db.String)
    tst23 = db.Column(db.String) 

    #sizing
    tst24 = db.Column(db.Integer)
    tst25 = db.Column(db.Integer)
    tst26 = db.Column(db.Integer)
    tst27 = db.Column(db.Integer)

    #esg 
    tst28 = db.Column(db.String)
    tst29 = db.Column(db.String) 
    
    #comments 
    tst30 = db.Column(db.String) 
    
    #close date
    tst31 = db.Column(db.String)
    tst32 = db.Column(db.String)

    def __init__(self, tst1, tst2, tst3, tst4, tst5, tst6, tst7, tst8, tst9, tst10, tst11, tst12,tst13, tst14, tst15, tst16, tst17, tst18, tst19, tst20, tst21, tst22, tst23, tst24,tst25, tst26, tst27, tst28, tst29, tst30, tst31, tst32):
        self.tst1 = tst1
        self.tst2 = tst2 
        self.tst3 = tst3
        self.tst4 = tst4
        self.tst5 = tst5
        self.tst6 = tst6
        self.tst7 = tst7
        self.tst8 = tst8
        self.tst9 = tst9
        self.tst10 = tst10
        self.tst11 = tst11
        self.tst12 = tst12
        self.tst13 = tst13
        self.tst14 = tst14
        self.tst15 = tst15
        self.tst16 = tst16
        self.tst17 = tst17 
        self.tst18 = tst18
        self.tst19 = tst19
        self.tst20 = tst20
        self.tst21 = tst21 
        self.tst22 = tst22
        self.tst23 = tst23           
        self.tst24 = tst24
        self.tst25 = tst25
        self.tst26 = tst26
        self.tst27 = tst27
        self.tst28 = tst28
        self.tst29 = tst29
        self.tst30 = tst30
        self.tst31 = tst31
        self.tst32 = tst32
        #self.country = country
        
        
    def to_dict(self):
        return{
        "id":self.id,
        "tst1": self.tst1,
        "tst2": self.tst2,
        "tst3": self.tst3,
        "tst4": self.tst4,
        "tst5": self.tst5,
        "tst6": self.tst6,
        "tst7": self.tst7,
        "tst8": self.tst8,
        "tst9": self.tst9,
        "tst10": self.tst10,
        "tst11": self.tst11,
        "tst12": self.tst12,
        "tst13": self.tst13,
        "tst14": self.tst14,
        "tst15": self.tst15,
        "tst16": self.tst16,
        "tst17": self.tst17,
        "tst18": self.tst18,
        "tst19": self.tst19,
        "tst20": self.tst20,
        "tst21": self.tst21,
        "tst22": self.tst22,
        "tst23": self.tst23,
        "tst24": self.tst24,
        "tst25": self.tst25,
        "tst26": self.tst26,
        "tst27": self.tst27,
        "tst28": self.tst28,
        "tst29": self.tst29,
        "tst30": self.tst30,
        "tst31": self.tst31,
        "tst32": self.tst32,
        
        }
            
        


engine = create_engine(f"sqlite:///{db_name}")
Entry.__table__.create(bind=engine, checkfirst=True)


# +++++++++++++++++++++++
# forms with Flask-WTF

# form for add_record and edit_or_delete
# each field includes validation requirements and messages
class AddRecord(FlaskForm):
    # id used only by update/edit
    #country_choices = [(country, country) for country in countries]
    id_field = HiddenField()
    tst1 = StringField("tst1", [InputRequired()], id="tst1")
    tst2 = StringField("tst2", [InputRequired()])
    tst3 = StringField("tst3", [InputRequired()])
    bols = ["True", "False"]
    bol_choices = [(bol, bol) for bol in bols]
    
    tst4 = SelectField("tst4", [InputRequired()], id="tst4", choices=bol_choices)
    tst5 = StringField("tst5", [InputRequired()]) #create a calendar dropdown
    lens= ["Long", "Short"]
    lens_choices = [(le, le) for le in lens]
    tst6 = SelectField("tst6", [InputRequired()], id="tst6", choices=lens_choices)
    tst7 = StringField("tst7", [InputRequired()])
    acts = ["Active", "Inactive", "Closed"]
    act_choices = [(ac, ac) for ac in acts]
    tst8 = SelectField("tst8", [InputRequired()], id="tst8", choices=act_choices) 
    optns = ["option1", "option2", "option3"]
    optn_choices = [(opt, opt) for opt in optns]
    tst9 = SelectField("tst9", [InputRequired()], id="tst9", choices=optn_choices)
    tst10 = StringField("tst10", [InputRequired()]) 
    tst11 = StringField("tst11", [InputRequired()])
    tst12 = StringField("tst12", [InputRequired()])
    tst13 = StringField("tst13", [InputRequired()])
    ooptns = ["option1", "option2", "option3"]
    ooptn_choices = [(oop, oop) for oop in ooptns]
    tst14 = SelectField("tst14", [InputRequired()], id="tst14", choices=ooptn_choices)
    tst15 = IntegerField("tst15", [InputRequired(), NumberRange(min=1, max=999, message="Invalid range")])
    thtwo = ["3","3-6","12"]
    tht_choices = [(th, th) for th in thtwo]
    tst16 = SelectField("tst16", [InputRequired()], id="tst16", choices=tht_choices)    
    tst17 = IntegerField("tst17", [InputRequired(), NumberRange(min=1, max=999, message="Invalid range")])
    tst18 = StringField("tst18", [InputRequired()], id="tst18")
    tst19 = StringField("tst19", [InputRequired()])
    tst20 = StringField("tst20", [InputRequired()])
    tst21 = StringField("tst21", [InputRequired()]) 
    tst22 = StringField("tst22", [InputRequired()])
    tst23 = StringField("tst23", [InputRequired()])
    tst24 = IntegerField("tst24", [InputRequired(), NumberRange(min=1, max=999, message="Invalid range")])
    tst25 = IntegerField("tst25", [InputRequired(), NumberRange(min=1, max=999, message="Invalid range")])
    tst26 = IntegerField("tst26", [InputRequired(), NumberRange(min=1, max=999, message="Invalid range")])
    tst27 = IntegerField("tst27", [InputRequired(), NumberRange(min=1, max=999, message="Invalid range")])   
    ontws = ["1","2","3"]
    ont_choices = [(on, on) for on in ontws]         
    tst28 = SelectField("tst28", [InputRequired()], id="tst28", choices=ont_choices)
    tst29 = StringField("tst29", [InputRequired()])
    tst30 = StringField("tst30", [InputRequired()], id="tst30")
    tst31 = StringField("tst31", [InputRequired()], id="tst31") #create a calendar dropdown
    # tst32 - date - ha ndled in the route
    tst32 = HiddenField()
    submit = SubmitField("Add Record")


def email_data(subject, name, quantity, country, tst32):
    # format body as html table
    body = f"""<html>
            <table width="600" style="border:1px solid #333">
            <tr>
            <td align="center">head</td>
            </tr>
            <tr>
            <td align="center">
                body 
                <table align="center" width="300" border="0" cellspacing="0" cellpadding="0" style="border:1px solid #ccc;">
                <tr>
                    <td> Name  </td>
                    <td> {name} </td>
                </tr>
                <tr>
                    <td> Quantity  </td>
                    <td> {quantity} </td>
                </tr>
                <tr>
                    <td> Country  </td>
                    <td> {country} </td>
                </tr>
                <tr>
                    <td> tst32  </td>
                    <td> {tst32} </td>
                </tr>
                </table>
            </td>
            </tr>
            </table>
            </html>"""

    return subject, body


def stringdate():
    today = date.today()
    date_list = str(today).split("-")
    # build string in format 01-01-2000
    date_string = date_list[1] + "-" + date_list[2] + "-" + date_list[0]
    return date_string


# +++++++++++++++++++++++
# routes
@app.route("/", methods=["GET", "POST"])
def index():
    form1 = AddRecord()
    if form1.validate_on_submit():
        tst1 = request.form["tst1"]
        tst2 = request.form["tst2"]
        tst3 = request.form["tst3"]
        tst4 = request.form["tst4"]
        tst5 = request.form["tst5"]
        tst6 = request.form["tst3"]
        tst7 = request.form["tst7"]
        tst8 = request.form["tst8"]
        tst9 = request.form["tst9"]
        tst10 = request.form["tst10"]
        tst11 = request.form["tst11"]
        tst12 = request.form["tst12"]
        tst13 = request.form["tst13"]
        tst14 = request.form["tst14"]
        tst15 = request.form["tst15"]
        tst16 = request.form["tst16"]
        tst17 = request.form["tst17"]
        tst18 = request.form["tst18"]
        tst19 = request.form["tst19"]
        tst20 = request.form["tst20"]
        tst21 = request.form["tst21"]
        tst22 = request.form["tst22"]
        tst23 = request.form["tst23"]
        tst24 = request.form["tst24"]
        tst25 = request.form["tst25"]
        tst26 = request.form["tst26"]
        tst27 = request.form["tst27"]
        tst28 = request.form["tst28"]
        tst29 = request.form["tst29"]
        tst30 = request.form["tst30"]
        tst31 = request.form["tst31"]
        tst32 = request.form["tst32"]
        
        record = Entry(tst1, tst2, tst3, tst4, tst5, tst6, tst7, tst8, tst9, tst10, tst11, tst12, tst13, tst14, tst15, tst16, tst17, tst18, tst19, tst20, tst21, tst22, tst23, tst24, tst25, tst26, tst27, tst28, tst29, tst30, tst31, tst32)
        
        
        # Flask-SQLAlchemy magic adds record to database
        db.session.add(record)
        db.session.commit()
        # create a message to send to the template
        message = f"The data for {tst1} Entry has been submitted."
        # update email subject
        subject = "New Entry"
        
        return render_template("index.html", message=message, entity=record)
    else:
        # show validaton errors
        # see https://pythonprogramming.net/flash-flask-tutorial/
        for field, errors in form1.errors.items():
            for error in errors:
                flash(
                    "Error in {}: {}".format(getattr(form1, field).label.text, error),
                    "error",
                )
        return render_template("index.html", form1=form1)
    #return render_template('index.html', entries=entries)

# small form
class DeleteForm(FlaskForm):
    id_field = HiddenField()
    purpose = HiddenField()
    submit = SubmitField('Delete This entry')

@app.route('/_autocomplete', methods=['GET'])
def autocomplete():
    return Response(json.dumps(countries), mimetype='application/json')


@app.route('/list_entries/', methods=['GET'])
def list_entries():   
    entries = Entry.query.all()
    return render_template('list_entries.html', entries=entries)


@app.route('/filter_data', methods=['GET'])
def entries_endpoint(): 
    query = Entry.query

    # search filter
    search = request.args.get('search[value]')
    if search:
        query = query.filter(db.or_(
            Entry.tst1.like(f'%{search}%'),
            Entry.tst2.like(f'%{search}%')
        ))
    total_filtered = query.count()

    # pagination
    start = request.args.get('start', type=int)
    length = request.args.get('length', type=int)
    query = query.offset(start).limit(length)

    # response
    return {
        'data': [user.to_dict() for user in query],
        'recordsFiltered': total_filtered,
        'recordsTotal': Entry.query.count()
    }



@app.route('/add_record/', methods=['GET', 'POST'])
def add_record():
    # get a list of unique values in the style column
    form1 = AddRecord()
    if form1.validate_on_submit():
        tst1 = request.form["tst1"]
        tst2 = request.form["tst2"]
        tst3 = request.form["tst3"]
        tst4 = request.form["tst4"]
        tst5 = request.form["tst5"]
        tst6 = request.form["tst3"]
        tst7 = request.form["tst7"]
        tst8 = request.form["tst8"]
        tst9 = request.form["tst9"]
        tst10 = request.form["tst10"]
        tst11 = request.form["tst11"]
        tst12 = request.form["tst12"]
        tst13 = request.form["tst13"]
        tst14 = request.form["tst14"]
        tst15 = request.form["tst15"]
        tst16 = request.form["tst16"]
        tst17 = request.form["tst17"]
        tst18 = request.form["tst18"]
        tst19 = request.form["tst19"]
        tst20 = request.form["tst20"]
        tst21 = request.form["tst21"]
        tst22 = request.form["tst22"]
        tst23 = request.form["tst23"]
        tst24 = request.form["tst24"]
        tst25 = request.form["tst25"]
        tst26 = request.form["tst26"]
        tst27 = request.form["tst27"]
        tst28 = request.form["tst28"]
        tst29 = request.form["tst29"]
        tst30 = request.form["tst30"]
        tst31 = request.form["tst31"]        
        tst32 = stringdate()
        record = Entry(tst1, tst2, tst3, tst4, tst5, tst6, tst7, tst8, tst9, tst10, tst11, tst12, tst13, tst14, tst15, tst16, tst17, tst18, tst19, tst20, tst21, tst22, tst23, tst24, tst25, tst26, tst27, tst28, tst29, tst30, tst31, tst32)
        
        
        # Flask-SQLAlchemy magic adds record to database
        db.session.add(record)
        db.session.commit()
        # create a message to send to the template
        message = f"The data for {name} Entry has been submitted."
        # update email subject
        subject = "New Entry"
        email_subject, body = email_data(subject, name, quantity, country, tst32)
        return render_template(
            "add_record.html", message=message, subject=email_subject, body=body, countries=countries
        )
    else:
        # show validaton errors
        # see https://pythonprogramming.net/flash-flask-tutorial/
        for field, errors in form1.errors.items():
            for error in errors:
                flash(
                    "Error in {}: {}".format(getattr(form1, field).label.text, error),
                    "error",
                )
        return render_template("add_record.html", form1=form1)

@app.route('/edit_or_delete', methods=['POST'])
def edit_or_delete():
    id = request.form['id']
    choice = request.form['choice']
    entry = Entry.query.filter(Entry.id == id).first()
    # two forms in this template
    form1 = AddRecord()
    form2 = DeleteForm()
    return render_template('edit_or_delete.html', entry=entry, form1=form1, form2=form2, choice=choice, countries=countries)


@app.route('/edit_result', methods=['POST'])
def edit_result():
    id = request.form['id_field']
    # call up the record from the database
    entry = Entry.query.filter(Entry.id == id).first()
    # update all values
    entry.tst1 = request.form['tst1']
    entry.tst2 = request.form['tst2']
    entry.tst3 = request.form['tst3']
    entry.tst32 = stringdate()

    form1 = AddRecord()
    if form1.validate_on_submit():
        # update database record
        db.session.commit()
        # create a message to send to the template
        message = f"The data for entry {entry.tst1} has been tst32."
        return render_template('result.html', message=message)
    else:
        # show validaton errors
        entry.id = id
        # see https://pythonprogramming.net/flash-flask-tutorial/
        for field, errors in form1.errors.items():
            for error in errors:
                flash("Error in {}: {}".format(
                    getattr(form1, field).label.text,
                    error
                ), 'error')
        return render_template('edit_or_delete.html', form1=form1, entry=entry, choice='edit', countries=countries)

@app.route('/delete_result', methods=['POST'])
def delete_result():
    id = request.form['id_field']
    purpose = request.form['purpose']
    entry = Entry.query.filter(Entry.id == id).first()
    if purpose == 'delete':
        db.session.delete(entry)
        db.session.commit()
        message = f"The entry {entry.tst1} has been deleted from the database."
        return render_template('result.html', message=message)


# +++++++++++++++++++++++
# error routes
# https://flask.palletsprojects.com/en/1.1.x/patterns/apierrors/#registering-an-error-handler


@app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "error.html",
            pagetitle="404 Error - Page Not Found",
            pageheading="Page not found (Error 404)",
            error=e,
        ),
        404,
    )


@app.errorhandler(405)
def form_not_posted(e):
    return (
        render_template(
            "error.html",
            pagetitle="405 Error - Form Not Submitted",
            pageheading="The form was not submitted (Error 405)",
            error=e,
        ),
        405,
    )


@app.errorhandler(500)
def internal_server_error(e):
    return (
        render_template(
            "error.html",
            pagetitle="500 Error - Internal Server Error",
            pageheading="Internal server error (500)",
            error=e,
        ),
        500,
    )


# +++++++++++++++++++++++

if __name__ == "__main__":
    app.run(debug=True)
