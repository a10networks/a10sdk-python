from a10sdk.common.A10BaseClass import A10BaseClass


class Log(A10BaseClass):
    
    """Class Description::
    Authentication log configuration.

    Class log supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param enable: {"default": 0, "optional": true, "type": "number", "description": "Enable authentication logs", "format": "flag"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param facility: {"description": "'local0': Local use; 'local1': Local use; 'local2': Local use; 'local3': Local use; 'local4': Local use; 'local5': Local use; 'local6': Local use; 'local7': Local use; ", "format": "enum", "default": "local0", "type": "string", "enum": ["local0", "local1", "local2", "local3", "local4", "local5", "local6", "local7"], "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/aam/authentication/log`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "log"
        self.a10_url="/axapi/v3/aam/authentication/log"
        self.DeviceProxy = ""
        self.enable = ""
        self.uuid = ""
        self.facility = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


