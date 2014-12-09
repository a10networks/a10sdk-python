from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param inechoreps: {"description": "In Echo replies", "format": "counter", "type": "number", "oid": "10", "optional": true, "size": "2"}
    :param outaddrmaskreps: {"description": "Out Address Mask Rep", "format": "counter", "type": "number", "oid": "27", "optional": true, "size": "2"}
    :param outtimestampreps: {"description": "Out Time Stamp Rep", "format": "counter", "type": "number", "oid": "25", "optional": true, "size": "2"}
    :param inechos: {"description": "In Echo requests", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "2"}
    :param num: {"description": "Total number", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "2"}
    :param intimestampreps: {"description": "In Timestamp Rep", "format": "counter", "type": "number", "oid": "12", "optional": true, "size": "2"}
    :param outechos: {"description": "Out Echo Requests", "format": "counter", "type": "number", "oid": "22", "optional": true, "size": "2"}
    :param inaddrmasks: {"description": "In Address Masks", "format": "counter", "type": "number", "oid": "13", "optional": true, "size": "2"}
    :param outsrcquenchs: {"description": "Out Source Quench Error", "format": "counter", "type": "number", "oid": "20", "optional": true, "size": "2"}
    :param inerrors: {"description": "In Errors", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "2"}
    :param inaddrmaskreps: {"description": "In Address Mask Rep", "format": "counter", "type": "number", "oid": "14", "optional": true, "size": "2"}
    :param outmsgs: {"description": "Out Message", "format": "counter", "type": "number", "oid": "15", "optional": true, "size": "2"}
    :param outtimestamps: {"description": "Out Time Stamp", "format": "counter", "type": "number", "oid": "24", "optional": true, "size": "2"}
    :param outaddrmasks: {"description": "Out Address Mask", "format": "counter", "type": "number", "oid": "26", "optional": true, "size": "2"}
    :param inparmprobs: {"description": "In Parameter Problem", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "2"}
    :param insrcquenchs: {"description": "In Source Quench Error", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "2"}
    :param inredirects: {"description": "In Redirects", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "2"}
    :param outerrors: {"description": "Out Errors", "format": "counter", "type": "number", "oid": "16", "optional": true, "size": "2"}
    :param inmsgs: {"description": "In Messages", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "2"}
    :param outtimeexcds: {"description": "Out TTL Exceeds", "format": "counter", "type": "number", "oid": "18", "optional": true, "size": "2"}
    :param outredirects: {"description": "Out Redirects", "format": "counter", "type": "number", "oid": "21", "optional": true, "size": "2"}
    :param indestunreachs: {"description": "In Destination Unreachable", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "2"}
    :param intimeexcds: {"description": "In TTL Exceeds", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "2"}
    :param outparmprobs: {"description": "Out Parameter Problem", "format": "counter", "type": "number", "oid": "19", "optional": true, "size": "2"}
    :param intimestamps: {"description": "In Timestamp", "format": "counter", "type": "number", "oid": "11", "optional": true, "size": "2"}
    :param outechoreps: {"description": "Out Echo Replies", "format": "counter", "type": "number", "oid": "23", "optional": true, "size": "2"}
    :param outdestunreachs: {"description": "Out Destination Unreachable", "format": "counter", "type": "number", "oid": "17", "optional": true, "size": "2"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.inechoreps = ""
        self.outaddrmaskreps = ""
        self.outtimestampreps = ""
        self.inechos = ""
        self.num = ""
        self.intimestampreps = ""
        self.outechos = ""
        self.inaddrmasks = ""
        self.outsrcquenchs = ""
        self.inerrors = ""
        self.inaddrmaskreps = ""
        self.outmsgs = ""
        self.outtimestamps = ""
        self.outaddrmasks = ""
        self.inparmprobs = ""
        self.insrcquenchs = ""
        self.inredirects = ""
        self.outerrors = ""
        self.inmsgs = ""
        self.outtimeexcds = ""
        self.outredirects = ""
        self.indestunreachs = ""
        self.intimeexcds = ""
        self.outparmprobs = ""
        self.intimestamps = ""
        self.outechoreps = ""
        self.outdestunreachs = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Icmp(A10BaseClass):
    
    """Class Description::
    Statistics for the object icmp.

    Class icmp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/system/icmp/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "icmp"
        self.a10_url="/axapi/v3/system/icmp/stats"
        self.DeviceProxy = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


