from a10sdk.common.A10BaseClass import A10BaseClass


class SharedCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param shared: {"default": 0, "not": "name", "type": "number", "description": "Shared partition", "format": "flag"}
    :param vrid: {"default": 0, "type": "number", "description": "VRRP-A id", "format": "flag"}
    :param vrid_value: {"description": "Specify ha VRRP-A vrid", "minimum": 0, "type": "number", "maximum": 31, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "shared-cfg"
        self.DeviceProxy = ""
        self.shared = ""
        self.vrid = ""
        self.vrid_value = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class NameCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param vrid_value: {"description": "Specify ha VRRP-A vrid", "minimum": 0, "type": "number", "maximum": 7, "format": "number"}
    :param vrid: {"default": 0, "type": "number", "description": "VRRP-A id", "format": "flag"}
    :param name: {"description": "Partition name", "format": "string", "minLength": 1, "maxLength": 14, "not": "shared", "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "name-cfg"
        self.DeviceProxy = ""
        self.vrid_value = ""
        self.vrid = ""
        self.name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Partition(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param partition: {"default": 0, "type": "number", "description": "Partition name", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "partition"
        self.DeviceProxy = ""
        self.shared_cfg = {}
        self.name_cfg = {}
        self.partition = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class VridLead(A10BaseClass):
    
    """Class Description::
    Define a vrid-lead.

    Class vrid-lead supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param vrid_lead_str: {"description": "VRRP-A VRID leader name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/vrrp-a/vrid-lead/{vrid_lead_str}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "vrid_lead_str"]

        self.b_key = "vrid-lead"
        self.a10_url="/axapi/v3/vrrp-a/vrid-lead/{vrid_lead_str}"
        self.DeviceProxy = ""
        self.vrid_lead_str = ""
        self.partition = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


