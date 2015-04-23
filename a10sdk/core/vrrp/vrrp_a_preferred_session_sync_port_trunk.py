from a10sdk.common.A10BaseClass import A10BaseClass


class Trunk(A10BaseClass):
    
    """Class Description::
    preferred-session-sync-port trunk.

    Class trunk supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param pre_vlan: {"description": "Interface VLAN (VLAN ID)", "format": "number", "type": "number", "maximum": 4094, "minimum": 1, "optional": true}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param pre_trunk: {"optional": false, "type": "number", "description": "Trunk Interface number", "format": "interface"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/vrrp-a/preferred-session-sync-port/trunk/{pre_trunk}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "pre_trunk"]

        self.b_key = "trunk"
        self.a10_url="/axapi/v3/vrrp-a/preferred-session-sync-port/trunk/{pre_trunk}"
        self.DeviceProxy = ""
        self.pre_vlan = ""
        self.uuid = ""
        self.pre_trunk = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


