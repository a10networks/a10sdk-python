from a10sdk.common.A10BaseClass import A10BaseClass


class VipServerName(A10BaseClass):
    
    """Class Description::
    Specify a VIP for the SLB device.

    Class vip-server-name supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param vip_name: {"description": "Specify a VIP name for the SLB device", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/gslb/service-ip"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/site/{site_name}/slb-dev/{device_name}/vip-server/vip-server-name/{vip_name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "vip_name"]

        self.b_key = "vip-server-name"
        self.a10_url="/axapi/v3/gslb/site/{site_name}/slb-dev/{device_name}/vip-server/vip-server-name/{vip_name}"
        self.DeviceProxy = ""
        self.vip_name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


