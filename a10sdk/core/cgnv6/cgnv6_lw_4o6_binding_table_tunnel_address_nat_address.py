from a10sdk.common.A10BaseClass import A10BaseClass


class PortList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param port_start: {"type": "number", "description": "Single Port or Port Range Start", "format": "number"}
    :param port_end: {"type": "number", "description": "Port Range End", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "port-list"
        self.DeviceProxy = ""
        self.port_start = ""
        self.port_end = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class NatAddress(A10BaseClass):
    
    """    :param ipv4_nat_addr: {"optional": false, "type": "string", "description": "NAT IPv4 Address", "format": "ipv4-address"}
    :param port_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "port-start": {"type": "number", "description": "Single Port or Port Range Start", "format": "number"}, "port-end": {"type": "number", "description": "Port Range End", "format": "number"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    NAT IPv4 address.

    Class nat-address supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/lw-4o6/binding-table/{name}/tunnel-address/{ipv6_tunnel_addr}/nat-address/{ipv4_nat_addr}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "ipv4_nat_addr"]

        self.b_key = "nat-address"
        self.a10_url="/axapi/v3/cgnv6/lw-4o6/binding-table/{name}/tunnel-address/{ipv6_tunnel_addr}/nat-address/{ipv4_nat_addr}"
        self.DeviceProxy = ""
        self.ipv4_nat_addr = ""
        self.port_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


