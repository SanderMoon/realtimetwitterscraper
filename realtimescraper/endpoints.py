from flask import Blueprint
from flask import request
from flask import abort
from views import view
from RealtimeScraper import RealtimeScraper


simple_endpoints = Blueprint('simple_page', __name__, template_folder='templates')


@simple_endpoints.route("/home")
def hello_world():
    return view.return_message()


@simple_endpoints.route("/changeHomeMessage", methods=['POST'])
def world_page():
    if not request.json or not 'message' in request.json:
        abort(400)
    view.change_message(request.json['message'])
    return 'succeeded'

@simple_endpoints.route("/startScrambler", methods=['GET'])
def start_scrambler():
    print("doing stuff")
    test = RealtimeScraper("crypto OR bitcoin OR BTC OR cryptocurrency OR ethereum OR ETH", 50)
    test.start_scrambler()
    return 'succeeded'

