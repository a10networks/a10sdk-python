from a10sdk.common.A10BaseClass import A10BaseClass


class Udp(A10BaseClass):
    
    """Class Description::
    Configure UDP parameters for stateful firewall.

    Class udp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param stun_timeout_list: {"minItems": 1, "items": {"type": "stun-timeout"}, "uniqueItems": true, "array": [{"required": ["port", "port-end"], "properties": {"stun-timeout-val-port-range": {"description": "STUN timeout (default: 2 minutes)", "format": "number", "default": 2, "optional": true, "maximum": 60, "minimum": 0, "type": "number"}, "port": {"description": "Single Destination Port or Port Range Start", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": false}, "port-end": {"description": "Port Range End", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": false}}}], "type": "array", "$ref": "/axapi/v3/cgnv6/stateful-firewall/udp/stun-timeout/{port}+{port-end}"}
    :param idle_timeout_list: {"minItems": 1, "items": {"type": "idle-timeout"}, "uniqueItems": true, "array": [{"required": ["port", "port-end"], "properties": {"idle-timeout-val-port-range": {"description": "Idle timeout for IPv4 and IPv6 TCP established sessions (Idle timeout for IPv4 and IPv6 TCP established sessions (default: 300 seconds))", "format": "number", "default": 300, "optional": true, "maximum": 3780, "minimum": 60, "not": "fast", "type": "number"}, "port": {"description": "Single Destination Port or Port Range Start", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": false}, "fast": {"description": "Fast aging for idle sessions", "format": "flag", "default": 0, "optional": true, "not": "idle-timeout-val-port-range", "type": "number"}, "port-end": {"description": "Port Range End", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": false}}}], "type": "array", "$ref": "/axapi/v3/cgnv6/stateful-firewall/udp/idle-timeout/{port}+{port-end}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/stateful-firewall/udp`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "udp"
        self.a10_url="/axapi/v3/cgnv6/stateful-firewall/udp"
        self.DeviceProxy = ""
        self.stun_timeout_list = []
        self.idle_timeout_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


