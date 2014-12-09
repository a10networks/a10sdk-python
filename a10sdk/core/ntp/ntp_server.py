from a10sdk.common.A10BaseClass import A10BaseClass


class Server(A10BaseClass):
    
    """Class Description::
    Set NTP time server.

    Class server supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param hostname_list: {"minItems": 1, "items": {"type": "hostname"}, "uniqueItems": true, "array": [{"required": ["host-servername"], "properties": {"action": {"description": "'enable': Enable this NTP server; 'disable': Disable this NTP server; ", "format": "enum", "default": "enable", "type": "string", "enum": ["enable", "disable"], "optional": true}, "prefer": {"default": 0, "optional": true, "type": "number", "description": "Set this NTP server as preferred", "format": "flag"}, "host-servername": {"description": "IPV4 address, IPV6 address or host name of NTP server(string1~63)", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}, "key": {"description": "Use trusted key to authenticate this NTP server (The trusted key number to use)", "format": "number", "optional": true, "maximum": 65535, "minimum": 1, "type": "number", "$ref": "/axapi/v3/ntp/trusted-key"}}}], "type": "array", "$ref": "/axapi/v3/ntp/server/hostname/{host-servername}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ntp/server`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "server"
        self.a10_url="/axapi/v3/ntp/server"
        self.DeviceProxy = ""
        self.hostname_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


