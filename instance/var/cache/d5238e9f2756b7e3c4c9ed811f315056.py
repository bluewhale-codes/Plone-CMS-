# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/plone/app/z3cform/templates/checkbox_input.pt'

__tokens = {129: ('view/items', 4, 14), 154: (' python:list(items', 5, 13), 197: ('x python:len(items) ==', 6, 22), 277: ('python:len(items) &gt', 10, 22), 324: ('single_checkbox', 11, 21), 377: ('view/id', 13, 12), 453: ('items', 17, 26), 500: ('python:single_checkbox and view.id or None', 19, 14), 826: ('item/checked', 32, 28), 947: ('s string:form-check-input ${view/klas', 36, 19), 888: ('item/id', 34, 18), 1796: ('              ', 58, 1), 1762: ('ly;\n    ', 56, 35), 916: (' item/nam', 35, 19), 1583: ('         tabi', 52, 6), 1070: ('itle view/', 39, 16), 1006: ('ue item/va', 37, 18), 1038: ('yle view/s', 38, 17), 1101: (' lang vie', 40, 14), 1134: ('nclick view/', 41, 16), 1173: ('blclick view/on', 42, 18), 1216: ('ousedown view/on', 43, 18), 1258: ('onmouseup view', 44, 15), 1300: ('nmouseover view/', 45, 16), 1344: ('onmousemove view', 46, 15), 1387: ('  onmouseout vi', 47, 13), 1429: ('   onkeypress v', 48, 12), 1470: ('     onkeydown', 49, 10), 1508: ('        onke', 50, 7), 1545: ('        disab', 51, 7), 1620: ('           o', 53, 4), 1655: ('           ', 54, 2), 1691: ('            o', 55, 3), 1729: ('             ', 56, 2), 1835: ('\n            ', 58, 40), 2126: ('not:item/checked', 70, 28), 2251: ('s string:form-check-input ${view/klas', 74, 19), 2192: ('item/id', 72, 18), 3100: ('              ', 96, 1), 3066: ('ly;\n    ', 94, 35), 2220: (' item/nam', 73, 19), 2887: ('         tabi', 90, 6), 2374: ('itle view/', 77, 16), 2310: ('ue item/va', 75, 18), 2342: ('yle view/s', 76, 17), 2405: (' lang vie', 78, 14), 2438: ('nclick view/', 79, 16), 2477: ('blclick view/on', 80, 18), 2520: ('ousedown view/on', 81, 18), 2562: ('onmouseup view', 82, 15), 2604: ('nmouseover view/', 83, 16), 2648: ('onmousemove view', 84, 15), 2691: ('  onmouseout vi', 85, 13), 2733: ('   onkeypress v', 86, 12), 2774: ('     onkeydown', 87, 10), 2812: ('        onke', 88, 7), 2849: ('        disab', 89, 7), 2924: ('           o', 91, 4), 2959: ('           ', 92, 2), 2995: ('            o', 93, 3), 3033: ('             ', 94, 2), 3139: ('\n            ', 96, 40), 3310: ('item/id', 103, 19), 3397: ('item/label', 107, 27), 3585: ('string:${view/name}-empty-marker', 116, 16)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140097364982656 = {'name': 'field-empty-marker', 'type': 'hidden', 'value': '1', }
_static_140097252657520 = {'class': 'label', }
_static_140097252661648 = {'class': 'form-check-label', 'for': '', }
_static_140097339911248 = {'class': '', 'id': '', 'accesskey': '', 'alt': '', 'name': '', 'tabindex': '', 'title': '', 'type': 'checkbox', 'value': '', 'style': 'view/style', 'lang': 'view/lang', 'onclick': 'view/onclick', 'ondblclick': 'view/ondblclick', 'onmousedown': 'view/onmousedown', 'onmouseup': 'view/onmouseup', 'onmouseover': 'view/onmouseover', 'onmousemove': 'view/onmousemove', 'onmouseout': 'view/onmouseout', 'onkeypress': 'view/onkeypress', 'onkeydown': 'view/onkeydown', 'onkeyup': 'view/onkeyup', 'disabled': 'view/disabled', 'onfocus': 'view/onfocus', 'onblur': 'view/onblur', 'onchange': 'view/onchange', 'readonly': 'view/readonly', 'onselect': 'view/onselect', }
_static_140097338173392 = {'class': '', 'id': '', 'accesskey': '', 'alt': '', 'checked': 'checked', 'name': '', 'tabindex': '', 'title': '', 'type': 'checkbox', 'value': '', 'style': 'view/style', 'lang': 'view/lang', 'onclick': 'view/onclick', 'ondblclick': 'view/ondblclick', 'onmousedown': 'view/onmousedown', 'onmouseup': 'view/onmouseup', 'onmouseover': 'view/onmouseover', 'onmousemove': 'view/onmousemove', 'onmouseout': 'view/onmouseout', 'onkeypress': 'view/onkeypress', 'onkeydown': 'view/onkeydown', 'onkeyup': 'view/onkeyup', 'disabled': 'view/disabled', 'onfocus': 'view/onfocus', 'onblur': 'view/onblur', 'onchange': 'view/onchange', 'readonly': 'view/readonly', 'onselect': 'view/onselect', }
_static_140097338352800 = {'class': 'form-check', 'id': 'python:single_checkbox and view.id or None', }
_static_140097337633440 = {'id': 'view/id', }
_static_140097413192176 = __C2ZContextWrapper
_static_140097413192464 = __compile_zt_expr
_static_140097337636176 = {'xmlns': 'http://www.w3.org/1999/xhtml', }

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

            # <Static value=<ast.Dict object at 0x7f6af40b3550> name=None at 7f6af40b0b50> -> __attrs_140097337625568
            __attrs_140097337625568 = _static_140097337636176
            __backup_items_140097337624464 = get('items', __marker)

            # <Value 'view/items' (4:14)> -> __value
            __token = 129
            try:
                __zt_tmp = __attrs_140097337625568
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('path', 'view/items', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['items'] = __value
            __backup_items_140097337634928 = get('items', __marker)

            # <Value 'python:list(items)' (5:13)> -> __value
            __token = 154
            try:
                __zt_tmp = __attrs_140097337625568
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('python', 'list(items)', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['items'] = __value
            __backup_single_checkbox_140097337634448 = get('single_checkbox', __marker)

            # <Value 'python:len(items) == 1' (6:22)> -> __value
            __token = 197
            try:
                __zt_tmp = __attrs_140097337625568
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('python', 'len(items) == 1', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['single_checkbox'] = __value
            __append('\n  ')

            # <Static value=<ast.Dict object at 0x7f6af40b2aa0> name=None at 7f6af40b2680> -> __attrs_140097338344448
            __attrs_140097338344448 = _static_140097337633440

            # <Value 'python:len(items) > 0' (10:22)> -> __condition
            __token = 277
            try:
                __zt_tmp = __attrs_140097338344448
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140097413192464('python', 'len(items) > 0', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            if __condition:

                # <Negate value=<Value 'single_checkbox' (11:21)> at 7f6af40b0a30> -> __cache_140097337625136

                # <Value 'single_checkbox' (11:21)> -> __cache_140097337625136
                __token = 324
                try:
                    __zt_tmp = __attrs_140097338344448
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140097337625136 = _static_140097413192464('path', 'single_checkbox', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                __cache_140097337625136 = not __cache_140097337625136
                __condition = __cache_140097337625136
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div')

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097337624560
                    __default_140097337624560 = _DEFAULT_MARKER

                    # <Substitution 'view/id' (13:12)> -> __attr_id
                    __token = 377
                    try:
                        __zt_tmp = __attrs_140097338344448
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_id = _static_140097413192464('path', 'view/id', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_id is not None):
                        __append((' id="%s"' % __attr_id))
                    __append(' >')
                __append('\n    ')

                # <Static value=<ast.Dict object at 0x7f6af41624a0> name=None at 7f6af4162080> -> __attrs_140097338350016
                __attrs_140097338350016 = _static_140097338352800
                __backup_item_140097338359664 = get('item', __marker)

                # <Value 'items' (17:26)> -> __iterator
                __token = 453
                try:
                    __zt_tmp = __attrs_140097338350016
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140097413192464('path', 'items', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                (__iterator, ____index_140097338350112, ) = getname('repeat')('item', __iterator)
                econtext['item'] = None
                for __item in __iterator:
                    econtext['item'] = __item

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="form-check"')

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338358176
                    __default_140097338358176 = _DEFAULT_MARKER

                    # <Substitution 'python:single_checkbox and view.id or None' (19:14)> -> __attr_id
                    __token = 500
                    try:
                        __zt_tmp = __attrs_140097338350016
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_id = _static_140097413192464('python', 'single_checkbox and view.id or None', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_id is not None):
                        __append((' id="%s"' % __attr_id))
                    __append(' >\n      ')

                    # <Static value=<ast.Dict object at 0x7f6af41367d0> name=None at 7f6af4136d40> -> __attrs_140097339907552
                    __attrs_140097339907552 = _static_140097338173392

                    # <Value 'item/checked' (32:28)> -> __condition
                    __token = 826
                    try:
                        __zt_tmp = __attrs_140097339907552
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140097413192464('path', 'item/checked', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    if __condition:

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input')

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338170656
                        __default_140097338170656 = _DEFAULT_MARKER

                        # <Substitution 'string:form-check-input ${view/klass}' (36:19)> -> __attr_class
                        __token = 947
                        try:
                            __zt_tmp = __attrs_140097339907552
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_class = _static_140097413192464('string', 'form-check-input ${view/klass}', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_class = __quote(__attr_class, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_class is not None):
                            __append((' class="%s"' % __attr_class))

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338352992
                        __default_140097338352992 = _DEFAULT_MARKER

                        # <Substitution 'item/id' (34:18)> -> __attr_id
                        __token = 888
                        try:
                            __zt_tmp = __attrs_140097339907552
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_id = _static_140097413192464('path', 'item/id', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_id = __quote(__attr_id, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_id is not None):
                            __append((' id="%s"' % __attr_id))

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338347376
                        __default_140097338347376 = _DEFAULT_MARKER

                        # <Substitution 'view/accesskey' (58:1)> -> __attr_accesskey
                        __token = 1796
                        try:
                            __zt_tmp = __attrs_140097339907552
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_accesskey = _static_140097413192464('path', 'view/accesskey', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_accesskey = __quote(__attr_accesskey, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_accesskey is not None):
                            __append((' accesskey="%s"' % __attr_accesskey))

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338356256
                        __default_140097338356256 = _DEFAULT_MARKER

                        # <Substitution 'view/alt' (56:35)> -> __attr_alt
                        __token = 1762
                        try:
                            __zt_tmp = __attrs_140097339907552
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_alt = _static_140097413192464('path', 'view/alt', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_alt = __quote(__attr_alt, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_alt is not None):
                            __append((' alt="%s"' % __attr_alt))
                        __append(' checked="checked"')

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338349200
                        __default_140097338349200 = _DEFAULT_MARKER

                        # <Substitution 'item/name' (35:19)> -> __attr_name
                        __token = 916
                        try:
                            __zt_tmp = __attrs_140097339907552
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_name = _static_140097413192464('path', 'item/name', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_name = __quote(__attr_name, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_name is not None):
                            __append((' name="%s"' % __attr_name))

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338345552
                        __default_140097338345552 = _DEFAULT_MARKER

                        # <Substitution 'view/tabindex' (52:6)> -> __attr_tabindex
                        __token = 1583
                        try:
                            __zt_tmp = __attrs_140097339907552
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_tabindex = _static_140097413192464('path', 'view/tabindex', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_tabindex = __quote(__attr_tabindex, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_tabindex is not None):
                            __append((' tabindex="%s"' % __attr_tabindex))

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338355632
                        __default_140097338355632 = _DEFAULT_MARKER

                        # <Substitution 'view/title' (39:16)> -> __attr_title
                        __token = 1070
                        try:
                            __zt_tmp = __attrs_140097339907552
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_title = _static_140097413192464('path', 'view/title', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_title = __quote(__attr_title, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_title is not None):
                            __append((' title="%s"' % __attr_title))
                        __append(' type="checkbox"')

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338349680
                        __default_140097338349680 = _DEFAULT_MARKER

                        # <Substitution 'item/value' (37:18)> -> __attr_value
                        __token = 1006
                        try:
                            __zt_tmp = __attrs_140097339907552
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_value = _static_140097413192464('path', 'item/value', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_value = __quote(__attr_value, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_value is not None):
                            __append((' value="%s"' % __attr_value))

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338354864
                        __default_140097338354864 = _DEFAULT_MARKER

                        # <Substitution 'view/style' (38:17)> -> __attr_style
                        __token = 1038
                        try:
                            __zt_tmp = __attrs_140097339907552
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_style = _static_140097413192464('path', 'view/style', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_style is not None):
                            __append((' style="%s"' % __attr_style))

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338355344
                        __default_140097338355344 = _DEFAULT_MARKER

                        # <Substitution 'view/lang' (40:14)> -> __attr_lang
                        __token = 1101
                        try:
                            __zt_tmp = __attrs_140097339907552
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_lang = _static_140097413192464('path', 'view/lang', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_lang = __quote(__attr_lang, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_lang is not None):
                            __append((' lang="%s"' % __attr_lang))

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338348048
                        __default_140097338348048 = _DEFAULT_MARKER

                        # <Substitution 'view/onclick' (41:16)> -> __attr_onclick
                        __token = 1134
                        try:
                            __zt_tmp = __attrs_140097339907552
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onclick = _static_140097413192464('path', 'view/onclick', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_onclick = __quote(__attr_onclick, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onclick is not None):
                            __append((' onclick="%s"' % __attr_onclick))

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338346944
                        __default_140097338346944 = _DEFAULT_MARKER

                        # <Substitution 'view/ondblclick' (42:18)> -> __attr_ondblclick
                        __token = 1173
                        try:
                            __zt_tmp = __attrs_140097339907552
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_ondblclick = _static_140097413192464('path', 'view/ondblclick', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_ondblclick = __quote(__attr_ondblclick, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_ondblclick is not None):
                            __append((' ondblclick="%s"' % __attr_ondblclick))

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338345216
                        __default_140097338345216 = _DEFAULT_MARKER

                        # <Substitution 'view/onmousedown' (43:18)> -> __attr_onmousedown
                        __token = 1216
                        try:
                            __zt_tmp = __attrs_140097339907552
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onmousedown = _static_140097413192464('path', 'view/onmousedown', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_onmousedown = __quote(__attr_onmousedown, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onmousedown is not None):
                            __append((' onmousedown="%s"' % __attr_onmousedown))

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338357456
                        __default_140097338357456 = _DEFAULT_MARKER

                        # <Substitution 'view/onmouseup' (44:15)> -> __attr_onmouseup
                        __token = 1258
                        try:
                            __zt_tmp = __attrs_140097339907552
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onmouseup = _static_140097413192464('path', 'view/onmouseup', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_onmouseup = __quote(__attr_onmouseup, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onmouseup is not None):
                            __append((' onmouseup="%s"' % __attr_onmouseup))

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338344208
                        __default_140097338344208 = _DEFAULT_MARKER

                        # <Substitution 'view/onmouseover' (45:16)> -> __attr_onmouseover
                        __token = 1300
                        try:
                            __zt_tmp = __attrs_140097339907552
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onmouseover = _static_140097413192464('path', 'view/onmouseover', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_onmouseover = __quote(__attr_onmouseover, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onmouseover is not None):
                            __append((' onmouseover="%s"' % __attr_onmouseover))

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097339907840
                        __default_140097339907840 = _DEFAULT_MARKER

                        # <Substitution 'view/onmousemove' (46:15)> -> __attr_onmousemove
                        __token = 1344
                        try:
                            __zt_tmp = __attrs_140097339907552
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onmousemove = _static_140097413192464('path', 'view/onmousemove', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_onmousemove = __quote(__attr_onmousemove, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onmousemove is not None):
                            __append((' onmousemove="%s"' % __attr_onmousemove))

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097339910384
                        __default_140097339910384 = _DEFAULT_MARKER

                        # <Substitution 'view/onmouseout' (47:13)> -> __attr_onmouseout
                        __token = 1387
                        try:
                            __zt_tmp = __attrs_140097339907552
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onmouseout = _static_140097413192464('path', 'view/onmouseout', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_onmouseout = __quote(__attr_onmouseout, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onmouseout is not None):
                            __append((' onmouseout="%s"' % __attr_onmouseout))

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097339911872
                        __default_140097339911872 = _DEFAULT_MARKER

                        # <Substitution 'view/onkeypress' (48:12)> -> __attr_onkeypress
                        __token = 1429
                        try:
                            __zt_tmp = __attrs_140097339907552
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onkeypress = _static_140097413192464('path', 'view/onkeypress', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_onkeypress = __quote(__attr_onkeypress, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onkeypress is not None):
                            __append((' onkeypress="%s"' % __attr_onkeypress))

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097339900448
                        __default_140097339900448 = _DEFAULT_MARKER

                        # <Substitution 'view/onkeydown' (49:10)> -> __attr_onkeydown
                        __token = 1470
                        try:
                            __zt_tmp = __attrs_140097339907552
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onkeydown = _static_140097413192464('path', 'view/onkeydown', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_onkeydown = __quote(__attr_onkeydown, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onkeydown is not None):
                            __append((' onkeydown="%s"' % __attr_onkeydown))

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097339900784
                        __default_140097339900784 = _DEFAULT_MARKER

                        # <Substitution 'view/onkeyup' (50:7)> -> __attr_onkeyup
                        __token = 1508
                        try:
                            __zt_tmp = __attrs_140097339907552
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onkeyup = _static_140097413192464('path', 'view/onkeyup', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_onkeyup = __quote(__attr_onkeyup, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onkeyup is not None):
                            __append((' onkeyup="%s"' % __attr_onkeyup))

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097339902896
                        __default_140097339902896 = _DEFAULT_MARKER

                        # <Boolean 'view/disabled' (51:7)> -> __attr_disabled
                        __token = 1545
                        try:
                            __zt_tmp = __attrs_140097339907552
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_disabled = _static_140097413192464('path', 'view/disabled', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        if (__attr_disabled is _DEFAULT_MARKER):
                            __attr_disabled = None
                        else:
                            if __attr_disabled:
                                __attr_disabled = 'disabled'
                            else:
                                __attr_disabled = None
                        if (__attr_disabled is not None):
                            __append((' disabled="%s"' % __attr_disabled))

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097339915472
                        __default_140097339915472 = _DEFAULT_MARKER

                        # <Substitution 'view/onfocus' (53:4)> -> __attr_onfocus
                        __token = 1620
                        try:
                            __zt_tmp = __attrs_140097339907552
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onfocus = _static_140097413192464('path', 'view/onfocus', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_onfocus = __quote(__attr_onfocus, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onfocus is not None):
                            __append((' onfocus="%s"' % __attr_onfocus))

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097339913456
                        __default_140097339913456 = _DEFAULT_MARKER

                        # <Substitution 'view/onblur' (54:2)> -> __attr_onblur
                        __token = 1655
                        try:
                            __zt_tmp = __attrs_140097339907552
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onblur = _static_140097413192464('path', 'view/onblur', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_onblur = __quote(__attr_onblur, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onblur is not None):
                            __append((' onblur="%s"' % __attr_onblur))

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097339902752
                        __default_140097339902752 = _DEFAULT_MARKER

                        # <Substitution 'view/onchange' (55:3)> -> __attr_onchange
                        __token = 1691
                        try:
                            __zt_tmp = __attrs_140097339907552
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onchange = _static_140097413192464('path', 'view/onchange', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_onchange = __quote(__attr_onchange, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onchange is not None):
                            __append((' onchange="%s"' % __attr_onchange))

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097339911104
                        __default_140097339911104 = _DEFAULT_MARKER

                        # <Boolean 'view/readonly' (56:2)> -> __attr_readonly
                        __token = 1729
                        try:
                            __zt_tmp = __attrs_140097339907552
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_readonly = _static_140097413192464('path', 'view/readonly', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        if (__attr_readonly is _DEFAULT_MARKER):
                            __attr_readonly = None
                        else:
                            if __attr_readonly:
                                __attr_readonly = 'readonly'
                            else:
                                __attr_readonly = None
                        if (__attr_readonly is not None):
                            __append((' readonly="%s"' % __attr_readonly))

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097339907504
                        __default_140097339907504 = _DEFAULT_MARKER

                        # <Substitution 'view/onselect' (58:40)> -> __attr_onselect
                        __token = 1835
                        try:
                            __zt_tmp = __attrs_140097339907552
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onselect = _static_140097413192464('path', 'view/onselect', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_onselect = __quote(__attr_onselect, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onselect is not None):
                            __append((' onselect="%s"' % __attr_onselect))
                        __append(' />')

                    # <Static value=<ast.Dict object at 0x7f6af42dec50> name=None at 7f6af42dff40> -> __attrs_140097252670384
                    __attrs_140097252670384 = _static_140097339911248

                    # <Value 'not:item/checked' (70:28)> -> __condition
                    __token = 2126
                    try:
                        __zt_tmp = __attrs_140097252670384
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140097413192464('not', 'item/checked', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    if __condition:

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input')

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097339914128
                        __default_140097339914128 = _DEFAULT_MARKER

                        # <Substitution 'string:form-check-input ${view/klass}' (74:19)> -> __attr_class
                        __token = 2251
                        try:
                            __zt_tmp = __attrs_140097252670384
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_class = _static_140097413192464('string', 'form-check-input ${view/klass}', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_class = __quote(__attr_class, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_class is not None):
                            __append((' class="%s"' % __attr_class))

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252656944
                        __default_140097252656944 = _DEFAULT_MARKER

                        # <Substitution 'item/id' (72:18)> -> __attr_id
                        __token = 2192
                        try:
                            __zt_tmp = __attrs_140097252670384
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_id = _static_140097413192464('path', 'item/id', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_id = __quote(__attr_id, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_id is not None):
                            __append((' id="%s"' % __attr_id))

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252661264
                        __default_140097252661264 = _DEFAULT_MARKER

                        # <Substitution 'view/accesskey' (96:1)> -> __attr_accesskey
                        __token = 3100
                        try:
                            __zt_tmp = __attrs_140097252670384
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_accesskey = _static_140097413192464('path', 'view/accesskey', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_accesskey = __quote(__attr_accesskey, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_accesskey is not None):
                            __append((' accesskey="%s"' % __attr_accesskey))

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252666208
                        __default_140097252666208 = _DEFAULT_MARKER

                        # <Substitution 'view/alt' (94:35)> -> __attr_alt
                        __token = 3066
                        try:
                            __zt_tmp = __attrs_140097252670384
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_alt = _static_140097413192464('path', 'view/alt', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_alt = __quote(__attr_alt, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_alt is not None):
                            __append((' alt="%s"' % __attr_alt))

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252661936
                        __default_140097252661936 = _DEFAULT_MARKER

                        # <Substitution 'item/name' (73:19)> -> __attr_name
                        __token = 2220
                        try:
                            __zt_tmp = __attrs_140097252670384
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_name = _static_140097413192464('path', 'item/name', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_name = __quote(__attr_name, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_name is not None):
                            __append((' name="%s"' % __attr_name))

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252664720
                        __default_140097252664720 = _DEFAULT_MARKER

                        # <Substitution 'view/tabindex' (90:6)> -> __attr_tabindex
                        __token = 2887
                        try:
                            __zt_tmp = __attrs_140097252670384
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_tabindex = _static_140097413192464('path', 'view/tabindex', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_tabindex = __quote(__attr_tabindex, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_tabindex is not None):
                            __append((' tabindex="%s"' % __attr_tabindex))

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252665632
                        __default_140097252665632 = _DEFAULT_MARKER

                        # <Substitution 'view/title' (77:16)> -> __attr_title
                        __token = 2374
                        try:
                            __zt_tmp = __attrs_140097252670384
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_title = _static_140097413192464('path', 'view/title', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_title = __quote(__attr_title, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_title is not None):
                            __append((' title="%s"' % __attr_title))
                        __append(' type="checkbox"')

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252669808
                        __default_140097252669808 = _DEFAULT_MARKER

                        # <Substitution 'item/value' (75:18)> -> __attr_value
                        __token = 2310
                        try:
                            __zt_tmp = __attrs_140097252670384
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_value = _static_140097413192464('path', 'item/value', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_value = __quote(__attr_value, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_value is not None):
                            __append((' value="%s"' % __attr_value))

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252664000
                        __default_140097252664000 = _DEFAULT_MARKER

                        # <Substitution 'view/style' (76:17)> -> __attr_style
                        __token = 2342
                        try:
                            __zt_tmp = __attrs_140097252670384
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_style = _static_140097413192464('path', 'view/style', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_style is not None):
                            __append((' style="%s"' % __attr_style))

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252660064
                        __default_140097252660064 = _DEFAULT_MARKER

                        # <Substitution 'view/lang' (78:14)> -> __attr_lang
                        __token = 2405
                        try:
                            __zt_tmp = __attrs_140097252670384
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_lang = _static_140097413192464('path', 'view/lang', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_lang = __quote(__attr_lang, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_lang is not None):
                            __append((' lang="%s"' % __attr_lang))

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252657232
                        __default_140097252657232 = _DEFAULT_MARKER

                        # <Substitution 'view/onclick' (79:16)> -> __attr_onclick
                        __token = 2438
                        try:
                            __zt_tmp = __attrs_140097252670384
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onclick = _static_140097413192464('path', 'view/onclick', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_onclick = __quote(__attr_onclick, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onclick is not None):
                            __append((' onclick="%s"' % __attr_onclick))

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252656272
                        __default_140097252656272 = _DEFAULT_MARKER

                        # <Substitution 'view/ondblclick' (80:18)> -> __attr_ondblclick
                        __token = 2477
                        try:
                            __zt_tmp = __attrs_140097252670384
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_ondblclick = _static_140097413192464('path', 'view/ondblclick', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_ondblclick = __quote(__attr_ondblclick, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_ondblclick is not None):
                            __append((' ondblclick="%s"' % __attr_ondblclick))

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252662560
                        __default_140097252662560 = _DEFAULT_MARKER

                        # <Substitution 'view/onmousedown' (81:18)> -> __attr_onmousedown
                        __token = 2520
                        try:
                            __zt_tmp = __attrs_140097252670384
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onmousedown = _static_140097413192464('path', 'view/onmousedown', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_onmousedown = __quote(__attr_onmousedown, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onmousedown is not None):
                            __append((' onmousedown="%s"' % __attr_onmousedown))

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252669904
                        __default_140097252669904 = _DEFAULT_MARKER

                        # <Substitution 'view/onmouseup' (82:15)> -> __attr_onmouseup
                        __token = 2562
                        try:
                            __zt_tmp = __attrs_140097252670384
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onmouseup = _static_140097413192464('path', 'view/onmouseup', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_onmouseup = __quote(__attr_onmouseup, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onmouseup is not None):
                            __append((' onmouseup="%s"' % __attr_onmouseup))

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252658144
                        __default_140097252658144 = _DEFAULT_MARKER

                        # <Substitution 'view/onmouseover' (83:16)> -> __attr_onmouseover
                        __token = 2604
                        try:
                            __zt_tmp = __attrs_140097252670384
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onmouseover = _static_140097413192464('path', 'view/onmouseover', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_onmouseover = __quote(__attr_onmouseover, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onmouseover is not None):
                            __append((' onmouseover="%s"' % __attr_onmouseover))

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252664960
                        __default_140097252664960 = _DEFAULT_MARKER

                        # <Substitution 'view/onmousemove' (84:15)> -> __attr_onmousemove
                        __token = 2648
                        try:
                            __zt_tmp = __attrs_140097252670384
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onmousemove = _static_140097413192464('path', 'view/onmousemove', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_onmousemove = __quote(__attr_onmousemove, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onmousemove is not None):
                            __append((' onmousemove="%s"' % __attr_onmousemove))

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252665296
                        __default_140097252665296 = _DEFAULT_MARKER

                        # <Substitution 'view/onmouseout' (85:13)> -> __attr_onmouseout
                        __token = 2691
                        try:
                            __zt_tmp = __attrs_140097252670384
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onmouseout = _static_140097413192464('path', 'view/onmouseout', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_onmouseout = __quote(__attr_onmouseout, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onmouseout is not None):
                            __append((' onmouseout="%s"' % __attr_onmouseout))

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252656320
                        __default_140097252656320 = _DEFAULT_MARKER

                        # <Substitution 'view/onkeypress' (86:12)> -> __attr_onkeypress
                        __token = 2733
                        try:
                            __zt_tmp = __attrs_140097252670384
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onkeypress = _static_140097413192464('path', 'view/onkeypress', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_onkeypress = __quote(__attr_onkeypress, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onkeypress is not None):
                            __append((' onkeypress="%s"' % __attr_onkeypress))

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252663424
                        __default_140097252663424 = _DEFAULT_MARKER

                        # <Substitution 'view/onkeydown' (87:10)> -> __attr_onkeydown
                        __token = 2774
                        try:
                            __zt_tmp = __attrs_140097252670384
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onkeydown = _static_140097413192464('path', 'view/onkeydown', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_onkeydown = __quote(__attr_onkeydown, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onkeydown is not None):
                            __append((' onkeydown="%s"' % __attr_onkeydown))

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252662464
                        __default_140097252662464 = _DEFAULT_MARKER

                        # <Substitution 'view/onkeyup' (88:7)> -> __attr_onkeyup
                        __token = 2812
                        try:
                            __zt_tmp = __attrs_140097252670384
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onkeyup = _static_140097413192464('path', 'view/onkeyup', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_onkeyup = __quote(__attr_onkeyup, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onkeyup is not None):
                            __append((' onkeyup="%s"' % __attr_onkeyup))

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252659728
                        __default_140097252659728 = _DEFAULT_MARKER

                        # <Boolean 'view/disabled' (89:7)> -> __attr_disabled
                        __token = 2849
                        try:
                            __zt_tmp = __attrs_140097252670384
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_disabled = _static_140097413192464('path', 'view/disabled', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        if (__attr_disabled is _DEFAULT_MARKER):
                            __attr_disabled = None
                        else:
                            if __attr_disabled:
                                __attr_disabled = 'disabled'
                            else:
                                __attr_disabled = None
                        if (__attr_disabled is not None):
                            __append((' disabled="%s"' % __attr_disabled))

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252657664
                        __default_140097252657664 = _DEFAULT_MARKER

                        # <Substitution 'view/onfocus' (91:4)> -> __attr_onfocus
                        __token = 2924
                        try:
                            __zt_tmp = __attrs_140097252670384
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onfocus = _static_140097413192464('path', 'view/onfocus', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_onfocus = __quote(__attr_onfocus, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onfocus is not None):
                            __append((' onfocus="%s"' % __attr_onfocus))

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252656128
                        __default_140097252656128 = _DEFAULT_MARKER

                        # <Substitution 'view/onblur' (92:2)> -> __attr_onblur
                        __token = 2959
                        try:
                            __zt_tmp = __attrs_140097252670384
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onblur = _static_140097413192464('path', 'view/onblur', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_onblur = __quote(__attr_onblur, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onblur is not None):
                            __append((' onblur="%s"' % __attr_onblur))

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252657280
                        __default_140097252657280 = _DEFAULT_MARKER

                        # <Substitution 'view/onchange' (93:3)> -> __attr_onchange
                        __token = 2995
                        try:
                            __zt_tmp = __attrs_140097252670384
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onchange = _static_140097413192464('path', 'view/onchange', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_onchange = __quote(__attr_onchange, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onchange is not None):
                            __append((' onchange="%s"' % __attr_onchange))

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252655600
                        __default_140097252655600 = _DEFAULT_MARKER

                        # <Boolean 'view/readonly' (94:2)> -> __attr_readonly
                        __token = 3033
                        try:
                            __zt_tmp = __attrs_140097252670384
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_readonly = _static_140097413192464('path', 'view/readonly', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        if (__attr_readonly is _DEFAULT_MARKER):
                            __attr_readonly = None
                        else:
                            if __attr_readonly:
                                __attr_readonly = 'readonly'
                            else:
                                __attr_readonly = None
                        if (__attr_readonly is not None):
                            __append((' readonly="%s"' % __attr_readonly))

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252670432
                        __default_140097252670432 = _DEFAULT_MARKER

                        # <Substitution 'view/onselect' (96:40)> -> __attr_onselect
                        __token = 3139
                        try:
                            __zt_tmp = __attrs_140097252670384
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onselect = _static_140097413192464('path', 'view/onselect', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_onselect = __quote(__attr_onselect, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onselect is not None):
                            __append((' onselect="%s"' % __attr_onselect))
                        __append(' />')
                    __append('\n      ')

                    # <Static value=<ast.Dict object at 0x7f6aeefa9990> name=None at 7f6aeefa9510> -> __attrs_140097252661360
                    __attrs_140097252661360 = _static_140097252661648

                    # <label ... (0:0)
                    # --------------------------------------------------------
                    __append('<label class="form-check-label"')

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252670144
                    __default_140097252670144 = _DEFAULT_MARKER

                    # <Substitution 'item/id' (103:19)> -> __attr_for
                    __token = 3310
                    try:
                        __zt_tmp = __attrs_140097252661360
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_for = _static_140097413192464('path', 'item/id', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    __attr_for = __quote(__attr_for, '"', '&quot;', '', _DEFAULT_MARKER)
                    if (__attr_for is not None):
                        __append((' for="%s"' % __attr_for))
                    __append(' >\n        ')

                    # <Static value=<ast.Dict object at 0x7f6aeefa8970> name=None at 7f6aeefa9450> -> __attrs_140097252671152
                    __attrs_140097252671152 = _static_140097252657520

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span class="label" >')

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252663184
                    __default_140097252663184 = _DEFAULT_MARKER

                    # <Value 'item/label' (107:27)> -> __cache_140097252667120
                    __token = 3397
                    try:
                        __zt_tmp = __attrs_140097252671152
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140097252667120 = _static_140097413192464('path', 'item/label', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                    # <BinOp left=<Value 'item/label' (107:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeefa9270> -> __condition
                    __expression = __cache_140097252667120

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('Label')
                    else:
                        __content = __cache_140097252667120
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</span>\n      </label>\n    </div>')
                    ____index_140097338350112 -= 1
                    if (____index_140097338350112 > 0):
                        __append('\n    ')
                if (__backup_item_140097338359664 is __marker):
                    del econtext['item']
                else:
                    econtext['item'] = __backup_item_140097338359664
                __append('\n  ')
                __condition = __cache_140097337625136
                if __condition:
                    __append('</div>')
            __append('\n  ')

            # <Static value=<ast.Dict object at 0x7f6af5ac7b80> name=None at 7f6af5ac77f0> -> __attrs_140097364277088
            __attrs_140097364277088 = _static_140097364982656

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input')

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252669472
            __default_140097252669472 = _DEFAULT_MARKER

            # <Substitution 'string:${view/name}-empty-marker' (116:16)> -> __attr_name
            __token = 3585
            try:
                __zt_tmp = __attrs_140097364277088
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_name = _static_140097413192464('string', '${view/name}-empty-marker', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_name = __quote(__attr_name, '"', '&quot;', 'field-empty-marker', _DEFAULT_MARKER)
            if (__attr_name is not None):
                __append((' name="%s"' % __attr_name))
            __append(' type="hidden" value="1" />\n')
            if (__backup_single_checkbox_140097337634448 is __marker):
                del econtext['single_checkbox']
            else:
                econtext['single_checkbox'] = __backup_single_checkbox_140097337634448
            if (__backup_items_140097337634928 is __marker):
                del econtext['items']
            else:
                econtext['items'] = __backup_items_140097337634928
            if (__backup_items_140097337624464 is __marker):
                del econtext['items']
            else:
                econtext['items'] = __backup_items_140097337624464
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }