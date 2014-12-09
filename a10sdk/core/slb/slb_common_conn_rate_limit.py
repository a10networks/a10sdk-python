from a10sdk.common.A10BaseClass import A10BaseClass


class ConnRateLimit(A10BaseClass):
    
    """Class Description::
    Set rate limiting on virtual ports.

    Class conn-rate-limit supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param src_ip_list: {"minItems": 1, "items": {"type": "src-ip"}, "uniqueItems": true, "array": [{"required": ["protocol"], "properties": {"protocol": {"optional": false, "enum": ["tcp", "udp"], "type": "string", "description": "'tcp': Set TCP connection rate limit; 'udp': Set UDP packet rate limit; ", "format": "enum"}, "log": {"default": 0, "optional": true, "type": "number", "description": "Send log if threshold exceeded", "format": "flag"}, "lock-out": {"description": "Set lockout period in seconds if threshold exceeded", "format": "number", "type": "number", "maximum": 3600, "minimum": 1, "optional": true}, "limit": {"description": "Set max packets per period", "format": "number", "type": "number", "maximum": 1000000, "minimum": 1, "optional": true}, "exceed-action": {"default": 0, "optional": true, "type": "number", "description": "Set action if threshold exceeded", "format": "flag"}, "shared": {"default": 0, "optional": true, "type": "number", "description": "Set threshold shared amongst all virtual ports", "format": "flag"}, "limit-period": {"optional": true, "enum": ["100", "1000"], "type": "string", "description": "'100': 100 ms; '1000': 1000 ms; ", "format": "enum"}}}], "type": "array", "$ref": "/axapi/v3/slb/common/conn-rate-limit/src-ip/{protocol}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/common/conn-rate-limit`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "conn-rate-limit"
        self.a10_url="/axapi/v3/slb/common/conn-rate-limit"
        self.DeviceProxy = ""
        self.src_ip_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


