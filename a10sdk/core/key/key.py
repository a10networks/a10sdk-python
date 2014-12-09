from a10sdk.common.A10BaseClass import A10BaseClass


class KeyChainCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param key_chain_flag: {"default": 0, "type": "number", "description": "Key-chain management", "format": "flag"}
    :param key_chain_name: {"minLength": 1, "maxLength": 128, "type": "string", "description": "Key-chain name", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "key-chain-cfg"
        self.DeviceProxy = ""
        self.key_chain_flag = ""
        self.key_chain_name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Key(A10BaseClass):
    
    """Class Description::
    Authentication key management.

    Class key supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param key_list: {"minItems": 1, "items": {"type": "key"}, "uniqueItems": true, "array": [{"required": ["key-number"], "properties": {"key-number": {"description": "Key identifier number", "format": "number", "type": "number", "maximum": 255, "minimum": 1, "optional": false}, "key-string": {"description": "Set key string (The key)", "format": "string", "minLength": 1, "optional": true, "maxLength": 128, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/key/{key-chain-flag}+{key-chain-name}/key/{key-number}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/key/{key_chain_flag}+{key_chain_name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "key_chain_flag","key_chain_name"]

        self.b_key = "key"
        self.a10_url="/axapi/v3/key/{key_chain_flag}+{key_chain_name}"
        self.DeviceProxy = ""
        self.key_chain_cfg = {}
        self.key_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


