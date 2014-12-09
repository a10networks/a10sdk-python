from a10sdk.common.A10BaseClass import A10BaseClass


class Bfd(A10BaseClass):
    
    """Class Description::
    Bidirectional Forwarding Detection.

    Class bfd supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param bfd_ipv6_list: {"minItems": 1, "items": {"type": "bfd-ipv6"}, "uniqueItems": true, "array": [{"required": ["local-ipv6", "nexthop-ipv6"], "properties": {"local-ipv6": {"optional": false, "type": "string", "description": "Local IPv6 address", "format": "ipv6-address"}, "nexthop-ipv6": {"optional": false, "type": "string", "description": "Nexthop IPv6 address", "format": "ipv6-address"}}}], "type": "array", "$ref": "/axapi/v3/ipv6/route/static/bfd/bfd-ipv6/{local-ipv6}+{nexthop-ipv6}"}
    :param ethernet_list: {"minItems": 1, "items": {"type": "ethernet"}, "uniqueItems": true, "array": [{"required": ["eth-num", "nexthop-ipv6-ll"], "properties": {"eth-num": {"optional": false, "type": "number", "description": "Ethernet (not a member of vlan or trunk)", "format": "number"}, "nexthop-ipv6-ll": {"optional": false, "type": "string", "description": "Nexthop IPv6 address (Link-local)", "format": "ipv6-address"}}}], "type": "array", "$ref": "/axapi/v3/ipv6/route/static/bfd/ethernet/{eth-num}+{nexthop-ipv6-ll}"}
    :param trunk_list: {"minItems": 1, "items": {"type": "trunk"}, "uniqueItems": true, "array": [{"required": ["trunk-num", "nexthop-ipv6-ll"], "properties": {"nexthop-ipv6-ll": {"optional": false, "type": "string", "description": "Nexthop IPv6 address (Link-local)", "format": "ipv6-address"}, "trunk-num": {"optional": false, "type": "number", "description": "Trunk interface", "format": "number"}}}], "type": "array", "$ref": "/axapi/v3/ipv6/route/static/bfd/trunk/{trunk-num}+{nexthop-ipv6-ll}"}
    :param ve_list: {"minItems": 1, "items": {"type": "ve"}, "uniqueItems": true, "array": [{"required": ["ve-num", "nexthop-ipv6-ll"], "properties": {"nexthop-ipv6-ll": {"optional": false, "type": "string", "description": "Nexthop IPv6 address (Link-local)", "format": "ipv6-address"}, "ve-num": {"optional": false, "type": "number", "description": "Virtual ethernet interface", "format": "number"}}}], "type": "array", "$ref": "/axapi/v3/ipv6/route/static/bfd/ve/{ve-num}+{nexthop-ipv6-ll}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ipv6/route/static/bfd`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "bfd"
        self.a10_url="/axapi/v3/ipv6/route/static/bfd"
        self.DeviceProxy = ""
        self.bfd_ipv6_list = []
        self.ethernet_list = []
        self.trunk_list = []
        self.ve_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


