from a10sdk.common.A10BaseClass import A10BaseClass


class Sshd(A10BaseClass):
    
    """    :param load: {"default": 0, "optional": true, "type": "number", "description": "Load SSH key", "format": "flag"}
    :param use_mgmt_port: {"default": 0, "optional": true, "type": "number", "description": "Use management port as source port", "format": "flag"}
    :param regenerate: {"default": 0, "optional": true, "type": "number", "description": "Wipe and generate SSH key", "format": "flag"}
    :param generate: {"default": 0, "optional": true, "type": "number", "description": "Generate SSH key", "format": "flag"}
    :param file_url: {"optional": true, "type": "string", "description": "File URL", "format": "url"}
    :param wipe: {"default": 0, "optional": true, "type": "number", "description": "Wipe SSH key", "format": "flag"}
    :param restart: {"default": 0, "optional": true, "type": "number", "description": "Restart SSH service", "format": "flag"}
    :param size: {"optional": true, "enum": ["2048", "4096"], "type": "string", "description": "'2048': Key size 2048bit; '4096': Key size 4096bit; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    SSHD service operation.

    Class sshd supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/sshd`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "sshd"
        self.a10_url="/axapi/v3/sshd"
        self.DeviceProxy = ""
        self.load = ""
        self.use_mgmt_port = ""
        self.regenerate = ""
        self.generate = ""
        self.file_url = ""
        self.wipe = ""
        self.restart = ""
        self.size = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


