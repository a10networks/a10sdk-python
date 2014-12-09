from a10sdk.common.A10BaseClass import A10BaseClass


class NssaCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param no_redistribution: {"default": 0, "type": "number", "description": "No redistribution into this NSSA area", "format": "flag"}
    :param translator_role: {"default": "candidate", "enum": ["always", "candidate", "never"], "type": "string", "description": "'always': Translate always; 'candidate': Candidate for translator (default); 'never': Do not translate; ", "format": "enum"}
    :param metric: {"description": "OSPF default metric (OSPF metric)", "format": "number", "default": 1, "maximum": 16777214, "minimum": 0, "type": "number"}
    :param nssa: {"default": 0, "type": "number", "description": "Specify a NSSA area", "format": "flag"}
    :param default_information_originate: {"default": 0, "type": "number", "description": "Originate Type 7 default into NSSA area", "format": "flag"}
    :param no_summary: {"default": 0, "type": "number", "description": "Do not send summary LSA into NSSA", "format": "flag"}
    :param metric_type: {"description": "OSPF metric type (OSPF metric type for default routes)", "format": "number", "default": 2, "maximum": 2, "minimum": 1, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "nssa-cfg"
        self.DeviceProxy = ""
        self.no_redistribution = ""
        self.translator_role = ""
        self.metric = ""
        self.nssa = ""
        self.default_information_originate = ""
        self.no_summary = ""
        self.metric_type = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class FilterLists(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param acl_direction: {"enum": ["in", "out"], "type": "string", "description": "'in': Filter networks sent to this area; 'out': Filter networks sent from this area; ", "format": "enum"}
    :param plist_direction: {"enum": ["in", "out"], "type": "string", "description": "'in': Filter networks sent to this area; 'out': Filter networks sent from this area; ", "format": "enum"}
    :param acl_name: {"minLength": 1, "maxLength": 128, "type": "string", "description": "Filter networks by access-list (Name of an access-list)", "format": "string"}
    :param plist_name: {"minLength": 1, "maxLength": 128, "type": "string", "description": "Filter networks by prefix-list (Name of an IP prefix-list)", "format": "string"}
    :param filter_list: {"default": 0, "type": "number", "description": "Filter networks between OSPF areas", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "filter-lists"
        self.DeviceProxy = ""
        self.acl_direction = ""
        self.plist_direction = ""
        self.acl_name = ""
        self.plist_name = ""
        self.filter_list = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class VirtualLinkList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param dead_interval: {"description": "Dead router detection time (Seconds)", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}
    :param message_digest_key: {"description": "Set message digest key (Key ID)", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}
    :param hello_interval: {"description": "Hello packet interval (Seconds)", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}
    :param bfd: {"default": 0, "type": "number", "description": "Bidirectional Forwarding Detection (BFD)", "format": "flag"}
    :param transmit_delay: {"description": "LSA transmission delay (Seconds)", "format": "number", "default": 1, "maximum": 3600, "minimum": 1, "type": "number"}
    :param virtual_link_authentication: {"default": 0, "type": "number", "description": "Enable authentication", "format": "flag"}
    :param virtual_link_ip_addr: {"type": "string", "description": "ID (IP addr) associated with virtual link neighbor", "format": "ipv4-address"}
    :param virtual_link_auth_type: {"enum": ["message-digest", "null"], "type": "string", "description": "'message-digest': Use message-digest authentication; 'null': Use null authentication; ", "format": "enum"}
    :param authentication_key: {"minLength": 1, "maxLength": 8, "type": "string", "description": "Set authentication key (Authentication key (8 chars))", "format": "string-rlx"}
    :param retransmit_interval: {"description": "LSA retransmit interval (Seconds)", "minimum": 1, "type": "number", "maximum": 3600, "format": "number"}
    :param md5: {"minLength": 1, "maxLength": 16, "type": "string", "description": "Use MD5 algorithm (Authentication key (16 chars))", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "virtual-link-list"
        self.DeviceProxy = ""
        self.dead_interval = ""
        self.message_digest_key = ""
        self.hello_interval = ""
        self.bfd = ""
        self.transmit_delay = ""
        self.virtual_link_authentication = ""
        self.virtual_link_ip_addr = ""
        self.virtual_link_auth_type = ""
        self.authentication_key = ""
        self.retransmit_interval = ""
        self.md5 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class StubCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param stub: {"default": 0, "type": "number", "description": "Configure OSPF area as stub", "format": "flag"}
    :param no_summary: {"default": 0, "type": "number", "description": "Do not inject inter-area routes into area", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stub-cfg"
        self.DeviceProxy = ""
        self.stub = ""
        self.no_summary = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class AuthCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param authentication: {"default": 0, "type": "number", "description": "Enable authentication", "format": "flag"}
    :param message_digest: {"default": 0, "type": "number", "description": "Use message-digest authentication", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "auth-cfg"
        self.DeviceProxy = ""
        self.authentication = ""
        self.message_digest = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class RangeList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param area_range_prefix: {"type": "string", "description": "Area range for IPv4 prefix", "format": "ipv4-cidr"}
    :param option: {"default": "advertise", "enum": ["advertise", "not-advertise"], "type": "string", "description": "'advertise': Advertise this range (default); 'not-advertise': DoNotAdvertise this range; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "range-list"
        self.DeviceProxy = ""
        self.area_range_prefix = ""
        self.option = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Area(A10BaseClass):
    
    """Class Description::
    OSPF area parameters.

    Class area supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param filter_lists: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"acl-direction": {"enum": ["in", "out"], "type": "string", "description": "'in': Filter networks sent to this area; 'out': Filter networks sent from this area; ", "format": "enum"}, "plist-direction": {"enum": ["in", "out"], "type": "string", "description": "'in': Filter networks sent to this area; 'out': Filter networks sent from this area; ", "format": "enum"}, "acl-name": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Filter networks by access-list (Name of an access-list)", "format": "string"}, "plist-name": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Filter networks by prefix-list (Name of an IP prefix-list)", "format": "string"}, "filter-list": {"default": 0, "type": "number", "description": "Filter networks between OSPF areas", "format": "flag"}, "optional": true}}]}
    :param area_ipv4: {"optional": false, "type": "string", "description": "OSPF area ID in IP address format", "format": "ipv4-address"}
    :param virtual_link_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"dead-interval": {"description": "Dead router detection time (Seconds)", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}, "message-digest-key": {"description": "Set message digest key (Key ID)", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}, "hello-interval": {"description": "Hello packet interval (Seconds)", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}, "bfd": {"default": 0, "type": "number", "description": "Bidirectional Forwarding Detection (BFD)", "format": "flag"}, "transmit-delay": {"description": "LSA transmission delay (Seconds)", "format": "number", "default": 1, "maximum": 3600, "minimum": 1, "type": "number"}, "virtual-link-authentication": {"default": 0, "type": "number", "description": "Enable authentication", "format": "flag"}, "virtual-link-ip-addr": {"type": "string", "description": "ID (IP addr) associated with virtual link neighbor", "format": "ipv4-address"}, "virtual-link-auth-type": {"enum": ["message-digest", "null"], "type": "string", "description": "'message-digest': Use message-digest authentication; 'null': Use null authentication; ", "format": "enum"}, "authentication-key": {"minLength": 1, "maxLength": 8, "type": "string", "description": "Set authentication key (Authentication key (8 chars))", "format": "string-rlx"}, "retransmit-interval": {"description": "LSA retransmit interval (Seconds)", "minimum": 1, "type": "number", "maximum": 3600, "format": "number"}, "optional": true, "md5": {"minLength": 1, "maxLength": 16, "type": "string", "description": "Use MD5 algorithm (Authentication key (16 chars))", "format": "string-rlx"}}}]}
    :param shortcut: {"description": "'default': Set default shortcutting behavior; 'disable': Disable shortcutting through the area; 'enable': Enable shortcutting through the area; ", "format": "enum", "default": "default", "type": "string", "enum": ["default", "disable", "enable"], "optional": true}
    :param range_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"area-range-prefix": {"type": "string", "description": "Area range for IPv4 prefix", "format": "ipv4-cidr"}, "optional": true, "option": {"default": "advertise", "enum": ["advertise", "not-advertise"], "type": "string", "description": "'advertise': Advertise this range (default); 'not-advertise': DoNotAdvertise this range; ", "format": "enum"}}}]}
    :param default_cost: {"description": "Set the summary-default cost of a NSSA or stub area (Stub's advertised default summary cost)", "format": "number", "default": 1, "optional": true, "maximum": 16777215, "minimum": 0, "type": "number"}
    :param area_num: {"description": "OSPF area ID as a decimal value", "format": "number", "type": "number", "maximum": 4294967295, "minimum": 0, "optional": false}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/router/ospf/{process_id}/area/{area_ipv4}+{area_num}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "area_ipv4","area_num"]

        self.b_key = "area"
        self.a10_url="/axapi/v3/router/ospf/{process_id}/area/{area_ipv4}+{area_num}"
        self.DeviceProxy = ""
        self.nssa_cfg = {}
        self.filter_lists = []
        self.area_ipv4 = ""
        self.virtual_link_list = []
        self.stub_cfg = {}
        self.shortcut = ""
        self.auth_cfg = {}
        self.range_list = []
        self.default_cost = ""
        self.area_num = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


