from a10sdk.common.A10BaseClass import A10BaseClass


class PortRange(A10BaseClass):
    
    """    :param port_start: {"optional": false, "type": "number", "description": "Single Port or Port Range Start", "format": "number"}
    :param port_end: {"optional": false, "type": "number", "description": "Port Range End", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Single Port or Port Range Start.

    Class port-range supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/lw-4o6/binding-table/{name}/tunnel-address/{ipv6_tunnel_addr}/nat-address/{ipv4_nat_addr}/port-range/{port_start}+{port_end}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "port_start","port_end"]

        self.b_key = "port-range"
        self.a10_url="/axapi/v3/cgnv6/lw-4o6/binding-table/{name}/tunnel-address/{ipv6_tunnel_addr}/nat-address/{ipv4_nat_addr}/port-range/{port_start}+{port_end}"
        self.DeviceProxy = ""
        self.port_start = ""
        self.port_end = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


