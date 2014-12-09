from a10sdk.common.A10BaseClass import A10BaseClass


class Static(A10BaseClass):
    
    """Class Description::
    static ARP Commands.

    Class static supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ethernet: {"not": "trunk", "optional": true, "type": "number", "description": "Ethernet port. help-val Port Value", "format": "interface"}
    :param ip_addr: {"optional": false, "type": "string", "description": "IP address", "format": "ipv4-address"}
    :param mac_addr: {"optional": true, "type": "string", "description": "MAC address", "format": "mac-address"}
    :param vlan: {"description": "VLAN ID. help-val VLAN Id", "format": "number", "type": "number", "maximum": 4094, "minimum": 1, "optional": true}
    :param trunk: {"description": "Trunk group. help-val Trunk group", "format": "number", "optional": true, "maximum": 16, "minimum": 1, "not": "ethernet", "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/arp/static/{ip_addr}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "ip_addr"]

        self.b_key = "static"
        self.a10_url="/axapi/v3/arp/static/{ip_addr}"
        self.DeviceProxy = ""
        self.ethernet = ""
        self.ip_addr = ""
        self.mac_addr = ""
        self.vlan = ""
        self.trunk = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


