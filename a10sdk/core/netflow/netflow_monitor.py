from a10sdk.common.A10BaseClass import A10BaseClass


class Monitor(A10BaseClass):
    
    """Class Description::
    Configure NetFlow Monitor.

    Class monitor supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param source_ip_use_mgmt: {"default": 0, "optional": true, "type": "number", "description": "Use management interface's IP address for source ip of netflow packets", "format": "flag"}
    :param protocol: {"description": "'v9': Netflow version 9; 'v10': Netflow version 10 (IPFIX); ", "format": "enum", "default": "v9", "type": "string", "enum": ["v9", "v10"], "optional": true}
    :param name: {"description": "Name of netflow monitor", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param disable: {"default": 0, "optional": true, "type": "number", "description": "Disable this netflow monitor", "format": "flag"}
    :param flow_timeout: {"description": "Configure timeout value to export flow records periodically for long-live session ( Number of minutes: default is 10, 0 means only send flow record when session is deleted)", "format": "number", "default": 10, "optional": true, "maximum": 1440, "minimum": 0, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/netflow/monitor/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "monitor"
        self.a10_url="/axapi/v3/netflow/monitor/{name}"
        self.DeviceProxy = ""
        self.source_ip_use_mgmt = ""
        self.protocol = ""
        self.name = ""
        self.source_address = {}
        self.destination = {}
        self.sample = {}
        self.record = {}
        self.disable = ""
        self.resend_template = {}
        self.flow_timeout = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


