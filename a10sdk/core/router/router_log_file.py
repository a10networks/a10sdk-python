from a10sdk.common.A10BaseClass import A10BaseClass


class File(A10BaseClass):
    
    """Class Description::
    Logging to file.

    Class file supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param rotate: {"description": "Log file rotation (Number of backup files)", "format": "number", "type": "number", "maximum": 100, "minimum": 0, "optional": true}
    :param name: {"description": "Logging filename (File name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 32, "type": "string"}
    :param per_protocol: {"default": 0, "optional": true, "type": "number", "description": "Per protocol", "format": "flag"}
    :param size: {"description": "Log file maximum size (File size in MBytes)", "format": "number", "type": "number", "maximum": 1000000, "minimum": 0, "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/router/log/file`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "file"
        self.a10_url="/axapi/v3/router/log/file"
        self.DeviceProxy = ""
        self.uuid = ""
        self.rotate = ""
        self.name = ""
        self.per_protocol = ""
        self.size = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


