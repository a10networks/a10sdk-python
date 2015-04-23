from a10sdk.common.A10BaseClass import A10BaseClass


class Pool(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param template: {"description": "Bind a NAT logging template", "format": "string-rlx", "minLength": 1, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/cgnv6/template/logging"}
    :param pool_name: {"minLength": 1, "maxLength": 63, "type": "string", "description": "NAT pool", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "pool"
        self.DeviceProxy = ""
        self.template = ""
        self.pool_name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Logging(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param pool: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "template": {"description": "Bind a NAT logging template", "format": "string-rlx", "minLength": 1, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/cgnv6/template/logging"}, "pool-name": {"minLength": 1, "maxLength": 63, "type": "string", "description": "NAT pool", "format": "string-rlx"}}}]}
    :param default_template: {"description": "Bind the default NAT logging template for LSN (Bind a NAT logging template)", "format": "string-rlx", "minLength": 1, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/cgnv6/template/logging"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "logging"
        self.DeviceProxy = ""
        self.pool = []
        self.default_template = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class PortBatching(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param tcp_time_wait_interval: {"description": "Minutes before TCP NAT ports can be reused (default: 2)", "format": "number", "default": 2, "maximum": 10, "minimum": 0, "type": "number"}
    :param size: {"default": "1", "enum": ["1", "8", "16", "32", "64", "128", "256", "512", "1024"], "type": "string", "description": "'1': Allocate 1 port at a time (default); '8': Allocate 8 ports at a time; '16': Allocate 16 ports at a time; '32': Allocate 32 ports at a time; '64': Allocate 64 ports at a time; '128': Allocate 128 ports at a time; '256': Allocate 256 ports at a time; '512': Allocate 512 ports at a time; '1024': Allocate 1024 ports at a time; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "port-batching"
        self.DeviceProxy = ""
        self.tcp_time_wait_interval = ""
        self.size = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Icmp(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param send_on_user_quota_exceeded: {"default": "admin-filtered", "enum": ["host-unreachable", "admin-filtered", "disable"], "type": "string", "description": "'host-unreachable': Send ICMP destination host unreachable; 'admin-filtered': Send ICMP admin filtered (default); 'disable': Disable ICMP quota exceeded message; ", "format": "enum"}
    :param send_on_port_unavailable: {"default": "disable", "enum": ["host-unreachable", "admin-filtered", "disable"], "type": "string", "description": "'host-unreachable': Send ICMP destination host unreachable; 'admin-filtered': Send ICMP admin filtered; 'disable': Disable ICMP port unavailable message (default); ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "icmp"
        self.DeviceProxy = ""
        self.send_on_user_quota_exceeded = ""
        self.send_on_port_unavailable = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Global(A10BaseClass):
    
    """    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param inbound_refresh: {"optional": true, "enum": ["disable"], "type": "string", "description": "'disable': Disable NAT Inbound Refresh Behavior; ", "format": "enum"}
    :param hairpinning: {"description": "'filter-none': Allow self-hairpinning (default). Warning: Only applies to UDP.  TCP will use filter-self-ip-port; 'filter-self-ip': Block hairpinning to the user's own IP; 'filter-self-ip-port': Block hairpinning to the user's same IP and port combination; ", "format": "enum", "default": "filter-none", "type": "string", "enum": ["filter-none", "filter-self-ip", "filter-self-ip-port"], "optional": true}
    :param attempt_port_preservation: {"optional": true, "enum": ["disable"], "type": "string", "description": "'disable': Don't attempt port preservation for NAT allocation; ", "format": "enum"}
    :param ip_selection: {"description": "'random': Random (long-run uniformly distributed) NAT IP selection (default); 'round-robin': Round-robin; 'least-used-strict': Fewest NAT ports used; 'least-udp-used-strict': Fewest UDP NAT ports used; 'least-tcp-used-strict': Fewest TCP NAT ports used; 'least-reserved-strict': Fewest NAT ports reserved; 'least-udp-reserved-strict': Fewest UDP NAT ports reserved; 'least-tcp-reserved-strict': Fewest TCP NAT ports reserved; 'least-users-strict': Fewest number of users; ", "format": "enum", "default": "random", "type": "string", "enum": ["random", "round-robin", "least-used-strict", "least-udp-used-strict", "least-tcp-used-strict", "least-reserved-strict", "least-udp-reserved-strict", "least-tcp-reserved-strict", "least-users-strict"], "optional": true}
    :param syn_timeout: {"description": "Set LSN SYN timeout (SYN idle-timeout in seconds (default: 4 seconds))", "format": "number", "default": 4, "optional": true, "maximum": 30, "minimum": 2, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Set Large-Scale NAT config parameters.

    Class global supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/lsn/global`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "global"
        self.a10_url="/axapi/v3/cgnv6/lsn/global"
        self.DeviceProxy = ""
        self.logging = {}
        self.uuid = ""
        self.inbound_refresh = ""
        self.hairpinning = ""
        self.port_batching = {}
        self.attempt_port_preservation = ""
        self.ip_selection = ""
        self.syn_timeout = ""
        self.icmp = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


