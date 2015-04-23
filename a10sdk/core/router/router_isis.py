from a10sdk.common.A10BaseClass import A10BaseClass


class Authenticate(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param snp: {"enum": ["send-only", "validate"], "type": "string", "description": "'send-only': Send but do not check PDUs on receiving; 'validate': Send and check PDUs on receiving; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "authenticate"
        self.DeviceProxy = ""
        self.snp = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class DomainPasswordCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param password: {"minLength": 1, "maxLength": 254, "type": "string", "description": "Set the authentication password for a routing domain (Routing domain password)", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "domain-password-cfg"
        self.DeviceProxy = ""
        self.password = ""
        self.authenticate = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class SuppressList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param suppress: {"enum": ["external", "interlevel"], "type": "string", "description": "'external': If overload-bit set, don't advertise IP prefixes learned from other protocols; 'interlevel': If overload-bit set, don't advertise IP prefixes learned from another ISIS level; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "suppress-list"
        self.DeviceProxy = ""
        self.suppress = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class OnStartup(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param delay: {"description": "Time in seconds to advertise ourself as overloaded after reboot", "format": "number", "maximum": 86400, "minimum": 5, "not": "wait-for-bgp", "type": "number"}
    :param wait_for_bgp: {"default": 0, "not": "delay", "type": "number", "description": "Let BGP decide when to unset the overload bit", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "on-startup"
        self.DeviceProxy = ""
        self.delay = ""
        self.wait_for_bgp = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class SetOverloadBitCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param suppress_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"suppress": {"enum": ["external", "interlevel"], "type": "string", "description": "'external': If overload-bit set, don't advertise IP prefixes learned from other protocols; 'interlevel': If overload-bit set, don't advertise IP prefixes learned from another ISIS level; ", "format": "enum"}, "optional": true}}]}
    :param set_overload_bit: {"default": 0, "type": "number", "description": "Signal other touers not to use us in SPF", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "set-overload-bit-cfg"
        self.DeviceProxy = ""
        self.suppress_list = []
        self.set_overload_bit = ""
        self.on_startup = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class NetList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param net: {"minLength": 1, "maxLength": 63, "type": "string", "description": "A Network Entity Title for this process (XX.XXXX. ... .XXXX.XX  Network entity title (NET))", "format": "nasp-string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "net-list"
        self.DeviceProxy = ""
        self.net = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class MetricStyleList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param type: {"default": "narrow", "enum": ["narrow", "wide", "transition", "narrow-transition", "wide-transition"], "type": "string", "description": "'narrow': Use old style of TLVs with narrow metric; 'wide': Use new style of TLVs to carry wider metric; 'transition': Send and accept both styles of TLVs during transition; 'narrow-transition': Send old style of TLVs with narrow metric with accepting both styles of TLVs; 'wide-transition': Send new style of TLVs to carry wider metric with accepting both styles of TLVs; ", "format": "enum"}
    :param level: {"default": "level-1-2", "enum": ["level-1", "level-1-2", "level-2"], "type": "string", "description": "'level-1': Level-1 only; 'level-1-2': Level-1-2; 'level-2': Level-2 only; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "metric-style-list"
        self.DeviceProxy = ""
        self.A10WW_type = ""
        self.level = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class KeyChainList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param key_chain: {"minLength": 1, "maxLength": 128, "type": "string", "description": "Authentication key-chain (Name of key-chain)", "format": "string"}
    :param level: {"enum": ["level-1", "level-2"], "type": "string", "description": "'level-1': Specify authentication key-chain for level-1 PDUs; 'level-2': Specify authentication key-chain for level-2 PDUs; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "key-chain-list"
        self.DeviceProxy = ""
        self.key_chain = ""
        self.level = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class ModeList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param mode: {"enum": ["md5"], "type": "string", "description": "'md5': Authentication mode; ", "format": "enum"}
    :param level: {"enum": ["level-1", "level-2"], "type": "string", "description": "'level-1': Specify authentication mode for level-1 PDUs; 'level-2': Specify authentication mode for level-2 PDUs; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "mode-list"
        self.DeviceProxy = ""
        self.mode = ""
        self.level = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class SendOnlyList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param send_only: {"default": 0, "type": "number", "description": "Authentication send-only", "format": "flag"}
    :param level: {"enum": ["level-1", "level-2"], "type": "string", "description": "'level-1': Specify authentication send-only for level-1 PDUs; 'level-2': Specify authentication send-only for level-2 PDUs; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "send-only-list"
        self.DeviceProxy = ""
        self.send_only = ""
        self.level = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Authentication(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param key_chain_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"key-chain": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Authentication key-chain (Name of key-chain)", "format": "string"}, "optional": true, "level": {"enum": ["level-1", "level-2"], "type": "string", "description": "'level-1': Specify authentication key-chain for level-1 PDUs; 'level-2': Specify authentication key-chain for level-2 PDUs; ", "format": "enum"}}}]}
    :param mode_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "mode": {"enum": ["md5"], "type": "string", "description": "'md5': Authentication mode; ", "format": "enum"}, "level": {"enum": ["level-1", "level-2"], "type": "string", "description": "'level-1': Specify authentication mode for level-1 PDUs; 'level-2': Specify authentication mode for level-2 PDUs; ", "format": "enum"}}}]}
    :param send_only_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"send-only": {"default": 0, "type": "number", "description": "Authentication send-only", "format": "flag"}, "optional": true, "level": {"enum": ["level-1", "level-2"], "type": "string", "description": "'level-1': Specify authentication send-only for level-1 PDUs; 'level-2': Specify authentication send-only for level-2 PDUs; ", "format": "enum"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "authentication"
        self.DeviceProxy = ""
        self.key_chain_list = []
        self.mode_list = []
        self.send_only_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class ProtocolList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param protocol_topology: {"default": 0, "type": "number", "description": "Protocol Topology", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "protocol-list"
        self.DeviceProxy = ""
        self.protocol_topology = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class LogAdjacencyChangesCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param state: {"enum": ["detail", "disable"], "type": "string", "description": "'detail': Log changes in adjacency state; 'disable': Disable logging; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "log-adjacency-changes-cfg"
        self.DeviceProxy = ""
        self.state = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class SpfIntervalExpList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param max: {"description": "Maximum Delay between receiving a change to SPF calculation in milliseconds", "format": "number", "default": 50000, "maximum": 2147483647, "minimum": 0, "type": "number"}
    :param level: {"enum": ["level-1", "level-2"], "type": "string", "description": "'level-1': Set interval for level 1 only; 'level-2': Set interval for level 2 only; ", "format": "enum"}
    :param min: {"description": "Minimum Delay between receiving a change to SPF calculation in milliseconds", "format": "number", "default": 500, "maximum": 2147483647, "minimum": 0, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "spf-interval-exp-list"
        self.DeviceProxy = ""
        self.A10WW_max = ""
        self.level = ""
        self.A10WW_min = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class PassiveInterfaceList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param lif: {"type": "number", "description": "Logical interface (Lif interface number)", "format": "interface"}
    :param ve: {"type": "number", "description": "Virtual ethernet interface (Virtual ethernet interface number)", "format": "interface"}
    :param loopback: {"type": "number", "description": "Loopback interface (Port number)", "format": "interface"}
    :param trunk: {"type": "number", "description": "Trunk interface (Trunk interface number)", "format": "interface"}
    :param ethernet: {"type": "number", "description": "Ethernet interface (Port number)", "format": "interface"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "passive-interface-list"
        self.DeviceProxy = ""
        self.lif = ""
        self.ve = ""
        self.loopback = ""
        self.trunk = ""
        self.ethernet = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class SummaryAddressList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param prefix: {"type": "string", "description": "IP network prefix", "format": "ipv4-cidr"}
    :param level: {"default": "level-2", "enum": ["level-1", "level-1-2", "level-2"], "type": "string", "description": "'level-1': Summarize into level-1 area; 'level-1-2': Summarize into both area and sub-domain; 'level-2': Summarize into level-2 sub-domain; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "summary-address-list"
        self.DeviceProxy = ""
        self.prefix = ""
        self.level = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Authenticate(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param snp: {"enum": ["send-only", "validate"], "type": "string", "description": "'send-only': Send but do not check PDUs on receiving; 'validate': Send and check PDUs on receiving; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "authenticate"
        self.DeviceProxy = ""
        self.snp = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class AreaPasswordCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param password: {"minLength": 1, "maxLength": 254, "type": "string", "description": "Configure the authentication password for an area (Area password)", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "area-password-cfg"
        self.DeviceProxy = ""
        self.password = ""
        self.authenticate = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class LspGenIntervalList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param interval: {"description": "Minimum interval in seconds", "format": "number", "default": 30, "maximum": 120, "minimum": 1, "type": "number"}
    :param level: {"enum": ["level-1", "level-2"], "type": "string", "description": "'level-1': Set interval for level 1 only; 'level-2': Set interval for level 2 only; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "lsp-gen-interval-list"
        self.DeviceProxy = ""
        self.interval = ""
        self.level = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class DistanceList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param distance: {"description": "ISIS Administrative Distance (Distance value)", "format": "number", "default": 115, "maximum": 255, "minimum": 1, "type": "number"}
    :param System_ID: {"minLength": 1, "maxLength": 128, "type": "string", "description": "System-ID in XXXX.XXXX.XXXX", "format": "string"}
    :param acl: {"minLength": 1, "maxLength": 128, "type": "string", "description": "Access list name", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "distance-list"
        self.DeviceProxy = ""
        self.distance = ""
        self.System_ID = ""
        self.acl = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Isis(A10BaseClass):
    
    """Class Description::
    Intermediate System - Intermediate System (IS-IS).

    Class isis supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param max_lsp_lifetime: {"description": "Set maximum LSP lifetime (Maximum LSP lifetime in seconds)", "format": "number", "default": 1200, "optional": true, "maximum": 65535, "minimum": 350, "type": "number"}
    :param tag: {"description": "ISO routing area tag", "format": "string", "minLength": 1, "optional": false, "maxLength": 128, "type": "string"}
    :param lsp_refresh_interval: {"description": "Set LSP refresh interval (LSP refresh time in seconds)", "format": "number", "default": 900, "optional": true, "maximum": 65535, "minimum": 1, "type": "number"}
    :param net_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"net": {"minLength": 1, "maxLength": 63, "type": "string", "description": "A Network Entity Title for this process (XX.XXXX. ... .XXXX.XX  Network entity title (NET))", "format": "nasp-string"}, "optional": true}}]}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param bfd: {"optional": true, "enum": ["all-interfaces"], "type": "string", "description": "'all-interfaces': Enable BFD on all interfaces; ", "format": "enum"}
    :param metric_style_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "type": {"default": "narrow", "enum": ["narrow", "wide", "transition", "narrow-transition", "wide-transition"], "type": "string", "description": "'narrow': Use old style of TLVs with narrow metric; 'wide': Use new style of TLVs to carry wider metric; 'transition': Send and accept both styles of TLVs during transition; 'narrow-transition': Send old style of TLVs with narrow metric with accepting both styles of TLVs; 'wide-transition': Send new style of TLVs to carry wider metric with accepting both styles of TLVs; ", "format": "enum"}, "level": {"default": "level-1-2", "enum": ["level-1", "level-1-2", "level-2"], "type": "string", "description": "'level-1': Level-1 only; 'level-1-2': Level-1-2; 'level-2': Level-2 only; ", "format": "enum"}}}]}
    :param ignore_lsp_errors: {"default": 0, "optional": true, "type": "number", "description": "Ignore LSPs with bad checksums", "format": "flag"}
    :param protocol_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "protocol-topology": {"default": 0, "type": "number", "description": "Protocol Topology", "format": "flag"}}}]}
    :param spf_interval_exp_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"max": {"description": "Maximum Delay between receiving a change to SPF calculation in milliseconds", "format": "number", "default": 50000, "maximum": 2147483647, "minimum": 0, "type": "number"}, "level": {"enum": ["level-1", "level-2"], "type": "string", "description": "'level-1': Set interval for level 1 only; 'level-2': Set interval for level 2 only; ", "format": "enum"}, "optional": true, "min": {"description": "Minimum Delay between receiving a change to SPF calculation in milliseconds", "format": "number", "default": 500, "maximum": 2147483647, "minimum": 0, "type": "number"}}}]}
    :param passive_interface_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"lif": {"type": "number", "description": "Logical interface (Lif interface number)", "format": "interface"}, "ve": {"type": "number", "description": "Virtual ethernet interface (Virtual ethernet interface number)", "format": "interface"}, "loopback": {"type": "number", "description": "Loopback interface (Port number)", "format": "interface"}, "trunk": {"type": "number", "description": "Trunk interface (Trunk interface number)", "format": "interface"}, "ethernet": {"type": "number", "description": "Ethernet interface (Port number)", "format": "interface"}, "optional": true}}]}
    :param summary_address_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"prefix": {"type": "string", "description": "IP network prefix", "format": "ipv4-cidr"}, "optional": true, "level": {"default": "level-2", "enum": ["level-1", "level-1-2", "level-2"], "type": "string", "description": "'level-1': Summarize into level-1 area; 'level-1-2': Summarize into both area and sub-domain; 'level-2': Summarize into level-2 sub-domain; ", "format": "enum"}}}]}
    :param adjacency_check: {"default": 1, "optional": true, "type": "number", "description": "Check ISIS neighbor protocol support", "format": "flag"}
    :param default_information: {"optional": true, "enum": ["originate"], "type": "string", "description": "'originate': Distribute a default route; ", "format": "enum"}
    :param lsp_gen_interval_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"interval": {"description": "Minimum interval in seconds", "format": "number", "default": 30, "maximum": 120, "minimum": 1, "type": "number"}, "optional": true, "level": {"enum": ["level-1", "level-2"], "type": "string", "description": "'level-1': Set interval for level 1 only; 'level-2': Set interval for level 2 only; ", "format": "enum"}}}]}
    :param is_type: {"description": "'level-1': Act as a station router only; 'level-1-2': Act as both a station router and an area router; 'level-2-only': Act as an area router only; ", "format": "enum", "default": "level-1", "type": "string", "enum": ["level-1", "level-1-2", "level-2-only"], "optional": true}
    :param distance_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"distance": {"description": "ISIS Administrative Distance (Distance value)", "format": "number", "default": 115, "maximum": 255, "minimum": 1, "type": "number"}, "System-ID": {"minLength": 1, "maxLength": 128, "type": "string", "description": "System-ID in XXXX.XXXX.XXXX", "format": "string"}, "optional": true, "acl": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Access list name", "format": "string"}}}]}
    :param ha_standby_extra_cost: {"description": "Extra IS-IS metric when there is any standby ha group (The extra cost value)", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/router/isis/{tag}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "tag"]

        self.b_key = "isis"
        self.a10_url="/axapi/v3/router/isis/{tag}"
        self.DeviceProxy = ""
        self.domain_password_cfg = {}
        self.max_lsp_lifetime = ""
        self.tag = ""
        self.lsp_refresh_interval = ""
        self.set_overload_bit_cfg = {}
        self.net_list = []
        self.uuid = ""
        self.bfd = ""
        self.metric_style_list = []
        self.authentication = {}
        self.ignore_lsp_errors = ""
        self.protocol_list = []
        self.log_adjacency_changes_cfg = {}
        self.spf_interval_exp_list = []
        self.passive_interface_list = []
        self.summary_address_list = []
        self.adjacency_check = ""
        self.default_information = ""
        self.address_family = {}
        self.redistribute = {}
        self.area_password_cfg = {}
        self.lsp_gen_interval_list = []
        self.is_type = ""
        self.distance_list = []
        self.ha_standby_extra_cost = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


