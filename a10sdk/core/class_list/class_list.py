from a10sdk.common.A10BaseClass import A10BaseClass


class Ipv4List(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param lid: {"description": "Use Limit ID defined in template (Specify LID index)", "format": "number", "maximum": 31, "minimum": 1, "not": "glid", "type": "number"}
    :param glid: {"description": "Use global Limit ID (Specify global LID index)", "format": "number", "maximum": 1023, "minimum": 1, "not": "lid", "type": "number"}
    :param age: {"description": "Specify age in minutes", "minimum": 1, "type": "number", "maximum": 2000, "format": "number"}
    :param ipv4addr: {"type": "string", "description": "Specify IP address", "format": "ipv4-cidr"}
    :param lsn_lid: {"description": "LSN Limit ID (LID index)", "minimum": 1, "type": "number", "maximum": 1023, "format": "number"}
    :param lsn_radius_profile: {"description": "LSN RADIUS Profile Index", "minimum": 1, "type": "number", "maximum": 16, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ipv4-list"
        self.DeviceProxy = ""
        self.lid = ""
        self.glid = ""
        self.age = ""
        self.ipv4addr = ""
        self.lsn_lid = ""
        self.lsn_radius_profile = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class StrList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param str: {"minLength": 1, "maxLength": 128, "type": "string", "description": "Specify key string", "format": "string-rlx"}
    :param value_str: {"minLength": 1, "maxLength": 128, "type": "string", "description": "Specify value string", "format": "string"}
    :param str_glid_dummy: {"default": 0, "not": "str-lid-dummy", "type": "number", "description": "Use global Limit ID", "format": "flag"}
    :param str_glid: {"description": "Global LID index", "minimum": 1, "type": "number", "maximum": 1023, "format": "number"}
    :param str_lid_dummy: {"default": 0, "not": "str-glid-dummy", "type": "number", "description": "Use Limit ID defined in template", "format": "flag"}
    :param str_lid: {"description": "LID index", "minimum": 1, "type": "number", "maximum": 31, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "str-list"
        self.DeviceProxy = ""
        self.A10WW_str = ""
        self.value_str = ""
        self.str_glid_dummy = ""
        self.str_glid = ""
        self.str_lid_dummy = ""
        self.str_lid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class AcList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ac_match_type: {"enum": ["contains", "ends-with", "equals", "starts-with"], "type": "string", "description": "'contains': String contains another string; 'ends-with': String ends with another string; 'equals': String equals another string; 'starts-with': String starts with another string; ", "format": "enum"}
    :param ac_key_string: {"minLength": 1, "maxLength": 255, "type": "string", "description": "Specify key string", "format": "string-rlx"}
    :param ac_value: {"minLength": 1, "maxLength": 639, "type": "string", "description": "Specify value string", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ac-list"
        self.DeviceProxy = ""
        self.ac_match_type = ""
        self.ac_key_string = ""
        self.ac_value = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Ipv6List(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param v6_lsn_lid: {"description": "LSN Limit ID (LID index)", "minimum": 1, "type": "number", "maximum": 1023, "format": "number"}
    :param v6_glid: {"description": "Use global Limit ID (Specify global LID index)", "format": "number", "maximum": 1023, "minimum": 1, "not": "v6-lid", "type": "number"}
    :param ipv6_addr: {"type": "string", "description": "Specify IPv6 host or subnet", "format": "ipv6-address-plen"}
    :param v6_age: {"description": "Specify age in minutes", "minimum": 1, "type": "number", "maximum": 2000, "format": "number"}
    :param v6_lid: {"description": "Use Limit ID defined in template (Specify LID index)", "format": "number", "maximum": 31, "minimum": 1, "not": "v6-glid", "type": "number"}
    :param v6_lsn_radius_profile: {"description": "LSN RADIUS Profile Index", "minimum": 1, "type": "number", "maximum": 16, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ipv6-list"
        self.DeviceProxy = ""
        self.v6_lsn_lid = ""
        self.v6_glid = ""
        self.ipv6_addr = ""
        self.v6_age = ""
        self.v6_lid = ""
        self.v6_lsn_radius_profile = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Dns(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param dns_glid: {"description": "Use global Limit ID (Specify global LID index)", "format": "number", "maximum": 1023, "minimum": 1, "not": "dns-lid", "type": "number"}
    :param dns_match_type: {"enum": ["contains", "ends-with", "starts-with"], "type": "string", "description": "'contains': Domain contains another string; 'ends-with': Domain ends with another string; 'starts-with': Domain starts-with another string; ", "format": "enum"}
    :param dns_match_string: {"minLength": 1, "maxLength": 128, "type": "string", "description": "Domain name", "format": "string"}
    :param dns_lid: {"description": "Use Limit ID defined in template (Specify LID index)", "format": "number", "maximum": 31, "minimum": 1, "not": "dns-glid", "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "dns"
        self.DeviceProxy = ""
        self.dns_glid = ""
        self.dns_match_type = ""
        self.dns_match_string = ""
        self.dns_lid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class ClassList(A10BaseClass):
    
    """Class Description::
    Configure classification list.

    Class class-list supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param file: {"description": "Create/Edit a class-list stored as a file", "format": "flag", "default": 0, "type": "number", "modify-not-allowed": 1, "optional": true}
    :param name: {"description": "Specify name of the class list", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param ipv4_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"lid": {"description": "Use Limit ID defined in template (Specify LID index)", "format": "number", "maximum": 31, "minimum": 1, "not": "glid", "type": "number"}, "glid": {"description": "Use global Limit ID (Specify global LID index)", "format": "number", "maximum": 1023, "minimum": 1, "not": "lid", "type": "number"}, "age": {"description": "Specify age in minutes", "minimum": 1, "type": "number", "maximum": 2000, "format": "number"}, "ipv4addr": {"type": "string", "description": "Specify IP address", "format": "ipv4-cidr"}, "lsn-lid": {"description": "LSN Limit ID (LID index)", "minimum": 1, "type": "number", "maximum": 1023, "format": "number"}, "lsn-radius-profile": {"description": "LSN RADIUS Profile Index", "minimum": 1, "type": "number", "maximum": 16, "format": "number"}, "optional": true}}]}
    :param str_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"str": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Specify key string", "format": "string-rlx"}, "value-str": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Specify value string", "format": "string"}, "str-glid-dummy": {"default": 0, "not": "str-lid-dummy", "type": "number", "description": "Use global Limit ID", "format": "flag"}, "str-glid": {"description": "Global LID index", "minimum": 1, "type": "number", "maximum": 1023, "format": "number"}, "str-lid-dummy": {"default": 0, "not": "str-glid-dummy", "type": "number", "description": "Use Limit ID defined in template", "format": "flag"}, "str-lid": {"description": "LID index", "minimum": 1, "type": "number", "maximum": 31, "format": "number"}, "optional": true}}]}
    :param ac_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"ac-match-type": {"enum": ["contains", "ends-with", "equals", "starts-with"], "type": "string", "description": "'contains': String contains another string; 'ends-with': String ends with another string; 'equals': String equals another string; 'starts-with': String starts with another string; ", "format": "enum"}, "ac-key-string": {"minLength": 1, "maxLength": 255, "type": "string", "description": "Specify key string", "format": "string-rlx"}, "ac-value": {"minLength": 1, "maxLength": 639, "type": "string", "description": "Specify value string", "format": "string-rlx"}, "optional": true}}]}
    :param ipv6_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"v6-lsn-lid": {"description": "LSN Limit ID (LID index)", "minimum": 1, "type": "number", "maximum": 1023, "format": "number"}, "v6-glid": {"description": "Use global Limit ID (Specify global LID index)", "format": "number", "maximum": 1023, "minimum": 1, "not": "v6-lid", "type": "number"}, "ipv6-addr": {"type": "string", "description": "Specify IPv6 host or subnet", "format": "ipv6-address-plen"}, "v6-age": {"description": "Specify age in minutes", "minimum": 1, "type": "number", "maximum": 2000, "format": "number"}, "v6-lid": {"description": "Use Limit ID defined in template (Specify LID index)", "format": "number", "maximum": 31, "minimum": 1, "not": "v6-glid", "type": "number"}, "optional": true, "v6-lsn-radius-profile": {"description": "LSN RADIUS Profile Index", "minimum": 1, "type": "number", "maximum": 16, "format": "number"}}}]}
    :param dns: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"dns-glid": {"description": "Use global Limit ID (Specify global LID index)", "format": "number", "maximum": 1023, "minimum": 1, "not": "dns-lid", "type": "number"}, "optional": true, "dns-match-type": {"enum": ["contains", "ends-with", "starts-with"], "type": "string", "description": "'contains': Domain contains another string; 'ends-with': Domain ends with another string; 'starts-with': Domain starts-with another string; ", "format": "enum"}, "dns-match-string": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Domain name", "format": "string"}, "dns-lid": {"description": "Use Limit ID defined in template (Specify LID index)", "format": "number", "maximum": 31, "minimum": 1, "not": "dns-glid", "type": "number"}}}]}
    :param type: {"description": "'ac': Make class-list type Aho-Corasick; 'dns': Make class-list type DNS; 'ipv4': Make class-list type IPv4; 'ipv6': Make class-list type IPv6; 'string': Make class-list type String; ", "format": "enum", "type": "string", "enum": ["ac", "dns", "ipv4", "ipv6", "string"], "modify-not-allowed": 1, "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/class-list/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "class-list"
        self.a10_url="/axapi/v3/class-list/{name}"
        self.DeviceProxy = ""
        self.A10WW_file = ""
        self.name = ""
        self.ipv4_list = []
        self.str_list = []
        self.ac_list = []
        self.ipv6_list = []
        self.dns = []
        self.A10WW_type = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


