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


class DnsARecordSrv(A10BaseClass):
    
    """Class Description::
    Statistics for the object dns-a-record-srv.

    Class dns-a-record-srv supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param svrname: {"description": "Specify name", "format": "string", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/zone/{name}/service/{service_port}+{service_name}/dns-a-record/dns-a-record-srv/{svrname}/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "svrname"]

        self.b_key = "dns-a-record-srv"
        self.a10_url="/axapi/v3/gslb/zone/{name}/service/{service_port}+{service_name}/dns-a-record/dns-a-record-srv/{svrname}/stats"
        self.DeviceProxy = ""
        self.stats = {}
        self.svrname = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


