from a10sdk.common.A10BaseClass import A10BaseClass


class Pki(A10BaseClass):
    
    """Class Description::
    PKI Commands.

    Class pki supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param scep_cert_list: {"minItems": 1, "items": {"type": "scep-cert"}, "uniqueItems": true, "array": [{"required": ["name"], "properties": {"dn": {"description": "Specify the Distinguished-Name to use while enrolling the certificate (Format: \"cn=user, dc=example, dc=com\")", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 127, "type": "string"}, "enroll": {"default": 0, "optional": true, "type": "number", "description": "Initiates enrollment of device with the CA", "format": "flag"}, "renew-before-value": {"description": "Value of renewal period", "format": "number", "type": "number", "maximum": 255, "minimum": 1, "optional": true}, "name": {"description": "Specify Certificate name to be enrolled", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}, "renew-every-type": {"optional": true, "enum": ["minute", "hour", "day", "week", "month"], "type": "string", "description": "'minute': Number of minute before cert expiry; 'hour': Number of hour before cert expiry; 'day': Number of day before cert expiry; 'week': Number of week before cert expiry; 'month': Number of month before cert expiry; ", "format": "enum"}, "url": {"description": "Specify the Enrollment Agent's absolute URL (Format: http://host/path)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 255, "type": "string"}, "encrypted": {"optional": true, "type": "encrypted", "description": "Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED secret string)", "format": "encrypted"}, "max-polltime": {"description": "Maximum time in seconds to poll when SCEP response is PENDING (default 180)", "format": "number", "type": "number", "maximum": 432000, "minimum": 15, "optional": true}, "interval": {"description": "Interval time in seconds to poll when SCEP response is PENDING (default 5)", "format": "number", "default": 5, "optional": true, "maximum": 3600, "minimum": 1, "type": "number"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "log-level": {"description": "level for logging output of scepclient commands(default 1 and detailed 4)", "format": "number", "type": "number", "maximum": 4, "minimum": 1, "optional": true}, "renew-before-type": {"optional": true, "enum": ["hour", "day", "week", "month"], "type": "string", "description": "'hour': Number of hour before cert expiry; 'day': Number of day before cert expiry; 'week': Number of week before cert expiry; 'month': Number of month before cert expiry; ", "format": "enum"}, "renew-every-value": {"description": "Value of renewal period", "format": "number", "type": "number", "maximum": 255, "minimum": 1, "optional": true}, "renew-every": {"description": "Specify interval before certificate expiry to renew the certificate", "format": "flag", "default": 0, "optional": true, "not": "renew-before", "type": "number"}, "method": {"optional": true, "enum": ["GET", "POST"], "type": "string", "description": "'GET': GET request; 'POST': POST request; ", "format": "enum"}, "password": {"default": 0, "optional": true, "type": "number", "description": "Specify the password used to enroll the device's certificate", "format": "flag"}, "key-length": {"description": "'1024': Key size 1024 bits; '2048': Key size 2048 bits(default); '4096': Key size 4096 bits; '8192': Key size 8192 bits; ", "format": "enum", "default": "2048", "type": "string", "enum": ["1024", "2048", "4096", "8192"], "optional": true}, "renew-before": {"description": "Specify interval before certificate expiry to renew the certificate", "format": "flag", "default": 0, "optional": true, "not": "renew-every", "type": "number"}, "secret-string": {"description": "secret password", "format": "password", "minLength": 1, "optional": true, "maxLength": 127, "type": "string"}, "subject-alternate-name": {"type": "object", "properties": {"san-value": {"minLength": 1, "maxLength": 127, "type": "string", "description": "Value of subject-alternate-name", "format": "string-rlx"}, "san-type": {"enum": ["email", "dns", "ip"], "type": "string", "description": "'email': Enter e-mail address of the subject; 'dns': Enter hostname of the subject; 'ip': Enter IP address of the subject; ", "format": "enum"}}}}}], "type": "array", "$ref": "/axapi/v3/pki/scep-cert/{name}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/pki`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "pki"
        self.a10_url="/axapi/v3/pki"
        self.DeviceProxy = ""
        self.delete_oper = {}
        self.A10WW_copy_key = {}
        self.A10WW_copy_cert = {}
        self.create_oper = {}
        self.scep_cert_list = []
        self.delete = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


