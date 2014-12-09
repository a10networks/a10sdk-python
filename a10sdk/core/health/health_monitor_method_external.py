from a10sdk.common.A10BaseClass import A10BaseClass


class External(A10BaseClass):
    
    """Class Description::
    EXTERNAL type.

    Class external supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ext_preference: {"default": 0, "optional": true, "type": "number", "description": "Get server's perference", "format": "flag"}
    :param ext_port: {"description": "Specify the server port (Port Number)", "format": "number", "type": "number", "maximum": 65534, "minimum": 1, "optional": true}
    :param external: {"default": 0, "optional": true, "type": "number", "description": "EXTERNAL type", "format": "flag"}
    :param ext_arguments: {"description": "Specify external application's arguments (Application arguments)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 127, "type": "string"}
    :param ext_program: {"description": "Specify external application (Program name)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/health/monitor/{name}/method/external`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "external"
        self.a10_url="/axapi/v3/health/monitor/{name}/method/external"
        self.DeviceProxy = ""
        self.ext_preference = ""
        self.ext_port = ""
        self.external = ""
        self.ext_arguments = ""
        self.ext_program = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


