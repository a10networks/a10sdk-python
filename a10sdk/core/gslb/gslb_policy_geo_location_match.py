from a10sdk.common.A10BaseClass import A10BaseClass


class GeoLocationMatch(A10BaseClass):
    
    """Class Description::
    Specify match order of geographic.

    Class geo-location-match supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param geo_type_overlap: {"optional": true, "enum": ["global", "policy"], "type": "string", "description": "'global': Global Geo-location; 'policy': Policy Geo-location; ", "format": "enum"}
    :param overlap: {"default": 0, "optional": true, "type": "number", "description": "Enable overlap mode to do longest match", "format": "flag"}
    :param match_first: {"description": "'global': Global Geo-location; 'policy': Policy Geo-location; ", "format": "enum", "default": "global", "type": "string", "enum": ["global", "policy"], "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/policy/{name}/geo-location-match`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "geo-location-match"
        self.a10_url="/axapi/v3/gslb/policy/{name}/geo-location-match"
        self.DeviceProxy = ""
        self.uuid = ""
        self.geo_type_overlap = ""
        self.overlap = ""
        self.match_first = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


