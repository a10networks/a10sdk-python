from a10sdk.common.A10BaseClass import A10BaseClass


class DnsCnameRecord(A10BaseClass):
    
    """Class Description::
    Specify DNS CNAME Record.

    Class dns-cname-record supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param as_backup: {"default": 0, "optional": true, "type": "number", "description": "As backup when fail", "format": "flag"}
    :param alias_name: {"description": "Specify the alias name", "format": "string", "minLength": 1, "optional": false, "maxLength": 127, "type": "string"}
    :param admin_preference: {"description": "Specify Administrative Preference, default is 100", "format": "number", "default": 100, "optional": true, "maximum": 255, "minimum": 0, "type": "number"}
    :param weight: {"description": "Specify Weight, default is 1", "format": "number", "default": 1, "optional": true, "maximum": 100, "minimum": 1, "type": "number"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/zone/{name}/service/{service_port}+{service_name}/dns-cname-record/{alias_name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "alias_name"]

        self.b_key = "dns-cname-record"
        self.a10_url="/axapi/v3/gslb/zone/{name}/service/{service_port}+{service_name}/dns-cname-record/{alias_name}"
        self.DeviceProxy = ""
        self.as_backup = ""
        self.alias_name = ""
        self.admin_preference = ""
        self.weight = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


