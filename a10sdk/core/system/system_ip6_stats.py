from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "inreceives", "inhdrerrors", "intoobigerrors", "innoroutes", "inaddrerrors", "inunknownprotos", "intruncatedpkts", "indiscards", "indelivers", "outforwdatagrams", "outrequests", "outdiscards", "outnoroutes", "reasmtimeout", "reasmreqds", "reasmoks", "reasmfails", "fragoks", "fragfails", "fragcreates", "inmcastpkts", "outmcastpkts"], "type": "string", "description": "'all': all; 'inreceives': inreceives; 'inhdrerrors': inhdrerrors; 'intoobigerrors': intoobigerrors; 'innoroutes': innoroutes; 'inaddrerrors': inaddrerrors; 'inunknownprotos': inunknownprotos; 'intruncatedpkts': intruncatedpkts; 'indiscards': indiscards; 'indelivers': indelivers; 'outforwdatagrams': outforwdatagrams; 'outrequests': outrequests; 'outdiscards': outdiscards; 'outnoroutes': outnoroutes; 'reasmtimeout': reasmtimeout; 'reasmreqds': reasmreqds; 'reasmoks': reasmoks; 'reasmfails': reasmfails; 'fragoks': fragoks; 'fragfails': fragfails; 'fragcreates': fragcreates; 'inmcastpkts': inmcastpkts; 'outmcastpkts': outmcastpkts; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Ip6Stats(A10BaseClass):
    
    """    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "inreceives", "inhdrerrors", "intoobigerrors", "innoroutes", "inaddrerrors", "inunknownprotos", "intruncatedpkts", "indiscards", "indelivers", "outforwdatagrams", "outrequests", "outdiscards", "outnoroutes", "reasmtimeout", "reasmreqds", "reasmoks", "reasmfails", "fragoks", "fragfails", "fragcreates", "inmcastpkts", "outmcastpkts"], "type": "string", "description": "'all': all; 'inreceives': inreceives; 'inhdrerrors': inhdrerrors; 'intoobigerrors': intoobigerrors; 'innoroutes': innoroutes; 'inaddrerrors': inaddrerrors; 'inunknownprotos': inunknownprotos; 'intruncatedpkts': intruncatedpkts; 'indiscards': indiscards; 'indelivers': indelivers; 'outforwdatagrams': outforwdatagrams; 'outrequests': outrequests; 'outdiscards': outdiscards; 'outnoroutes': outnoroutes; 'reasmtimeout': reasmtimeout; 'reasmreqds': reasmreqds; 'reasmoks': reasmoks; 'reasmfails': reasmfails; 'fragoks': fragoks; 'fragfails': fragfails; 'fragcreates': fragcreates; 'inmcastpkts': inmcastpkts; 'outmcastpkts': outmcastpkts; ", "format": "enum"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    IPv6 related statistics.

    Class ip6-stats supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/system/ip6-stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "ip6-stats"
        self.a10_url="/axapi/v3/system/ip6-stats"
        self.DeviceProxy = ""
        self.sampling_enable = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


