"""Support encoding of date and datetime objects to/from JSON."""

import datetime
import json


class _EncodedTypes(object):
    DATETIME = 'datetime.datetime'
    DATE = 'datetime.date'


class _DateTimeDecoder(json.JSONDecoder):

    def __init__(self, *args, **kargs):
        json.JSONDecoder.__init__(
            self, object_hook=self._dict_to_object, *args, **kargs)

    def _dict_to_object(self, dict_obj):
        if '__type__' not in dict_obj:
            return dict_obj
        objtype = dict_obj.pop('__type__')
        try:
            if objtype == _EncodedTypes.DATETIME:
                return datetime.datetime(**dict_obj)
            if objtype == _EncodedTypes.DATE:
                return datetime.date(**dict_obj)
        except BaseException:
            dict_obj['__type__'] = objtype
            return dict_obj


class _DateTimeEncoder(json.JSONEncoder):

    def default(self, obj): # pylint: disable=E0202
        if isinstance(obj, datetime.datetime):
            return {
                '__type__' : _EncodedTypes.DATETIME,
                'year' : obj.year,
                'month' : obj.month,
                'day' : obj.day,
                'hour' : obj.hour,
                'minute' : obj.minute,
                'second' : obj.second,
                'microsecond' : obj.microsecond,
            }
        if isinstance(obj, datetime.date):
            return {
                '__type__' : _EncodedTypes.DATE,
                'year' : obj.year,
                'month' : obj.month,
                'day' : obj.day
            }
        else:
            return json.JSONEncoder.default(self, obj)


def load(fp, **kwargs): # pylint: disable=C0103, C0111
    load.__doc__ = json.load.__doc__
    if 'cls' in kwargs:
        kwargs.pop('cls')
    return json.load(fp, cls=_DateTimeDecoder, **kwargs)


def dump(obj, fp, **kwargs): # pylint: disable=C0103, C0111
    if 'cls' in kwargs:
        kwargs.pop('cls')
    json.dump(obj, fp, cls=_DateTimeEncoder, **kwargs)
