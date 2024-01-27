# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/plone/app/z3cform/templates/submit_input.pt'

__tokens = {190: ("python:'btn-secondary ' if not 'btn-' in view.klass else ''", 7, 23), 340: ('view/id', 11, 15), 365: (' view/nam', 12, 16), 393: ('s string:btn ${bsFallback}${view/klas', 13, 16), 449: ('ue view/va', 14, 15), 478: ('yle view/s', 15, 14), 506: ('lang view', 16, 12), 536: ('click view/o', 17, 14), 572: ('lclick view/ond', 18, 16), 612: ('usedown view/onm', 19, 16), 651: ('nmouseup view/', 20, 13), 690: ('mouseover view/o', 21, 14), 731: ('nmousemove view/', 22, 13), 771: (' onmouseout vie', 23, 11), 810: ('  onkeypress vi', 24, 10), 848: ('    onkeydown ', 25, 8), 883: ('       onkey', 26, 5), 917: ('       disabl', 27, 5), 952: ('        tabin', 28, 4), 986: ('          on', 29, 2), 1018: ('           ', 30, 0), 1051: ('           on', 31, 1), 1086: ('            r', 32, 0), 1116: ('only;\n  ', 32, 30), 1147: ('\n            a', 33, 25), 1183: ('y;\n          ', 34, 35), 1224: ('          formnovalidate python:view.ignoreReq', 36, 2), 286: ('view/value', 9, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140097413192176 = __C2ZContextWrapper
_static_140097413192464 = __compile_zt_expr
_static_140097337743520 = {'type': 'submit', 'id': 'view/id', 'name': 'view/name', 'class': 'string:btn ${bsFallback}${view/klass}', 'value': 'view/value', 'style': 'view/style', 'lang': 'view/lang', 'onclick': 'view/onclick', 'ondblclick': 'view/ondblclick', 'onmousedown': 'view/onmousedown', 'onmouseup': 'view/onmouseup', 'onmouseover': 'view/onmouseover', 'onmousemove': 'view/onmousemove', 'onmouseout': 'view/onmouseout', 'onkeypress': 'view/onkeypress', 'onkeydown': 'view/onkeydown', 'onkeyup': 'view/onkeyup', 'disabled': 'view/disabled', 'tabindex': 'view/tabindex', 'onfocus': 'view/onfocus', 'onblur': 'view/onblur', 'onchange': 'view/onchange', 'readonly': 'view/readonly', 'alt': 'view/alt', 'accesskey': 'view/accesskey', 'onselect': 'view/onselect', 'formnovalidate': 'python:view.ignoreRequiredOnValidation or None', }
_static_140097338359920 = {'xmlns': 'http://www.w3.org/1999/xhtml', }

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

            # <Static value=<ast.Dict object at 0x7f6af4164070> name=None at 7f6af41656c0> -> __attrs_140097339072688
            __attrs_140097339072688 = _static_140097338359920
            __append('\n  ')

            # <Static value=<ast.Dict object at 0x7f6af40cd8a0> name=None at 7f6af40cfbb0> -> __attrs_140097252054240
            __attrs_140097252054240 = _static_140097337743520
            __backup_bsFallback_140097247576992 = get('bsFallback', __marker)

            # <Value "python:'btn-secondary ' if not 'btn-' in view.klass else ''" (7:23)> -> __value
            __token = 190
            try:
                __zt_tmp = __attrs_140097252054240
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('python', "'btn-secondary ' if not 'btn-' in view.klass else ''", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['bsFallback'] = __value

            # <button ... (0:0)
            # --------------------------------------------------------
            __append('<button type="submit"')

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097337745056
            __default_140097337745056 = _DEFAULT_MARKER

            # <Substitution 'view/id' (11:15)> -> __attr_id
            __token = 340
            try:
                __zt_tmp = __attrs_140097252054240
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_140097413192464('path', 'view/id', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_id is not None):
                __append((' id="%s"' % __attr_id))

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097337741312
            __default_140097337741312 = _DEFAULT_MARKER

            # <Substitution 'view/name' (12:16)> -> __attr_name
            __token = 365
            try:
                __zt_tmp = __attrs_140097252054240
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_name = _static_140097413192464('path', 'view/name', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_name is not None):
                __append((' name="%s"' % __attr_name))

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097337752064
            __default_140097337752064 = _DEFAULT_MARKER

            # <Substitution 'string:btn ${bsFallback}${view/klass}' (13:16)> -> __attr_class
            __token = 393
            try:
                __zt_tmp = __attrs_140097252054240
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_140097413192464('string', 'btn ${bsFallback}${view/klass}', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((' class="%s"' % __attr_class))

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097337743952
            __default_140097337743952 = _DEFAULT_MARKER

            # <Substitution 'view/value' (14:15)> -> __attr_value
            __token = 449
            try:
                __zt_tmp = __attrs_140097252054240
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_value = _static_140097413192464('path', 'view/value', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_value is not None):
                __append((' value="%s"' % __attr_value))

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097337742560
            __default_140097337742560 = _DEFAULT_MARKER

            # <Substitution 'view/style' (15:14)> -> __attr_style
            __token = 478
            try:
                __zt_tmp = __attrs_140097252054240
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_style = _static_140097413192464('path', 'view/style', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_style is not None):
                __append((' style="%s"' % __attr_style))

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097337744048
            __default_140097337744048 = _DEFAULT_MARKER

            # <Substitution 'view/lang' (16:12)> -> __attr_lang
            __token = 506
            try:
                __zt_tmp = __attrs_140097252054240
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_lang = _static_140097413192464('path', 'view/lang', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_lang = __quote(__attr_lang, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_lang is not None):
                __append((' lang="%s"' % __attr_lang))

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097337750480
            __default_140097337750480 = _DEFAULT_MARKER

            # <Substitution 'view/onclick' (17:14)> -> __attr_onclick
            __token = 536
            try:
                __zt_tmp = __attrs_140097252054240
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onclick = _static_140097413192464('path', 'view/onclick', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_onclick = __quote(__attr_onclick, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onclick is not None):
                __append((' onclick="%s"' % __attr_onclick))

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097337741216
            __default_140097337741216 = _DEFAULT_MARKER

            # <Substitution 'view/ondblclick' (18:16)> -> __attr_ondblclick
            __token = 572
            try:
                __zt_tmp = __attrs_140097252054240
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_ondblclick = _static_140097413192464('path', 'view/ondblclick', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_ondblclick = __quote(__attr_ondblclick, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_ondblclick is not None):
                __append((' ondblclick="%s"' % __attr_ondblclick))

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097337742272
            __default_140097337742272 = _DEFAULT_MARKER

            # <Substitution 'view/onmousedown' (19:16)> -> __attr_onmousedown
            __token = 612
            try:
                __zt_tmp = __attrs_140097252054240
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmousedown = _static_140097413192464('path', 'view/onmousedown', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_onmousedown = __quote(__attr_onmousedown, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmousedown is not None):
                __append((' onmousedown="%s"' % __attr_onmousedown))

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252050544
            __default_140097252050544 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseup' (20:13)> -> __attr_onmouseup
            __token = 651
            try:
                __zt_tmp = __attrs_140097252054240
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseup = _static_140097413192464('path', 'view/onmouseup', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_onmouseup = __quote(__attr_onmouseup, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseup is not None):
                __append((' onmouseup="%s"' % __attr_onmouseup))

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252051456
            __default_140097252051456 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseover' (21:14)> -> __attr_onmouseover
            __token = 690
            try:
                __zt_tmp = __attrs_140097252054240
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseover = _static_140097413192464('path', 'view/onmouseover', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_onmouseover = __quote(__attr_onmouseover, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseover is not None):
                __append((' onmouseover="%s"' % __attr_onmouseover))

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252051120
            __default_140097252051120 = _DEFAULT_MARKER

            # <Substitution 'view/onmousemove' (22:13)> -> __attr_onmousemove
            __token = 731
            try:
                __zt_tmp = __attrs_140097252054240
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmousemove = _static_140097413192464('path', 'view/onmousemove', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_onmousemove = __quote(__attr_onmousemove, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmousemove is not None):
                __append((' onmousemove="%s"' % __attr_onmousemove))

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252051648
            __default_140097252051648 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseout' (23:11)> -> __attr_onmouseout
            __token = 771
            try:
                __zt_tmp = __attrs_140097252054240
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseout = _static_140097413192464('path', 'view/onmouseout', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_onmouseout = __quote(__attr_onmouseout, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseout is not None):
                __append((' onmouseout="%s"' % __attr_onmouseout))

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252056976
            __default_140097252056976 = _DEFAULT_MARKER

            # <Substitution 'view/onkeypress' (24:10)> -> __attr_onkeypress
            __token = 810
            try:
                __zt_tmp = __attrs_140097252054240
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeypress = _static_140097413192464('path', 'view/onkeypress', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_onkeypress = __quote(__attr_onkeypress, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeypress is not None):
                __append((' onkeypress="%s"' % __attr_onkeypress))

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252059904
            __default_140097252059904 = _DEFAULT_MARKER

            # <Substitution 'view/onkeydown' (25:8)> -> __attr_onkeydown
            __token = 848
            try:
                __zt_tmp = __attrs_140097252054240
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeydown = _static_140097413192464('path', 'view/onkeydown', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_onkeydown = __quote(__attr_onkeydown, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeydown is not None):
                __append((' onkeydown="%s"' % __attr_onkeydown))

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252056400
            __default_140097252056400 = _DEFAULT_MARKER

            # <Substitution 'view/onkeyup' (26:5)> -> __attr_onkeyup
            __token = 883
            try:
                __zt_tmp = __attrs_140097252054240
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeyup = _static_140097413192464('path', 'view/onkeyup', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_onkeyup = __quote(__attr_onkeyup, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeyup is not None):
                __append((' onkeyup="%s"' % __attr_onkeyup))

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252059760
            __default_140097252059760 = _DEFAULT_MARKER

            # <Boolean 'view/disabled' (27:5)> -> __attr_disabled
            __token = 917
            try:
                __zt_tmp = __attrs_140097252054240
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

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252059520
            __default_140097252059520 = _DEFAULT_MARKER

            # <Substitution 'view/tabindex' (28:4)> -> __attr_tabindex
            __token = 952
            try:
                __zt_tmp = __attrs_140097252054240
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_tabindex = _static_140097413192464('path', 'view/tabindex', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_tabindex = __quote(__attr_tabindex, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_tabindex is not None):
                __append((' tabindex="%s"' % __attr_tabindex))

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252051600
            __default_140097252051600 = _DEFAULT_MARKER

            # <Substitution 'view/onfocus' (29:2)> -> __attr_onfocus
            __token = 986
            try:
                __zt_tmp = __attrs_140097252054240
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onfocus = _static_140097413192464('path', 'view/onfocus', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_onfocus = __quote(__attr_onfocus, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onfocus is not None):
                __append((' onfocus="%s"' % __attr_onfocus))

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252055008
            __default_140097252055008 = _DEFAULT_MARKER

            # <Substitution 'view/onblur' (30:0)> -> __attr_onblur
            __token = 1018
            try:
                __zt_tmp = __attrs_140097252054240
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onblur = _static_140097413192464('path', 'view/onblur', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_onblur = __quote(__attr_onblur, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onblur is not None):
                __append((' onblur="%s"' % __attr_onblur))

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252049872
            __default_140097252049872 = _DEFAULT_MARKER

            # <Substitution 'view/onchange' (31:1)> -> __attr_onchange
            __token = 1051
            try:
                __zt_tmp = __attrs_140097252054240
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onchange = _static_140097413192464('path', 'view/onchange', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_onchange = __quote(__attr_onchange, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onchange is not None):
                __append((' onchange="%s"' % __attr_onchange))

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252050448
            __default_140097252050448 = _DEFAULT_MARKER

            # <Boolean 'view/readonly' (32:0)> -> __attr_readonly
            __token = 1086
            try:
                __zt_tmp = __attrs_140097252054240
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

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252062256
            __default_140097252062256 = _DEFAULT_MARKER

            # <Substitution 'view/alt' (32:30)> -> __attr_alt
            __token = 1116
            try:
                __zt_tmp = __attrs_140097252054240
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_alt = _static_140097413192464('path', 'view/alt', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_alt = __quote(__attr_alt, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_alt is not None):
                __append((' alt="%s"' % __attr_alt))

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252057600
            __default_140097252057600 = _DEFAULT_MARKER

            # <Substitution 'view/accesskey' (33:25)> -> __attr_accesskey
            __token = 1147
            try:
                __zt_tmp = __attrs_140097252054240
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_accesskey = _static_140097413192464('path', 'view/accesskey', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_accesskey = __quote(__attr_accesskey, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_accesskey is not None):
                __append((' accesskey="%s"' % __attr_accesskey))

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252053520
            __default_140097252053520 = _DEFAULT_MARKER

            # <Substitution 'view/onselect' (34:35)> -> __attr_onselect
            __token = 1183
            try:
                __zt_tmp = __attrs_140097252054240
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onselect = _static_140097413192464('path', 'view/onselect', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_onselect = __quote(__attr_onselect, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onselect is not None):
                __append((' onselect="%s"' % __attr_onselect))

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252051888
            __default_140097252051888 = _DEFAULT_MARKER

            # <Substitution 'python:view.ignoreRequiredOnValidation or None' (36:2)> -> __attr_formnovalidate
            __token = 1224
            try:
                __zt_tmp = __attrs_140097252054240
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_formnovalidate = _static_140097413192464('python', 'view.ignoreRequiredOnValidation or None', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_formnovalidate = __quote(__attr_formnovalidate, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_formnovalidate is not None):
                __append((' formnovalidate="%s"' % __attr_formnovalidate))
            __append(' >')

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097337751776
            __default_140097337751776 = _DEFAULT_MARKER

            # <Value 'view/value' (9:23)> -> __cache_140097337751488
            __token = 286
            try:
                __zt_tmp = __attrs_140097252054240
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140097337751488 = _static_140097413192464('path', 'view/value', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

            # <BinOp left=<Value 'view/value' (9:23)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6af40cf340> -> __condition
            __expression = __cache_140097337751488

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                __append('value')
            else:
                __content = __cache_140097337751488
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append('</button>')
            if (__backup_bsFallback_140097247576992 is __marker):
                del econtext['bsFallback']
            else:
                econtext['bsFallback'] = __backup_bsFallback_140097247576992
            __append('\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }