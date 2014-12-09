from a10sdk.common.A10BaseClass import A10BaseClass


class VirtualServer(A10BaseClass):
    
    """Class Description::
    Virtual server template.

    Class virtual-server supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param conn_limit: {"description": "Connection limit", "format": "number", "type": "number", "maximum": 8000000, "minimum": 1, "optional": true}
    :param conn_rate_limit_no_logging: {"default": 0, "optional": true, "type": "number", "description": "Do not log connection over limit event", "format": "flag"}
    :param name: {"description": "Virtual server template name", "format": "string", "default": "default", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param conn_limit_reset: {"default": 0, "optional": true, "type": "number", "description": "Send client reset when connection over limit", "format": "flag"}
    :param conn_rate_limit_reset: {"default": 0, "optional": true, "type": "number", "description": "Send client reset when connection rate over limit", "format": "flag"}
    :param rate_interval: {"description": "'100ms': Use 100 ms as sampling interval; 'second': Use 1 second as sampling interval; ", "format": "enum", "default": "second", "type": "string", "enum": ["100ms", "second"], "optional": true}
    :param icmpv6_rate_limit: {"description": "ICMPv6 rate limit (Normal rate limit. If exceeds this limit, drop the ICMP packet that goes over the limit)", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": true}
    :param subnet_gratuitous_arp: {"default": 0, "optional": true, "type": "number", "description": "Send gratuitous ARP for every IP in the subnet virtual server", "format": "flag"}
    :param icmpv6_lockup: {"description": "Enter lockup state when ICMP rate exceeds lockup rate limit (Maximum rate limit. If exceeds this limit, drop all ICMP packet for a time period)", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": true}
    :param conn_rate_limit: {"description": "Connection rate limit", "format": "number", "type": "number", "maximum": 1048575, "minimum": 1, "optional": true}
    :param icmp_lockup_period: {"description": "Lockup period (second)", "format": "number", "type": "number", "maximum": 16383, "minimum": 1, "optional": true}
    :param icmpv6_lockup_period: {"description": "Lockup period (second)", "format": "number", "type": "number", "maximum": 16383, "minimum": 1, "optional": true}
    :param conn_limit_no_logging: {"default": 0, "optional": true, "type": "number", "description": "Do not log connection over limit event", "format": "flag"}
    :param icmp_rate_limit: {"description": "ICMP rate limit (Normal rate limit. If exceeds this limit, drop the ICMP packet that goes over the limit)", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": true}
    :param icmp_lockup: {"description": "Enter lockup state when ICMP rate exceeds lockup rate limit (Maximum rate limit. If exceeds this limit, drop all ICMP packet for a time period)", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/template/virtual-server/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "virtual-server"
        self.a10_url="/axapi/v3/slb/template/virtual-server/{name}"
        self.DeviceProxy = ""
        self.conn_limit = ""
        self.conn_rate_limit_no_logging = ""
        self.name = ""
        self.conn_limit_reset = ""
        self.conn_rate_limit_reset = ""
        self.rate_interval = ""
        self.icmpv6_rate_limit = ""
        self.subnet_gratuitous_arp = ""
        self.icmpv6_lockup = ""
        self.conn_rate_limit = ""
        self.icmp_lockup_period = ""
        self.icmpv6_lockup_period = ""
        self.conn_limit_no_logging = ""
        self.icmp_rate_limit = ""
        self.icmp_lockup = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


