from a10sdk.common.A10BaseClass import A10BaseClass


class Ipv4Gateway(A10BaseClass):
    
    """Class Description::
    IPv4 Gateway.

    Class ipv4-gateway supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ip_address: {"optional": false, "type": "string", "description": "IP Address", "format": "ipv4-address"}
    :param priority_cost: {"description": "The amount the priority will decrease. help-val Priority", "format": "number", "type": "number", "maximum": 255, "minimum": 1, "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/vrrp-a/vrid/{vrid_val}/tracking-options/gateway/ipv4-gateway/{ip_address}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "ip_address"]

        self.b_key = "ipv4-gateway"
        self.a10_url="/axapi/v3/vrrp-a/vrid/{vrid_val}/tracking-options/gateway/ipv4-gateway/{ip_address}"
        self.DeviceProxy = ""
        self.ip_address = ""
        self.priority_cost = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


