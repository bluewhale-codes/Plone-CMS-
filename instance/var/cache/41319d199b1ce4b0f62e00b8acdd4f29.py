# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/plone/app/z3cform/templates/textarea_input.pt'

__tokens = {475: ('ss string:form-control ${view/kla', 17, 17), 351: ('view/id', 14, 17), 1298: ('\n             ', 38, 37), 1198: ('e;\n      ', 35, 35), 378: (' view/nam', 15, 18), 1227: ('ls;\n     ', 36, 26), 1060: ('         tabi', 32, 5), 411: ("d python:view.required and 'required' or No", 16, 21), 529: ('yle view/s', 18, 16), 560: ('itle view/', 19, 15), 590: (' lang vie', 20, 13), 622: ('nclick view/', 21, 15), 660: ('blclick view/on', 22, 17), 702: ('ousedown view/on', 23, 17), 743: ('onmouseup view', 24, 14), 784: ('nmouseover view/', 25, 15), 827: ('onmousemove view', 26, 14), 869: ('  onmouseout vi', 27, 12), 910: ('   onkeypress v', 28, 11), 950: ('     onkeydown', 29, 9), 987: ('        onke', 30, 6), 1023: ('        disab', 31, 6), 1096: ('           o', 33, 3), 1130: ('           ', 34, 1), 1165: ('            o', 35, 2), 1260: ('\n            ', 37, 29), 1336: ('y;\n          ', 39, 37), 293: ('view/value', 12, 25)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140097413192176 = __C2ZContextWrapper
_static_140097413192464 = __compile_zt_expr
_static_140097248373840 = {'class': '', 'id': '', 'accesskey': '', 'cols': '', 'name': '', 'rows': '', 'tabindex': '', 'required': "python:view.required and 'required' or None", 'style': 'view/style', 'title': 'view/title', 'lang': 'view/lang', 'onclick': 'view/onclick', 'ondblclick': 'view/ondblclick', 'onmousedown': 'view/onmousedown', 'onmouseup': 'view/onmouseup', 'onmouseover': 'view/onmouseover', 'onmousemove': 'view/onmousemove', 'onmouseout': 'view/onmouseout', 'onkeypress': 'view/onkeypress', 'onkeydown': 'view/onkeydown', 'onkeyup': 'view/onkeyup', 'disabled': 'view/disabled', 'onfocus': 'view/onfocus', 'onblur': 'view/onblur', 'onchange': 'view/onchange', 'readonly': 'view/readonly', 'onselect': 'view/onselect', }
_static_140097248371584 = {'xmlns': 'http://www.w3.org/1999/xhtml', }

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

            # <Static value=<ast.Dict object at 0x7f6aeeb92380> name=None at 7f6aeeb90b80> -> __attrs_140097248367408
            __attrs_140097248367408 = _static_140097248371584
            __append('\n  ')

            # <Static value=<ast.Dict object at 0x7f6aeeb92c50> name=None at 7f6aeeb91ae0> -> __attrs_140097252732752
            __attrs_140097252732752 = _static_140097248373840

            # <textarea ... (0:0)
            # --------------------------------------------------------
            __append('<textarea')

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097248365728
            __default_140097248365728 = _DEFAULT_MARKER

            # <Substitution 'string:form-control ${view/klass}' (17:17)> -> __attr_class
            __token = 475
            try:
                __zt_tmp = __attrs_140097252732752
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_140097413192464('string', 'form-control ${view/klass}', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((' class="%s"' % __attr_class))

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097248375424
            __default_140097248375424 = _DEFAULT_MARKER

            # <Substitution 'view/id' (14:17)> -> __attr_id
            __token = 351
            try:
                __zt_tmp = __attrs_140097252732752
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_140097413192464('path', 'view/id', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_id is not None):
                __append((' id="%s"' % __attr_id))

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097248369040
            __default_140097248369040 = _DEFAULT_MARKER

            # <Substitution 'view/accesskey' (38:37)> -> __attr_accesskey
            __token = 1298
            try:
                __zt_tmp = __attrs_140097252732752
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_accesskey = _static_140097413192464('path', 'view/accesskey', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_accesskey = __quote(__attr_accesskey, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_accesskey is not None):
                __append((' accesskey="%s"' % __attr_accesskey))

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097248377344
            __default_140097248377344 = _DEFAULT_MARKER

            # <Substitution 'view/cols' (35:35)> -> __attr_cols
            __token = 1198
            try:
                __zt_tmp = __attrs_140097252732752
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_cols = _static_140097413192464('path', 'view/cols', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_cols = __quote(__attr_cols, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_cols is not None):
                __append((' cols="%s"' % __attr_cols))

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097248365200
            __default_140097248365200 = _DEFAULT_MARKER

            # <Substitution 'view/name' (15:18)> -> __attr_name
            __token = 378
            try:
                __zt_tmp = __attrs_140097252732752
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_name = _static_140097413192464('path', 'view/name', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_name = __quote(__attr_name, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_name is not None):
                __append((' name="%s"' % __attr_name))

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097248366736
            __default_140097248366736 = _DEFAULT_MARKER

            # <Substitution 'view/rows' (36:26)> -> __attr_rows
            __token = 1227
            try:
                __zt_tmp = __attrs_140097252732752
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_rows = _static_140097413192464('path', 'view/rows', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_rows = __quote(__attr_rows, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_rows is not None):
                __append((' rows="%s"' % __attr_rows))

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097248375904
            __default_140097248375904 = _DEFAULT_MARKER

            # <Substitution 'view/tabindex' (32:5)> -> __attr_tabindex
            __token = 1060
            try:
                __zt_tmp = __attrs_140097252732752
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_tabindex = _static_140097413192464('path', 'view/tabindex', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_tabindex = __quote(__attr_tabindex, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_tabindex is not None):
                __append((' tabindex="%s"' % __attr_tabindex))

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097248363808
            __default_140097248363808 = _DEFAULT_MARKER

            # <Substitution "python:view.required and 'required' or None" (16:21)> -> __attr_required
            __token = 411
            try:
                __zt_tmp = __attrs_140097252732752
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_required = _static_140097413192464('python', "view.required and 'required' or None", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_required = __quote(__attr_required, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_required is not None):
                __append((' required="%s"' % __attr_required))

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097248370048
            __default_140097248370048 = _DEFAULT_MARKER

            # <Substitution 'view/style' (18:16)> -> __attr_style
            __token = 529
            try:
                __zt_tmp = __attrs_140097252732752
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_style = _static_140097413192464('path', 'view/style', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_style is not None):
                __append((' style="%s"' % __attr_style))

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097248362608
            __default_140097248362608 = _DEFAULT_MARKER

            # <Substitution 'view/title' (19:15)> -> __attr_title
            __token = 560
            try:
                __zt_tmp = __attrs_140097252732752
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_title = _static_140097413192464('path', 'view/title', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_title is not None):
                __append((' title="%s"' % __attr_title))

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097248369808
            __default_140097248369808 = _DEFAULT_MARKER

            # <Substitution 'view/lang' (20:13)> -> __attr_lang
            __token = 590
            try:
                __zt_tmp = __attrs_140097252732752
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_lang = _static_140097413192464('path', 'view/lang', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_lang = __quote(__attr_lang, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_lang is not None):
                __append((' lang="%s"' % __attr_lang))

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252730688
            __default_140097252730688 = _DEFAULT_MARKER

            # <Substitution 'view/onclick' (21:15)> -> __attr_onclick
            __token = 622
            try:
                __zt_tmp = __attrs_140097252732752
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onclick = _static_140097413192464('path', 'view/onclick', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_onclick = __quote(__attr_onclick, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onclick is not None):
                __append((' onclick="%s"' % __attr_onclick))

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252736256
            __default_140097252736256 = _DEFAULT_MARKER

            # <Substitution 'view/ondblclick' (22:17)> -> __attr_ondblclick
            __token = 660
            try:
                __zt_tmp = __attrs_140097252732752
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_ondblclick = _static_140097413192464('path', 'view/ondblclick', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_ondblclick = __quote(__attr_ondblclick, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_ondblclick is not None):
                __append((' ondblclick="%s"' % __attr_ondblclick))

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252732848
            __default_140097252732848 = _DEFAULT_MARKER

            # <Substitution 'view/onmousedown' (23:17)> -> __attr_onmousedown
            __token = 702
            try:
                __zt_tmp = __attrs_140097252732752
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmousedown = _static_140097413192464('path', 'view/onmousedown', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_onmousedown = __quote(__attr_onmousedown, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmousedown is not None):
                __append((' onmousedown="%s"' % __attr_onmousedown))

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252722432
            __default_140097252722432 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseup' (24:14)> -> __attr_onmouseup
            __token = 743
            try:
                __zt_tmp = __attrs_140097252732752
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseup = _static_140097413192464('path', 'view/onmouseup', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_onmouseup = __quote(__attr_onmouseup, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseup is not None):
                __append((' onmouseup="%s"' % __attr_onmouseup))

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252725744
            __default_140097252725744 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseover' (25:15)> -> __attr_onmouseover
            __token = 784
            try:
                __zt_tmp = __attrs_140097252732752
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseover = _static_140097413192464('path', 'view/onmouseover', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_onmouseover = __quote(__attr_onmouseover, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseover is not None):
                __append((' onmouseover="%s"' % __attr_onmouseover))

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252731408
            __default_140097252731408 = _DEFAULT_MARKER

            # <Substitution 'view/onmousemove' (26:14)> -> __attr_onmousemove
            __token = 827
            try:
                __zt_tmp = __attrs_140097252732752
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmousemove = _static_140097413192464('path', 'view/onmousemove', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_onmousemove = __quote(__attr_onmousemove, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmousemove is not None):
                __append((' onmousemove="%s"' % __attr_onmousemove))

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252721904
            __default_140097252721904 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseout' (27:12)> -> __attr_onmouseout
            __token = 869
            try:
                __zt_tmp = __attrs_140097252732752
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseout = _static_140097413192464('path', 'view/onmouseout', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_onmouseout = __quote(__attr_onmouseout, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseout is not None):
                __append((' onmouseout="%s"' % __attr_onmouseout))

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252731312
            __default_140097252731312 = _DEFAULT_MARKER

            # <Substitution 'view/onkeypress' (28:11)> -> __attr_onkeypress
            __token = 910
            try:
                __zt_tmp = __attrs_140097252732752
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeypress = _static_140097413192464('path', 'view/onkeypress', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_onkeypress = __quote(__attr_onkeypress, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeypress is not None):
                __append((' onkeypress="%s"' % __attr_onkeypress))

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252727952
            __default_140097252727952 = _DEFAULT_MARKER

            # <Substitution 'view/onkeydown' (29:9)> -> __attr_onkeydown
            __token = 950
            try:
                __zt_tmp = __attrs_140097252732752
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeydown = _static_140097413192464('path', 'view/onkeydown', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_onkeydown = __quote(__attr_onkeydown, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeydown is not None):
                __append((' onkeydown="%s"' % __attr_onkeydown))

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252734768
            __default_140097252734768 = _DEFAULT_MARKER

            # <Substitution 'view/onkeyup' (30:6)> -> __attr_onkeyup
            __token = 987
            try:
                __zt_tmp = __attrs_140097252732752
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeyup = _static_140097413192464('path', 'view/onkeyup', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_onkeyup = __quote(__attr_onkeyup, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeyup is not None):
                __append((' onkeyup="%s"' % __attr_onkeyup))

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252722720
            __default_140097252722720 = _DEFAULT_MARKER

            # <Boolean 'view/disabled' (31:6)> -> __attr_disabled
            __token = 1023
            try:
                __zt_tmp = __attrs_140097252732752
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

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252722912
            __default_140097252722912 = _DEFAULT_MARKER

            # <Substitution 'view/onfocus' (33:3)> -> __attr_onfocus
            __token = 1096
            try:
                __zt_tmp = __attrs_140097252732752
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onfocus = _static_140097413192464('path', 'view/onfocus', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_onfocus = __quote(__attr_onfocus, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onfocus is not None):
                __append((' onfocus="%s"' % __attr_onfocus))

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252725264
            __default_140097252725264 = _DEFAULT_MARKER

            # <Substitution 'view/onblur' (34:1)> -> __attr_onblur
            __token = 1130
            try:
                __zt_tmp = __attrs_140097252732752
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onblur = _static_140097413192464('path', 'view/onblur', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_onblur = __quote(__attr_onblur, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onblur is not None):
                __append((' onblur="%s"' % __attr_onblur))

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252731120
            __default_140097252731120 = _DEFAULT_MARKER

            # <Substitution 'view/onchange' (35:2)> -> __attr_onchange
            __token = 1165
            try:
                __zt_tmp = __attrs_140097252732752
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onchange = _static_140097413192464('path', 'view/onchange', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_onchange = __quote(__attr_onchange, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onchange is not None):
                __append((' onchange="%s"' % __attr_onchange))

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252729008
            __default_140097252729008 = _DEFAULT_MARKER

            # <Boolean 'view/readonly' (37:29)> -> __attr_readonly
            __token = 1260
            try:
                __zt_tmp = __attrs_140097252732752
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

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252731744
            __default_140097252731744 = _DEFAULT_MARKER

            # <Substitution 'view/onselect' (39:37)> -> __attr_onselect
            __token = 1336
            try:
                __zt_tmp = __attrs_140097252732752
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onselect = _static_140097413192464('path', 'view/onselect', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_onselect = __quote(__attr_onselect, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onselect is not None):
                __append((' onselect="%s"' % __attr_onselect))
            __append(' >')

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097248374320
            __default_140097248374320 = _DEFAULT_MARKER

            # <Value 'view/value' (12:25)> -> __cache_140097248370288
            __token = 293
            try:
                __zt_tmp = __attrs_140097252732752
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140097248370288 = _static_140097413192464('path', 'view/value', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

            # <BinOp left=<Value 'view/value' (12:25)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeeb92260> -> __condition
            __expression = __cache_140097248370288

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140097248370288
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append('</textarea>\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }