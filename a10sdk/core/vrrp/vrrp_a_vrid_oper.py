from a10sdk.common.A10BaseClass import A10BaseClass


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param weight: {"type": "number", "format": "number"}
    :param priority: {"type": "number", "format": "number"}
    :param state: {"enum": ["Active", "Standby"], "type": "string", "format": "enum"}
    :param became_active: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param force_standby: {"type": "number", "format": "number"}
    :param unit: {"type": "number", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.weight = ""
        self.priority = ""
        self.state = ""
        self.became_active = ""
        self.force_standby = ""
        self.unit = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Gateway(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "gateway"
        self.DeviceProxy = ""
        self.oper = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class TrackingOptions(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "tracking-options"
        self.DeviceProxy = ""
        self.oper = {}
        self.gateway = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class BladeParameters(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "blade-parameters"
        self.DeviceProxy = ""
        self.oper = {}
        self.tracking_options = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Vrid(A10BaseClass):
    
    """Class Description::
    Operational Status for the object vrid.

    Class vrid supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param vrid_val: {"description": "Specify ha VRRP-A vrid", "format": "number", "default": 0, "optional": false, "oid": "1001", "maximum": 31, "minimum": 0, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/vrrp-a/vrid/{vrid_val}/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "vrid"
        self.a10_url="/axapi/v3/vrrp-a/vrid/{vrid_val}/oper"
        self.DeviceProxy = ""
        self.oper = {}
        self.blade_parameters = {}
        self.vrid_val = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


