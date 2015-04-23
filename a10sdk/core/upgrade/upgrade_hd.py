from a10sdk.common.A10BaseClass import A10BaseClass


class Hd(A10BaseClass):
    
    """    :param reboot_after_upgrade: {"default": 0, "optional": true, "type": "number", "description": "reboot system after upgrade is done", "format": "flag"}
    :param use_mgmt_port: {"description": "Use management port as source port", "format": "flag", "default": 0, "optional": true, "not": "local", "type": "number"}
    :param image: {"optional": true, "enum": ["pri", "sec"], "type": "string", "description": "'pri': Primary image; 'sec': Secondary image; ", "format": "enum"}
    :param Device: {"platform-specific-range": 1, "platform-specific-default": 1, "type": "number", "optional": true, "format": "number"}
    :param local: {"description": "Use image from local VCS image repository (Specify an image name, format: aximage_XX_XX_XX_XX.tar.gz)", "format": "string", "minLength": 1, "not-list": ["use-mgmt-port", "file-url", "image-file"], "optional": true, "maxLength": 128, "type": "string"}
    :param staggered_upgrade_mode: {"default": 0, "optional": true, "type": "number", "description": "in staggered upgrade mode", "format": "flag"}
    :param file_url: {"not-list": ["local", "image-file"], "type": "string", "description": "File URL", "optional": true, "format": "url"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Hard Disk.

    Class hd supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/upgrade/hd`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "hd"
        self.a10_url="/axapi/v3/upgrade/hd"
        self.DeviceProxy = ""
        self.reboot_after_upgrade = ""
        self.use_mgmt_port = ""
        self.image = ""
        self.Device = ""
        self.local = ""
        self.staggered_upgrade_mode = ""
        self.file_url = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


