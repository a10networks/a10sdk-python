from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param hits: {"description": "Number of times the record has been used", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.hits = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class DnsSrvRecord(A10BaseClass):
    
    """Class Description::
    Statistics for the object dns-srv-record.

    Class dns-srv-record supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param srv_name: {"description": "Specify Domain Name", "format": "string", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 127, "type": "string"}
    :param port: {"description": "Specify Port (Port Number)", "format": "number", "optional": false, "oid": "1002", "maximum": 65534, "minimum": 0, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/zone/{name}/service/{service_port}+{service_name}/dns-srv-record/{srv_name}+{port}/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "srv_name","port"]

        self.b_key = "dns-srv-record"
        self.a10_url="/axapi/v3/gslb/zone/{name}/service/{service_port}+{service_name}/dns-srv-record/{srv_name}+{port}/stats"
        self.DeviceProxy = ""
        self.srv_name = ""
        self.stats = {}
        self.port = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


