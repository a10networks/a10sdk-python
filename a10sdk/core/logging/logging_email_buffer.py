from a10sdk.common.A10BaseClass import A10BaseClass


class Buffer(A10BaseClass):
    
    """Class Description::
    Logging via email buffering settings.

    Class buffer supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param number: {"description": "Number of log messages that can be buffered (Number of log messages that can be buffered, default 50)", "format": "number", "default": 50, "optional": true, "maximum": 256, "minimum": 16, "type": "number"}
    :param time: {"description": "Number of minutes a log message can stay in buffer (Number of minutes a log message can stay in buffer, default 10)", "format": "number", "default": 10, "optional": true, "maximum": 1440, "minimum": 10, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/logging/email/buffer`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "buffer"
        self.a10_url="/axapi/v3/logging/email/buffer"
        self.DeviceProxy = ""
        self.uuid = ""
        self.number = ""
        self.time = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


