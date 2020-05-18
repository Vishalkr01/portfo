from flask import Flask , render_template,request,redirect
import csv
app = Flask(__name__)
# set FLASK_APP=server.py this command for set serverApp
# set FLASK_ENV=development  for debugor mode on
# flash run   this command for run ther server
# @app.route('/')
# def hello_world():
#     return 'Hello, Vishal!'

@app.route('/')
def hello_world():
    return render_template('index.html')
@app.route('/<string:pagename>')
def html_page(pagename):
    return render_template(pagename)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_Form():
    if request.method=='POST':
        try:
            data=request.form.to_dict()
            wirte_data_incsv(data)
            return render_template('/thankyou.html')
        except:
            return 'did not save to datebase'
    else:
        return 'something went wrong try again!'

def wirte_data(data):

    try:
        with open('./database.txt',mode='a') as database:
            email=data['email']
            subject=data['subject']
            message=data['message']
            database.write(f'\n{email},{subject},{message}')
    except FileNotFoundError :
        print('file not found')


def wirte_data_incsv(data):

    try:
        with open('./database.csv',mode='a',newline='') as database1:
            email=data['email']
            subject=data['subject']
            message=data['message']
            csv_writer=csv.writer(database1,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow([email,subject,message])

    except (FileNotFoundError ,csv.Error) as e:
        print(e)


