from a10sdk.common.A10BaseClass import A10BaseClass


class Method(A10BaseClass):
    
    """Class Description::
    Define the health method object, default is ICMP.

    Class method supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/health/monitor/{name}/method`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "method"
        self.a10_url="/axapi/v3/health/monitor/{name}/method"
        self.DeviceProxy = ""
        self.ftp = {}
        self.udp = {}
        self.sip = {}
        self.http = {}
        self.https = {}
        self.compound = {}
        self.database = {}
        self.smtp = {}
        self.ntp = {}
        self.rtsp = {}
        self.snmp = {}
        self.tcp = {}
        self.pop3 = {}
        self.radius = {}
        self.external = {}
        self.dns = {}
        self.ldap = {}
        self.icmp = {}
        self.kerberos_kdc = {}
        self.imap = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


