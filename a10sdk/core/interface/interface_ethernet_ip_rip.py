from a10sdk.common.A10BaseClass import A10BaseClass


class ReceiveCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param receive: {"default": 0, "type": "number", "description": "Advertisement reception", "format": "flag"}
    :param version: {"enum": ["1", "2", "1-2"], "type": "string", "description": "'1': RIP version 1; '2': RIP version 2; '1-2': RIP version 1 & 2; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "receive-cfg"
        self.DeviceProxy = ""
        self.receive = ""
        self.version = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class SplitHorizonCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param state: {"default": "poisoned", "enum": ["poisoned", "disable", "enable"], "type": "string", "description": "'poisoned': Perform split horizon with poisoned reverse; 'disable': Disable split horizon; 'enable': Perform split horizon without poisoned reverse; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "split-horizon-cfg"
        self.DeviceProxy = ""
        self.state = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class KeyChain(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param key_chain: {"type": "string", "description": "Authentication key-chain (Name of key-chain)", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "key-chain"
        self.DeviceProxy = ""
        self.key_chain = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Mode(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param mode: {"default": "text", "enum": ["md5", "text"], "type": "string", "description": "'md5': Keyed message digest; 'text': Clear text authentication; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "mode"
        self.DeviceProxy = ""
        self.mode = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Str(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param string: {"minLength": 1, "maxLength": 16, "type": "string", "description": "The RIP authentication string", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "str"
        self.DeviceProxy = ""
        self.string = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Authentication(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "authentication"
        self.DeviceProxy = ""
        self.key_chain = {}
        self.mode = {}
        self.A10WW_str = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class SendCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param version: {"enum": ["1", "2", "1-compatible", "1-2"], "type": "string", "description": "'1': RIP version 1; '2': RIP version 2; '1-compatible': RIPv1-compatible; '1-2': RIP version 1 & 2; ", "format": "enum"}
    :param send: {"default": 0, "type": "number", "description": "Advertisement transmission", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "send-cfg"
        self.DeviceProxy = ""
        self.version = ""
        self.send = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Rip(A10BaseClass):
    
    """Class Description::
    RIP.

    Class rip supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param receive_packet: {"default": 1, "optional": true, "type": "number", "description": "Enable receiving packet through the specified interface", "format": "flag"}
    :param send_packet: {"default": 1, "optional": true, "type": "number", "description": "Enable sending packets through the specified interface", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/interface/ethernet/{ifnum}/ip/rip`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "rip"
        self.a10_url="/axapi/v3/interface/ethernet/{ifnum}/ip/rip"
        self.DeviceProxy = ""
        self.receive_cfg = {}
        self.uuid = ""
        self.receive_packet = ""
        self.split_horizon_cfg = {}
        self.authentication = {}
        self.send_cfg = {}
        self.send_packet = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


