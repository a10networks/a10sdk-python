from a10sdk.common.A10BaseClass import A10BaseClass


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


class Vcs(A10BaseClass):
    
    """Class Description::
    Virtual Chassis System.

    Class vcs supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param multicast_port: {"description": "Port used in multicast communication (Port number)", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": true}
    :param dead_interval: {"description": "The node will be considered dead as lack of hearbeats after this time (in unit of second, 10 by default)", "format": "number", "default": 10, "optional": true, "maximum": 240, "minimum": 5, "type": "number"}
    :param force_wait_interval: {"description": "The node will wait the specified time interval before it start aVCS (in unit of second (default is 5))", "format": "number", "default": 5, "optional": true, "maximum": 240, "minimum": 5, "type": "number"}
    :param ssl_enable: {"default": 0, "optional": true, "type": "number", "description": "Enable SSL", "format": "flag"}
    :param multicast_ipv6: {"not": "multicast-ip", "optional": true, "type": "string", "description": "Multicast (group) IPv6 address (Multicast IPv6 address)", "format": "ipv6-address"}
    :param floating_ip_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"floating-ip-mask": {"type": "string", "description": "Netmask", "format": "ipv4-netmask"}, "floating-ip": {"type": "string", "description": "Floating IP address (IPv4 address)", "format": "ipv4-address"}, "optional": true}}]}
    :param device_list: {"minItems": 1, "items": {"type": "device"}, "uniqueItems": true, "array": [{"required": ["device"], "properties": {"management": {"default": 0, "optional": true, "type": "number", "description": "Management interface", "format": "flag"}, "ethernet-cfg": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"ethernet": {"type": "number", "description": "Ethernet (Ethernet interface number)", "format": "interface"}, "optional": true}}]}, "priority": {"description": "Device priority", "format": "number", "type": "number", "maximum": 255, "minimum": 1, "optional": true}, "enable": {"default": 0, "optional": true, "type": "number", "description": "Enable", "format": "flag"}, "ve-cfg": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "ve": {"description": "VE interface (VE interface number)", "minimum": 2, "type": "number", "maximum": 4094, "format": "number"}}}]}, "device": {"description": "Device ID", "format": "number", "type": "number", "maximum": 8, "minimum": 1, "optional": false}, "affinity-vrrp-a-vrid": {"description": "vrid-group", "format": "number", "type": "number", "maximum": 31, "minimum": 0, "optional": true}, "unicast-port": {"description": "Port used in unicast communication (Port number)", "format": "number", "type": "number", "maximum": 65535, "minimum": 1024, "optional": true}, "trunk-cfg": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "trunk": {"description": "Trunk interface (Trunk interface number)", "minimum": 1, "type": "number", "maximum": 16, "format": "number"}}}]}}}], "type": "array", "$ref": "/axapi/v3/vcs/device/{device}"}
    :param time_interval: {"description": "how long between heartbeats (in unit of second, default is 3)", "format": "number", "default": 3, "optional": true, "maximum": 60, "minimum": 1, "type": "number"}
    :param action: {"description": "'enable': enable VCS; 'disable': disable VCS; ", "format": "enum", "default": "disable", "type": "string", "enum": ["enable", "disable"], "optional": true}
    :param failure_retry_count: {"description": "VCS retry count after fails to join the chassis (0-255, default is 2  means retry forever)", "format": "number", "default": 2, "optional": true, "maximum": 255, "minimum": 0, "type": "number"}
    :param multicast_ip: {"not": "multicast-ipv6", "optional": true, "type": "string", "description": "Multicast (group) IP address (Multicast IP address)", "format": "ipv4-address"}
    :param config_seq: {"description": "Configuration sequence number", "format": "string", "minLength": 1, "optional": true, "maxLength": 128, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/vcs`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "vcs"
        self.a10_url="/axapi/v3/vcs"
        self.DeviceProxy = ""
        self.multicast_port = ""
        self.dead_interval = ""
        self.force_wait_interval = ""
        self.ssl_enable = ""
        self.debug = {}
        self.multicast_ipv6 = ""
        self.vmaster_take_over = {}
        self.floating_ip_cfg = []
        self.device_list = []
        self.A10WW_reload = {}
        self.time_interval = ""
        self.admin_session_connect = {}
        self.action = ""
        self.vMaster_maintenance = {}
        self.failure_retry_count = ""
        self.multicast_ip = ""
        self.config_seq = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


