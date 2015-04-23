from a10sdk.common.A10BaseClass import A10BaseClass


class StringEntries(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param string_glid: {"type": "number", "format": "number"}
    :param string_key: {"type": "string", "format": "string"}
    :param string_lid: {"type": "number", "format": "number"}
    :param string_value: {"type": "string", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "string-entries"
        self.DeviceProxy = ""
        self.string_glid = ""
        self.string_key = ""
        self.string_lid = ""
        self.string_value = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class DnsEntries(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param dns_glid: {"type": "number", "format": "number"}
    :param dns_match_type: {"enum": ["contains", "ends-with", "starts-with"], "type": "string", "format": "enum"}
    :param dns_match_string: {"type": "string", "format": "string"}
    :param dns_lid: {"type": "number", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "dns-entries"
        self.DeviceProxy = ""
        self.dns_glid = ""
        self.dns_match_type = ""
        self.dns_match_string = ""
        self.dns_lid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Ipv4Entries(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ipv4_lsn_lid: {"type": "number", "format": "number"}
    :param ipv4_addr: {"type": "string", "format": "string"}
    :param ipv4_lid: {"type": "number", "format": "number"}
    :param ipv4_lsn_radius_profile: {"type": "number", "format": "number"}
    :param ipv4_glid: {"type": "number", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ipv4-entries"
        self.DeviceProxy = ""
        self.ipv4_lsn_lid = ""
        self.ipv4_addr = ""
        self.ipv4_lid = ""
        self.ipv4_lsn_radius_profile = ""
        self.ipv4_glid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Ipv6Entries(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ipv6_lsn_lid: {"type": "number", "format": "number"}
    :param ipv6_lsn_radius_profile: {"type": "number", "format": "number"}
    :param ipv6_lid: {"type": "number", "format": "number"}
    :param ipv6_glid: {"type": "number", "format": "number"}
    :param ipv6addr: {"type": "string", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ipv6-entries"
        self.DeviceProxy = ""
        self.ipv6_lsn_lid = ""
        self.ipv6_lsn_radius_profile = ""
        self.ipv6_lid = ""
        self.ipv6_glid = ""
        self.ipv6addr = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class AcEntries(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ac_match_type: {"enum": ["contains", "ends-with", "starts-with", "equals"], "type": "string", "format": "enum"}
    :param ac_match_string: {"type": "string", "format": "string"}
    :param ac_match_value: {"type": "string", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ac-entries"
        self.DeviceProxy = ""
        self.ac_match_type = ""
        self.ac_match_string = ""
        self.ac_match_value = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param file_or_string: {"enum": ["file", "config"], "type": "string", "format": "enum"}
    :param string_entries: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"string-glid": {"type": "number", "format": "number"}, "string-key": {"type": "string", "format": "string"}, "optional": true, "string-lid": {"type": "number", "format": "number"}, "string-value": {"type": "string", "format": "string"}}}]}
    :param dns_entries: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"dns-glid": {"type": "number", "format": "number"}, "optional": true, "dns-match-type": {"enum": ["contains", "ends-with", "starts-with"], "type": "string", "format": "enum"}, "dns-match-string": {"type": "string", "format": "string"}, "dns-lid": {"type": "number", "format": "number"}}}]}
    :param ipv4_entries: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"ipv4-lsn-lid": {"type": "number", "format": "number"}, "ipv4-addr": {"type": "string", "format": "string"}, "ipv4-lid": {"type": "number", "format": "number"}, "ipv4-lsn-radius-profile": {"type": "number", "format": "number"}, "optional": true, "ipv4-glid": {"type": "number", "format": "number"}}}]}
    :param ipv6_entries: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"ipv6-lsn-lid": {"type": "number", "format": "number"}, "ipv6-lsn-radius-profile": {"type": "number", "format": "number"}, "ipv6-lid": {"type": "number", "format": "number"}, "ipv6-glid": {"type": "number", "format": "number"}, "ipv6addr": {"type": "string", "format": "string"}, "optional": true}}]}
    :param ac_entries: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"ac-match-type": {"enum": ["contains", "ends-with", "starts-with", "equals"], "type": "string", "format": "enum"}, "ac-match-string": {"type": "string", "format": "string"}, "ac-match-value": {"type": "string", "format": "string"}, "optional": true}}]}
    :param type: {"enum": ["ac", "dns", "ipv4", "ipv6", "string", "string-case-insensitive", "[ipv4]", "[ipv6]", "[dns]", "[dns, ipv4]", "[dns, ipv6]"], "type": "string", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.file_or_string = ""
        self.string_entries = []
        self.dns_entries = []
        self.ipv4_entries = []
        self.ipv6_entries = []
        self.ac_entries = []
        self.A10WW_type = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class ClassList(A10BaseClass):
    
    """Class Description::
    Operational Status for the object class-list.

    Class class-list supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param name: {"description": "Specify name of the class list", "format": "string-rlx", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/class-list/{name}/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "class-list"
        self.a10_url="/axapi/v3/class-list/{name}/oper"
        self.DeviceProxy = ""
        self.oper = {}
        self.name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


