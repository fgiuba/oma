#!/usr/bin/env python

from flask import Flask, jsonify


app = Flask('MyApp')
server_bind = '0.0.0.0'
server_port = 12345
max_connections = 1000

# SSL/TLS params (recommended, but optional)
ssl_certificate = None
ssl_key = None


@app.route('/hello/<string:name>', methods=['GET'])
def hello(name):
    """
    ************************
    * Write your API here! *
    ************************
    """
    return jsonify('hello {}!'.format(name))


if __name__ == '__main__':

    from gevent.pywsgi import WSGIServer

    config = {
        'listener': (server_bind, server_port),
        'application': app,
        'spawn': max_connections,
    }
    if ssl_certificate:
        config['certfile'] = ssl_certificate
    if ssl_key:
        config['keyfile'] = ssl_key

    http_server = WSGIServer(**config)
    http_server.serve_forever()
