from a10sdk.common.A10BaseClass import A10BaseClass


class Debug(A10BaseClass):
    
    """    :param info: {"default": 0, "optional": true, "type": "number", "description": "Information component", "format": "flag"}
    :param daemon: {"default": 0, "optional": true, "type": "number", "description": "Daemon component", "format": "flag"}
    :param vblade: {"default": 0, "optional": true, "type": "number", "description": "vBlade component", "format": "flag"}
    :param election: {"default": 0, "optional": true, "type": "number", "description": "Election component", "format": "flag"}
    :param vmaster: {"default": 0, "optional": true, "type": "number", "description": "vMaster component", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    VCS debug.

    Class debug supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/vcs/debug`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "debug"
        self.a10_url="/axapi/v3/vcs/debug"
        self.DeviceProxy = ""
        self.info = ""
        self.daemon = ""
        self.vblade = ""
        self.election = ""
        self.vmaster = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


