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
                'first_person_class': first_person_name.lower(),
                'second_person_class': second_person_name.lower(),
                'info_email': 'info@%sand%s.com' % (first_person_name.lower(), second_person_name.lower())
            })

            return render(
                template,
                context,
            )
        return renderer

    return func_wrapper


@app.route('/getting-married/the-day/')
@render_template('the-day')
def the_day():
    return {
        'section_header': 'The Day',
        'body_class': 'the-day',
    }


@app.route('/getting-married/getting-there/')
@render_template('getting-there')
def getting_there():
    return {
        'section_header': 'Getting There',
        'body_class': 'getting-there',
    }


@app.route('/getting-married/staying-there/')
@render_template('staying-there')
def staying_there():
    return {
        'section_header': 'Staying There',
        'body_class': 'staying-there',
    }


@app.route('/getting-married/photography/')
@render_template('photography')
def photography():
    return {
        'section_header': 'Photography',
        'body_class': 'photography',
    }


@app.route('/getting-married/gifts/')
@render_template('gifts')
def gifts():
    return {
        'section_header': 'Gifts',
        'body_class': 'gifts',
    }


@app.route('/getting-married/rsvp/')
@render_template('rsvp')
def rsvp():
    return {
        'section_header': 'RSVP',
        'body_class': 'rsvp',
    }


@app.route('/getting-married/')
@render_template('getting-married')
def getting_married():
    return {
        'show_event_information': True,
        'show_navigation': True,
        'section_header': 'Getting Married',
        'body_class': 'getting-married',
    }


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    http_server = WSGIServer(('0.0.0.0', port), app)
    http_server.serve_forever()
