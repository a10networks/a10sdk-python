from a10sdk.common.A10BaseClass import A10BaseClass


class SlbDataCacheTimeout(A10BaseClass):
    
    """Class Description::
    Configure the SLB data cache time-out in seconds.

    Class slb-data-cache-timeout supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param slblimit: {"description": "Cache time-out in seconds, default as 60 seconds", "format": "number", "type": "number", "maximum": 120, "minimum": 5, "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/snmp-server/slb-data-cache-timeout`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "slb-data-cache-timeout"
        self.a10_url="/axapi/v3/snmp-server/slb-data-cache-timeout"
        self.DeviceProxy = ""
        self.uuid = ""
        self.slblimit = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


