from a10sdk.common.A10BaseClass import A10BaseClass


class BroadcastRateLimit(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param rate: {"description": "packets per second. Default is 500. (packets per second. Please specify an even number. Default is 500)", "format": "number", "default": 500, "maximum": 5000, "minimum": 50, "type": "number"}
    :param bcast_rate_limit_enable: {"default": 0, "type": "number", "description": "Rate limit the l2 broadcast packet on mgmt port", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "broadcast-rate-limit"
        self.DeviceProxy = ""
        self.rate = ""
        self.bcast_rate_limit_enable = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Ipv6(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param inbound: {"default": 0, "type": "number", "description": "ACL applied on incoming packets to this interface", "format": "flag"}
    :param address_type: {"enum": ["link-local"], "type": "string", "description": "'link-local': Configure an IPv6 link local address; ", "format": "enum"}
    :param default_ipv6_gateway: {"type": "string", "description": "Set default gateway (Default gateway address)", "format": "ipv6-address"}
    :param ipv6_addr: {"type": "string", "description": "Set the IPv6 address of an interface", "format": "ipv6-address-plen"}
    :param v6_acl_name: {"description": "Apply ACL rules to incoming packets on this interface (Named Access List)", "format": "string", "minLength": 1, "maxLength": 32, "type": "string", "$ref": "/axapi/v3/ipv6/access-list"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ipv6"
        self.DeviceProxy = ""
        self.inbound = ""
        self.address_type = ""
        self.default_ipv6_gateway = ""
        self.ipv6_addr = ""
        self.v6_acl_name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Ip(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param dhcp: {"default": 0, "not": "ipv4-address", "type": "number", "description": "Use DHCP to configure IP address", "format": "flag"}
    :param ipv4_address: {"not": "dhcp", "type": "string", "description": "IP address", "format": "ipv4-address"}
    :param default_gateway: {"type": "string", "description": "Set default gateway (Default gateway address)", "format": "ipv4-address"}
    :param control_apps_use_mgmt_port: {"default": 0, "type": "number", "description": "Control applications use management port", "format": "flag"}
    :param ipv4_netmask: {"type": "string", "description": "IP subnet mask", "format": "ipv4-netmask"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ip"
        self.DeviceProxy = ""
        self.dhcp = ""
        self.ipv4_address = ""
        self.default_gateway = ""
        self.control_apps_use_mgmt_port = ""
        self.ipv4_netmask = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class AccessList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param acl_name: {"minLength": 1, "maxLength": 16, "type": "string", "description": "Apply an access list (Named Access List)", "format": "string"}
    :param acl_id: {"description": "ACL id", "format": "number", "maximum": 199, "minimum": 1, "type": "number", "$ref": "/axapi/v3/access-list/standard"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "access-list"
        self.DeviceProxy = ""
        self.acl_name = ""
        self.acl_id = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Management(A10BaseClass):
    
    """Class Description::
    Management interface.

    Class management supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param duplexity: {"description": "'Full': Full; 'Half': Half; 'auto': Auto; ", "format": "enum", "default": "auto", "type": "string", "enum": ["Full", "Half", "auto"], "optional": true}
    :param speed: {"description": "'10': 10 Mbs/sec; '100': 100 Mbs/sec; '1000': 1 Gb/sec; 'auto': Auto Negotiate Speed;  (Interface Speed)", "format": "enum", "default": "auto", "type": "string", "enum": ["10", "100", "1000", "auto"], "optional": true}
    :param action: {"optional": true, "enum": ["enable", "disable"], "type": "string", "description": "'enable': Enable Management Port; 'disable': Disable Management Port; ", "format": "enum"}
    :param flow_control: {"default": 0, "optional": true, "type": "number", "description": "Enable 802.3x flow control on full duplex port", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/interface/management`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "management"
        self.a10_url="/axapi/v3/interface/management"
        self.DeviceProxy = ""
        self.lldp = {}
        self.broadcast_rate_limit = {}
        self.uuid = ""
        self.duplexity = ""
        self.speed = ""
        self.ipv6 = {}
        self.action = ""
        self.ip = {}
        self.access_list = {}
        self.flow_control = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


