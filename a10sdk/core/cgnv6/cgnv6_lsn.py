from a10sdk.common.A10BaseClass import A10BaseClass


class Lsn(A10BaseClass):
    
    """Class Description::
    Set Large-Scale NAT parameters.

    Class lsn supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param health_check_gateway_list: {"minItems": 1, "items": {"type": "health-check-gateway"}, "uniqueItems": true, "array": [{"required": ["ipv4-addr", "ipv6-addr"], "properties": {"ipv4-addr": {"optional": false, "type": "string", "description": "Specify IPv4 Gateway", "format": "ipv4-address"}, "ipv6-addr": {"optional": false, "type": "string", "description": "Specify IPv6 Gateway", "format": "ipv6-address"}}}], "type": "array", "$ref": "/axapi/v3/cgnv6/lsn/health-check-gateway/{ipv4-addr}+{ipv6-addr}"}
    :param port_reservation_list: {"minItems": 1, "items": {"type": "port-reservation"}, "uniqueItems": true, "array": [{"required": ["inside", "inside-port-start", "inside-port-end", "nat", "nat-port-start", "nat-port-end"], "properties": {"inside-port-start": {"description": "Inside Start Port", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": false}, "nat-port-start": {"description": "NAT Start Port", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": false}, "inside-port-end": {"description": "Inside End Port", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": false}, "inside": {"optional": false, "type": "string", "description": "Inside User Address and Port Range (Inside User IP address)", "format": "ipv4-address"}, "nat": {"optional": false, "type": "string", "description": "NAT IP address", "format": "ipv4-address"}, "nat-port-end": {"description": "NAT End Port", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": false}}}], "type": "array", "$ref": "/axapi/v3/cgnv6/lsn/port-reservation/{inside}+{inside-port-start}+{inside-port-end}+{nat}+{nat-port-start}+{nat-port-end}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/lsn`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "lsn"
        self.a10_url="/axapi/v3/cgnv6/lsn"
        self.DeviceProxy = ""
        self.port_overloading = {}
        self.endpoint_independent_mapping = {}
        self.health_check_gateway_list = []
        self.alg = {}
        self.inside = {}
        self.A10WW_global = {}
        self.tcp = {}
        self.port_reservation_list = []
        self.stun_timeout = {}
        self.radius = {}
        self.endpoint_independent_filtering = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


