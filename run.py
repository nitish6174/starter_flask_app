# External modules
import argparse
import sys
# Local modules
from flaskapp.app import app


def get_args():
    """
    Get command-line arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', action='store_true', help='Run in debug mode')
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = get_args()
    app.run(host='0.0.0.0', debug=args.debug)
