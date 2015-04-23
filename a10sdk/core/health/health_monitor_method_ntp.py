from a10sdk.common.A10BaseClass import A10BaseClass


class Ntp(A10BaseClass):
    
    """Class Description::
    NTP type.

    Class ntp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ntp: {"default": 0, "optional": true, "type": "number", "description": "NTP type", "format": "flag"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param ntp_port: {"description": "Specify the NTP port, default is 123 (Port Number (default 123))", "format": "number", "default": 123, "optional": true, "maximum": 65534, "minimum": 1, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/health/monitor/{name}/method/ntp`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "ntp"
        self.a10_url="/axapi/v3/health/monitor/{name}/method/ntp"
        self.DeviceProxy = ""
        self.ntp = ""
        self.uuid = ""
        self.ntp_port = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


