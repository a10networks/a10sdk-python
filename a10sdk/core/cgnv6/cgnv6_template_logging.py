from a10sdk.common.A10BaseClass import A10BaseClass


class LogReceiver(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param encrypted: {"type": "encrypted", "description": "Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED secret string)", "format": "encrypted"}
    :param radius: {"default": 0, "type": "number", "description": "Use RADIUS server for NAT logging", "format": "flag"}
    :param secret_string: {"minLength": 1, "maxLength": 127, "type": "string", "description": "The RADIUS server's secret", "format": "password"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "log-receiver"
        self.DeviceProxy = ""
        self.encrypted = ""
        self.radius = ""
        self.secret_string = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Severity(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param severity_string: {"description": "'emergency': 0: Emergency; 'alert': 1: Alert; 'critical': 2: Critical; 'error': 3: Error; 'warning': 4: Warning; 'notice': 5: Notice; 'informational': 6: Informational; 'debug': 7: Debug; ", "format": "enum", "default": "debug", "enum": ["emergency", "alert", "critical", "error", "warning", "notice", "informational", "debug"], "not": "severity-val", "type": "string"}
    :param severity_val: {"description": "Logging severity level", "format": "number", "default": 7, "maximum": 7, "minimum": 0, "not": "severity-string", "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "severity"
        self.DeviceProxy = ""
        self.severity_string = ""
        self.severity_val = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class AttrCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param attr_event: {"enum": ["http-requests", "port-mappings", "sessions"], "type": "string", "description": "'http-requests': Include in HTTP request logs; 'port-mappings': Include in port-mapping logs; 'sessions': Include in session logs; ", "format": "enum"}
    :param attr: {"enum": ["imei", "imsi", "msisdn", "custom1", "custom2", "custom3"], "type": "string", "description": "'imei': Include IMEI; 'imsi': Include IMSI; 'msisdn': Include MSISDN; 'custom1': Customized attribute 1; 'custom2': Customized attribute 2; 'custom3': Customized attribute 3; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "attr-cfg"
        self.DeviceProxy = ""
        self.attr_event = ""
        self.attr = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class IncludeRadiusAttribute(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param attr_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"attr-event": {"enum": ["http-requests", "port-mappings", "sessions"], "type": "string", "description": "'http-requests': Include in HTTP request logs; 'port-mappings': Include in port-mapping logs; 'sessions': Include in session logs; ", "format": "enum"}, "optional": true, "attr": {"enum": ["imei", "imsi", "msisdn", "custom1", "custom2", "custom3"], "type": "string", "description": "'imei': Include IMEI; 'imsi': Include IMSI; 'msisdn': Include MSISDN; 'custom1': Customized attribute 1; 'custom2': Customized attribute 2; 'custom3': Customized attribute 3; ", "format": "enum"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "include-radius-attribute"
        self.DeviceProxy = ""
        self.attr_cfg = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class DestPort(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param include_byte_count: {"default": 0, "type": "number", "description": "Include the byte count of HTTP Request/Response in CGN session deletion logs", "format": "flag"}
    :param dest_port_number: {"minimum": 1, "type": "number", "maximum": 65535, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "dest-port"
        self.DeviceProxy = ""
        self.include_byte_count = ""
        self.dest_port_number = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class RuleHttpRequests(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param log_every_http_request: {"default": 0, "type": "number", "description": "Log every HTTP request in an HTTP 1.1 session (Default: Log the first HTTP request in a session)", "format": "flag"}
    :param dest_port: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"include-byte-count": {"default": 0, "type": "number", "description": "Include the byte count of HTTP Request/Response in CGN session deletion logs", "format": "flag"}, "optional": true, "dest-port-number": {"minimum": 1, "type": "number", "maximum": 65535, "format": "number"}}}]}
    :param max_url_len: {"description": "Max length of URL log (Max URL length (Default: 100 char))", "format": "number", "default": 100, "maximum": 1000, "minimum": 100, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "rule-http-requests"
        self.DeviceProxy = ""
        self.log_every_http_request = ""
        self.dest_port = []
        self.max_url_len = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Rule(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "rule"
        self.DeviceProxy = ""
        self.rule_http_requests = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class CustomMessage(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param custom_http_request_got: {"minLength": 1, "maxLength": 255, "type": "string", "description": "HTTP request got (Custom message string)", "format": "string-rlx"}
    :param custom_fixed_nat_allocated: {"minLength": 1, "maxLength": 255, "type": "string", "description": "Fixed-NAT allocated (Custom message string)", "format": "string-rlx"}
    :param custom_port_batch_freed: {"minLength": 1, "maxLength": 255, "type": "string", "description": "Port Batch freed (Custom message string)", "format": "string-rlx"}
    :param custom_fixed_nat_freed: {"minLength": 1, "maxLength": 255, "type": "string", "description": "Fixed-NAT freed (Custom message string)", "format": "string-rlx"}
    :param custom_port_batch_allocated: {"minLength": 1, "maxLength": 255, "type": "string", "description": "Port Batch allocated (Custom message string)", "format": "string-rlx"}
    :param custom_port_allocated: {"minLength": 1, "maxLength": 255, "type": "string", "description": "Port allocated (Custom message string)", "format": "string-rlx"}
    :param custom_session_deleted: {"minLength": 1, "maxLength": 255, "type": "string", "description": "Session deleted (Custom message string)", "format": "string-rlx"}
    :param custom_port_freed: {"minLength": 1, "maxLength": 255, "type": "string", "description": "Port freed (Custom message string)", "format": "string-rlx"}
    :param custom_session_created: {"minLength": 1, "maxLength": 255, "type": "string", "description": "Session created (Custom message string)", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "custom-message"
        self.DeviceProxy = ""
        self.custom_http_request_got = ""
        self.custom_fixed_nat_allocated = ""
        self.custom_port_batch_freed = ""
        self.custom_fixed_nat_freed = ""
        self.custom_port_batch_allocated = ""
        self.custom_port_allocated = ""
        self.custom_session_deleted = ""
        self.custom_port_freed = ""
        self.custom_session_created = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Custom(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param custom_header: {"enum": ["use-syslog-header"], "type": "string", "description": "'use-syslog-header': Use syslog header as custom log header; ", "format": "enum"}
    :param custom_time_stamp_format: {"minLength": 1, "maxLength": 31, "type": "string", "description": "Customize the time stamp format (Customize the time-stamp format. Default:%Y%m%d%H%M%S)", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "custom"
        self.DeviceProxy = ""
        self.custom_header = ""
        self.custom_message = {}
        self.custom_time_stamp_format = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Header(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param use_alternate_timestamp: {"default": 0, "type": "number", "description": "Use alternate non-RFC5424 compliant timestamp. Ex: 1990 Jan 15 12:30:30", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "header"
        self.DeviceProxy = ""
        self.use_alternate_timestamp = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Ipv6Tech(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param fixed_nat_freed: {"minLength": 1, "maxLength": 255, "type": "string", "description": "Fixed-NAT freed (Custom message string. Should be in the format of \"MSGID [STRUCTURED-DATA] MSG\")", "format": "string-rlx"}
    :param port_batch_freed: {"minLength": 1, "maxLength": 255, "type": "string", "description": "Port Batch freed (Custom message string. Should be in the format of \"MSGID [STRUCTURED-DATA] MSG\")", "format": "string-rlx"}
    :param tech_type: {"enum": ["lsn", "nat64", "ds-lite", "sixrd-nat64"], "type": "string", "description": "'lsn': LSN; 'nat64': NAT64; 'ds-lite': DS-Lite; 'sixrd-nat64': 6rd-NAT64; ", "format": "enum"}
    :param fixed_nat_allocated: {"minLength": 1, "maxLength": 255, "type": "string", "description": "Fixed-NAT allocated (Custom message string. Should be in the format of \"MSGID [STRUCTURED-DATA] MSG\")", "format": "string-rlx"}
    :param port_allocated: {"minLength": 1, "maxLength": 255, "type": "string", "description": "Port allocated (Custom message string. Should be in the format of \"MSGID [STRUCTURED-DATA] MSG\")", "format": "string-rlx"}
    :param port_freed: {"minLength": 1, "maxLength": 255, "type": "string", "description": "Port freed (Custom message string. Should be in the format of \"MSGID [STRUCTURED-DATA] MSG\")", "format": "string-rlx"}
    :param port_batch_allocated: {"minLength": 1, "maxLength": 255, "type": "string", "description": "Port Batch allocated (Custom message string. Should be in the format of \"MSGID [STRUCTURED-DATA] MSG\")", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ipv6-tech"
        self.DeviceProxy = ""
        self.fixed_nat_freed = ""
        self.port_batch_freed = ""
        self.tech_type = ""
        self.fixed_nat_allocated = ""
        self.port_allocated = ""
        self.port_freed = ""
        self.port_batch_allocated = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Message(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param session_created: {"minLength": 1, "maxLength": 255, "type": "string", "description": "Session created (Custom message string. Should be in the format of \"MSGID [STRUCTURED-DATA] MSG\")", "format": "string-rlx"}
    :param http_request_got: {"minLength": 1, "maxLength": 255, "type": "string", "description": "HTTP request got (Custom message string. Should be in the format of \"MSGID [STRUCTURED-DATA] MSG\")", "format": "string-rlx"}
    :param session_deleted: {"minLength": 1, "maxLength": 255, "type": "string", "description": "Session deleted (Custom message string. Should be in the format of \"MSGID [STRUCTURED-DATA] MSG\")", "format": "string-rlx"}
    :param ipv6_tech: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"fixed-nat-freed": {"minLength": 1, "maxLength": 255, "type": "string", "description": "Fixed-NAT freed (Custom message string. Should be in the format of \"MSGID [STRUCTURED-DATA] MSG\")", "format": "string-rlx"}, "port-batch-freed": {"minLength": 1, "maxLength": 255, "type": "string", "description": "Port Batch freed (Custom message string. Should be in the format of \"MSGID [STRUCTURED-DATA] MSG\")", "format": "string-rlx"}, "tech-type": {"enum": ["lsn", "nat64", "ds-lite", "sixrd-nat64"], "type": "string", "description": "'lsn': LSN; 'nat64': NAT64; 'ds-lite': DS-Lite; 'sixrd-nat64': 6rd-NAT64; ", "format": "enum"}, "fixed-nat-allocated": {"minLength": 1, "maxLength": 255, "type": "string", "description": "Fixed-NAT allocated (Custom message string. Should be in the format of \"MSGID [STRUCTURED-DATA] MSG\")", "format": "string-rlx"}, "port-allocated": {"minLength": 1, "maxLength": 255, "type": "string", "description": "Port allocated (Custom message string. Should be in the format of \"MSGID [STRUCTURED-DATA] MSG\")", "format": "string-rlx"}, "port-freed": {"minLength": 1, "maxLength": 255, "type": "string", "description": "Port freed (Custom message string. Should be in the format of \"MSGID [STRUCTURED-DATA] MSG\")", "format": "string-rlx"}, "optional": true, "port-batch-allocated": {"minLength": 1, "maxLength": 255, "type": "string", "description": "Port Batch allocated (Custom message string. Should be in the format of \"MSGID [STRUCTURED-DATA] MSG\")", "format": "string-rlx"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "message"
        self.DeviceProxy = ""
        self.session_created = ""
        self.http_request_got = ""
        self.session_deleted = ""
        self.ipv6_tech = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class RfcCustom(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "rfc-custom"
        self.DeviceProxy = ""
        self.header = {}
        self.message = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class HeaderCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param custom_max_length: {"description": "Max length for a HTTP request log (Max header length (Default: 100 char))", "format": "number", "default": 100, "maximum": 1000, "minimum": 100, "type": "number"}
    :param http_header: {"enum": ["cookie", "referer", "user-agent", "header1", "header2", "header3"], "type": "string", "description": "'cookie': Log HTTP Cookie Header; 'referer': Log HTTP Referer Header; 'user-agent': Log HTTP User-Agent Header; 'header1': Log HTTP Header 1; 'header2': Log HTTP Header 2; 'header3': Log HTTP Header 3; ", "format": "enum"}
    :param custom_header_name: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Header name", "format": "string"}
    :param max_length: {"description": "Max length for a HTTP request log (Max header length (Default: 100 char))", "format": "number", "default": 100, "maximum": 1000, "minimum": 100, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "header-cfg"
        self.DeviceProxy = ""
        self.custom_max_length = ""
        self.http_header = ""
        self.custom_header_name = ""
        self.max_length = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class IncludeHttp(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param header_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"custom-max-length": {"description": "Max length for a HTTP request log (Max header length (Default: 100 char))", "format": "number", "default": 100, "maximum": 1000, "minimum": 100, "type": "number"}, "http-header": {"enum": ["cookie", "referer", "user-agent", "header1", "header2", "header3"], "type": "string", "description": "'cookie': Log HTTP Cookie Header; 'referer': Log HTTP Referer Header; 'user-agent': Log HTTP User-Agent Header; 'header1': Log HTTP Header 1; 'header2': Log HTTP Header 2; 'header3': Log HTTP Header 3; ", "format": "enum"}, "optional": true, "custom-header-name": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Header name", "format": "string"}, "max-length": {"description": "Max length for a HTTP request log (Max header length (Default: 100 char))", "format": "number", "default": 100, "maximum": 1000, "minimum": 100, "type": "number"}}}]}
    :param request_number: {"default": 0, "type": "number", "description": "HTTP Request Number", "format": "flag"}
    :param method: {"default": 0, "type": "number", "description": "Log the HTTP Request Method", "format": "flag"}
    :param l4_session_info: {"default": 0, "type": "number", "description": "Log the L4 session information of the HTTP request", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "include-http"
        self.DeviceProxy = ""
        self.header_cfg = []
        self.request_number = ""
        self.method = ""
        self.l4_session_info = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class SourceAddress(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ip: {"type": "string", "description": "Specify source IP address", "format": "ipv4-address"}
    :param ipv6: {"type": "string", "description": "Specify source IPv6 address", "format": "ipv6-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "source-address"
        self.DeviceProxy = ""
        self.ip = ""
        self.ipv6 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class SourcePort(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param source_port_num: {"description": "Set source port for sending NAT syslogs (default: 514)", "format": "number", "default": 514, "maximum": 65535, "minimum": 1, "not": "any", "type": "number"}
    :param any: {"default": 0, "not": "source-port-num", "type": "number", "description": "Use any source port", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "source-port"
        self.DeviceProxy = ""
        self.source_port_num = ""
        self.A10WW_any = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class UserPorts(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param start_time: {"type": "string", "description": "Time when periodic logging starts (Specify start time(hh:mm))", "format": "time-hhmm"}
    :param user_ports: {"default": 0, "type": "number", "description": "Log Fixed NAT User Ports Configured", "format": "flag"}
    :param days: {"description": "Specify period in days", "minimum": 1, "type": "number", "maximum": 30, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "user-ports"
        self.DeviceProxy = ""
        self.start_time = ""
        self.user_ports = ""
        self.days = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class FixedNat(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param fixed_nat_http_requests: {"enum": ["host", "url"], "type": "string", "description": "'host': Log the HTTP Host Header; 'url': Log the HTTP Request URL; ", "format": "enum"}
    :param fixed_nat_sessions: {"default": 0, "type": "number", "description": "Log all Fixed NAT sessions", "format": "flag"}
    :param fixed_nat_port_mappings: {"enum": ["both", "creation"], "type": "string", "description": "'both': Log creation and deletion of NAT mappings; 'creation': Log creation of NAT mappings; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "fixed-nat"
        self.DeviceProxy = ""
        self.user_ports = {}
        self.fixed_nat_http_requests = ""
        self.fixed_nat_sessions = ""
        self.fixed_nat_port_mappings = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Log(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param port_mappings: {"enum": ["creation", "disable"], "type": "string", "description": "'creation': Log only creation of NAT mappgins; 'disable': Disable Log creation and deletion of NAT mappings; ", "format": "enum"}
    :param port_overloading: {"default": 0, "type": "number", "description": "Force logging of all port-overloading sessions", "format": "flag"}
    :param http_requests: {"enum": ["host", "url"], "type": "string", "description": "'host': Log the HTTP Host Header; 'url': Log the HTTP Request URL; ", "format": "enum"}
    :param sessions: {"default": 0, "type": "number", "description": "Log all data sessions created using NAT", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "log"
        self.DeviceProxy = ""
        self.port_mappings = ""
        self.port_overloading = ""
        self.fixed_nat = {}
        self.http_requests = ""
        self.sessions = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Logging(A10BaseClass):
    
    """Class Description::
    Logging Template.

    Class logging supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param include_partition_name: {"default": 0, "optional": true, "type": "number", "description": "Include partition name in logging events", "format": "flag"}
    :param batched_logging_disable: {"default": 0, "optional": true, "type": "number", "description": "Disable multiple logs per packet", "format": "flag"}
    :param name: {"description": "Logging template name", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param include_inside_user_mac: {"default": 0, "optional": true, "type": "number", "description": "Include the inside user MAC address in logs", "format": "flag"}
    :param facility: {"description": "'kernel': 0: Kernel; 'user': 1: User-level; 'mail': 2: Mail; 'daemon': 3: System daemons; 'security-authorization': 4: Security/authorization; 'syslog': 5: Syslog internal; 'line-printer': 6: Line printer; 'news': 7: Network news; 'uucp': 8: UUCP subsystem; 'cron': 9: Time-related; 'security-authorization-private': 10: Private security/authorization; 'ftp': 11: FTP; 'ntp': 12: NTP; 'audit': 13: Audit; 'alert': 14: Alert; 'clock': 15: Clock-related; 'local0': 16: Local use 0; 'local1': 17: Local use 1; 'local2': 18: Local use 2; 'local3': 19: Local use 3; 'local4': 20: Local use 4; 'local5': 21: Local use 5; 'local6': 22: Local use 6; 'local7': 23: Local use 7; ", "format": "enum", "default": "local0", "type": "string", "enum": ["kernel", "user", "mail", "daemon", "security-authorization", "syslog", "line-printer", "news", "uucp", "cron", "security-authorization-private", "ftp", "ntp", "audit", "alert", "clock", "local0", "local1", "local2", "local3", "local4", "local5", "local6", "local7"], "optional": true}
    :param include_destination: {"default": 0, "optional": true, "type": "number", "description": "Include the destination IP and port in logs", "format": "flag"}
    :param format: {"description": "'binary': Binary logging format; 'compact': Compact ASCII logging format (Hex format with compact representation); 'custom': Arbitrary custom logging format; 'default': Default A10 logging format (ASCII); 'rfc5424': RFC5424 compliant logging format; ", "format": "enum", "default": "default", "type": "string", "enum": ["binary", "compact", "custom", "default", "rfc5424"], "optional": true}
    :param service_group: {"description": "Set NAT logging service-group", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param shared: {"description": "Service group is in shared patition", "partition-visibility": "private", "default": 0, "type": "number", "format": "flag", "optional": true}
    :param resolution: {"description": "'seconds': Logging timestamp resolution in seconds (default); '10-milliseconds': Logging timestamp resolution in 10s of milli-seconds; ", "format": "enum", "default": "seconds", "type": "string", "enum": ["seconds", "10-milliseconds"], "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/template/logging/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "logging"
        self.a10_url="/axapi/v3/cgnv6/template/logging/{name}"
        self.DeviceProxy = ""
        self.include_partition_name = ""
        self.batched_logging_disable = ""
        self.log_receiver = {}
        self.name = ""
        self.include_inside_user_mac = ""
        self.facility = ""
        self.include_destination = ""
        self.severity = {}
        self.A10WW_format = ""
        self.include_radius_attribute = {}
        self.rule = {}
        self.custom = {}
        self.service_group = ""
        self.rfc_custom = {}
        self.include_http = {}
        self.source_address = {}
        self.shared = ""
        self.source_port = {}
        self.resolution = ""
        self.log = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


