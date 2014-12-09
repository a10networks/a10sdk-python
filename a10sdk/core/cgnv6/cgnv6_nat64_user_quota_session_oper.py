from a10sdk.common.A10BaseClass import A10BaseClass


class SessionList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param lid_number: {"type": "number", "format": "number"}
    :param tcp_quota: {"minimum": 1, "type": "number", "maximum": 65535, "format": "number"}
    :param nat_address: {"type": "string", "format": "ipv4-address"}
    :param icmp_quota: {"minimum": 1, "type": "number", "maximum": 65535, "format": "number"}
    :param nat_pool_name: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param session_count: {"type": "number", "format": "number"}
    :param inside_address: {"type": "string", "format": "ipv6-address"}
    :param udp_quota: {"minimum": 1, "type": "number", "maximum": 65535, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "session-list"
        self.DeviceProxy = ""
        self.lid_number = ""
        self.tcp_quota = ""
        self.nat_address = ""
        self.icmp_quota = ""
        self.nat_pool_name = ""
        self.session_count = ""
        self.inside_address = ""
        self.udp_quota = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param prefix_filter: {"type": "string", "format": "ipv6-address-plen"}
    :param session_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"lid-number": {"type": "number", "format": "number"}, "tcp-quota": {"minimum": 1, "type": "number", "maximum": 65535, "format": "number"}, "nat-address": {"type": "string", "format": "ipv4-address"}, "icmp-quota": {"minimum": 1, "type": "number", "maximum": 65535, "format": "number"}, "nat-pool-name": {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}, "session-count": {"type": "number", "format": "number"}, "optional": true, "inside-address": {"type": "string", "format": "ipv6-address"}, "udp-quota": {"minimum": 1, "type": "number", "maximum": 65535, "format": "number"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.prefix_filter = ""
        self.session_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class UserQuotaSession(A10BaseClass):
    
    """Class Description::
    Operational Status for the object user-quota-session.

    Class user-quota-session supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/nat64/user-quota-session/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "user-quota-session"
        self.a10_url="/axapi/v3/cgnv6/nat64/user-quota-session/oper"
        self.DeviceProxy = ""
        self.oper = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


