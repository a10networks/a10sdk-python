from a10sdk.common.A10BaseClass import A10BaseClass


class TxDot1Cfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param link_aggregation: {"default": 0, "type": "number", "description": "Interface link aggregation information", "format": "flag"}
    :param vlan: {"default": 0, "type": "number", "description": "Interface vlan information", "format": "flag"}
    :param tx_dot1_tlvs: {"default": 0, "type": "number", "description": "Interface lldp tx IEEE 802.1 Organizationally specific TLVs configuration", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "tx-dot1-cfg"
        self.DeviceProxy = ""
        self.link_aggregation = ""
        self.vlan = ""
        self.tx_dot1_tlvs = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class NotificationCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param notification: {"default": 0, "type": "number", "description": "Interface lldp notification configuration", "format": "flag"}
    :param notif_enable: {"default": 0, "type": "number", "description": "Interface lldp notification enable", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "notification-cfg"
        self.DeviceProxy = ""
        self.notification = ""
        self.notif_enable = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class TxTlvsCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param system_capabilities: {"default": 0, "type": "number", "description": "Interface lldp system capabilities", "format": "flag"}
    :param system_description: {"default": 0, "type": "number", "description": "Interface lldp system description", "format": "flag"}
    :param management_address: {"default": 0, "type": "number", "description": "Interface lldp management address", "format": "flag"}
    :param tx_tlvs: {"default": 0, "type": "number", "description": "Interface lldp tx TLVs configuration", "format": "flag"}
    :param exclude: {"default": 0, "type": "number", "description": "Configure which TLVs excluded. All basic TLVs will be included by default", "format": "flag"}
    :param port_description: {"default": 0, "type": "number", "description": "Interface lldp port description", "format": "flag"}
    :param system_name: {"default": 0, "type": "number", "description": "Interface lldp system name", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "tx-tlvs-cfg"
        self.DeviceProxy = ""
        self.system_capabilities = ""
        self.system_description = ""
        self.management_address = ""
        self.tx_tlvs = ""
        self.exclude = ""
        self.port_description = ""
        self.system_name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class EnableCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param rx: {"default": 0, "type": "number", "description": "Enable lldp rx", "format": "flag"}
    :param tx: {"default": 0, "type": "number", "description": "Enable lldp tx", "format": "flag"}
    :param rt_enable: {"default": 0, "type": "number", "description": "Interface lldp enable/disable", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "enable-cfg"
        self.DeviceProxy = ""
        self.rx = ""
        self.tx = ""
        self.rt_enable = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Lldp(A10BaseClass):
    
    """Class Description::
    Interface lldp configuration.

    Class lldp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/interface/ethernet/{ifnum}/lldp`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "lldp"
        self.a10_url="/axapi/v3/interface/ethernet/{ifnum}/lldp"
        self.DeviceProxy = ""
        self.tx_dot1_cfg = {}
        self.notification_cfg = {}
        self.tx_tlvs_cfg = {}
        self.enable_cfg = {}
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


