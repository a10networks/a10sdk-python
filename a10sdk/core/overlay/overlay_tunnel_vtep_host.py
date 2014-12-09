from a10sdk.common.A10BaseClass import A10BaseClass


class Host(A10BaseClass):
    
    """Class Description::
    IP Address of the local tunnel end point.

    Class host supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param destination_vtep: {"optional": false, "type": "string", "description": "Configure the VTEP IP address (IPv4 address of the VTEP for the remote host)", "format": "ipv4-address"}
    :param ip_addr: {"optional": false, "type": "string", "description": "IPv4 address of the overlay host", "format": "ipv4-address"}
    :param vni: {"description": " Configure the segment id ( VNI of the remote host)", "format": "number", "type": "number", "maximum": 16777215, "minimum": 1, "optional": false}
    :param overlay_mac_addr: {"optional": false, "type": "string", "description": "MAC Address of the overlay host", "format": "mac-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/overlay-tunnel/vtep/{id}/host/{ip_addr}+{overlay_mac_addr}+{vni}+{destination_vtep}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "ip_addr","overlay_mac_addr","vni","destination_vtep"]

        self.b_key = "host"
        self.a10_url="/axapi/v3/overlay-tunnel/vtep/{id}/host/{ip_addr}+{overlay_mac_addr}+{vni}+{destination_vtep}"
        self.DeviceProxy = ""
        self.destination_vtep = ""
        self.ip_addr = ""
        self.vni = ""
        self.overlay_mac_addr = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


