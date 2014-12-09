from a10sdk.common.A10BaseClass import A10BaseClass


class AllVlanLimit(A10BaseClass):
    
    """Class Description::
    all vlan flooding packet limit.

    Class all-vlan-limit supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param unknown_ucast: {"description": "unknown unicast packets (per second limit)", "format": "number", "default": 1000, "optional": true, "maximum": 65535, "minimum": 1, "type": "number"}
    :param bcast: {"description": "broadcast packets (per second limit)", "format": "number", "default": 1000, "optional": true, "maximum": 65535, "minimum": 1, "type": "number"}
    :param mcast: {"description": "multicast packets (per second limit)", "format": "number", "default": 1000, "optional": true, "maximum": 65535, "minimum": 1, "type": "number"}
    :param ipmcast: {"description": "IP multicast packets (per second limit)", "format": "number", "default": 1000, "optional": true, "maximum": 65535, "minimum": 1, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/system/all-vlan-limit`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "all-vlan-limit"
        self.a10_url="/axapi/v3/system/all-vlan-limit"
        self.DeviceProxy = ""
        self.unknown_ucast = ""
        self.bcast = ""
        self.mcast = ""
        self.ipmcast = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


