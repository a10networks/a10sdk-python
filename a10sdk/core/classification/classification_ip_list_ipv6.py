from a10sdk.common.A10BaseClass import A10BaseClass


class Ipv6(A10BaseClass):
    
    """Class Description::
    Add IPv6 address range to the current IP list.

    Class ipv6 supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ipv6_subnet: {"optional": false, "type": "string", "description": "Specify IPv6 subnet range", "format": "ipv6-address-plen"}
    :param ipv6_end_ip: {"optional": true, "type": "string", "description": "Add a range of IPs into the current IP list (Specify IPv6 address)", "format": "ipv6-address"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param ipv6_start_ip: {"optional": false, "type": "string", "description": "Specify IPv6 address", "format": "ipv6-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/classification/ip-list/{listname}/ipv6/{ipv6_subnet}+{ipv6_start_ip}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "ipv6_subnet","ipv6_start_ip"]

        self.b_key = "ipv6"
        self.a10_url="/axapi/v3/classification/ip-list/{listname}/ipv6/{ipv6_subnet}+{ipv6_start_ip}"
        self.DeviceProxy = ""
        self.ipv6_subnet = ""
        self.ipv6_end_ip = ""
        self.uuid = ""
        self.ipv6_start_ip = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


