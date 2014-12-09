from a10sdk.common.A10BaseClass import A10BaseClass


class System(A10BaseClass):
    
    """Class Description::
    Configure System Parameters.

    Class system supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param promiscuous_mode: {"description": "Run in promiscous mode settings", "format": "flag", "default": 0, "type": "number", "plat-pos-list": ["soft-ax"], "optional": true}
    :param glid: {"description": "Apply limits to the whole system", "format": "number", "optional": true, "maximum": 1023, "minimum": 1, "type": "number", "$ref": "/axapi/v3/glid"}
    :param template_policy: {"description": "Apply policy template to the whole system (Policy template name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/slb/template/policy"}
    :param ddos_log: {"default": 0, "optional": true, "type": "number", "description": "log DDoS attack anomalies", "format": "flag"}
    :param ddos_attack: {"default": 0, "optional": true, "type": "number", "description": "System DDoS Attack", "format": "flag"}
    :param module_ctrl_cpu: {"optional": true, "enum": ["high", "low", "medium"], "type": "string", "description": "'high': high cpu usage; 'low': low cpu usage; 'medium': medium cpu usage; ", "format": "enum"}
    :param attack: {"default": 0, "optional": true, "type": "number", "description": "System Attack", "format": "flag"}
    :param template_monitor: {"description": "Apply monitor template to the whole system (Monitor template ID Number)", "format": "number", "optional": true, "maximum": 16, "minimum": 1, "type": "number", "$ref": "/axapi/v3/slb/template/monitor"}
    :param log_cpu_interval: {"description": "Log high CPU interval (Specify consecutive seconds before logging high CPU)", "format": "number", "type": "number", "maximum": 255, "minimum": 15, "optional": true}
    :param anomaly_log: {"default": 0, "optional": true, "type": "number", "description": "log system anomalies", "format": "flag"}
    :param attack_log: {"default": 0, "optional": true, "type": "number", "description": "log attack anomalies", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/system`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "system"
        self.a10_url="/axapi/v3/system"
        self.DeviceProxy = ""
        self.resource_usage = {}
        self.cpu_load_sharing = {}
        self.promiscuous_mode = ""
        self.per_vlan_limit = {}
        self.glid = ""
        self.all_vlan_limit = {}
        self.template_policy = ""
        self.ddos_log = ""
        self.ddos_attack = ""
        self.module_ctrl_cpu = ""
        self.attack = ""
        self.template_monitor = ""
        self.ve_mac_scheme = {}
        self.log_cpu_interval = ""
        self.anomaly_log = ""
        self.attack_log = ""
        self.ipsec = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


