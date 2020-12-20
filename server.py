from flask import Flask, render_template, request, redirect, url_for
import csv
app = Flask(__name__)
print(__name__)

@app.route('/')
def index_page(username=None):
    return render_template('index.html')

@app.route('/thankyou')
def thanks_page(username=None):
    return render_template('thanks.html')

@app.route('/blog')
def blog():
    return 'This is my blog'


@app.route('/blog/2020/dogs')
def catsblog():
    return 'This is my car'      


@app.route('/blog/2020/dogs/')
def dogsblog():
    return 'This is my dog'    

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email=data["email"]
        subject=data["subject"]
        message=data["message"]
        file=database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email=data["email"]
        subject=data["subject"]
        message=data["message"]
        csv_writer=csv.writer(database2, delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL) 
        csv_writer.writerow([email,subject,message])       

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    error = None
    """ if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password' """
    if request.method=='POST':
        data= request.form.to_dict() 
        #print(data) 
        write_to_file(data)    
        write_to_csv(data)  
        #return "Form submitted successfully"
        return redirect('/thankyou')
    else:
        return "Something went wrong, try again please!"    
    # the code below is executed if the request method
    # was GET or the credentials were invalid    
    #return render_template('login.html', error=error)