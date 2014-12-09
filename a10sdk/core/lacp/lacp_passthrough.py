from a10sdk.common.A10BaseClass import A10BaseClass


class LacpPassthrough(A10BaseClass):
    
    """Class Description::
    Peer ports to forward received lacp packets.

    Class lacp-passthrough supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param peer_from: {"optional": false, "type": "number", "description": "Peer member to forward received LACP packets. help-val Peer member to forward received LACP packets", "format": "interface"}
    :param peer_to: {"optional": false, "type": "number", "description": "Peer member to forward received LACP packets. help-val Peer member to forward received LACP packets", "format": "interface"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/lacp-passthrough/{peer_from}+{peer_to}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "peer_from","peer_to"]

        self.b_key = "lacp-passthrough"
        self.a10_url="/axapi/v3/lacp-passthrough/{peer_from}+{peer_to}"
        self.DeviceProxy = ""
        self.peer_from = ""
        self.peer_to = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


