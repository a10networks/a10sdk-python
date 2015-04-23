from a10sdk.common.A10BaseClass import A10BaseClass


class VeCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ve_end: {"type": "number", "description": "VE port", "format": "number"}
    :param ve_start: {"type": "number", "description": "VE port (VE Interface number)", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ve-cfg"
        self.DeviceProxy = ""
        self.ve_end = ""
        self.ve_start = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class EthCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ethernet_start: {"type": "number", "description": "Ethernet port (Ethernet Interface number)", "format": "interface"}
    :param ethernet_end: {"type": "number", "description": "Ethernet port", "format": "interface"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "eth-cfg"
        self.DeviceProxy = ""
        self.ethernet_start = ""
        self.ethernet_end = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class AclV6(A10BaseClass):
    
    """Class Description::
    IPv6 ACL for Ping service.

    Class acl-v6 supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param acl_name: {"description": "ACL name", "format": "string", "minLength": 1, "optional": false, "maxLength": 16, "type": "string"}
    :param ve_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"ve-end": {"type": "number", "description": "VE port", "format": "number"}, "ve-start": {"type": "number", "description": "VE port (VE Interface number)", "format": "number"}, "optional": true}}]}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param eth_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"ethernet-start": {"type": "number", "description": "Ethernet port (Ethernet Interface number)", "format": "interface"}, "ethernet-end": {"type": "number", "description": "Ethernet port", "format": "interface"}, "optional": true}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/enable-management/service/ping/acl-v6/{acl_name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "acl_name"]

        self.b_key = "acl-v6"
        self.a10_url="/axapi/v3/enable-management/service/ping/acl-v6/{acl_name}"
        self.DeviceProxy = ""
        self.acl_name = ""
        self.ve_cfg = []
        self.uuid = ""
        self.eth_cfg = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


