import os
import gevent
import gevent.monkey
import functools
import random

from gevent.pywsgi import WSGIServer
gevent.monkey.patch_all()

from pystache.loader import Loader
from pystache import render

from flask import Flask, redirect

app = Flask(__name__)
app.debug = True
loader = Loader()


@app.route('/')
def index():
    return redirect('/getting-married/')


def render_template(section_name):
    template = loader.load_name('templates/%s' % section_name)

    def func_wrapper(func):
        @functools.wraps(func)
        def renderer():
            context = func()

            context.update({
                'body_class': section_name,
                'body_theme_class': random.choice([
                    'evil-dead',
                    'reservoir-troopers',
                    'axe-cop-star-wars',
                    'bohnanza',
                ]),
            })

            return render(
                template,
                context,
            )
        return renderer

    return func_wrapper


@app.route('/getting-married/join-us/')
@render_template('join-us')
def join_us():
    return {}


@app.route('/getting-married/the-shindig/')
@render_template('the-shindig')
def the_shindig():
    return {}


@app.route('/getting-married/costume/')
@render_template('costume')
def costume():
    return {}


@app.route('/getting-married/venue/')
@render_template('venue')
def venue():
    return {}


@app.route('/getting-married/accommodation/')
@render_template('accommodation')
def accommodation():
    return {}


@app.route('/getting-married/photography/')
@render_template('photography')
def photography():
    return {}


@app.route('/getting-married/gifts/')
@render_template('gifts')
def gifts():
    return {}


@app.route('/getting-married/contact/')
@render_template('contact')
def contact():
    return {}


@app.route('/getting-married/')
@render_template('getting-married')
def getting_married():
    return {}


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    http_server = WSGIServer(('0.0.0.0', port), app)
    http_server.serve_forever()
