from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param fullcone_created_previous_epoch_first: {"optional": true, "size": "8", "type": "number", "oid": "5", "format": "counter"}
    :param fullcone_created_previous_epoch_last: {"optional": true, "size": "8", "type": "number", "oid": "8", "format": "counter"}
    :param data_sessions_previous_epoch_first: {"optional": true, "size": "8", "type": "number", "oid": "4", "format": "counter"}
    :param user_quote_created_current_epoch: {"optional": true, "size": "8", "type": "number", "oid": "3", "format": "counter"}
    :param user_quote_created_previous_epoch_first: {"optional": true, "size": "8", "type": "number", "oid": "6", "format": "counter"}
    :param user_quote_created_previous_epoch_last: {"optional": true, "size": "8", "type": "number", "oid": "9", "format": "counter"}
    :param fullcone_created_current_epoch: {"optional": true, "size": "8", "type": "number", "oid": "2", "format": "counter"}
    :param data_sessions_previous_epoch_last: {"optional": true, "size": "8", "type": "number", "oid": "7", "format": "counter"}
    :param data_sessions_current_epoch: {"optional": true, "size": "8", "type": "number", "oid": "1", "format": "counter"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.fullcone_created_previous_epoch_first = ""
        self.fullcone_created_previous_epoch_last = ""
        self.data_sessions_previous_epoch_first = ""
        self.user_quote_created_current_epoch = ""
        self.user_quote_created_previous_epoch_first = ""
        self.user_quote_created_previous_epoch_last = ""
        self.fullcone_created_current_epoch = ""
        self.data_sessions_previous_epoch_last = ""
        self.data_sessions_current_epoch = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Performance(A10BaseClass):
    
    """Class Description::
    Statistics for the object performance.

    Class performance supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/lsn/performance/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "performance"
        self.a10_url="/axapi/v3/cgnv6/lsn/performance/stats"
        self.DeviceProxy = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


