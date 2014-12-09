from a10sdk.common.A10BaseClass import A10BaseClass


class BypassIpCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param bypass_ip: {"type": "string", "description": "ip address to bypass external service", "format": "ipv4-address"}
    :param mask: {"type": "string", "description": "IP prefix mask", "format": "ipv4-netmask"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "bypass-ip-cfg"
        self.DeviceProxy = ""
        self.bypass_ip = ""
        self.mask = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class ExternalService(A10BaseClass):
    
    """Class Description::
    External service template.

    Class external-service supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param name: {"description": "External Service Template Name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param source_ip: {"description": "Source IP persistence template (Source IP persistence template name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/slb/template/persist/source-ip"}
    :param service_group: {"description": "Bind a Service Group to the template (Service Group Name)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 127, "type": "string", "$ref": "/axapi/v3/slb/service-group"}
    :param bypass_ip_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "bypass-ip": {"type": "string", "description": "ip address to bypass external service", "format": "ipv4-address"}, "mask": {"type": "string", "description": "IP prefix mask", "format": "ipv4-netmask"}}}]}
    :param failure_action: {"optional": true, "enum": ["continue", "drop", "reset"], "type": "string", "description": "'continue': Continue; 'drop': Drop; 'reset': Reset; ", "format": "enum"}
    :param timeout: {"description": "timeout value 1 - 200 in units of 200ms, default is 5 (default is 1000ms) (1 - 200 in units of 200ms, default is 5 (1000ms))", "format": "number", "default": 5, "optional": true, "maximum": 200, "minimum": 1, "type": "number"}
    :param tcp_proxy: {"description": "TCP proxy template (TCP proxy template name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/slb/template/tcp-proxy"}
    :param action: {"description": "'continue': Continue; 'drop': Drop; 'reset': Reset; ", "format": "enum", "default": "continue", "type": "string", "enum": ["continue", "drop", "reset"], "optional": true}
    :param type: {"description": "'skyfire-icap': Skyfire ICAP service; 'url-filter': URL filtering service; ", "format": "enum", "default": "url-filter", "type": "string", "enum": ["skyfire-icap", "url-filter"], "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/template/external-service/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "external-service"
        self.a10_url="/axapi/v3/slb/template/external-service/{name}"
        self.DeviceProxy = ""
        self.name = ""
        self.source_ip = ""
        self.service_group = ""
        self.bypass_ip_cfg = []
        self.failure_action = ""
        self.timeout = ""
        self.tcp_proxy = ""
        self.action = ""
        self.A10WW_type = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


