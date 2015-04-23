from a10sdk.common.A10BaseClass import A10BaseClass


class Exception(A10BaseClass):
    
    """    :param action: {"optional": true, "enum": ["add", "delete", "clean"], "type": "string", "description": "'add': Add an exception; 'delete': Delete an exception; 'clean': Delete all exception; ", "format": "enum"}
    :param certificate_name: {"description": "The certificate name", "format": "string", "minLength": 1, "optional": true, "maxLength": 255, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Config the exception which will not be checked.

    Class exception supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/ssl-expire-check/exception`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "exception"
        self.a10_url="/axapi/v3/slb/ssl-expire-check/exception"
        self.DeviceProxy = ""
        self.action = ""
        self.certificate_name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


