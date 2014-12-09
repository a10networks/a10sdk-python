from a10sdk.common.A10BaseClass import A10BaseClass


class Poap(A10BaseClass):
    
    """    :param action: {"optional": true, "enum": ["enable", "disable"], "type": "string", "description": "'enable': Enable POAP mode; 'disable': Disable POAP mode; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Set POAP; when next boot, if startup-config is empty, system will enter POAP Mode.

    Class poap supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/poap`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "poap"
        self.a10_url="/axapi/v3/poap"
        self.DeviceProxy = ""
        self.action = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


