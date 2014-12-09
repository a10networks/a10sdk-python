from a10sdk.common.A10BaseClass import A10BaseClass


class PreferredSessionSyncPort(A10BaseClass):
    
    """Class Description::
    VRRP-A preferred-session-sync-port.

    Class preferred-session-sync-port supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param trunk_list: {"minItems": 1, "items": {"type": "trunk"}, "uniqueItems": true, "array": [{"required": ["pre-trunk"], "properties": {"pre-vlan": {"description": "Interface VLAN (VLAN ID)", "format": "number", "type": "number", "maximum": 4094, "minimum": 1, "optional": true}, "pre-trunk": {"optional": false, "type": "number", "description": "Trunk Interface number", "format": "interface"}}}], "type": "array", "$ref": "/axapi/v3/vrrp-a/preferred-session-sync-port/trunk/{pre-trunk}"}
    :param ethernet_list: {"minItems": 1, "items": {"type": "ethernet"}, "uniqueItems": true, "array": [{"required": ["pre-eth"], "properties": {"pre-eth": {"optional": false, "type": "number", "description": "Ethernet interface number", "format": "interface"}, "pre-vlan": {"description": "Interface VLAN (VLAN ID)", "format": "number", "type": "number", "maximum": 4094, "minimum": 1, "optional": true}}}], "type": "array", "$ref": "/axapi/v3/vrrp-a/preferred-session-sync-port/ethernet/{pre-eth}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/vrrp-a/preferred-session-sync-port`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "preferred-session-sync-port"
        self.a10_url="/axapi/v3/vrrp-a/preferred-session-sync-port"
        self.DeviceProxy = ""
        self.trunk_list = []
        self.ethernet_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


