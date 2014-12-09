from a10sdk.common.A10BaseClass import A10BaseClass


class Host(A10BaseClass):
    
    """Class Description::
    Set remote syslog host DNS name or ip address.

    Class host supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ipv6addr_list: {"minItems": 1, "items": {"type": "ipv6addr"}, "uniqueItems": true, "array": [{"required": ["host-ipv6"], "properties": {"host-ipv6": {"optional": false, "type": "string", "description": "Set syslog host ipv6 address", "format": "ipv6-address"}, "tcp": {"description": "Use TCP as transport protocol", "partition-visibility": "shared", "default": 0, "type": "number", "format": "flag", "optional": true}, "port": {"description": "Set remote syslog port number", "format": "number", "default": 514, "optional": true, "maximum": 32767, "minimum": 1, "type": "number"}, "use-mgmt-port": {"description": "Use management port for connections", "partition-visibility": "shared", "default": 0, "type": "number", "format": "flag", "optional": true}}}], "type": "array", "$ref": "/axapi/v3/logging/host/ipv6addr/{host-ipv6}"}
    :param ipv4addr_list: {"minItems": 1, "items": {"type": "ipv4addr"}, "uniqueItems": true, "array": [{"required": ["host-ipv4"], "properties": {"tcp": {"description": "Use TCP as transport protocol", "partition-visibility": "shared", "default": 0, "type": "number", "format": "flag", "optional": true}, "host-ipv4": {"optional": false, "type": "string", "description": "Set syslog host ip address", "format": "host"}, "port": {"description": "Set remote syslog port number", "format": "number", "default": 514, "optional": true, "maximum": 32767, "minimum": 1, "type": "number"}, "use-mgmt-port": {"description": "Use management port for connections", "partition-visibility": "shared", "default": 0, "type": "number", "format": "flag", "optional": true}}}], "type": "array", "$ref": "/axapi/v3/logging/host/ipv4addr/{host-ipv4}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/logging/host`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "host"
        self.a10_url="/axapi/v3/logging/host"
        self.DeviceProxy = ""
        self.ipv6addr_list = []
        self.partition = {}
        self.ipv4addr_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


