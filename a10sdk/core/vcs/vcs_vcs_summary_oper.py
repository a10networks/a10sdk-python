from a10sdk.common.A10BaseClass import A10BaseClass


class FloatingIpv6List(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param floating_ipv6: {"type": "string", "format": "string"}
    :param floating_ipv6_prefix: {"type": "number", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "floating-ipv6-list"
        self.DeviceProxy = ""
        self.floating_ipv6 = ""
        self.floating_ipv6_prefix = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class IpList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ip: {"type": "string", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ip-list"
        self.DeviceProxy = ""
        self.ip = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class MemberList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param port: {"type": "number", "format": "number"}
    :param priority: {"type": "number", "format": "number"}
    :param state: {"type": "string", "format": "string"}
    :param ip_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"ip": {"type": "string", "format": "string"}, "optional": true}}]}
    :param location: {"type": "string", "format": "string"}
    :param id: {"type": "number", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "member-list"
        self.DeviceProxy = ""
        self.port = ""
        self.priority = ""
        self.state = ""
        self.ip_list = []
        self.location = ""
        self.A10WW_id = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class FloatingIpv4List(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param floating_ipv4_mask: {"type": "string", "format": "string"}
    :param floating_ipv4: {"type": "string", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "floating-ipv4-list"
        self.DeviceProxy = ""
        self.floating_ipv4_mask = ""
        self.floating_ipv4 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param chassis_id: {"type": "number", "format": "number"}
    :param multicast_port: {"type": "number", "format": "number"}
    :param floating_ipv6_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"floating-ipv6": {"type": "string", "format": "string"}, "optional": true, "floating-ipv6-prefix": {"type": "number", "format": "number"}}}]}
    :param multicast_addr: {"type": "string", "format": "string"}
    :param vmaster_maintenance_interval: {"type": "number", "format": "number"}
    :param version: {"type": "string", "format": "string"}
    :param vmaster_maintenance_left: {"type": "number", "format": "number"}
    :param member_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"port": {"type": "number", "format": "number"}, "priority": {"type": "number", "format": "number"}, "state": {"type": "string", "format": "string"}, "ip-list": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"ip": {"type": "string", "format": "string"}, "optional": true}}]}, "location": {"type": "string", "format": "string"}, "optional": true, "id": {"type": "number", "format": "number"}}}]}
    :param floating_ipv4_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"floating-ipv4-mask": {"type": "string", "format": "string"}, "floating-ipv4": {"type": "string", "format": "string"}, "optional": true}}]}
    :param vcs_enabled: {"type": "string", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.chassis_id = ""
        self.multicast_port = ""
        self.floating_ipv6_list = []
        self.multicast_addr = ""
        self.vmaster_maintenance_interval = ""
        self.version = ""
        self.vmaster_maintenance_left = ""
        self.member_list = []
        self.floating_ipv4_list = []
        self.vcs_enabled = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class VcsSummary(A10BaseClass):
    
    """Class Description::
    Operational Status for the object vcs-summary.

    Class vcs-summary supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/vcs/vcs-summary/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "vcs-summary"
        self.a10_url="/axapi/v3/vcs/vcs-summary/oper"
        self.DeviceProxy = ""
        self.oper = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


