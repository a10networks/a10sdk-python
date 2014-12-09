from a10sdk.common.A10BaseClass import A10BaseClass


class TunnelAddress(A10BaseClass):
    
    """    :param ipv6_tunnel_addr: {"optional": false, "type": "string", "description": "Tunnel IPv6 Endpoint Address", "format": "ipv6-address"}
    :param nat_address_list: {"minItems": 1, "items": {"type": "nat-address"}, "uniqueItems": true, "array": [{"required": ["ipv4-nat-addr"], "properties": {"ipv4-nat-addr": {"optional": false, "type": "string", "description": "NAT IPv4 Address", "format": "ipv4-address"}, "port-list": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "port-start": {"type": "number", "description": "Single Port or Port Range Start", "format": "number"}, "port-end": {"type": "number", "description": "Port Range End", "format": "number"}}}]}}}], "type": "array", "$ref": "/axapi/v3/cgnv6/lw-4o6/binding-table/{name}/tunnel-address/{ipv6-tunnel-addr}/nat-address/{ipv4-nat-addr}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Tunnel IPv6 Endpoint Address.

    Class tunnel-address supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/lw-4o6/binding-table/{name}/tunnel-address/{ipv6_tunnel_addr}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "ipv6_tunnel_addr"]

        self.b_key = "tunnel-address"
        self.a10_url="/axapi/v3/cgnv6/lw-4o6/binding-table/{name}/tunnel-address/{ipv6_tunnel_addr}"
        self.DeviceProxy = ""
        self.ipv6_tunnel_addr = ""
        self.nat_address_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


