from a10sdk.common.A10BaseClass import A10BaseClass


class ActiveRdt(A10BaseClass):
    
    """Class Description::
    Active RDT Options for SLB device.

    Class active-rdt supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param domain: {"description": "Specify Query Domain (Specify Domain Name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}
    :param retry: {"description": "Specify Retry Count, default is 3", "format": "number", "default": 3, "optional": true, "maximum": 16, "minimum": 0, "type": "number"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param track: {"description": "Specify Tracking Time, unit: second, default is 60", "format": "number", "default": 60, "optional": true, "maximum": 16383, "minimum": 3, "type": "number"}
    :param interval: {"description": "Specify Query Interval, unit: second, default is 1", "format": "number", "default": 1, "optional": true, "maximum": 16383, "minimum": 1, "type": "number"}
    :param sleep: {"description": "Specify Sleep Time when query fail, unit: second, default is 3", "format": "number", "default": 3, "optional": true, "maximum": 300, "minimum": 1, "type": "number"}
    :param timeout: {"description": "Specify Query Timeout, unit: msec, default is 3000", "format": "number", "default": 3000, "optional": true, "maximum": 16383, "minimum": 1, "type": "number"}
    :param port: {"description": "Specify local port to send probe packet, default is 0 (no port)", "format": "number", "default": 0, "optional": true, "maximum": 65535, "minimum": 0, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/active-rdt`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "active-rdt"
        self.a10_url="/axapi/v3/gslb/active-rdt"
        self.DeviceProxy = ""
        self.domain = ""
        self.retry = ""
        self.uuid = ""
        self.track = ""
        self.interval = ""
        self.sleep = ""
        self.timeout = ""
        self.port = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


