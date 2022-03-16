from flask import Blueprint, jsonify,request
from shorty.model.link_shorter_model import ShorthenLinkSchema
from shorty.service.link_shorter_service import shortLink


api = Blueprint('api', __name__)


@api.route('/shortlinks', methods=['POST'])
def create_shortlink():
    shortenLink = ShorthenLinkSchema().load(request.get_json())
    result = shortLink(shortenLink)
    return jsonify({"url":shortenLink["url"],"link":result})