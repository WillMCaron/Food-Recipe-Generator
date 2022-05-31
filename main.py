from flask import Flask, render_template, request, redirect, url_for
import sys
sys.path.append('/home/runner/MOMTRY/sorting')
from final import *
app = Flask('Food App')

username_curr = None
inputdata = None

@app.route("/")
# function that loads the web page files, name is based on purpose
def index():
    # loads the webpage from template, returns to flask
    return render_template('index.html')


@app.route("/login", methods=["POST","GET"])
def login_signup():
  if request.method == "POST":
    if request.form["submit"] == "login":
      return redirect(url_for('LOGIN'))
    elif request.form["submit"] == 'signup':
      return redirect(url_for('SIGNUP'))
  return render_template('login_signup.html')


@app.route('/LOGIN', methods=["POST","GET"])
def LOGIN():
  global username_curr
  username = request.form.get("username")
  password = request.form.get("password")
  users = []
  with open("users.txt","r") as f:
    contents = f.read()
    contents = contents.split("\n")
    for line in range(0,len(contents)-1,2):
      users.append([contents[line],contents[line+1]])
    print(users)
  if request.method == "POST":
    username = username.lower()
    password = password.lower()
    if [username,password] not in users:
      return render_template('signup.html', warning = "Account Doesn't Exists")
      username_curr = None
    elif request.form['submit'] == 'submit' and username and password:
      username_curr = username
      return redirect(url_for('admin'))
  username_curr = None
  return render_template('login.html', warning = " ")


@app.route('/SIGNUP', methods=["POST","GET"])
def SIGNUP():
  username = request.form.get("username")
  password = request.form.get("password")
  users = []
  with open("users.txt","r") as f:
    contents = f.read()
    contents = contents.split("\n")
    for line in range(0,len(contents)-1,2):
      users.append([contents[line]])
    print(users)
  if request.method == "POST":
    username = username.lower()
    password = password.lower()
    if [username] in users:
      return render_template('signup.html', warning = "Account Already Exists")
    elif request.form['submit'] == 'submit' and username and password:
      with open('users.txt','a') as f:
        f.write(username+"\n"+password+'\n')
      return redirect(url_for('LOGIN'))
  return render_template('signup.html', warning = " ")
  
  
# secondary route
@app.route('/admin', methods=['POST','GET'])
def admin():
    global username_curr
    global inputdata
    # get the data values from the form
    name = username_curr
    food = request.form.get("values")
    # get the current list values
    with open("list.txt","r") as f:
        contents = f.read()
        contents = contents.replace("\n","<br>")
    if username_curr:
      contents = contents.split("<br>")
      #print(contents)
      contents = contents[:len(contents)-1]
      #print(contents)
      user_contents = []
      for item in contents:
        if item.partition(":")[0] == name:
          user_contents.append(item)
      print(user_contents)
      inputdata = user_contents
      string = ""
      for item in user_contents:
        string += str(item)+"<br>"
      contents = string
    # if receiving data and data has been received
    if request.method == "POST":
        if request.form['submit'] == 'submit' and food:# and amounts and units:
            # write new data to food file
            with open("list.txt","a") as f:
                f.write(str(name)+": "+str(food)+"\n")
                # reload page
                return redirect(url_for('admin'))
        elif request.form['submit'] == 'reset':
            with open("list.txt","r") as f:
              contents = f.read()
            contents = contents.split("\n")
            contents = contents[:len(contents)-1]
            print(contents)
            nonuser_contents = []
            for item in contents:
              if item.partition(":")[0] != name:
                nonuser_contents.append(item)
            string = ""
            for item in nonuser_contents:
              string += str(item)+"\n"
            contents = string
            with open("list.txt","w") as f:
              f.write(contents)
            return redirect(url_for('admin'))
        elif request.form['submit'] == 'cont':
          return redirect(url_for('final'))
            
    # pass the results from list gather (GET) to form
    return render_template('admin.html', stuff=contents)

@app.route('/final',methods = ['POST','GET'])
def final():
  global username_curr
  """
  global inputdata
  if len(inputdata) < 4:
    stuff = eliminate2(username_curr)
    print("Little data, going extermination")
  elif len(inputdata) < 9:
    stuff = eliminate3(username_curr)
    print("Some data, going reduction")
  else:
    stuff = eliminate1(username_curr)
    print("Data galore, going elimination")
  """
  stuff = eliminate(username_curr)
  return render_template('recipe.html', stuff = stuff)

# if run from main file
if __name__ == '__main__':
    # port reuse prevention
    port = 5000 
    print(port)
    url = "http://127.0.0.1:{0}".format(port)
    print(url)
    # run the app
    app.run(debug=True, host='0.0.0.0', port=str(port))
