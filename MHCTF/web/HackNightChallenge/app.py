from flask import Flask, make_response, request, session

app = Flask(__name__)
app.secret_key = b'\xaf\x1f\x8eTd|\xd2\xfa\xb9yYc'


@app.route('/')
def index():
    # BONUS flag in session cookie (decode on jwt.io)
    session["secret_flag"] = "mhctf{you_found_another_one!}"

    # Make response object
    resp = make_response()

    # Check if correct cookie was sent
    cookie = request.cookies.get("cookie")
    if cookie == "10":
        # Cookie value is correct, return flag
        resp.set_data('<h1>mhctf{you_found_the_flag!}</h1>')
        return resp

    # Set the cookie
    resp.set_cookie("cookie", "0")

    # Add the html to be displayed
    resp.set_data('<h1>Hello, World!</h1>')
    return resp
