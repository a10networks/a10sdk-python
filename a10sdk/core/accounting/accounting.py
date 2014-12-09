from a10sdk.common.A10BaseClass import A10BaseClass


class Accounting(A10BaseClass):
    
    """Class Description::
    Configuration for accounting.

    Class accounting supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param debug: {"description": "Specify the debug level for accounting (Debug level for command accounting. bitwise OR of the following: 1(common), 2(packet),4(packet detail), 8(md5))", "format": "number", "type": "number", "maximum": 15, "minimum": 1, "optional": true}
    :param commands: {"description": "Enable level for commands accounting", "format": "number", "default": 0, "optional": true, "maximum": 15, "minimum": 0, "type": "number"}
    :param tacplus: {"default": 0, "optional": true, "type": "number", "description": "Use TACACS+ servers for accounting", "format": "flag"}
    :param stop_only: {"default": 0, "optional": true, "type": "number", "description": "Record stop when service terminates", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/accounting`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "accounting"
        self.a10_url="/axapi/v3/accounting"
        self.DeviceProxy = ""
        self.debug = ""
        self.commands = ""
        self.tacplus = ""
        self.stop_only = ""
        self.A10WW_exec = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


