from a10sdk.common.A10BaseClass import A10BaseClass


class Static(A10BaseClass):
    
    """Class Description::
    Allow static routes.

    Class static supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param bfd_list: {"minItems": 1, "items": {"type": "bfd"}, "uniqueItems": true, "array": [{"required": ["local-ip", "nexthop-ip"], "properties": {"local-ip": {"optional": false, "type": "string", "description": "Local IP address", "format": "ipv4-address"}, "nexthop-ip": {"optional": false, "type": "string", "description": "Nexthop IP address", "format": "ipv4-address"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/ip/route/static/bfd/{local-ip}+{nexthop-ip}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ip/route/static`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "static"
        self.a10_url="/axapi/v3/ip/route/static"
        self.DeviceProxy = ""
        self.bfd_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


