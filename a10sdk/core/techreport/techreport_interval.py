from a10sdk.common.A10BaseClass import A10BaseClass


class Interval(A10BaseClass):
    
    """Class Description::
    Configure polling techreport interval.

    Class interval supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param value: {"description": "Showtech interval in minutes (default is 15)", "format": "number", "type": "number", "maximum": 120, "minimum": 15, "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/techreport/interval`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "interval"
        self.a10_url="/axapi/v3/techreport/interval"
        self.DeviceProxy = ""
        self.uuid = ""
        self.value = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


