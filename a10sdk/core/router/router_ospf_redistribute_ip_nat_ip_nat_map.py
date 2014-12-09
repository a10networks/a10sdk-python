from a10sdk.common.A10BaseClass import A10BaseClass


class IpNatMapList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param floating_IP_forward_address: {"type": "string", "description": "Floating-IP as forward address. help-val Address", "format": "ipv4-address"}
    :param ip_nat_prefix: {"type": "string", "description": "Address", "format": "ipv4-cidr"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ip-nat-map-list"
        self.DeviceProxy = ""
        self.floating_IP_forward_address = ""
        self.ip_nat_prefix = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class IpNatMap(A10BaseClass):
    
    """Class Description::
    IP NAT redistribution map.

    Class ip-nat-map supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ip_nat_map_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"floating-IP-forward-address": {"type": "string", "description": "Floating-IP as forward address. help-val Address", "format": "ipv4-address"}, "optional": true, "ip-nat-prefix": {"type": "string", "description": "Address", "format": "ipv4-cidr"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/router/ospf/{process_id}/redistribute/ip-nat/ip-nat-map`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "ip-nat-map"
        self.a10_url="/axapi/v3/router/ospf/{process_id}/redistribute/ip-nat/ip-nat-map"
        self.DeviceProxy = ""
        self.ip_nat_map_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


