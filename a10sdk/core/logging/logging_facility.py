from a10sdk.common.A10BaseClass import A10BaseClass


class Facility(A10BaseClass):
    
    """Class Description::
    Facility parameter for syslog messages.

    Class facility supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param facilityname: {"description": "'local0': Local use; 'local1': Local use; 'local2': Local use; 'local3': Local use; 'local4': Local use; 'local5': Local use; 'local6': Local use; 'local7': Local use;  (Facility parameter for syslog messages)", "format": "enum", "default": "local0", "type": "string", "enum": ["local0", "local1", "local2", "local3", "local4", "local5", "local6", "local7"], "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/logging/facility`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "facility"
        self.a10_url="/axapi/v3/logging/facility"
        self.DeviceProxy = ""
        self.facilityname = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


