# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/Products/Five/utilities/browser/edit_markers.pt'

__tokens = {803: ('request/ACTUAL_URL', 22, 33), 991: ('view/getInterfaceNames', 27, 34), 1141: ('interface/name', 30, 27), 1226: ('view/getDirectlyProvidedNames', 33, 34), 1416: ('interface/name', 36, 38), 1472: (' interface/nam', 37, 40), 1570: ('interface/name', 40, 27), 1648: ('view/getDirectlyProvidedNames', 43, 27), 2151: ('view/getAvailableInterfaceNames', 57, 34), 2340: ('interface/name', 60, 38), 2396: (' interface/nam', 61, 40), 2494: ('interface/name', 64, 27), 2629: ('view/getAvailableInterfaceNames', 67, 70), 23: ('context/@@standard_macros/page', 1, 23), 23: ('context/@@standard_macros/page', 1, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from collections import deque as _deque
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140533346148864 = 'page'
_static_140533346088704 = {'class': 'btn btn-primary', 'type': 'submit', 'name': 'SAVE', 'value': 'Add', }
_static_140533346086496 = {'class': 'zmi-controls form-group form-inline', }
_static_140533346082320 = {'class': 'zmi-object-id', }
_static_140533346078000 = {'type': 'checkbox', 'id': 'INTERFACE', 'name': 'add:list', 'value': 'interface/name', }
_static_140533346080064 = {'class': 'zmi-object-check text-right', }
_static_140533346082608 = {'class': 'table table-striped table-hover table-sm', }
_static_140533346014816 = {'class': 'btn btn-primary', 'type': 'submit', 'name': 'SAVE', 'value': 'Remove', }
_static_140533346011792 = {'class': 'zmi-controls', }
_static_140533346012848 = {'class': 'zmi-object-check text-right', }
_static_140533346018944 = {'class': 'zmi-object-id', }
_static_140533348994160 = {'type': 'checkbox', 'id': 'INTERFACE', 'name': 'remove:list', 'value': 'interface/name', }
_static_140533346014528 = {'class': 'zmi-object-check text-right', }
_static_140533346015008 = {'class': 'zmi-object-id', }
_static_140533346021248 = {'class': 'zmi-object-check text-right', }
_static_140533346146080 = {'class': 'table table-striped table-hover table-sm', }
_static_140533417024992 = __C2ZContextWrapper
_static_140533417025280 = __compile_zt_expr
_static_140533346152656 = {'action': '.', 'method': 'post', }
_static_140533346145648 = {'class': 'form-help formHelp', }
_static_140533416833664 = {}

import re
import functools
from itertools import chain as __chain
from sys import intern
__default = intern('__default__')
__marker = object()
g_re_amp = re.compile('&(?!([A-Za-z]+|#[0-9]+);)')
g_re_needs_escape = re.compile('[&<>\\"\\\']').search
__re_whitespace = functools.partial(re.compile('\\s+').sub, ' ')

def initialize(modules, nothing, tales, zope_version_5_8_5_):

    def render_heading(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
        __append = __stream.append
        __re_amp = g_re_amp
        __token = None
        __re_needs_escape = g_re_needs_escape

        def __convert(target):
            if (target is None):
                return
            __tt = type(target)
            if ((__tt is int) or (__tt is float) or (__tt is int)):
                target = str(target)
            else:
                if (__tt is bytes):
                    target = decode(target)
                else:
                    if (__tt is not str):
                        try:
                            target = target.__html__
                        except AttributeError:
                            __converted = convert(target)
                            target = (str(target) if (target is __converted) else __converted)
                        else:
                            target = target()
            return target

        def __quote(target, quote, quote_entity, default, default_marker):
            if (target is None):
                return
            if (target is default_marker):
                return default
            __tt = type(target)
            if ((__tt is int) or (__tt is float) or (__tt is int)):
                target = str(target)
            else:
                if (__tt is bytes):
                    target = decode(target)
                else:
                    if (__tt is not str):
                        try:
                            target = target.__html__
                        except:
                            __converted = convert(target)
                            target = (str(target) if (target is __converted) else __converted)
                        else:
                            return target()
                if (target is not None):
                    try:
                        escape = (__re_needs_escape(target) is not None)
                    except TypeError:
                        pass
                    else:
                        if escape:
                            if ('&' in target):
                                target = target.replace('&', '&amp;')
                            if ('<' in target):
                                target = target.replace('<', '&lt;')
                            if ('>' in target):
                                target = target.replace('>', '&gt;')
                            if ((quote is not None) and (quote in target)):
                                target = target.replace(quote, quote_entity)
            return target
        translate = econtext['__translate']
        decode = econtext['__decode']
        convert = econtext['__convert']
        on_error_handler = econtext['__on_error_handler']
        try:
            getname = econtext.get_name
            get = econtext.get

            # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533346143872
            __attrs_140533346143872 = _static_140533416833664
            __append('\n    ')

            # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533346144544
            __attrs_140533346144544 = _static_140533416833664

            # <h1 ... (0:0)
            # --------------------------------------------------------
            __append('<h1>')
            __stream_140533346144016 = []
            __append_140533346144016 = __stream_140533346144016.append
            __append_140533346144016('Assign Marker Interfaces')
            __msgid_140533346144016 = __re_whitespace(''.join(__stream_140533346144016)).strip()
            if 'heading_edit_marker':
                __append(translate('heading_edit_marker', mapping=None, default=__msgid_140533346144016, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</h1>\n  ')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_main(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
        __append = __stream.append
        __re_amp = g_re_amp
        __token = None
        __re_needs_escape = g_re_needs_escape

        def __convert(target):
            if (target is None):
                return
            __tt = type(target)
            if ((__tt is int) or (__tt is float) or (__tt is int)):
                target = str(target)
            else:
                if (__tt is bytes):
                    target = decode(target)
                else:
                    if (__tt is not str):
                        try:
                            target = target.__html__
                        except AttributeError:
                            __converted = convert(target)
                            target = (str(target) if (target is __converted) else __converted)
                        else:
                            target = target()
            return target

        def __quote(target, quote, quote_entity, default, default_marker):
            if (target is None):
                return
            if (target is default_marker):
                return default
            __tt = type(target)
            if ((__tt is int) or (__tt is float) or (__tt is int)):
                target = str(target)
            else:
                if (__tt is bytes):
                    target = decode(target)
                else:
                    if (__tt is not str):
                        try:
                            target = target.__html__
                        except:
                            __converted = convert(target)
                            target = (str(target) if (target is __converted) else __converted)
                        else:
                            return target()
                if (target is not None):
                    try:
                        escape = (__re_needs_escape(target) is not None)
                    except TypeError:
                        pass
                    else:
                        if escape:
                            if ('&' in target):
                                target = target.replace('&', '&amp;')
                            if ('<' in target):
                                target = target.replace('<', '&lt;')
                            if ('>' in target):
                                target = target.replace('>', '&gt;')
                            if ((quote is not None) and (quote in target)):
                                target = target.replace(quote, quote_entity)
            return target
        translate = econtext['__translate']
        decode = econtext['__decode']
        convert = econtext['__convert']
        on_error_handler = econtext['__on_error_handler']
        try:
            getname = econtext.get_name
            get = econtext.get

            # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533346145072
            __attrs_140533346145072 = _static_140533416833664
            __append('\n    ')

            # <Static value=<ast.Dict object at 0x7fd0782d1570> name=None at 7fd0782d1510> -> __attrs_140533346143296
            __attrs_140533346143296 = _static_140533346145648

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p class="form-help formHelp">')
            __stream_140533346145744 = []
            __append_140533346145744 = __stream_140533346145744.append
            __append_140533346145744('\n      Change the behavior of this object by adding or removing marker\n      interfaces. You can choose one or more interfaces to be added to the\n      list of provided interfaces for this object.\n      ')

            # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533346140944
            __attrs_140533346140944 = _static_140533416833664

            # <br ... (0:0)
            # --------------------------------------------------------
            __append_140533346145744('<br />\n      A marker interface is used to identify an instance of a piece of\n      content. This allows you to enable and disable views based on marker\n      interfaces for example.\n    ')
            __msgid_140533346145744 = __re_whitespace(''.join(__stream_140533346145744)).strip()
            if __msgid_140533346145744:
                __append(translate(__msgid_140533346145744, mapping=None, default=__msgid_140533346145744, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</p>\n    \n    ')

            # <Static value=<ast.Dict object at 0x7fd0782d30d0> name=None at 7fd0782d36a0> -> __attrs_140533346153568
            __attrs_140533346153568 = _static_140533346152656

            # <form ... (0:0)
            # --------------------------------------------------------
            __append('<form')

            # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533346151984
            __default_140533346151984 = _DEFAULT_MARKER

            # <Substitution 'request/ACTUAL_URL' (22:33)> -> __attr_action
            __token = 803
            try:
                __zt_tmp = __attrs_140533346153568
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_action = _static_140533417025280('path', 'request/ACTUAL_URL', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
            __attr_action = __quote(__attr_action, '"', '&quot;', '.', _DEFAULT_MARKER)
            if (__attr_action is not None):
                __append((' action="%s"' % __attr_action))
            __append(' method="post">\n\n      ')

            # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533346151648
            __attrs_140533346151648 = _static_140533416833664

            # <h3 ... (0:0)
            # --------------------------------------------------------
            __append('<h3>')
            __stream_140533346152944 = []
            __append_140533346152944 = __stream_140533346152944.append
            __append_140533346152944('Provided interfaces')
            __msgid_140533346152944 = __re_whitespace(''.join(__stream_140533346152944)).strip()
            if 'legend_provided':
                __append(translate('legend_provided', mapping=None, default=__msgid_140533346152944, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</h3>\n\n      ')

            # <Static value=<ast.Dict object at 0x7fd0782d1720> name=None at 7fd0782d1210> -> __attrs_140533346020624
            __attrs_140533346020624 = _static_140533346146080

            # <table ... (0:0)
            # --------------------------------------------------------
            __append('<table class="table table-striped table-hover table-sm">\n        ')

            # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533346017648
            __attrs_140533346017648 = _static_140533416833664
            __backup_interface_140533346079248 = get('interface', __marker)

            # <Value 'view/getInterfaceNames' (27:34)> -> __iterator
            __token = 991
            try:
                __zt_tmp = __attrs_140533346017648
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140533417025280('path', 'view/getInterfaceNames', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
            (__iterator, ____index_140533346012608, ) = getname('repeat')('interface', __iterator)
            econtext['interface'] = None
            for __item in __iterator:
                econtext['interface'] = __item

                # <tr ... (0:0)
                # --------------------------------------------------------
                __append('<tr>\n          ')

                # <Static value=<ast.Dict object at 0x7fd0782b2f80> name=None at 7fd0782b3a30> -> __attrs_140533346013232
                __attrs_140533346013232 = _static_140533346021248

                # <td ... (0:0)
                # --------------------------------------------------------
                __append('<td class="zmi-object-check text-right">&nbsp;</td>\n          ')

                # <Static value=<ast.Dict object at 0x7fd0782b1720> name=None at 7fd0782b1810> -> __attrs_140533346024944
                __attrs_140533346024944 = _static_140533346015008

                # <td ... (0:0)
                # --------------------------------------------------------
                __append('<td class="zmi-object-id">')

                # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533346016352
                __default_140533346016352 = _DEFAULT_MARKER

                # <Value 'interface/name' (30:27)> -> __cache_140533346025376
                __token = 1141
                try:
                    __zt_tmp = __attrs_140533346024944
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140533346025376 = _static_140533417025280('path', 'interface/name', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))

                # <BinOp left=<Value 'interface/name' (30:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fd07c5afbe0> at 7fd0782b1d50> -> __condition
                __expression = __cache_140533346025376

                # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('Interface Name')
                else:
                    __content = __cache_140533346025376
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</td>\n        </tr>')
                ____index_140533346012608 -= 1
                if (____index_140533346012608 > 0):
                    __append('\n        ')
            if (__backup_interface_140533346079248 is __marker):
                del econtext['interface']
            else:
                econtext['interface'] = __backup_interface_140533346079248
            __append('\n\n        ')

            # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533346022928
            __attrs_140533346022928 = _static_140533416833664
            __backup_interface_140533348030192 = get('interface', __marker)

            # <Value 'view/getDirectlyProvidedNames' (33:34)> -> __iterator
            __token = 1226
            try:
                __zt_tmp = __attrs_140533346022928
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140533417025280('path', 'view/getDirectlyProvidedNames', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
            (__iterator, ____index_140533346024320, ) = getname('repeat')('interface', __iterator)
            econtext['interface'] = None
            for __item in __iterator:
                econtext['interface'] = __item

                # <tr ... (0:0)
                # --------------------------------------------------------
                __append('<tr>\n          ')

                # <Static value=<ast.Dict object at 0x7fd0782b1540> name=None at 7fd0782d3a30> -> __attrs_140533348693952
                __attrs_140533348693952 = _static_140533346014528

                # <td ... (0:0)
                # --------------------------------------------------------
                __append('<td class="zmi-object-check text-right">\n            ')

                # <Static value=<ast.Dict object at 0x7fd078588c70> name=None at 7fd0785895d0> -> __attrs_140533346025328
                __attrs_140533346025328 = _static_140533348994160

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="checkbox"')

                # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533346024608
                __default_140533346024608 = _DEFAULT_MARKER

                # <Substitution 'interface/name' (36:38)> -> __attr_id
                __token = 1416
                try:
                    __zt_tmp = __attrs_140533346025328
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_id = _static_140533417025280('path', 'interface/name', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                __attr_id = __quote(__attr_id, '"', '&quot;', 'INTERFACE', _DEFAULT_MARKER)
                if (__attr_id is not None):
                    __append((' id="%s"' % __attr_id))
                __append(' name="remove:list"')

                # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533346024416
                __default_140533346024416 = _DEFAULT_MARKER

                # <Substitution 'interface/name' (37:40)> -> __attr_value
                __token = 1472
                try:
                    __zt_tmp = __attrs_140533346025328
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_140533417025280('path', 'interface/name', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append('/>\n          </td>\n          ')

                # <Static value=<ast.Dict object at 0x7fd0782b2680> name=None at 7fd0782b2500> -> __attrs_140533346018224
                __attrs_140533346018224 = _static_140533346018944

                # <td ... (0:0)
                # --------------------------------------------------------
                __append('<td class="zmi-object-id">')

                # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533346019520
                __default_140533346019520 = _DEFAULT_MARKER

                # <Value 'interface/name' (40:27)> -> __cache_140533346019952
                __token = 1570
                try:
                    __zt_tmp = __attrs_140533346018224
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140533346019952 = _static_140533417025280('path', 'interface/name', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))

                # <BinOp left=<Value 'interface/name' (40:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fd07c5afbe0> at 7fd0782b1a50> -> __condition
                __expression = __cache_140533346019952

                # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('Interface Name')
                else:
                    __content = __cache_140533346019952
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</td>\n        </tr>')
                ____index_140533346024320 -= 1
                if (____index_140533346024320 > 0):
                    __append('\n        ')
            if (__backup_interface_140533348030192 is __marker):
                del econtext['interface']
            else:
                econtext['interface'] = __backup_interface_140533348030192
            __append('\n\n        ')

            # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533346019472
            __attrs_140533346019472 = _static_140533416833664

            # <Value 'view/getDirectlyProvidedNames' (43:27)> -> __condition
            __token = 1648
            try:
                __zt_tmp = __attrs_140533346019472
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140533417025280('path', 'view/getDirectlyProvidedNames', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
            if __condition:

                # <tr ... (0:0)
                # --------------------------------------------------------
                __append('<tr>\n          ')

                # <Static value=<ast.Dict object at 0x7fd0782b0eb0> name=None at 7fd0782b1600> -> __attrs_140533346013568
                __attrs_140533346013568 = _static_140533346012848

                # <td ... (0:0)
                # --------------------------------------------------------
                __append('<td class="zmi-object-check text-right">&nbsp;</td>\n          ')

                # <Static value=<ast.Dict object at 0x7fd0782b0a90> name=None at 7fd0782b0b20> -> __attrs_140533346010736
                __attrs_140533346010736 = _static_140533346011792

                # <td ... (0:0)
                # --------------------------------------------------------
                __append('<td class="zmi-controls">\n            ')

                # <Static value=<ast.Dict object at 0x7fd0782b1660> name=None at 7fd0782b0070> -> __attrs_140533346090528
                __attrs_140533346090528 = _static_140533346014816

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input class="btn btn-primary" type="submit" name="SAVE"')

                # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533346089424
                __default_140533346089424 = _DEFAULT_MARKER

                # <Translate msgid=None node=<ast.Constant object at 0x7fd0782c3970> at 7fd0782c3940> -> __attr_value
                __attr_value = 'Remove'
                __attr_value = translate(__attr_value, default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append('/>\n          </td>\n        </tr>')
            __append('\n      </table>\n\n      ')

            # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533346075600
            __attrs_140533346075600 = _static_140533416833664

            # <h3 ... (0:0)
            # --------------------------------------------------------
            __append('<h3>')
            __stream_140533346010784 = []
            __append_140533346010784 = __stream_140533346010784.append
            __append_140533346010784('\n        Available Marker Interfaces\n      ')
            __msgid_140533346010784 = __re_whitespace(''.join(__stream_140533346010784)).strip()
            if 'legend_available_marker':
                __append(translate('legend_available_marker', mapping=None, default=__msgid_140533346010784, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</h3>\n\n      ')

            # <Static value=<ast.Dict object at 0x7fd0782c1f30> name=None at 7fd0782c1ff0> -> __attrs_140533346083232
            __attrs_140533346083232 = _static_140533346082608

            # <table ... (0:0)
            # --------------------------------------------------------
            __append('<table class="table table-striped table-hover table-sm">\n        ')

            # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533346084384
            __attrs_140533346084384 = _static_140533416833664
            __backup_interface_140533347936736 = get('interface', __marker)

            # <Value 'view/getAvailableInterfaceNames' (57:34)> -> __iterator
            __token = 2151
            try:
                __zt_tmp = __attrs_140533346084384
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140533417025280('path', 'view/getAvailableInterfaceNames', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
            (__iterator, ____index_140533346084672, ) = getname('repeat')('interface', __iterator)
            econtext['interface'] = None
            for __item in __iterator:
                econtext['interface'] = __item

                # <tr ... (0:0)
                # --------------------------------------------------------
                __append('<tr>\n          ')

                # <Static value=<ast.Dict object at 0x7fd0782c1540> name=None at 7fd0782c06a0> -> __attrs_140533346078768
                __attrs_140533346078768 = _static_140533346080064

                # <td ... (0:0)
                # --------------------------------------------------------
                __append('<td class="zmi-object-check text-right">\n            ')

                # <Static value=<ast.Dict object at 0x7fd0782c0d30> name=None at 7fd0782c07f0> -> __attrs_140533346079104
                __attrs_140533346079104 = _static_140533346078000

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="checkbox"')

                # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533346080496
                __default_140533346080496 = _DEFAULT_MARKER

                # <Substitution 'interface/name' (60:38)> -> __attr_id
                __token = 2340
                try:
                    __zt_tmp = __attrs_140533346079104
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_id = _static_140533417025280('path', 'interface/name', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                __attr_id = __quote(__attr_id, '"', '&quot;', 'INTERFACE', _DEFAULT_MARKER)
                if (__attr_id is not None):
                    __append((' id="%s"' % __attr_id))
                __append(' name="add:list"')

                # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533346077232
                __default_140533346077232 = _DEFAULT_MARKER

                # <Substitution 'interface/name' (61:40)> -> __attr_value
                __token = 2396
                try:
                    __zt_tmp = __attrs_140533346079104
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_140533417025280('path', 'interface/name', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append('/>\n          </td>\n          ')

                # <Static value=<ast.Dict object at 0x7fd0782c1e10> name=None at 7fd0782c1870> -> __attrs_140533346075360
                __attrs_140533346075360 = _static_140533346082320

                # <td ... (0:0)
                # --------------------------------------------------------
                __append('<td class="zmi-object-id">')

                # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533346083616
                __default_140533346083616 = _DEFAULT_MARKER

                # <Value 'interface/name' (64:27)> -> __cache_140533346076608
                __token = 2494
                try:
                    __zt_tmp = __attrs_140533346075360
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140533346076608 = _static_140533417025280('path', 'interface/name', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))

                # <BinOp left=<Value 'interface/name' (64:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fd07c5afbe0> at 7fd0782c1600> -> __condition
                __expression = __cache_140533346076608

                # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('Interface Name')
                else:
                    __content = __cache_140533346076608
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</td>\n        </tr>')
                ____index_140533346084672 -= 1
                if (____index_140533346084672 > 0):
                    __append('\n        ')
            if (__backup_interface_140533347936736 is __marker):
                del econtext['interface']
            else:
                econtext['interface'] = __backup_interface_140533347936736
            __append('\n      </table>\n      ')

            # <Static value=<ast.Dict object at 0x7fd0782c2e60> name=None at 7fd0782c2f20> -> __attrs_140533346081408
            __attrs_140533346081408 = _static_140533346086496

            # <Value 'view/getAvailableInterfaceNames' (67:70)> -> __condition
            __token = 2629
            try:
                __zt_tmp = __attrs_140533346081408
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140533417025280('path', 'view/getAvailableInterfaceNames', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="zmi-controls form-group form-inline">\n            ')

                # <Static value=<ast.Dict object at 0x7fd0782c3700> name=None at 7fd0782c3760> -> __attrs_140533346081792
                __attrs_140533346081792 = _static_140533346088704

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input class="btn btn-primary" type="submit" name="SAVE"')

                # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533346085152
                __default_140533346085152 = _DEFAULT_MARKER

                # <Translate msgid=None node=<ast.Constant object at 0x7fd0782c2c20> at 7fd0782c2a40> -> __attr_value
                __attr_value = 'Add'
                __attr_value = translate(__attr_value, default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append('/>\n      </div>')
            __append('\n    </form>\n  ')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
        __append = __stream.append
        __re_amp = g_re_amp
        __token = None
        __re_needs_escape = g_re_needs_escape

        def __convert(target):
            if (target is None):
                return
            __tt = type(target)
            if ((__tt is int) or (__tt is float) or (__tt is int)):
                target = str(target)
            else:
                if (__tt is bytes):
                    target = decode(target)
                else:
                    if (__tt is not str):
                        try:
                            target = target.__html__
                        except AttributeError:
                            __converted = convert(target)
                            target = (str(target) if (target is __converted) else __converted)
                        else:
                            target = target()
            return target

        def __quote(target, quote, quote_entity, default, default_marker):
            if (target is None):
                return
            if (target is default_marker):
                return default
            __tt = type(target)
            if ((__tt is int) or (__tt is float) or (__tt is int)):
                target = str(target)
            else:
                if (__tt is bytes):
                    target = decode(target)
                else:
                    if (__tt is not str):
                        try:
                            target = target.__html__
                        except:
                            __converted = convert(target)
                            target = (str(target) if (target is __converted) else __converted)
                        else:
                            return target()
                if (target is not None):
                    try:
                        escape = (__re_needs_escape(target) is not None)
                    except TypeError:
                        pass
                    else:
                        if escape:
                            if ('&' in target):
                                target = target.replace('&', '&amp;')
                            if ('<' in target):
                                target = target.replace('<', '&lt;')
                            if ('>' in target):
                                target = target.replace('>', '&gt;')
                            if ((quote is not None) and (quote in target)):
                                target = target.replace(quote, quote_entity)
            return target
        translate = econtext['__translate']
        decode = econtext['__decode']
        convert = econtext['__convert']
        on_error_handler = econtext['__on_error_handler']
        try:
            getname = econtext.get_name
            get = econtext.get

            # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533346150736
            __attrs_140533346150736 = _static_140533416833664
            __backup_macroname_140533402790720 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7fd0782d2200> name=None at 7fd0782d2aa0> -> __value
            __value = _static_140533346148864
            econtext['macroname'] = __value

            def __fill_body(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533346149728
                __attrs_140533346149728 = _static_140533416833664
                __append('\n\n  ')
                __token = None
                render_heading(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append('\n  \n  ')
                __token = None
                render_main(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append('\n')
            _slots = econtext['__slot_body'] = _deque((__fill_body, ))

            # <Value 'context/@@standard_macros/page' (1:23)> -> __macro
            __token = 23
            try:
                __zt_tmp = __attrs_140533346150736
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140533417025280('path', 'context/@@standard_macros/page', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
            __token = 23
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140533402790720 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140533402790720
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_heading': render_heading, 'render_main': render_main, 'render': render, }