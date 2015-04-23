from a10sdk.common.A10BaseClass import A10BaseClass


class GeolocRdtList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param rdt: {"type": "number", "format": "number"}
    :param site_name: {"type": "string", "format": "string"}
    :param gl_name: {"type": "string", "format": "string"}
    :param type: {"type": "string", "format": "string"}
    :param age: {"type": "number", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "geoloc-rdt-list"
        self.DeviceProxy = ""
        self.rdt = ""
        self.site_name = ""
        self.gl_name = ""
        self.A10WW_type = ""
        self.age = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param geoloc_rdt_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"rdt": {"type": "number", "format": "number"}, "optional": true, "site-name": {"type": "string", "format": "string"}, "gl-name": {"type": "string", "format": "string"}, "type": {"type": "string", "format": "string"}, "age": {"type": "number", "format": "number"}}}]}
    :param geo_name: {"type": "string", "format": "string"}
    :param site_name: {"type": "string", "format": "string"}
    :param active_status: {"type": "string", "format": "string"}
    :param total_rdt: {"type": "number", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.geoloc_rdt_list = []
        self.geo_name = ""
        self.site_name = ""
        self.active_status = ""
        self.total_rdt = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class GeolocRdt(A10BaseClass):
    
    """Class Description::
    Operational Status for the object geoloc-rdt.

    Class geoloc-rdt supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/geoloc-rdt/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "geoloc-rdt"
        self.a10_url="/axapi/v3/gslb/geoloc-rdt/oper"
        self.DeviceProxy = ""
        self.oper = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


