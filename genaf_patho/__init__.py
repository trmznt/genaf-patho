from pyramid.config import Configurator

from rhombus.lib.utils import set_dbhandler_class
from genaf_patho.models import handler

def includeme( config ):

	# this will be included by Rhombus mechanism

	print('genaf-patho includeme()')


set_dbhandler_class( handler.DBHandler )