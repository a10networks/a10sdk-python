from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "port-requests", "eprt-requests", "lprt-requests", "pasv-replies", "epsv-replies", "lpsv-replies", "port-retransmits", "pasv-retransmits", "port-helper-created", "pasv-helper-created", "port-helper-freed", "pasv-helper-freed", "port-helper-unused", "pasv-helper-unused", "port-helper-creation-failure", "pasv-helper-creation-failure", "get-conn-ext-failure", "smp-app-type-mismatch"], "type": "string", "description": "'all': all; 'port-requests': PORT Requests From Client; 'eprt-requests': EPRT Requests From Client; 'lprt-requests': LPRT Requests From Client; 'pasv-replies': PASV Replies From Server; 'epsv-replies': EPSV Replies From Server; 'lpsv-replies': LPSV Replies From Server; 'port-retransmits': Port Mode Request Retransmits; 'pasv-retransmits': Passive Mode Reply Retransmits; 'port-helper-created': Port Mode Helper Created; 'pasv-helper-created': Passive Mode Helper Created; 'port-helper-freed': Port Mode Helper Freed; 'pasv-helper-freed': Passive Mode Helper Freed; 'port-helper-unused': Port Mode Helper Unused; 'pasv-helper-unused': Passive Mode Helper Unused; 'port-helper-creation-failure': Port Helper Creation Failure; 'pasv-helper-creation-failure': Passive Helper Creation Failure; 'get-conn-ext-failure': Get Conn Extension Failure; 'smp-app-type-mismatch': SMP ALG App Type Mismatch; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Ftp(A10BaseClass):
    
    """    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "port-requests", "eprt-requests", "lprt-requests", "pasv-replies", "epsv-replies", "lpsv-replies", "port-retransmits", "pasv-retransmits", "port-helper-created", "pasv-helper-created", "port-helper-freed", "pasv-helper-freed", "port-helper-unused", "pasv-helper-unused", "port-helper-creation-failure", "pasv-helper-creation-failure", "get-conn-ext-failure", "smp-app-type-mismatch"], "type": "string", "description": "'all': all; 'port-requests': PORT Requests From Client; 'eprt-requests': EPRT Requests From Client; 'lprt-requests': LPRT Requests From Client; 'pasv-replies': PASV Replies From Server; 'epsv-replies': EPSV Replies From Server; 'lpsv-replies': LPSV Replies From Server; 'port-retransmits': Port Mode Request Retransmits; 'pasv-retransmits': Passive Mode Reply Retransmits; 'port-helper-created': Port Mode Helper Created; 'pasv-helper-created': Passive Mode Helper Created; 'port-helper-freed': Port Mode Helper Freed; 'pasv-helper-freed': Passive Mode Helper Freed; 'port-helper-unused': Port Mode Helper Unused; 'pasv-helper-unused': Passive Mode Helper Unused; 'port-helper-creation-failure': Port Helper Creation Failure; 'pasv-helper-creation-failure': Passive Helper Creation Failure; 'get-conn-ext-failure': Get Conn Extension Failure; 'smp-app-type-mismatch': SMP ALG App Type Mismatch; ", "format": "enum"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Change Fixed NAT FTP ALG Settings.

    Class ftp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/fixed-nat/alg/ftp`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "ftp"
        self.a10_url="/axapi/v3/cgnv6/fixed-nat/alg/ftp"
        self.DeviceProxy = ""
        self.sampling_enable = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


