# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/plone/app/z3cform/templates/textlines_input.pt'

__tokens = {418: ('s string:form-control ${view/klas', 16, 18), 361: ('view/id', 14, 17), 1241: ('              ', 38, 0), 1141: (';\n       ', 34, 36), 388: (' view/nam', 15, 18), 1170: ('s;\n      ', 35, 27), 1003: ('        tabin', 31, 6), 472: ('le view/st', 17, 17), 503: ('tle view/t', 18, 16), 533: ('lang view', 19, 14), 565: ('click view/o', 20, 16), 603: ('lclick view/ond', 21, 18), 645: ('usedown view/onm', 22, 18), 686: ('nmouseup view/', 23, 15), 727: ('mouseover view/o', 24, 16), 770: ('nmousemove view/', 25, 15), 812: (' onmouseout vie', 26, 13), 853: ('  onkeypress vi', 27, 12), 893: ('    onkeydown ', 28, 10), 930: ('       onkey', 29, 7), 966: ('       disabl', 30, 7), 1039: ('          on', 32, 4), 1073: ('           ', 33, 2), 1108: ('           on', 34, 3), 1203: ('             ', 37, 0), 1279: (';\n           ', 38, 38), 303: ('view/value', 12, 35)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140453526790416 = __C2ZContextWrapper
_static_140453526790704 = __compile_zt_expr
_static_140453434588128 = {'class': '', 'id': '', 'accesskey': '', 'cols': '', 'name': '', 'rows': '', 'tabindex': '', 'style': 'view/style', 'title': 'view/title', 'lang': 'view/lang', 'onclick': 'view/onclick', 'ondblclick': 'view/ondblclick', 'onmousedown': 'view/onmousedown', 'onmouseup': 'view/onmouseup', 'onmouseover': 'view/onmouseover', 'onmousemove': 'view/onmousemove', 'onmouseout': 'view/onmouseout', 'onkeypress': 'view/onkeypress', 'onkeydown': 'view/onkeydown', 'onkeyup': 'view/onkeyup', 'disabled': 'view/disabled', 'onfocus': 'view/onfocus', 'onblur': 'view/onblur', 'onchange': 'view/onchange', 'readonly': 'view/readonly', 'onselect': 'view/onselect', }
_static_140453436013392 = {'xmlns': 'http://www.w3.org/1999/xhtml', }

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

            # <Static value=<ast.Dict object at 0x7fbddd293b50> name=None at 7fbddd290dc0> -> __attrs_140453436013296
            __attrs_140453436013296 = _static_140453436013392
            __append('\n  ')

            # <Static value=<ast.Dict object at 0x7fbddd137be0> name=None at 7fbddd137b20> -> __attrs_140453434581984
            __attrs_140453434581984 = _static_140453434588128

            # <textarea ... (0:0)
            # --------------------------------------------------------
            __append('<textarea')

            # <Symbol value=<DEFAULT> at 7fbde28a8340> -> __default_140453434580784
            __default_140453434580784 = _DEFAULT_MARKER

            # <Substitution 'string:form-control ${view/klass}' (16:18)> -> __attr_class
            __token = 418
            try:
                __zt_tmp = __attrs_140453434581984
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_140453526790704('string', 'form-control ${view/klass}', econtext=econtext)(_static_140453526790416(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((' class="%s"' % __attr_class))

            # <Symbol value=<DEFAULT> at 7fbde28a8340> -> __default_140453434578144
            __default_140453434578144 = _DEFAULT_MARKER

            # <Substitution 'view/id' (14:17)> -> __attr_id
            __token = 361
            try:
                __zt_tmp = __attrs_140453434581984
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_140453526790704('path', 'view/id', econtext=econtext)(_static_140453526790416(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_id is not None):
                __append((' id="%s"' % __attr_id))

            # <Symbol value=<DEFAULT> at 7fbde28a8340> -> __default_140453434587408
            __default_140453434587408 = _DEFAULT_MARKER

            # <Substitution 'view/accesskey' (38:0)> -> __attr_accesskey
            __token = 1241
            try:
                __zt_tmp = __attrs_140453434581984
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_accesskey = _static_140453526790704('path', 'view/accesskey', econtext=econtext)(_static_140453526790416(econtext, __zt_tmp))
            __attr_accesskey = __quote(__attr_accesskey, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_accesskey is not None):
                __append((' accesskey="%s"' % __attr_accesskey))

            # <Symbol value=<DEFAULT> at 7fbde28a8340> -> __default_140453434587168
            __default_140453434587168 = _DEFAULT_MARKER

            # <Substitution 'view/cols' (34:36)> -> __attr_cols
            __token = 1141
            try:
                __zt_tmp = __attrs_140453434581984
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_cols = _static_140453526790704('path', 'view/cols', econtext=econtext)(_static_140453526790416(econtext, __zt_tmp))
            __attr_cols = __quote(__attr_cols, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_cols is not None):
                __append((' cols="%s"' % __attr_cols))

            # <Symbol value=<DEFAULT> at 7fbde28a8340> -> __default_140453434585248
            __default_140453434585248 = _DEFAULT_MARKER

            # <Substitution 'view/name' (15:18)> -> __attr_name
            __token = 388
            try:
                __zt_tmp = __attrs_140453434581984
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_name = _static_140453526790704('path', 'view/name', econtext=econtext)(_static_140453526790416(econtext, __zt_tmp))
            __attr_name = __quote(__attr_name, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_name is not None):
                __append((' name="%s"' % __attr_name))

            # <Symbol value=<DEFAULT> at 7fbde28a8340> -> __default_140453434579200
            __default_140453434579200 = _DEFAULT_MARKER

            # <Substitution 'view/rows' (35:27)> -> __attr_rows
            __token = 1170
            try:
                __zt_tmp = __attrs_140453434581984
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_rows = _static_140453526790704('path', 'view/rows', econtext=econtext)(_static_140453526790416(econtext, __zt_tmp))
            __attr_rows = __quote(__attr_rows, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_rows is not None):
                __append((' rows="%s"' % __attr_rows))

            # <Symbol value=<DEFAULT> at 7fbde28a8340> -> __default_140453434587456
            __default_140453434587456 = _DEFAULT_MARKER

            # <Substitution 'view/tabindex' (31:6)> -> __attr_tabindex
            __token = 1003
            try:
                __zt_tmp = __attrs_140453434581984
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_tabindex = _static_140453526790704('path', 'view/tabindex', econtext=econtext)(_static_140453526790416(econtext, __zt_tmp))
            __attr_tabindex = __quote(__attr_tabindex, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_tabindex is not None):
                __append((' tabindex="%s"' % __attr_tabindex))

            # <Symbol value=<DEFAULT> at 7fbde28a8340> -> __default_140453434586688
            __default_140453434586688 = _DEFAULT_MARKER

            # <Substitution 'view/style' (17:17)> -> __attr_style
            __token = 472
            try:
                __zt_tmp = __attrs_140453434581984
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_style = _static_140453526790704('path', 'view/style', econtext=econtext)(_static_140453526790416(econtext, __zt_tmp))
            __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_style is not None):
                __append((' style="%s"' % __attr_style))

            # <Symbol value=<DEFAULT> at 7fbde28a8340> -> __default_140453434586736
            __default_140453434586736 = _DEFAULT_MARKER

            # <Substitution 'view/title' (18:16)> -> __attr_title
            __token = 503
            try:
                __zt_tmp = __attrs_140453434581984
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_title = _static_140453526790704('path', 'view/title', econtext=econtext)(_static_140453526790416(econtext, __zt_tmp))
            __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_title is not None):
                __append((' title="%s"' % __attr_title))

            # <Symbol value=<DEFAULT> at 7fbde28a8340> -> __default_140453434585680
            __default_140453434585680 = _DEFAULT_MARKER

            # <Substitution 'view/lang' (19:14)> -> __attr_lang
            __token = 533
            try:
                __zt_tmp = __attrs_140453434581984
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_lang = _static_140453526790704('path', 'view/lang', econtext=econtext)(_static_140453526790416(econtext, __zt_tmp))
            __attr_lang = __quote(__attr_lang, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_lang is not None):
                __append((' lang="%s"' % __attr_lang))

            # <Symbol value=<DEFAULT> at 7fbde28a8340> -> __default_140453434573392
            __default_140453434573392 = _DEFAULT_MARKER

            # <Substitution 'view/onclick' (20:16)> -> __attr_onclick
            __token = 565
            try:
                __zt_tmp = __attrs_140453434581984
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onclick = _static_140453526790704('path', 'view/onclick', econtext=econtext)(_static_140453526790416(econtext, __zt_tmp))
            __attr_onclick = __quote(__attr_onclick, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onclick is not None):
                __append((' onclick="%s"' % __attr_onclick))

            # <Symbol value=<DEFAULT> at 7fbde28a8340> -> __default_140453434577664
            __default_140453434577664 = _DEFAULT_MARKER

            # <Substitution 'view/ondblclick' (21:18)> -> __attr_ondblclick
            __token = 603
            try:
                __zt_tmp = __attrs_140453434581984
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_ondblclick = _static_140453526790704('path', 'view/ondblclick', econtext=econtext)(_static_140453526790416(econtext, __zt_tmp))
            __attr_ondblclick = __quote(__attr_ondblclick, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_ondblclick is not None):
                __append((' ondblclick="%s"' % __attr_ondblclick))

            # <Symbol value=<DEFAULT> at 7fbde28a8340> -> __default_140453434578096
            __default_140453434578096 = _DEFAULT_MARKER

            # <Substitution 'view/onmousedown' (22:18)> -> __attr_onmousedown
            __token = 645
            try:
                __zt_tmp = __attrs_140453434581984
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmousedown = _static_140453526790704('path', 'view/onmousedown', econtext=econtext)(_static_140453526790416(econtext, __zt_tmp))
            __attr_onmousedown = __quote(__attr_onmousedown, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmousedown is not None):
                __append((' onmousedown="%s"' % __attr_onmousedown))

            # <Symbol value=<DEFAULT> at 7fbde28a8340> -> __default_140453434575600
            __default_140453434575600 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseup' (23:15)> -> __attr_onmouseup
            __token = 686
            try:
                __zt_tmp = __attrs_140453434581984
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseup = _static_140453526790704('path', 'view/onmouseup', econtext=econtext)(_static_140453526790416(econtext, __zt_tmp))
            __attr_onmouseup = __quote(__attr_onmouseup, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseup is not None):
                __append((' onmouseup="%s"' % __attr_onmouseup))

            # <Symbol value=<DEFAULT> at 7fbde28a8340> -> __default_140453434581216
            __default_140453434581216 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseover' (24:16)> -> __attr_onmouseover
            __token = 727
            try:
                __zt_tmp = __attrs_140453434581984
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseover = _static_140453526790704('path', 'view/onmouseover', econtext=econtext)(_static_140453526790416(econtext, __zt_tmp))
            __attr_onmouseover = __quote(__attr_onmouseover, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseover is not None):
                __append((' onmouseover="%s"' % __attr_onmouseover))

            # <Symbol value=<DEFAULT> at 7fbde28a8340> -> __default_140453434581024
            __default_140453434581024 = _DEFAULT_MARKER

            # <Substitution 'view/onmousemove' (25:15)> -> __attr_onmousemove
            __token = 770
            try:
                __zt_tmp = __attrs_140453434581984
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmousemove = _static_140453526790704('path', 'view/onmousemove', econtext=econtext)(_static_140453526790416(econtext, __zt_tmp))
            __attr_onmousemove = __quote(__attr_onmousemove, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmousemove is not None):
                __append((' onmousemove="%s"' % __attr_onmousemove))

            # <Symbol value=<DEFAULT> at 7fbde28a8340> -> __default_140453434582272
            __default_140453434582272 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseout' (26:13)> -> __attr_onmouseout
            __token = 812
            try:
                __zt_tmp = __attrs_140453434581984
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseout = _static_140453526790704('path', 'view/onmouseout', econtext=econtext)(_static_140453526790416(econtext, __zt_tmp))
            __attr_onmouseout = __quote(__attr_onmouseout, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseout is not None):
                __append((' onmouseout="%s"' % __attr_onmouseout))

            # <Symbol value=<DEFAULT> at 7fbde28a8340> -> __default_140453434581120
            __default_140453434581120 = _DEFAULT_MARKER

            # <Substitution 'view/onkeypress' (27:12)> -> __attr_onkeypress
            __token = 853
            try:
                __zt_tmp = __attrs_140453434581984
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeypress = _static_140453526790704('path', 'view/onkeypress', econtext=econtext)(_static_140453526790416(econtext, __zt_tmp))
            __attr_onkeypress = __quote(__attr_onkeypress, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeypress is not None):
                __append((' onkeypress="%s"' % __attr_onkeypress))

            # <Symbol value=<DEFAULT> at 7fbde28a8340> -> __default_140453434583856
            __default_140453434583856 = _DEFAULT_MARKER

            # <Substitution 'view/onkeydown' (28:10)> -> __attr_onkeydown
            __token = 893
            try:
                __zt_tmp = __attrs_140453434581984
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeydown = _static_140453526790704('path', 'view/onkeydown', econtext=econtext)(_static_140453526790416(econtext, __zt_tmp))
            __attr_onkeydown = __quote(__attr_onkeydown, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeydown is not None):
                __append((' onkeydown="%s"' % __attr_onkeydown))

            # <Symbol value=<DEFAULT> at 7fbde28a8340> -> __default_140453434588464
            __default_140453434588464 = _DEFAULT_MARKER

            # <Substitution 'view/onkeyup' (29:7)> -> __attr_onkeyup
            __token = 930
            try:
                __zt_tmp = __attrs_140453434581984
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeyup = _static_140453526790704('path', 'view/onkeyup', econtext=econtext)(_static_140453526790416(econtext, __zt_tmp))
            __attr_onkeyup = __quote(__attr_onkeyup, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeyup is not None):
                __append((' onkeyup="%s"' % __attr_onkeyup))

            # <Symbol value=<DEFAULT> at 7fbde28a8340> -> __default_140453434584528
            __default_140453434584528 = _DEFAULT_MARKER

            # <Boolean 'view/disabled' (30:7)> -> __attr_disabled
            __token = 966
            try:
                __zt_tmp = __attrs_140453434581984
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_disabled = _static_140453526790704('path', 'view/disabled', econtext=econtext)(_static_140453526790416(econtext, __zt_tmp))
            if (__attr_disabled is _DEFAULT_MARKER):
                __attr_disabled = None
            else:
                if __attr_disabled:
                    __attr_disabled = 'disabled'
                else:
                    __attr_disabled = None
            if (__attr_disabled is not None):
                __append((' disabled="%s"' % __attr_disabled))

            # <Symbol value=<DEFAULT> at 7fbde28a8340> -> __default_140453434581456
            __default_140453434581456 = _DEFAULT_MARKER

            # <Substitution 'view/onfocus' (32:4)> -> __attr_onfocus
            __token = 1039
            try:
                __zt_tmp = __attrs_140453434581984
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onfocus = _static_140453526790704('path', 'view/onfocus', econtext=econtext)(_static_140453526790416(econtext, __zt_tmp))
            __attr_onfocus = __quote(__attr_onfocus, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onfocus is not None):
                __append((' onfocus="%s"' % __attr_onfocus))

            # <Symbol value=<DEFAULT> at 7fbde28a8340> -> __default_140453434582752
            __default_140453434582752 = _DEFAULT_MARKER

            # <Substitution 'view/onblur' (33:2)> -> __attr_onblur
            __token = 1073
            try:
                __zt_tmp = __attrs_140453434581984
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onblur = _static_140453526790704('path', 'view/onblur', econtext=econtext)(_static_140453526790416(econtext, __zt_tmp))
            __attr_onblur = __quote(__attr_onblur, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onblur is not None):
                __append((' onblur="%s"' % __attr_onblur))

            # <Symbol value=<DEFAULT> at 7fbde28a8340> -> __default_140453434586448
            __default_140453434586448 = _DEFAULT_MARKER

            # <Substitution 'view/onchange' (34:3)> -> __attr_onchange
            __token = 1108
            try:
                __zt_tmp = __attrs_140453434581984
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onchange = _static_140453526790704('path', 'view/onchange', econtext=econtext)(_static_140453526790416(econtext, __zt_tmp))
            __attr_onchange = __quote(__attr_onchange, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onchange is not None):
                __append((' onchange="%s"' % __attr_onchange))

            # <Symbol value=<DEFAULT> at 7fbde28a8340> -> __default_140453434585968
            __default_140453434585968 = _DEFAULT_MARKER

            # <Boolean 'view/readonly' (37:0)> -> __attr_readonly
            __token = 1203
            try:
                __zt_tmp = __attrs_140453434581984
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_readonly = _static_140453526790704('path', 'view/readonly', econtext=econtext)(_static_140453526790416(econtext, __zt_tmp))
            if (__attr_readonly is _DEFAULT_MARKER):
                __attr_readonly = None
            else:
                if __attr_readonly:
                    __attr_readonly = 'readonly'
                else:
                    __attr_readonly = None
            if (__attr_readonly is not None):
                __append((' readonly="%s"' % __attr_readonly))

            # <Symbol value=<DEFAULT> at 7fbde28a8340> -> __default_140453434583712
            __default_140453434583712 = _DEFAULT_MARKER

            # <Substitution 'view/onselect' (38:38)> -> __attr_onselect
            __token = 1279
            try:
                __zt_tmp = __attrs_140453434581984
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onselect = _static_140453526790704('path', 'view/onselect', econtext=econtext)(_static_140453526790416(econtext, __zt_tmp))
            __attr_onselect = __quote(__attr_onselect, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onselect is not None):
                __append((' onselect="%s"' % __attr_onselect))
            __append(' >')

            # <Symbol value=<DEFAULT> at 7fbde28a8340> -> __default_140453434581888
            __default_140453434581888 = _DEFAULT_MARKER

            # <Value 'view/value' (12:35)> -> __cache_140453434578672
            __token = 303
            try:
                __zt_tmp = __attrs_140453434581984
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140453434578672 = _static_140453526790704('path', 'view/value', econtext=econtext)(_static_140453526790416(econtext, __zt_tmp))

            # <BinOp left=<Value 'view/value' (12:35)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fbde28a8340> at 7fbddd135960> -> __condition
            __expression = __cache_140453434578672

            # <Symbol value=<DEFAULT> at 7fbde28a8340> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140453434578672
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('</textarea>\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }