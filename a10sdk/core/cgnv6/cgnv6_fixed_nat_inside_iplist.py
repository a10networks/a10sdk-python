from a10sdk.common.A10BaseClass import A10BaseClass


class UsableNatPorts(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param usable_start_port: {"description": "Start Port of Usable NAT Ports", "minimum": 1024, "type": "number", "maximum": 65535, "format": "number"}
    :param usable_end_port: {"description": "End Port of Usable NAT Ports", "minimum": 1024, "type": "number", "maximum": 65535, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "usable-nat-ports"
        self.DeviceProxy = ""
        self.usable_start_port = ""
        self.usable_end_port = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Offset(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param numeric_offset: {"description": "Configure a numeric offset to the first NAT IP address", "format": "number", "default": 0, "maximum": 1024000, "minimum": 0, "not": "random", "type": "number"}
    :param random: {"default": 0, "not": "numeric-offset", "type": "number", "description": "Randomly choose the first NAT IP address", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "offset"
        self.DeviceProxy = ""
        self.numeric_offset = ""
        self.random = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Iplist(A10BaseClass):
    
    """Class Description::
    Configure Fixed NAT with Inside IP List.

    Class iplist supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ports_per_user: {"description": "Configure Ports per Inside User (ports-per-user)", "format": "number", "type": "number", "maximum": 64512, "minimum": 1, "optional": true}
    :param vrid: {"description": "VRRP-A vrid (Specify ha VRRP-A vrid)", "format": "number", "type": "number", "maximum": 31, "minimum": 1, "optional": true}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param nat_end_address: {"optional": true, "type": "string", "description": "IPv4 End NAT Address", "format": "ipv4-address"}
    :param partition: {"description": "Inside User Partition (Partition Name)", "partition-visibility": "shared", "minLength": 1, "format": "string", "optional": false, "maxLength": 63, "type": "string"}
    :param nat_netmask: {"optional": true, "type": "string", "description": "NAT Addresses IP Netmask", "format": "ipv4-netmask"}
    :param inside_ip_list: {"description": "Name of IP List used to specify Inside Users", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param session_quota: {"description": "Configure per user quota on sessions", "format": "number", "type": "number", "maximum": 2147483647, "minimum": 1, "optional": true}
    :param nat_start_address: {"optional": true, "type": "string", "description": "Start NAT Address", "format": "ipv4-address"}
    :param nat_ip_list: {"description": "Name of IP List used to specify NAT addresses", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param respond_to_user_mac: {"default": 0, "optional": true, "type": "number", "description": "Use the user's source MAC for the next hop rather than the routing table (Default: off)", "format": "flag"}
    :param method: {"description": "'use-all-nat-ips': Use all the NAT IP addresses configured; 'use-least-nat-ips': Use the least number of NAT IP addresses required (default); ", "format": "enum", "default": "use-least-nat-ips", "type": "string", "enum": ["use-all-nat-ips", "use-least-nat-ips"], "optional": true}
    :param dest_rule_list: {"description": "Bind destination based Rule-List (Fixed NAT Rule-List Name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param dynamic_pool_size: {"description": "Configure size of Dynamic pool (Default: 0)", "format": "number", "default": 0, "optional": true, "maximum": 64511, "minimum": 0, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/fixed-nat/inside/iplist/{inside_ip_list}+{partition}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "inside_ip_list","partition"]

        self.b_key = "iplist"
        self.a10_url="/axapi/v3/cgnv6/fixed-nat/inside/iplist/{inside_ip_list}+{partition}"
        self.DeviceProxy = ""
        self.ports_per_user = ""
        self.vrid = ""
        self.uuid = ""
        self.nat_end_address = ""
        self.partition = ""
        self.nat_netmask = ""
        self.inside_ip_list = ""
        self.session_quota = ""
        self.usable_nat_ports = {}
        self.nat_start_address = ""
        self.nat_ip_list = ""
        self.offset = {}
        self.respond_to_user_mac = ""
        self.method = ""
        self.dest_rule_list = ""
        self.dynamic_pool_size = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


