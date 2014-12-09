from a10sdk.common.A10BaseClass import A10BaseClass


class RedistList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param type: {"enum": ["bgp", "connected", "floating-ip", "ip-nat-list", "lw4o6", "isis", "rip", "static"], "type": "string", "description": "'bgp': Border Gateway Protocol (BGP); 'connected': Connected; 'floating-ip': Floating IP; 'ip-nat-list': IP NAT list; 'lw4o6': LW4O6 Prefix; 'isis': ISO IS-IS; 'rip': Routing Information Protocol (RIP); 'static': Static routes; ", "format": "enum"}
    :param metric: {"description": "OSPF default metric (OSPF metric)", "minimum": 0, "type": "number", "maximum": 16777214, "format": "number"}
    :param route_map: {"minLength": 1, "maxLength": 128, "type": "string", "description": "Route map reference (Pointer to route-map entries)", "format": "string"}
    :param tag: {"description": "Set tag for routes redistributed into OSPF (32-bit tag value)", "minimum": 0, "type": "number", "maximum": 4294967295, "format": "number"}
    :param metric_type: {"default": "2", "enum": ["1", "2"], "type": "string", "description": "'1': Set OSPF External Type 1 metrics; '2': Set OSPF External Type 2 metrics; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "redist-list"
        self.DeviceProxy = ""
        self.A10WW_type = ""
        self.metric = ""
        self.route_map = ""
        self.tag = ""
        self.metric_type = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class OspfList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param tag_ospf: {"description": "Set tag for routes redistributed into OSPF (32-bit tag value)", "minimum": 0, "type": "number", "maximum": 4294967295, "format": "number"}
    :param process_id: {"description": "OSPF process ID", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}
    :param route_map_ospf: {"minLength": 1, "maxLength": 128, "type": "string", "description": "Route map reference (Pointer to route-map entries)", "format": "string"}
    :param metric_ospf: {"description": "OSPF default metric (OSPF metric)", "minimum": 0, "type": "number", "maximum": 16777214, "format": "number"}
    :param ospf: {"default": 0, "type": "number", "description": "Open Shortest Path First (OSPF)", "format": "flag"}
    :param metric_type_ospf: {"default": "2", "enum": ["1", "2"], "type": "string", "description": "'1': Set OSPF External Type 1 metrics; '2': Set OSPF External Type 2 metrics; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ospf-list"
        self.DeviceProxy = ""
        self.tag_ospf = ""
        self.process_id = ""
        self.route_map_ospf = ""
        self.metric_ospf = ""
        self.ospf = ""
        self.metric_type_ospf = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class IpNatFloatingList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ip_nat_floating_IP_forward: {"type": "string", "description": "Floating-IP as forward address", "format": "ipv4-address"}
    :param ip_nat_prefix: {"type": "string", "description": "Address", "format": "ipv4-cidr"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ip-nat-floating-list"
        self.DeviceProxy = ""
        self.ip_nat_floating_IP_forward = ""
        self.ip_nat_prefix = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class VipFloatingList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param vip_address: {"type": "string", "description": "Address", "format": "ipv4-address"}
    :param vip_floating_IP_forward: {"type": "string", "description": "Floating-IP as forward address", "format": "ipv4-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "vip-floating-list"
        self.DeviceProxy = ""
        self.vip_address = ""
        self.vip_floating_IP_forward = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class VipList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param metric_type_vip: {"default": "2", "enum": ["1", "2"], "type": "string", "description": "'1': Set OSPF External Type 1 metrics; '2': Set OSPF External Type 2 metrics; ", "format": "enum"}
    :param tag_vip: {"type": "number", "description": "Set tag for routes redistributed into OSPF (32-bit tag value)", "format": "number"}
    :param metric_vip: {"description": "OSPF default metric (OSPF metric)", "minimum": 0, "type": "number", "maximum": 16777214, "format": "number"}
    :param route_map_vip: {"minLength": 1, "maxLength": 128, "type": "string", "description": "Route map reference (Pointer to route-map entries)", "format": "string"}
    :param type_vip: {"enum": ["only-flagged", "only-not-flagged"], "type": "string", "description": "'only-flagged': Selected Virtual IP (VIP); 'only-not-flagged': Only not flagged; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "vip-list"
        self.DeviceProxy = ""
        self.metric_type_vip = ""
        self.tag_vip = ""
        self.metric_vip = ""
        self.route_map_vip = ""
        self.type_vip = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Redistribute(A10BaseClass):
    
    """Class Description::
    Redistribute information from another routing protocol.

    Class redistribute supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param redist_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"type": {"enum": ["bgp", "connected", "floating-ip", "ip-nat-list", "lw4o6", "isis", "rip", "static"], "type": "string", "description": "'bgp': Border Gateway Protocol (BGP); 'connected': Connected; 'floating-ip': Floating IP; 'ip-nat-list': IP NAT list; 'lw4o6': LW4O6 Prefix; 'isis': ISO IS-IS; 'rip': Routing Information Protocol (RIP); 'static': Static routes; ", "format": "enum"}, "metric": {"description": "OSPF default metric (OSPF metric)", "minimum": 0, "type": "number", "maximum": 16777214, "format": "number"}, "route-map": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Route map reference (Pointer to route-map entries)", "format": "string"}, "tag": {"description": "Set tag for routes redistributed into OSPF (32-bit tag value)", "minimum": 0, "type": "number", "maximum": 4294967295, "format": "number"}, "optional": true, "metric-type": {"default": "2", "enum": ["1", "2"], "type": "string", "description": "'1': Set OSPF External Type 1 metrics; '2': Set OSPF External Type 2 metrics; ", "format": "enum"}}}]}
    :param ospf_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "tag-ospf": {"description": "Set tag for routes redistributed into OSPF (32-bit tag value)", "minimum": 0, "type": "number", "maximum": 4294967295, "format": "number"}, "process-id": {"description": "OSPF process ID", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}, "route-map-ospf": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Route map reference (Pointer to route-map entries)", "format": "string"}, "metric-ospf": {"description": "OSPF default metric (OSPF metric)", "minimum": 0, "type": "number", "maximum": 16777214, "format": "number"}, "ospf": {"default": 0, "type": "number", "description": "Open Shortest Path First (OSPF)", "format": "flag"}, "metric-type-ospf": {"default": "2", "enum": ["1", "2"], "type": "string", "description": "'1': Set OSPF External Type 1 metrics; '2': Set OSPF External Type 2 metrics; ", "format": "enum"}}}]}
    :param ip_nat_floating_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"ip-nat-floating-IP-forward": {"type": "string", "description": "Floating-IP as forward address", "format": "ipv4-address"}, "optional": true, "ip-nat-prefix": {"type": "string", "description": "Address", "format": "ipv4-cidr"}}}]}
    :param vip: {"default": 0, "optional": true, "type": "number", "description": "Virtual IP (VIP)", "format": "flag"}
    :param tag_ip_nat: {"optional": true, "type": "number", "description": "Set tag for routes redistributed into OSPF (32-bit tag value)", "format": "number"}
    :param ip_nat: {"default": 0, "optional": true, "type": "number", "description": "IP-NAT", "format": "flag"}
    :param metric_ip_nat: {"description": "OSPF default metric (OSPF metric)", "format": "number", "type": "number", "maximum": 16777214, "minimum": 0, "optional": true}
    :param route_map_ip_nat: {"description": "Route map reference (Pointer to route-map entries)", "format": "string", "minLength": 1, "optional": true, "maxLength": 128, "type": "string"}
    :param vip_floating_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "vip-address": {"type": "string", "description": "Address", "format": "ipv4-address"}, "vip-floating-IP-forward": {"type": "string", "description": "Floating-IP as forward address", "format": "ipv4-address"}}}]}
    :param metric_type_ip_nat: {"description": "'1': Set OSPF External Type 1 metrics; '2': Set OSPF External Type 2 metrics; ", "format": "enum", "default": "2", "type": "string", "enum": ["1", "2"], "optional": true}
    :param vip_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"metric-type-vip": {"default": "2", "enum": ["1", "2"], "type": "string", "description": "'1': Set OSPF External Type 1 metrics; '2': Set OSPF External Type 2 metrics; ", "format": "enum"}, "tag-vip": {"type": "number", "description": "Set tag for routes redistributed into OSPF (32-bit tag value)", "format": "number"}, "metric-vip": {"description": "OSPF default metric (OSPF metric)", "minimum": 0, "type": "number", "maximum": 16777214, "format": "number"}, "route-map-vip": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Route map reference (Pointer to route-map entries)", "format": "string"}, "optional": true, "type-vip": {"enum": ["only-flagged", "only-not-flagged"], "type": "string", "description": "'only-flagged': Selected Virtual IP (VIP); 'only-not-flagged': Only not flagged; ", "format": "enum"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/router/ospf/{process_id}/redistribute`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "redistribute"
        self.a10_url="/axapi/v3/router/ospf/{process_id}/redistribute"
        self.DeviceProxy = ""
        self.redist_list = []
        self.ospf_list = []
        self.ip_nat_floating_list = []
        self.vip = ""
        self.tag_ip_nat = ""
        self.ip_nat = ""
        self.metric_ip_nat = ""
        self.route_map_ip_nat = ""
        self.vip_floating_list = []
        self.metric_type_ip_nat = ""
        self.vip_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


