from a10sdk.common.A10BaseClass import A10BaseClass


class VipServer(A10BaseClass):
    
    """Class Description::
    Specify a VIP for the SLB device.

    Class vip-server supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param vip_server_v4_list: {"minItems": 1, "items": {"type": "vip-server-v4"}, "uniqueItems": true, "array": [{"required": ["ipv4"], "properties": {"ipv4": {"optional": false, "type": "string", "description": "Specify IP address", "format": "ipv4-address"}}}], "type": "array", "$ref": "/axapi/v3/gslb/site/{site-name}/slb-dev/{device-name}/vip-server/vip-server-v4/{ipv4}"}
    :param vip_server_v6_list: {"minItems": 1, "items": {"type": "vip-server-v6"}, "uniqueItems": true, "array": [{"required": ["ipv6"], "properties": {"ipv6": {"optional": false, "type": "string", "description": "Specify IP address (IPv6 address)", "format": "ipv6-address"}}}], "type": "array", "$ref": "/axapi/v3/gslb/site/{site-name}/slb-dev/{device-name}/vip-server/vip-server-v6/{ipv6}"}
    :param vip_server_name_list: {"minItems": 1, "items": {"type": "vip-server-name"}, "uniqueItems": true, "array": [{"required": ["vip-name"], "properties": {"vip-name": {"description": "Specify a VIP name for the SLB device", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/gslb/service-ip"}}}], "type": "array", "$ref": "/axapi/v3/gslb/site/{site-name}/slb-dev/{device-name}/vip-server/vip-server-name/{vip-name}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/site/{site_name}/slb-dev/{device_name}/vip-server`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "vip-server"
        self.a10_url="/axapi/v3/gslb/site/{site_name}/slb-dev/{device_name}/vip-server"
        self.DeviceProxy = ""
        self.vip_server_v4_list = []
        self.vip_server_v6_list = []
        self.vip_server_name_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


