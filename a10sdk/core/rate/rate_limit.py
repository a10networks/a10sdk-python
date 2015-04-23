from a10sdk.common.A10BaseClass import A10BaseClass


class RateLimit(A10BaseClass):
    
    """    :param maxPktNum: {"description": "Max number of packets", "format": "number", "default": 10000, "optional": true, "maximum": 100000, "minimum": 1000, "type": "number"}
    :param rl_type: {"optional": true, "enum": ["ctrl"], "type": "string", "description": "'ctrl': The max number of packets that can be sent to kernel in 100ms; ", "format": "enum"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Rate limit configuration.

    Class rate-limit supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/rate-limit`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "rate-limit"
        self.a10_url="/axapi/v3/rate-limit"
        self.DeviceProxy = ""
        self.maxPktNum = ""
        self.rl_type = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


