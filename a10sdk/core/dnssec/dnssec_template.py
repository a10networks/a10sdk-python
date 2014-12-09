from a10sdk.common.A10BaseClass import A10BaseClass


class DnssecTemplateKsk(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ksk_keysize_k: {"default": 0, "type": "number", "description": "Specify the number of bits in the DNSSEC KSK keys", "format": "flag"}
    :param zsk_rollover_time_v: {"description": "7 days less than the lifetime by default", "format": "number", "default": 358, "maximum": 3650, "minimum": 1, "type": "number"}
    :param ksk_lifetime_v: {"description": "Default value is 365 days", "minimum": 2, "type": "number", "maximum": 3650, "format": "number"}
    :param ksk_keysize_v: {"description": "Default size is 2048 and must be an exact multiple of 64", "minimum": 1024, "type": "number", "maximum": 4096, "format": "number"}
    :param ksk_rollover_time_k: {"default": 0, "type": "number", "description": "Set the rollover time in days", "format": "flag"}
    :param ksk_lifetime_k: {"default": 0, "type": "number", "description": "Set the lifetime for DNSSEC KSK keys in days", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "dnssec-template-ksk"
        self.DeviceProxy = ""
        self.ksk_keysize_k = ""
        self.zsk_rollover_time_v = ""
        self.ksk_lifetime_v = ""
        self.ksk_keysize_v = ""
        self.ksk_rollover_time_k = ""
        self.ksk_lifetime_k = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class DnssecTemplateZsk(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param zsk_keysize_v: {"description": "Default size is 2048 and must be an exact multiple of 64", "minimum": 1024, "type": "number", "maximum": 4096, "format": "number"}
    :param zsk_rollover_time_v: {"description": "7 days less than the lifetime by default", "format": "number", "default": 83, "maximum": 3650, "minimum": 1, "type": "number"}
    :param zsk_lifetime_v: {"description": "Default value is 90 days", "format": "number", "default": 90, "maximum": 3650, "minimum": 2, "type": "number"}
    :param zsk_lifetime_k: {"default": 0, "type": "number", "description": "Set the lifetime for DNSSEC ZSK keys in days", "format": "flag"}
    :param zsk_keysize_k: {"default": 0, "type": "number", "description": "Specify the number of bits in the DNSSEC ZSK keys", "format": "flag"}
    :param zsk_rollover_time_k: {"default": 0, "type": "number", "description": "Set the rollover time in days", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "dnssec-template-zsk"
        self.DeviceProxy = ""
        self.zsk_keysize_v = ""
        self.zsk_rollover_time_v = ""
        self.zsk_lifetime_v = ""
        self.zsk_lifetime_k = ""
        self.zsk_keysize_k = ""
        self.zsk_rollover_time_k = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Template(A10BaseClass):
    
    """Class Description::
    template Settings.

    Class template supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param algorithm: {"optional": true, "enum": ["RSASHA1", "RSASHA256", "RSASHA512"], "type": "string", "description": "'RSASHA1': RSASHA1 algorithm; 'RSASHA256': RSASHA256 algorithm; 'RSASHA512': RSASHA512 algorithm; ", "format": "enum"}
    :param combinations_limit: {"description": "the max number of combinations per RRset (Default value is 31)", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": true}
    :param dnskey_ttl_k: {"default": 0, "optional": true, "type": "number", "description": "The TTL value of DNSKEY RR", "format": "flag"}
    :param signature_validity_period_k: {"default": 0, "optional": true, "type": "number", "description": "The period that a signature is valid", "format": "flag"}
    :param hsm: {"description": "specify the HSM template", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/hsm/template"}
    :param enable_nsec3: {"default": 0, "optional": true, "type": "number", "description": "enable NSEC3 support. disabled by default", "format": "flag"}
    :param return_nsec_on_failure: {"default": 1, "optional": true, "type": "number", "description": "return NSEC/NSEC3 or not on failure case. return by default", "format": "flag"}
    :param dnskey_ttl_v: {"description": "in seconds, 14400 seconds by default", "format": "number", "default": 14400, "optional": true, "maximum": 864000, "minimum": 1, "type": "number"}
    :param dnssec_temp_name: {"description": "DNSSEC Template Name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param signature_validity_period_v: {"description": "in days, 10 days by default", "format": "number", "default": 10, "optional": true, "maximum": 30, "minimum": 5, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/dnssec/template/{dnssec_temp_name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "dnssec_temp_name"]

        self.b_key = "template"
        self.a10_url="/axapi/v3/dnssec/template/{dnssec_temp_name}"
        self.DeviceProxy = ""
        self.dnssec_template_ksk = {}
        self.algorithm = ""
        self.combinations_limit = ""
        self.dnskey_ttl_k = ""
        self.signature_validity_period_k = ""
        self.hsm = ""
        self.enable_nsec3 = ""
        self.return_nsec_on_failure = ""
        self.dnskey_ttl_v = ""
        self.dnssec_temp_name = ""
        self.signature_validity_period_v = ""
        self.dnssec_template_zsk = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


