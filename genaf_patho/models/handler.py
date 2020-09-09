
from rhombus.lib.utils import get_dbhandler_class, cerr
from genaf_patho.models.dbschema import PathoSample

class DBHandler(get_dbhandler_class()):

    Sample = PathoSample


    def initdb(self, create_table=True, init_data=True, rootpasswd=None):
        """ initialize database """
        super().initdb(create_table, init_data, rootpasswd)
        if init_data:
            from .setup import setup
            setup(self)
            cerr('[genaf-patho] Database has been initialized')

DBHandler.Batch.set_sample_class(PathoSample)
