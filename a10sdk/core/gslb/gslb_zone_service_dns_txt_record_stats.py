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


class DnsTxtRecord(A10BaseClass):
    
    """Class Description::
    Statistics for the object dns-txt-record.

    Class dns-txt-record supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param record_name: {"description": "Specify the Object Name for TXT Data", "format": "string", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/zone/{name}/service/{service_port}+{service_name}/dns-txt-record/{record_name}/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "record_name"]

        self.b_key = "dns-txt-record"
        self.a10_url="/axapi/v3/gslb/zone/{name}/service/{service_port}+{service_name}/dns-txt-record/{record_name}/stats"
        self.DeviceProxy = ""
        self.record_name = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


