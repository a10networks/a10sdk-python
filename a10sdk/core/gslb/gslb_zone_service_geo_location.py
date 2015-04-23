from a10sdk.common.A10BaseClass import A10BaseClass


class Alias(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param alias: {"minLength": 1, "maxLength": 127, "type": "string", "description": "Send CNAME response for this geo-location (Specify a CNAME record)", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "alias"
        self.DeviceProxy = ""
        self.alias = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class GeoLocation(A10BaseClass):
    
    """Class Description::
    Geo location settings.

    Class geo-location supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param forward_type: {"optional": true, "enum": ["both", "query", "response"], "type": "string", "description": "'both': Forward both query and response; 'query': Forward query from this geo-location; 'response': Forward response to this geo-location; ", "format": "enum"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param alias: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"alias": {"minLength": 1, "maxLength": 127, "type": "string", "description": "Send CNAME response for this geo-location (Specify a CNAME record)", "format": "string"}, "optional": true}}]}
    :param action_type: {"optional": true, "enum": ["allow", "drop", "forward", "ignore", "reject"], "type": "string", "description": "'allow': Allow query from this geo-location; 'drop': Drop query from this geo-location; 'forward': Forward packet for this geo-location; 'ignore': Send empty response to this geo-location; 'reject': Send refuse response to this geo-location; ", "format": "enum"}
    :param policy: {"description": "Policy for this geo-location (Specify the policy name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "not": "action", "type": "string"}
    :param action: {"description": "Action for this geo-location", "format": "flag", "default": 0, "optional": true, "not": "policy", "type": "number"}
    :param geo_name: {"description": "Specify the geo-location", "format": "string", "minLength": 1, "optional": false, "maxLength": 127, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/zone/{name}/service/{service_port}+{service_name}/geo-location/{geo_name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "geo_name"]

        self.b_key = "geo-location"
        self.a10_url="/axapi/v3/gslb/zone/{name}/service/{service_port}+{service_name}/geo-location/{geo_name}"
        self.DeviceProxy = ""
        self.forward_type = ""
        self.uuid = ""
        self.alias = []
        self.action_type = ""
        self.policy = ""
        self.action = ""
        self.geo_name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


