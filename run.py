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
    parser.add_argument('--host',
                        type=str,
                        default='0.0.0.0',
                        help='Sets the host on which the app is to be run')
    parser.add_argument('--port',
                        type=int,
                        default=5000,
                        help='Sets the port on which the app is to be run')
    parser.add_argument('--debug',
                        action='store_true',
                        help='Run in debug mode')

    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = get_args()
    app.run(host=args.host, port=args.port, debug=args.debug)
