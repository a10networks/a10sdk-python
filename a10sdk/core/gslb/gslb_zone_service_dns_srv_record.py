from a10sdk.common.A10BaseClass import A10BaseClass


class DnsSrvRecord(A10BaseClass):
    
    """Class Description::
    Specify DNS SRV Record.

    Class dns-srv-record supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param priority: {"description": "Specify Priority", "format": "number", "type": "number", "maximum": 65535, "minimum": 0, "optional": true}
    :param srv_name: {"description": "Specify Domain Name", "format": "string", "minLength": 1, "optional": false, "maxLength": 127, "type": "string"}
    :param port: {"description": "Specify Port (Port Number)", "format": "number", "type": "number", "maximum": 65534, "minimum": 0, "optional": false}
    :param weight: {"description": "Specify Weight, default is 10", "format": "number", "default": 10, "optional": true, "maximum": 100, "minimum": 1, "type": "number"}
    :param ttl: {"optional": true, "type": "number", "description": "Specify TTL", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/zone/{name}/service/{service_port}+{service_name}/dns-srv-record/{srv_name}+{port}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "srv_name","port"]

        self.b_key = "dns-srv-record"
        self.a10_url="/axapi/v3/gslb/zone/{name}/service/{service_port}+{service_name}/dns-srv-record/{srv_name}+{port}"
        self.DeviceProxy = ""
        self.priority = ""
        self.srv_name = ""
        self.port = ""
        self.weight = ""
        self.ttl = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


