from a10sdk.common.A10BaseClass import A10BaseClass


class MultiTopologyCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param multi_topology: {"default": 0, "type": "number", "description": "Enable multi-topology mode", "format": "flag"}
    :param level_transition: {"default": 0, "type": "number", "description": "Accept and generate both IS-IS IPv6 and Multi-topology IPV6 TLVs", "format": "flag"}
    :param transition: {"default": 0, "not": "level", "type": "number", "description": "Accept and generate both IS-IS IPv6 and Multi-topology IPV6 TLVs", "format": "flag"}
    :param level: {"not": "transition", "enum": ["level-1", "level-1-2", "level-2"], "type": "string", "description": "'level-1': Level-1 only; 'level-1-2': Level-1-2; 'level-2': Level-2 only; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "multi-topology-cfg"
        self.DeviceProxy = ""
        self.multi_topology = ""
        self.level_transition = ""
        self.transition = ""
        self.level = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class SummaryPrefixList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param prefix: {"type": "string", "description": "IPv6 prefix", "format": "ipv6-address-plen"}
    :param level: {"default": "level-2", "enum": ["level-1", "level-1-2", "level-2"], "type": "string", "description": "'level-1': Summarize into level-1 area; 'level-1-2': Summarize into both area and sub-domain; 'level-2': Summarize into level-2 sub-domain; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "summary-prefix-list"
        self.DeviceProxy = ""
        self.prefix = ""
        self.level = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Ipv6(A10BaseClass):
    
    """Class Description::
    Address family.

    Class ipv6 supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param distance: {"description": "ISIS Administrative Distance (Distance value)", "format": "number", "default": 115, "optional": true, "maximum": 255, "minimum": 1, "type": "number"}
    :param adjacency_check: {"default": 1, "optional": true, "type": "number", "description": "Check ISIS neighbor protocol support", "format": "flag"}
    :param summary_prefix_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"prefix": {"type": "string", "description": "IPv6 prefix", "format": "ipv6-address-plen"}, "optional": true, "level": {"default": "level-2", "enum": ["level-1", "level-1-2", "level-2"], "type": "string", "description": "'level-1': Summarize into level-1 area; 'level-1-2': Summarize into both area and sub-domain; 'level-2': Summarize into level-2 sub-domain; ", "format": "enum"}}}]}
    :param default_information: {"optional": true, "enum": ["originate"], "type": "string", "description": "'originate': Distribute a default route; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/router/isis/{tag}/address-family/ipv6`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "ipv6"
        self.a10_url="/axapi/v3/router/isis/{tag}/address-family/ipv6"
        self.DeviceProxy = ""
        self.distance = ""
        self.redistribute = {}
        self.multi_topology_cfg = {}
        self.adjacency_check = ""
        self.summary_prefix_list = []
        self.default_information = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


