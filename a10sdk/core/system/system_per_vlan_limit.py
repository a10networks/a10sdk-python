from a10sdk.common.A10BaseClass import A10BaseClass


class PerVlanLimit(A10BaseClass):
    
    """    :param unknown_ucast: {"description": "unknown unicast packets (per second limit)", "format": "number", "default": 1000, "optional": true, "maximum": 65535, "minimum": 1, "type": "number"}
    :param bcast: {"description": "broadcast packets (per second limit)", "format": "number", "default": 1000, "optional": true, "maximum": 65535, "minimum": 1, "type": "number"}
    :param mcast: {"description": "multicast packets (per second limit)", "format": "number", "default": 1000, "optional": true, "maximum": 65535, "minimum": 1, "type": "number"}
    :param ipmcast: {"description": "IP multicast packets (per second limit)", "format": "number", "default": 1000, "optional": true, "maximum": 65535, "minimum": 1, "type": "number"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Per vlan flooding packet limit.

    Class per-vlan-limit supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/system/per-vlan-limit`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "per-vlan-limit"
        self.a10_url="/axapi/v3/system/per-vlan-limit"
        self.DeviceProxy = ""
        self.unknown_ucast = ""
        self.bcast = ""
        self.mcast = ""
        self.ipmcast = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


