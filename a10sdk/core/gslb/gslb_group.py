from a10sdk.common.A10BaseClass import A10BaseClass


class PrimaryList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param primary: {"type": "string", "description": "Specify Primary controller's IP address", "format": "ipv4-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "primary-list"
        self.DeviceProxy = ""
        self.primary = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Group(A10BaseClass):
    
    """Class Description::
    GSLB Group.

    Class group supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param enable: {"default": 0, "optional": true, "type": "number", "description": "Join GSLB Group", "format": "flag"}
    :param name: {"description": "Specify Group domain name", "format": "string", "default": "default", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param standalone: {"default": 0, "optional": true, "type": "number", "description": "Run GSLB Group in standalone mode", "format": "flag"}
    :param learn: {"default": 1, "optional": true, "type": "number", "description": "Learn neighbour information from other controllers", "format": "flag"}
    :param mgmt_interface: {"default": 1, "optional": true, "type": "number", "description": "Management Interface IP Address", "format": "flag"}
    :param dns_discover: {"default": 1, "optional": true, "type": "number", "description": "Discover member via DNS Protocol", "format": "flag"}
    :param priority: {"description": "Specify Local Priority, default is 100", "format": "number", "default": 100, "optional": true, "maximum": 255, "minimum": 1, "type": "number"}
    :param config_anywhere: {"default": 0, "optional": true, "type": "number", "description": "Every member can do config", "format": "flag"}
    :param data_interface: {"default": 1, "optional": true, "type": "number", "description": "Data Interface IP Address", "format": "flag"}
    :param auto_map_primary: {"default": 1, "optional": true, "type": "number", "description": "Primary Controller's IP address", "format": "flag"}
    :param auto_map_learn: {"default": 1, "optional": true, "type": "number", "description": "IP Address learned from other controller", "format": "flag"}
    :param primary_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "primary": {"type": "string", "description": "Specify Primary controller's IP address", "format": "ipv4-address"}}}]}
    :param suffix: {"description": "Set DNS Suffix (Name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param config_merge: {"default": 0, "optional": true, "type": "number", "description": "Merge old master's config when new one take over", "format": "flag"}
    :param auto_map_smart: {"default": 1, "optional": true, "type": "number", "description": "Choose Best IP address", "format": "flag"}
    :param config_save: {"default": 1, "optional": true, "type": "number", "description": "Accept config-save message from master", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/group/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "group"
        self.a10_url="/axapi/v3/gslb/group/{name}"
        self.DeviceProxy = ""
        self.enable = ""
        self.name = ""
        self.standalone = ""
        self.learn = ""
        self.mgmt_interface = ""
        self.dns_discover = ""
        self.priority = ""
        self.config_anywhere = ""
        self.data_interface = ""
        self.auto_map_primary = ""
        self.auto_map_learn = ""
        self.primary_list = []
        self.suffix = ""
        self.config_merge = ""
        self.auto_map_smart = ""
        self.config_save = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


