# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/plone/app/z3cform/templates/radio_input_single.pt'

__tokens = {128: ('python:args[0]', 4, 13), 384: ('item/checked', 18, 19), 500: ('s string:form-check-input ${view/klas', 23, 15), 449: ('item/id', 21, 14), 1261: ('t;\n           ', 44, 22), 1231: ('adonly;\n', 43, 27), 473: (' item/nam', 22, 15), 1072: ('         tabi', 39, 2), 611: ('itle view/', 26, 12), 555: ('ue item/va', 24, 14), 583: ('yle view/s', 25, 13), 638: (' lang vie', 27, 10), 667: ('nclick view/', 28, 12), 702: ('blclick view/on', 29, 14), 741: ('ousedown view/on', 30, 14), 779: ('onmouseup view', 31, 11), 817: ('nmouseover view/', 32, 12), 857: ('onmousemove view', 33, 11), 896: ('  onmouseout vi', 34, 9), 934: ('   onkeypress v', 35, 8), 971: ('     onkeydown', 36, 6), 1005: ('        onke', 37, 3), 1038: ('        disab', 38, 3), 1105: ('           o', 40, 0), 1136: (';\n         ', 40, 31), 1168: ('\n           o', 41, 30), 1202: (';\n           ', 42, 33), 1296: ('key;\n        ', 45, 32), 1329: ('elect;\n           checked python: che', 46, 28)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139906201064192 = {'class': '', 'id': '', 'accesskey': '', 'alt': '', 'name': '', 'tabindex': '', 'title': '', 'type': 'radio', 'value': '', 'style': 'view/style', 'lang': 'view/lang', 'onclick': 'view/onclick', 'ondblclick': 'view/ondblclick', 'onmousedown': 'view/onmousedown', 'onmouseup': 'view/onmouseup', 'onmouseover': 'view/onmouseover', 'onmousemove': 'view/onmousemove', 'onmouseout': 'view/onmouseout', 'onkeypress': 'view/onkeypress', 'onkeydown': 'view/onkeydown', 'onkeyup': 'view/onkeyup', 'disabled': 'view/disabled', 'onfocus': 'view/onfocus', 'onblur': 'view/onblur', 'onchange': 'view/onchange', 'readonly': 'view/readonly', 'onselect': 'view/onselect', 'checked': "python: checked and 'checked' or None", }
_static_139906490555248 = __C2ZContextWrapper
_static_139906490555536 = __compile_zt_expr
_static_139906201073840 = {'xmlns': 'http://www.w3.org/1999/xhtml', }

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

            # <Static value=<ast.Dict object at 0x7f3e736ab8b0> name=None at 7f3e736ab700> -> __attrs_139906201074080
            __attrs_139906201074080 = _static_139906201073840
            __backup_item_139906200870608 = get('item', __marker)

            # <Value 'python:args[0]' (4:13)> -> __value
            __token = 128
            try:
                __zt_tmp = __attrs_139906201074080
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139906490555536('python', 'args[0]', econtext=econtext)(_static_139906490555248(econtext, __zt_tmp))
            econtext['item'] = __value
            __append('\n  ')

            # <Static value=<ast.Dict object at 0x7f3e736a9300> name=None at 7f3e736a9360> -> __attrs_139906201009456
            __attrs_139906201009456 = _static_139906201064192
            __backup_checked_139906200994048 = get('checked', __marker)

            # <Value 'item/checked' (18:19)> -> __value
            __token = 384
            try:
                __zt_tmp = __attrs_139906201009456
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139906490555536('path', 'item/checked', econtext=econtext)(_static_139906490555248(econtext, __zt_tmp))
            econtext['checked'] = __value

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input')

            # <Symbol value=<DEFAULT> at 7f3e84a07cd0> -> __default_139906201075232
            __default_139906201075232 = _DEFAULT_MARKER

            # <Substitution 'string:form-check-input ${view/klass}' (23:15)> -> __attr_class
            __token = 500
            try:
                __zt_tmp = __attrs_139906201009456
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_139906490555536('string', 'form-check-input ${view/klass}', econtext=econtext)(_static_139906490555248(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((' class="%s"' % __attr_class))

            # <Symbol value=<DEFAULT> at 7f3e84a07cd0> -> __default_139906201069040
            __default_139906201069040 = _DEFAULT_MARKER

            # <Substitution 'item/id' (21:14)> -> __attr_id
            __token = 449
            try:
                __zt_tmp = __attrs_139906201009456
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_139906490555536('path', 'item/id', econtext=econtext)(_static_139906490555248(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_id is not None):
                __append((' id="%s"' % __attr_id))

            # <Symbol value=<DEFAULT> at 7f3e84a07cd0> -> __default_139906201067504
            __default_139906201067504 = _DEFAULT_MARKER

            # <Substitution 'view/accesskey' (44:22)> -> __attr_accesskey
            __token = 1261
            try:
                __zt_tmp = __attrs_139906201009456
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_accesskey = _static_139906490555536('path', 'view/accesskey', econtext=econtext)(_static_139906490555248(econtext, __zt_tmp))
            __attr_accesskey = __quote(__attr_accesskey, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_accesskey is not None):
                __append((' accesskey="%s"' % __attr_accesskey))

            # <Symbol value=<DEFAULT> at 7f3e84a07cd0> -> __default_139906201068320
            __default_139906201068320 = _DEFAULT_MARKER

            # <Substitution 'view/alt' (43:27)> -> __attr_alt
            __token = 1231
            try:
                __zt_tmp = __attrs_139906201009456
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_alt = _static_139906490555536('path', 'view/alt', econtext=econtext)(_static_139906490555248(econtext, __zt_tmp))
            __attr_alt = __quote(__attr_alt, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_alt is not None):
                __append((' alt="%s"' % __attr_alt))

            # <Symbol value=<DEFAULT> at 7f3e84a07cd0> -> __default_139906201061312
            __default_139906201061312 = _DEFAULT_MARKER

            # <Substitution 'item/name' (22:15)> -> __attr_name
            __token = 473
            try:
                __zt_tmp = __attrs_139906201009456
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_name = _static_139906490555536('path', 'item/name', econtext=econtext)(_static_139906490555248(econtext, __zt_tmp))
            __attr_name = __quote(__attr_name, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_name is not None):
                __append((' name="%s"' % __attr_name))

            # <Symbol value=<DEFAULT> at 7f3e84a07cd0> -> __default_139906201059968
            __default_139906201059968 = _DEFAULT_MARKER

            # <Substitution 'view/tabindex' (39:2)> -> __attr_tabindex
            __token = 1072
            try:
                __zt_tmp = __attrs_139906201009456
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_tabindex = _static_139906490555536('path', 'view/tabindex', econtext=econtext)(_static_139906490555248(econtext, __zt_tmp))
            __attr_tabindex = __quote(__attr_tabindex, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_tabindex is not None):
                __append((' tabindex="%s"' % __attr_tabindex))

            # <Symbol value=<DEFAULT> at 7f3e84a07cd0> -> __default_139906201068080
            __default_139906201068080 = _DEFAULT_MARKER

            # <Substitution 'view/title' (26:12)> -> __attr_title
            __token = 611
            try:
                __zt_tmp = __attrs_139906201009456
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_title = _static_139906490555536('path', 'view/title', econtext=econtext)(_static_139906490555248(econtext, __zt_tmp))
            __attr_title = __quote(__attr_title, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_title is not None):
                __append((' title="%s"' % __attr_title))
            __append(' type="radio"')

            # <Symbol value=<DEFAULT> at 7f3e84a07cd0> -> __default_139906201061024
            __default_139906201061024 = _DEFAULT_MARKER

            # <Substitution 'item/value' (24:14)> -> __attr_value
            __token = 555
            try:
                __zt_tmp = __attrs_139906201009456
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_value = _static_139906490555536('path', 'item/value', econtext=econtext)(_static_139906490555248(econtext, __zt_tmp))
            __attr_value = __quote(__attr_value, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_value is not None):
                __append((' value="%s"' % __attr_value))

            # <Symbol value=<DEFAULT> at 7f3e84a07cd0> -> __default_139906201067216
            __default_139906201067216 = _DEFAULT_MARKER

            # <Substitution 'view/style' (25:13)> -> __attr_style
            __token = 583
            try:
                __zt_tmp = __attrs_139906201009456
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_style = _static_139906490555536('path', 'view/style', econtext=econtext)(_static_139906490555248(econtext, __zt_tmp))
            __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_style is not None):
                __append((' style="%s"' % __attr_style))

            # <Symbol value=<DEFAULT> at 7f3e84a07cd0> -> __default_139906201068416
            __default_139906201068416 = _DEFAULT_MARKER

            # <Substitution 'view/lang' (27:10)> -> __attr_lang
            __token = 638
            try:
                __zt_tmp = __attrs_139906201009456
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_lang = _static_139906490555536('path', 'view/lang', econtext=econtext)(_static_139906490555248(econtext, __zt_tmp))
            __attr_lang = __quote(__attr_lang, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_lang is not None):
                __append((' lang="%s"' % __attr_lang))

            # <Symbol value=<DEFAULT> at 7f3e84a07cd0> -> __default_139906201067936
            __default_139906201067936 = _DEFAULT_MARKER

            # <Substitution 'view/onclick' (28:12)> -> __attr_onclick
            __token = 667
            try:
                __zt_tmp = __attrs_139906201009456
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onclick = _static_139906490555536('path', 'view/onclick', econtext=econtext)(_static_139906490555248(econtext, __zt_tmp))
            __attr_onclick = __quote(__attr_onclick, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onclick is not None):
                __append((' onclick="%s"' % __attr_onclick))

            # <Symbol value=<DEFAULT> at 7f3e84a07cd0> -> __default_139906201068752
            __default_139906201068752 = _DEFAULT_MARKER

            # <Substitution 'view/ondblclick' (29:14)> -> __attr_ondblclick
            __token = 702
            try:
                __zt_tmp = __attrs_139906201009456
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_ondblclick = _static_139906490555536('path', 'view/ondblclick', econtext=econtext)(_static_139906490555248(econtext, __zt_tmp))
            __attr_ondblclick = __quote(__attr_ondblclick, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_ondblclick is not None):
                __append((' ondblclick="%s"' % __attr_ondblclick))

            # <Symbol value=<DEFAULT> at 7f3e84a07cd0> -> __default_139906201069424
            __default_139906201069424 = _DEFAULT_MARKER

            # <Substitution 'view/onmousedown' (30:14)> -> __attr_onmousedown
            __token = 741
            try:
                __zt_tmp = __attrs_139906201009456
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmousedown = _static_139906490555536('path', 'view/onmousedown', econtext=econtext)(_static_139906490555248(econtext, __zt_tmp))
            __attr_onmousedown = __quote(__attr_onmousedown, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmousedown is not None):
                __append((' onmousedown="%s"' % __attr_onmousedown))

            # <Symbol value=<DEFAULT> at 7f3e84a07cd0> -> __default_139906201075664
            __default_139906201075664 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseup' (31:11)> -> __attr_onmouseup
            __token = 779
            try:
                __zt_tmp = __attrs_139906201009456
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseup = _static_139906490555536('path', 'view/onmouseup', econtext=econtext)(_static_139906490555248(econtext, __zt_tmp))
            __attr_onmouseup = __quote(__attr_onmouseup, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseup is not None):
                __append((' onmouseup="%s"' % __attr_onmouseup))

            # <Symbol value=<DEFAULT> at 7f3e84a07cd0> -> __default_139906201075376
            __default_139906201075376 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseover' (32:12)> -> __attr_onmouseover
            __token = 817
            try:
                __zt_tmp = __attrs_139906201009456
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseover = _static_139906490555536('path', 'view/onmouseover', econtext=econtext)(_static_139906490555248(econtext, __zt_tmp))
            __attr_onmouseover = __quote(__attr_onmouseover, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseover is not None):
                __append((' onmouseover="%s"' % __attr_onmouseover))

            # <Symbol value=<DEFAULT> at 7f3e84a07cd0> -> __default_139906201069760
            __default_139906201069760 = _DEFAULT_MARKER

            # <Substitution 'view/onmousemove' (33:11)> -> __attr_onmousemove
            __token = 857
            try:
                __zt_tmp = __attrs_139906201009456
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmousemove = _static_139906490555536('path', 'view/onmousemove', econtext=econtext)(_static_139906490555248(econtext, __zt_tmp))
            __attr_onmousemove = __quote(__attr_onmousemove, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmousemove is not None):
                __append((' onmousemove="%s"' % __attr_onmousemove))

            # <Symbol value=<DEFAULT> at 7f3e84a07cd0> -> __default_139906201070144
            __default_139906201070144 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseout' (34:9)> -> __attr_onmouseout
            __token = 896
            try:
                __zt_tmp = __attrs_139906201009456
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseout = _static_139906490555536('path', 'view/onmouseout', econtext=econtext)(_static_139906490555248(econtext, __zt_tmp))
            __attr_onmouseout = __quote(__attr_onmouseout, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseout is not None):
                __append((' onmouseout="%s"' % __attr_onmouseout))

            # <Symbol value=<DEFAULT> at 7f3e84a07cd0> -> __default_139906201060352
            __default_139906201060352 = _DEFAULT_MARKER

            # <Substitution 'view/onkeypress' (35:8)> -> __attr_onkeypress
            __token = 934
            try:
                __zt_tmp = __attrs_139906201009456
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeypress = _static_139906490555536('path', 'view/onkeypress', econtext=econtext)(_static_139906490555248(econtext, __zt_tmp))
            __attr_onkeypress = __quote(__attr_onkeypress, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeypress is not None):
                __append((' onkeypress="%s"' % __attr_onkeypress))

            # <Symbol value=<DEFAULT> at 7f3e84a07cd0> -> __default_139906201066736
            __default_139906201066736 = _DEFAULT_MARKER

            # <Substitution 'view/onkeydown' (36:6)> -> __attr_onkeydown
            __token = 971
            try:
                __zt_tmp = __attrs_139906201009456
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeydown = _static_139906490555536('path', 'view/onkeydown', econtext=econtext)(_static_139906490555248(econtext, __zt_tmp))
            __attr_onkeydown = __quote(__attr_onkeydown, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeydown is not None):
                __append((' onkeydown="%s"' % __attr_onkeydown))

            # <Symbol value=<DEFAULT> at 7f3e84a07cd0> -> __default_139906201064912
            __default_139906201064912 = _DEFAULT_MARKER

            # <Substitution 'view/onkeyup' (37:3)> -> __attr_onkeyup
            __token = 1005
            try:
                __zt_tmp = __attrs_139906201009456
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeyup = _static_139906490555536('path', 'view/onkeyup', econtext=econtext)(_static_139906490555248(econtext, __zt_tmp))
            __attr_onkeyup = __quote(__attr_onkeyup, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeyup is not None):
                __append((' onkeyup="%s"' % __attr_onkeyup))

            # <Symbol value=<DEFAULT> at 7f3e84a07cd0> -> __default_139906201065536
            __default_139906201065536 = _DEFAULT_MARKER

            # <Boolean 'view/disabled' (38:3)> -> __attr_disabled
            __token = 1038
            try:
                __zt_tmp = __attrs_139906201009456
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_disabled = _static_139906490555536('path', 'view/disabled', econtext=econtext)(_static_139906490555248(econtext, __zt_tmp))
            if (__attr_disabled is _DEFAULT_MARKER):
                __attr_disabled = None
            else:
                if __attr_disabled:
                    __attr_disabled = 'disabled'
                else:
                    __attr_disabled = None
            if (__attr_disabled is not None):
                __append((' disabled="%s"' % __attr_disabled))

            # <Symbol value=<DEFAULT> at 7f3e84a07cd0> -> __default_139906201065200
            __default_139906201065200 = _DEFAULT_MARKER

            # <Substitution 'view/onfocus' (40:0)> -> __attr_onfocus
            __token = 1105
            try:
                __zt_tmp = __attrs_139906201009456
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onfocus = _static_139906490555536('path', 'view/onfocus', econtext=econtext)(_static_139906490555248(econtext, __zt_tmp))
            __attr_onfocus = __quote(__attr_onfocus, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onfocus is not None):
                __append((' onfocus="%s"' % __attr_onfocus))

            # <Symbol value=<DEFAULT> at 7f3e84a07cd0> -> __default_139906201065056
            __default_139906201065056 = _DEFAULT_MARKER

            # <Substitution 'view/onblur' (40:31)> -> __attr_onblur
            __token = 1136
            try:
                __zt_tmp = __attrs_139906201009456
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onblur = _static_139906490555536('path', 'view/onblur', econtext=econtext)(_static_139906490555248(econtext, __zt_tmp))
            __attr_onblur = __quote(__attr_onblur, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onblur is not None):
                __append((' onblur="%s"' % __attr_onblur))

            # <Symbol value=<DEFAULT> at 7f3e84a07cd0> -> __default_139906201065872
            __default_139906201065872 = _DEFAULT_MARKER

            # <Substitution 'view/onchange' (41:30)> -> __attr_onchange
            __token = 1168
            try:
                __zt_tmp = __attrs_139906201009456
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onchange = _static_139906490555536('path', 'view/onchange', econtext=econtext)(_static_139906490555248(econtext, __zt_tmp))
            __attr_onchange = __quote(__attr_onchange, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onchange is not None):
                __append((' onchange="%s"' % __attr_onchange))

            # <Symbol value=<DEFAULT> at 7f3e84a07cd0> -> __default_139906201061072
            __default_139906201061072 = _DEFAULT_MARKER

            # <Boolean 'view/readonly' (42:33)> -> __attr_readonly
            __token = 1202
            try:
                __zt_tmp = __attrs_139906201009456
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_readonly = _static_139906490555536('path', 'view/readonly', econtext=econtext)(_static_139906490555248(econtext, __zt_tmp))
            if (__attr_readonly is _DEFAULT_MARKER):
                __attr_readonly = None
            else:
                if __attr_readonly:
                    __attr_readonly = 'readonly'
                else:
                    __attr_readonly = None
            if (__attr_readonly is not None):
                __append((' readonly="%s"' % __attr_readonly))

            # <Symbol value=<DEFAULT> at 7f3e84a07cd0> -> __default_139906201059632
            __default_139906201059632 = _DEFAULT_MARKER

            # <Substitution 'view/onselect' (45:32)> -> __attr_onselect
            __token = 1296
            try:
                __zt_tmp = __attrs_139906201009456
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onselect = _static_139906490555536('path', 'view/onselect', econtext=econtext)(_static_139906490555248(econtext, __zt_tmp))
            __attr_onselect = __quote(__attr_onselect, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onselect is not None):
                __append((' onselect="%s"' % __attr_onselect))

            # <Symbol value=<DEFAULT> at 7f3e84a07cd0> -> __default_139906201066016
            __default_139906201066016 = _DEFAULT_MARKER

            # <Boolean "python: checked and 'checked' or None" (46:28)> -> __attr_checked
            __token = 1329
            try:
                __zt_tmp = __attrs_139906201009456
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_checked = _static_139906490555536('python', " checked and 'checked' or None", econtext=econtext)(_static_139906490555248(econtext, __zt_tmp))
            if (__attr_checked is _DEFAULT_MARKER):
                __attr_checked = None
            else:
                if __attr_checked:
                    __attr_checked = 'checked'
                else:
                    __attr_checked = None
            if (__attr_checked is not None):
                __append((' checked="%s"' % __attr_checked))
            __append(' />')
            if (__backup_checked_139906200994048 is __marker):
                del econtext['checked']
            else:
                econtext['checked'] = __backup_checked_139906200994048
            __append('\n')
            if (__backup_item_139906200870608 is __marker):
                del econtext['item']
            else:
                econtext['item'] = __backup_item_139906200870608
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }