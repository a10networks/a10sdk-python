from a10sdk.common.A10BaseClass import A10BaseClass


class RulesList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ext_list_value: {"type": "string", "description": "An ordered list as a regular-expression", "format": "string-rlx"}
    :param ext_list_action: {"enum": ["deny", "permit"], "type": "string", "description": "'deny': Specify community to reject; 'permit': Specify community to accept; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "rules-list"
        self.DeviceProxy = ""
        self.ext_list_value = ""
        self.ext_list_action = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class ExpandedNumList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ext_list_num: {"description": "Extended Community list number (expanded)", "format": "number", "type": "number", "maximum": 199, "minimum": 100, "optional": false}
    :param rules_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "ext-list-value": {"type": "string", "description": "An ordered list as a regular-expression", "format": "string-rlx"}, "ext-list-action": {"enum": ["deny", "permit"], "type": "string", "description": "'deny': Specify community to reject; 'permit': Specify community to accept; ", "format": "enum"}}}]}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "expanded-num-list"
        self.DeviceProxy = ""
        self.ext_list_num = ""
        self.rules_list = []
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class RulesList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param expanded_value: {"type": "string", "description": "An ordered list as a regular-expression", "format": "string-rlx"}
    :param expanded_action: {"enum": ["deny", "permit"], "type": "string", "description": "'deny': Specify community to reject; 'permit': Specify community to accept; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "rules-list"
        self.DeviceProxy = ""
        self.expanded_value = ""
        self.expanded_action = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class ExpandedList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param expanded: {"description": "Add an expanded extcommunity-list entry (Extended Community list name)", "format": "string", "minLength": 1, "optional": false, "maxLength": 128, "type": "string"}
    :param rules_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"expanded-value": {"type": "string", "description": "An ordered list as a regular-expression", "format": "string-rlx"}, "optional": true, "expanded-action": {"enum": ["deny", "permit"], "type": "string", "description": "'deny': Specify community to reject; 'permit': Specify community to accept; ", "format": "enum"}}}]}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "expanded-list"
        self.DeviceProxy = ""
        self.expanded = ""
        self.rules_list = []
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class RulesList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param std_list_action: {"enum": ["deny", "permit"], "type": "string", "description": "'deny': Specify community to reject; 'permit': Specify community to accept; ", "format": "enum"}
    :param std_list_value: {"type": "string", "description": "rt Route Target extended community in aa:nn or IPaddr:nn format OR soo Site-of-Origin extended community in aa:nn or IPaddr:nn ", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "rules-list"
        self.DeviceProxy = ""
        self.std_list_action = ""
        self.std_list_value = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class StandardNumList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param rules_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "std-list-action": {"enum": ["deny", "permit"], "type": "string", "description": "'deny': Specify community to reject; 'permit': Specify community to accept; ", "format": "enum"}, "std-list-value": {"type": "string", "description": "rt Route Target extended community in aa:nn or IPaddr:nn format OR soo Site-of-Origin extended community in aa:nn or IPaddr:nn ", "format": "string-rlx"}}}]}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param std_list_num: {"description": "Extended Community list number (standard)", "format": "number", "type": "number", "maximum": 99, "minimum": 1, "optional": false}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "standard-num-list"
        self.DeviceProxy = ""
        self.rules_list = []
        self.uuid = ""
        self.std_list_num = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class RulesList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param standard_action: {"enum": ["deny", "permit"], "type": "string", "description": "'deny': Specify community to reject; 'permit': Specify community to accept; ", "format": "enum"}
    :param standard_value: {"type": "string", "description": "rt Route Target extended community in aa:nn or IPaddr:nn format OR soo Site-of-Origin extended community in aa:nn or IPaddr:nn ", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "rules-list"
        self.DeviceProxy = ""
        self.standard_action = ""
        self.standard_value = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class StandardList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param rules_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"standard-action": {"enum": ["deny", "permit"], "type": "string", "description": "'deny': Specify community to reject; 'permit': Specify community to accept; ", "format": "enum"}, "optional": true, "standard-value": {"type": "string", "description": "rt Route Target extended community in aa:nn or IPaddr:nn format OR soo Site-of-Origin extended community in aa:nn or IPaddr:nn ", "format": "string-rlx"}}}]}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param standard: {"description": "Add a standard extcommunity-list entry (Extended Community list name)", "format": "string", "minLength": 1, "optional": false, "maxLength": 128, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "standard-list"
        self.DeviceProxy = ""
        self.rules_list = []
        self.uuid = ""
        self.standard = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class ExtcommunityList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param expanded_num_list: {"minItems": 1, "items": {"type": "expanded-num"}, "uniqueItems": true, "array": [{"required": ["ext-list-num"], "properties": {"ext-list-num": {"description": "Extended Community list number (expanded)", "format": "number", "type": "number", "maximum": 199, "minimum": 100, "optional": false}, "rules-list": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "ext-list-value": {"type": "string", "description": "An ordered list as a regular-expression", "format": "string-rlx"}, "ext-list-action": {"enum": ["deny", "permit"], "type": "string", "description": "'deny': Specify community to reject; 'permit': Specify community to accept; ", "format": "enum"}}}]}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/ip/extcommunity-list/expanded-num/{ext-list-num}"}
    :param expanded_list: {"minItems": 1, "items": {"type": "expanded"}, "uniqueItems": true, "array": [{"required": ["expanded"], "properties": {"expanded": {"description": "Add an expanded extcommunity-list entry (Extended Community list name)", "format": "string", "minLength": 1, "optional": false, "maxLength": 128, "type": "string"}, "rules-list": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"expanded-value": {"type": "string", "description": "An ordered list as a regular-expression", "format": "string-rlx"}, "optional": true, "expanded-action": {"enum": ["deny", "permit"], "type": "string", "description": "'deny': Specify community to reject; 'permit': Specify community to accept; ", "format": "enum"}}}]}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/ip/extcommunity-list/expanded/{expanded}"}
    :param standard_num_list: {"minItems": 1, "items": {"type": "standard-num"}, "uniqueItems": true, "array": [{"required": ["std-list-num"], "properties": {"rules-list": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "std-list-action": {"enum": ["deny", "permit"], "type": "string", "description": "'deny': Specify community to reject; 'permit': Specify community to accept; ", "format": "enum"}, "std-list-value": {"type": "string", "description": "rt Route Target extended community in aa:nn or IPaddr:nn format OR soo Site-of-Origin extended community in aa:nn or IPaddr:nn ", "format": "string-rlx"}}}]}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "std-list-num": {"description": "Extended Community list number (standard)", "format": "number", "type": "number", "maximum": 99, "minimum": 1, "optional": false}}}], "type": "array", "$ref": "/axapi/v3/ip/extcommunity-list/standard-num/{std-list-num}"}
    :param standard_list: {"minItems": 1, "items": {"type": "standard"}, "uniqueItems": true, "array": [{"required": ["standard"], "properties": {"rules-list": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"standard-action": {"enum": ["deny", "permit"], "type": "string", "description": "'deny': Specify community to reject; 'permit': Specify community to accept; ", "format": "enum"}, "optional": true, "standard-value": {"type": "string", "description": "rt Route Target extended community in aa:nn or IPaddr:nn format OR soo Site-of-Origin extended community in aa:nn or IPaddr:nn ", "format": "string-rlx"}}}]}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "standard": {"description": "Add a standard extcommunity-list entry (Extended Community list name)", "format": "string", "minLength": 1, "optional": false, "maxLength": 128, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/ip/extcommunity-list/standard/{standard}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "extcommunity-list"
        self.DeviceProxy = ""
        self.expanded_num_list = []
        self.expanded_list = []
        self.standard_num_list = []
        self.standard_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Rules(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param geo_location: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Specify geo-location name", "format": "string"}
    :param icmp_type: {"description": "ICMP type number", "format": "number", "not-list": ["any-type", "special-type"], "maximum": 254, "minimum": 0, "type": "number"}
    :param ip: {"default": 0, "not-list": ["icmp", "tcp", "udp", "service-obj-group"], "type": "number", "description": "Any Internet Protocol", "format": "flag"}
    :param service_obj_group: {"description": "Service object group (Source object group name)", "format": "string", "minLength": 1, "not-list": ["icmp", "tcp", "udp", "ip"], "maxLength": 63, "type": "string"}
    :param dst_eq: {"description": "Match only packets on a given destination port (port number)", "format": "number", "not-list": ["dst-gt", "dst-lt", "dst-range"], "maximum": 65535, "minimum": 1, "type": "number"}
    :param tcp: {"default": 0, "not-list": ["icmp", "udp", "ip", "service-obj-group"], "type": "number", "description": "protocol TCP", "format": "flag"}
    :param src_range: {"description": "match only packets in the range of port numbers (Starting Port Number)", "format": "number", "not-list": ["src-eq", "src-gt", "src-lt"], "maximum": 65535, "minimum": 1, "type": "number"}
    :param any_code: {"default": 0, "not-list": ["icmp-code", "special-code"], "type": "number", "description": "Any ICMP code", "format": "flag"}
    :param src_lt: {"description": "Match only packets with a lower port number", "format": "number", "not-list": ["src-eq", "src-gt", "src-range"], "maximum": 65535, "minimum": 2, "type": "number"}
    :param src_mask: {"type": "string", "description": "Source Mask 0=apply 255=ignore", "format": "ipv4-rev-netmask"}
    :param src_port_end: {"description": "Ending Port Number", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}
    :param dst_port_end: {"description": "Edning Destination Port Number", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}
    :param dst_range: {"description": "Match only packets in the range of port numbers (Starting Destination Port Number)", "format": "number", "not-list": ["dst-eq", "dst-gt", "dst-lt"], "maximum": 65535, "minimum": 1, "type": "number"}
    :param established: {"default": 0, "type": "number", "description": "TCP established", "format": "flag"}
    :param dst_mask: {"type": "string", "description": "Destination Mask 0=apply 255=ignore", "format": "ipv4-rev-netmask"}
    :param seq_num: {"description": "Sequence Number", "minimum": 1, "type": "number", "maximum": 8192, "format": "number"}
    :param src_any: {"default": 0, "not-list": ["src-host", "src-subnet", "src-object-group"], "type": "number", "description": "Any source host", "format": "flag"}
    :param fragments: {"default": 0, "type": "number", "description": "IP fragments", "format": "flag"}
    :param icmp_code: {"description": "ICMP code number", "format": "number", "not-list": ["any-code", "special-code"], "maximum": 254, "minimum": 0, "type": "number"}
    :param src_gt: {"description": "Match only packets with a greater port number", "format": "number", "not-list": ["src-eq", "src-lt", "src-range"], "maximum": 65534, "minimum": 1, "type": "number"}
    :param udp: {"default": 0, "not-list": ["icmp", "tcp", "ip", "service-obj-group"], "type": "number", "description": "protocol UDP", "format": "flag"}
    :param dst_subnet: {"not-list": ["dst-any", "dst-host", "dst-object-group"], "type": "string", "description": "Destination Address", "format": "ipv4-address"}
    :param src_subnet: {"not-list": ["src-any", "src-host", "src-object-group"], "type": "string", "description": "Source Address", "format": "ipv4-address"}
    :param vlan: {"description": "VLAN ID", "minimum": 1, "type": "number", "maximum": 4094, "format": "number"}
    :param dscp: {"description": "DSCP", "minimum": 1, "type": "number", "maximum": 63, "format": "number"}
    :param dst_lt: {"description": "Match only packets with a lesser port number", "format": "number", "not-list": ["dst-eq", "dst-gt", "dst-range"], "maximum": 65535, "minimum": 2, "type": "number"}
    :param icmp: {"default": 0, "not-list": ["tcp", "udp", "ip", "service-obj-group"], "type": "number", "description": "Internet Control Message Protocol", "format": "flag"}
    :param dst_gt: {"description": "Match only packets with a greater port number", "format": "number", "not-list": ["dst-eq", "dst-lt", "dst-range"], "maximum": 65534, "minimum": 1, "type": "number"}
    :param acl_log: {"default": 0, "type": "number", "description": "Log matches against this entry", "format": "flag"}
    :param src_object_group: {"description": "Network object group (Source network object group name)", "format": "string", "minLength": 1, "not-list": ["src-any", "src-host", "src-subnet"], "maxLength": 63, "type": "string"}
    :param remark: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Access list entry comment (Notes for this ACL)", "format": "string-rlx"}
    :param dst_object_group: {"description": "Destination network object group name (Source network object group name)", "format": "string", "minLength": 1, "not-list": ["dst-any", "dst-host", "dst-subnet"], "maxLength": 63, "type": "string"}
    :param any_type: {"default": 0, "not-list": ["icmp-type", "special-type"], "type": "number", "description": "Any ICMP type", "format": "flag"}
    :param transparent_session_only: {"default": 0, "type": "number", "description": "Only log transparent sessions", "format": "flag"}
    :param dst_any: {"default": 0, "not-list": ["dst-host", "dst-subnet", "dst-object-group"], "type": "number", "description": "Any destination host", "format": "flag"}
    :param src_host: {"not-list": ["src-any", "src-subnet", "src-object-group"], "type": "string", "description": "A single source host (Host address)", "format": "ipv4-address"}
    :param action: {"enum": ["deny", "permit", "l3-vlan-fwd-disable"], "type": "string", "description": "'deny': Deny; 'permit': Permit; 'l3-vlan-fwd-disable': Disable L3 forwarding between VLANs; ", "format": "enum"}
    :param special_code: {"not-list": ["any-code", "icmp-code"], "enum": ["frag-required", "host-unreachable", "network-unreachable", "port-unreachable", "proto-unreachable", "route-failed"], "type": "string", "description": "'frag-required': Code 4, fragmentation required; 'host-unreachable': Code 1, destination host unreachable; 'network-unreachable': Code 0, destination network unreachable; 'port-unreachable': Code 3, destination port unreachable; 'proto-unreachable': Code 2, destination protocol unreachable; 'route-failed': Code 5, source route failed; ", "format": "enum"}
    :param special_type: {"not-list": ["icmp-type", "any-type"], "enum": ["echo-reply", "echo-request", "info-reply", "info-request", "mask-reply", "mask-request", "parameter-problem", "redirect", "source-quench", "time-exceeded", "timestamp", "timestamp-reply", "dest-unreachable"], "type": "string", "description": "'echo-reply': Type 0, echo reply; 'echo-request': Type 8, echo request; 'info-reply': Type 16, information reply; 'info-request': Type 15, information request; 'mask-reply': Type 18, address mask reply; 'mask-request': Type 17, address mask request; 'parameter-problem': Type 12, parameter problem; 'redirect': Type 5, redirect message; 'source-quench': Type 4, source quench; 'time-exceeded': Type 11, time exceeded; 'timestamp': Type 13, timestamp; 'timestamp-reply': Type 14, timestamp reply; 'dest-unreachable': Type 3, destination unreachable; ", "format": "enum"}
    :param src_eq: {"description": "Match only packets on a given source port (port number)", "format": "number", "not-list": ["src-gt", "src-lt", "src-range"], "maximum": 65535, "minimum": 1, "type": "number"}
    :param dst_host: {"not-list": ["dst-any", "dst-subnet", "dst-object-group"], "type": "string", "description": "A single destination host (Host address)", "format": "ipv4-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "rules"
        self.DeviceProxy = ""
        self.geo_location = ""
        self.icmp_type = ""
        self.ip = ""
        self.service_obj_group = ""
        self.dst_eq = ""
        self.tcp = ""
        self.src_range = ""
        self.any_code = ""
        self.src_lt = ""
        self.src_mask = ""
        self.src_port_end = ""
        self.dst_port_end = ""
        self.dst_range = ""
        self.established = ""
        self.dst_mask = ""
        self.seq_num = ""
        self.src_any = ""
        self.fragments = ""
        self.icmp_code = ""
        self.src_gt = ""
        self.udp = ""
        self.dst_subnet = ""
        self.src_subnet = ""
        self.vlan = ""
        self.dscp = ""
        self.dst_lt = ""
        self.icmp = ""
        self.dst_gt = ""
        self.acl_log = ""
        self.src_object_group = ""
        self.remark = ""
        self.dst_object_group = ""
        self.any_type = ""
        self.transparent_session_only = ""
        self.dst_any = ""
        self.src_host = ""
        self.action = ""
        self.special_code = ""
        self.special_type = ""
        self.src_eq = ""
        self.dst_host = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class AccessListList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param rules: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"geo-location": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Specify geo-location name", "format": "string"}, "icmp-type": {"description": "ICMP type number", "format": "number", "not-list": ["any-type", "special-type"], "maximum": 254, "minimum": 0, "type": "number"}, "ip": {"default": 0, "not-list": ["icmp", "tcp", "udp", "service-obj-group"], "type": "number", "description": "Any Internet Protocol", "format": "flag"}, "service-obj-group": {"description": "Service object group (Source object group name)", "format": "string", "minLength": 1, "not-list": ["icmp", "tcp", "udp", "ip"], "maxLength": 63, "type": "string"}, "dst-eq": {"description": "Match only packets on a given destination port (port number)", "format": "number", "not-list": ["dst-gt", "dst-lt", "dst-range"], "maximum": 65535, "minimum": 1, "type": "number"}, "tcp": {"default": 0, "not-list": ["icmp", "udp", "ip", "service-obj-group"], "type": "number", "description": "protocol TCP", "format": "flag"}, "src-range": {"description": "match only packets in the range of port numbers (Starting Port Number)", "format": "number", "not-list": ["src-eq", "src-gt", "src-lt"], "maximum": 65535, "minimum": 1, "type": "number"}, "any-code": {"default": 0, "not-list": ["icmp-code", "special-code"], "type": "number", "description": "Any ICMP code", "format": "flag"}, "src-lt": {"description": "Match only packets with a lower port number", "format": "number", "not-list": ["src-eq", "src-gt", "src-range"], "maximum": 65535, "minimum": 2, "type": "number"}, "src-mask": {"type": "string", "description": "Source Mask 0=apply 255=ignore", "format": "ipv4-rev-netmask"}, "src-port-end": {"description": "Ending Port Number", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}, "dst-port-end": {"description": "Edning Destination Port Number", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}, "dst-range": {"description": "Match only packets in the range of port numbers (Starting Destination Port Number)", "format": "number", "not-list": ["dst-eq", "dst-gt", "dst-lt"], "maximum": 65535, "minimum": 1, "type": "number"}, "established": {"default": 0, "type": "number", "description": "TCP established", "format": "flag"}, "dst-mask": {"type": "string", "description": "Destination Mask 0=apply 255=ignore", "format": "ipv4-rev-netmask"}, "seq-num": {"description": "Sequence Number", "minimum": 1, "type": "number", "maximum": 8192, "format": "number"}, "src-any": {"default": 0, "not-list": ["src-host", "src-subnet", "src-object-group"], "type": "number", "description": "Any source host", "format": "flag"}, "fragments": {"default": 0, "type": "number", "description": "IP fragments", "format": "flag"}, "icmp-code": {"description": "ICMP code number", "format": "number", "not-list": ["any-code", "special-code"], "maximum": 254, "minimum": 0, "type": "number"}, "src-gt": {"description": "Match only packets with a greater port number", "format": "number", "not-list": ["src-eq", "src-lt", "src-range"], "maximum": 65534, "minimum": 1, "type": "number"}, "udp": {"default": 0, "not-list": ["icmp", "tcp", "ip", "service-obj-group"], "type": "number", "description": "protocol UDP", "format": "flag"}, "dst-subnet": {"not-list": ["dst-any", "dst-host", "dst-object-group"], "type": "string", "description": "Destination Address", "format": "ipv4-address"}, "src-subnet": {"not-list": ["src-any", "src-host", "src-object-group"], "type": "string", "description": "Source Address", "format": "ipv4-address"}, "vlan": {"description": "VLAN ID", "minimum": 1, "type": "number", "maximum": 4094, "format": "number"}, "dscp": {"description": "DSCP", "minimum": 1, "type": "number", "maximum": 63, "format": "number"}, "dst-lt": {"description": "Match only packets with a lesser port number", "format": "number", "not-list": ["dst-eq", "dst-gt", "dst-range"], "maximum": 65535, "minimum": 2, "type": "number"}, "icmp": {"default": 0, "not-list": ["tcp", "udp", "ip", "service-obj-group"], "type": "number", "description": "Internet Control Message Protocol", "format": "flag"}, "optional": true, "dst-gt": {"description": "Match only packets with a greater port number", "format": "number", "not-list": ["dst-eq", "dst-lt", "dst-range"], "maximum": 65534, "minimum": 1, "type": "number"}, "acl-log": {"default": 0, "type": "number", "description": "Log matches against this entry", "format": "flag"}, "src-object-group": {"description": "Network object group (Source network object group name)", "format": "string", "minLength": 1, "not-list": ["src-any", "src-host", "src-subnet"], "maxLength": 63, "type": "string"}, "remark": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Access list entry comment (Notes for this ACL)", "format": "string-rlx"}, "dst-object-group": {"description": "Destination network object group name (Source network object group name)", "format": "string", "minLength": 1, "not-list": ["dst-any", "dst-host", "dst-subnet"], "maxLength": 63, "type": "string"}, "any-type": {"default": 0, "not-list": ["icmp-type", "special-type"], "type": "number", "description": "Any ICMP type", "format": "flag"}, "transparent-session-only": {"default": 0, "type": "number", "description": "Only log transparent sessions", "format": "flag"}, "dst-any": {"default": 0, "not-list": ["dst-host", "dst-subnet", "dst-object-group"], "type": "number", "description": "Any destination host", "format": "flag"}, "src-host": {"not-list": ["src-any", "src-subnet", "src-object-group"], "type": "string", "description": "A single source host (Host address)", "format": "ipv4-address"}, "action": {"enum": ["deny", "permit", "l3-vlan-fwd-disable"], "type": "string", "description": "'deny': Deny; 'permit': Permit; 'l3-vlan-fwd-disable': Disable L3 forwarding between VLANs; ", "format": "enum"}, "special-code": {"not-list": ["any-code", "icmp-code"], "enum": ["frag-required", "host-unreachable", "network-unreachable", "port-unreachable", "proto-unreachable", "route-failed"], "type": "string", "description": "'frag-required': Code 4, fragmentation required; 'host-unreachable': Code 1, destination host unreachable; 'network-unreachable': Code 0, destination network unreachable; 'port-unreachable': Code 3, destination port unreachable; 'proto-unreachable': Code 2, destination protocol unreachable; 'route-failed': Code 5, source route failed; ", "format": "enum"}, "special-type": {"not-list": ["icmp-type", "any-type"], "enum": ["echo-reply", "echo-request", "info-reply", "info-request", "mask-reply", "mask-request", "parameter-problem", "redirect", "source-quench", "time-exceeded", "timestamp", "timestamp-reply", "dest-unreachable"], "type": "string", "description": "'echo-reply': Type 0, echo reply; 'echo-request': Type 8, echo request; 'info-reply': Type 16, information reply; 'info-request': Type 15, information request; 'mask-reply': Type 18, address mask reply; 'mask-request': Type 17, address mask request; 'parameter-problem': Type 12, parameter problem; 'redirect': Type 5, redirect message; 'source-quench': Type 4, source quench; 'time-exceeded': Type 11, time exceeded; 'timestamp': Type 13, timestamp; 'timestamp-reply': Type 14, timestamp reply; 'dest-unreachable': Type 3, destination unreachable; ", "format": "enum"}, "src-eq": {"description": "Match only packets on a given source port (port number)", "format": "number", "not-list": ["src-gt", "src-lt", "src-range"], "maximum": 65535, "minimum": 1, "type": "number"}, "dst-host": {"not-list": ["dst-any", "dst-subnet", "dst-object-group"], "type": "string", "description": "A single destination host (Host address)", "format": "ipv4-address"}}}]}
    :param name: {"description": "IP Access List Name. Does not support name as digits or start with digit.", "format": "string", "minLength": 1, "optional": false, "maxLength": 16, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "access-list-list"
        self.DeviceProxy = ""
        self.rules = []
        self.name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class RulesList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ext_list_value: {"type": "string", "description": "An ordered list as a regular-expression", "format": "string-rlx"}
    :param ext_list_action: {"enum": ["deny", "permit"], "type": "string", "description": "'deny': Specify community to reject; 'permit': Specify community to accept; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "rules-list"
        self.DeviceProxy = ""
        self.ext_list_value = ""
        self.ext_list_action = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class ExpandedNumList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ext_list_num: {"description": "Community list number (expanded)", "format": "number", "type": "number", "maximum": 199, "minimum": 100, "optional": false}
    :param rules_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "ext-list-value": {"type": "string", "description": "An ordered list as a regular-expression", "format": "string-rlx"}, "ext-list-action": {"enum": ["deny", "permit"], "type": "string", "description": "'deny': Specify community to reject; 'permit': Specify community to accept; ", "format": "enum"}}}]}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "expanded-num-list"
        self.DeviceProxy = ""
        self.ext_list_num = ""
        self.rules_list = []
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class RulesList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param expanded_value: {"type": "string", "description": "An ordered list as a regular-expression", "format": "string-rlx"}
    :param expanded_action: {"enum": ["deny", "permit"], "type": "string", "description": "'deny': Specify community to reject; 'permit': Specify community to accept; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "rules-list"
        self.DeviceProxy = ""
        self.expanded_value = ""
        self.expanded_action = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class ExpandedList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param expanded: {"description": "Add an expanded community-list entry (Community list name)", "format": "string", "minLength": 1, "optional": false, "maxLength": 128, "type": "string"}
    :param rules_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"expanded-value": {"type": "string", "description": "An ordered list as a regular-expression", "format": "string-rlx"}, "optional": true, "expanded-action": {"enum": ["deny", "permit"], "type": "string", "description": "'deny': Specify community to reject; 'permit': Specify community to accept; ", "format": "enum"}}}]}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "expanded-list"
        self.DeviceProxy = ""
        self.expanded = ""
        self.rules_list = []
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class RulesList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param std_list_action: {"enum": ["deny", "permit"], "type": "string", "description": "'deny': Specify community to reject; 'permit': Specify community to accept; ", "format": "enum"}
    :param std_list_comm_value: {"type": "string", "description": "community value in the format 1-4294967295|AA:NN|internet|local-AS|no-advertise|no-export", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "rules-list"
        self.DeviceProxy = ""
        self.std_list_action = ""
        self.std_list_comm_value = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class StandardNumList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param rules_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "std-list-action": {"enum": ["deny", "permit"], "type": "string", "description": "'deny': Specify community to reject; 'permit': Specify community to accept; ", "format": "enum"}, "std-list-comm-value": {"type": "string", "description": "community value in the format 1-4294967295|AA:NN|internet|local-AS|no-advertise|no-export", "format": "string-rlx"}}}]}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param std_list_num: {"description": "Community list number (standard)", "format": "number", "type": "number", "maximum": 99, "minimum": 1, "optional": false}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "standard-num-list"
        self.DeviceProxy = ""
        self.rules_list = []
        self.uuid = ""
        self.std_list_num = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class RulesList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param standard_action: {"enum": ["deny", "permit"], "type": "string", "description": "'deny': Specify community to reject; 'permit': Specify community to accept; ", "format": "enum"}
    :param standard_comm_value: {"type": "string", "description": "community value in the format 1-4294967295|AA:NN|internet|local-AS|no-advertise|no-export", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "rules-list"
        self.DeviceProxy = ""
        self.standard_action = ""
        self.standard_comm_value = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class StandardList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param rules_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"standard-action": {"enum": ["deny", "permit"], "type": "string", "description": "'deny': Specify community to reject; 'permit': Specify community to accept; ", "format": "enum"}, "optional": true, "standard-comm-value": {"type": "string", "description": "community value in the format 1-4294967295|AA:NN|internet|local-AS|no-advertise|no-export", "format": "string-rlx"}}}]}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param standard: {"description": "Add a standard community-list entry (Community list name)", "format": "string", "minLength": 1, "optional": false, "maxLength": 128, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "standard-list"
        self.DeviceProxy = ""
        self.rules_list = []
        self.uuid = ""
        self.standard = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class CommunityList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param expanded_num_list: {"minItems": 1, "items": {"type": "expanded-num"}, "uniqueItems": true, "array": [{"required": ["ext-list-num"], "properties": {"ext-list-num": {"description": "Community list number (expanded)", "format": "number", "type": "number", "maximum": 199, "minimum": 100, "optional": false}, "rules-list": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "ext-list-value": {"type": "string", "description": "An ordered list as a regular-expression", "format": "string-rlx"}, "ext-list-action": {"enum": ["deny", "permit"], "type": "string", "description": "'deny': Specify community to reject; 'permit': Specify community to accept; ", "format": "enum"}}}]}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/ip/community-list/expanded-num/{ext-list-num}"}
    :param expanded_list: {"minItems": 1, "items": {"type": "expanded"}, "uniqueItems": true, "array": [{"required": ["expanded"], "properties": {"expanded": {"description": "Add an expanded community-list entry (Community list name)", "format": "string", "minLength": 1, "optional": false, "maxLength": 128, "type": "string"}, "rules-list": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"expanded-value": {"type": "string", "description": "An ordered list as a regular-expression", "format": "string-rlx"}, "optional": true, "expanded-action": {"enum": ["deny", "permit"], "type": "string", "description": "'deny': Specify community to reject; 'permit': Specify community to accept; ", "format": "enum"}}}]}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/ip/community-list/expanded/{expanded}"}
    :param standard_num_list: {"minItems": 1, "items": {"type": "standard-num"}, "uniqueItems": true, "array": [{"required": ["std-list-num"], "properties": {"rules-list": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "std-list-action": {"enum": ["deny", "permit"], "type": "string", "description": "'deny': Specify community to reject; 'permit': Specify community to accept; ", "format": "enum"}, "std-list-comm-value": {"type": "string", "description": "community value in the format 1-4294967295|AA:NN|internet|local-AS|no-advertise|no-export", "format": "string-rlx"}}}]}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "std-list-num": {"description": "Community list number (standard)", "format": "number", "type": "number", "maximum": 99, "minimum": 1, "optional": false}}}], "type": "array", "$ref": "/axapi/v3/ip/community-list/standard-num/{std-list-num}"}
    :param standard_list: {"minItems": 1, "items": {"type": "standard"}, "uniqueItems": true, "array": [{"required": ["standard"], "properties": {"rules-list": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"standard-action": {"enum": ["deny", "permit"], "type": "string", "description": "'deny': Specify community to reject; 'permit': Specify community to accept; ", "format": "enum"}, "optional": true, "standard-comm-value": {"type": "string", "description": "community value in the format 1-4294967295|AA:NN|internet|local-AS|no-advertise|no-export", "format": "string-rlx"}}}]}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "standard": {"description": "Add a standard community-list entry (Community list name)", "format": "string", "minLength": 1, "optional": false, "maxLength": 128, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/ip/community-list/standard/{standard}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "community-list"
        self.DeviceProxy = ""
        self.expanded_num_list = []
        self.expanded_list = []
        self.standard_num_list = []
        self.standard_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Rules(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param le: {"description": "Maximum prefix length to be matched", "minimum": 0, "type": "number", "maximum": 32, "format": "number"}
    :param description: {"minLength": 1, "maxLength": 80, "type": "string", "description": "Prefix-list specific description (Up to 80 characters describing this prefix-list)", "format": "string"}
    :param seq: {"description": "Sequence number of an entry", "minimum": 1, "type": "number", "maximum": 4294967295, "format": "number"}
    :param ipaddr: {"type": "string", "description": "IP prefix, e.g., 35.0.0.0/8", "format": "ipv4-cidr"}
    :param ge: {"description": "Minimum prefix length to be matched", "minimum": 0, "type": "number", "maximum": 32, "format": "number"}
    :param action: {"enum": ["deny", "permit"], "type": "string", "description": "'deny': Specify packets to reject; 'permit': Specify packets to forward; ", "format": "enum"}
    :param any: {"default": 0, "type": "number", "description": "Any prefix match. Same as \"0.0.0.0/0 le 32\"", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "rules"
        self.DeviceProxy = ""
        self.le = ""
        self.description = ""
        self.seq = ""
        self.ipaddr = ""
        self.ge = ""
        self.action = ""
        self.A10WW_any = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class PrefixListList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param rules: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"le": {"description": "Maximum prefix length to be matched", "minimum": 0, "type": "number", "maximum": 32, "format": "number"}, "description": {"minLength": 1, "maxLength": 80, "type": "string", "description": "Prefix-list specific description (Up to 80 characters describing this prefix-list)", "format": "string"}, "seq": {"description": "Sequence number of an entry", "minimum": 1, "type": "number", "maximum": 4294967295, "format": "number"}, "ipaddr": {"type": "string", "description": "IP prefix, e.g., 35.0.0.0/8", "format": "ipv4-cidr"}, "ge": {"description": "Minimum prefix length to be matched", "minimum": 0, "type": "number", "maximum": 32, "format": "number"}, "action": {"enum": ["deny", "permit"], "type": "string", "description": "'deny': Specify packets to reject; 'permit': Specify packets to forward; ", "format": "enum"}, "optional": true, "any": {"default": 0, "type": "number", "description": "Any prefix match. Same as \"0.0.0.0/0 le 32\"", "format": "flag"}}}]}
    :param name: {"description": "Name of a prefix list", "format": "string", "minLength": 1, "optional": false, "maxLength": 128, "type": "string"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "prefix-list-list"
        self.DeviceProxy = ""
        self.rules = []
        self.name = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class MappingList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param count: {"description": "Number of addresses to be translated in this range", "minimum": 1, "type": "number", "maximum": 16777216, "format": "number"}
    :param local_start_ip: {"type": "string", "description": "Local Start IPv4 Address of this list", "format": "ipv4-address"}
    :param global_start_ip: {"type": "string", "description": "Global Start IPv4 Address of this list", "format": "ipv4-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "mapping-list"
        self.DeviceProxy = ""
        self.count = ""
        self.local_start_ip = ""
        self.global_start_ip = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class MapListList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param mapping_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"count": {"description": "Number of addresses to be translated in this range", "minimum": 1, "type": "number", "maximum": 16777216, "format": "number"}, "local-start-ip": {"type": "string", "description": "Local Start IPv4 Address of this list", "format": "ipv4-address"}, "optional": true, "global-start-ip": {"type": "string", "description": "Global Start IPv4 Address of this list", "format": "ipv4-address"}}}]}
    :param name: {"description": "Specify name of the IP Map List", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param file: {"default": 0, "optional": true, "type": "number", "description": "Create/Edit a IP Map List stored as a file", "format": "flag"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "map-list-list"
        self.DeviceProxy = ""
        self.mapping_list = []
        self.name = ""
        self.A10WW_file = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Ip(A10BaseClass):
    
    """    :param as_path_list: {"minItems": 1, "items": {"type": "as-path"}, "uniqueItems": true, "array": [{"required": ["access-list", "action", "value"], "properties": {"access-list": {"description": "Specify an access list name (Regular expression access-list name)", "format": "string", "minLength": 1, "optional": false, "maxLength": 128, "type": "string"}, "action": {"optional": false, "enum": ["deny", "permit"], "type": "string", "description": "'deny': Specify packets to reject; 'permit': Specify packets to forward; ", "format": "enum"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "value": {"optional": false, "type": "string", "description": "A regular-expression to match the BGP AS paths", "format": "string-rlx"}}}], "type": "array", "$ref": "/axapi/v3/ip/as-path/{access-list}+{action}+{value}"}
    :param access_list_list: {"minItems": 1, "items": {"type": "access-list"}, "uniqueItems": true, "array": [{"required": ["name"], "properties": {"rules": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"geo-location": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Specify geo-location name", "format": "string"}, "icmp-type": {"description": "ICMP type number", "format": "number", "not-list": ["any-type", "special-type"], "maximum": 254, "minimum": 0, "type": "number"}, "ip": {"default": 0, "not-list": ["icmp", "tcp", "udp", "service-obj-group"], "type": "number", "description": "Any Internet Protocol", "format": "flag"}, "service-obj-group": {"description": "Service object group (Source object group name)", "format": "string", "minLength": 1, "not-list": ["icmp", "tcp", "udp", "ip"], "maxLength": 63, "type": "string"}, "dst-eq": {"description": "Match only packets on a given destination port (port number)", "format": "number", "not-list": ["dst-gt", "dst-lt", "dst-range"], "maximum": 65535, "minimum": 1, "type": "number"}, "tcp": {"default": 0, "not-list": ["icmp", "udp", "ip", "service-obj-group"], "type": "number", "description": "protocol TCP", "format": "flag"}, "src-range": {"description": "match only packets in the range of port numbers (Starting Port Number)", "format": "number", "not-list": ["src-eq", "src-gt", "src-lt"], "maximum": 65535, "minimum": 1, "type": "number"}, "any-code": {"default": 0, "not-list": ["icmp-code", "special-code"], "type": "number", "description": "Any ICMP code", "format": "flag"}, "src-lt": {"description": "Match only packets with a lower port number", "format": "number", "not-list": ["src-eq", "src-gt", "src-range"], "maximum": 65535, "minimum": 2, "type": "number"}, "src-mask": {"type": "string", "description": "Source Mask 0=apply 255=ignore", "format": "ipv4-rev-netmask"}, "src-port-end": {"description": "Ending Port Number", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}, "dst-port-end": {"description": "Edning Destination Port Number", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}, "dst-range": {"description": "Match only packets in the range of port numbers (Starting Destination Port Number)", "format": "number", "not-list": ["dst-eq", "dst-gt", "dst-lt"], "maximum": 65535, "minimum": 1, "type": "number"}, "established": {"default": 0, "type": "number", "description": "TCP established", "format": "flag"}, "dst-mask": {"type": "string", "description": "Destination Mask 0=apply 255=ignore", "format": "ipv4-rev-netmask"}, "seq-num": {"description": "Sequence Number", "minimum": 1, "type": "number", "maximum": 8192, "format": "number"}, "src-any": {"default": 0, "not-list": ["src-host", "src-subnet", "src-object-group"], "type": "number", "description": "Any source host", "format": "flag"}, "fragments": {"default": 0, "type": "number", "description": "IP fragments", "format": "flag"}, "icmp-code": {"description": "ICMP code number", "format": "number", "not-list": ["any-code", "special-code"], "maximum": 254, "minimum": 0, "type": "number"}, "src-gt": {"description": "Match only packets with a greater port number", "format": "number", "not-list": ["src-eq", "src-lt", "src-range"], "maximum": 65534, "minimum": 1, "type": "number"}, "udp": {"default": 0, "not-list": ["icmp", "tcp", "ip", "service-obj-group"], "type": "number", "description": "protocol UDP", "format": "flag"}, "dst-subnet": {"not-list": ["dst-any", "dst-host", "dst-object-group"], "type": "string", "description": "Destination Address", "format": "ipv4-address"}, "src-subnet": {"not-list": ["src-any", "src-host", "src-object-group"], "type": "string", "description": "Source Address", "format": "ipv4-address"}, "vlan": {"description": "VLAN ID", "minimum": 1, "type": "number", "maximum": 4094, "format": "number"}, "dscp": {"description": "DSCP", "minimum": 1, "type": "number", "maximum": 63, "format": "number"}, "dst-lt": {"description": "Match only packets with a lesser port number", "format": "number", "not-list": ["dst-eq", "dst-gt", "dst-range"], "maximum": 65535, "minimum": 2, "type": "number"}, "icmp": {"default": 0, "not-list": ["tcp", "udp", "ip", "service-obj-group"], "type": "number", "description": "Internet Control Message Protocol", "format": "flag"}, "optional": true, "dst-gt": {"description": "Match only packets with a greater port number", "format": "number", "not-list": ["dst-eq", "dst-lt", "dst-range"], "maximum": 65534, "minimum": 1, "type": "number"}, "acl-log": {"default": 0, "type": "number", "description": "Log matches against this entry", "format": "flag"}, "src-object-group": {"description": "Network object group (Source network object group name)", "format": "string", "minLength": 1, "not-list": ["src-any", "src-host", "src-subnet"], "maxLength": 63, "type": "string"}, "remark": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Access list entry comment (Notes for this ACL)", "format": "string-rlx"}, "dst-object-group": {"description": "Destination network object group name (Source network object group name)", "format": "string", "minLength": 1, "not-list": ["dst-any", "dst-host", "dst-subnet"], "maxLength": 63, "type": "string"}, "any-type": {"default": 0, "not-list": ["icmp-type", "special-type"], "type": "number", "description": "Any ICMP type", "format": "flag"}, "transparent-session-only": {"default": 0, "type": "number", "description": "Only log transparent sessions", "format": "flag"}, "dst-any": {"default": 0, "not-list": ["dst-host", "dst-subnet", "dst-object-group"], "type": "number", "description": "Any destination host", "format": "flag"}, "src-host": {"not-list": ["src-any", "src-subnet", "src-object-group"], "type": "string", "description": "A single source host (Host address)", "format": "ipv4-address"}, "action": {"enum": ["deny", "permit", "l3-vlan-fwd-disable"], "type": "string", "description": "'deny': Deny; 'permit': Permit; 'l3-vlan-fwd-disable': Disable L3 forwarding between VLANs; ", "format": "enum"}, "special-code": {"not-list": ["any-code", "icmp-code"], "enum": ["frag-required", "host-unreachable", "network-unreachable", "port-unreachable", "proto-unreachable", "route-failed"], "type": "string", "description": "'frag-required': Code 4, fragmentation required; 'host-unreachable': Code 1, destination host unreachable; 'network-unreachable': Code 0, destination network unreachable; 'port-unreachable': Code 3, destination port unreachable; 'proto-unreachable': Code 2, destination protocol unreachable; 'route-failed': Code 5, source route failed; ", "format": "enum"}, "special-type": {"not-list": ["icmp-type", "any-type"], "enum": ["echo-reply", "echo-request", "info-reply", "info-request", "mask-reply", "mask-request", "parameter-problem", "redirect", "source-quench", "time-exceeded", "timestamp", "timestamp-reply", "dest-unreachable"], "type": "string", "description": "'echo-reply': Type 0, echo reply; 'echo-request': Type 8, echo request; 'info-reply': Type 16, information reply; 'info-request': Type 15, information request; 'mask-reply': Type 18, address mask reply; 'mask-request': Type 17, address mask request; 'parameter-problem': Type 12, parameter problem; 'redirect': Type 5, redirect message; 'source-quench': Type 4, source quench; 'time-exceeded': Type 11, time exceeded; 'timestamp': Type 13, timestamp; 'timestamp-reply': Type 14, timestamp reply; 'dest-unreachable': Type 3, destination unreachable; ", "format": "enum"}, "src-eq": {"description": "Match only packets on a given source port (port number)", "format": "number", "not-list": ["src-gt", "src-lt", "src-range"], "maximum": 65535, "minimum": 1, "type": "number"}, "dst-host": {"not-list": ["dst-any", "dst-subnet", "dst-object-group"], "type": "string", "description": "A single destination host (Host address)", "format": "ipv4-address"}}}]}, "name": {"description": "IP Access List Name. Does not support name as digits or start with digit.", "format": "string", "minLength": 1, "optional": false, "maxLength": 16, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/ip/access-list/{name}"}
    :param mgmt_traffic_list: {"minItems": 1, "items": {"type": "mgmt-traffic"}, "uniqueItems": true, "array": [{"required": ["traffic-type"], "properties": {"traffic-type": {"optional": false, "enum": ["all", "ftp", "ntp", "rcp", "snmp", "ssh", "syslog", "telnet", "tftp", "web"], "type": "string", "description": "'all': All; 'ftp': FTP; 'ntp': NTP; 'rcp': RCP; 'snmp': SNMP; 'ssh': SSH and SCP; 'syslog': SYSLOG; 'telnet': Telnet; 'tftp': TFTP; 'web': Web - HTTP and HTTPS; ", "format": "enum"}, "source-interface": {"type": "object", "properties": {"loopback": {"type": "number", "description": "Loopback interface (Port number)", "format": "interface"}}}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/ip/mgmt-traffic/{traffic-type}"}
    :param prefix_list_list: {"minItems": 1, "items": {"type": "prefix-list"}, "uniqueItems": true, "array": [{"required": ["name"], "properties": {"rules": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"le": {"description": "Maximum prefix length to be matched", "minimum": 0, "type": "number", "maximum": 32, "format": "number"}, "description": {"minLength": 1, "maxLength": 80, "type": "string", "description": "Prefix-list specific description (Up to 80 characters describing this prefix-list)", "format": "string"}, "seq": {"description": "Sequence number of an entry", "minimum": 1, "type": "number", "maximum": 4294967295, "format": "number"}, "ipaddr": {"type": "string", "description": "IP prefix, e.g., 35.0.0.0/8", "format": "ipv4-cidr"}, "ge": {"description": "Minimum prefix length to be matched", "minimum": 0, "type": "number", "maximum": 32, "format": "number"}, "action": {"enum": ["deny", "permit"], "type": "string", "description": "'deny': Specify packets to reject; 'permit': Specify packets to forward; ", "format": "enum"}, "optional": true, "any": {"default": 0, "type": "number", "description": "Any prefix match. Same as \"0.0.0.0/0 le 32\"", "format": "flag"}}}]}, "name": {"description": "Name of a prefix list", "format": "string", "minLength": 1, "optional": false, "maxLength": 128, "type": "string"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/ip/prefix-list/{name}"}
    :param map_list_list: {"minItems": 1, "items": {"type": "map-list"}, "uniqueItems": true, "array": [{"required": ["name"], "properties": {"mapping-list": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"count": {"description": "Number of addresses to be translated in this range", "minimum": 1, "type": "number", "maximum": 16777216, "format": "number"}, "local-start-ip": {"type": "string", "description": "Local Start IPv4 Address of this list", "format": "ipv4-address"}, "optional": true, "global-start-ip": {"type": "string", "description": "Global Start IPv4 Address of this list", "format": "ipv4-address"}}}]}, "name": {"description": "Specify name of the IP Map List", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}, "file": {"default": 0, "optional": true, "type": "number", "description": "Create/Edit a IP Map List stored as a file", "format": "flag"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/ip/map-list/{name}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Global IP configuration subcommands.

    Class ip supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ip`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "ip"
        self.a10_url="/axapi/v3/ip"
        self.DeviceProxy = ""
        self.frag = {}
        self.extcommunity_list = {}
        self.nat = {}
        self.anomaly_drop = {}
        self.as_path_list = []
        self.route = {}
        self.access_list_list = []
        self.community_list = {}
        self.tcp = {}
        self.mgmt_traffic_list = []
        self.nat_global = {}
        self.default_gateway = {}
        self.dns = {}
        self.address = {}
        self.prefix_list_list = []
        self.icmp = {}
        self.map_list_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


