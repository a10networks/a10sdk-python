from a10sdk.common.A10BaseClass import A10BaseClass


class PortReservation(A10BaseClass):
    
    """Class Description::
    DS-Lite Static Port Reservation.

    Class port-reservation supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param nat_end_port: {"description": "NAT End Port", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": false}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param inside: {"optional": false, "type": "string", "description": "Inside User Address and Port Range (DS-Lite Inside User's Tunnel Source IPv6 Address)", "format": "ipv6-address"}
    :param tunnel_dest_address: {"optional": false, "type": "string", "description": "DS-Lite Inside User's Tunnel Destination IPv6 Address", "format": "ipv6-address"}
    :param inside_start_port: {"description": "Inside Start Port", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": false}
    :param nat: {"optional": false, "type": "string", "description": "NAT Port Range (NAT IP address)", "format": "ipv4-address"}
    :param inside_end_port: {"description": "Inside End Port", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": false}
    :param nat_start_port: {"description": "NAT Start Port", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": false}
    :param inside_addr: {"optional": false, "type": "string", "description": "Inside User IP address", "format": "ipv4-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/ds-lite/port-reservation/{inside}+{tunnel_dest_address}+{inside_addr}+{inside_start_port}+{inside_end_port}+{nat}+{nat_start_port}+{nat_end_port}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "inside","tunnel_dest_address","inside_addr","inside_start_port","inside_end_port","nat","nat_start_port","nat_end_port"]

        self.b_key = "port-reservation"
        self.a10_url="/axapi/v3/cgnv6/ds-lite/port-reservation/{inside}+{tunnel_dest_address}+{inside_addr}+{inside_start_port}+{inside_end_port}+{nat}+{nat_start_port}+{nat_end_port}"
        self.DeviceProxy = ""
        self.nat_end_port = ""
        self.uuid = ""
        self.inside = ""
        self.tunnel_dest_address = ""
        self.inside_start_port = ""
        self.nat = ""
        self.inside_end_port = ""
        self.nat_start_port = ""
        self.inside_addr = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


