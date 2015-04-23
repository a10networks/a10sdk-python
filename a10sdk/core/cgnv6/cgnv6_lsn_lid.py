from a10sdk.common.A10BaseClass import A10BaseClass


class Udp(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param udp_sessions: {"description": "Number of Extended Quota sessions allowed for this service", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}
    :param udp_service_port: {"description": "Port (Port Value)", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "udp"
        self.DeviceProxy = ""
        self.udp_sessions = ""
        self.udp_service_port = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Tcp(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param tcp_service_port: {"description": "Port (Port Value)", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}
    :param tcp_sessions: {"description": "Number of Extended Quota sessions allowed for this service", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "tcp"
        self.DeviceProxy = ""
        self.tcp_service_port = ""
        self.tcp_sessions = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class ExtendedUserQuota(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param udp: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"udp-sessions": {"description": "Number of Extended Quota sessions allowed for this service", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}, "optional": true, "udp-service-port": {"description": "Port (Port Value)", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}}}]}
    :param tcp: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"tcp-service-port": {"description": "Port (Port Value)", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}, "optional": true, "tcp-sessions": {"description": "Number of Extended Quota sessions allowed for this service", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "extended-user-quota"
        self.DeviceProxy = ""
        self.udp = []
        self.tcp = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class DsLite(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param inside_src_permit_list: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Class-List of IPv4 addresses permitted (Class-list to match for DS-Lite)", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ds-lite"
        self.DeviceProxy = ""
        self.inside_src_permit_list = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class QuotaTcp(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param tcp_quota: {"description": "NAT port quota per user (default: not configured)", "minimum": 1, "type": "number", "maximum": 64000, "format": "number"}
    :param tcp_reserve: {"description": "Number of ports to reserve per user (default: same as user-quota value) (Reserved quota per user (default: same as user-quota value))", "minimum": 0, "type": "number", "maximum": 64000, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "quota-tcp"
        self.DeviceProxy = ""
        self.tcp_quota = ""
        self.tcp_reserve = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class QuotaUdp(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param udp_reserve: {"description": "Number of ports to reserve per user (default: same as user-quota value) (Reserved quota per user (default: same as user-quota value))", "minimum": 0, "type": "number", "maximum": 64000, "format": "number"}
    :param udp_quota: {"description": "NAT port quota per user (default: not configured)", "minimum": 1, "type": "number", "maximum": 64000, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "quota-udp"
        self.DeviceProxy = ""
        self.udp_reserve = ""
        self.udp_quota = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class UserQuota(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param session: {"description": "User Quota for number of data sessions", "minimum": 1, "type": "number", "maximum": 2147483647, "format": "number"}
    :param icmp: {"description": "User Quota for ICMP identifiers (NAT port quota per user (default: not configured))", "minimum": 1, "type": "number", "maximum": 64000, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "user-quota"
        self.DeviceProxy = ""
        self.session = ""
        self.quota_tcp = {}
        self.icmp = ""
        self.quota_udp = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class SourceNatPool(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param shared: {"default": 0, "type": "number", "description": "Use a shared source NAT pool or pool-group", "format": "flag"}
    :param pool_name: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Source NAT Pool or Pool-Group", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "source-nat-pool"
        self.DeviceProxy = ""
        self.shared = ""
        self.pool_name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class ConnRateLimit(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param conn_rate_limit_val: {"description": "Maximum connections per second (Default: No limit)", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "conn-rate-limit"
        self.DeviceProxy = ""
        self.conn_rate_limit_val = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class LsnRuleList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param destination: {"description": "Apply LSN Rule-List on Destination (LSN Rule-List Name)", "format": "string-rlx", "minLength": 1, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/cgnv6/lsn-rule-list"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "lsn-rule-list"
        self.DeviceProxy = ""
        self.destination = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class LsnLid(A10BaseClass):
    
    """Class Description::
    Create an LSN Lid.

    Class lsn-lid supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param drop_on_nat_pool_mismatch: {"default": 0, "optional": true, "type": "number", "description": "Drop traffic from users if their current NAT pool does not match the lid's (default: off)", "format": "flag"}
    :param user_quota_prefix_length: {"description": "NAT64 user quota prefix length (Prefix Length (Default: Uses the global NAT64 configured value))", "format": "number", "type": "number", "maximum": 128, "minimum": 1, "optional": true}
    :param lid_number: {"description": "LSN Lid", "format": "number", "type": "number", "maximum": 1023, "minimum": 1, "optional": false}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param override: {"description": "'none': Apply source NAT if configured (default); 'drop': Drop packets that match this LSN lid; 'pass-through': Layer-3 route packets that match this LSN lid and do not apply source NAT; ", "format": "enum", "default": "none", "type": "string", "enum": ["none", "drop", "pass-through"], "optional": true}
    :param respond_to_user_mac: {"default": 0, "optional": true, "type": "number", "description": "Use the user's source MAC for the next hop rather than the routing table (default: off)", "format": "flag"}
    :param name: {"description": "LSN Lid Name", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/lsn-lid/{lid_number}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "lid_number"]

        self.b_key = "lsn-lid"
        self.a10_url="/axapi/v3/cgnv6/lsn-lid/{lid_number}"
        self.DeviceProxy = ""
        self.drop_on_nat_pool_mismatch = ""
        self.user_quota_prefix_length = ""
        self.lid_number = ""
        self.extended_user_quota = {}
        self.ds_lite = {}
        self.user_quota = {}
        self.uuid = ""
        self.override = ""
        self.source_nat_pool = {}
        self.conn_rate_limit = {}
        self.lsn_rule_list = {}
        self.respond_to_user_mac = ""
        self.name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


