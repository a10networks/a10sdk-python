from a10sdk.common.A10BaseClass import A10BaseClass


class Geofiles(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param success: {"type": "number", "format": "number"}
    :param error_warning: {"type": "number", "format": "number"}
    :param lines: {"type": "number", "format": "number"}
    :param filename: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param template: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param percentage_loaded: {"type": "number", "format": "number"}
    :param type: {"enum": ["template", "builtin"], "type": "string", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "geofiles"
        self.DeviceProxy = ""
        self.success = ""
        self.error_warning = ""
        self.lines = ""
        self.filename = ""
        self.template = ""
        self.percentage_loaded = ""
        self.A10WW_type = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param geofiles: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"success": {"type": "number", "format": "number"}, "error-warning": {"type": "number", "format": "number"}, "lines": {"type": "number", "format": "number"}, "filename": {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}, "optional": true, "template": {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}, "percentage-loaded": {"type": "number", "format": "number"}, "type": {"enum": ["template", "builtin"], "type": "string", "format": "enum"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.geofiles = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class GeolocationFile(A10BaseClass):
    
    """Class Description::
    Operational Status for the object geolocation-file.

    Class geolocation-file supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/geolocation-file/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "geolocation-file"
        self.a10_url="/axapi/v3/gslb/geolocation-file/oper"
        self.DeviceProxy = ""
        self.oper = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


