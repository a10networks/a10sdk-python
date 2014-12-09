from a10sdk.common.A10BaseClass import A10BaseClass


class ServiceTimeout(A10BaseClass):
    
    """Class Description::
    Specify any custom service timeout.

    Class service-timeout supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param timeout_val: {"description": "Timeout in seconds (Interval of 60 seconds)", "format": "number", "type": "number", "maximum": 15000, "minimum": 2, "optional": true}
    :param service_type: {"optional": false, "enum": ["tcp", "udp"], "type": "string", "description": "'tcp': TCP Protocol; 'udp': UDP Protocol; ", "format": "enum"}
    :param timeout_type: {"optional": true, "enum": ["age", "fast"], "type": "string", "description": "'age': Expiration time; 'fast': Use Fast aging; ", "format": "enum"}
    :param port: {"description": "Port Number", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": false}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ip/nat/translation/service-timeout/{service_type}+{port}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "service_type","port"]

        self.b_key = "service-timeout"
        self.a10_url="/axapi/v3/ip/nat/translation/service-timeout/{service_type}+{port}"
        self.DeviceProxy = ""
        self.timeout_val = ""
        self.service_type = ""
        self.timeout_type = ""
        self.port = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


