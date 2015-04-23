from a10sdk.common.A10BaseClass import A10BaseClass


class Tunnel(A10BaseClass):
    
    """Class Description::
    Tunnel interface.

    Class tunnel supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ifnum: {"description": "Tunnel interface number", "format": "number", "type": "number", "maximum": 128, "minimum": 1, "optional": false}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/interface/tunnel/{ifnum}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "ifnum"]

        self.b_key = "tunnel"
        self.a10_url="/axapi/v3/interface/tunnel/{ifnum}"
        self.DeviceProxy = ""
        self.ip = {}
        self.ifnum = ""
        self.uuid = ""
        self.ipv6 = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


