from a10sdk.common.A10BaseClass import A10BaseClass


class Trap(A10BaseClass):
    
    """Class Description::
    Set logging level which sent to snmp trap host.

    Class trap supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param trap_levelname: {"optional": true, "enum": ["emergency", "alert", "critical"], "type": "string", "description": "'emergency': System unusable log messages      (severity=0); 'alert': Action must be taken immediately  (severity=1); 'critical': Critical conditions               (severity=2); ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/logging/trap`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "trap"
        self.a10_url="/axapi/v3/logging/trap"
        self.DeviceProxy = ""
        self.trap_levelname = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


