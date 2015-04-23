from a10sdk.common.A10BaseClass import A10BaseClass


class Capacity(A10BaseClass):
    
    """Class Description::
    Select Service-IP for the device having highest available connection capacity.

    Class capacity supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param threshold: {"description": "Specify capacity threshold, default is 90", "format": "number", "default": 90, "optional": true, "maximum": 100, "minimum": 0, "type": "number"}
    :param capacity_enable: {"default": 0, "optional": true, "type": "number", "description": "Enable capacity", "format": "flag"}
    :param capacity_fail_break: {"default": 0, "optional": true, "type": "number", "description": "Break when exceed threshold", "format": "flag"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/policy/{name}/capacity`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "capacity"
        self.a10_url="/axapi/v3/gslb/policy/{name}/capacity"
        self.DeviceProxy = ""
        self.threshold = ""
        self.capacity_enable = ""
        self.capacity_fail_break = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


