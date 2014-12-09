from a10sdk.common.A10BaseClass import A10BaseClass


class Cf(A10BaseClass):
    
    """    :param use_mgmt_port: {"description": "Use management port as source port", "format": "flag", "default": 0, "optional": true, "not-list": ["local", "file-url", "image-file"], "type": "number"}
    :param image: {"optional": true, "enum": ["pri"], "type": "string", "description": "'pri': Primary image; ", "format": "enum"}
    :param Device: {"optional": true, "minimum": 1, "type": "number", "maximum": 8, "format": "number"}
    :param local: {"description": "Use image from local VCS image repository (Specify an image name, format: aximage_XX_XX_XX_XX.tar.gz)", "format": "string", "minLength": 1, "not-list": ["use-mgmt-port", "file-url", "image-file"], "optional": true, "maxLength": 128, "type": "string"}
    :param staggered_upgrade_mode: {"default": 0, "optional": true, "type": "number", "description": "in staggered upgrade mode", "format": "flag"}
    :param file_url: {"not-list": ["local", "use-mgmt-port", "image-file"], "type": "string", "description": "File URL", "optional": true, "format": "url"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Compact flash.

    Class cf supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/upgrade/cf`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "cf"
        self.a10_url="/axapi/v3/upgrade/cf"
        self.DeviceProxy = ""
        self.use_mgmt_port = ""
        self.image = ""
        self.Device = ""
        self.local = ""
        self.staggered_upgrade_mode = ""
        self.file_url = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


