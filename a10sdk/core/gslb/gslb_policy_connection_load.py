from a10sdk.common.A10BaseClass import A10BaseClass


class ConnectionLoad(A10BaseClass):
    
    """Class Description::
    Select Service-IP with the lowest connection-load.

    Class connection-load supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param connection_load_enable: {"default": 0, "optional": true, "type": "number", "description": "Enable connection-load", "format": "flag"}
    :param connection_load_interval: {"description": "Interval between two samples, Unit: second (Interval value,default is 5)", "format": "number", "default": 5, "optional": true, "maximum": 60, "minimum": 1, "type": "number"}
    :param limit: {"default": 0, "optional": true, "type": "number", "description": "Limit of maxinum connection load, default is unlimited", "format": "flag"}
    :param connection_load_samples: {"description": "Specify samples for connection-load (Number of samples used to calculate the connection load, default is 5)", "format": "number", "default": 5, "optional": true, "maximum": 8, "minimum": 1, "type": "number"}
    :param connection_load_limit: {"description": "The value of the connection-load limit, default is unlimited", "format": "number", "type": "number", "maximum": 999999999, "minimum": 1, "optional": true}
    :param connection_load_fail_break: {"default": 0, "optional": true, "type": "number", "description": "Break when exceed limit", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/policy/{name}/connection-load`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "connection-load"
        self.a10_url="/axapi/v3/gslb/policy/{name}/connection-load"
        self.DeviceProxy = ""
        self.connection_load_enable = ""
        self.connection_load_interval = ""
        self.limit = ""
        self.connection_load_samples = ""
        self.connection_load_limit = ""
        self.connection_load_fail_break = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


