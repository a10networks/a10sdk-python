from a10sdk.common.A10BaseClass import A10BaseClass


class SrcIp(A10BaseClass):
    
    """Class Description::
    Set connection limit based on source IP address.

    Class src-ip supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param protocol: {"optional": false, "enum": ["tcp", "udp"], "type": "string", "description": "'tcp': Set TCP connection rate limit; 'udp': Set UDP packet rate limit; ", "format": "enum"}
    :param log: {"default": 0, "optional": true, "type": "number", "description": "Send log if threshold exceeded", "format": "flag"}
    :param lock_out: {"description": "Set lockout period in seconds if threshold exceeded", "format": "number", "type": "number", "maximum": 3600, "minimum": 1, "optional": true}
    :param limit: {"description": "Set max packets per period", "format": "number", "type": "number", "maximum": 1000000, "minimum": 1, "optional": true}
    :param exceed_action: {"default": 0, "optional": true, "type": "number", "description": "Set action if threshold exceeded", "format": "flag"}
    :param shared: {"default": 0, "optional": true, "type": "number", "description": "Set threshold shared amongst all virtual ports", "format": "flag"}
    :param limit_period: {"optional": true, "enum": ["100", "1000"], "type": "string", "description": "'100': 100 ms; '1000': 1000 ms; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/common/conn-rate-limit/src-ip/{protocol}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "protocol"]

        self.b_key = "src-ip"
        self.a10_url="/axapi/v3/slb/common/conn-rate-limit/src-ip/{protocol}"
        self.DeviceProxy = ""
        self.protocol = ""
        self.log = ""
        self.lock_out = ""
        self.limit = ""
        self.exceed_action = ""
        self.shared = ""
        self.limit_period = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


