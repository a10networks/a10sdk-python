from a10sdk.common.A10BaseClass import A10BaseClass


class IpNexthopLif(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param cpu_process_1: {"default": 0, "type": "number", "description": "CPU rather than HW handle this entity", "plat-neg-list": ["non-fpga", "soft-ax"], "format": "flag"}
    :param lif: {"description": "LIF Interface (Logical tunnel interface number)", "minimum": 1, "type": "number", "maximum": 128, "format": "number"}
    :param description_nexthop_lif: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Description for static route", "format": "string-rlx"}
    :param distance_nexthop_lif: {"description": "Distance value for this route", "format": "number", "default": 1, "maximum": 255, "minimum": 1, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ip-nexthop-lif"
        self.DeviceProxy = ""
        self.cpu_process_1 = ""
        self.lif = ""
        self.description_nexthop_lif = ""
        self.distance_nexthop_lif = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class IpNexthopIpv4(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param cpu_process_3: {"default": 0, "type": "number", "description": "CPU rather than HW handle this entity", "plat-neg-list": ["non-fpga", "soft-ax"], "format": "flag"}
    :param description_nexthop_ip: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Description for static route", "format": "string-rlx"}
    :param ip_next_hop: {"type": "string", "description": "Forwarding router's address", "format": "ipv4-address"}
    :param distance_nexthop_ip: {"description": "Distance value for this route", "format": "number", "default": 1, "maximum": 255, "minimum": 1, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ip-nexthop-ipv4"
        self.DeviceProxy = ""
        self.cpu_process_3 = ""
        self.description_nexthop_ip = ""
        self.ip_next_hop = ""
        self.distance_nexthop_ip = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class IpNexthopTunnel(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param description_nexthop_tunnel: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Description for static route", "format": "string-rlx"}
    :param tunnel: {"description": "Tunnel interface (Tunnel interface number)", "minimum": 1, "type": "number", "maximum": 128, "format": "number"}
    :param ip_next_hop_tunnel: {"type": "string", "description": "Forwarding router's address", "format": "ipv4-address"}
    :param distance_nexthop_tunnel: {"description": "Distance value for this route", "format": "number", "default": 1, "maximum": 255, "minimum": 1, "type": "number"}
    :param cpu_process_2: {"default": 0, "type": "number", "description": "CPU rather than HW handle this entity", "plat-neg-list": ["non-fpga", "soft-ax"], "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ip-nexthop-tunnel"
        self.DeviceProxy = ""
        self.description_nexthop_tunnel = ""
        self.tunnel = ""
        self.ip_next_hop_tunnel = ""
        self.distance_nexthop_tunnel = ""
        self.cpu_process_2 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class IpNexthopPartition(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param partition_name: {"minLength": 1, "maxLength": 14, "type": "string", "description": "Name of network partition", "format": "string"}
    :param vrid_num_in_partition: {"description": "Specify ha VRRP-A vrid", "minimum": 0, "type": "number", "maximum": 31, "format": "number"}
    :param description_partition_vrid: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Description for static route", "format": "string-rlx"}
    :param description_nexthop_partition: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Description for static route", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ip-nexthop-partition"
        self.DeviceProxy = ""
        self.partition_name = ""
        self.vrid_num_in_partition = ""
        self.description_partition_vrid = ""
        self.description_nexthop_partition = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Rib(A10BaseClass):
    
    """Class Description::
    Establish static routes.

    Class rib supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ip_nexthop_lif: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"cpu-process-1": {"default": 0, "type": "number", "description": "CPU rather than HW handle this entity", "plat-neg-list": ["non-fpga", "soft-ax"], "format": "flag"}, "lif": {"description": "LIF Interface (Logical tunnel interface number)", "minimum": 1, "type": "number", "maximum": 128, "format": "number"}, "description-nexthop-lif": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Description for static route", "format": "string-rlx"}, "distance-nexthop-lif": {"description": "Distance value for this route", "format": "number", "default": 1, "maximum": 255, "minimum": 1, "type": "number"}, "optional": true}}]}
    :param ip_nexthop_ipv4: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "cpu-process-3": {"default": 0, "type": "number", "description": "CPU rather than HW handle this entity", "plat-neg-list": ["non-fpga", "soft-ax"], "format": "flag"}, "description-nexthop-ip": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Description for static route", "format": "string-rlx"}, "ip-next-hop": {"type": "string", "description": "Forwarding router's address", "format": "ipv4-address"}, "distance-nexthop-ip": {"description": "Distance value for this route", "format": "number", "default": 1, "maximum": 255, "minimum": 1, "type": "number"}}}]}
    :param ip_dest_addr: {"optional": false, "type": "string", "description": "Destination prefix", "format": "ipv4-address"}
    :param ip_nexthop_tunnel: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"description-nexthop-tunnel": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Description for static route", "format": "string-rlx"}, "tunnel": {"description": "Tunnel interface (Tunnel interface number)", "minimum": 1, "type": "number", "maximum": 128, "format": "number"}, "ip-next-hop-tunnel": {"type": "string", "description": "Forwarding router's address", "format": "ipv4-address"}, "distance-nexthop-tunnel": {"description": "Distance value for this route", "format": "number", "default": 1, "maximum": 255, "minimum": 1, "type": "number"}, "optional": true, "cpu-process-2": {"default": 0, "type": "number", "description": "CPU rather than HW handle this entity", "plat-neg-list": ["non-fpga", "soft-ax"], "format": "flag"}}}]}
    :param ip_nexthop_partition: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"partition-name": {"minLength": 1, "maxLength": 14, "type": "string", "description": "Name of network partition", "format": "string"}, "vrid-num-in-partition": {"description": "Specify ha VRRP-A vrid", "minimum": 0, "type": "number", "maximum": 31, "format": "number"}, "optional": true, "description-partition-vrid": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Description for static route", "format": "string-rlx"}, "description-nexthop-partition": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Description for static route", "format": "string-rlx"}}}]}
    :param ip_mask: {"optional": false, "type": "string", "description": "Destination prefix mask", "format": "ipv4-netmask-brief"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ip/route/rib/{ip_dest_addr}+{ip_mask}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "ip_dest_addr","ip_mask"]

        self.b_key = "rib"
        self.a10_url="/axapi/v3/ip/route/rib/{ip_dest_addr}+{ip_mask}"
        self.DeviceProxy = ""
        self.ip_nexthop_lif = []
        self.ip_nexthop_ipv4 = []
        self.ip_dest_addr = ""
        self.ip_nexthop_tunnel = []
        self.ip_nexthop_partition = []
        self.ip_mask = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


