from a10sdk.common.A10BaseClass import A10BaseClass


class Protocol(A10BaseClass):
    
    """Class Description::
    Specify GSLB Message Protocol parameters.

    Class protocol supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param use_mgmt_port: {"default": 0, "optional": true, "type": "number", "description": "Use management port for connections", "format": "flag"}
    :param ping_site: {"description": "name of site or ip address to ping", "format": "string", "minLength": 1, "optional": true, "maxLength": 128, "type": "string"}
    :param auto_detect: {"default": 0, "optional": true, "type": "number", "description": "Automatically detect SLB Config", "format": "flag"}
    :param enable_list: {"minItems": 1, "items": {"type": "enable"}, "uniqueItems": true, "array": [{"required": ["type"], "properties": {"type": {"optional": false, "enum": ["controller", "device"], "type": "string", "description": "'controller': Enable/Disable GSLB protocol as GSLB controller; 'device': Enable/Disable GSLB protocol as site device; ", "format": "enum"}}}], "type": "array", "$ref": "/axapi/v3/gslb/protocol/enable/{type}"}
    :param status_interval: {"description": "Specify GSLB Message Protocol update period (The GSLB Protocol update interval (seconds), default is 30)", "format": "number", "type": "number", "maximum": 1800, "minimum": 1, "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/protocol`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "protocol"
        self.a10_url="/axapi/v3/gslb/protocol"
        self.DeviceProxy = ""
        self.use_mgmt_port = ""
        self.limit = {}
        self.ping_site = ""
        self.auto_detect = ""
        self.enable_list = []
        self.status_interval = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


