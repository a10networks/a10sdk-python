from a10sdk.common.A10BaseClass import A10BaseClass


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ptr_memory: {"type": "number", "format": "number"}
    :param total_memory: {"type": "number", "format": "number"}
    :param reference_objects: {"type": "number", "format": "number"}
    :param mx_objects: {"type": "number", "format": "number"}
    :param ds_objects: {"type": "number", "format": "number"}
    :param nsec_objects: {"type": "number", "format": "number"}
    :param array_memory: {"type": "number", "format": "number"}
    :param nsec3param_objects: {"type": "number", "format": "number"}
    :param srv_memory: {"type": "number", "format": "number"}
    :param reference_memory: {"type": "number", "format": "number"}
    :param srv_objects: {"type": "number", "format": "number"}
    :param table_memory: {"type": "number", "format": "number"}
    :param a_objects: {"type": "number", "format": "number"}
    :param ns_memory: {"type": "number", "format": "number"}
    :param aaaa_memory: {"type": "number", "format": "number"}
    :param zone_objects: {"type": "number", "format": "number"}
    :param table_objects: {"type": "number", "format": "number"}
    :param mx_memory: {"type": "number", "format": "number"}
    :param soa_memory: {"type": "number", "format": "number"}
    :param domain_objects: {"type": "number", "format": "number"}
    :param nsec_memory: {"type": "number", "format": "number"}
    :param nsec3_objects: {"type": "number", "format": "number"}
    :param a_memory: {"type": "number", "format": "number"}
    :param array_objects: {"type": "number", "format": "number"}
    :param total_objects: {"type": "number", "format": "number"}
    :param soa_objects: {"type": "number", "format": "number"}
    :param ds_memory: {"type": "number", "format": "number"}
    :param cname_objects: {"type": "number", "format": "number"}
    :param domain_memory: {"type": "number", "format": "number"}
    :param nsec3param_memory: {"type": "number", "format": "number"}
    :param txt_memory: {"type": "number", "format": "number"}
    :param dnskey_memory: {"type": "number", "format": "number"}
    :param ns_objects: {"type": "number", "format": "number"}
    :param ptr_objects: {"type": "number", "format": "number"}
    :param aaaa_objects: {"type": "number", "format": "number"}
    :param cname_memory: {"type": "number", "format": "number"}
    :param txt_objects: {"type": "number", "format": "number"}
    :param rrsig_objects: {"type": "number", "format": "number"}
    :param rrsig2_memory: {"type": "number", "format": "number"}
    :param nsec3_memory: {"type": "number", "format": "number"}
    :param zone_memory: {"type": "number", "format": "number"}
    :param rrsig2_objects: {"type": "number", "format": "number"}
    :param rrsig_memory: {"type": "number", "format": "number"}
    :param dnskey_objects: {"type": "number", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.ptr_memory = ""
        self.total_memory = ""
        self.reference_objects = ""
        self.mx_objects = ""
        self.ds_objects = ""
        self.nsec_objects = ""
        self.array_memory = ""
        self.nsec3param_objects = ""
        self.srv_memory = ""
        self.reference_memory = ""
        self.srv_objects = ""
        self.table_memory = ""
        self.a_objects = ""
        self.ns_memory = ""
        self.aaaa_memory = ""
        self.zone_objects = ""
        self.table_objects = ""
        self.mx_memory = ""
        self.soa_memory = ""
        self.domain_objects = ""
        self.nsec_memory = ""
        self.nsec3_objects = ""
        self.a_memory = ""
        self.array_objects = ""
        self.total_objects = ""
        self.soa_objects = ""
        self.ds_memory = ""
        self.cname_objects = ""
        self.domain_memory = ""
        self.nsec3param_memory = ""
        self.txt_memory = ""
        self.dnskey_memory = ""
        self.ns_objects = ""
        self.ptr_objects = ""
        self.aaaa_objects = ""
        self.cname_memory = ""
        self.txt_objects = ""
        self.rrsig_objects = ""
        self.rrsig2_memory = ""
        self.nsec3_memory = ""
        self.zone_memory = ""
        self.rrsig2_objects = ""
        self.rrsig_memory = ""
        self.dnskey_objects = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Dnssec(A10BaseClass):
    
    """Class Description::
    Operational Status for the object dnssec.

    Class dnssec supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/dnssec/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "dnssec"
        self.a10_url="/axapi/v3/dnssec/oper"
        self.DeviceProxy = ""
        self.oper = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


