class Budget(object):
    def __init__(self, value):
        self.__value = value
    
    # a budget can't variable, must be have a fixed value, so we use property decorator
    @property
    def value(self):
        return self.__value
