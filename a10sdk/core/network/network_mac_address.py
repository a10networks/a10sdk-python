from a10sdk.common.A10BaseClass import A10BaseClass


class MacAddress(A10BaseClass):
    
    """    :param static_list: {"minItems": 1, "items": {"type": "static"}, "uniqueItems": true, "array": [{"required": ["mac", "vlan"], "properties": {"dest": {"default": 0, "optional": true, "type": "number", "description": "Trap MAC with this DA to CPU", "format": "flag"}, "mac": {"optional": false, "type": "string", "description": "Configure a Static MAC address", "format": "mac-address"}, "vlan": {"description": "VLAN Id", "format": "number", "optional": false, "maximum": 4094, "minimum": 2, "type": "number", "$ref": "/axapi/v3/network/vlan"}, "port": {"optional": true, "type": "number", "description": "Ethernet Port on which the Address is applicable (Port Value (Defualt VLAN is 1))", "format": "interface"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/network/mac-address/static/{mac}+{vlan}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Configure a MAC address.

    Class mac-address supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/network/mac-address`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "mac-address"
        self.a10_url="/axapi/v3/network/mac-address"
        self.DeviceProxy = ""
        self.static_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


