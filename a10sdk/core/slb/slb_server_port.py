from a10sdk.common.A10BaseClass import A10BaseClass


class AlternatePort(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param alternate_name: {"minLength": 1, "maxLength": 127, "type": "string", "description": "Alternate Name", "format": "string-rlx"}
    :param alternate_server_port: {"description": "Port (Alternate Server Port Value)", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}
    :param alternate: {"description": "Alternate Server Number", "minimum": 1, "type": "number", "maximum": 16, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "alternate-port"
        self.DeviceProxy = ""
        self.alternate_name = ""
        self.alternate_server_port = ""
        self.alternate = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class AuthCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param service_principal_name: {"minLength": 1, "maxLength": 128, "type": "string", "description": "Service Principal Name (Kerberos principal name)", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "auth-cfg"
        self.DeviceProxy = ""
        self.service_principal_name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Port(A10BaseClass):
    
    """Class Description::
    Real Server Port.

    Class port supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param conn_limit: {"description": "Connection Limit", "format": "number", "default": 8000000, "optional": true, "maximum": 8000000, "minimum": 1, "type": "number"}
    :param health_check_disable: {"description": "Disable health check", "format": "flag", "default": 0, "optional": true, "not-list": ["health-check", "health-check-follow-port"], "type": "number"}
    :param extended_stats: {"default": 0, "optional": true, "type": "number", "description": "Enable extended statistics on real server port", "format": "flag"}
    :param template_server_ssl: {"description": "Server side SSL template (Server side SSL Name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/slb/template/server-ssl"}
    :param weight: {"description": "Port Weight (Connection Weight)", "format": "number", "default": 1, "optional": true, "maximum": 100, "minimum": 1, "type": "number"}
    :param conn_resume: {"description": "Connection Resume", "format": "number", "type": "number", "maximum": 1000000, "minimum": 1, "optional": true}
    :param alternate_port: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"alternate-name": {"minLength": 1, "maxLength": 127, "type": "string", "description": "Alternate Name", "format": "string-rlx"}, "alternate-server-port": {"description": "Port (Alternate Server Port Value)", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}, "alternate": {"description": "Alternate Server Number", "minimum": 1, "type": "number", "maximum": 16, "format": "number"}, "optional": true}}]}
    :param no_logging: {"default": 0, "optional": true, "type": "number", "description": "Do not log connection over limit event", "format": "flag"}
    :param stats_data_action: {"description": "'stats-data-enable': Enable statistical data collection for real server port; 'stats-data-disable': Disable statistical data collection for real server port; ", "format": "enum", "default": "stats-data-enable", "type": "string", "enum": ["stats-data-enable", "stats-data-disable"], "optional": true}
    :param follow_port_protocol: {"optional": true, "enum": ["tcp", "udp"], "type": "string", "description": "'tcp': TCP Port; 'udp': UDP Port; ", "format": "enum"}
    :param port_number: {"description": "Port Number", "format": "number", "type": "number", "maximum": 65534, "minimum": 0, "optional": false}
    :param range: {"description": "Port range (Port range value - used for vip-to-rport-mapping)", "format": "number", "default": 0, "optional": true, "maximum": 254, "minimum": 0, "type": "number"}
    :param no_ssl: {"default": 0, "optional": true, "type": "number", "description": "No SSL", "format": "flag"}
    :param action: {"description": "'enable': enable; 'disable': disable; ", "format": "enum", "default": "enable", "type": "string", "enum": ["enable", "disable"], "optional": true}
    :param protocol: {"optional": false, "enum": ["tcp", "udp"], "type": "string", "description": "'tcp': TCP Port; 'udp': UDP Port; ", "format": "enum"}
    :param health_check_follow_port: {"description": "Specify which port to follow for health status (Port Number)", "format": "number", "optional": true, "not-list": ["health-check", "health-check-disable"], "maximum": 65534, "minimum": 1, "type": "number"}
    :param health_check: {"description": "Health Check (Monitor Name)", "format": "string", "minLength": 1, "not-list": ["health-check-follow-port", "health-check-disable"], "optional": true, "maxLength": 31, "type": "string", "$ref": "/axapi/v3/health/monitor"}
    :param template_port: {"description": "Port template (Port template name)", "format": "string", "default": "default", "minLength": 1, "optional": true, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/slb/template/port"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/server/{name}/port/{port_number}+{protocol}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "port_number","protocol"]

        self.b_key = "port"
        self.a10_url="/axapi/v3/slb/server/{name}/port/{port_number}+{protocol}"
        self.DeviceProxy = ""
        self.conn_limit = ""
        self.health_check_disable = ""
        self.extended_stats = ""
        self.template_server_ssl = ""
        self.weight = ""
        self.conn_resume = ""
        self.alternate_port = []
        self.no_logging = ""
        self.stats_data_action = ""
        self.follow_port_protocol = ""
        self.port_number = ""
        self.A10WW_range = ""
        self.no_ssl = ""
        self.auth_cfg = {}
        self.action = ""
        self.protocol = ""
        self.health_check_follow_port = ""
        self.health_check = ""
        self.template_port = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


