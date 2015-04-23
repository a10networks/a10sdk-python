from a10sdk.common.A10BaseClass import A10BaseClass


class Dnssec(A10BaseClass):
    
    """    :param standalone: {"default": 0, "optional": true, "type": "number", "description": "Run DNSSEC in standalone mode, in GSLB group mode by default", "format": "flag"}
    :param template_list: {"minItems": 1, "items": {"type": "template"}, "uniqueItems": true, "array": [{"required": ["dnssec-temp-name"], "properties": {"dnssec-template-ksk": {"type": "object", "properties": {"ksk-keysize-k": {"default": 0, "type": "number", "description": "Specify the number of bits in the DNSSEC KSK keys", "format": "flag"}, "zsk-rollover-time-v": {"description": "7 days less than the lifetime by default", "format": "number", "default": 358, "maximum": 3650, "minimum": 1, "type": "number"}, "ksk-lifetime-v": {"description": "Default value is 365 days", "minimum": 2, "type": "number", "maximum": 3650, "format": "number"}, "ksk-keysize-v": {"description": "Default size is 2048 and must be an exact multiple of 64", "minimum": 1024, "type": "number", "maximum": 4096, "format": "number"}, "ksk-rollover-time-k": {"default": 0, "type": "number", "description": "Set the rollover time in days", "format": "flag"}, "ksk-lifetime-k": {"default": 0, "type": "number", "description": "Set the lifetime for DNSSEC KSK keys in days", "format": "flag"}}}, "algorithm": {"optional": true, "enum": ["RSASHA1", "RSASHA256", "RSASHA512"], "type": "string", "description": "'RSASHA1': RSASHA1 algorithm; 'RSASHA256': RSASHA256 algorithm; 'RSASHA512': RSASHA512 algorithm; ", "format": "enum"}, "combinations-limit": {"description": "the max number of combinations per RRset (Default value is 31)", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": true}, "dnskey-ttl-k": {"default": 0, "optional": true, "type": "number", "description": "The TTL value of DNSKEY RR", "format": "flag"}, "signature-validity-period-k": {"default": 0, "optional": true, "type": "number", "description": "The period that a signature is valid", "format": "flag"}, "hsm": {"description": "specify the HSM template", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/hsm/template"}, "enable-nsec3": {"default": 0, "optional": true, "type": "number", "description": "enable NSEC3 support. disabled by default", "format": "flag"}, "return-nsec-on-failure": {"default": 1, "optional": true, "type": "number", "description": "return NSEC/NSEC3 or not on failure case. return by default", "format": "flag"}, "dnskey-ttl-v": {"description": "in seconds, 14400 seconds by default", "format": "number", "default": 14400, "optional": true, "maximum": 864000, "minimum": 1, "type": "number"}, "dnssec-temp-name": {"description": "DNSSEC Template Name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}, "signature-validity-period-v": {"description": "in days, 10 days by default", "format": "number", "default": 10, "optional": true, "maximum": 30, "minimum": 5, "type": "number"}, "dnssec-template-zsk": {"type": "object", "properties": {"zsk-keysize-v": {"description": "Default size is 2048 and must be an exact multiple of 64", "minimum": 1024, "type": "number", "maximum": 4096, "format": "number"}, "zsk-rollover-time-v": {"description": "7 days less than the lifetime by default", "format": "number", "default": 83, "maximum": 3650, "minimum": 1, "type": "number"}, "zsk-lifetime-v": {"description": "Default value is 90 days", "format": "number", "default": 90, "maximum": 3650, "minimum": 2, "type": "number"}, "zsk-lifetime-k": {"default": 0, "type": "number", "description": "Set the lifetime for DNSSEC ZSK keys in days", "format": "flag"}, "zsk-keysize-k": {"default": 0, "type": "number", "description": "Specify the number of bits in the DNSSEC ZSK keys", "format": "flag"}, "zsk-rollover-time-k": {"default": 0, "type": "number", "description": "Set the rollover time in days", "format": "flag"}}}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/dnssec/template/{dnssec-temp-name}"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Domain Name System Security Extensions commands.

    Class dnssec supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/dnssec`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "dnssec"
        self.a10_url="/axapi/v3/dnssec"
        self.DeviceProxy = ""
        self.key_rollover = {}
        self.standalone = ""
        self.sign_zone_now = {}
        self.dnskey = {}
        self.template_list = []
        self.ds = {}
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


