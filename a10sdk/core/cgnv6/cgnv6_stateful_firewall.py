from a10sdk.common.A10BaseClass import A10BaseClass


class StatefulFirewall(A10BaseClass):
    
    """Class Description::
    Stateful Firewall Configuration.

    Class stateful-firewall supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param stun_timeout_list: {"minItems": 1, "items": {"type": "stun-timeout"}, "uniqueItems": true, "array": [{"required": ["port", "port-end"], "properties": {"stun-timeout-val-port-range": {"description": "STUN timeout (default: 2 minutes)", "format": "number", "default": 2, "optional": true, "maximum": 60, "minimum": 0, "type": "number"}, "port": {"description": "Single Destination Port or Port Range Start", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": false}, "port-end": {"description": "Port Range End", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": false}}}], "type": "array", "$ref": "/axapi/v3/cgnv6/stateful-firewall/stun-timeout/{port}+{port-end}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/stateful-firewall`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "stateful-firewall"
        self.a10_url="/axapi/v3/cgnv6/stateful-firewall"
        self.DeviceProxy = ""
        self.udp = {}
        self.vrid = {}
        self.alg = {}
        self.A10WW_global = {}
        self.tcp = {}
        self.stun_timeout_list = []
        self.endpoint_independent_filtering = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


