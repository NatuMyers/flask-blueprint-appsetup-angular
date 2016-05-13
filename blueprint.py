from flask import Flask

from home.home import home


app = Flask(__name__)

app.register_blueprint(home)
app.register_blueprint(home, url_prefix='/pages')


from deceptron.deceptron import deceptron
app.register_blueprint(deceptron)
app.register_blueprint(deceptron, url_prefix='/pages')

if __name__ == '__main__':
    app.run()