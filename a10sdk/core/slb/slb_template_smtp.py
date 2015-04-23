from a10sdk.common.A10BaseClass import A10BaseClass


class ClientDomainSwitching(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param service_group: {"description": "Select service group (Service group name)", "format": "string-rlx", "minLength": 1, "maxLength": 127, "type": "string", "$ref": "/axapi/v3/slb/service-group"}
    :param match_string: {"minLength": 1, "maxLength": 31, "type": "string", "description": "Domain name string", "format": "string-rlx"}
    :param switching_type: {"enum": ["contains", "ends-with", "starts-with"], "type": "string", "description": "'contains': Specify domain name string if domain contains another string; 'ends-with': Specify domain name string if domain ends with another string; 'starts-with': Specify domain string if domain starts with another string; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "client-domain-switching"
        self.DeviceProxy = ""
        self.service_group = ""
        self.match_string = ""
        self.switching_type = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class CommandDisable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param disable_type: {"enum": ["expn", "turn", "vrfy"], "type": "string", "description": "'expn': Disable SMTP EXPN commands; 'turn': Disable SMTP TURN commands; 'vrfy': Disable SMTP VRFY commands; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "command-disable"
        self.DeviceProxy = ""
        self.disable_type = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Smtp(A10BaseClass):
    
    """Class Description::
    SMTP.

    Class smtp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param name: {"description": "SMTP Template Name", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param starttls: {"description": "'disabled': Disable STARTTLS; 'optional': STARTTLS is optional requirement; 'enforced': Must issue STARTTLS command before mail transaction; ", "format": "enum", "default": "disabled", "type": "string", "enum": ["disabled", "optional", "enforced"], "optional": true}
    :param server_domain: {"description": "Config the domain of the email servers (Server's domain, default is \"mail-server-domain\")", "format": "string-rlx", "default": "mail-server-domain", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}
    :param client_domain_switching: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"service-group": {"description": "Select service group (Service group name)", "format": "string-rlx", "minLength": 1, "maxLength": 127, "type": "string", "$ref": "/axapi/v3/slb/service-group"}, "match-string": {"minLength": 1, "maxLength": 31, "type": "string", "description": "Domain name string", "format": "string-rlx"}, "optional": true, "switching-type": {"enum": ["contains", "ends-with", "starts-with"], "type": "string", "description": "'contains': Specify domain name string if domain contains another string; 'ends-with': Specify domain name string if domain ends with another string; 'starts-with': Specify domain string if domain starts with another string; ", "format": "enum"}}}]}
    :param command_disable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "disable-type": {"enum": ["expn", "turn", "vrfy"], "type": "string", "description": "'expn': Disable SMTP EXPN commands; 'turn': Disable SMTP TURN commands; 'vrfy': Disable SMTP VRFY commands; ", "format": "enum"}}}]}
    :param service_ready_msg: {"description": "Set SMTP service ready message (SMTP service ready message, default is \"ESMTP mail service ready\")", "format": "string-rlx", "default": "ESMTP mail service ready", "minLength": 1, "optional": true, "maxLength": 127, "type": "string"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/template/smtp/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "smtp"
        self.a10_url="/axapi/v3/slb/template/smtp/{name}"
        self.DeviceProxy = ""
        self.name = ""
        self.starttls = ""
        self.server_domain = ""
        self.client_domain_switching = []
        self.command_disable = []
        self.service_ready_msg = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


