from a10sdk.common.A10BaseClass import A10BaseClass


class Enable(A10BaseClass):
    
    """Class Description::
    Enable SNMP service.

    Class enable supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param service: {"default": 0, "optional": true, "type": "number", "description": "Enable SNMP service", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/snmp-server/enable`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "enable"
        self.a10_url="/axapi/v3/snmp-server/enable"
        self.DeviceProxy = ""
        self.traps = {}
        self.service = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


