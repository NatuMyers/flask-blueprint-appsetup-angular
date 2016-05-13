__author__ = 'danielqueiroz'

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound


deceptron = Blueprint('deceptron', __name__,
                        template_folder='templates')


@deceptron.route('/', defaults={'page': 'index'})
@deceptron.route('/<page>')
def show(page):
    try:
        return render_template('pages/%s.html' % page)
    except TemplateNotFound:
        abort(404)