from a10sdk.common.A10BaseClass import A10BaseClass


class Collector(A10BaseClass):
    
    """Class Description::
    Configure sFlow collector (a.k.a. receiver).

    Class collector supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ip_list: {"minItems": 1, "items": {"type": "ip"}, "uniqueItems": true, "array": [{"required": ["addr", "port"], "properties": {"addr": {"optional": false, "type": "string", "description": "Configure sFlow collector IP address", "format": "ipv4-address"}, "port": {"description": "Port number (default is 6343)", "format": "number", "default": 6343, "optional": false, "maximum": 65535, "minimum": 1, "type": "number"}}}], "type": "array", "$ref": "/axapi/v3/sflow/collector/ip/{addr}+{port}"}
    :param ipv6_list: {"minItems": 1, "items": {"type": "ipv6"}, "uniqueItems": true, "array": [{"required": ["addr", "port"], "properties": {"addr": {"optional": false, "type": "string", "description": "Configure sFlow collector IPv6 address", "format": "ipv6-address"}, "port": {"description": "Port number (default is 6343)", "format": "number", "default": 6343, "optional": false, "maximum": 65535, "minimum": 1, "type": "number"}}}], "type": "array", "$ref": "/axapi/v3/sflow/collector/ipv6/{addr}+{port}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/sflow/collector`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "collector"
        self.a10_url="/axapi/v3/sflow/collector"
        self.DeviceProxy = ""
        self.ip_list = []
        self.ipv6_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


