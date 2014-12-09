from a10sdk.common.A10BaseClass import A10BaseClass


class VipMap(A10BaseClass):
    
    """Class Description::
    VIP redistribution map.

    Class vip-map supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param floating_IP_forward_address: {"optional": true, "type": "string", "description": "Floating-IP as forward address. help-val Address", "format": "ipv6-address"}
    :param vip_address: {"optional": false, "type": "string", "description": "Address", "format": "ipv6-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/router/ipv6/ospf/{process_id}/redistribute/vip/vip-map/{vip_address}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "vip_address"]

        self.b_key = "vip-map"
        self.a10_url="/axapi/v3/router/ipv6/ospf/{process_id}/redistribute/vip/vip-map/{vip_address}"
        self.DeviceProxy = ""
        self.floating_IP_forward_address = ""
        self.vip_address = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


