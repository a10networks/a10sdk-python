from a10sdk.common.A10BaseClass import A10BaseClass


class Rules(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param icmp_type: {"description": "ICMP type number", "format": "number", "not-list": ["any-type", "special-type"], "maximum": 254, "minimum": 0, "type": "number"}
    :param icmpv6_code: {"description": "ICMPv6 code number", "format": "number", "maximum": 254, "minimum": 0, "not": "v6-any-code", "type": "number"}
    :param lt_src: {"description": "Match only packets with a lower port number", "minimum": 2, "type": "number", "maximum": 65535, "format": "number"}
    :param eq_dst: {"description": "Match only packets on a given destination port (port number)", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}
    :param range_dst: {"description": "Match only packets in the range of port numbers (Starting Destination Port Number)", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}
    :param seq_num: {"description": "Sequence number", "minimum": 1, "type": "number", "maximum": 8192, "format": "number"}
    :param source: {"default": 0, "type": "number", "description": "Source Port Information", "format": "flag"}
    :param eq_src: {"description": "Match only packets on a given source port (port number)", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}
    :param v6_any_code: {"default": 0, "not": "icmpv6-code", "type": "number", "description": "Any ICMPv6 code", "format": "flag"}
    :param icmpv6_type: {"description": "ICMPv6 type number", "format": "number", "not-list": ["v6-any-type", "special-v6-type"], "maximum": 254, "minimum": 0, "type": "number"}
    :param icmp_code: {"description": "ICMP code number", "format": "number", "maximum": 254, "minimum": 0, "not": "any-code", "type": "number"}
    :param description: {"minLength": 1, "maxLength": 128, "type": "string", "description": "Description of the object-group instance", "format": "string-rlx"}
    :param special_code: {"not": "icmp-code", "enum": ["frag-required", "host-unreachable", "network-unreachable", "port-unreachable", "proto-unreachable", "route-failed"], "type": "string", "description": "'frag-required': Code 4, fragmentation required; 'host-unreachable': Code 1, destination host unreachable; 'network-unreachable': Code 0, destination network unreachable; 'port-unreachable': Code 3, destination port unreachable; 'proto-unreachable': Code 2, destination protocol unreachable; 'route-failed': Code 5, source route failed; ", "format": "enum"}
    :param tcp_udp: {"enum": ["tcp", "udp"], "type": "string", "description": "'tcp': Protocol TCP; 'udp': Protocol UDP; ", "format": "enum"}
    :param gt_dst: {"description": "Match only packets with a greater port number", "minimum": 1, "type": "number", "maximum": 65534, "format": "number"}
    :param icmp: {"default": 0, "type": "number", "description": "Internet Control Message Protocol", "format": "flag"}
    :param port_num_end_src: {"description": "Ending Port Number", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}
    :param special_v6_type: {"not-list": ["icmpv6-type", "v6-any-type"], "enum": ["dest-unreachable", "echo-reply", "echo-request", "packet-too-big", "param-prob", "time-exceeded"], "type": "string", "description": "'dest-unreachable': Type 1, destination unreachable; 'echo-reply': Type 129, echo reply; 'echo-request': Type 128, echo request; 'packet-too-big': Type 2, packet too big; 'param-prob': Type 4, parameter problem; 'time-exceeded': Type 3, time exceeded; ", "format": "enum"}
    :param any_type: {"default": 0, "not-list": ["icmp-type", "special-type"], "type": "number", "description": "Any ICMP type", "format": "flag"}
    :param lt_dst: {"description": "Match only packets with a lesser port number", "minimum": 2, "type": "number", "maximum": 65535, "format": "number"}
    :param gt_src: {"description": "Match only packets with a greater port number", "minimum": 1, "type": "number", "maximum": 65534, "format": "number"}
    :param special_v6_code: {"not": "icmpv6-code", "enum": ["addr-unreachable", "admin-prohibited", "no-route", "not-neighbour", "port-unreachable"], "type": "string", "description": "'addr-unreachable': Code 3, address unreachable; 'admin-prohibited': Code 1, admin prohibited; 'no-route': Code 0, no route to destination; 'not-neighbour': Code 2, not neighbor; 'port-unreachable': Code 4, destination port unreachable; ", "format": "enum"}
    :param icmpv6: {"default": 0, "type": "number", "description": "Internet Control Message Protocol version 6", "format": "flag"}
    :param range_src: {"description": "match only packets in the range of port numbers (Starting Port Number)", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}
    :param port_num_end_dst: {"description": "Ending Destination Port Number", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}
    :param v6_any_type: {"default": 0, "not-list": ["icmpv6-type", "special-v6-type"], "type": "number", "description": "Any ICMP type", "format": "flag"}
    :param any_code: {"default": 0, "not": "icmp-code", "type": "number", "description": "Any ICMP code", "format": "flag"}
    :param special_type: {"not-list": ["icmp-type", "any-type"], "enum": ["echo-reply", "echo-request", "info-reply", "info-request", "mask-reply", "mask-request", "parameter-problem", "redirect", "source-quench", "time-exceeded", "timestamp", "timestamp-reply", "dest-unreachable"], "type": "string", "description": "'echo-reply': Type 0, echo reply; 'echo-request': Type 8, echo request; 'info-reply': Type 16, information reply; 'info-request': Type 15, information request; 'mask-reply': Type 18, address mask reply; 'mask-request': Type 17, address mask request; 'parameter-problem': Type 12, parameter problem; 'redirect': Type 5, redirect message; 'source-quench': Type 4, source quench; 'time-exceeded': Type 11, time exceeded; 'timestamp': Type 13, timestamp; 'timestamp-reply': Type 14, timestamp reply; 'dest-unreachable': Type 3, destination unreachable; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "rules"
        self.DeviceProxy = ""
        self.icmp_type = ""
        self.icmpv6_code = ""
        self.lt_src = ""
        self.eq_dst = ""
        self.range_dst = ""
        self.seq_num = ""
        self.source = ""
        self.eq_src = ""
        self.v6_any_code = ""
        self.icmpv6_type = ""
        self.icmp_code = ""
        self.description = ""
        self.special_code = ""
        self.tcp_udp = ""
        self.gt_dst = ""
        self.icmp = ""
        self.port_num_end_src = ""
        self.special_v6_type = ""
        self.any_type = ""
        self.lt_dst = ""
        self.gt_src = ""
        self.special_v6_code = ""
        self.icmpv6 = ""
        self.range_src = ""
        self.port_num_end_dst = ""
        self.v6_any_type = ""
        self.any_code = ""
        self.special_type = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Service(A10BaseClass):
    
    """Class Description::
    Configure Service Object Group.

    Class service supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param rules: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"icmp-type": {"description": "ICMP type number", "format": "number", "not-list": ["any-type", "special-type"], "maximum": 254, "minimum": 0, "type": "number"}, "icmpv6-code": {"description": "ICMPv6 code number", "format": "number", "maximum": 254, "minimum": 0, "not": "v6-any-code", "type": "number"}, "lt-src": {"description": "Match only packets with a lower port number", "minimum": 2, "type": "number", "maximum": 65535, "format": "number"}, "eq-dst": {"description": "Match only packets on a given destination port (port number)", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}, "range-dst": {"description": "Match only packets in the range of port numbers (Starting Destination Port Number)", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}, "seq-num": {"description": "Sequence number", "minimum": 1, "type": "number", "maximum": 8192, "format": "number"}, "source": {"default": 0, "type": "number", "description": "Source Port Information", "format": "flag"}, "eq-src": {"description": "Match only packets on a given source port (port number)", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}, "v6-any-code": {"default": 0, "not": "icmpv6-code", "type": "number", "description": "Any ICMPv6 code", "format": "flag"}, "icmpv6-type": {"description": "ICMPv6 type number", "format": "number", "not-list": ["v6-any-type", "special-v6-type"], "maximum": 254, "minimum": 0, "type": "number"}, "icmp-code": {"description": "ICMP code number", "format": "number", "maximum": 254, "minimum": 0, "not": "any-code", "type": "number"}, "description": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Description of the object-group instance", "format": "string-rlx"}, "special-code": {"not": "icmp-code", "enum": ["frag-required", "host-unreachable", "network-unreachable", "port-unreachable", "proto-unreachable", "route-failed"], "type": "string", "description": "'frag-required': Code 4, fragmentation required; 'host-unreachable': Code 1, destination host unreachable; 'network-unreachable': Code 0, destination network unreachable; 'port-unreachable': Code 3, destination port unreachable; 'proto-unreachable': Code 2, destination protocol unreachable; 'route-failed': Code 5, source route failed; ", "format": "enum"}, "tcp-udp": {"enum": ["tcp", "udp"], "type": "string", "description": "'tcp': Protocol TCP; 'udp': Protocol UDP; ", "format": "enum"}, "gt-dst": {"description": "Match only packets with a greater port number", "minimum": 1, "type": "number", "maximum": 65534, "format": "number"}, "icmp": {"default": 0, "type": "number", "description": "Internet Control Message Protocol", "format": "flag"}, "optional": true, "port-num-end-src": {"description": "Ending Port Number", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}, "special-v6-type": {"not-list": ["icmpv6-type", "v6-any-type"], "enum": ["dest-unreachable", "echo-reply", "echo-request", "packet-too-big", "param-prob", "time-exceeded"], "type": "string", "description": "'dest-unreachable': Type 1, destination unreachable; 'echo-reply': Type 129, echo reply; 'echo-request': Type 128, echo request; 'packet-too-big': Type 2, packet too big; 'param-prob': Type 4, parameter problem; 'time-exceeded': Type 3, time exceeded; ", "format": "enum"}, "any-type": {"default": 0, "not-list": ["icmp-type", "special-type"], "type": "number", "description": "Any ICMP type", "format": "flag"}, "lt-dst": {"description": "Match only packets with a lesser port number", "minimum": 2, "type": "number", "maximum": 65535, "format": "number"}, "gt-src": {"description": "Match only packets with a greater port number", "minimum": 1, "type": "number", "maximum": 65534, "format": "number"}, "special-v6-code": {"not": "icmpv6-code", "enum": ["addr-unreachable", "admin-prohibited", "no-route", "not-neighbour", "port-unreachable"], "type": "string", "description": "'addr-unreachable': Code 3, address unreachable; 'admin-prohibited': Code 1, admin prohibited; 'no-route': Code 0, no route to destination; 'not-neighbour': Code 2, not neighbor; 'port-unreachable': Code 4, destination port unreachable; ", "format": "enum"}, "icmpv6": {"default": 0, "type": "number", "description": "Internet Control Message Protocol version 6", "format": "flag"}, "range-src": {"description": "match only packets in the range of port numbers (Starting Port Number)", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}, "port-num-end-dst": {"description": "Ending Destination Port Number", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}, "v6-any-type": {"default": 0, "not-list": ["icmpv6-type", "special-v6-type"], "type": "number", "description": "Any ICMP type", "format": "flag"}, "any-code": {"default": 0, "not": "icmp-code", "type": "number", "description": "Any ICMP code", "format": "flag"}, "special-type": {"not-list": ["icmp-type", "any-type"], "enum": ["echo-reply", "echo-request", "info-reply", "info-request", "mask-reply", "mask-request", "parameter-problem", "redirect", "source-quench", "time-exceeded", "timestamp", "timestamp-reply", "dest-unreachable"], "type": "string", "description": "'echo-reply': Type 0, echo reply; 'echo-request': Type 8, echo request; 'info-reply': Type 16, information reply; 'info-request': Type 15, information request; 'mask-reply': Type 18, address mask reply; 'mask-request': Type 17, address mask request; 'parameter-problem': Type 12, parameter problem; 'redirect': Type 5, redirect message; 'source-quench': Type 4, source quench; 'time-exceeded': Type 11, time exceeded; 'timestamp': Type 13, timestamp; 'timestamp-reply': Type 14, timestamp reply; 'dest-unreachable': Type 3, destination unreachable; ", "format": "enum"}}}]}
    :param svc_name: {"description": "Service Object Name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/object-group/service/{svc_name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "svc_name"]

        self.b_key = "service"
        self.a10_url="/axapi/v3/object-group/service/{svc_name}"
        self.DeviceProxy = ""
        self.rules = []
        self.svc_name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


