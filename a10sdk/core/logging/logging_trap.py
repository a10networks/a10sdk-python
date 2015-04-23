from a10sdk.common.A10BaseClass import A10BaseClass


class Trap(A10BaseClass):
    
    """    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param trap_levelname: {"description": "'disable': Do not send trap to snmp host; 'emergency': System unusable log messages      (severity=0); 'alert': Action must be taken immediately  (severity=1); 'critical': Critical conditions               (severity=2); ", "format": "enum", "default": "disable", "type": "string", "enum": ["disable", "emergency", "alert", "critical"], "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Set logging level which sent to snmp trap host.

    Class trap supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/logging/trap`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "trap"
        self.a10_url="/axapi/v3/logging/trap"
        self.DeviceProxy = ""
        self.uuid = ""
        self.trap_levelname = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


