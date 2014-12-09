from a10sdk.common.A10BaseClass import A10BaseClass


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param state: {"enum": ["All-Up", "Functional-Up", "Partial-Up", "Down", "Disb", "Unkn"], "type": "string", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.state = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Port(A10BaseClass):
    
    """Class Description::
    Operational Status for the object port.

    Class port supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param protocol: {"enum": ["tcp", "udp", "others", "diameter", "dns-tcp", "dns-udp", "fast-http", "fix", "ftp", "ftp-proxy", "http", "https", "mlb", "mms", "mysql", "mssql", "radius", "rtsp", "sip", "sip-tcp", "sips", "smpp-tcp", "spdy", "spdys", "smtp", "ssl-proxy", "tcp-proxy", "tftp"], "description": "'tcp': TCP LB service; 'udp': UDP Port; 'others': for no tcp/udp protocol, do IP load balancing; 'diameter': diameter port; 'dns-tcp': DNS service over TCP; 'dns-udp': DNS service over UDP; 'fast-http': Fast HTTP Port; 'fix': FIX Port; 'ftp': File Transfer Protocol Port; 'ftp-proxy': ftp proxy port; 'http': HTTP Port; 'https': HTTPS port; 'mlb': Message based load balancing; 'mms': Microsoft Multimedia Service Port; 'mysql': mssql port; 'mssql': mssql; 'radius': Radius Port; 'rtsp': Real Time Streaming Protocol Port; 'sip': Session initiation protocol over UDP; 'sip-tcp': Session initiation protocol over TCP; 'sips': Session initiation protocol over TLS; 'smpp-tcp': SMPP service over TCP; 'spdy': spdy port; 'spdys': spdys port; 'smtp': SMTP Port; 'ssl-proxy': Generic SSL proxy; 'tcp-proxy': Generic TCP proxy; 'tftp': TFTP Port; ", "format": "enum", "type": "string", "oid": "1002", "optional": false}
    :param port_number: {"description": "Port", "format": "number", "optional": false, "oid": "1001", "maximum": 65534, "minimum": 0, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/virtual-server/{name}/port/{port_number}+{protocol}/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "port"
        self.a10_url="/axapi/v3/slb/virtual-server/{name}/port/{port_number}+{protocol}/oper"
        self.DeviceProxy = ""
        self.oper = {}
        self.protocol = ""
        self.port_number = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


