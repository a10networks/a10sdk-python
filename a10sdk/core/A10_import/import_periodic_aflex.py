from a10sdk.common.A10BaseClass import A10BaseClass


class Aflex(A10BaseClass):
    
    """Class Description::
    aFleX Script Source File.

    Class aflex supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param aflex: {"description": "aFleX Script Source File", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param remote_file: {"optional": true, "type": "string", "description": "profile name for remote url", "format": "url"}
    :param use_mgmt_port: {"default": 0, "optional": true, "type": "number", "description": "Use management port as source port", "format": "flag"}
    :param period: {"description": "Specify the period in second", "format": "number", "type": "number", "maximum": 31536000, "minimum": 60, "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/import-periodic/aflex/{aflex}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "aflex"]

        self.b_key = "aflex"
        self.a10_url="/axapi/v3/import-periodic/aflex/{aflex}"
        self.DeviceProxy = ""
        self.aflex = ""
        self.remote_file = ""
        self.use_mgmt_port = ""
        self.period = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


