class MyBaseException(Exception):
    def __init__(self, code = 500,msg=''):
        super().__init__()
        self.code = code
        self.msg = msg