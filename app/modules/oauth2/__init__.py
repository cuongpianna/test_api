from flask import Blueprint


bp = Blueprint('oauth2', __name__)
from app.modules.oauth2 import views
