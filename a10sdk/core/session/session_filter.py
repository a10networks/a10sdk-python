from a10sdk.common.A10BaseClass import A10BaseClass


class FilterCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param dport1: {"description": "Forward Destination Port", "format": "number", "maximum": 65535, "minimum": 1, "not": "dport2", "type": "number"}
    :param source_addr: {"type": "string", "description": "Forward Source IP (Source IP address)", "format": "ipv4-address"}
    :param dport2: {"description": "Forward Destination Port (Dest Port)", "format": "number", "maximum": 65535, "minimum": 1, "not": "dport1", "type": "number"}
    :param dest_mask: {"type": "string", "description": "Forward Destination IP Subnet (Destination Netmask)", "format": "ipv4-netmask"}
    :param session_type: {"enum": ["ipv6", "sip"], "type": "string", "description": "'ipv6': Display ipv6 sessions only; 'sip': SIP sessions; ", "format": "enum"}
    :param source_port: {"description": "Forward Source Port", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}
    :param dest_addr: {"type": "string", "description": "Forward Destination IP (Destination IP address)", "format": "ipv4-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "filter-cfg"
        self.DeviceProxy = ""
        self.dport1 = ""
        self.source_addr = ""
        self.dport2 = ""
        self.dest_mask = ""
        self.session_type = ""
        self.source_port = ""
        self.dest_addr = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class SessionFilter(A10BaseClass):
    
    """Class Description::
    Create a convenience Filter to display/clear sessions.

    Class session-filter supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param set: {"default": 0, "optional": true, "type": "number", "description": "Set filter criteria", "format": "flag"}
    :param name: {"description": "Session filter name", "format": "string", "minLength": 1, "optional": false, "maxLength": 31, "type": "string"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/session-filter/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "session-filter"
        self.a10_url="/axapi/v3/session-filter/{name}"
        self.DeviceProxy = ""
        self.filter_cfg = {}
        self.A10WW_set = ""
        self.name = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


