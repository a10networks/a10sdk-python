from a10sdk.common.A10BaseClass import A10BaseClass


class Bgp(A10BaseClass):
    
    """Class Description::
    Enable bgp traps.

    Class bgp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param bgpEstablishedNotification: {"default": 0, "optional": true, "type": "number", "description": "Enable bgpEstablishedNotification traps", "format": "flag"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param bgpBackwardTransNotification: {"default": 0, "optional": true, "type": "number", "description": "Enable bgpBackwardTransNotification traps", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/snmp-server/enable/traps/routing/bgp`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "bgp"
        self.a10_url="/axapi/v3/snmp-server/enable/traps/routing/bgp"
        self.DeviceProxy = ""
        self.bgpEstablishedNotification = ""
        self.uuid = ""
        self.bgpBackwardTransNotification = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


