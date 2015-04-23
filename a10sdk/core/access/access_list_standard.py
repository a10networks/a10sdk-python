from a10sdk.common.A10BaseClass import A10BaseClass


class Stdrules(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param subnet: {"not-list": ["any", "host"], "type": "string", "description": "Address to match", "format": "ipv4-address"}
    :param std_remark: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Access list entry comment (Notes for this ACL)", "format": "string-rlx"}
    :param log: {"default": 0, "type": "number", "description": "Log matches against this entry", "format": "flag"}
    :param transparent_session_only: {"default": 0, "type": "number", "description": "Only log transparent sessions", "format": "flag"}
    :param seq_num: {"description": "Sequence number", "minimum": 1, "type": "number", "maximum": 8192, "format": "number"}
    :param rev_subnet_mask: {"type": "string", "description": "Network Mask 0=apply 255=ignore", "format": "ipv4-rev-netmask"}
    :param host: {"not-list": ["any", "subnet"], "type": "string", "description": "A single source host (Host address)", "format": "ipv4-address"}
    :param action: {"enum": ["deny", "permit", "l3-vlan-fwd-disable"], "type": "string", "description": "'deny': Deny; 'permit': Permit; 'l3-vlan-fwd-disable': Disable L3 forwarding between VLANs; ", "format": "enum"}
    :param any: {"default": 0, "not-list": ["host", "subnet"], "type": "number", "description": "Any source host", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stdrules"
        self.DeviceProxy = ""
        self.subnet = ""
        self.std_remark = ""
        self.log = ""
        self.transparent_session_only = ""
        self.seq_num = ""
        self.rev_subnet_mask = ""
        self.host = ""
        self.action = ""
        self.A10WW_any = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Standard(A10BaseClass):
    
    """Class Description::
    Configure Standard Access List.

    Class standard supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param std: {"description": "IP standard access list", "format": "number", "type": "number", "maximum": 99, "minimum": 1, "optional": false}
    :param stdrules: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"subnet": {"not-list": ["any", "host"], "type": "string", "description": "Address to match", "format": "ipv4-address"}, "std-remark": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Access list entry comment (Notes for this ACL)", "format": "string-rlx"}, "log": {"default": 0, "type": "number", "description": "Log matches against this entry", "format": "flag"}, "transparent-session-only": {"default": 0, "type": "number", "description": "Only log transparent sessions", "format": "flag"}, "seq-num": {"description": "Sequence number", "minimum": 1, "type": "number", "maximum": 8192, "format": "number"}, "rev-subnet-mask": {"type": "string", "description": "Network Mask 0=apply 255=ignore", "format": "ipv4-rev-netmask"}, "host": {"not-list": ["any", "subnet"], "type": "string", "description": "A single source host (Host address)", "format": "ipv4-address"}, "action": {"enum": ["deny", "permit", "l3-vlan-fwd-disable"], "type": "string", "description": "'deny': Deny; 'permit': Permit; 'l3-vlan-fwd-disable': Disable L3 forwarding between VLANs; ", "format": "enum"}, "optional": true, "any": {"default": 0, "not-list": ["host", "subnet"], "type": "number", "description": "Any source host", "format": "flag"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/access-list/standard/{std}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "std"]

        self.b_key = "standard"
        self.a10_url="/axapi/v3/access-list/standard/{std}"
        self.DeviceProxy = ""
        self.std = ""
        self.stdrules = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


