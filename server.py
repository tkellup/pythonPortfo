# import the Flask class
from flask import Flask, render_template, request, redirect
import csv

# create an instance of this class where __name__ is
# the name of the application's module or package.
app = Flask(__name__)

# the route() tells Flask what URL should trigger our function
@app.route("/index.html")
@app.route("/")
def my_home():
    return render_template('index.html')

# dynamically render the pages
@app.route("/<string:page_name>")
def html_page(page_name):
     return render_template(page_name)

# tedious way of creating endpoints
# @app.route("/about.html")
# def about():
#     return render_template('about.html')
#
# @app.route("/contact.html")
# def contact():
#     return render_template('contact.html')
#
# @app.route("/works.html")
# def work():
#     return render_template('works.html')

# send data to a text file
def write_to_file(data):
    email = data['email']
    subject = data['subject']
    message = data['message']
    with open('database.txt', mode='a',newline='') as my_file:
        file = my_file.write(f"\n{email},{subject},{message}")

# send data to a csv file
def write_to_csv(data):
    email = data['email']
    subject = data['subject']
    message = data['message']
    with open('database.csv', mode='a',newline='') as database:
        # fieldnames= ['email','subject','message']
        # csv_writer = csv.DictWriter(database,fieldnames=fieldnames)
        # csv_writer.writeheader()
        csv_writer = csv.writer(database,delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data= request.form.to_dict() # converts form data into a dictionary
            #print(data)
            #write_to_file(data)
            write_to_csv(data)
            return redirect('thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong. Try again!'

# To run this file in debug mode use: flask --app server run --debug
