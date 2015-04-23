from a10sdk.common.A10BaseClass import A10BaseClass


class Udp(A10BaseClass):
    
    """Class Description::
    UDP type.

    Class udp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param udp: {"default": 0, "optional": true, "type": "number", "description": "UDP type", "format": "flag"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param udp_port: {"description": "Specify UDP port (Specify port number)", "format": "number", "type": "number", "maximum": 65534, "minimum": 1, "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/health/monitor/{name}/method/udp`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "udp"
        self.a10_url="/axapi/v3/health/monitor/{name}/method/udp"
        self.DeviceProxy = ""
        self.udp = ""
        self.uuid = ""
        self.udp_port = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


