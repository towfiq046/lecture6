import time
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)\

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/posts", methods=["POST"])    # can access via ajax or http request
def posts():

    # provide argument to the load function for http XMLHttpRequest.
    start = int(request.form.get("start") or 0)     # start point.
    end = int(request.form.get("end") or (start + 9))   #end point.

    # generate fake posts. as db is not connected.
    data = []   # posts as list of array. used in js load function.
    for i in range(start, end + 1):
        data.append(f"Post #{i}")

    # fake delay of response.
    time.sleep(1)

    # return list of posts.
    return jsonify(data)    # in js load function.
