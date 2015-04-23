from a10sdk.common.A10BaseClass import A10BaseClass


class DnsSrvRecord(A10BaseClass):
    
    """Class Description::
    Specify DNS SRV Record.

    Class dns-srv-record supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param srv_name: {"description": "Specify Domain Name", "format": "string", "minLength": 1, "optional": false, "maxLength": 127, "type": "string"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param weight: {"description": "Specify Weight, default is 10", "format": "number", "default": 10, "optional": true, "maximum": 100, "minimum": 1, "type": "number"}
    :param priority: {"description": "Specify Priority", "format": "number", "type": "number", "maximum": 65535, "minimum": 0, "optional": true}
    :param ttl: {"description": "Specify TTL", "format": "number", "type": "number", "maximum": 2147483647, "minimum": 0, "optional": true}
    :param port: {"description": "Specify Port (Port Number)", "format": "number", "type": "number", "maximum": 65534, "minimum": 0, "optional": false}
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
        self.srv_name = ""
        self.uuid = ""
        self.weight = ""
        self.priority = ""
        self.ttl = ""
        self.port = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


