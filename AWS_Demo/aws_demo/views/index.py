from pyramid.view import view_config
from pyramid.response import Response
from pyramid.httpexceptions import HTTPFound
from MySQLdb.cursors import DictCursor
import json, mimetypes
from recaptcha.client import captcha
from pyramid_mailer.mailer import Mailer
from pyramid_mailer.message import Message
from Crypto.Hash import SHA256
import ftplib as ftp

@view_config(route_name='index_view', renderer='index.html')
def index_view(request):
    """ The index view callable. """


    return {}

