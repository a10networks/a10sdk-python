from a10sdk.common.A10BaseClass import A10BaseClass


class Remote(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ipv4_list: {"minLength": 1, "maxLength": 63, "type": "string", "description": "IP-list of IPv4 remote clients (IP-list name)", "format": "string-rlx"}
    :param ipv6_list: {"minLength": 1, "maxLength": 63, "type": "string", "description": "IP-list of IPv6 remote clients (IP-list name)", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "remote"
        self.DeviceProxy = ""
        self.ipv4_list = ""
        self.ipv6_list = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "msisdn-received", "imei-received", "imsi-received", "custom-received", "radius-request-received", "radius-request-dropped", "radius-table-full", "ha-standby-dropped", "smp-mem-allocated", "smp-mem-alloc-failed", "smp-mem-freed", "smp-created", "smp-in-rml", "smp-deleted", "mem-allocated", "mem-alloc-failed", "mem-freed", "ha-sync-create-sent", "ha-sync-delete-sent", "ha-sync-create-recv", "ha-sync-delete-recv"], "type": "string", "description": "'all': all; 'msisdn-received': MSISDN Received; 'imei-received': IMEI Received; 'imsi-received': IMSI Received; 'custom-received': Custom attribute Received; 'radius-request-received': RADIUS Request Received; 'radius-request-dropped': RADIUS Request Dropped (Malformed Packet); 'radius-table-full': RADIUS Request Dropped (Table Full); 'ha-standby-dropped': HA Standby Dropped; 'smp-mem-allocated': RADIUS SMP Memory Allocated; 'smp-mem-alloc-failed': RADIUS SMP Memory Allocation Failed; 'smp-mem-freed': RADIUS SMP Memory Freed; 'smp-created': RADIUS SMP Created; 'smp-in-rml': RADIUS SMP in RML; 'smp-deleted': RADIUS SMP Deleted; 'mem-allocated': RADIUS Memory Allocated; 'mem-alloc-failed': RADIUS Memory Allocation Failed; 'mem-freed': RADIUS Memory Freed; 'ha-sync-create-sent': HA Record Sync Create Sent; 'ha-sync-delete-sent': HA Record Sync Delete Sent; 'ha-sync-create-recv': HA Record Sync Create Received; 'ha-sync-delete-recv': HA Record Sync Delete Received; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Attribute(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param vendor: {"description": "RADIUS vendor attribute information (RADIUS vendor ID)", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}
    :param name: {"minLength": 1, "maxLength": 15, "type": "string", "description": "Customized attribute name", "format": "string"}
    :param number: {"description": "RADIUS attribute number", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}
    :param value: {"enum": ["hexadecimal"], "type": "string", "description": "'hexadecimal': Type of attribute value is hexadecimal; ", "format": "enum"}
    :param custom_vendor: {"description": "RADIUS vendor attribute information (RADIUS vendor ID)", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}
    :param custom_number: {"description": "RADIUS attribute number", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}
    :param attribute_value: {"enum": ["inside-ip", "inside-ipv6", "imei", "imsi", "msisdn", "custom1", "custom2", "custom3"], "type": "string", "description": "'inside-ip': Inside IP address; 'inside-ipv6': Inside IPv6 address; 'imei': International Mobile Equipment Identity (IMEI); 'imsi': International Mobile Subscriber Identity (IMSI); 'msisdn': Mobile Subscriber Integrated Services Digital Network-Number (MSISDN); 'custom1': Customized attribute 1; 'custom2': Customized attribute 2; 'custom3': Customized attribute 3; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "attribute"
        self.DeviceProxy = ""
        self.vendor = ""
        self.name = ""
        self.number = ""
        self.value = ""
        self.custom_vendor = ""
        self.custom_number = ""
        self.attribute_value = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Server(A10BaseClass):
    
    """    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param encrypted: {"optional": true, "type": "encrypted", "description": "Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED secret string)", "format": "encrypted"}
    :param vrid: {"description": "Join a VRRP-A failover group", "format": "number", "type": "number", "maximum": 31, "minimum": 1, "optional": true}
    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "msisdn-received", "imei-received", "imsi-received", "custom-received", "radius-request-received", "radius-request-dropped", "radius-table-full", "ha-standby-dropped", "smp-mem-allocated", "smp-mem-alloc-failed", "smp-mem-freed", "smp-created", "smp-in-rml", "smp-deleted", "mem-allocated", "mem-alloc-failed", "mem-freed", "ha-sync-create-sent", "ha-sync-delete-sent", "ha-sync-create-recv", "ha-sync-delete-recv"], "type": "string", "description": "'all': all; 'msisdn-received': MSISDN Received; 'imei-received': IMEI Received; 'imsi-received': IMSI Received; 'custom-received': Custom attribute Received; 'radius-request-received': RADIUS Request Received; 'radius-request-dropped': RADIUS Request Dropped (Malformed Packet); 'radius-table-full': RADIUS Request Dropped (Table Full); 'ha-standby-dropped': HA Standby Dropped; 'smp-mem-allocated': RADIUS SMP Memory Allocated; 'smp-mem-alloc-failed': RADIUS SMP Memory Allocation Failed; 'smp-mem-freed': RADIUS SMP Memory Freed; 'smp-created': RADIUS SMP Created; 'smp-in-rml': RADIUS SMP in RML; 'smp-deleted': RADIUS SMP Deleted; 'mem-allocated': RADIUS Memory Allocated; 'mem-alloc-failed': RADIUS Memory Allocation Failed; 'mem-freed': RADIUS Memory Freed; 'ha-sync-create-sent': HA Record Sync Create Sent; 'ha-sync-delete-sent': HA Record Sync Delete Sent; 'ha-sync-create-recv': HA Record Sync Create Received; 'ha-sync-delete-recv': HA Record Sync Delete Received; ", "format": "enum"}}}]}
    :param secret: {"default": 0, "optional": true, "type": "number", "description": "Configure shared secret", "format": "flag"}
    :param attribute: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"vendor": {"description": "RADIUS vendor attribute information (RADIUS vendor ID)", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}, "name": {"minLength": 1, "maxLength": 15, "type": "string", "description": "Customized attribute name", "format": "string"}, "number": {"description": "RADIUS attribute number", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}, "value": {"enum": ["hexadecimal"], "type": "string", "description": "'hexadecimal': Type of attribute value is hexadecimal; ", "format": "enum"}, "custom-vendor": {"description": "RADIUS vendor attribute information (RADIUS vendor ID)", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}, "custom-number": {"description": "RADIUS attribute number", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}, "attribute-value": {"enum": ["inside-ip", "inside-ipv6", "imei", "imsi", "msisdn", "custom1", "custom2", "custom3"], "type": "string", "description": "'inside-ip': Inside IP address; 'inside-ipv6': Inside IPv6 address; 'imei': International Mobile Equipment Identity (IMEI); 'imsi': International Mobile Subscriber Identity (IMSI); 'msisdn': Mobile Subscriber Integrated Services Digital Network-Number (MSISDN); 'custom1': Customized attribute 1; 'custom2': Customized attribute 2; 'custom3': Customized attribute 3; ", "format": "enum"}, "optional": true}}]}
    :param listen_port: {"description": "Configure the listen port of RADIUS server (Port number)", "format": "number", "type": "number", "maximum": 65535, "minimum": 1024, "optional": true}
    :param secret_string: {"description": "The RADIUS secret", "format": "password", "minLength": 1, "optional": true, "maxLength": 127, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Configure system as a RADIUS server.

    Class server supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/lsn/radius/server`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "server"
        self.a10_url="/axapi/v3/cgnv6/lsn/radius/server"
        self.DeviceProxy = ""
        self.remote = {}
        self.uuid = ""
        self.encrypted = ""
        self.vrid = ""
        self.sampling_enable = []
        self.secret = ""
        self.attribute = []
        self.listen_port = ""
        self.secret_string = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


