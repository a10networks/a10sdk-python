from a10sdk.common.A10BaseClass import A10BaseClass


class DnsTxtRecord(A10BaseClass):
    
    """Class Description::
    Specify DNS TXT Record.

    Class dns-txt-record supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param record_name: {"description": "Specify the Object Name for TXT Data", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param txt_data: {"description": "Specify TXT Data", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 1000, "type": "string"}
    :param ttl: {"description": "Specify TTL", "format": "number", "default": 0, "optional": true, "maximum": 2147483647, "minimum": 0, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/zone/{name}/service/{service_port}+{service_name}/dns-txt-record/{record_name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "record_name"]

        self.b_key = "dns-txt-record"
        self.a10_url="/axapi/v3/gslb/zone/{name}/service/{service_port}+{service_name}/dns-txt-record/{record_name}"
        self.DeviceProxy = ""
        self.uuid = ""
        self.record_name = ""
        self.txt_data = ""
        self.ttl = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


