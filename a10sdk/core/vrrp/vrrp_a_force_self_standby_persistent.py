from a10sdk.common.A10BaseClass import A10BaseClass


class ForceSelfStandbyPersistent(A10BaseClass):
    
    """Class Description::
    HA VRRP-A Configured  Command to force the unit or a group to HA standby state.

    Class force-self-standby-persistent supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param vrid: {"description": "Specify one VRRP-A vrid to force into standby state", "format": "number", "type": "number", "maximum": 31, "minimum": 0, "optional": false}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/vrrp-a/force-self-standby-persistent/{vrid}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "vrid"]

        self.b_key = "force-self-standby-persistent"
        self.a10_url="/axapi/v3/vrrp-a/force-self-standby-persistent/{vrid}"
        self.DeviceProxy = ""
        self.vrid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


