from a10sdk.common.A10BaseClass import A10BaseClass


class Rules(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param geo_location: {"description": "Specify geo-location name", "format": "string", "minLength": 1, "not-list": ["tcp", "udp", "ipv6", "service-obj-group"], "maxLength": 63, "type": "string"}
    :param icmp_type: {"description": "ICMP type number", "format": "number", "maximum": 254, "minimum": 0, "not": "any-type", "type": "number"}
    :param service_obj_group: {"description": "Service object group (Source object group name)", "format": "string", "minLength": 1, "not-list": ["tcp", "udp", "ipv6", "geo-location"], "maxLength": 63, "type": "string"}
    :param dst_eq: {"description": "Match only packets on a given destination port (port number)", "format": "number", "not-list": ["dst-gt", "dst-lt"], "maximum": 65535, "minimum": 1, "type": "number"}
    :param tcp: {"default": 0, "not-list": ["udp", "ipv6", "service-obj-group", "geo-location"], "type": "number", "description": "protocol TCP", "format": "flag"}
    :param src_range: {"description": "match only packets in the range of port numbers (Starting Port Number)", "format": "number", "not-list": ["src-eq", "src-gt"], "maximum": 65535, "minimum": 1, "type": "number"}
    :param any_code: {"default": 0, "not": "icmp-code", "type": "number", "description": "Any ICMP code", "format": "flag"}
    :param src_lt: {"description": "Match only packets with a lower port number", "format": "number", "not-list": ["src-eq", "src-gt"], "maximum": 65535, "minimum": 2, "type": "number"}
    :param src_port_end: {"description": "Ending Port Number", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}
    :param dst_port_end: {"description": "Edning Destination Port Number", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}
    :param dst_range: {"description": "Match only packets in the range of port numbers (Starting Destination Port Number)", "format": "number", "not-list": ["dst-eq", "dst-gt"], "maximum": 65535, "minimum": 1, "type": "number"}
    :param established: {"default": 0, "type": "number", "description": "TCP established", "format": "flag"}
    :param seq_num: {"description": "Sequence Number", "minimum": 1, "type": "number", "maximum": 8192, "format": "number"}
    :param src_any: {"default": 0, "not-list": ["src-host", "src-object-group"], "type": "number", "description": "Any source host", "format": "flag"}
    :param ipv6: {"default": 0, "not-list": ["tcp", "udp", "service-obj-group", "geo-location"], "type": "number", "description": "Any Internet Protocol", "format": "flag"}
    :param fragments: {"default": 0, "type": "number", "description": "IP fragments", "format": "flag"}
    :param icmp_code: {"description": "ICMP code number", "format": "number", "maximum": 254, "minimum": 0, "not": "any-code", "type": "number"}
    :param src_gt: {"description": "Match only packets with a greater port number", "format": "number", "not-list": ["src-eq", "src-lt"], "maximum": 65534, "minimum": 1, "type": "number"}
    :param udp: {"default": 0, "not-list": ["tcp", "ipv6", "service-obj-group", "geo-location"], "type": "number", "description": "protocol UDP", "format": "flag"}
    :param dst_subnet: {"not-list": ["dst-any", "dst-host"], "type": "string", "description": "Destination Address", "format": "ipv6-address-plen"}
    :param src_subnet: {"not-list": ["src-any", "src-host"], "type": "string", "description": "Source Address", "format": "ipv6-address-plen"}
    :param vlan: {"description": "VLAN ID", "minimum": 1, "type": "number", "maximum": 4094, "format": "number"}
    :param dscp: {"description": "DSCP", "minimum": 1, "type": "number", "maximum": 63, "format": "number"}
    :param dst_lt: {"description": "Match only packets with a lesser port number", "format": "number", "not-list": ["dst-eq", "dst-gt"], "maximum": 65535, "minimum": 2, "type": "number"}
    :param icmp: {"default": 0, "not-list": ["tcp", "udp", "ipv6", "service-obj-group", "geo-location"], "type": "number", "description": "Internet Control Message Protocol", "format": "flag"}
    :param dst_gt: {"description": "Match only packets with a greater port number", "format": "number", "not-list": ["dst-eq", "dst-lt"], "maximum": 65534, "minimum": 1, "type": "number"}
    :param acl_log: {"default": 0, "type": "number", "description": "Log matches against this entry", "format": "flag"}
    :param src_object_group: {"description": "Network object group (Source network object group name)", "format": "string", "minLength": 1, "not-list": ["src-any", "src-host"], "maxLength": 63, "type": "string"}
    :param remark: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Access list entry comment (Notes for this ACL)", "format": "string-rlx"}
    :param dst_object_group: {"description": "Destination network object group name (Source network object group name)", "format": "string", "minLength": 1, "not-list": ["dst-any", "dst-host"], "maxLength": 63, "type": "string"}
    :param any_type: {"default": 0, "not": "icmp-type", "type": "number", "description": "Any ICMP type", "format": "flag"}
    :param dst_any: {"default": 0, "not-list": ["dst-host", "dst-object-group"], "type": "number", "description": "Any destination host", "format": "flag"}
    :param src_host: {"not-list": ["src-any", "src-object-group"], "type": "string", "description": "A single source host (Host address)", "format": "ipv6-address"}
    :param action: {"enum": ["deny", "permit", "l3-vlan-fwd-disable"], "type": "string", "description": "'deny': Deny; 'permit': Permit; 'l3-vlan-fwd-disable': Disable L3 forwarding between VLANs; ", "format": "enum"}
    :param special_code: {"not": "any-code", "enum": ["addr-unreachable", "admin-prohibited", "no-route", "not-neighbour", "port-unreachable"], "type": "string", "description": "'addr-unreachable': Code 3, address unreachable; 'admin-prohibited': Code 1, admin prohibited; 'no-route': Code 0, no route to destination; 'not-neighbour': Code 2, not neighbor; 'port-unreachable': Code 4, destination port unreachable; ", "format": "enum"}
    :param special_type: {"not": "icmp-type", "enum": ["echo-reply", "echo-request", "packet-too-big", "param-prob", "time-exceeded", "dest-unreachable"], "type": "string", "description": "'echo-reply': Type 129, echo reply; 'echo-request': help Type 128, echo request; 'packet-too-big': Type 2, packet too big; 'param-prob': Type 4, parameter problem; 'time-exceeded': Type 3, time exceeded; 'dest-unreachable': Type 1, destination unreachable; ", "format": "enum"}
    :param src_eq: {"description": "Match only packets on a given source port (port number)", "format": "number", "not-list": ["src-gt", "src-lt"], "maximum": 65535, "minimum": 1, "type": "number"}
    :param dst_host: {"not-list": ["dst-any", "dst-object-group"], "type": "string", "description": "A single destination host (Host address)", "format": "ipv6-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "rules"
        self.DeviceProxy = ""
        self.geo_location = ""
        self.icmp_type = ""
        self.service_obj_group = ""
        self.dst_eq = ""
        self.tcp = ""
        self.src_range = ""
        self.any_code = ""
        self.src_lt = ""
        self.src_port_end = ""
        self.dst_port_end = ""
        self.dst_range = ""
        self.established = ""
        self.seq_num = ""
        self.src_any = ""
        self.ipv6 = ""
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

    :param rules: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"geo-location": {"description": "Specify geo-location name", "format": "string", "minLength": 1, "not-list": ["tcp", "udp", "ipv6", "service-obj-group"], "maxLength": 63, "type": "string"}, "icmp-type": {"description": "ICMP type number", "format": "number", "maximum": 254, "minimum": 0, "not": "any-type", "type": "number"}, "service-obj-group": {"description": "Service object group (Source object group name)", "format": "string", "minLength": 1, "not-list": ["tcp", "udp", "ipv6", "geo-location"], "maxLength": 63, "type": "string"}, "dst-eq": {"description": "Match only packets on a given destination port (port number)", "format": "number", "not-list": ["dst-gt", "dst-lt"], "maximum": 65535, "minimum": 1, "type": "number"}, "tcp": {"default": 0, "not-list": ["udp", "ipv6", "service-obj-group", "geo-location"], "type": "number", "description": "protocol TCP", "format": "flag"}, "src-range": {"description": "match only packets in the range of port numbers (Starting Port Number)", "format": "number", "not-list": ["src-eq", "src-gt"], "maximum": 65535, "minimum": 1, "type": "number"}, "any-code": {"default": 0, "not": "icmp-code", "type": "number", "description": "Any ICMP code", "format": "flag"}, "src-lt": {"description": "Match only packets with a lower port number", "format": "number", "not-list": ["src-eq", "src-gt"], "maximum": 65535, "minimum": 2, "type": "number"}, "src-port-end": {"description": "Ending Port Number", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}, "dst-port-end": {"description": "Edning Destination Port Number", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}, "dst-range": {"description": "Match only packets in the range of port numbers (Starting Destination Port Number)", "format": "number", "not-list": ["dst-eq", "dst-gt"], "maximum": 65535, "minimum": 1, "type": "number"}, "established": {"default": 0, "type": "number", "description": "TCP established", "format": "flag"}, "seq-num": {"description": "Sequence Number", "minimum": 1, "type": "number", "maximum": 8192, "format": "number"}, "src-any": {"default": 0, "not-list": ["src-host", "src-object-group"], "type": "number", "description": "Any source host", "format": "flag"}, "ipv6": {"default": 0, "not-list": ["tcp", "udp", "service-obj-group", "geo-location"], "type": "number", "description": "Any Internet Protocol", "format": "flag"}, "fragments": {"default": 0, "type": "number", "description": "IP fragments", "format": "flag"}, "icmp-code": {"description": "ICMP code number", "format": "number", "maximum": 254, "minimum": 0, "not": "any-code", "type": "number"}, "src-gt": {"description": "Match only packets with a greater port number", "format": "number", "not-list": ["src-eq", "src-lt"], "maximum": 65534, "minimum": 1, "type": "number"}, "udp": {"default": 0, "not-list": ["tcp", "ipv6", "service-obj-group", "geo-location"], "type": "number", "description": "protocol UDP", "format": "flag"}, "dst-subnet": {"not-list": ["dst-any", "dst-host"], "type": "string", "description": "Destination Address", "format": "ipv6-address-plen"}, "src-subnet": {"not-list": ["src-any", "src-host"], "type": "string", "description": "Source Address", "format": "ipv6-address-plen"}, "vlan": {"description": "VLAN ID", "minimum": 1, "type": "number", "maximum": 4094, "format": "number"}, "dscp": {"description": "DSCP", "minimum": 1, "type": "number", "maximum": 63, "format": "number"}, "dst-lt": {"description": "Match only packets with a lesser port number", "format": "number", "not-list": ["dst-eq", "dst-gt"], "maximum": 65535, "minimum": 2, "type": "number"}, "icmp": {"default": 0, "not-list": ["tcp", "udp", "ipv6", "service-obj-group", "geo-location"], "type": "number", "description": "Internet Control Message Protocol", "format": "flag"}, "optional": true, "dst-gt": {"description": "Match only packets with a greater port number", "format": "number", "not-list": ["dst-eq", "dst-lt"], "maximum": 65534, "minimum": 1, "type": "number"}, "acl-log": {"default": 0, "type": "number", "description": "Log matches against this entry", "format": "flag"}, "src-object-group": {"description": "Network object group (Source network object group name)", "format": "string", "minLength": 1, "not-list": ["src-any", "src-host"], "maxLength": 63, "type": "string"}, "remark": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Access list entry comment (Notes for this ACL)", "format": "string-rlx"}, "dst-object-group": {"description": "Destination network object group name (Source network object group name)", "format": "string", "minLength": 1, "not-list": ["dst-any", "dst-host"], "maxLength": 63, "type": "string"}, "any-type": {"default": 0, "not": "icmp-type", "type": "number", "description": "Any ICMP type", "format": "flag"}, "dst-any": {"default": 0, "not-list": ["dst-host", "dst-object-group"], "type": "number", "description": "Any destination host", "format": "flag"}, "src-host": {"not-list": ["src-any", "src-object-group"], "type": "string", "description": "A single source host (Host address)", "format": "ipv6-address"}, "action": {"enum": ["deny", "permit", "l3-vlan-fwd-disable"], "type": "string", "description": "'deny': Deny; 'permit': Permit; 'l3-vlan-fwd-disable': Disable L3 forwarding between VLANs; ", "format": "enum"}, "special-code": {"not": "any-code", "enum": ["addr-unreachable", "admin-prohibited", "no-route", "not-neighbour", "port-unreachable"], "type": "string", "description": "'addr-unreachable': Code 3, address unreachable; 'admin-prohibited': Code 1, admin prohibited; 'no-route': Code 0, no route to destination; 'not-neighbour': Code 2, not neighbor; 'port-unreachable': Code 4, destination port unreachable; ", "format": "enum"}, "special-type": {"not": "icmp-type", "enum": ["echo-reply", "echo-request", "packet-too-big", "param-prob", "time-exceeded", "dest-unreachable"], "type": "string", "description": "'echo-reply': Type 129, echo reply; 'echo-request': help Type 128, echo request; 'packet-too-big': Type 2, packet too big; 'param-prob': Type 4, parameter problem; 'time-exceeded': Type 3, time exceeded; 'dest-unreachable': Type 1, destination unreachable; ", "format": "enum"}, "src-eq": {"description": "Match only packets on a given source port (port number)", "format": "number", "not-list": ["src-gt", "src-lt"], "maximum": 65535, "minimum": 1, "type": "number"}, "dst-host": {"not-list": ["dst-any", "dst-object-group"], "type": "string", "description": "A single destination host (Host address)", "format": "ipv6-address"}}}]}
    :param name: {"description": "Named Access List", "format": "string", "minLength": 1, "optional": false, "maxLength": 16, "type": "string"}
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


class Rules(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param le: {"description": "Maximum prefix length to be matched", "minimum": 0, "type": "number", "maximum": 128, "format": "number"}
    :param description: {"minLength": 1, "maxLength": 80, "type": "string", "description": "Prefix-list specific description (Up to 80 characters describing this prefix-list)", "format": "string"}
    :param seq: {"description": "Sequence number of an entry", "minimum": 1, "type": "number", "maximum": 4294967295, "format": "number"}
    :param ipaddr: {"type": "string", "description": "IPv6 prefix, e.g., 3ffe::/16", "format": "ipv6-address-plen"}
    :param ge: {"description": "Minimum prefix length to be matched", "minimum": 0, "type": "number", "maximum": 128, "format": "number"}
    :param action: {"enum": ["deny", "permit"], "type": "string", "description": "'deny': Specify packets to reject; 'permit': Specify packets to forward; ", "format": "enum"}
    :param any: {"default": 0, "type": "number", "description": "Any prefix match. Same as \"::0/0 le le 128\"", "format": "flag"}
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

    :param rules: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"le": {"description": "Maximum prefix length to be matched", "minimum": 0, "type": "number", "maximum": 128, "format": "number"}, "description": {"minLength": 1, "maxLength": 80, "type": "string", "description": "Prefix-list specific description (Up to 80 characters describing this prefix-list)", "format": "string"}, "seq": {"description": "Sequence number of an entry", "minimum": 1, "type": "number", "maximum": 4294967295, "format": "number"}, "ipaddr": {"type": "string", "description": "IPv6 prefix, e.g., 3ffe::/16", "format": "ipv6-address-plen"}, "ge": {"description": "Minimum prefix length to be matched", "minimum": 0, "type": "number", "maximum": 128, "format": "number"}, "action": {"enum": ["deny", "permit"], "type": "string", "description": "'deny': Specify packets to reject; 'permit': Specify packets to forward; ", "format": "enum"}, "optional": true, "any": {"default": 0, "type": "number", "description": "Any prefix match. Same as \"::0/0 le le 128\"", "format": "flag"}}}]}
    :param name: {"description": "Name of a prefix list", "format": "string", "minLength": 1, "optional": false, "maxLength": 128, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "prefix-list-list"
        self.DeviceProxy = ""
        self.rules = []
        self.name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Ipv6(A10BaseClass):
    
    """Class Description::
    Global IP configuration subcommands.

    Class ipv6 supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param access_list_list: {"minItems": 1, "items": {"type": "access-list"}, "uniqueItems": true, "array": [{"required": ["name"], "properties": {"rules": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"geo-location": {"description": "Specify geo-location name", "format": "string", "minLength": 1, "not-list": ["tcp", "udp", "ipv6", "service-obj-group"], "maxLength": 63, "type": "string"}, "icmp-type": {"description": "ICMP type number", "format": "number", "maximum": 254, "minimum": 0, "not": "any-type", "type": "number"}, "service-obj-group": {"description": "Service object group (Source object group name)", "format": "string", "minLength": 1, "not-list": ["tcp", "udp", "ipv6", "geo-location"], "maxLength": 63, "type": "string"}, "dst-eq": {"description": "Match only packets on a given destination port (port number)", "format": "number", "not-list": ["dst-gt", "dst-lt"], "maximum": 65535, "minimum": 1, "type": "number"}, "tcp": {"default": 0, "not-list": ["udp", "ipv6", "service-obj-group", "geo-location"], "type": "number", "description": "protocol TCP", "format": "flag"}, "src-range": {"description": "match only packets in the range of port numbers (Starting Port Number)", "format": "number", "not-list": ["src-eq", "src-gt"], "maximum": 65535, "minimum": 1, "type": "number"}, "any-code": {"default": 0, "not": "icmp-code", "type": "number", "description": "Any ICMP code", "format": "flag"}, "src-lt": {"description": "Match only packets with a lower port number", "format": "number", "not-list": ["src-eq", "src-gt"], "maximum": 65535, "minimum": 2, "type": "number"}, "src-port-end": {"description": "Ending Port Number", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}, "dst-port-end": {"description": "Edning Destination Port Number", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}, "dst-range": {"description": "Match only packets in the range of port numbers (Starting Destination Port Number)", "format": "number", "not-list": ["dst-eq", "dst-gt"], "maximum": 65535, "minimum": 1, "type": "number"}, "established": {"default": 0, "type": "number", "description": "TCP established", "format": "flag"}, "seq-num": {"description": "Sequence Number", "minimum": 1, "type": "number", "maximum": 8192, "format": "number"}, "src-any": {"default": 0, "not-list": ["src-host", "src-object-group"], "type": "number", "description": "Any source host", "format": "flag"}, "ipv6": {"default": 0, "not-list": ["tcp", "udp", "service-obj-group", "geo-location"], "type": "number", "description": "Any Internet Protocol", "format": "flag"}, "fragments": {"default": 0, "type": "number", "description": "IP fragments", "format": "flag"}, "icmp-code": {"description": "ICMP code number", "format": "number", "maximum": 254, "minimum": 0, "not": "any-code", "type": "number"}, "src-gt": {"description": "Match only packets with a greater port number", "format": "number", "not-list": ["src-eq", "src-lt"], "maximum": 65534, "minimum": 1, "type": "number"}, "udp": {"default": 0, "not-list": ["tcp", "ipv6", "service-obj-group", "geo-location"], "type": "number", "description": "protocol UDP", "format": "flag"}, "dst-subnet": {"not-list": ["dst-any", "dst-host"], "type": "string", "description": "Destination Address", "format": "ipv6-address-plen"}, "src-subnet": {"not-list": ["src-any", "src-host"], "type": "string", "description": "Source Address", "format": "ipv6-address-plen"}, "vlan": {"description": "VLAN ID", "minimum": 1, "type": "number", "maximum": 4094, "format": "number"}, "dscp": {"description": "DSCP", "minimum": 1, "type": "number", "maximum": 63, "format": "number"}, "dst-lt": {"description": "Match only packets with a lesser port number", "format": "number", "not-list": ["dst-eq", "dst-gt"], "maximum": 65535, "minimum": 2, "type": "number"}, "icmp": {"default": 0, "not-list": ["tcp", "udp", "ipv6", "service-obj-group", "geo-location"], "type": "number", "description": "Internet Control Message Protocol", "format": "flag"}, "optional": true, "dst-gt": {"description": "Match only packets with a greater port number", "format": "number", "not-list": ["dst-eq", "dst-lt"], "maximum": 65534, "minimum": 1, "type": "number"}, "acl-log": {"default": 0, "type": "number", "description": "Log matches against this entry", "format": "flag"}, "src-object-group": {"description": "Network object group (Source network object group name)", "format": "string", "minLength": 1, "not-list": ["src-any", "src-host"], "maxLength": 63, "type": "string"}, "remark": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Access list entry comment (Notes for this ACL)", "format": "string-rlx"}, "dst-object-group": {"description": "Destination network object group name (Source network object group name)", "format": "string", "minLength": 1, "not-list": ["dst-any", "dst-host"], "maxLength": 63, "type": "string"}, "any-type": {"default": 0, "not": "icmp-type", "type": "number", "description": "Any ICMP type", "format": "flag"}, "dst-any": {"default": 0, "not-list": ["dst-host", "dst-object-group"], "type": "number", "description": "Any destination host", "format": "flag"}, "src-host": {"not-list": ["src-any", "src-object-group"], "type": "string", "description": "A single source host (Host address)", "format": "ipv6-address"}, "action": {"enum": ["deny", "permit", "l3-vlan-fwd-disable"], "type": "string", "description": "'deny': Deny; 'permit': Permit; 'l3-vlan-fwd-disable': Disable L3 forwarding between VLANs; ", "format": "enum"}, "special-code": {"not": "any-code", "enum": ["addr-unreachable", "admin-prohibited", "no-route", "not-neighbour", "port-unreachable"], "type": "string", "description": "'addr-unreachable': Code 3, address unreachable; 'admin-prohibited': Code 1, admin prohibited; 'no-route': Code 0, no route to destination; 'not-neighbour': Code 2, not neighbor; 'port-unreachable': Code 4, destination port unreachable; ", "format": "enum"}, "special-type": {"not": "icmp-type", "enum": ["echo-reply", "echo-request", "packet-too-big", "param-prob", "time-exceeded", "dest-unreachable"], "type": "string", "description": "'echo-reply': Type 129, echo reply; 'echo-request': help Type 128, echo request; 'packet-too-big': Type 2, packet too big; 'param-prob': Type 4, parameter problem; 'time-exceeded': Type 3, time exceeded; 'dest-unreachable': Type 1, destination unreachable; ", "format": "enum"}, "src-eq": {"description": "Match only packets on a given source port (port number)", "format": "number", "not-list": ["src-gt", "src-lt"], "maximum": 65535, "minimum": 1, "type": "number"}, "dst-host": {"not-list": ["dst-any", "dst-object-group"], "type": "string", "description": "A single destination host (Host address)", "format": "ipv6-address"}}}]}, "name": {"description": "Named Access List", "format": "string", "minLength": 1, "optional": false, "maxLength": 16, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/ipv6/access-list/{name}"}
    :param prefix_list_list: {"minItems": 1, "items": {"type": "prefix-list"}, "uniqueItems": true, "array": [{"required": ["name"], "properties": {"rules": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"le": {"description": "Maximum prefix length to be matched", "minimum": 0, "type": "number", "maximum": 128, "format": "number"}, "description": {"minLength": 1, "maxLength": 80, "type": "string", "description": "Prefix-list specific description (Up to 80 characters describing this prefix-list)", "format": "string"}, "seq": {"description": "Sequence number of an entry", "minimum": 1, "type": "number", "maximum": 4294967295, "format": "number"}, "ipaddr": {"type": "string", "description": "IPv6 prefix, e.g., 3ffe::/16", "format": "ipv6-address-plen"}, "ge": {"description": "Minimum prefix length to be matched", "minimum": 0, "type": "number", "maximum": 128, "format": "number"}, "action": {"enum": ["deny", "permit"], "type": "string", "description": "'deny': Specify packets to reject; 'permit': Specify packets to forward; ", "format": "enum"}, "optional": true, "any": {"default": 0, "type": "number", "description": "Any prefix match. Same as \"::0/0 le le 128\"", "format": "flag"}}}]}, "name": {"description": "Name of a prefix list", "format": "string", "minLength": 1, "optional": false, "maxLength": 128, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/ipv6/prefix-list/{name}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ipv6`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "ipv6"
        self.a10_url="/axapi/v3/ipv6"
        self.DeviceProxy = ""
        self.frag = {}
        self.nat = {}
        self.route = {}
        self.access_list_list = []
        self.icmpv6 = {}
        self.default_gateway = {}
        self.neighbor = {}
        self.address = {}
        self.prefix_list_list = []
        self.ospf = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


