from a10sdk.common.A10BaseClass import A10BaseClass


class SlbChange(A10BaseClass):
    
    """Class Description::
    Enable SLB change traps.

    Class slb-change supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param all: {"default": 0, "optional": true, "type": "number", "description": "Enable all system group traps", "format": "flag"}
    :param resource_usage_warning: {"default": 0, "optional": true, "type": "number", "description": "Enable partition resource usage warning trap", "format": "flag"}
    :param ssl_cert_change: {"default": 0, "optional": true, "type": "number", "description": "Enable SSL certificate change trap", "format": "flag"}
    :param ssl_cert_expire: {"default": 0, "optional": true, "type": "number", "description": "Enable SSL certificate expiring trap", "format": "flag"}
    :param server: {"default": 0, "optional": true, "type": "number", "description": "Enable slb server create/delete trap", "format": "flag"}
    :param vip: {"default": 0, "optional": true, "type": "number", "description": "Enable slb vip create/delete trap", "format": "flag"}
    :param connection_resource_event: {"default": 0, "optional": true, "type": "number", "description": "Enable system connection resource event trap", "format": "flag"}
    :param server_port: {"default": 0, "optional": true, "type": "number", "description": "Enable slb server port create/delete trap", "format": "flag"}
    :param vip_port: {"default": 0, "optional": true, "type": "number", "description": "Enable slb vip-port create/delete trap", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/snmp-server/enable/traps/slb-change`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "slb-change"
        self.a10_url="/axapi/v3/snmp-server/enable/traps/slb-change"
        self.DeviceProxy = ""
        self.A10WW_all = ""
        self.resource_usage_warning = ""
        self.ssl_cert_change = ""
        self.ssl_cert_expire = ""
        self.server = ""
        self.vip = ""
        self.connection_resource_event = ""
        self.server_port = ""
        self.vip_port = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


