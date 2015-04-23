from a10sdk.common.A10BaseClass import A10BaseClass


class GslbCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param group_role: {"default": 0, "type": "number", "description": "Show GSLB group role on CLI prompt", "format": "flag"}
    :param symbol: {"default": 0, "type": "number", "description": "Show \"gslb\" symbol on CLI prompt", "format": "flag"}
    :param disable: {"default": 0, "type": "number", "description": "Group status show disable", "format": "flag"}
    :param gslb_prompt: {"default": 0, "type": "number", "description": "The gslb status prompt function set", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "gslb-cfg"
        self.DeviceProxy = ""
        self.group_role = ""
        self.symbol = ""
        self.disable = ""
        self.gslb_prompt = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class HistoryCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param enable: {"default": 1, "type": "number", "description": "Enable terminal history", "format": "flag"}
    :param size: {"description": "Set history buffer size (Size of history buffer, default is 256)", "format": "number", "default": 256, "maximum": 1000, "minimum": 0, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "history-cfg"
        self.DeviceProxy = ""
        self.enable = ""
        self.size = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class VcsCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param vcs_status: {"default": 0, "type": "number", "description": "Display VCS status in prompt, eg. vMaster, vBlade", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "vcs-cfg"
        self.DeviceProxy = ""
        self.vcs_status = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class PromptCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param hostname: {"default": 0, "type": "number", "description": "Dispaly hostname in prompt", "format": "flag"}
    :param prompt: {"default": 0, "type": "number", "description": "Configure the normal prompt format", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "prompt-cfg"
        self.DeviceProxy = ""
        self.hostname = ""
        self.prompt = ""
        self.vcs_cfg = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Terminal(A10BaseClass):
    
    """    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param idle_timeout: {"description": "Set interval for closing connection when there is no input detected (Timeout in minutes, 0 means never timeout, default is 15)", "format": "number", "default": 15, "optional": true, "maximum": 60, "minimum": 0, "type": "number"}
    :param width: {"description": "Set width of the display terminal (Number of characters on a screen line, 0 means infinite, default is 80)", "format": "number", "default": 80, "optional": true, "maximum": 512, "minimum": 0, "type": "number"}
    :param length: {"description": "Set number of lines on a screen(0 for no pausing) (Number of lines on screen, 0 for no pausing, default is 24)", "format": "number", "default": 24, "optional": true, "maximum": 512, "minimum": 0, "type": "number"}
    :param editing: {"default": 0, "optional": true, "type": "number", "description": "Enable command line editing", "format": "flag"}
    :param auto_size: {"default": 1, "optional": true, "type": "number", "description": "Enable terminal length and width automatically (not work if width or length set to 0)", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Set Terminal Startup Parameters.

    Class terminal supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/terminal`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "terminal"
        self.a10_url="/axapi/v3/terminal"
        self.DeviceProxy = ""
        self.uuid = ""
        self.gslb_cfg = {}
        self.history_cfg = {}
        self.idle_timeout = ""
        self.prompt_cfg = {}
        self.width = ""
        self.length = ""
        self.editing = ""
        self.auto_size = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


