from a10sdk.common.A10BaseClass import A10BaseClass


class SourceInterface(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param loopback: {"type": "number", "description": "Loopback interface (Port number)", "format": "interface"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "source-interface"
        self.DeviceProxy = ""
        self.loopback = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class MgmtTraffic(A10BaseClass):
    
    """Class Description::
    Management traffic IP parameters.

    Class mgmt-traffic supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param traffic_type: {"optional": false, "enum": ["all", "ftp", "ntp", "rcp", "snmp", "ssh", "syslog", "telnet", "tftp", "web"], "type": "string", "description": "'all': All; 'ftp': FTP; 'ntp': NTP; 'rcp': RCP; 'snmp': SNMP; 'ssh': SSH and SCP; 'syslog': SYSLOG; 'telnet': Telnet; 'tftp': TFTP; 'web': Web - HTTP and HTTPS; ", "format": "enum"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ip/mgmt-traffic/{traffic_type}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "traffic_type"]

        self.b_key = "mgmt-traffic"
        self.a10_url="/axapi/v3/ip/mgmt-traffic/{traffic_type}"
        self.DeviceProxy = ""
        self.traffic_type = ""
        self.source_interface = {}
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


