from a10sdk.common.A10BaseClass import A10BaseClass


class CopyCert(A10BaseClass):
    
    """    :param rotation: {"description": "Specify rotation number of SCEP generated certificate file", "format": "number", "type": "number", "maximum": 4, "minimum": 1, "optional": true}
    :param src_cert: {"description": "Source certificate file", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param dest_cert: {"description": "Destination certificate file", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param overwrite: {"default": 0, "optional": true, "type": "number", "description": "Overwrite the destination file if already present", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Copy SSL certificate to another file.

    Class copy-cert supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/pki/copy-cert`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "copy-cert"
        self.a10_url="/axapi/v3/pki/copy-cert"
        self.DeviceProxy = ""
        self.rotation = ""
        self.src_cert = ""
        self.dest_cert = ""
        self.overwrite = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


