__author__ = 'mthompson'
import copy
import inspect
import importlib
import urllib
import json
from urlparse import urlparse
import collections
import re
import os
import keyword

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class A10BaseClass(object):
    is_POST = True

    def __init__(self):
        self.ERROR_MSG = ""

    @classmethod
    def __json__(self, class_object, **kwargs):
        try:
            temp_require = copy.deepcopy(class_object.required)
            del class_object.required
        except:
            pass
        try:
            dp = copy.deepcopy(class_object.DeviceProxy)
            delattr(class_object, "DeviceProxy")
        except:
            pass
        json_object = self.Obj_to_json(class_object.__dict__)

        if 'a10-url' in json_object:
            del json_object['a10-url']
        if "b-key" in json_object:
            del json_object['b-key']

        debug_keys = ["DEBUG-CONNECTION", "DEBUG-Payload", "DEBUG-Response", "DEBUG-URL", "DEBUG-headers"]
        for d_keys in debug_keys:
            try:
                del json_object[d_keys]

            except:
                try:
                    del json_object[class_object.b_key][d_keys]
                except:
                    pass

        try:
            class_object.__setattr__("DeviceProxy", dp)
        except:
            pass
        #(Raunak):json_object is None or empty dictionary return None
        try:
            class_object.__setattr__("required", temp_require)
        except:
            pass
        if not json_object:
            return ''
        elif "sub" in kwargs and kwargs['sub'] == 0:
            return json_object
        else:
            r_object = {}
            r_object[class_object.b_key] = json_object
            return r_object

    @classmethod
    def Obj_to_json(self, obj):
        new_obj = {}
        for k, v in obj.items():
            key = k.replace("_", "-").replace("A10WW_", "").replace(
                "A10WW-", "")
            if "class" in str(type(v)):
                json_obj = self.__json__(v)
                #(Raunak):If the response exists update the new_obj dictionary
                #with the json data
                if json_obj:
                    new_obj.update(json_obj)

            elif (isinstance(v, dict) or
                      isinstance(v, unicode) or
                      isinstance(v, str) or
                      isinstance(v, list)) and len(v) != 0:

                if isinstance(v, list):
                    temp_list = []
                    if len(v) != 0:
                        for i in v:
                            temp_list.append(i.__json__(i, sub=0))

                        new_obj[key] = temp_list

                elif isinstance(v, dict) and len(v) != 0:
                    new_obj[key] = self.Obj_to_json(v)
                elif v is True:
                    new_obj[key] = "1"
                elif v is False:
                    new_obj[key] = "0"
                elif v is not None:
                    if len(v) != 0:
                        new_obj[key] = v
            elif isinstance(v, int):
                new_obj[key] = v

            # If it's an attribute and it's value is None, use None
            # (grao): adding null value attributes only when POST (avoiding for PUT)
            elif v is None and A10BaseClass.is_POST:
                new_obj[key] = v

        return new_obj

    '''
    Converts from Unicode
    '''

    def convert(self, data):
        if isinstance(data, basestring):
            return str(data)
        elif isinstance(data, collections.Mapping):
            return dict(map(self.convert, data.iteritems()))
        elif isinstance(data, collections.Iterable):
            return type(data)(map(self.convert, data))
        else:
            return data

    """
    GET THE PARENT KEY ASS NEEDED
    """

    def find_key(self, d, key):
        for k, v in d.items():
            if isinstance(v, dict):
                p = self.find_key(v, key)
                if p:
                    return [k] + p
            elif v == key:
                return [k]

    def _format_key_name_for_module_lookup(self, key, lambda_expression):
        if key.startswith('A10WW_'):
            return lambda_expression(key)
        else:
            return lambda_expression(key).title()


    def _search_for_child_object_module(self, caller, sub_class):
        try:
            if caller.__name__.endswith('_oper'):
                module_name = caller.__name__.replace('_oper', '')
                caller_name = importlib.import_module(module_name + "_" + sub_class.lower() + "_oper")
            elif caller.__name__.endswith('_stats'):
                module_name = caller.__name__.replace('_stats', '')
                caller_name = importlib.import_module(module_name + "_" + sub_class.lower() + "_stats")
            else:
                caller_name = importlib.import_module(caller.__name__ + "_" + sub_class.lower())
        except:
            caller_name = importlib.import_module(caller.__name__)

        return caller_name

    def _search_for_child_class_inside_module(self, child_node_name, caller_name, DeviceProxy):
        k = child_node_name
        sub_class = ''.join(
            x for x in k.replace("-list", "", 1).replace("-", "_").title() if
            not x.isspace())
        try:
            obj_class = getattr(caller_name, sub_class)(DeviceProxy=DeviceProxy)
        except:
            try:
                sub_class = ''.join(
                    x for x in k.replace("-", " ").replace("-list", "", 1).title()
                    if not x.isspace())
                obj_class = getattr(caller_name, sub_class)(DeviceProxy=DeviceProxy)
            except:
                try:
                    sub_class = ''.join(x for x in
                                        k.replace("-", "").replace("list", "").replace("list",
                                                                                       "").title()
                                        if not x.isspace())
                    obj_class = getattr(caller_name, sub_class)(DeviceProxy=DeviceProxy)
                except:
                    try:
                        sub_class = ''.join(x for x in
                                            k.replace("-", "_").replace("list", "").replace("list",
                                                                                            "").title()
                                            if not x.isspace())
                        obj_class = getattr(caller_name, sub_class)(DeviceProxy=DeviceProxy)
                    except:
                        #(RAUNAK):Added one more check for the VLAN tagged_ethernet_list like cases
                        #Would check for the class with the name TaggedEthernet
                        try:
                            sub_class = ''.join(x for x in
                                                k.replace("-", "_").replace("list", "").replace(
                                                    "list",
                                                    "").title().replace('_', '')
                                                if not x.isspace())
                            obj_class = getattr(caller_name, sub_class)(DeviceProxy=DeviceProxy)
                        except:
                            #(Raunak):Added this for ClassList
                            try:
                                sub_class = ''.join(x for x in
                                                    k.replace("-list", "").title() + 'List'
                                                    if not x.isspace())
                                obj_class = getattr(caller_name, sub_class)(DeviceProxy=DeviceProxy)
                            except:
                                pass

        return obj_class


    def Factory(self, DeviceProxy, obj, name, parent=''):

        obj = self.convert(obj)

        # for i in obj:
        #     self.default_object_key = i

        if parent:
            caller = inspect.getmodule(parent)
        else:
            caller = inspect.getmodule(self)
        top_node_obj_list = []
        for list_name_key, list_name_value in obj.items():
            if list_name_key == 'class-list-list':
                class_object = 'ClassList'
                break
            else:
                class_object = ''.join(
                    x for x in list_name_key.replace("-", " ").replace(
                        "list", "").title() if not x.isspace())
                if not class_object:
                    class_object = ''.join(
                        x for x in list_name_key.replace("-", " ").title() if not x.isspace())

                class_object = kwbl().kwbl(class_object)
            try:
                caller = importlib.import_module(caller.__name__)
                new_class = getattr(caller, class_object)(DeviceProxy=DeviceProxy)

            except:
                try:
                    caller = importlib.import_module(caller.__name__)
                    new_class = getattr(caller, class_object + 'List')(DeviceProxy=DeviceProxy)
                except:
                    try:
                        caller = importlib.import_module(caller.__name__ + "_" + list_name_key.lower())
                        new_class = getattr(caller, class_object)(DeviceProxy=DeviceProxy)

                    except:

                        try:
                            caller = importlib.import_module(
                                caller.__name__ + "_" + list_name_key.replace('-', '_').lower())
                            new_class = getattr(caller, class_object)(DeviceProxy=DeviceProxy)

                        except:
                            try:
                                temp_name = list_name_key.split("-")
                                test_module = temp_name[0]
                                caller = importlib.import_module(caller.__name__ + "_" + test_module.lower())
                                new_class = getattr(caller, class_object)(DeviceProxy=DeviceProxy)
                            except:
                                try:
                                    caller = importlib.import_module(
                                        caller.__name__ + "_" + parent.lower() + "_" + list_name_key.lower())
                                    new_class = getattr(caller, class_object)(DeviceProxy=DeviceProxy)

                                except:
                                    try:
                                        caller = importlib.import_module(caller.__name__ + "_" + parent.lower())
                                        new_class = getattr(caller, class_object)(DeviceProxy=DeviceProxy)

                                    except Exception as e:
                                        try:
                                            # try to import class from all sibling modules
                                            found_in_sibling = False
                                            for module in os.listdir(os.path.dirname(caller.__file__)):
                                                if module.endswith("py") and module != "__init__.py":
                                                    try:
                                                        class_name = ''.join(
                                                            x for x in list_name_key.split("-").pop().title() if
                                                            not x.isspace())
                                                        caller_sibling_modules = importlib.import_module(
                                                            "." + module.replace(".py", ""), caller.__package__)
                                                        new_class = getattr(caller_sibling_modules, class_name)(
                                                            DeviceProxy=DeviceProxy)
                                                        found_in_sibling = True
                                                        break
                                                    except:
                                                        try:
                                                            class_name = ''.join(
                                                                x for x in list_name_key.replace("-", " ").title() if
                                                                not x.isspace())
                                                            caller_sibling_modules = importlib.import_module(
                                                                "." + module.replace(".py", ""), caller.__package__)
                                                            new_class = getattr(caller_sibling_modules, class_name)(
                                                                DeviceProxy=DeviceProxy)
                                                            found_in_sibling = True
                                                            break
                                                        except:
                                                            pass
                                                        pass
                                            if found_in_sibling is False:
                                                raise e
                                        except:
                                            return obj

            # class_object
            if isinstance(list_name_value, list):
                for list_obj in list_name_value:
                    sdk_obj = copy.deepcopy(new_class)

                    for k, v in list_obj.items():
                        k = kwbl().kwbl(k)
                        new_obj_name = k.replace("-list", "", 1).replace("-", "_")
                        if new_obj_name[len(new_obj_name) - 1] == "_":
                            new_obj_name = ''.join(
                                x for x in k.replace("-", " ").replace("-list", "", 1).title() if
                                not x.isspace())

                        if isinstance(v, list):
                            obj_name_list = []
                            caller_name = self._search_for_child_object_module(caller, new_obj_name)
                            for keys in v:
                                obj_class = self._search_for_child_class_inside_module(k, caller_name, DeviceProxy)
                                # obj_class = getattr(caller_name, new_obj_name)(DeviceProxy=DeviceProxy)
                                for v_key, v_val in keys.items():
                                    v_key = kwbl().kwbl(v_key)
                                    if v_key == "a10-url":
                                        temp_v = urlparse(v_val)
                                        v_val = temp_v.path
                                    obj_class.__setattr__(v_key.replace("-", "_"), v_val)
                                obj_name_list.append(obj_class)
                            sdk_obj.__setattr__(k.replace("-", "_"), obj_name_list)
                        elif isinstance(v, dict):
                            sdk_obj.__setattr__(k.replace("-", "_"),
                                                  (sdk_obj.Factory(DeviceProxy, {k: v}, k, sdk_obj)))
                        else:
                            sdk_obj.__setattr__(new_obj_name.replace("-", "_"), v)
                    top_node_obj_list.append(copy.deepcopy(sdk_obj))
            else:
                with_native_list_in_name = ['access-list', 'ip-map-list', 'acl-id-list-list', 'acl-name-list-list',
                                            'lsn-rule-list',
                                            'inside-src-permit-list', 'nat-ip-list', 'inside-ip-list', 'ipv4-list']
                for k, v in list_name_value.items():
                    k = kwbl().kwbl(k)
                    if k == "a10-url":
                        temp_v = urlparse(v)
                        v = temp_v.path

                    if k in with_native_list_in_name:
                        new_obj_name = with_native_list_in_name[with_native_list_in_name.index(k)].replace('-', '_')
                        # Bug 191464  Mike Thompson detecting type vs name.
                    elif not isinstance(v, list):
                        new_obj_name = k.replace("-", "_")
                    else:
                        new_obj_name = k.replace("-list", "", 1).replace("-", "_") if k.endswith('list') else k.replace(
                            "-", "_")

                    if isinstance(v, list):
                        obj_name_list = []
                        caller_name = self._search_for_child_object_module(caller, new_obj_name)
                        for keys in v:
                            obj_class = self._search_for_child_class_inside_module(k, caller_name, DeviceProxy)
                            for v_key, v_val in keys.items():
                                v_key = kwbl().kwbl(v_key)
                                if v_key == "a10-url":
                                    temp_v = urlparse(v_val)
                                    v_val = temp_v.path
                                elif isinstance(v_val, dict):
                                    obj_class.__setattr__(v_key.replace("-", "_"), (
                                        obj_class.Factory(DeviceProxy, {v_key: v_val}, v_key, obj_class)))
                                    continue
                                elif isinstance(v_val, list):
                                    sub_obj = obj_class.Factory(DeviceProxy, {v_key: v_val}, v_key, obj_class)
                                    sub_obj_list = getattr(obj_class, v_key, [])
                                    if isinstance(sub_obj, list):
                                        sub_obj_list = sub_obj_list + sub_obj
                                    else:
                                        sub_obj_list.append(sub_obj)
                                    setattr(obj_class, v_key.replace("-", "_"), sub_obj_list)
                                    continue

                                obj_class.__setattr__(v_key.replace("-", "_"), v_val)

                            obj_name_list.append(obj_class)

                        new_class.__setattr__(k.replace("-", "_"), copy.deepcopy(obj_name_list))

                    elif isinstance(v, dict):
                        new_class.__setattr__(new_obj_name, (new_class.Factory(DeviceProxy, {k: v}, k, new_class)))
                    else:
                        new_class.__setattr__(new_obj_name, v)
            try:
                if top_node_obj_list and len(top_node_obj_list) > 0:
                    return top_node_obj_list
                else:
                    return new_class
            except:
                pass

    def depth_finder(self, d, depth=0):

        if isinstance(d, list):
            if not isinstance(d, dict) or not d or not isinstance(d, list):
                return depth
            elif isinstance(d, dict):
                depth

        if not isinstance(d, dict) or not d:
            return depth

        return max(self.depth_finder(v, depth + 1) for k, v in d.iteritems())


    def get(self, query_params=None, **kwargs):
        if len(kwargs) > 0:
            self.a10_url_update(**kwargs)
        else:
            self.a10_url_parent()
        request = self.DeviceProxy.GET(self, query_params)
        try:
            #Hack decode unicode something:zli, bug:237218
            hack = kwargs.get("json_before_load", None)
            if hack and callable(hack):
                try:
                    request = hack(request)
                except:
                    pass
            request = json.loads(request, encoding='utf-8')
        except:
            if request is None:
                self.ERROR_MSG = "None Returned"
                return self
            elif 'response' in request and request['response']['err']:
                self.ERROR_MSG = request
                return self
            elif "Session Timeout" in request:
                self.ERROR_MSG = request
                return self

        if request is None:
            self.ERROR_MSG = "None Returned"
            return self
        elif not isinstance(request, dict):
            self.ERROR_MSG = 'Invalid Response'
            return self
        # elif 'response' in request and request['response']['err']:
        elif 'response' in request and request.get('response').get('err', None):
            self.ERROR_MSG = request
            return self
        elif "Session Timeout" in request:
            self.ERROR_MSG = request
            return self

        if len(kwargs) > 0:
            temp_object = self.Factory(self.DeviceProxy, request, name=1)
            try:
                temp_object.__setattr__("_HTTP_RESPONSE", self._HTTP_RESPONSE)
                temp_object.__setattr__("DEBUG_CONNECTION", self.DEBUG_CONNECTION)
                temp_object.__setattr__("DEBUG_Payload", self.DEBUG_Payload)
                temp_object.__setattr__("DEBUG_Response", self.DEBUG_Response)
                temp_object.__setattr__("DEBUG_URL", self.DEBUG_URL)
                temp_object.__setattr__("DEBUG_headers", self.DEBUG_headers)
            except Exception:
                pass
            return temp_object
        else:
            r_list = []
            for k, v in request.items():
                if "List" in k:
                    wrapper_key = k.replace("-list", "", 1)

                elif "list" in k:
                    wrapper_key = k.replace("-list", "", 1)
                else:
                    wrapper_key = k
                if wrapper_key[len(wrapper_key) - 1] == "_":
                    wrapper_key = wrapper_key[:len(wrapper_key) - 1]
                if isinstance(v, list):
                    for i in v:
                        new_object = self.Factory(self.DeviceProxy, {wrapper_key: i}, name=0, parent="")
                        new_object.__setattr__("_HTTP_RESPONSE", self._HTTP_RESPONSE)
                        new_object.__setattr__("DEBUG_CONNECTION", self.DEBUG_CONNECTION)
                        new_object.__setattr__("DEBUG_Payload", self.DEBUG_Payload)
                        new_object.__setattr__("DEBUG_Response", self.DEBUG_Response)
                        new_object.__setattr__("DEBUG_URL", self.DEBUG_URL)
                        new_object.__setattr__("DEBUG_headers", self.DEBUG_headers)
                        r_list.append(new_object)
                else:
                    try:
                        new_object = self.Factory(self.DeviceProxy, request, name=1)
                        new_object.__setattr__("_HTTP_RESPONSE", self._HTTP_RESPONSE)
                        new_object.__setattr__("DEBUG_CONNECTION", self.DEBUG_CONNECTION)
                        new_object.__setattr__("DEBUG_Payload", self.DEBUG_Payload)
                        new_object.__setattr__("DEBUG_Response", self.DEBUG_Response)
                        new_object.__setattr__("DEBUG_URL", self.DEBUG_URL)
                        new_object.__setattr__("DEBUG_headers", self.DEBUG_headers)
                    except:
                        pass
                    return new_object

        return r_list


    def get_stream_response(self, **kwargs):
        A10BaseClass.is_POST = True
        o_url = self.a10_url
        if len(kwargs) > 0:
            self.a10_url_update(**kwargs)
        else:
            self.a10_url_parent()
        response = self.DeviceProxy.POST(self)
        self.a10_url = o_url
        return response

    def create(self, **kwargs):
        A10BaseClass.is_POST = True
        o_url = self.a10_url
        if len(kwargs) > 0:
            self.a10_url_update(**kwargs)
        else:
            self.a10_url_parent()
        response = self.response_handler(self.DeviceProxy.POST(self))
        self.a10_url = o_url
        return response

    def update(self, **kwargs):
        A10BaseClass.is_POST = True
        o_url = self.a10_url
        if len(kwargs) > 0:
            self.a10_url_update(**kwargs)
        else:
            self.a10_url_parent()

        response = self.response_handler(self.DeviceProxy.POST(self))
        self.a10_url = o_url
        return response

    def replace(self, **kwargs):
        A10BaseClass.is_POST = False
        o_url = self.a10_url
        if len(kwargs) > 0:
            self.a10_url_update(**kwargs)
        else:
            self.a10_url_parent()
        response = self.response_handler(self.DeviceProxy.PUT(self))
        self.a10_url = o_url
        return response

    def replace_all(self, obj_list):
        A10BaseClass.is_POST = False
        o_url = self.a10_url
        self.a10_url_parent()
        response = self.response_handler(self.DeviceProxy.PUT_ALL(self, obj_list))
        self.a10_url = o_url
        return response

    def create_all(self, obj_list):
        A10BaseClass.is_POST = True
        o_url = self.a10_url
        self.a10_url_parent()
        response = self.response_handler(self.DeviceProxy.POST_ALL(self, obj_list))
        self.a10_url = o_url
        return response


    def delete(self, query_params=None, **kwargs):
        o_url = self.a10_url
        if len(kwargs) > 0:
            self.a10_url_update(**kwargs)
        else:
            self.a10_url_parent()
        response = self.response_handler(self.DeviceProxy.DELETE(self, query_params))
        self.a10_url = o_url
        return response


    def a10_url_update(self, **kwargs):
        temp_url = self.a10_url
        try:
            for key, value in kwargs.items():
                if isinstance(value, tuple) or isinstance(value, list):
                    for v in value:
                        v = urllib.quote_plus(str(v).replace(' ', "%20"))
                        v = v.replace('%2520', '%20')
                        self.a10_url = self.a10_url.replace('{%s}' % key, v, 1)
                else:
                    #Python converts white spaces to +
                    #Modifying this behavior to use %20 encoding instead
                    value = urllib.quote_plus(str(value).replace(' ', '%20'))
                    value = value.replace('%2520', '%20')
                    self.a10_url = self.a10_url.replace('{%s}' % key, value, 1)
            #Removing any unresolved keys and removing the +
            while(len(kwargs)> 0 and '{' in self.a10_url):
                try:
                    start_index = self.a10_url.index('{')
                    end_index = self.a10_url.index('}')
                    self.a10_url = self.a10_url.replace(self.a10_url[start_index:end_index+1], '')
                except ValueError as e:
                    print 'Substring not found', e
                    break
            self.a10_url = self.a10_url.replace('+/', '/')
            self.a10_url = self.a10_url.replace('/+', '/')
            #zli fixed bug:243614
            p = re.compile('\+$')
            #self.a10_url = self.a10_url.replace('+', '', -1) if self.a10_url.endswith('+') else self.a10_url
            self.a10_url = p.sub('', self.a10_url) if self.a10_url.endswith('+') else self.a10_url
            if '{' in self.a10_url:
                self.a10_url_parent(**kwargs)
        except:
            try:
                self.a10_url_parent(**kwargs)
            except:
                self.a10_url = temp_url


    def a10_url_override(self, url):
        self.a10_url = url

    #TODO: Need to build a more intelligent handler.


    def a10_url_parent(self, **kwargs):
        if "{" in self.a10_url:
            p_list = self.a10_url.split("/")

            if self.a10_url.endswith('oper'):
                temp = self.a10_url.replace(p_list[(len(p_list) - 2)] + '/', "")
                self.a10_url = temp
            elif self.a10_url.endswith('stats'):
                temp = self.a10_url.replace(p_list[(len(p_list) - 2)] + '/', "")
                self.a10_url = temp
            else:
                temp = self.a10_url.replace(p_list[(len(p_list) - 1)], "")
                self.a10_url = temp[0:len(temp) - 1]
        if len(kwargs) > 0:
            try:
                self.a10_url = self.a10_url.format(**kwargs)
            except:
                pass

    def get_stats(self, url="", Filters={}, **kwargs):
        if url == "":
            o_url = self.a10_url
        else:
            o_url = self.a10_url
            self.a10_url = url

        if len(kwargs) > 0:
            try:
                self.a10_url = self.a10_url.format(**kwargs)

            except:
                pass
            """
            If you are utilizing the stats class &| you want to get stats from a parent.
            """
        if "{" in self.a10_url:
            self.a10_url = re.match(r'^(/.+?/{)', self.a10_url).group(0).replace("/{", "")

        if "stats" not in self.a10_url:
            self.a10_url = self.a10_url + "/stats"

        if len(Filters) > 0:
            query = urllib.urlencode(**Filters)
            endpoint = self.a10_url + "?" + query
            temp_url = self.a10_url
            self.a10_url = endpoint
        response = self.response_handler(self.DeviceProxy.GET(self), False)
        self.a10_url = o_url
        return response


    def del_stats(self, url="", Filters={}, **kwargs):
        if url == "":
            o_url = self.a10_url
        else:
            o_url = self.a10_url
            self.a10_url = url

        if len(kwargs) > 0:
            try:
                self.a10_url = self.a10_url.format(**kwargs)

            except:
                pass
            """
            If you are utilizing the stats class &| you want to get stats from a parent.
            """
        if "{" in self.a10_url:
            self.a10_url = re.match(r'^(/.+?/{)', self.a10_url).group(0).replace("/{", "")

        if "stats" not in self.a10_url:
            self.a10_url = self.a10_url + "/stats"

        if len(Filters) > 0:
            query = urllib.urlencode(**Filters)
            endpoint = self.a10_url + "?" + query
            temp_url = self.a10_url
            self.a10_url = endpoint
        response = self.response_handler(self.DeviceProxy.DELETE(self), False)
        self.a10_url = o_url
        return response

    def get_oper(self, url="", Filters={}, **kwargs):
        if url == "":
            o_url = self.a10_url
        else:
            o_url = self.a10_url
            self.a10_url = url

        if len(kwargs) > 0:
            try:
                self.a10_url = self.a10_url.format(**kwargs)
            except:
                pass
            """
            If you are utilizing the stats class &| you want to get stats from a parent.
            """
        if "{" in self.a10_url:
            self.a10_url = re.match(r'^(/.+?/{)', self.a10_url).group(0).replace("/{", "")

        if "oper" not in self.a10_url:
            self.a10_url = self.a10_url + "/oper"
        if len(Filters) > 0:
            query = urllib.urlencode(**Filters)
            endpoint = self.a10_url + "?" + query
            temp_url = self.a10_url
            self.a10_url = endpoint
        response = self.response_handler(self.DeviceProxy.GET(self), False)
        self.a10_url = o_url
        return response

    def response_handler(self, response, r_obj=True):
        try:
            response = json.loads(response, encoding='utf-8')
        except:
            pass
        try:
            if response is None:
                self.ERROR_MSG = "None Returned"
                return self
            elif 'response' in response:
                if "err" in response['response']:
                    self.ERROR_MSG = response
                    return self
                elif "status" in response['response']:
                    if response['response']['status'] == "OK":
                        return self
            elif "Session Timeout" in response:
                self.ERROR_MSG = response
                return self
            else:
                if r_obj == True:
                    self.ERROR_MSG = ""
                    return self
                else:
                    return response
        except:
            self.ERROR_MSG = response
            return self


    #Helper method for single file upload
    def file_upload(self, filename=None, file_handle=None, file_obj=None):
        u_fields = [("json", {self.b_key:{"file":filename,
                                          "file-handle":file_handle,
                                          "action":'import'}})]

        u_files = [(filename, file_handle, file_obj)]

        return self.files_upload(u_fields, u_files)

    #Added to address file_upload and downloads
    def files_upload(self, fields=[], files=[]):

        '''
        API only supports one file being uploaded at a time.
        :params fields: [("json", {self.b_key:{"file":filename,
                                             "file-handle":file_handle,
                                             "action":action}})]
        :params files:[("file", filename, file_obj)]
        '''

        self.fields = fields
        self.files = files
        return self.DeviceProxy.post_multipart(self)

    def file_download(self, name=None):
        '''
        This bypasses the factory so the raw file content can be returned.
        '''

        self.a10_url = self.a10_url + "/" + name
        return self.DeviceProxy.multi_part_get(self)


    def file_replace(self, filename=None, file_handle=None, file_obj=None):
        u_fields = [("json", {self.b_key:{"file":filename,
                                          "file-handle":file_handle,
                                          "action":'import'}})]

        u_files = [(filename, file_handle, file_obj)]

        return self.files_upload(u_fields, u_files)

    def file_delete(self, name=None):
        self.a10_url = self.a10_url + "/" + name
        return self.DeviceProxy.DELETE(self)


