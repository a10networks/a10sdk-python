from a10sdk.common.A10BaseClass import A10BaseClass


class SlbDev(A10BaseClass):
    
    """Class Description::
    Specify a SLB device for the GSLB site.

    Class slb-dev supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param client_ip: {"optional": true, "type": "string", "description": "Specify client IP address", "format": "ipv4-address"}
    :param device_name: {"description": "Specify SLB device name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param proto_aging_fast: {"default": 1, "optional": true, "type": "number", "description": "Fast GSLB Protocol aging", "format": "flag"}
    :param proto_compatible: {"default": 0, "optional": true, "type": "number", "description": "Run GSLB Protocol in compatible mode", "format": "flag"}
    :param auto_map: {"default": 1, "optional": true, "type": "number", "description": "Enable DNS Auto Mapping", "format": "flag"}
    :param proto_aging_time: {"description": "Specify GSLB Protocol aging time, default is 60", "format": "number", "default": 60, "optional": true, "maximum": 65535, "minimum": 1, "type": "number"}
    :param rdt_value: {"description": "Specify Round-delay-time", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": true}
    :param admin_preference: {"description": "Specify administrative preference (Specify admin-preference value,default is 100)", "format": "number", "default": 100, "optional": true, "maximum": 255, "minimum": 0, "type": "number"}
    :param ip_address: {"optional": true, "type": "string", "description": "IP address", "format": "ipv4-address"}
    :param auto_detect: {"description": "'ip': Service IP only; 'port': Service Port only; 'ip-and-port': Both service IP and service port; 'disabled': disable auto-detect; ", "format": "enum", "default": "ip-and-port", "type": "string", "enum": ["ip", "port", "ip-and-port", "disabled"], "optional": true}
    :param health_check_action: {"description": "'health-check': Enable health Check; 'health-check-disable': Disable health check; ", "format": "enum", "default": "health-check", "type": "string", "enum": ["health-check", "health-check-disable"], "optional": true}
    :param max_client: {"description": "Specify maximum number of clients, default is 32768", "format": "number", "default": 32768, "optional": true, "maximum": 2147483647, "minimum": 1, "type": "number"}
    :param gateway_ip_addr: {"optional": true, "type": "string", "description": "IP address", "format": "ipv4-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/site/{site_name}/slb-dev/{device_name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "device_name"]

        self.b_key = "slb-dev"
        self.a10_url="/axapi/v3/gslb/site/{site_name}/slb-dev/{device_name}"
        self.DeviceProxy = ""
        self.client_ip = ""
        self.vip_server = {}
        self.device_name = ""
        self.proto_aging_fast = ""
        self.proto_compatible = ""
        self.auto_map = ""
        self.proto_aging_time = ""
        self.rdt_value = ""
        self.admin_preference = ""
        self.ip_address = ""
        self.auto_detect = ""
        self.health_check_action = ""
        self.max_client = ""
        self.gateway_ip_addr = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


