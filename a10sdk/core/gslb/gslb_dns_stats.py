from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param bad_header_query: {"description": "Number of queries with incorrect header", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "8"}
    :param total_response: {"description": "Total number of DNS replies sent to clients", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param bad_service_response: {"description": "Number of replies with unknown service", "format": "counter", "type": "number", "oid": "10", "optional": true, "size": "8"}
    :param bad_service_query: {"description": "Number of queries with unknown service", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "8"}
    :param bad_format_query: {"description": "Number of queries with incorrect format", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "8"}
    :param bad_packet_query: {"description": "Number of queries with incorrect data length", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
    :param total_query: {"description": "Total number of DNS queries received", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param no_answer: {"description": "Number of replies with unknown server IP", "format": "counter", "type": "number", "oid": "15", "optional": true, "size": "8"}
    :param bad_class_query: {"description": "Number of queries with incorrect class", "format": "counter", "type": "number", "oid": "11", "optional": true, "size": "8"}
    :param bad_type_query: {"description": "Number of queries with incorrect type", "format": "counter", "type": "number", "oid": "13", "optional": true, "size": "8"}
    :param bad_packet_response: {"description": "Number of replies with incorrect data length", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}
    :param bad_class_response: {"description": "Number of replies with incorrect class", "format": "counter", "type": "number", "oid": "12", "optional": true, "size": "8"}
    :param bad_format_response: {"description": "Number of replies with incorrect format", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "8"}
    :param bad_type_response: {"description": "Number of replies with incorrect type", "format": "counter", "type": "number", "oid": "14", "optional": true, "size": "8"}
    :param bad_header_response: {"description": "Number of replies with incorrect header", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.bad_header_query = ""
        self.total_response = ""
        self.bad_service_response = ""
        self.bad_service_query = ""
        self.bad_format_query = ""
        self.bad_packet_query = ""
        self.total_query = ""
        self.no_answer = ""
        self.bad_class_query = ""
        self.bad_type_query = ""
        self.bad_packet_response = ""
        self.bad_class_response = ""
        self.bad_format_response = ""
        self.bad_type_response = ""
        self.bad_header_response = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Dns(A10BaseClass):
    
    """Class Description::
    Statistics for the object dns.

    Class dns supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/dns/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "dns"
        self.a10_url="/axapi/v3/gslb/dns/stats"
        self.DeviceProxy = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


