from flask import Flask, flash, redirect, render_template, request, session
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = "4debug"
debug = DebugToolbarExtension(app)

# homepage
@app.route('/')
def index():
    """Show homepage"""

    return """
      <html>
        <body>
          <h1>I am the landing page</h1>
        </body>
      </html>
      """
# page
@app.route('/hello')
def say_hello():
    """Return simple "Hello" Greeting."""

    # html = "<html><body><h1>Hello</h1></body></html>"
    # return html
    flash("you are successfuly logged in")  

    return render_template("hello.html")

#request and term
@app.route("/search")
def search():
    """Handle GET requests like /search?term=fun"""

    term = request.args["term"]
    return f"<h1>Searching for {term}</h1>"


#POSTT
@app.route("/add-comment")
def add_comment_form():
    """Show form for adding a comment."""

    return """
      <form method="POST">
        <input name="comment">
        <button>Submit</button>
      </form>
      """

@app.route("/add-comment", methods=["POST"])
def add_comment():
    """Handle adding comment."""

    comment = request.form["comment"]

    # TODO: save that into a database!

    return f'<h1>Received "{comment}".</h1>'


#using ids
POSTS = {
  1: "Flask is pretty cool",
  2: "Python is neat-o"
}

@app.route('/post/<int:post_id>')
def show_post(post_id):
    """Show post with given integer id."""

    print("post_id is a ", type(post_id))

    post = POSTS[post_id]

    return f"<h1>Post #{post_id}</h1><p>{post}</p>"

#working??
@app.route('/greet')
def offer_greeting():
    """Give player compliment."""

    player = request.args["person"]
    # nice_thing = choice(COMPLIMENTS)
    nice_thing = "trsttttt"

    return render_template("compliment.html", 
                           name=player, 
                           compliment=nice_thing)

@app.route("/form")
def form_pre():
    """Show form for adding a comment."""

    return render_template("form.html")

@app.route("/form", methods=["POST"])
def form_after():
    """?"""

    return render_template("compliment.html")

#session
@app.route('/some-route')
def some_route():
    """Set fav_number in session."""

    session['fav_number'] = 42
    flash(f"Favorite number is {session['fav_number']}")
    flash("Favorite n}")

    return redirect("/hello")
