from a10sdk.common.A10BaseClass import A10BaseClass


class Log(A10BaseClass):
    
    """Class Description::
    Router log options.

    Class log supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param log_buffer: {"default": 1, "optional": true, "type": "number", "description": "Logging goes to log-buffer", "format": "flag"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/router/log`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "log"
        self.a10_url="/axapi/v3/router/log"
        self.DeviceProxy = ""
        self.log_buffer = ""
        self.uuid = ""
        self.A10WW_file = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


