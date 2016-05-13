from flask import Flask




app = Flask(__name__)

from home.home import home
app.register_blueprint(home)
app.register_blueprint(home, url_prefix='/pages')

from deceptron.deceptron import deceptron
app.register_blueprint(deceptron)
app.register_blueprint(deceptron, url_prefix='/pages')


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True) #or you could keep it empty
