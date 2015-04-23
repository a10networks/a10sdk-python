from a10sdk.common.A10BaseClass import A10BaseClass


class GeoLocation(A10BaseClass):
    
    """Class Description::
    Geo-location CSV File.

    Class geo-location supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param geo_location: {"description": "Geo-location CSV File", "partition-visibility": "shared", "minLength": 1, "format": "string", "optional": false, "maxLength": 63, "type": "string"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param remote_file: {"optional": true, "partition-visibility": "shared", "type": "string", "description": "profile name for remote url", "format": "url"}
    :param use_mgmt_port: {"description": "Use management port as source port", "partition-visibility": "shared", "default": 0, "type": "number", "format": "flag", "optional": true}
    :param period: {"description": "Specify the period in second", "format": "number", "type": "number", "maximum": 31536000, "minimum": 60, "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/export-periodic/geo-location/{geo_location}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "geo_location"]

        self.b_key = "geo-location"
        self.a10_url="/axapi/v3/export-periodic/geo-location/{geo_location}"
        self.DeviceProxy = ""
        self.geo_location = ""
        self.uuid = ""
        self.remote_file = ""
        self.use_mgmt_port = ""
        self.period = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


