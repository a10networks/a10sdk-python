from a10sdk.common.A10BaseClass import A10BaseClass


class Trunk(A10BaseClass):
    
    """Class Description::
    VRRP-A interface trunk.

    Class trunk supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param both: {"description": "both a router and server interface", "format": "flag", "default": 0, "optional": true, "not-list": ["router-interface", "server-interface"], "type": "number"}
    :param vlan: {"description": "VLAN ID", "format": "number", "optional": true, "maximum": 4094, "minimum": 1, "not": "no-heartbeat", "type": "number"}
    :param router_interface: {"description": "interface to upstream router", "format": "flag", "default": 0, "optional": true, "not-list": ["server-interface", "both"], "type": "number"}
    :param no_heartbeat: {"description": "do not send out heartbeat packet from this interface", "format": "flag", "default": 0, "optional": true, "not": "vlan", "type": "number"}
    :param server_interface: {"description": "interface to real server", "format": "flag", "default": 0, "optional": true, "not-list": ["router-interface", "both"], "type": "number"}
    :param trunk_val: {"description": "Ethernet Interface", "format": "number", "type": "number", "maximum": 16, "minimum": 1, "optional": false}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/vrrp-a/interface/trunk/{trunk_val}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "trunk_val"]

        self.b_key = "trunk"
        self.a10_url="/axapi/v3/vrrp-a/interface/trunk/{trunk_val}"
        self.DeviceProxy = ""
        self.both = ""
        self.vlan = ""
        self.router_interface = ""
        self.no_heartbeat = ""
        self.server_interface = ""
        self.trunk_val = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


