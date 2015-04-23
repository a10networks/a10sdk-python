from a10sdk.common.A10BaseClass import A10BaseClass


class Source(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param class_list: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Class-list to match for NAT64", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "source"
        self.DeviceProxy = ""
        self.class_list = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Inside(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "inside"
        self.DeviceProxy = ""
        self.source = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class MssClamp(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param mss_subtract: {"description": "Specify the value to subtract from the TCP MSS (default: 20)", "format": "number", "default": 20, "maximum": 1420, "minimum": 0, "type": "number"}
    :param mss_value: {"description": "The max value allowed for the TCP MSS (default: not configured)", "minimum": 0, "type": "number", "maximum": 1420, "format": "number"}
    :param mss_clamp_type: {"enum": ["fixed", "none", "subtract"], "type": "string", "description": "'fixed': Specify a fixed max value for the TCP MSS; 'none': No TCP MSS clamping; 'subtract': Specify the value to subtract from the TCP MSS (default: 20); ", "format": "enum"}
    :param min: {"description": "Specify the min value allowed for the TCP MSS (Specify the min value allowed for the TCP MSS (default: 476))", "format": "number", "default": 476, "maximum": 1420, "minimum": 0, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "mss-clamp"
        self.DeviceProxy = ""
        self.mss_subtract = ""
        self.mss_value = ""
        self.mss_clamp_type = ""
        self.A10WW_min = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class ResetOnError(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param outbound: {"enum": ["disable"], "type": "string", "description": "'disable': Disable send TCP reset on error; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "reset-on-error"
        self.DeviceProxy = ""
        self.outbound = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Tcp(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "tcp"
        self.DeviceProxy = ""
        self.mss_clamp = {}
        self.reset_on_error = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Icmp(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param send_on_user_quota_exceeded: {"default": "admin-filtered", "enum": ["host-unreachable", "admin-filtered", "disable"], "type": "string", "description": "'host-unreachable': Send ICMP destination host unreachable; 'admin-filtered': Send ICMP admin filtered (default); 'disable': Disable ICMP quota exceeded message; ", "format": "enum"}
    :param send_on_port_unavailable: {"default": "disable", "enum": ["host-unreachable", "admin-filtered", "disable"], "type": "string", "description": "'host-unreachable': Send ICMPv6 destination host unreachable; 'admin-filtered': Send ICMPv6 admin filtered; 'disable': Disable ICMPv6 port unavailable message (default); ", "format": "enum"}
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
    
    """    :param user_quota_prefix_length: {"description": "User Quota Prefix Length (Default: 128)", "format": "number", "default": 128, "optional": true, "maximum": 128, "minimum": 1, "type": "number"}
    :param all: {"default": 0, "optional": true, "type": "number", "description": "All packet sizes", "format": "flag"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param force_non_zero_ipv4_id: {"default": 0, "optional": true, "type": "number", "description": "Enable non-zero Identification field in IPv4 header when no IPv6 Fragment for packet size more than 88 & less than 1280 bytes", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Configure NAT64 parameters.

    Class global supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/nat64/global`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "global"
        self.a10_url="/axapi/v3/cgnv6/nat64/global"
        self.DeviceProxy = ""
        self.user_quota_prefix_length = ""
        self.A10WW_all = ""
        self.uuid = ""
        self.inside = {}
        self.tcp = {}
        self.force_non_zero_ipv4_id = ""
        self.icmp = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


