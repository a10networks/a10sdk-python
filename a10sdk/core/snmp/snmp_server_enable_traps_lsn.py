from a10sdk.common.A10BaseClass import A10BaseClass


class Lsn(A10BaseClass):
    
    """Class Description::
    Enable LSN group traps.

    Class lsn supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param all: {"default": 0, "optional": true, "type": "number", "description": "Enable all system group traps", "format": "flag"}
    :param traffic_exceeded: {"default": 0, "optional": true, "type": "number", "description": "Enable LSN trap when NAT pool reaches the threshold", "format": "flag"}
    :param per_ip_port_usage_threshold: {"default": 0, "optional": true, "type": "number", "description": "Enable LSN trap when IP total port usage reaches the threshold (default 64512)", "format": "flag"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param total_port_usage_threshold: {"default": 0, "optional": true, "type": "number", "description": "Enable LSN trap when NAT total port usage reaches the threshold (default 655350000)", "format": "flag"}
    :param max_port_threshold: {"description": "Maximum threshold", "format": "number", "default": 655350000, "optional": true, "maximum": 655355000, "minimum": 10000, "type": "number"}
    :param max_ipport_threshold: {"description": "Maximum threshold", "format": "number", "default": 64512, "optional": true, "maximum": 64512, "minimum": 10000, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/snmp-server/enable/traps/lsn`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "lsn"
        self.a10_url="/axapi/v3/snmp-server/enable/traps/lsn"
        self.DeviceProxy = ""
        self.A10WW_all = ""
        self.traffic_exceeded = ""
        self.per_ip_port_usage_threshold = ""
        self.uuid = ""
        self.total_port_usage_threshold = ""
        self.max_port_threshold = ""
        self.max_ipport_threshold = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


