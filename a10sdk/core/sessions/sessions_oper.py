from a10sdk.common.A10BaseClass import A10BaseClass


class SessionList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param protocol: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param forward_source: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param age: {"type": "number", "format": "number"}
    :param app_type: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param forward_dest: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param flags: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param hash: {"type": "number", "format": "number"}
    :param reverse_source: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param reverse_dest: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "session-list"
        self.DeviceProxy = ""
        self.protocol = ""
        self.forward_source = ""
        self.age = ""
        self.app_type = ""
        self.forward_dest = ""
        self.flags = ""
        self.A10WW_hash = ""
        self.reverse_source = ""
        self.reverse_dest = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param dst_ipv4_addr: {"type": "string", "format": "ipv4-address"}
    :param src_ipv6_addr: {"type": "string", "format": "ipv6-address"}
    :param src_port: {"type": "number", "format": "number"}
    :param dst_ipv6_addr: {"type": "string", "format": "ipv6-address"}
    :param name_str: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param total_sessions: {"type": "number", "format": "number"}
    :param src_ipv4_addr: {"type": "string", "format": "ipv4-address"}
    :param filter_type: {"enum": ["ipv4", "ipv6", "nat44", "nat64", "persist-ipv6-srcp-ip", "persist-ipv6-dst-ip", "persist-ipv6-ssl-id", "persist-dst-ip", "persist-src-ip", "persist-uie", "persist-ssl-id", "radius", "rserver", "vserver", "sip", "sixrd", "filter", "ds-lite", "dns-id-switch", "lsn"], "type": "string", "format": "enum"}
    :param session_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"protocol": {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}, "forward-source": {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}, "age": {"type": "number", "format": "number"}, "app-type": {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}, "forward-dest": {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}, "flags": {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}, "hash": {"type": "number", "format": "number"}, "reverse-source": {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}, "optional": true, "reverse-dest": {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}}}]}
    :param dest_port: {"type": "number", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.dst_ipv4_addr = ""
        self.src_ipv6_addr = ""
        self.src_port = ""
        self.dst_ipv6_addr = ""
        self.name_str = ""
        self.total_sessions = ""
        self.src_ipv4_addr = ""
        self.filter_type = ""
        self.session_list = []
        self.dest_port = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Sessions(A10BaseClass):
    
    """Class Description::
    Operational Status for the object sessions.

    Class sessions supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/sessions/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "sessions"
        self.a10_url="/axapi/v3/sessions/oper"
        self.DeviceProxy = ""
        self.oper = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


