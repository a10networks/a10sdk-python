from a10sdk.common.A10BaseClass import A10BaseClass


class GeolocList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param tomask: {"type": "string", "format": "string"}
    :param hits: {"type": "number", "format": "number"}
    :param from: {"type": "string", "format": "string"}
    :param subcnt: {"type": "number", "format": "number"}
    :param last: {"type": "string", "format": "string"}
    :param type: {"type": "string", "format": "string"}
    :param name: {"type": "string", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "geoloc-list"
        self.DeviceProxy = ""
        self.tomask = ""
        self.hits = ""
        self.A10WW_from = ""
        self.subcnt = ""
        self.last = ""
        self.A10WW_type = ""
        self.name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ipv6rangestrt: {"type": "string", "format": "ipv6-address"}
    :param pol_name: {"type": "string", "format": "string"}
    :param total_geolocs: {"type": "number", "format": "number"}
    :param iprangestrt: {"type": "string", "format": "ipv4-address"}
    :param filter4: {"enum": ["ip", "ipv6", "ipstat", "ipv6stat"], "type": "string", "format": "enum"}
    :param iprangeend: {"type": "string", "format": "ipv4-address"}
    :param filter1: {"enum": ["directory", "statistics", "global"], "type": "string", "format": "enum"}
    :param filter3: {"enum": ["directory", "statistics", "global"], "type": "string", "format": "enum"}
    :param filter2: {"enum": ["directory", "statistics", "global"], "type": "string", "format": "enum"}
    :param geo_name: {"type": "string", "format": "string"}
    :param geoloc_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"tomask": {"type": "string", "format": "string"}, "hits": {"type": "number", "format": "number"}, "from": {"type": "string", "format": "string"}, "subcnt": {"type": "number", "format": "number"}, "optional": true, "last": {"type": "string", "format": "string"}, "type": {"type": "string", "format": "string"}, "name": {"type": "string", "format": "string"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.ipv6rangestrt = ""
        self.pol_name = ""
        self.total_geolocs = ""
        self.iprangestrt = ""
        self.filter4 = ""
        self.iprangeend = ""
        self.filter1 = ""
        self.filter3 = ""
        self.filter2 = ""
        self.geo_name = ""
        self.geoloc_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Geoloc(A10BaseClass):
    
    """Class Description::
    Operational Status for the object geoloc.

    Class geoloc supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/geoloc/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "geoloc"
        self.a10_url="/axapi/v3/gslb/geoloc/oper"
        self.DeviceProxy = ""
        self.oper = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


