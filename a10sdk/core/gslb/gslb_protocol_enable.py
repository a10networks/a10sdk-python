from a10sdk.common.A10BaseClass import A10BaseClass


class Enable(A10BaseClass):
    
    """Class Description::
    Enable/Disable GSLB Message Protocol.

    Class enable supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param type: {"optional": false, "enum": ["controller", "device"], "type": "string", "description": "'controller': Enable/Disable GSLB protocol as GSLB controller; 'device': Enable/Disable GSLB protocol as site device; ", "format": "enum"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/protocol/enable/{type}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "type"]

        self.b_key = "enable"
        self.a10_url="/axapi/v3/gslb/protocol/enable/{type}"
        self.DeviceProxy = ""
        self.A10WW_type = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


