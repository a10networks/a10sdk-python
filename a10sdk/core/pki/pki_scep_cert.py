from a10sdk.common.A10BaseClass import A10BaseClass


class SubjectAlternateName(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param san_value: {"minLength": 1, "maxLength": 127, "type": "string", "description": "Value of subject-alternate-name", "format": "string-rlx"}
    :param san_type: {"enum": ["email", "dns", "ip"], "type": "string", "description": "'email': Enter e-mail address of the subject; 'dns': Enter hostname of the subject; 'ip': Enter IP address of the subject; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "subject-alternate-name"
        self.DeviceProxy = ""
        self.san_value = ""
        self.san_type = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class ScepCert(A10BaseClass):
    
    """Class Description::
    SCEP Certificate enrollment object.

    Class scep-cert supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param dn: {"description": "Specify the Distinguished-Name to use while enrolling the certificate (Format: \"cn=user, dc=example, dc=com\")", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 127, "type": "string"}
    :param enroll: {"default": 0, "optional": true, "type": "number", "description": "Initiates enrollment of device with the CA", "format": "flag"}
    :param renew_before_value: {"description": "Value of renewal period", "format": "number", "type": "number", "maximum": 255, "minimum": 1, "optional": true}
    :param name: {"description": "Specify Certificate name to be enrolled", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param renew_every_type: {"optional": true, "enum": ["minute", "hour", "day", "week", "month"], "type": "string", "description": "'minute': Number of minute before cert expiry; 'hour': Number of hour before cert expiry; 'day': Number of day before cert expiry; 'week': Number of week before cert expiry; 'month': Number of month before cert expiry; ", "format": "enum"}
    :param url: {"description": "Specify the Enrollment Agent's absolute URL (Format: http://host/path)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 255, "type": "string"}
    :param encrypted: {"optional": true, "type": "encrypted", "description": "Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED secret string)", "format": "encrypted"}
    :param max_polltime: {"description": "Maximum time in seconds to poll when SCEP response is PENDING (default 180)", "format": "number", "type": "number", "maximum": 432000, "minimum": 15, "optional": true}
    :param interval: {"description": "Interval time in seconds to poll when SCEP response is PENDING (default 5)", "format": "number", "default": 5, "optional": true, "maximum": 3600, "minimum": 1, "type": "number"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param log_level: {"description": "level for logging output of scepclient commands(default 1 and detailed 4)", "format": "number", "type": "number", "maximum": 4, "minimum": 1, "optional": true}
    :param renew_before_type: {"optional": true, "enum": ["hour", "day", "week", "month"], "type": "string", "description": "'hour': Number of hour before cert expiry; 'day': Number of day before cert expiry; 'week': Number of week before cert expiry; 'month': Number of month before cert expiry; ", "format": "enum"}
    :param renew_every_value: {"description": "Value of renewal period", "format": "number", "type": "number", "maximum": 255, "minimum": 1, "optional": true}
    :param renew_every: {"description": "Specify interval before certificate expiry to renew the certificate", "format": "flag", "default": 0, "optional": true, "not": "renew-before", "type": "number"}
    :param method: {"optional": true, "enum": ["GET", "POST"], "type": "string", "description": "'GET': GET request; 'POST': POST request; ", "format": "enum"}
    :param password: {"default": 0, "optional": true, "type": "number", "description": "Specify the password used to enroll the device's certificate", "format": "flag"}
    :param key_length: {"description": "'1024': Key size 1024 bits; '2048': Key size 2048 bits(default); '4096': Key size 4096 bits; '8192': Key size 8192 bits; ", "format": "enum", "default": "2048", "type": "string", "enum": ["1024", "2048", "4096", "8192"], "optional": true}
    :param renew_before: {"description": "Specify interval before certificate expiry to renew the certificate", "format": "flag", "default": 0, "optional": true, "not": "renew-every", "type": "number"}
    :param secret_string: {"description": "secret password", "format": "password", "minLength": 1, "optional": true, "maxLength": 127, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/pki/scep-cert/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "scep-cert"
        self.a10_url="/axapi/v3/pki/scep-cert/{name}"
        self.DeviceProxy = ""
        self.dn = ""
        self.enroll = ""
        self.renew_before_value = ""
        self.name = ""
        self.renew_every_type = ""
        self.url = ""
        self.encrypted = ""
        self.max_polltime = ""
        self.interval = ""
        self.uuid = ""
        self.log_level = ""
        self.renew_before_type = ""
        self.renew_every_value = ""
        self.renew_every = ""
        self.method = ""
        self.password = ""
        self.key_length = ""
        self.renew_before = ""
        self.secret_string = ""
        self.subject_alternate_name = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


