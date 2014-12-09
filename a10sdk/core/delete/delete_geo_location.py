from a10sdk.common.A10BaseClass import A10BaseClass


class GeoLocation(A10BaseClass):
    
    """    :param all: {"description": "Delete all files", "format": "flag", "default": 0, "optional": true, "not": "filename", "type": "number"}
    :param filename: {"description": "Specify file to be deleted", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "not": "all", "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Delete geo-location file.

    Class geo-location supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/delete/geo-location`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "geo-location"
        self.a10_url="/axapi/v3/delete/geo-location"
        self.DeviceProxy = ""
        self.A10WW_all = ""
        self.filename = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


