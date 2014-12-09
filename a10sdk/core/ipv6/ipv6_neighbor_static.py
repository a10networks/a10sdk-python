from a10sdk.common.A10BaseClass import A10BaseClass


class Static(A10BaseClass):
    
    """Class Description::
    static IPv6 Neighbor commands.

    Class static supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ethernet: {"not": "trunk", "optional": true, "type": "number", "description": "Ethernet port (Port Value)", "format": "interface"}
    :param mac: {"optional": false, "type": "string", "description": "MAC Address", "format": "mac-address"}
    :param vlan: {"description": "VLAN ID", "format": "number", "type": "number", "maximum": 4094, "minimum": 1, "optional": true}
    :param ipv6_addr: {"optional": false, "type": "string", "description": "IPV6 address", "format": "ipv6-address"}
    :param trunk: {"description": "Trunk group", "format": "number", "optional": true, "maximum": 16, "minimum": 1, "not": "ethernet", "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ipv6/neighbor/static/{ipv6_addr}+{mac}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "ipv6_addr","mac"]

        self.b_key = "static"
        self.a10_url="/axapi/v3/ipv6/neighbor/static/{ipv6_addr}+{mac}"
        self.DeviceProxy = ""
        self.ethernet = ""
        self.mac = ""
        self.vlan = ""
        self.ipv6_addr = ""
        self.trunk = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


