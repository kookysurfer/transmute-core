from abc import ABCMeta, abstractmethod


class ObjectSerializer(object):
    """
    The object serializer is responsible for converting objects to and
    from basic data types. Basic data types are serializable to and
    from most common data representation languages (such as yaml or json)

    Basic data types are:

    - str (basestring in Python2, str in Python3)
    - float
    - int
    - None
    - dict
    - list

    The serializer decides what it can and can not serialize, and should raise
    an exception when a type it can not serialize is passed.

    `SchematicsSerializer` is the default implementation used.
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def load(self, model, value):
        """
        load the value from a basic datatype, into a class.

        if the model or value is not valid, raise a SerializationException
        """

    @abstractmethod
    def dump(self, model, value):
        """
        dump the value from a class to a basic datatype.

        if the model or value is not valid, raise a SerializationException
        """