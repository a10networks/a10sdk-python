from a10sdk.common.A10BaseClass import A10BaseClass


class CopyKey(A10BaseClass):
    
    """    :param rotation: {"description": "Specify rotation number of SCEP generated key file", "format": "number", "type": "number", "maximum": 4, "minimum": 1, "optional": true}
    :param overwrite: {"default": 0, "optional": true, "type": "number", "description": "Overwrite the destination file if already present", "format": "flag"}
    :param dest_key: {"description": "Destination key file", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param src_key: {"description": "Source key file", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Copy SSL key to another file.

    Class copy-key supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/pki/copy-key`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "copy-key"
        self.a10_url="/axapi/v3/pki/copy-key"
        self.DeviceProxy = ""
        self.rotation = ""
        self.overwrite = ""
        self.dest_key = ""
        self.src_key = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


