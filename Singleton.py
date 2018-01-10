#!/usr/bin/env/python

class Singleton(type):
    instance = None
    def __call__(cls, *args, **kargs):
        if not cls.instance:
            cls.instance = super(Singleton, cls).__call__(*args, **kargs)
        return cls.instance
