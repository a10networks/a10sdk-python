from a10sdk.common.A10BaseClass import A10BaseClass


class ResendTemplate(A10BaseClass):
    
    """Class Description::
    Configure when to resend netflow template.

    Class resend-template supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param records: {"description": "To resend template once for each number of records (Number of records: default is 1000, 0 means never resend template)", "format": "number", "default": 1000, "optional": true, "maximum": 1000000, "minimum": 0, "type": "number"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param timeout: {"description": "To set time interval to resend template (number of seconds: default is 1800, 0 means never resend template)", "format": "number", "default": 1800, "optional": true, "maximum": 86400, "minimum": 0, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/netflow/monitor/{name}/resend-template`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "resend-template"
        self.a10_url="/axapi/v3/netflow/monitor/{name}/resend-template"
        self.DeviceProxy = ""
        self.records = ""
        self.uuid = ""
        self.timeout = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


