from a10sdk.common.A10BaseClass import A10BaseClass


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param conn_rate_unit: {"enum": ["100ms", "second"], "type": "string", "format": "enum"}
    :param icmpv6_rate_over_limit_drop: {"type": "number", "format": "number"}
    :param curr_conn_rate: {"type": "number", "format": "number"}
    :param state: {"enum": ["All Up", "Functional Up", "Partial Up", "Down", "Disb", "Unkn"], "type": "string", "format": "enum"}
    :param curr_icmp_rate: {"type": "number", "format": "number"}
    :param icmpv6_lockup_time_left: {"type": "number", "format": "number"}
    :param mac: {"minLength": 11, "maxLength": 17, "type": "string", "format": "mac-address"}
    :param curr_icmpv6_rate: {"type": "number", "format": "number"}
    :param icmp_rate_over_limit_drop: {"type": "number", "format": "number"}
    :param icmp_lockup_time_left: {"type": "number", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.conn_rate_unit = ""
        self.icmpv6_rate_over_limit_drop = ""
        self.curr_conn_rate = ""
        self.state = ""
        self.curr_icmp_rate = ""
        self.icmpv6_lockup_time_left = ""
        self.mac = ""
        self.curr_icmpv6_rate = ""
        self.icmp_rate_over_limit_drop = ""
        self.icmp_lockup_time_left = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Dns64Virtualserver(A10BaseClass):
    
    """Class Description::
    Operational Status for the object dns64-virtualserver.

    Class dns64-virtualserver supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param port_list: {"minItems": 1, "items": {"type": "port"}, "uniqueItems": true, "array": [{"required": ["port-number", "protocol"], "properties": {"oper": {"type": "object", "properties": {"state": {"enum": ["All Up", "Functional Up", "Partial Up", "Down", "Disb", "Unkn"], "type": "string", "format": "enum"}}}, "protocol": {"enum": ["dns-udp"], "description": "'dns-udp': DNS service over UDP; ", "format": "enum", "type": "string", "oid": "1002", "optional": false}, "port-number": {"description": "Port", "format": "number", "optional": false, "oid": "1001", "maximum": 65534, "minimum": 0, "type": "number"}}}], "type": "array", "$ref": "/axapi/v3/cgnv6/dns64-virtualserver/{name}/port/{port-number}+{protocol}"}
    :param name: {"description": "CGNV6 Virtual Server Name", "format": "string-rlx", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 127, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/dns64-virtualserver/{name}/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "dns64-virtualserver"
        self.a10_url="/axapi/v3/cgnv6/dns64-virtualserver/{name}/oper"
        self.DeviceProxy = ""
        self.oper = {}
        self.port_list = []
        self.name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


