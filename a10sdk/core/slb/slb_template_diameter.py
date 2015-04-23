from a10sdk.common.A10BaseClass import A10BaseClass


class AvpList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param int32: {"description": "32 bits integer", "format": "number", "not-list": ["int64", "string"], "maximum": 2147483647, "minimum": 0, "type": "number"}
    :param mandatory: {"default": 0, "type": "number", "description": "mandatory avp", "format": "flag"}
    :param string: {"description": "String (string name, max length 127 bytes)", "format": "string", "minLength": 1, "not-list": ["int32", "int64"], "maxLength": 128, "type": "string"}
    :param avp: {"description": "customize avps for cer to the server (avp number)", "minimum": 0, "type": "number", "maximum": 2147483647, "format": "number"}
    :param int64: {"description": "64 bits integer", "format": "number", "not-list": ["int32", "string"], "maximum": 2147483647, "minimum": 0, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "avp-list"
        self.DeviceProxy = ""
        self.int32 = ""
        self.mandatory = ""
        self.string = ""
        self.avp = ""
        self.int64 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class MessageCodeList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param message_code: {"minimum": 1, "type": "number", "maximum": 2147483647, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "message-code-list"
        self.DeviceProxy = ""
        self.message_code = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Diameter(A10BaseClass):
    
    """Class Description::
    diameter template.

    Class diameter supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param avp_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"int32": {"description": "32 bits integer", "format": "number", "not-list": ["int64", "string"], "maximum": 2147483647, "minimum": 0, "type": "number"}, "mandatory": {"default": 0, "type": "number", "description": "mandatory avp", "format": "flag"}, "string": {"description": "String (string name, max length 127 bytes)", "format": "string", "minLength": 1, "not-list": ["int32", "int64"], "maxLength": 128, "type": "string"}, "avp": {"description": "customize avps for cer to the server (avp number)", "minimum": 0, "type": "number", "maximum": 2147483647, "format": "number"}, "int64": {"description": "64 bits integer", "format": "number", "not-list": ["int32", "string"], "maximum": 2147483647, "minimum": 0, "type": "number"}, "optional": true}}]}
    :param service_group_name: {"description": "service group name, this is the service group that the message needs to be copied to", "format": "string", "minLength": 1, "optional": true, "maxLength": 127, "type": "string", "$ref": "/axapi/v3/slb/service-group"}
    :param name: {"description": "diameter template Name", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param dwr_time: {"description": "dwr health-check timer interval (in 100 milli second unit, default is 100, 0 means unset this option)", "format": "number", "default": 0, "optional": true, "maximum": 2147483647, "minimum": 0, "type": "number"}
    :param avp_string: {"description": "pattern to be matched in the avp string name, max length 127 bytes", "format": "string", "minLength": 1, "optional": true, "maxLength": 128, "type": "string"}
    :param idle_timeout: {"description": " user sesison idle timeout (in minutes, default is 5)", "format": "number", "default": 5, "optional": true, "maximum": 65535, "minimum": 1, "type": "number"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param avp_code: {"description": "avp code", "format": "number", "type": "number", "maximum": 2147483647, "minimum": 1, "optional": true}
    :param message_code_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "message-code": {"minimum": 1, "type": "number", "maximum": 2147483647, "format": "number"}}}]}
    :param origin_realm: {"description": "origin-realm name avp", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}
    :param origin_host: {"description": "origin-host name avp", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}
    :param customize_cea: {"default": 0, "optional": true, "type": "number", "description": "customizing cea response", "format": "flag"}
    :param multiple_origin_host: {"default": 0, "optional": true, "type": "number", "description": "allowing multiple origin-host to a single server", "format": "flag"}
    :param product_name: {"description": "product name avp", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}
    :param session_age: {"description": "user session age allowed (default 10), this is not idle-time (in minutes)", "format": "number", "default": 10, "optional": true, "maximum": 65535, "minimum": 1, "type": "number"}
    :param vendor_id: {"description": "vendor-id avp (Vendon Id)", "format": "number", "type": "number", "maximum": 2147483647, "minimum": 0, "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/template/diameter/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "diameter"
        self.a10_url="/axapi/v3/slb/template/diameter/{name}"
        self.DeviceProxy = ""
        self.avp_list = []
        self.service_group_name = ""
        self.name = ""
        self.dwr_time = ""
        self.avp_string = ""
        self.idle_timeout = ""
        self.uuid = ""
        self.avp_code = ""
        self.message_code_list = []
        self.origin_realm = ""
        self.origin_host = ""
        self.customize_cea = ""
        self.multiple_origin_host = ""
        self.product_name = ""
        self.session_age = ""
        self.vendor_id = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


