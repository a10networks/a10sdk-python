from a10sdk.common.A10BaseClass import A10BaseClass


class AutoMap(A10BaseClass):
    
    """Class Description::
    Auto Mapping Options.

    Class auto-map supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param all: {"description": "All modules", "format": "flag", "default": 0, "optional": true, "not": "module-type", "type": "number"}
    :param module_disable: {"default": 0, "optional": true, "type": "number", "description": "Specify Disable Auto Map Module", "format": "flag"}
    :param module_type: {"not": "all", "optional": true, "enum": ["slb-virtual-server", "slb-device", "slb-server", "gslb-service-ip", "gslb-site", "gslb-group", "hostname"], "type": "string", "format": "enum-list"}
    :param ttl: {"description": "Specify Auto Map TTL (TTL, default is 300)", "format": "number", "default": 300, "optional": true, "maximum": 65535, "minimum": 1, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/policy/{name}/auto-map`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "auto-map"
        self.a10_url="/axapi/v3/gslb/policy/{name}/auto-map"
        self.DeviceProxy = ""
        self.uuid = ""
        self.A10WW_all = ""
        self.module_disable = ""
        self.module_type = ""
        self.ttl = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


