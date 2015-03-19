#!env/bin/python
# -*- coding: utf-8 -*-

from app import app, DEFAULT_CONFIG_CLASS
import argparse

DESCRIPTION = "Run-script & configuration chooser for Salespaper Flask application"

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=DESCRIPTION)

    parser.add_argument("--config", "-c", help="Launch with configuration from CONFIG_CLASS in ./config.py",
                        dest="config_class", type=str, default=DEFAULT_CONFIG_CLASS)
    args = parser.parse_args()

    try:
        pass # app.config.from_object('config.' + args.config_class)
    except ImportError:
        print "Configuration class " + args.config + " not found in ./config.py, aborting"
        exit(1)

    app.run(debug=app.config['DEBUG'], host=app.config['HOST'], port=app.config['PORT'])
