from a10sdk.common.A10BaseClass import A10BaseClass


class GeoLocationMatch(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param geo_location: {"minLength": 1, "maxLength": 128, "type": "string", "description": "Geolocation name", "format": "string"}
    :param geo_location_service_group: {"description": "Service Group to be used (Service Group Name)", "format": "string-rlx", "minLength": 1, "maxLength": 127, "type": "string", "$ref": "/axapi/v3/slb/service-group"}
    :param geo_location_template: {"enum": ["waf"], "type": "string", "description": "'waf': waf;  (WAF template to be used)", "format": "enum"}
    :param geo_location_template_name: {"description": "WAF template to be used (Template Name)", "format": "string-rlx", "minLength": 1, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/waf/template"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "geo-location-match"
        self.DeviceProxy = ""
        self.geo_location = ""
        self.geo_location_service_group = ""
        self.geo_location_template = ""
        self.geo_location_template_name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class HttpPolicyMatch(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param match_string: {"minLength": 1, "maxLength": 128, "type": "string", "description": "URL String", "format": "string-rlx"}
    :param template_name: {"description": "WAF template to be used (Template Name)", "format": "string-rlx", "minLength": 1, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/waf/template"}
    :param service_group: {"description": "Service Group to be used (Service Group Name)", "format": "string", "minLength": 1, "maxLength": 127, "type": "string", "$ref": "/axapi/v3/slb/service-group"}
    :param template: {"enum": ["waf"], "type": "string", "description": "'waf': waf;  (WAF template to be used)", "format": "enum"}
    :param type: {"enum": ["cookie", "host", "url"], "type": "string", "description": "'cookie': cookie value match; 'host': hostname match; 'url': URL match; ", "format": "enum"}
    :param match_type: {"enum": ["contains", "ends-with", "equals", "starts-with"], "type": "string", "description": "'contains': Select service group if URL string contains another string; 'ends-with': Select service group if URL string ends with another string; 'equals': Select service group if URL string equals another string; 'starts-with': Select service group if URL string starts with another string; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "http-policy-match"
        self.DeviceProxy = ""
        self.match_string = ""
        self.template_name = ""
        self.service_group = ""
        self.template = ""
        self.A10WW_type = ""
        self.match_type = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class HttpPolicy(A10BaseClass):
    
    """Class Description::
    http-policy template.

    Class http-policy supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param geo_location_match: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"geo-location": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Geolocation name", "format": "string"}, "geo-location-service-group": {"description": "Service Group to be used (Service Group Name)", "format": "string-rlx", "minLength": 1, "maxLength": 127, "type": "string", "$ref": "/axapi/v3/slb/service-group"}, "optional": true, "geo-location-template": {"enum": ["waf"], "type": "string", "description": "'waf': waf;  (WAF template to be used)", "format": "enum"}, "geo-location-template-name": {"description": "WAF template to be used (Template Name)", "format": "string-rlx", "minLength": 1, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/waf/template"}}}]}
    :param name: {"description": "http-policy template name", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param http_policy_match: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "match-string": {"minLength": 1, "maxLength": 128, "type": "string", "description": "URL String", "format": "string-rlx"}, "template-name": {"description": "WAF template to be used (Template Name)", "format": "string-rlx", "minLength": 1, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/waf/template"}, "service-group": {"description": "Service Group to be used (Service Group Name)", "format": "string", "minLength": 1, "maxLength": 127, "type": "string", "$ref": "/axapi/v3/slb/service-group"}, "template": {"enum": ["waf"], "type": "string", "description": "'waf': waf;  (WAF template to be used)", "format": "enum"}, "type": {"enum": ["cookie", "host", "url"], "type": "string", "description": "'cookie': cookie value match; 'host': hostname match; 'url': URL match; ", "format": "enum"}, "match-type": {"enum": ["contains", "ends-with", "equals", "starts-with"], "type": "string", "description": "'contains': Select service group if URL string contains another string; 'ends-with': Select service group if URL string ends with another string; 'equals': Select service group if URL string equals another string; 'starts-with': Select service group if URL string starts with another string; ", "format": "enum"}}}]}
    :param cookie_name: {"description": "name of cookie to match (Cookie Name)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/template/http-policy/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "http-policy"
        self.a10_url="/axapi/v3/slb/template/http-policy/{name}"
        self.DeviceProxy = ""
        self.geo_location_match = []
        self.name = ""
        self.http_policy_match = []
        self.cookie_name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


