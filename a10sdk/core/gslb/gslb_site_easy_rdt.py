from a10sdk.common.A10BaseClass import A10BaseClass


class EasyRdt(A10BaseClass):
    
    """Class Description::
    Active RDT options.

    Class easy-rdt supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param range_factor: {"description": "Factor of RDT Range, default is 25 (Range Factor of Smooth RDT)", "format": "number", "default": 25, "optional": true, "maximum": 1000, "minimum": 0, "type": "number"}
    :param smooth_factor: {"description": "Factor of Smooth RDT, default is 10", "format": "number", "default": 10, "optional": true, "maximum": 100, "minimum": 0, "type": "number"}
    :param mask: {"default": "/32", "optional": true, "type": "string", "description": "Client IP subnet mask, default is 32", "format": "ipv4-netmask-brief"}
    :param overlap: {"default": 0, "optional": true, "type": "number", "description": "Enable overlap for geo-location to do longest match", "format": "flag"}
    :param limit: {"description": "Limit of valid RDT, default is 16383 (Limit, unit: millisecond)", "format": "number", "default": 16383, "optional": true, "maximum": 16383, "minimum": 1, "type": "number"}
    :param ignore_count: {"description": "Ignore count if RDT is out of range, default is 5", "format": "number", "default": 5, "optional": true, "maximum": 15, "minimum": 0, "type": "number"}
    :param aging_time: {"description": "Aging Time, Unit: min, default is 10", "format": "number", "default": 10, "optional": true, "maximum": 15360, "minimum": 1, "type": "number"}
    :param bind_geoloc: {"default": 0, "optional": true, "type": "number", "description": "Bind RDT to geo-location", "format": "flag"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/site/{site_name}/easy-rdt`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "easy-rdt"
        self.a10_url="/axapi/v3/gslb/site/{site_name}/easy-rdt"
        self.DeviceProxy = ""
        self.range_factor = ""
        self.smooth_factor = ""
        self.mask = ""
        self.overlap = ""
        self.limit = ""
        self.ignore_count = ""
        self.aging_time = ""
        self.bind_geoloc = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


