from a10sdk.common.A10BaseClass import A10BaseClass


class Neighbor(A10BaseClass):
    
    """Class Description::
    Static IPv6 Neighbor.

    Class neighbor supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param static_list: {"minItems": 1, "items": {"type": "static"}, "uniqueItems": true, "array": [{"required": ["ipv6-addr", "mac"], "properties": {"ethernet": {"not": "trunk", "optional": true, "type": "number", "description": "Ethernet port (Port Value)", "format": "interface"}, "mac": {"optional": false, "type": "string", "description": "MAC Address", "format": "mac-address"}, "vlan": {"description": "VLAN ID", "format": "number", "type": "number", "maximum": 4094, "minimum": 1, "optional": true}, "ipv6-addr": {"optional": false, "type": "string", "description": "IPV6 address", "format": "ipv6-address"}, "trunk": {"description": "Trunk group", "format": "number", "optional": true, "maximum": 16, "minimum": 1, "not": "ethernet", "type": "number"}}}], "type": "array", "$ref": "/axapi/v3/ipv6/neighbor/static/{ipv6-addr}+{mac}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ipv6/neighbor`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "neighbor"
        self.a10_url="/axapi/v3/ipv6/neighbor"
        self.DeviceProxy = ""
        self.static_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


