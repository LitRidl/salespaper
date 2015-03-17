# -*- coding: utf-8 -*-

from app import app
import argparse

app.config.from_object('config.DevelopmentConfig')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("--host", help="host", default=app.config['HOST'])
    parser.add_argument("--port", help="port", type=int, default=app.config['PORT'])
    parser.add_argument("--debug", help="debug", action='store_true', default=app.config['DEBUG'])

    args = parser.parse_args()

    app.run(host=args.host, port=args.port, debug=args.debug)
