from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param dev_vip_hits: {"description": "Number of times the service-ip was selected", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.dev_vip_hits = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class VipServerV4(A10BaseClass):
    
    """Class Description::
    Statistics for the object vip-server-v4.

    Class vip-server-v4 supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ipv4: {"optional": false, "oid": "1001", "type": "string", "description": "Specify IP address", "format": "ipv4-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/site/{site_name}/slb-dev/{device_name}/vip-server/vip-server-v4/{ipv4}/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "ipv4"]

        self.b_key = "vip-server-v4"
        self.a10_url="/axapi/v3/gslb/site/{site_name}/slb-dev/{device_name}/vip-server/vip-server-v4/{ipv4}/stats"
        self.DeviceProxy = ""
        self.stats = {}
        self.ipv4 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


