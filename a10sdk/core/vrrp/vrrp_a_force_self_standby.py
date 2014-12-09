from a10sdk.common.A10BaseClass import A10BaseClass


class ForceSelfStandby(A10BaseClass):
    
    """    :param vrid: {"description": "Specify one VRRP-A vrid to force into standby state", "format": "number", "type": "number", "maximum": 31, "minimum": 0, "optional": true}
    :param all_partitions: {"default": 0, "optional": true, "type": "number", "description": "force all partitions in standby state", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    HA VRRP-A Operational Command to force the unit or a group to HA standby state.

    Class force-self-standby supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/vrrp-a/force-self-standby`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "force-self-standby"
        self.a10_url="/axapi/v3/vrrp-a/force-self-standby"
        self.DeviceProxy = ""
        self.vrid = ""
        self.all_partitions = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


