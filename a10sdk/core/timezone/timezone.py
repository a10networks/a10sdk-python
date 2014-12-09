from a10sdk.common.A10BaseClass import A10BaseClass


class TimezoneIndexCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param timezone_index: {"enum": ["UTC", "Pacific/Midway", "Pacific/Honolulu", "America/Anchorage", "America/Tijuana", "America/Los_Angeles", "America/Vancouver", "America/Phoenix", "America/Shiprock", "America/Chicago", "America/Mexico_City", "America/Regina", "America/Swift_Current", "America/Kentucky/Monticello", "America/Indiana/Marengo", "America/Montreal", "America/New_York", "America/Toronto", "America/Caracas", "America/Halifax", "America/Santiago", "America/St_Johns", "America/Buenos_Aires", "America/Godthab", "America/Brasilia", "Atlantic/South_Georgia", "Atlantic/Azores", "Atlantic/Cape_Verde", "Europe/Dublin", "Africa/Algiers", "Europe/Amsterdam", "Europe/Belgrade", "Europe/Brussels", "Europe/Sarajevo", "Europe/Bucharest", "Africa/Cairo", "Europe/Athens", "Africa/Harare", "Asia/Jerusalem", "Europe/Helsinki", "Africa/Nairobi", "Asia/Baghdad", "Asia/Kuwait", "Europe/Moscow", "Asia/Tehran", "Asia/Baku", "Asia/Muscat", "Asia/Kabul", "Asia/Karachi", "Asia/Yekaterinburg", "Asia/Calcutta", "Asia/Katmandu", "Asia/Almaty", "Asia/Dhaka", "Indian/Chagos", "Asia/Rangoon", "Asia/Bangkok", "Asia/Krasnoyarsk", "Asia/Irkutsk", "Asia/Kuala_Lumpur", "Asia/Shanghai", "Asia/Taipei", "Australia/Perth", "Asia/Seoul", "Asia/Tokyo", "Asia/Yakutsk", "Australia/Adelaide", "Australia/Darwin", "Australia/Hobart", "Australia/Brisbane", "Asia/Vladivostok", "Australia/Sydney", "Pacific/Guam", "Asia/Magadan", "Pacific/Auckland", "Pacific/Fiji", "Pacific/Kwajalein", "Pacific/Enderbury"], "type": "string", "description": "'UTC': Coordinated Universal Time (UTC); 'Pacific/Midway': (GMT-11:00)Midway Island, Samoa; 'Pacific/Honolulu': (GMT-10:00)Hawaii; 'America/Anchorage': (GMT-09:00)Alaska; 'America/Tijuana': (GMT-08:00)Pacific Time - Tijuana; 'America/Los_Angeles': (GMT-08:00)Pacific Time(US & Canada); 'America/Vancouver': (GMT-08:00)Pacific Time - west British Columbia; 'America/Phoenix': (GMT-07:00)Arizona; 'America/Shiprock': (GMT-07:00)Mountain Time(US & Canada); 'America/Chicago': (GMT-06:00)Central Time(US & Canada); 'America/Mexico_City': (GMT-06:00)Mexico City; 'America/Regina': (GMT-06:00)Saskatchewan; 'America/Swift_Current': (GMT-06:00)Central America; 'America/Kentucky/Monticello': (GMT-05:00)Eastern Time(US & Canada); 'America/Indiana/Marengo': (GMT-05:00)Indiana(East); 'America/Montreal': (GMT-05:00)Eastern Time - Ontario & Quebec - most locations; 'America/New_York': (GMT-05:00)Eastern Time; 'America/Toronto': (GMT-05:00)Eastern Time - Toronto, Ontario; 'America/Caracas': (GMT-04:00)Caracas, La Paz; 'America/Halifax': (GMT-04:00)Atlantic Time(Canada); 'America/Santiago': (GMT-04:00)Santiago; 'America/St_Johns': (GMT-03:30)Newfoundland; 'America/Buenos_Aires': (GMT-03:00)Buenos Aires, Georgetown; 'America/Godthab': (GMT-03:00)Greenland; 'America/Brasilia': (GMT-03:00)Brasilia; 'Atlantic/South_Georgia': (GMT-02:00)Mid-Atlantic; 'Atlantic/Azores': (GMT-01:00)Azores; 'Atlantic/Cape_Verde': (GMT-01:00)Cape Verde Is.; 'Europe/Dublin': (GMT)Greenwich Mean Time: Dublin, Edinburgh, Lisbon, London; 'Africa/Algiers': (GMT+01:00)West Central Africa; 'Europe/Amsterdam': (GMT+01:00)Amsterdam, Berlin, Bern, Rome, Stockholm, Vienna; 'Europe/Belgrade': (GMT+01:00)Belgrade, Bratislava, Budapest, Ljubljana, Prague; 'Europe/Brussels': (GMT+01:00)Brussels, Copenhagen, Madrid, Paris; 'Europe/Sarajevo': (GMT+01:00)Sarajevo, Skopje, Sofija, Vilnius, Warsaw, Zagreb; 'Europe/Bucharest': (GMT+02:00)Bucharest; 'Africa/Cairo': (GMT+02:00)Cairo; 'Europe/Athens': (GMT+02:00)Athens, Istanbul, Minsk; 'Africa/Harare': (GMT+02:00)Harare, Pretoria; 'Asia/Jerusalem': (GMT+02:00)Jerusalem; 'Europe/Helsinki': (GMT+02:00)Helsinki, Riga, Tallinn; 'Africa/Nairobi': (GMT+03:00)Nairobi; 'Asia/Baghdad': (GMT+03:00)Baghdad; 'Asia/Kuwait': (GMT+03:00)Kuwait, Riyadh; 'Europe/Moscow': (GMT+03:00)Moscow, St.Petersburg, Volgogard; 'Asia/Tehran': (GMT+03:30)Tehran; 'Asia/Baku': (GMT+04:00)Baku, Tbilisi, Yerevan; 'Asia/Muscat': (GMT+04:00)Abu Dhabi, Muscat; 'Asia/Kabul': (GMT+04:30)Kabul; 'Asia/Karachi': (GMT+05:00)Islamabad, Karachi, Tashkent; 'Asia/Yekaterinburg': (GMT+05:00)Ekaterinburg; 'Asia/Calcutta': (GMT+05:30)Calcutta, Chennai, Mumbai, New Delhi; 'Asia/Katmandu': (GMT+05:45)Kathmandu; 'Asia/Almaty': (GMT+06:00)Almaty, Novosibirsk; 'Asia/Dhaka': (GMT+06:00)Astana, Dhaka; 'Indian/Chagos': (GMT+06:00)Sri Jayawardenepura; 'Asia/Rangoon': (GMT+06:30)Rangoon; 'Asia/Bangkok': (GMT+07:00)Bangkok, Hanoi, Jakarta; 'Asia/Krasnoyarsk': (GMT+07:00)Krasnoyarsk; 'Asia/Irkutsk': (GMT+08:00)Irkutsk, Ulaan Bataar; 'Asia/Kuala_Lumpur': (GMT+08:00)Kuala Lumpur, Singapore; 'Asia/Shanghai': (GMT+08:00)Beijing, Chongqing, Hong Kong, Urumqi; 'Asia/Taipei': (GMT+08:00)Taipei; 'Australia/Perth': (GMT+08:00)Perth; 'Asia/Seoul': (GMT+09:00)Seoul; 'Asia/Tokyo': (GMT+09:00)Osaka, Sapporo, Tokyo; 'Asia/Yakutsk': (GMT+09:00)Yakutsk; 'Australia/Adelaide': (GMT+09:30)Adelaide; 'Australia/Darwin': (GMT+09:30)Darwin; 'Australia/Hobart': (GMT+10:00)Hobart; 'Australia/Brisbane': (GMT+10:00)Brisbane; 'Asia/Vladivostok': (GMT+10:00)Vladivostok; 'Australia/Sydney': (GMT+10:00)Canberra, Melbourne, Sydney; 'Pacific/Guam': (GMT+10:00)Guam, Port Moresby; 'Asia/Magadan': (GMT+11:00)Magadan, Solomon., New Caledonia; 'Pacific/Auckland': (GMT+12:00)Auckland, Wellington; 'Pacific/Fiji': (GMT+12:00)Fiji, Kamchatka, Marshall Is.; 'Pacific/Kwajalein': (GMT+12:00)Eniwetok, Kwajalein; 'Pacific/Enderbury': (GMT+13:00)Nuku'alofa; ", "format": "enum"}
    :param nodst: {"default": 0, "type": "number", "description": "Disable daylight saving time", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "timezone-index-cfg"
        self.DeviceProxy = ""
        self.timezone_index = ""
        self.nodst = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Timezone(A10BaseClass):
    
    """Class Description::
    Configure the Time Zone.

    Class timezone supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/timezone`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "timezone"
        self.a10_url="/axapi/v3/timezone"
        self.DeviceProxy = ""
        self.timezone_index_cfg = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


