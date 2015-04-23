from a10sdk.common.A10BaseClass import A10BaseClass


class System(A10BaseClass):
    
    """    :param promiscuous_mode: {"description": "Run in promiscous mode settings", "format": "flag", "default": 0, "type": "number", "plat-pos-list": ["soft-ax"], "optional": true}
    :param attack_log: {"default": 0, "optional": true, "type": "number", "description": "log attack anomalies", "format": "flag"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param ddos_attack: {"default": 0, "optional": true, "type": "number", "description": "System DDoS Attack", "format": "flag"}
    :param attack: {"default": 0, "optional": true, "type": "number", "description": "System Attack", "format": "flag"}
    :param anomaly_log: {"default": 0, "optional": true, "type": "number", "description": "log system anomalies", "format": "flag"}
    :param glid: {"description": "Apply limits to the whole system", "format": "number", "optional": true, "maximum": 1023, "minimum": 1, "type": "number", "$ref": "/axapi/v3/glid"}
    :param ddos_log: {"default": 0, "optional": true, "type": "number", "description": "log DDoS attack anomalies", "format": "flag"}
    :param log_cpu_interval: {"description": "Log high CPU interval (Specify consecutive seconds before logging high CPU)", "format": "number", "type": "number", "maximum": 255, "minimum": 15, "optional": true}
    :param module_ctrl_cpu: {"optional": true, "enum": ["high", "low", "medium"], "type": "string", "description": "'high': high cpu usage; 'low': low cpu usage; 'medium': medium cpu usage; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Configure System Parameters.

    Class system supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/system`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "system"
        self.a10_url="/axapi/v3/system"
        self.DeviceProxy = ""
        self.promiscuous_mode = ""
        self.ndisc_ra = {}
        self.tcp = {}
        self.cpu_load_sharing = {}
        self.session = {}
        self.tcp_stats = {}
        self.all_vlan_limit = {}
        self.ip_stats = {}
        self.attack_log = ""
        self.uuid = ""
        self.bfd = {}
        self.ddos_attack = ""
        self.ip6_stats = {}
        self.attack = ""
        self.ve_mac_scheme = {}
        self.anomaly_log = ""
        self.ipsec = {}
        self.template = {}
        self.glid = ""
        self.ddos_log = ""
        self.icmp_rate = {}
        self.log_cpu_interval = ""
        self.icmp = {}
        self.per_vlan_limit = {}
        self.resource_usage = {}
        self.module_ctrl_cpu = ""
        self.icmp6 = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


