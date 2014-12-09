from a10sdk.common.A10BaseClass import A10BaseClass


class Audit(A10BaseClass):
    
    """Class Description::
    Configure audit.

    Class audit supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param privilege: {"default": 0, "optional": true, "type": "number", "description": "Enable privilege command for audit service", "format": "flag"}
    :param enable: {"default": 0, "optional": true, "type": "number", "description": "Enable audit service", "format": "flag"}
    :param size: {"description": "Config audit buffer size, default is 20,000 (Audit buffer size(in items), default is 20,000)", "format": "number", "type": "number", "maximum": 30000, "minimum": 1000, "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/audit`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "audit"
        self.a10_url="/axapi/v3/audit"
        self.DeviceProxy = ""
        self.privilege = ""
        self.enable = ""
        self.size = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


