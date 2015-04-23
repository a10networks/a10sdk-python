from a10sdk.common.A10BaseClass import A10BaseClass


class Ipv6Gateway(A10BaseClass):
    
    """Class Description::
    IPv6 Gateway.

    Class ipv6-gateway supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ipv6_address: {"optional": false, "type": "string", "description": "IPV6 address", "format": "ipv6-address"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param priority_cost: {"description": "The amount the priority will decrease", "format": "number", "type": "number", "maximum": 255, "minimum": 1, "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/vrrp-a/vrid/{vrid_val}/blade-parameters/tracking-options/gateway/ipv6-gateway/{ipv6_address}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "ipv6_address"]

        self.b_key = "ipv6-gateway"
        self.a10_url="/axapi/v3/vrrp-a/vrid/{vrid_val}/blade-parameters/tracking-options/gateway/ipv6-gateway/{ipv6_address}"
        self.DeviceProxy = ""
        self.ipv6_address = ""
        self.uuid = ""
        self.priority_cost = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


