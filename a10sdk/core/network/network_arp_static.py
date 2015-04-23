from a10sdk.common.A10BaseClass import A10BaseClass


class Static(A10BaseClass):
    
    """Class Description::
    static ARP Commands.

    Class static supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param vlan: {"description": "VLAN ID", "format": "number", "optional": false, "maximum": 4094, "minimum": 2, "type": "number", "$ref": "/axapi/v3/network/vlan"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param mac_addr: {"optional": true, "type": "string", "description": "MAC address", "format": "mac-address"}
    :param trunk: {"description": "Trunk group", "format": "number", "optional": true, "maximum": 16, "minimum": 1, "not": "ethernet", "type": "number"}
    :param ethernet: {"not": "trunk", "optional": true, "type": "number", "description": "Ethernet port (Port Value)", "format": "interface"}
    :param ip_addr: {"optional": false, "type": "string", "description": "IP address", "format": "ipv4-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/network/arp/static/{ip_addr}+{vlan}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "ip_addr","vlan"]

        self.b_key = "static"
        self.a10_url="/axapi/v3/network/arp/static/{ip_addr}+{vlan}"
        self.DeviceProxy = ""
        self.vlan = ""
        self.uuid = ""
        self.mac_addr = ""
        self.trunk = ""
        self.ethernet = ""
        self.ip_addr = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


