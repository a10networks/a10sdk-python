from a10sdk.common.A10BaseClass import A10BaseClass


class Vip(A10BaseClass):
    
    """Class Description::
    Virtual IP (VIP).

    Class vip supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param vip_map_list: {"minItems": 1, "items": {"type": "vip-map"}, "uniqueItems": true, "array": [{"required": ["vip-address"], "properties": {"floating-IP-forward-address": {"optional": true, "type": "string", "description": "Floating-IP as forward address. help-val Address", "format": "ipv4-address"}, "vip-address": {"optional": false, "type": "string", "description": "Address", "format": "ipv4-address"}}}], "type": "array", "$ref": "https://axapi.a10networks.com/axapi/v3/router/ospf/{process-id}/redistribute/vip/vip-map/{vip-address}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/router/ospf/{process_id}/redistribute/vip`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "vip"
        self.a10_url="/axapi/v3/router/ospf/{process_id}/redistribute/vip"
        self.DeviceProxy = ""
        self.vip_map_list = []
        self.vip_redist = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


