from a10sdk.common.A10BaseClass import A10BaseClass


class Ospf(A10BaseClass):
    
    """Class Description::
    Open Shortest Path First for IPv4 (OSPF).

    Class ospf supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ospf_ip_list: {"minItems": 1, "items": {"type": "ospf-ip"}, "uniqueItems": true, "array": [{"required": ["ip-addr"], "properties": {"dead-interval": {"description": "Interval after which a neighbor is declared dead (Seconds)", "format": "number", "default": 40, "optional": true, "maximum": 65535, "minimum": 1, "type": "number"}, "authentication-key": {"description": "Authentication password (key) (The OSPF password (key))", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 8, "type": "string"}, "mtu-ignore": {"default": 0, "optional": true, "type": "number", "description": "Ignores the MTU in DBD packets", "format": "flag"}, "priority": {"description": "Router priority", "format": "number", "default": 1, "optional": true, "maximum": 255, "minimum": 0, "type": "number"}, "transmit-delay": {"description": "Link state transmit delay (Seconds)", "format": "number", "default": 1, "optional": true, "maximum": 65535, "minimum": 1, "type": "number"}, "value": {"optional": true, "enum": ["message-digest", "null"], "type": "string", "description": "'message-digest': Use message-digest authentication; 'null': Use no authentication; ", "format": "enum"}, "hello-interval": {"description": "Time between HELLO packets (Seconds)", "format": "number", "default": 10, "optional": true, "maximum": 65535, "minimum": 1, "type": "number"}, "authentication": {"default": 0, "optional": true, "type": "number", "description": "Enable authentication", "format": "flag"}, "cost": {"description": "Interface cost", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": true}, "database-filter": {"optional": true, "enum": ["all"], "type": "string", "description": "'all': Filter all LSA; ", "format": "enum"}, "ip-addr": {"optional": false, "type": "string", "description": "Address of interface", "format": "ipv4-address"}, "retransmit-interval": {"description": "Time between retransmitting lost link state advertisements (Seconds)", "format": "number", "default": 5, "optional": true, "maximum": 65535, "minimum": 1, "type": "number"}, "message-digest-cfg": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"md5-value": {"minLength": 1, "maxLength": 16, "type": "string", "description": "The OSPF password (1-16)", "format": "password"}, "message-digest-key": {"description": "Message digest authentication password (key) (Key id)", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}, "optional": true, "encrypted": {"type": "encrypted", "description": "Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string)", "format": "encrypted"}}}]}, "out": {"default": 0, "optional": true, "type": "number", "description": "Outgoing LSA", "format": "flag"}}}], "type": "array", "$ref": "/axapi/v3/interface/lif/{ifnum}/ip/ospf/ospf-ip/{ip-addr}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/interface/lif/{ifnum}/ip/ospf`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "ospf"
        self.a10_url="/axapi/v3/interface/lif/{ifnum}/ip/ospf"
        self.DeviceProxy = ""
        self.ospf_ip_list = []
        self.ospf_global = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


