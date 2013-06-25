import os
import gevent
import gevent.monkey
import functools
import random

from gevent.pywsgi import WSGIServer
gevent.monkey.patch_all()

from pystache.loader import Loader
from pystache import render

from flask import Flask, redirect, request

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

            host = request.host

            if host.endswith('kevinandria.com'):
                first_person_name = 'Kevin'
                second_person_name = 'Ria'
            else:
                first_person_name = 'Ria'
                second_person_name = 'Kevin'

            context.update({
                'first_person_name': first_person_name,
                'second_person_name': second_person_name,
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


@app.route('/getting-married/the-day/')
@render_template('the-day')
def the_day():
    return {
        'byline': 'The Day',
    }


@app.route('/getting-married/the-shindig/')
@render_template('the-shindig')
def the_shindig():
    return {}


@app.route('/getting-married/costume/')
@render_template('costume')
def costume():
    return {}


@app.route('/getting-married/getting-there/')
@render_template('getting-there')
def getting_there():
    return {
        'byline': 'Getting There',
    }


@app.route('/getting-married/venue/')
@render_template('venue')
def venue():
    return {}


@app.route('/getting-married/staying-there/')
@render_template('staying-there')
def staying_there():
    return {
        'byline': 'Staying There',
    }

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
    return {
        'byline': 'Gifts',
    }


@app.route('/getting-married/contact/')
@render_template('contact')
def contact():
    return {}


@app.route('/getting-married/')
@render_template('getting-married')
def getting_married():
    return {
        'show_event_information': True,
        'show_navigation': True,
        'byline': 'Getting Married',
    }


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    http_server = WSGIServer(('0.0.0.0', port), app)
    http_server.serve_forever()
