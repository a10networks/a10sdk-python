from a10sdk.common.A10BaseClass import A10BaseClass


class Instance(A10BaseClass):
    
    """Class Description::
    HTTP Basic Authentication Relay instance.

    Class instance supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param name: {"description": "Specify HTTP basic authentication relay name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/aam/authentication/relay/http-basic/instance/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "instance"
        self.a10_url="/axapi/v3/aam/authentication/relay/http-basic/instance/{name}"
        self.DeviceProxy = ""
        self.name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


