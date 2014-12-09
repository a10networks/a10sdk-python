from a10sdk.common.A10BaseClass import A10BaseClass


class PortReservation(A10BaseClass):
    
    """Class Description::
    Set Port Reservations.

    Class port-reservation supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param inside_port_start: {"description": "Inside Start Port", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": false}
    :param nat_port_start: {"description": "NAT Start Port", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": false}
    :param inside_port_end: {"description": "Inside End Port", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": false}
    :param inside: {"optional": false, "type": "string", "description": "Inside User Address and Port Range (Inside User IP address)", "format": "ipv4-address"}
    :param nat: {"optional": false, "type": "string", "description": "NAT IP address", "format": "ipv4-address"}
    :param nat_port_end: {"description": "NAT End Port", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": false}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/lsn/port-reservation/{inside}+{inside_port_start}+{inside_port_end}+{nat}+{nat_port_start}+{nat_port_end}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "inside","inside_port_start","inside_port_end","nat","nat_port_start","nat_port_end"]

        self.b_key = "port-reservation"
        self.a10_url="/axapi/v3/cgnv6/lsn/port-reservation/{inside}+{inside_port_start}+{inside_port_end}+{nat}+{nat_port_start}+{nat_port_end}"
        self.DeviceProxy = ""
        self.inside_port_start = ""
        self.nat_port_start = ""
        self.inside_port_end = ""
        self.inside = ""
        self.nat = ""
        self.nat_port_end = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


