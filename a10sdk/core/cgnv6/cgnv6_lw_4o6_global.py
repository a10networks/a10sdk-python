from a10sdk.common.A10BaseClass import A10BaseClass


class NoForwardMatch(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param send_icmpv6: {"default": 0, "type": "number", "description": "Send ICMPv6 Type 1 Code 5", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "no-forward-match"
        self.DeviceProxy = ""
        self.send_icmpv6 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class NoReverseMatch(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param send_icmp: {"default": 0, "type": "number", "description": "Send ICMP Type 3 Code 1", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "no-reverse-match"
        self.DeviceProxy = ""
        self.send_icmp = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Global(A10BaseClass):
    
    """    :param nat_prefix_list: {"description": "Configure LW-4over6 NAT Prefix List (LW-4over6 NAT Prefix Class-list)", "format": "string", "minLength": 1, "optional": true, "maxLength": 128, "type": "string"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param hairpinning: {"description": "'filter-all': Disable all Hairpinning; 'filter-none': Allow all Hairpinning (default); 'filter-self-ip': Block Hairpinning to same IP; 'filter-self-ip-port': Block hairpinning to same IP and Port combination; ", "format": "enum", "default": "filter-none", "type": "string", "enum": ["filter-all", "filter-none", "filter-self-ip", "filter-self-ip-port"], "optional": true}
    :param icmp_inbound: {"description": "'drop': Drop Inbound ICMP packets; 'handle': Handle Inbound ICMP packets(default); ", "format": "enum", "default": "handle", "type": "string", "enum": ["drop", "handle"], "optional": true}
    :param use_binding_table: {"description": "Bind LW-4over6 binding table for use (LW-4over6 Binding Table Name)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 128, "type": "string"}
    :param tunnel_endpoint_address: {"optional": true, "type": "string", "description": "Configure LW-4over6 IPIP Tunnel Endpoint Address (LW-4over6 Tunnel Endpoint Address)", "format": "ipv6-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Configure LW-4over6 parameters.

    Class global supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/lw-4o6/global`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "global"
        self.a10_url="/axapi/v3/cgnv6/lw-4o6/global"
        self.DeviceProxy = ""
        self.no_forward_match = {}
        self.nat_prefix_list = ""
        self.uuid = ""
        self.hairpinning = ""
        self.icmp_inbound = ""
        self.use_binding_table = ""
        self.no_reverse_match = {}
        self.tunnel_endpoint_address = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


