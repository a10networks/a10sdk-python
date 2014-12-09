from a10sdk.common.A10BaseClass import A10BaseClass


class RouteMap(A10BaseClass):
    
    """Class Description::
    Configure route-map.

    Class route-map supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param action: {"optional": false, "enum": ["permit", "deny"], "type": "string", "description": "'permit': Route map permits set operations; 'deny': Route map denies set operations; ", "format": "enum"}
    :param tag: {"description": "Route map tag", "format": "string", "minLength": 1, "optional": false, "maxLength": 128, "type": "string"}
    :param sequence: {"description": "Sequence to insert to/delete from existing route-map entry", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": false}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/route-map/{tag}+{action}+{sequence}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "tag","action","sequence"]

        self.b_key = "route-map"
        self.a10_url="/axapi/v3/route-map/{tag}+{action}+{sequence}"
        self.DeviceProxy = ""
        self.action = ""
        self.tag = ""
        self.A10WW_set = {}
        self.match = {}
        self.sequence = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


