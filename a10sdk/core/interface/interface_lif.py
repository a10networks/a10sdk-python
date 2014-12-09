from a10sdk.common.A10BaseClass import A10BaseClass


class AccessList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param acl_name: {"minLength": 1, "maxLength": 16, "type": "string", "description": "Apply an access list (Named Access List)", "format": "string"}
    :param acl_id: {"description": "ACL id", "format": "number", "maximum": 199, "minimum": 1, "type": "number", "$ref": "/axapi/v3/access-list/standard"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "access-list"
        self.DeviceProxy = ""
        self.acl_name = ""
        self.acl_id = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Lif(A10BaseClass):
    
    """Class Description::
    Logical interface.

    Class lif supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param mtu: {"platform-specific-range": 1, "platform-specific-default": 1, "description": "Interface mtu (Interface MTU, default 1500 (min MTU is 1280 for IPv6))", "format": "number", "optional": true, "type": "number"}
    :param ifnum: {"description": "Lif interface number", "format": "number", "type": "number", "maximum": 128, "minimum": 1, "optional": false}
    :param action: {"description": "'enable': Enable; 'disable': Disable; ", "format": "enum", "default": "enable", "type": "string", "enum": ["enable", "disable"], "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/interface/lif/{ifnum}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "ifnum"]

        self.b_key = "lif"
        self.a10_url="/axapi/v3/interface/lif/{ifnum}"
        self.DeviceProxy = ""
        self.isis = {}
        self.bfd = {}
        self.ip = {}
        self.mtu = ""
        self.access_list = {}
        self.ifnum = ""
        self.action = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


