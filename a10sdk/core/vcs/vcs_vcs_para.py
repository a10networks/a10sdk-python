from a10sdk.common.A10BaseClass import A10BaseClass


class FloatingIpv6Cfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param floating_ipv6: {"type": "string", "description": "Floating IPv6 address", "format": "ipv6-address-plen"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "floating-ipv6-cfg"
        self.DeviceProxy = ""
        self.floating_ipv6 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class FloatingIpCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param floating_ip_mask: {"type": "string", "description": "Netmask", "format": "ipv4-netmask"}
    :param floating_ip: {"type": "string", "description": "Floating IP address (IPv4 address)", "format": "ipv4-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "floating-ip-cfg"
        self.DeviceProxy = ""
        self.floating_ip_mask = ""
        self.floating_ip = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class VcsPara(A10BaseClass):
    
    """    :param multicast_port: {"description": "Port used in multicast communication (Port number)", "format": "number", "default": 41217, "optional": true, "maximum": 65535, "minimum": 1, "type": "number"}
    :param dead_interval: {"description": "The node will be considered dead as lack of hearbeats after this time (in unit of second, 10 by default)", "format": "number", "default": 10, "optional": true, "maximum": 240, "minimum": 5, "type": "number"}
    :param forever: {"description": "VCS retry forever if fails to join the chassis", "format": "flag", "default": 0, "optional": true, "not": "failure-retry-count-value", "type": "number"}
    :param ssl_enable: {"default": 0, "optional": true, "type": "number", "description": "Enable SSL", "format": "flag"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param floating_ipv6_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"floating-ipv6": {"type": "string", "description": "Floating IPv6 address", "format": "ipv6-address-plen"}, "optional": true}}]}
    :param multicast_ipv6: {"not": "multicast-ip", "optional": true, "type": "string", "description": "Multicast (group) IPv6 address (Multicast IPv6 address)", "format": "ipv6-address"}
    :param force_wait_interval: {"description": "The node will wait the specified time interval before it start aVCS (in unit of second (default is 5))", "format": "number", "default": 5, "optional": true, "maximum": 240, "minimum": 5, "type": "number"}
    :param floating_ip_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"floating-ip-mask": {"type": "string", "description": "Netmask", "format": "ipv4-netmask"}, "floating-ip": {"type": "string", "description": "Floating IP address (IPv4 address)", "format": "ipv4-address"}, "optional": true}}]}
    :param failure_retry_count_value: {"description": "0-255, default is 2", "format": "number", "default": 2, "optional": true, "maximum": 255, "minimum": 0, "not": "forever", "type": "number"}
    :param time_interval: {"description": "how long between heartbeats (in unit of second, default is 3)", "format": "number", "default": 3, "optional": true, "maximum": 60, "minimum": 1, "type": "number"}
    :param config_seq: {"description": "Configuration sequence number", "format": "string", "minLength": 1, "optional": true, "maxLength": 128, "type": "string"}
    :param multicast_ip: {"description": "Multicast (group) IP address (Multicast IP address)", "format": "ipv4-address", "default": "224.0.0.210", "optional": true, "not": "multicast-ipv6", "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Virtual Chassis System Paramter.

    Class vcs-para supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/vcs/vcs-para`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "vcs-para"
        self.a10_url="/axapi/v3/vcs/vcs-para"
        self.DeviceProxy = ""
        self.multicast_port = ""
        self.dead_interval = ""
        self.forever = ""
        self.ssl_enable = ""
        self.uuid = ""
        self.floating_ipv6_cfg = []
        self.multicast_ipv6 = ""
        self.force_wait_interval = ""
        self.floating_ip_cfg = []
        self.failure_retry_count_value = ""
        self.time_interval = ""
        self.config_seq = ""
        self.multicast_ip = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


