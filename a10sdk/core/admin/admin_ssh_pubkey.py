from a10sdk.common.A10BaseClass import A10BaseClass


class SshPubkey(A10BaseClass):
    
    """Class Description::
    Config openssh authorized public keys management.

    Class ssh-pubkey supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param use_mgmt_port: {"default": 0, "optional": true, "type": "number", "description": "Use management port as source port", "format": "flag"}
    :param list: {"default": 0, "optional": true, "type": "number", "description": "List all authorized public keys", "format": "flag"}
    :param import: {"default": 0, "optional": true, "type": "number", "description": "Import an authorized public key", "format": "flag"}
    :param file_url: {"optional": true, "type": "string", "description": "File URL", "format": "url"}
    :param delete: {"description": "Delete an authorized public key (SSH key index)", "format": "number", "type": "number", "maximum": 1000000, "minimum": 1, "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/admin/{user}/ssh-pubkey`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "ssh-pubkey"
        self.a10_url="/axapi/v3/admin/{user}/ssh-pubkey"
        self.DeviceProxy = ""
        self.uuid = ""
        self.use_mgmt_port = ""
        self.A10WW_list = ""
        self.A10WW_import = ""
        self.file_url = ""
        self.delete = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


