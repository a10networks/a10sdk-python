from a10sdk.common.A10BaseClass import A10BaseClass


class GeoLocList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param conn_limit: {"type": "number", "format": "number"}
    :param L: {"default": 0, "type": "number", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "geo-loc-list"
        self.DeviceProxy = ""
        self.conn_limit = ""
        self.L = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class ClassListGeoLocation(A10BaseClass):
    
    """Class Description::
    Configure classification list.

    Class class-list-geo-location supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param geo_loc_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"conn-limit": {"type": "number", "format": "number"}, "optional": true, "L": {"default": 0, "type": "number", "format": "flag"}}}]}
    :param name: {"description": "Specify name of the class list", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param file: {"description": "Create/Edit a class-list stored as a file", "format": "flag", "default": 0, "type": "number", "modify-not-allowed": 1, "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/class-list-geo-location/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "class-list-geo-location"
        self.a10_url="/axapi/v3/class-list-geo-location/{name}"
        self.DeviceProxy = ""
        self.geo_loc_list = []
        self.name = ""
        self.A10WW_file = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


