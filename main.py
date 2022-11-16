import flask
import datetime
import os
import json
import geocoder

app = flask.Flask("heatmap")

admins = {
    "morgan": "password"
}

@app.route("/heatmap/")
def heatmap():
    UID = flask.request.args.get("UID")
    activity = flask.request.args.get("activity")
    ip = flask.request.remote_addr
    if not os.path.exists("clients/"):
        os.mkdir("clients/")
    with open("bought.json") as f:
        data = json.load(f)
    if not os.path.exists(f"clients/{UID}.json") and UID in data:
        with open(f"clients/{UID}.json", "w") as f:
            json.dump({}, f, indent=2)
    if UID in data:
        with open(f"clients/{UID}.json") as f:
            data = json.load(f)
        if ip not in data:
            with open(f"templates/{UID}.json", "r") as f:
                template = json.load(f)
            data[ip] = template
            data[ip]["country"] = geocoder.ipinfo(ip).country
        data[ip]["activity"][activity] += 1
        with open(f"clients/{UID}.json", "w") as f:
            json.dump(data, f, indent=2)
    return "done"

@app.route("/dump/")
def dump():
    UID = flask.request.args.get("UID")
    with open(f"clients/{UID}.json") as f:
        data = json.load(f)
    return flask.jsonify(data)

@app.route("/login/")
def login():
    flask.request.redirect("https://copperhead.000webhostapp.com/login.html")
    user = flask.request.args.get("user")
    password = flask.request.args.get("password")
    with open("logins.json", "r") as f:
        data = json.load(f)
    if user in data:
        if data[user]["password"] == password:
            return data[user]["UID"]
        else:
            return "invalid password"
    else:
        return "invalid username"

@app.route("/register/")
def register():
    admin = flask.request.args.get("admin")
    user = flask.request.args.get("user")
    password = flask.request.args.get("password")
    UID = flask.request.args.get("UID")
    with open("logins.json", "r") as f:
        data = json.load(f)
    if user in data:
        return "user exists already"
    else:
        if admin in admins:
            data[user] = {"password": password, "UID": UID}
    with open("logins.json", "w") as f:
        json.dump(data, f, indent=2)
    with open("bought.json", "r") as f:
        data = json.load(f)
    data[UID] = True
    with open("bought.json", "w") as f:
        json.dump(data, f, indent=2)
    return data[user]

app.run(host="0.0.0.0", port=5000)