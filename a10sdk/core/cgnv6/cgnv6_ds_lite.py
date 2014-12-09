from a10sdk.common.A10BaseClass import A10BaseClass


class DsLite(A10BaseClass):
    
    """Class Description::
    Configure Dual-Stack Lite (DS-Lite).

    Class ds-lite supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param port_reservation_list: {"minItems": 1, "items": {"type": "port-reservation"}, "uniqueItems": true, "array": [{"required": ["inside", "tunnel-dest-address", "inside-addr", "inside-start-port", "inside-end-port", "nat", "nat-start-port", "nat-end-port"], "properties": {"nat-end-port": {"description": "NAT End Port", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": false}, "inside": {"optional": false, "type": "string", "description": "Inside User Address and Port Range (DS-Lite Inside User's Tunnel Source IPv6 Address)", "format": "ipv6-address"}, "tunnel-dest-address": {"optional": false, "type": "string", "description": "DS-Lite Inside User's Tunnel Destination IPv6 Address", "format": "ipv6-address"}, "inside-start-port": {"description": "Inside Start Port", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": false}, "nat": {"optional": false, "type": "string", "description": "NAT Port Range (NAT IP address)", "format": "ipv4-address"}, "inside-end-port": {"description": "Inside End Port", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": false}, "nat-start-port": {"description": "NAT Start Port", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": false}, "inside-addr": {"optional": false, "type": "string", "description": "Inside User IP address", "format": "ipv4-address"}}}], "type": "array", "$ref": "/axapi/v3/cgnv6/ds-lite/port-reservation/{inside}+{tunnel-dest-address}+{inside-addr}+{inside-start-port}+{inside-end-port}+{nat}+{nat-start-port}+{nat-end-port}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/ds-lite`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "ds-lite"
        self.a10_url="/axapi/v3/cgnv6/ds-lite"
        self.DeviceProxy = ""
        self.alg = {}
        self.fragmentation = {}
        self.A10WW_global = {}
        self.port_reservation_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


