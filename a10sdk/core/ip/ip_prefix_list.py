from a10sdk.common.A10BaseClass import A10BaseClass


class Rules(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param le: {"description": "Maximum prefix length to be matched", "minimum": 0, "type": "number", "maximum": 32, "format": "number"}
    :param description: {"minLength": 1, "maxLength": 80, "type": "string", "description": "Prefix-list specific description (Up to 80 characters describing this prefix-list)", "format": "string"}
    :param seq: {"description": "Sequence number of an entry", "minimum": 1, "type": "number", "maximum": 4294967295, "format": "number"}
    :param ipaddr: {"type": "string", "description": "IP prefix, e.g., 35.0.0.0/8", "format": "ipv4-cidr"}
    :param ge: {"description": "Minimum prefix length to be matched", "minimum": 0, "type": "number", "maximum": 32, "format": "number"}
    :param action: {"enum": ["deny", "permit"], "type": "string", "description": "'deny': Specify packets to reject; 'permit': Specify packets to forward; ", "format": "enum"}
    :param any: {"default": 0, "type": "number", "description": "Any prefix match. Same as \"0.0.0.0/0 le 32\"", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "rules"
        self.DeviceProxy = ""
        self.le = ""
        self.description = ""
        self.seq = ""
        self.ipaddr = ""
        self.ge = ""
        self.action = ""
        self.A10WW_any = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class PrefixList(A10BaseClass):
    
    """Class Description::
    Configure Prefix-list.

    Class prefix-list supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param rules: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"le": {"description": "Maximum prefix length to be matched", "minimum": 0, "type": "number", "maximum": 32, "format": "number"}, "description": {"minLength": 1, "maxLength": 80, "type": "string", "description": "Prefix-list specific description (Up to 80 characters describing this prefix-list)", "format": "string"}, "seq": {"description": "Sequence number of an entry", "minimum": 1, "type": "number", "maximum": 4294967295, "format": "number"}, "ipaddr": {"type": "string", "description": "IP prefix, e.g., 35.0.0.0/8", "format": "ipv4-cidr"}, "ge": {"description": "Minimum prefix length to be matched", "minimum": 0, "type": "number", "maximum": 32, "format": "number"}, "action": {"enum": ["deny", "permit"], "type": "string", "description": "'deny': Specify packets to reject; 'permit': Specify packets to forward; ", "format": "enum"}, "optional": true, "any": {"default": 0, "type": "number", "description": "Any prefix match. Same as \"0.0.0.0/0 le 32\"", "format": "flag"}}}]}
    :param name: {"description": "Name of a prefix list", "format": "string", "minLength": 1, "optional": false, "maxLength": 128, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ip/prefix-list/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "prefix-list"
        self.a10_url="/axapi/v3/ip/prefix-list/{name}"
        self.DeviceProxy = ""
        self.rules = []
        self.name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


