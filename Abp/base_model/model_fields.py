'''
Created on Jan 5, 2012

@author: jiazou
'''

from django.db import models
import pickle
import base64

# Represents the price of a product
class TimePrice() :
    
    def __init__(self, time, local_currency_value, currency):
        self.time = time
        self.local_currency_value = local_currency_value
        self.currency = currency
    
class TimePriceField(models.Field):

    description = "A mapping from time to prices"

    __metaclass__ = models.SubfieldBase

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 104
        super(TimePriceField, self).__init__(*args, **kwargs)
        
    def db_type(self, connection):
        return 'timeprice'
    
    def to_python(self, value):
        if isinstance(value, TimePrice):
            return value
        value = pickle.loads(base64.b64decode(value))
        return value
    
    def get_db_prep_value(self, value):
        if value is None: return
        return base64.b64encode(pickle.dumps(value))