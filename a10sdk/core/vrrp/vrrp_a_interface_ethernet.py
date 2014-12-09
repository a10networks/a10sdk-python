from a10sdk.common.A10BaseClass import A10BaseClass


class Ethernet(A10BaseClass):
    
    """Class Description::
    VRRP-A interface ethernet.

    Class ethernet supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param both: {"description": "both a router and server interface", "format": "flag", "default": 0, "optional": true, "not-list": ["router-interface", "server-interface"], "type": "number"}
    :param vlan: {"description": "VLAN ID", "format": "number", "optional": true, "maximum": 4094, "minimum": 1, "not": "no-heartbeat", "type": "number"}
    :param ethernet_val: {"optional": false, "type": "number", "description": "Ethernet Interface", "format": "interface"}
    :param router_interface: {"description": "interface to upstream router", "format": "flag", "default": 0, "optional": true, "not-list": ["server-interface", "both"], "type": "number"}
    :param no_heartbeat: {"description": "do not send out heartbeat packet from this interface", "format": "flag", "default": 0, "optional": true, "not": "vlan", "type": "number"}
    :param server_interface: {"description": "interface to real server", "format": "flag", "default": 0, "optional": true, "not-list": ["router-interface", "both"], "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/vrrp-a/interface/ethernet/{ethernet_val}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "ethernet_val"]

        self.b_key = "ethernet"
        self.a10_url="/axapi/v3/vrrp-a/interface/ethernet/{ethernet_val}"
        self.DeviceProxy = ""
        self.both = ""
        self.vlan = ""
        self.ethernet_val = ""
        self.router_interface = ""
        self.no_heartbeat = ""
        self.server_interface = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


