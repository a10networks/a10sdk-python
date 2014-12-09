from a10sdk.common.A10BaseClass import A10BaseClass


class Arp(A10BaseClass):
    
    """Class Description::
    Configure ARP.

    Class arp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param static_list: {"minItems": 1, "items": {"type": "static"}, "uniqueItems": true, "array": [{"required": ["ip-addr"], "properties": {"ethernet": {"not": "trunk", "optional": true, "type": "number", "description": "Ethernet port (Port Value)", "format": "interface"}, "ip-addr": {"optional": false, "type": "string", "description": "IP address", "format": "ipv4-address"}, "mac-addr": {"optional": true, "type": "string", "description": "MAC address", "format": "mac-address"}, "vlan": {"description": "VLAN ID", "format": "number", "type": "number", "maximum": 4094, "minimum": 1, "optional": true}, "trunk": {"description": "Trunk group", "format": "number", "optional": true, "maximum": 16, "minimum": 1, "not": "ethernet", "type": "number"}}}], "type": "array", "$ref": "/axapi/v3/network/arp/static/{ip-addr}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/network/arp`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "arp"
        self.a10_url="/axapi/v3/network/arp"
        self.DeviceProxy = ""
        self.static_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


