import typing as t


# CHP_adapter ################################################################################################
class LoginException(AttributeError):
    def __init__(self, string_message: str):
        self.txt = string_message


##############################################################################################################



# ChpClient ##################################################################################################

class ChpError(RuntimeError):
    pass


class ApiConnectionError(ChpError):
    def __init__(self, msg: str, data: t.Optional[t.Union[t.List, t.Dict]] = None):
        self.txt = msg
        self.resp_data = data


class ApiRequestException(ChpError):
    def __init__(self, msg: str, data: t.Optional[t.Union[t.List, t.Dict]] = None):
        self.txt = msg
        self.resp_data = data

##############################################################################################################
