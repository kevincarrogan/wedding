import os
import gevent
import gevent.monkey

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


def render_template(template_name):
    template = loader.load_name('templates/%s' % template_name)

    def func_wrapper(func):
        def renderer():
            context = func()

            return render(
                template,
                context,
            )
        return renderer

    return func_wrapper


@app.route('/getting-married/')
@render_template('getting-married')
def getting_married():
    return {}


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    http_server = WSGIServer(('0.0.0.0', port), app)
    http_server.serve_forever()
