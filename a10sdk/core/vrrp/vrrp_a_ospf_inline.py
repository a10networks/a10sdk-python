from a10sdk.common.A10BaseClass import A10BaseClass


class OspfInline(A10BaseClass):
    
    """Class Description::
    Enable OSPF under Layer 3 Inline Hot Standby Mode.

    Class ospf-inline supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param vlan: {"description": "Do not filter OSPF packet on specific vlan (Vlan number)", "format": "number", "type": "number", "maximum": 4094, "minimum": 1, "optional": false}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/vrrp-a/ospf-inline/{vlan}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "vlan"]

        self.b_key = "ospf-inline"
        self.a10_url="/axapi/v3/vrrp-a/ospf-inline/{vlan}"
        self.DeviceProxy = ""
        self.vlan = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


