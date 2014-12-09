from a10sdk.common.A10BaseClass import A10BaseClass


class TacacsServer(A10BaseClass):
    
    """Class Description::
    Configure TACACS+ servers.

    Class tacacs-server supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param interval: {"description": "The moniter interval in seconds (default 60)", "format": "number", "default": 60, "optional": true, "maximum": 120, "minimum": 1, "type": "number"}
    :param monitor: {"default": 0, "optional": true, "type": "number", "description": "Configure TACACS+ servers", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/tacacs-server`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "tacacs-server"
        self.a10_url="/axapi/v3/tacacs-server"
        self.DeviceProxy = ""
        self.host = {}
        self.interval = ""
        self.monitor = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


