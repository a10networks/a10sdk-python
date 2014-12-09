from a10sdk.common.A10BaseClass import A10BaseClass


class DnsNsRecord(A10BaseClass):
    
    """Class Description::
    Specify DNS NS Record.

    Class dns-ns-record supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ns_name: {"description": "Specify Domain Name", "format": "string", "minLength": 1, "optional": false, "maxLength": 127, "type": "string"}
    :param ttl: {"optional": true, "type": "number", "description": "Specify TTL", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/zone/{name}/service/{service_port}+{service_name}/dns-ns-record/{ns_name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "ns_name"]

        self.b_key = "dns-ns-record"
        self.a10_url="/axapi/v3/gslb/zone/{name}/service/{service_port}+{service_name}/dns-ns-record/{ns_name}"
        self.DeviceProxy = ""
        self.ns_name = ""
        self.ttl = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


