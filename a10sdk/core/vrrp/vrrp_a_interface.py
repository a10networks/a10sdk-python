from a10sdk.common.A10BaseClass import A10BaseClass


class Interface(A10BaseClass):
    
    """Class Description::
    VRRP-A interface.

    Class interface supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param trunk_list: {"minItems": 1, "items": {"type": "trunk"}, "uniqueItems": true, "array": [{"required": ["trunk-val"], "properties": {"both": {"description": "both a router and server interface", "format": "flag", "default": 0, "optional": true, "not-list": ["router-interface", "server-interface"], "type": "number"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "vlan": {"description": "VLAN ID", "format": "number", "optional": true, "maximum": 4094, "minimum": 1, "not": "no-heartbeat", "type": "number"}, "router-interface": {"description": "interface to upstream router", "format": "flag", "default": 0, "optional": true, "not-list": ["server-interface", "both"], "type": "number"}, "no-heartbeat": {"description": "do not send out heartbeat packet from this interface", "format": "flag", "default": 0, "optional": true, "not": "vlan", "type": "number"}, "server-interface": {"description": "interface to real server", "format": "flag", "default": 0, "optional": true, "not-list": ["router-interface", "both"], "type": "number"}, "trunk-val": {"description": "Ethernet Interface", "format": "number", "type": "number", "maximum": 16, "minimum": 1, "optional": false}}}], "type": "array", "$ref": "/axapi/v3/vrrp-a/interface/trunk/{trunk-val}"}
    :param ethernet_list: {"minItems": 1, "items": {"type": "ethernet"}, "uniqueItems": true, "array": [{"required": ["ethernet-val"], "properties": {"both": {"description": "both a router and server interface", "format": "flag", "default": 0, "optional": true, "not-list": ["router-interface", "server-interface"], "type": "number"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "vlan": {"description": "VLAN ID", "format": "number", "optional": true, "maximum": 4094, "minimum": 1, "not": "no-heartbeat", "type": "number"}, "ethernet-val": {"optional": false, "type": "number", "description": "Ethernet Interface", "format": "interface"}, "router-interface": {"description": "interface to upstream router", "format": "flag", "default": 0, "optional": true, "not-list": ["server-interface", "both"], "type": "number"}, "no-heartbeat": {"description": "do not send out heartbeat packet from this interface", "format": "flag", "default": 0, "optional": true, "not": "vlan", "type": "number"}, "server-interface": {"description": "interface to real server", "format": "flag", "default": 0, "optional": true, "not-list": ["router-interface", "both"], "type": "number"}}}], "type": "array", "$ref": "/axapi/v3/vrrp-a/interface/ethernet/{ethernet-val}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/vrrp-a/interface`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "interface"
        self.a10_url="/axapi/v3/vrrp-a/interface"
        self.DeviceProxy = ""
        self.trunk_list = []
        self.ethernet_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


