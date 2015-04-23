from a10sdk.common.A10BaseClass import A10BaseClass


class DnsMxRecord(A10BaseClass):
    
    """Class Description::
    Specify DNS MX Record.

    Class dns-mx-record supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param priority: {"description": "Specify Priority", "format": "number", "type": "number", "maximum": 65535, "minimum": 0, "optional": true}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param mx_name: {"description": "Specify Domain Name", "format": "string", "minLength": 1, "optional": false, "maxLength": 127, "type": "string"}
    :param ttl: {"description": "Specify TTL", "format": "number", "type": "number", "maximum": 2147483647, "minimum": 0, "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/zone/{name}/dns-mx-record/{mx_name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "mx_name"]

        self.b_key = "dns-mx-record"
        self.a10_url="/axapi/v3/gslb/zone/{name}/dns-mx-record/{mx_name}"
        self.DeviceProxy = ""
        self.priority = ""
        self.uuid = ""
        self.mx_name = ""
        self.ttl = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


