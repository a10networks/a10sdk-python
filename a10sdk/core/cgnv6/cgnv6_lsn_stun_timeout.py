from a10sdk.common.A10BaseClass import A10BaseClass


class StunTimeout(A10BaseClass):
    
    """Class Description::
    Set STUN timeout.

    Class stun-timeout supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param udp_list: {"minItems": 1, "items": {"type": "udp"}, "uniqueItems": true, "array": [{"required": ["port-start", "port-end"], "properties": {"port-start": {"description": "Port Range (Port Range Start)", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": false}, "port-end": {"description": "Port Range (Port Range End)", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": false}, "timeout": {"description": "STUN timeout in minutes (default: 2 minutes)", "format": "number", "type": "number", "maximum": 60, "minimum": 0, "optional": true}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/cgnv6/lsn/stun-timeout/udp/{port-start}+{port-end}"}
    :param tcp_list: {"minItems": 1, "items": {"type": "tcp"}, "uniqueItems": true, "array": [{"required": ["port-start", "port-end"], "properties": {"port-start": {"description": "Port Range (Port Range Start)", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": false}, "port-end": {"description": "Port Range (Port Range End)", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": false}, "timeout": {"description": "STUN timeout in minutes (default: 2 minutes)", "format": "number", "type": "number", "maximum": 60, "minimum": 0, "optional": true}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/cgnv6/lsn/stun-timeout/tcp/{port-start}+{port-end}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/lsn/stun-timeout`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "stun-timeout"
        self.a10_url="/axapi/v3/cgnv6/lsn/stun-timeout"
        self.DeviceProxy = ""
        self.udp_list = []
        self.tcp_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


