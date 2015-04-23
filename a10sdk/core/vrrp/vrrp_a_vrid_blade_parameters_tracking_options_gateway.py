from a10sdk.common.A10BaseClass import A10BaseClass


class Gateway(A10BaseClass):
    
    """Class Description::
    VRRP-A tracking gateway.

    Class gateway supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ipv4_gateway_list: {"minItems": 1, "items": {"type": "ipv4-gateway"}, "uniqueItems": true, "array": [{"required": ["ip-address"], "properties": {"uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "ip-address": {"optional": false, "type": "string", "description": "IP Address", "format": "ipv4-address"}, "priority-cost": {"description": "The amount the priority will decrease", "format": "number", "type": "number", "maximum": 255, "minimum": 1, "optional": true}}}], "type": "array", "$ref": "/axapi/v3/vrrp-a/vrid/{vrid-val}/blade-parameters/tracking-options/gateway/ipv4-gateway/{ip-address}"}
    :param ipv6_gateway_list: {"minItems": 1, "items": {"type": "ipv6-gateway"}, "uniqueItems": true, "array": [{"required": ["ipv6-address"], "properties": {"ipv6-address": {"optional": false, "type": "string", "description": "IPV6 address", "format": "ipv6-address"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "priority-cost": {"description": "The amount the priority will decrease", "format": "number", "type": "number", "maximum": 255, "minimum": 1, "optional": true}}}], "type": "array", "$ref": "/axapi/v3/vrrp-a/vrid/{vrid-val}/blade-parameters/tracking-options/gateway/ipv6-gateway/{ipv6-address}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/vrrp-a/vrid/{vrid_val}/blade-parameters/tracking-options/gateway`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "gateway"
        self.a10_url="/axapi/v3/vrrp-a/vrid/{vrid_val}/blade-parameters/tracking-options/gateway"
        self.DeviceProxy = ""
        self.ipv4_gateway_list = []
        self.ipv6_gateway_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


