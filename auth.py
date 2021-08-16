from replit import db # importing the database
from encoder import to_json
from flask import Flask, render_template, redirect
app = Flask('app', template_folder = "templates")

def process(data):
  d = data.split("_")
  res = {}
  for i in d:
    res[i.split("=")[0]] = eval(i.split("=")[1])
  return res

@app.route('/get_user_data/<user>')
def hello_world(user):
  try:
    return render_template("get.html", name = user, json_data = db[user])
  except:
    return "Invalid!"

@app.route("/register/<name>/<age>/<extra_data>")
def register(name, age, extra_data):
  db[name] = to_json({
    "name": name,
    "age": age,
    "extra_data": process(extra_data)
  })
  return redirect("/")

app.run(host='0.0.0.0', port=8080)