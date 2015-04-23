from a10sdk.common.A10BaseClass import A10BaseClass


class HelperAddressList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param helper_address: {"type": "string", "description": "Helper address for DHCP packets (IP address)", "format": "ipv4-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "helper-address-list"
        self.DeviceProxy = ""
        self.helper_address = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Nat(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param inside: {"default": 0, "type": "number", "description": "Configure interface as inside", "format": "flag"}
    :param outside: {"default": 0, "type": "number", "description": "Configure interface as outside", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "nat"
        self.DeviceProxy = ""
        self.inside = ""
        self.outside = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class AddressList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ipv4_address: {"type": "string", "description": "IP address", "format": "ipv4-address"}
    :param ipv4_netmask: {"type": "string", "description": "IP subnet mask", "format": "ipv4-netmask"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "address-list"
        self.DeviceProxy = ""
        self.ipv4_address = ""
        self.ipv4_netmask = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Ip(A10BaseClass):
    
    """Class Description::
    Global IP configuration subcommands.

    Class ip supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param generate_membership_query: {"default": 0, "optional": true, "type": "number", "description": "Enable Membership Query", "format": "flag"}
    :param cache_spoofing_port: {"default": 0, "optional": true, "type": "number", "description": "This interface connects to spoofing cache", "format": "flag"}
    :param allow_promiscuous_vip: {"default": 0, "optional": true, "type": "number", "description": "Allow traffic to be associated with promiscuous VIP", "format": "flag"}
    :param max_resp_time: {"description": "Maximum Response Time (Max Response Time (Default is 100))", "format": "number", "default": 100, "optional": true, "maximum": 255, "minimum": 1, "type": "number"}
    :param query_interval: {"description": "1 - 255 (Default is 125)", "format": "number", "default": 125, "optional": true, "maximum": 255, "minimum": 1, "type": "number"}
    :param helper_address_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"helper-address": {"type": "string", "description": "Helper address for DHCP packets (IP address)", "format": "ipv4-address"}, "optional": true}}]}
    :param address_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"ipv4-address": {"type": "string", "description": "IP address", "format": "ipv4-address"}, "optional": true, "ipv4-netmask": {"type": "string", "description": "IP subnet mask", "format": "ipv4-netmask"}}}]}
    :param dhcp: {"default": 0, "optional": true, "type": "number", "description": "Use DHCP to configure IP address", "format": "flag"}
    :param slb_partition_redirect: {"default": 0, "optional": true, "type": "number", "description": "Redirect SLB traffic across partition", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/interface/trunk/{ifnum}/ip`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "ip"
        self.a10_url="/axapi/v3/interface/trunk/{ifnum}/ip"
        self.DeviceProxy = ""
        self.uuid = ""
        self.generate_membership_query = ""
        self.cache_spoofing_port = ""
        self.router = {}
        self.allow_promiscuous_vip = ""
        self.max_resp_time = ""
        self.query_interval = ""
        self.helper_address_list = []
        self.stateful_firewall = {}
        self.rip = {}
        self.nat = {}
        self.address_list = []
        self.dhcp = ""
        self.ospf = {}
        self.slb_partition_redirect = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


