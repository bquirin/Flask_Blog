from flask import Flask, render_template  # url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'e213755c707768b0d9d77cae155265d8'

posts = [
    {
        'author': 'Brandon Vernon',
        'title': 'Blog Post 1',
        'content': 'First Post content',
        'date_posted': 'April 16, 2018'
    },
    {
        'author': 'Jane Vernon',
        'title': 'Blog Post 2',
        'content': 'Second Post content',
        'date_posted': 'April 17, 2018'
    }
]


@app.route("/")
@app.route("/home")
def hello():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template("register.html", title="Register", form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title="Login", form=form)


if __name__ == '__main__':
    app.run(debug=True)
# testing comment
