from a10sdk.common.A10BaseClass import A10BaseClass


class Key(A10BaseClass):
    
    """Class Description::
    Configure a key.

    Class key supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param key_number: {"description": "Key identifier number", "format": "number", "type": "number", "maximum": 255, "minimum": 1, "optional": false}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param key_string: {"description": "Set key string (The key)", "format": "string", "minLength": 1, "optional": true, "maxLength": 128, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/key/{key_chain_flag}+{key_chain_name}/key/{key_number}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "key_number"]

        self.b_key = "key"
        self.a10_url="/axapi/v3/key/{key_chain_flag}+{key_chain_name}/key/{key_number}"
        self.DeviceProxy = ""
        self.key_number = ""
        self.uuid = ""
        self.key_string = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


