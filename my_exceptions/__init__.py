
class BaseException(Exception):
    def __init__(self,error_msg):
        self.error_msg=error_msg


class NotFoundError(BaseException):
    """404 error"""
    pass
