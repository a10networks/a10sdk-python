from a10sdk.common.A10BaseClass import A10BaseClass


class L2InlinePeerIp(A10BaseClass):
    
    """Class Description::
    Peer IP for Layer 2 inline mode.

    Class l2-inline-peer-ip supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param ip_address: {"optional": false, "type": "string", "description": "IP address (IPv4 address)", "format": "ipv4-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/vrrp-a/l2-inline-peer-ip/{ip_address}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "ip_address"]

        self.b_key = "l2-inline-peer-ip"
        self.a10_url="/axapi/v3/vrrp-a/l2-inline-peer-ip/{ip_address}"
        self.DeviceProxy = ""
        self.uuid = ""
        self.ip_address = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


