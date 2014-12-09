from a10sdk.common.A10BaseClass import A10BaseClass


class VlanList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param vlan_start: {"$ref": "https://axapi.a10networks.com/axapi/v3/vlan", "type": "number", "description": "VLAN id. help-val VLAN id", "format": "number"}
    :param vlan_end: {"type": "number", "description": "VLAN id", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "vlan-list"
        self.DeviceProxy = ""
        self.vlan_start = ""
        self.vlan_end = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class BridgeVlanGroup(A10BaseClass):
    
    """Class Description::
    Bridge VLAN Group Settings.

    Class bridge-vlan-group supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ve: {"description": "Virtual Ethernet Port. help-val Virtual Ethernet Port number", "format": "number", "type": "number", "maximum": 4094, "minimum": 2, "optional": true}
    :param vlan_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "vlan-start": {"$ref": "https://axapi.a10networks.com/axapi/v3/vlan", "type": "number", "description": "VLAN id. help-val VLAN id", "format": "number"}, "vlan-end": {"type": "number", "description": "VLAN id", "format": "number"}}}]}
    :param forward_traffic: {"description": "forward-all-traffic: \"Forward all traffic between bridge members\"; forward-ip-traffic: \"Forward only IP traffic between bridge members (default)\"; ", "format": "enum", "default": "forward-ip-traffic", "type": "string", "enum": ["forward-all-traffic", "forward-ip-traffic"], "optional": true}
    :param bridge_vlan_group_number: {"description": "Bridge VLAN Group Number", "format": "number", "type": "number", "maximum": 255, "minimum": 1, "optional": false}
    :param name: {"description": "Bridge Group Name. help-val Bridge Group Name", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/bridge-vlan-group/{bridge_vlan_group_number}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "bridge_vlan_group_number"]

        self.b_key = "bridge-vlan-group"
        self.a10_url="/axapi/v3/bridge-vlan-group/{bridge_vlan_group_number}"
        self.DeviceProxy = ""
        self.ve = ""
        self.vlan_list = []
        self.forward_traffic = ""
        self.bridge_vlan_group_number = ""
        self.name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


