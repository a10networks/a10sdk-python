from a10sdk.common.A10BaseClass import A10BaseClass


class IpList(A10BaseClass):
    
    """Class Description::
    Configure or create IP list.

    Class ip-list supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param listname: {"description": "Specify IP list name", "format": "string", "minLength": 1, "optional": false, "maxLength": 31, "type": "string"}
    :param ip_list: {"minItems": 1, "items": {"type": "ip"}, "uniqueItems": true, "array": [{"required": ["ipv4-start-ip"], "properties": {"ipv4-start-ip": {"optional": false, "type": "string", "description": "Specify IP address (A.B.C.D)", "format": "ipv4-address"}, "mask": {"optional": true, "type": "string", "description": "Specify IP network mask", "format": "ipv4-netmask"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "ipv4-end-ip": {"optional": true, "type": "string", "description": "Add a range of IPs into the current IP list (Specify IP address (A.B.C.D))", "format": "ipv4-address"}}}], "type": "array", "$ref": "/axapi/v3/classification/ip-list/{listname}/ip/{ipv4-start-ip}"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param ipv6_list: {"minItems": 1, "items": {"type": "ipv6"}, "uniqueItems": true, "array": [{"required": ["ipv6-subnet", "ipv6-start-ip"], "properties": {"ipv6-subnet": {"optional": false, "type": "string", "description": "Specify IPv6 subnet range", "format": "ipv6-address-plen"}, "ipv6-end-ip": {"optional": true, "type": "string", "description": "Add a range of IPs into the current IP list (Specify IPv6 address)", "format": "ipv6-address"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "ipv6-start-ip": {"optional": false, "type": "string", "description": "Specify IPv6 address", "format": "ipv6-address"}}}], "type": "array", "$ref": "/axapi/v3/classification/ip-list/{listname}/ipv6/{ipv6-subnet}+{ipv6-start-ip}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/classification/ip-list/{listname}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "listname"]

        self.b_key = "ip-list"
        self.a10_url="/axapi/v3/classification/ip-list/{listname}"
        self.DeviceProxy = ""
        self.listname = ""
        self.ip_list = []
        self.uuid = ""
        self.ipv6_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


