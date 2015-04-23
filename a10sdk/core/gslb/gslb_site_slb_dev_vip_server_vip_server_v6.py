from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "dev_vip_hits"], "type": "string", "description": "'all': all; 'dev_vip_hits': Number of times the service-ip was selected; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class VipServerV6(A10BaseClass):
    
    """Class Description::
    Specify a VIP for the SLB device.

    Class vip-server-v6 supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "dev_vip_hits"], "type": "string", "description": "'all': all; 'dev_vip_hits': Number of times the service-ip was selected; ", "format": "enum"}}}]}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param ipv6: {"optional": false, "type": "string", "description": "Specify IP address (IPv6 address)", "format": "ipv6-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/site/{site_name}/slb-dev/{device_name}/vip-server/vip-server-v6/{ipv6}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "ipv6"]

        self.b_key = "vip-server-v6"
        self.a10_url="/axapi/v3/gslb/site/{site_name}/slb-dev/{device_name}/vip-server/vip-server-v6/{ipv6}"
        self.DeviceProxy = ""
        self.sampling_enable = []
        self.uuid = ""
        self.ipv6 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


