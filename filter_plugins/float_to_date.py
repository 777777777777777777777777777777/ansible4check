import datetime

def float_to_date(arg):
    return datetime.datetime.utcfromtimestamp(arg)

class FilterModule(object):
    def filters(self):
        return { 'float_to_date': float_to_date }
