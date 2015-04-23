from a10sdk.common.A10BaseClass import A10BaseClass


class Template(A10BaseClass):
    
    """Class Description::
    NAT behavior templates.

    Class template supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param logging_list: {"minItems": 1, "items": {"type": "logging"}, "uniqueItems": true, "array": [{"required": ["name"], "properties": {"severity": {"type": "object", "properties": {"severity-string": {"description": "'emergency': 0: Emergency; 'alert': 1: Alert; 'critical': 2: Critical; 'error': 3: Error; 'warning': 4: Warning; 'notice': 5: Notice; 'informational': 6: Informational; 'debug': 7: Debug; ", "format": "enum", "default": "debug", "enum": ["emergency", "alert", "critical", "error", "warning", "notice", "informational", "debug"], "not": "severity-val", "type": "string"}, "severity-val": {"description": "Logging severity level", "format": "number", "default": 7, "maximum": 7, "minimum": 0, "not": "severity-string", "type": "number"}}}, "facility": {"description": "'kernel': 0: Kernel; 'user': 1: User-level; 'mail': 2: Mail; 'daemon': 3: System daemons; 'security-authorization': 4: Security/authorization; 'syslog': 5: Syslog internal; 'line-printer': 6: Line printer; 'news': 7: Network news; 'uucp': 8: UUCP subsystem; 'cron': 9: Time-related; 'security-authorization-private': 10: Private security/authorization; 'ftp': 11: FTP; 'ntp': 12: NTP; 'audit': 13: Audit; 'alert': 14: Alert; 'clock': 15: Clock-related; 'local0': 16: Local use 0; 'local1': 17: Local use 1; 'local2': 18: Local use 2; 'local3': 19: Local use 3; 'local4': 20: Local use 4; 'local5': 21: Local use 5; 'local6': 22: Local use 6; 'local7': 23: Local use 7; ", "format": "enum", "default": "local0", "type": "string", "enum": ["kernel", "user", "mail", "daemon", "security-authorization", "syslog", "line-printer", "news", "uucp", "cron", "security-authorization-private", "ftp", "ntp", "audit", "alert", "clock", "local0", "local1", "local2", "local3", "local4", "local5", "local6", "local7"], "optional": true}, "include-destination": {"default": 0, "optional": true, "type": "number", "description": "Include the destination IP and port in logs", "format": "flag"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "service-group": {"description": "Set NAT logging service-group", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/slb/service-group"}, "log": {"type": "object", "properties": {"port-mappings": {"enum": ["creation", "disable"], "type": "string", "description": "'creation': Log creation of NAT mappgins; 'disable': Disable Log creation and deletion of NAT mappings; ", "format": "enum"}}}, "source-port": {"type": "object", "properties": {"source-port-num": {"description": "Set source port for sending NAT syslogs (default: 514)", "format": "number", "default": 514, "maximum": 65535, "minimum": 1, "not": "any", "type": "number"}, "any": {"default": 0, "not": "source-port-num", "type": "number", "description": "Use any source port", "format": "flag"}}}, "include-rip-rport": {"default": 0, "optional": true, "type": "number", "description": "Include the IP and port of real server in logs", "format": "flag"}, "name": {"description": "NAT logging template name", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/ip/nat/template/logging/{name}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ip/nat/template`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "template"
        self.a10_url="/axapi/v3/ip/nat/template"
        self.DeviceProxy = ""
        self.logging_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


