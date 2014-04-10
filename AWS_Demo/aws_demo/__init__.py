from pyramid.config import Configurator
from pyramid.renderers import JSON
from pyramid_beaker import session_factory_from_settings
from adapter import new_datetime_adapter
from pyramid_mailer.mailer import Mailer

import datetime


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application. """


    config = Configurator(settings=settings)

    #set up beaker session
    session_factory = session_factory_from_settings(settings)
    config.set_session_factory(session_factory)


    # add security tweens
 #   config.add_tween('aws_demo.tweens.clickjacking.clickjacking_factory')
 #   config.add_tween('aws_demo.tweens.secure_headers.secure_headers_factory')

    config.registry['mailer'] = Mailer.from_settings(settings=settings)

    # modify the built in json renderer to serialize dates properly
    json_date_renderer = JSON()
    json_date_renderer.add_adapter(datetime.datetime, new_datetime_adapter)
    
    # set .html renderer to allow mako templating
    config.add_renderer('.html', 'pyramid.mako_templating.renderer_factory')
    config.add_renderer('.htm', 'pyramid.mako_templating.renderer_factory')
    config.add_renderer('json', json_date_renderer)
    
    config.add_static_view('static', 'static', cache_max_age=3600)

    # login / registration
    config.add_route('index_view', '/')


    config.scan()
    return config.make_wsgi_app()
