class SingletonMeta(type):
   # """The singleton class template is a feature of Python"""
    _instances = {}
    def __call__(self, *args, **kwargs):
        #""" """
        if self not in self._instances:
            instance = super().__call__(*args, **kwargs)
            self._instances[self] = instance
        return self._instances[self]