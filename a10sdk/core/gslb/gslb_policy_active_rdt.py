from a10sdk.common.A10BaseClass import A10BaseClass


class ActiveRdt(A10BaseClass):
    
    """Class Description::
    Select SLB device with the shortest round delay time to local DNS.

    Class active-rdt supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ignore_id: {"description": "Ignore IP Address specified in IP List by ID", "format": "number", "type": "number", "maximum": 31, "minimum": 0, "optional": true}
    :param keep_tracking: {"default": 0, "optional": true, "type": "number", "description": "Keep tracking client even round-delay-time samples are ready", "format": "flag"}
    :param enable: {"default": 0, "optional": true, "type": "number", "description": "Enable the active rdt", "format": "flag"}
    :param samples: {"description": "Specify samples number for round-delay-time (Number of samples,default is 5)", "format": "number", "default": 5, "optional": true, "maximum": 8, "minimum": 1, "type": "number"}
    :param skip: {"description": "Skip query if round-delay-time samples are not ready (Specify maximum skip count,default is 3)", "format": "number", "default": 3, "optional": true, "maximum": 31, "minimum": 1, "type": "number"}
    :param fail_break: {"default": 0, "optional": true, "type": "number", "description": "Break when no valid RDT", "format": "flag"}
    :param limit: {"description": "Limit of allowed RDT, default is 16383 (Limit, unit: millisecond)", "format": "number", "default": 16383, "optional": true, "maximum": 16383, "minimum": 1, "type": "number"}
    :param timeout: {"description": "Specify timeout if round-delay-time samples are not ready (Specify timeout, unit:sec,default is 3)", "format": "number", "default": 3, "optional": true, "maximum": 255, "minimum": 1, "type": "number"}
    :param single_shot: {"default": 0, "optional": true, "type": "number", "description": "Single Shot RDT", "format": "flag"}
    :param difference: {"description": "The difference between the round-delay-time, default is 0", "format": "number", "default": 0, "optional": true, "maximum": 16383, "minimum": 0, "type": "number"}
    :param tolerance: {"description": "The difference percentage between the round-delay-time, default is 10 (Tolerance)", "format": "number", "default": 10, "optional": true, "maximum": 100, "minimum": 0, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/policy/{name}/active-rdt`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "active-rdt"
        self.a10_url="/axapi/v3/gslb/policy/{name}/active-rdt"
        self.DeviceProxy = ""
        self.ignore_id = ""
        self.keep_tracking = ""
        self.enable = ""
        self.samples = ""
        self.skip = ""
        self.fail_break = ""
        self.limit = ""
        self.timeout = ""
        self.single_shot = ""
        self.difference = ""
        self.tolerance = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


