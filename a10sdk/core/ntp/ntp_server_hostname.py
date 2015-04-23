from a10sdk.common.A10BaseClass import A10BaseClass


class Hostname(A10BaseClass):
    
    """Class Description::
    IPV4 address, IPV6 address or host name of NTP server.

    Class hostname supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param action: {"description": "'enable': Enable this NTP server; 'disable': Disable this NTP server; ", "format": "enum", "default": "enable", "type": "string", "enum": ["enable", "disable"], "optional": true}
    :param prefer: {"default": 0, "optional": true, "type": "number", "description": "Set this NTP server as preferred", "format": "flag"}
    :param host_servername: {"description": "IPV4 address, IPV6 address or host name of NTP server(string1~63)", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param key: {"description": "Use trusted key to authenticate this NTP server (The trusted key number to use)", "format": "number", "optional": true, "maximum": 65535, "minimum": 1, "type": "number", "$ref": "/axapi/v3/ntp/trusted-key"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ntp/server/hostname/{host_servername}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "host_servername"]

        self.b_key = "hostname"
        self.a10_url="/axapi/v3/ntp/server/hostname/{host_servername}"
        self.DeviceProxy = ""
        self.action = ""
        self.prefer = ""
        self.host_servername = ""
        self.uuid = ""
        self.key = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


