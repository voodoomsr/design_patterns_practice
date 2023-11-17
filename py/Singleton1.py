class Singleton:
    instance = None

    @classmethod
    def getInstance(cls):
        if not cls.instance:
            cls.instance = cls()
        return cls.instance
