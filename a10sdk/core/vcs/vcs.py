from a10sdk.common.A10BaseClass import A10BaseClass


class Vcs(A10BaseClass):
    
    """    :param device_list: {"minItems": 1, "items": {"type": "device"}, "uniqueItems": true, "array": [{"required": ["device"], "properties": {"management": {"default": 0, "optional": true, "type": "number", "description": "Management interface", "format": "flag"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "ethernet-cfg": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"ethernet": {"type": "number", "description": "Ethernet (Ethernet interface number)", "format": "interface"}, "optional": true}}]}, "priority": {"description": "Device priority", "format": "number", "type": "number", "maximum": 255, "minimum": 1, "optional": true}, "enable": {"default": 0, "optional": true, "type": "number", "description": "Enable", "format": "flag"}, "ve-cfg": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "ve": {"description": "VE interface (VE interface number)", "minimum": 2, "type": "number", "maximum": 4094, "format": "number"}}}]}, "device": {"platform-specific-range": 1, "platform-specific-default": 1, "description": "Device ID", "format": "number", "optional": false, "type": "number"}, "affinity-vrrp-a-vrid": {"description": "vrid-group", "format": "number", "type": "number", "maximum": 31, "minimum": 0, "optional": true}, "unicast-port": {"description": "Port used in unicast communication (Port number)", "format": "number", "default": 41216, "optional": true, "maximum": 65535, "minimum": 1024, "type": "number"}, "trunk-cfg": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "trunk": {"description": "Trunk interface (Trunk interface number)", "minimum": 1, "type": "number", "maximum": 16, "format": "number"}}}]}}}], "type": "array", "$ref": "/axapi/v3/vcs/device/{device}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Virtual Chassis System.

    Class vcs supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/vcs`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "vcs"
        self.a10_url="/axapi/v3/vcs"
        self.DeviceProxy = ""
        self.vmaster_take_over = {}
        self.vcs_para = {}
        self.A10WW_reload = {}
        self.stat = {}
        self.device_list = []
        self.debug = {}
        self.action = {}
        self.vMaster_maintenance = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


