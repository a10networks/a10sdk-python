from a10sdk.common.A10BaseClass import A10BaseClass


class DnsRecord(A10BaseClass):
    
    """Class Description::
    Specify DNS Record.

    Class dns-record supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param data: {"description": "Specify DNS Data", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 512, "type": "string"}
    :param type: {"description": "Specify DNS Type", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": false}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/zone/{name}/service/{service_port}+{service_name}/dns-record/{type}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "type"]

        self.b_key = "dns-record"
        self.a10_url="/axapi/v3/gslb/zone/{name}/service/{service_port}+{service_name}/dns-record/{type}"
        self.DeviceProxy = ""
        self.data = ""
        self.A10WW_type = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