class kwbl():
    def kwbl(self, word, key=0):
        # if word in dir(__builtins__) or 'copy' in word:
        # (echou): Replace to workaround Django vs Python __builtins__
        # (raunak): Use the Python builtins to have a consistent behavior with the sdk_generator
        python_built_in = ['bytearray', 'IndexError', 'all', 'help', 'vars', 'SyntaxError', 'unicode',
                           'UnicodeDecodeError', 'memoryview',
                           'isinstance', 'copyright', 'NameError', 'BytesWarning', 'dict', 'IOError', 'oct', 'bin',
                           'SystemExit',
                           'StandardError', 'format', 'TabError', 'sorted', 'False', 'RuntimeWarning', 'list', 'iter',
                           'reload',
                           'Warning', '__package__', 'round', 'dir', 'cmp', 'set', 'bytes', 'UnicodeTranslateError',
                           'intern',
                           'issubclass', 'Ellipsis', 'EOFError', 'locals', 'BufferError', 'slice', 'FloatingPointError',
                           'sum', 'getattr',
                           'abs', 'exit', 'print', 'True', 'FutureWarning', 'ImportWarning', 'None', 'hash',
                           'ReferenceError', 'len',
                           'credits', 'frozenset', '__name__', 'ord', 'super', '_', 'TypeError', 'license',
                           'KeyboardInterrupt',
                           'UserWarning', 'filter', 'range', 'staticmethod', 'SystemError', 'BaseException', 'pow',
                           'RuntimeError',
                           'float', 'GeneratorExit', 'StopIteration', 'globals', 'divmod', 'enumerate', 'apply',
                           'LookupError', 'open',
                           'quit', 'basestring', 'UnicodeError', 'zip', 'hex', 'long', 'next', 'ImportError', 'chr',
                           '__import__', 'type',
                           'Exception', 'tuple', 'reduce', 'reversed', 'UnicodeEncodeError', 'input', 'hasattr',
                           'delattr', 'setattr',
                           'raw_input', 'PendingDeprecationWarning', 'compile', 'ArithmeticError', 'str', 'property',
                           'MemoryError',
                           'int', 'xrange', 'KeyError', 'coerce', 'SyntaxWarning', 'file', 'EnvironmentError', 'unichr',
                           'id', 'OSError',
                           'DeprecationWarning', 'min', 'UnicodeWarning', 'execfile', 'any', 'complex', 'bool',
                           'ValueError',
                           'NotImplemented', 'map', 'buffer', 'max', 'object', 'repr', 'callable', 'ZeroDivisionError',
                           'eval',
                           '__debug__', 'IndentationError', 'AssertionError', 'classmethod', 'UnboundLocalError',
                           'NotImplementedError',
                           'AttributeError', 'OverflowError']
        if word in dir(__builtins__) or 'copy' in word or word in python_built_in:
            if key == 0:
                return "A10WW_" + word
            else:
                return "A10_" + word
        # (echou): Comment out sys.modules check per discussionw with mthompson and raunaka
        # elif word in sys.modules.keys():
        #     if key == 0:
        #         return "A10WW_" + word
        #     else:
        #         return "A10_" + word
        elif word in keyword.kwlist:
            if key == 0:
                return "A10WW_" + word
            else:
                return "A10_" + word
        elif re.search(r'^[0-9]', word):
            if key == 0:
                return "A10WW_" + word
            else:
                return "A10_" + word
        else:
            return word
