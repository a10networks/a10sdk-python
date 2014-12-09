from a10sdk.common.A10BaseClass import A10BaseClass


class Ethernet(A10BaseClass):
    
    """Class Description::
    preferred-session-sync-port ethernet.

    Class ethernet supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param pre_eth: {"optional": false, "type": "number", "description": "Ethernet interface number", "format": "interface"}
    :param pre_vlan: {"description": "Interface VLAN (VLAN ID)", "format": "number", "type": "number", "maximum": 4094, "minimum": 1, "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/vrrp-a/preferred-session-sync-port/ethernet/{pre_eth}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "pre_eth"]

        self.b_key = "ethernet"
        self.a10_url="/axapi/v3/vrrp-a/preferred-session-sync-port/ethernet/{pre_eth}"
        self.DeviceProxy = ""
        self.pre_eth = ""
        self.pre_vlan = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


