from a10sdk.common.A10BaseClass import A10BaseClass


class VlanGlobal(A10BaseClass):
    
    """Class Description::
    Configure global options for vlan.

    Class vlan-global supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param l3_vlan_fwd_disable: {"default": 0, "optional": true, "type": "number", "description": "Disable L3 forwarding between VLANs", "format": "flag"}
    :param enable_def_vlan_l2_forwarding: {"default": 0, "optional": true, "type": "number", "description": "Enable layer 2 forwarding on default vlan", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/network/vlan-global`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "vlan-global"
        self.a10_url="/axapi/v3/network/vlan-global"
        self.DeviceProxy = ""
        self.l3_vlan_fwd_disable = ""
        self.enable_def_vlan_l2_forwarding = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


