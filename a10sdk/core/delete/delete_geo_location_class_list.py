from a10sdk.common.A10BaseClass import A10BaseClass


class GeoLocationClassList(A10BaseClass):
    
    """    :param filename: {"description": "Specify file to be deleted", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Delete geo-location class-list file.

    Class geo-location-class-list supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/delete/geo-location-class-list`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "geo-location-class-list"
        self.a10_url="/axapi/v3/delete/geo-location-class-list"
        self.DeviceProxy = ""
        self.filename = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


