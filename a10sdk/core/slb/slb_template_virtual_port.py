from a10sdk.common.A10BaseClass import A10BaseClass


class VirtualPort(A10BaseClass):
    
    """Class Description::
    Virtual port template.

    Class virtual-port supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param aflow: {"default": 0, "optional": true, "type": "number", "description": "Use aFlow to eliminate the traffic surge", "format": "flag"}
    :param conn_limit: {"description": "Connection limit", "format": "number", "type": "number", "maximum": 8000000, "minimum": 1, "optional": true}
    :param conn_rate_limit_no_logging: {"default": 0, "optional": true, "type": "number", "description": "Do not log connection over limit event", "format": "flag"}
    :param drop_unknown_conn: {"default": 0, "optional": true, "type": "number", "description": "Drop conection if receives TCP packet without SYN or RST flag and it does not belong to any existing connections", "format": "flag"}
    :param name: {"description": "Virtual port template name", "format": "string-rlx", "default": "default", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param allow_vip_to_rport_mapping: {"default": 0, "optional": true, "type": "number", "description": "Allow mapping of VIP to real port", "format": "flag"}
    :param conn_limit_reset: {"default": 0, "optional": true, "type": "number", "description": "Send client reset when connection over limit", "format": "flag"}
    :param conn_rate_limit_reset: {"default": 0, "optional": true, "type": "number", "description": "Send client reset when connection rate over limit", "format": "flag"}
    :param rate_interval: {"description": "'100ms': Use 100 ms as sampling interval; 'second': Use 1 second as sampling interval; ", "format": "enum", "default": "second", "type": "string", "enum": ["100ms", "second"], "optional": true}
    :param dscp: {"description": "Differentiated Services Code Point (DSCP to Real Server IP Mapping Value)", "format": "number", "type": "number", "maximum": 63, "minimum": 1, "optional": true}
    :param ignore_tcp_msl: {"default": 0, "optional": true, "type": "number", "description": "reclaim TCP resource immediately without MSL", "format": "flag"}
    :param snat_port_preserve: {"default": 0, "optional": true, "type": "number", "description": "Source NAT Port Preservation", "format": "flag"}
    :param conn_rate_limit: {"description": "Connection rate limit", "format": "number", "type": "number", "maximum": 1048575, "minimum": 1, "optional": true}
    :param reset_l7_on_failover: {"default": 0, "optional": true, "type": "number", "description": "Send reset to L7 client and server connection upon a failover", "format": "flag"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param conn_limit_no_logging: {"default": 0, "optional": true, "type": "number", "description": "Do not log connection over limit event", "format": "flag"}
    :param snat_msl: {"description": "Source NAT MSL (Source NAT MSL value)", "format": "number", "type": "number", "maximum": 1800, "minimum": 1, "optional": true}
    :param allow_syn_otherflags: {"default": 0, "optional": true, "type": "number", "description": "Allow initial SYN packet with other flags", "format": "flag"}
    :param reset_unknown_conn: {"default": 0, "optional": true, "type": "number", "description": "Send reset back if receives TCP packet without SYN or RST flag and it does not belong to any existing connections", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/template/virtual-port/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "virtual-port"
        self.a10_url="/axapi/v3/slb/template/virtual-port/{name}"
        self.DeviceProxy = ""
        self.aflow = ""
        self.conn_limit = ""
        self.conn_rate_limit_no_logging = ""
        self.drop_unknown_conn = ""
        self.name = ""
        self.allow_vip_to_rport_mapping = ""
        self.conn_limit_reset = ""
        self.conn_rate_limit_reset = ""
        self.rate_interval = ""
        self.dscp = ""
        self.ignore_tcp_msl = ""
        self.snat_port_preserve = ""
        self.conn_rate_limit = ""
        self.reset_l7_on_failover = ""
        self.uuid = ""
        self.conn_limit_no_logging = ""
        self.snat_msl = ""
        self.allow_syn_otherflags = ""
        self.reset_unknown_conn = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


