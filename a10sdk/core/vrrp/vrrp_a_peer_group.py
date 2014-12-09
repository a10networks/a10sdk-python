from a10sdk.common.A10BaseClass import A10BaseClass


class IpPeerAddressCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ip_peer_address: {"type": "string", "description": "IP Address", "format": "ipv4-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ip-peer-address-cfg"
        self.DeviceProxy = ""
        self.ip_peer_address = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Ipv6PeerAddressCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ipv6_peer_address: {"type": "string", "description": "IPV6 address", "format": "ipv6-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ipv6-peer-address-cfg"
        self.DeviceProxy = ""
        self.ipv6_peer_address = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Peer(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ip_peer_address_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"ip-peer-address": {"type": "string", "description": "IP Address", "format": "ipv4-address"}, "optional": true}}]}
    :param ipv6_peer_address_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "ipv6-peer-address": {"type": "string", "description": "IPV6 address", "format": "ipv6-address"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "peer"
        self.DeviceProxy = ""
        self.ip_peer_address_cfg = []
        self.ipv6_peer_address_cfg = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class PeerGroup(A10BaseClass):
    
    """Class Description::
    VRRP-A peer group.

    Class peer-group supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/vrrp-a/peer-group`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "peer-group"
        self.a10_url="/axapi/v3/vrrp-a/peer-group"
        self.DeviceProxy = ""
        self.peer = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


