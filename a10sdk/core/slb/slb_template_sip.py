from a10sdk.common.A10BaseClass import A10BaseClass


class ServerRequestHeader(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param server_request_header_insert: {"minLength": 1, "maxLength": 127, "type": "string", "description": "Insert a SIP header (Header Content (Format: \"name: value\"))", "format": "string-rlx"}
    :param server_request_erase_all: {"default": 0, "type": "number", "description": "Erase all headers", "format": "flag"}
    :param insert_condition_server_request: {"enum": ["insert-if-not-exist", "insert-always"], "type": "string", "description": "'insert-if-not-exist': Only insert the header when it does not exist; 'insert-always': Always insert the header even when there is a header with the same name; ", "format": "enum"}
    :param server_request_header_erase: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Erase a SIP header (Header Name)", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "server-request-header"
        self.DeviceProxy = ""
        self.server_request_header_insert = ""
        self.server_request_erase_all = ""
        self.insert_condition_server_request = ""
        self.server_request_header_erase = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class ServerResponseHeader(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param server_response_header_insert: {"minLength": 1, "maxLength": 127, "type": "string", "description": "Insert a SIP header (Header Content (Format: \"name: value\"))", "format": "string-rlx"}
    :param server_response_header_erase: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Erase a SIP header (Header Name)", "format": "string-rlx"}
    :param server_response_erase_all: {"default": 0, "type": "number", "description": "Erase all headers", "format": "flag"}
    :param insert_condition_server_response: {"enum": ["insert-if-not-exist", "insert-always"], "type": "string", "description": "'insert-if-not-exist': Only insert the header when it does not exist; 'insert-always': Always insert the header even when there is a header with the same name; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "server-response-header"
        self.DeviceProxy = ""
        self.server_response_header_insert = ""
        self.server_response_header_erase = ""
        self.server_response_erase_all = ""
        self.insert_condition_server_response = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class ClientRequestHeader(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param client_request_header_erase: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Erase a SIP header (Header Name)", "format": "string-rlx"}
    :param client_request_header_insert: {"minLength": 1, "maxLength": 127, "type": "string", "description": "Insert a SIP header (Header Content (Format: \"name: value\"))", "format": "string-rlx"}
    :param client_request_erase_all: {"default": 0, "type": "number", "description": "Erase all headers", "format": "flag"}
    :param insert_condition_client_request: {"enum": ["insert-if-not-exist", "insert-always"], "type": "string", "description": "'insert-if-not-exist': Only insert the header when it does not exist; 'insert-always': Always insert the header even when there is a header with the same name; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "client-request-header"
        self.DeviceProxy = ""
        self.client_request_header_erase = ""
        self.client_request_header_insert = ""
        self.client_request_erase_all = ""
        self.insert_condition_client_request = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class ClientResponseHeader(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param client_response_erase_all: {"default": 0, "type": "number", "description": "Erase all headers", "format": "flag"}
    :param insert_condition_client_response: {"enum": ["insert-if-not-exist", "insert-always"], "type": "string", "description": "'insert-if-not-exist': Only insert the header when it does not exist; 'insert-always': Always insert the header even when there is a header with the same name; ", "format": "enum"}
    :param client_response_header_insert: {"minLength": 1, "maxLength": 127, "type": "string", "description": "Insert a SIP header (Header Content (Format: \"name: value\"))", "format": "string-rlx"}
    :param client_response_header_erase: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Erase a SIP header (Header Name)", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "client-response-header"
        self.DeviceProxy = ""
        self.client_response_erase_all = ""
        self.insert_condition_client_response = ""
        self.client_response_header_insert = ""
        self.client_response_header_erase = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class ExcludeTranslation(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param translation_value: {"enum": ["start-line", "header", "body"], "type": "string", "description": "'start-line': SIP request line or status line; 'header': SIP message headers; 'body': SIP message body; ", "format": "enum"}
    :param header_string: {"minLength": 1, "maxLength": 63, "type": "string", "description": "SIP header name", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "exclude-translation"
        self.DeviceProxy = ""
        self.translation_value = ""
        self.header_string = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Sip(A10BaseClass):
    
    """Class Description::
    SIP Template.

    Class sip supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param server_request_header: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"server-request-header-insert": {"minLength": 1, "maxLength": 127, "type": "string", "description": "Insert a SIP header (Header Content (Format: \"name: value\"))", "format": "string-rlx"}, "server-request-erase-all": {"default": 0, "type": "number", "description": "Erase all headers", "format": "flag"}, "optional": true, "insert-condition-server-request": {"enum": ["insert-if-not-exist", "insert-always"], "type": "string", "description": "'insert-if-not-exist': Only insert the header when it does not exist; 'insert-always': Always insert the header even when there is a header with the same name; ", "format": "enum"}, "server-request-header-erase": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Erase a SIP header (Header Name)", "format": "string-rlx"}}}]}
    :param keep_server_ip_if_match_acl: {"default": 0, "optional": true, "type": "number", "description": "Use Real Server IP for addresses matching the ACL for a Call-Id", "format": "flag"}
    :param client_keep_alive: {"default": 0, "optional": true, "type": "number", "description": "Respond client keep-alive packet directly instead of forwarding to server", "format": "flag"}
    :param alg_source_nat: {"default": 0, "optional": true, "type": "number", "description": "Translate source IP to NAT IP in SIP message when source NAT is used", "format": "flag"}
    :param server_response_header: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"server-response-header-insert": {"minLength": 1, "maxLength": 127, "type": "string", "description": "Insert a SIP header (Header Content (Format: \"name: value\"))", "format": "string-rlx"}, "server-response-header-erase": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Erase a SIP header (Header Name)", "format": "string-rlx"}, "optional": true, "server-response-erase-all": {"default": 0, "type": "number", "description": "Erase all headers", "format": "flag"}, "insert-condition-server-response": {"enum": ["insert-if-not-exist", "insert-always"], "type": "string", "description": "'insert-if-not-exist': Only insert the header when it does not exist; 'insert-always': Always insert the header even when there is a header with the same name; ", "format": "enum"}}}]}
    :param server_selection_per_request: {"default": 0, "optional": true, "type": "number", "description": "Force server selection on every SIP request", "format": "flag"}
    :param client_request_header: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"client-request-header-erase": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Erase a SIP header (Header Name)", "format": "string-rlx"}, "optional": true, "client-request-header-insert": {"minLength": 1, "maxLength": 127, "type": "string", "description": "Insert a SIP header (Header Content (Format: \"name: value\"))", "format": "string-rlx"}, "client-request-erase-all": {"default": 0, "type": "number", "description": "Erase all headers", "format": "flag"}, "insert-condition-client-request": {"enum": ["insert-if-not-exist", "insert-always"], "type": "string", "description": "'insert-if-not-exist': Only insert the header when it does not exist; 'insert-always': Always insert the header even when there is a header with the same name; ", "format": "enum"}}}]}
    :param service_group: {"description": "service group name", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 127, "type": "string", "$ref": "/axapi/v3/slb/service-group"}
    :param insert_client_ip: {"default": 0, "optional": true, "type": "number", "description": "Insert Client IP address into SIP header", "format": "flag"}
    :param failed_client_selection: {"default": 0, "optional": true, "type": "number", "description": "Define action when select client fail", "format": "flag"}
    :param failed_client_selection_message: {"description": "Send SIP message (includs status code) to server when select client fail(Format: 3 digits(1XX~6XX) space reason)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "not": "drop-when-client-fail", "type": "string"}
    :param call_id_persist_disable: {"default": 0, "optional": true, "type": "number", "description": "Disable call-ID persistence", "format": "flag"}
    :param acl_id: {"description": "ACL id", "format": "number", "optional": true, "maximum": 199, "minimum": 100, "not": "acl-name-value", "type": "number", "$ref": "/axapi/v3/access-list/standard"}
    :param alg_dest_nat: {"default": 0, "optional": true, "type": "number", "description": "Translate VIP to real server IP in SIP message when destination NAT is used", "format": "flag"}
    :param server_keep_alive: {"default": 0, "optional": true, "type": "number", "description": "Send server keep-alive packet for every persist connection when enable conn-reuse", "format": "flag"}
    :param client_response_header: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"client-response-erase-all": {"default": 0, "type": "number", "description": "Erase all headers", "format": "flag"}, "insert-condition-client-response": {"enum": ["insert-if-not-exist", "insert-always"], "type": "string", "description": "'insert-if-not-exist': Only insert the header when it does not exist; 'insert-always': Always insert the header even when there is a header with the same name; ", "format": "enum"}, "optional": true, "client-response-header-insert": {"minLength": 1, "maxLength": 127, "type": "string", "description": "Insert a SIP header (Header Content (Format: \"name: value\"))", "format": "string-rlx"}, "client-response-header-erase": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Erase a SIP header (Header Name)", "format": "string-rlx"}}}]}
    :param failed_server_selection_message: {"description": "Send SIP message (includs status code) to client when select server fail(Format: 3 digits(1XX~6XX) space reason)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "not": "drop-when-server-fail", "type": "string"}
    :param name: {"description": "SIP Template Name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param exclude_translation: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"translation-value": {"enum": ["start-line", "header", "body"], "type": "string", "description": "'start-line': SIP request line or status line; 'header': SIP message headers; 'body': SIP message body; ", "format": "enum"}, "optional": true, "header-string": {"minLength": 1, "maxLength": 63, "type": "string", "description": "SIP header name", "format": "string-rlx"}}}]}
    :param interval: {"description": "The interval of keep-alive packet for each persist connection (second)", "format": "number", "default": 30, "optional": true, "maximum": 300, "minimum": 5, "type": "number"}
    :param dialog_aware: {"default": 0, "optional": true, "type": "number", "description": "Permit system processes dialog session", "format": "flag"}
    :param failed_server_selection: {"default": 0, "optional": true, "type": "number", "description": "Define action when select server fail", "format": "flag"}
    :param drop_when_client_fail: {"description": "Drop current SIP message when select client fail", "format": "flag", "default": 0, "optional": true, "not": "failed-client-selection-message", "type": "number"}
    :param timeout: {"description": "Time in minutes", "format": "number", "default": 30, "optional": true, "maximum": 250, "minimum": 1, "type": "number"}
    :param drop_when_server_fail: {"description": "Drop current SIP message when select server fail", "format": "flag", "default": 0, "optional": true, "not": "failed-server-selection-message", "type": "number"}
    :param acl_name_value: {"description": "IPv4 Access List Name", "format": "string", "minLength": 1, "optional": true, "maxLength": 16, "not": "acl-id", "type": "string", "$ref": "/axapi/v3/ip/access-list"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/template/sip/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "sip"
        self.a10_url="/axapi/v3/slb/template/sip/{name}"
        self.DeviceProxy = ""
        self.server_request_header = []
        self.keep_server_ip_if_match_acl = ""
        self.client_keep_alive = ""
        self.alg_source_nat = ""
        self.server_response_header = []
        self.server_selection_per_request = ""
        self.client_request_header = []
        self.service_group = ""
        self.insert_client_ip = ""
        self.failed_client_selection = ""
        self.failed_client_selection_message = ""
        self.call_id_persist_disable = ""
        self.acl_id = ""
        self.alg_dest_nat = ""
        self.server_keep_alive = ""
        self.client_response_header = []
        self.failed_server_selection_message = ""
        self.name = ""
        self.exclude_translation = []
        self.interval = ""
        self.dialog_aware = ""
        self.failed_server_selection = ""
        self.drop_when_client_fail = ""
        self.timeout = ""
        self.drop_when_server_fail = ""
        self.acl_name_value = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


