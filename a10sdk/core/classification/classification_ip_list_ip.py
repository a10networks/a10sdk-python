from a10sdk.common.A10BaseClass import A10BaseClass


class Ip(A10BaseClass):
    
    """Class Description::
    Add IP to the current IP list.

    Class ip supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ipv4_start_ip: {"optional": false, "type": "string", "description": "Specify IP address (A.B.C.D)", "format": "ipv4-address"}
    :param mask: {"optional": true, "type": "string", "description": "Specify IP network mask", "format": "ipv4-netmask"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param ipv4_end_ip: {"optional": true, "type": "string", "description": "Add a range of IPs into the current IP list (Specify IP address (A.B.C.D))", "format": "ipv4-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/classification/ip-list/{listname}/ip/{ipv4_start_ip}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "ipv4_start_ip"]

        self.b_key = "ip"
        self.a10_url="/axapi/v3/classification/ip-list/{listname}/ip/{ipv4_start_ip}"
        self.DeviceProxy = ""
        self.ipv4_start_ip = ""
        self.mask = ""
        self.uuid = ""
        self.ipv4_end_ip = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


