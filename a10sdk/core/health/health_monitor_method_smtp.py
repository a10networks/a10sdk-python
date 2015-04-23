from a10sdk.common.A10BaseClass import A10BaseClass


class Smtp(A10BaseClass):
    
    """Class Description::
    SMTP type.

    Class smtp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param smtp_port: {"description": "Specify SMTP port, default is 25 (Port Number (default 25))", "format": "number", "default": 25, "optional": true, "maximum": 65534, "minimum": 1, "type": "number"}
    :param smtp_domain: {"description": "Specify domain name of 'helo' command", "format": "string", "minLength": 1, "optional": true, "maxLength": 255, "type": "string"}
    :param smtp: {"default": 0, "optional": true, "type": "number", "description": "SMTP type", "format": "flag"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/health/monitor/{name}/method/smtp`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "smtp"
        self.a10_url="/axapi/v3/health/monitor/{name}/method/smtp"
        self.DeviceProxy = ""
        self.smtp_port = ""
        self.smtp_domain = ""
        self.smtp = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


