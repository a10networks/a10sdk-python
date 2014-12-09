from a10sdk.common.A10BaseClass import A10BaseClass


class NotificationCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param notification: {"default": 0, "type": "number", "description": "Enable lldp notification", "format": "flag"}
    :param interval: {"description": "Configure lldp notification interval, default is 30. help-val The lldp notification interval value, default is 30", "format": "number", "default": 30, "maximum": 3600, "minimum": 5, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "notification-cfg"
        self.DeviceProxy = ""
        self.notification = ""
        self.interval = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class TxSet(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param fast_interval: {"description": "Configure lldp tx fast interval value. help-val The lldp tx fast interval value, default is 1", "format": "number", "default": 1, "maximum": 3600, "minimum": 1, "type": "number"}
    :param fast_count: {"description": "Configure lldp tx fast count value. help-val The lldp tx fast count value, default is 4", "format": "number", "default": 4, "maximum": 8, "minimum": 1, "type": "number"}
    :param hold: {"description": "Configure lldp tx hold multiplier. help-val The lldp tx hold value, default is 4", "format": "number", "default": 4, "maximum": 10, "minimum": 1, "type": "number"}
    :param tx_interval: {"description": "Configure lldp tx interval. help-val The lldp tx interval value, default is 30", "format": "number", "default": 30, "maximum": 3600, "minimum": 1, "type": "number"}
    :param reinit_delay: {"description": "Configure lldp tx reinit delay. help-val The lldp tx reinit_delay value, default is 2", "format": "number", "default": 2, "maximum": 10, "minimum": 1, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "tx-set"
        self.DeviceProxy = ""
        self.fast_interval = ""
        self.fast_count = ""
        self.hold = ""
        self.tx_interval = ""
        self.reinit_delay = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class EnableCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param enable: {"default": 0, "type": "number", "description": "Enable lldp", "format": "flag"}
    :param rx: {"default": 0, "type": "number", "description": "Enable lldp rx", "format": "flag"}
    :param tx: {"default": 0, "type": "number", "description": "Enable lldp tx", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "enable-cfg"
        self.DeviceProxy = ""
        self.enable = ""
        self.rx = ""
        self.tx = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Lldp(A10BaseClass):
    
    """Class Description::
    Configure LLDP.

    Class lldp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param system_description: {"description": "Configure lldp system description. help-val Lldp system description", "format": "string", "minLength": 1, "optional": true, "maxLength": 127, "type": "string"}
    :param system_name: {"description": "Configure lldp system name. help-val Lldp system name", "format": "string", "minLength": 1, "optional": true, "maxLength": 127, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/lldp`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "lldp"
        self.a10_url="/axapi/v3/lldp"
        self.DeviceProxy = ""
        self.system_description = ""
        self.notification_cfg = {}
        self.management_address = {}
        self.tx_set = {}
        self.enable_cfg = {}
        self.system_name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


