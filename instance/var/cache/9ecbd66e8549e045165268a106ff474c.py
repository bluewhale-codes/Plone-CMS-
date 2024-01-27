# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/plone/app/z3cform/templates/password_input.pt'

__tokens = {419: ("s python:'form-control {0}{1}'.format(view.klass, view.error and ' is-invalid' or '", 19, 15), 368: ('view/id', 17, 14), 1198: (';\n           a', 39, 23), 1168: ('donly;\n ', 38, 28), 575: ('lang view', 22, 11), 1294: ('ize;\n         ', 42, 22), 392: (' view/nam', 18, 15), 1263: ('nselect;\n', 41, 26), 1009: ('        tabin', 34, 3), 548: ('tle view/t', 21, 13), 520: ('le view/st', 20, 14), 604: ('click view/o', 23, 13), 639: ('lclick view/ond', 24, 15), 678: ('usedown view/onm', 25, 15), 716: ('nmouseup view/', 26, 12), 754: ('mouseover view/o', 27, 13), 794: ('nmousemove view/', 28, 12), 833: (' onmouseout vie', 29, 10), 871: ('  onkeypress vi', 30, 9), 908: ('    onkeydown ', 31, 7), 942: ('       onkey', 32, 4), 975: ('       disabl', 33, 4), 1042: ('          on', 35, 1), 1073: ('\n          ', 35, 32), 1105: ('           on', 37, 0), 1139: ('\n           r', 37, 34), 1233: ('ey;\n         ', 40, 33), 1332: ('th;\n           p', 43, 33), 1375: (';\n           autoca', 44, 39)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140080122692944 = __C2ZContextWrapper
_static_140080122693232 = __compile_zt_expr
_static_140080037789760 = {'class': '', 'id': '', 'accesskey': '', 'alt': '', 'lang': '', 'maxlength': '', 'name': '', 'size': '', 'tabindex': '', 'title': '', 'type': 'password', 'style': 'view/style', 'onclick': 'view/onclick', 'ondblclick': 'view/ondblclick', 'onmousedown': 'view/onmousedown', 'onmouseup': 'view/onmouseup', 'onmouseover': 'view/onmouseover', 'onmousemove': 'view/onmousemove', 'onmouseout': 'view/onmouseout', 'onkeypress': 'view/onkeypress', 'onkeydown': 'view/onkeydown', 'onkeyup': 'view/onkeyup', 'disabled': 'view/disabled', 'onfocus': 'view/onfocus', 'onblur': 'view/onblur', 'onchange': 'view/onchange', 'readonly': 'view/readonly', 'onselect': 'view/onselect', 'placeholder': 'view/placeholder', 'autocapitalize': 'view/autocapitalize', }
_static_140080037795760 = {'xmlns': 'http://www.w3.org/1999/xhtml', }

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

            # <Static value=<ast.Dict object at 0x7f66ece497b0> name=None at 7f66ece48a00> -> __attrs_140080037796000
            __attrs_140080037796000 = _static_140080037795760
            __append('\n  ')

            # <Static value=<ast.Dict object at 0x7f66ece48040> name=None at 7f66ece48070> -> __attrs_140080037853936
            __attrs_140080037853936 = _static_140080037789760

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input')

            # <Symbol value=<DEFAULT> at 7f66f1ea2740> -> __default_140080037792976
            __default_140080037792976 = _DEFAULT_MARKER

            # <Substitution "python:'form-control {0}{1}'.format(view.klass, view.error and ' is-invalid' or '')" (19:15)> -> __attr_class
            __token = 419
            try:
                __zt_tmp = __attrs_140080037853936
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_140080122693232('python', "'form-control {0}{1}'.format(view.klass, view.error and ' is-invalid' or '')", econtext=econtext)(_static_140080122692944(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((' class="%s"' % __attr_class))

            # <Symbol value=<DEFAULT> at 7f66f1ea2740> -> __default_140080037791872
            __default_140080037791872 = _DEFAULT_MARKER

            # <Substitution 'view/id' (17:14)> -> __attr_id
            __token = 368
            try:
                __zt_tmp = __attrs_140080037853936
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_140080122693232('path', 'view/id', econtext=econtext)(_static_140080122692944(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_id is not None):
                __append((' id="%s"' % __attr_id))

            # <Symbol value=<DEFAULT> at 7f66f1ea2740> -> __default_140080037849232
            __default_140080037849232 = _DEFAULT_MARKER

            # <Substitution 'view/accesskey' (39:23)> -> __attr_accesskey
            __token = 1198
            try:
                __zt_tmp = __attrs_140080037853936
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_accesskey = _static_140080122693232('path', 'view/accesskey', econtext=econtext)(_static_140080122692944(econtext, __zt_tmp))
            __attr_accesskey = __quote(__attr_accesskey, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_accesskey is not None):
                __append((' accesskey="%s"' % __attr_accesskey))

            # <Symbol value=<DEFAULT> at 7f66f1ea2740> -> __default_140080037848704
            __default_140080037848704 = _DEFAULT_MARKER

            # <Substitution 'view/alt' (38:28)> -> __attr_alt
            __token = 1168
            try:
                __zt_tmp = __attrs_140080037853936
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_alt = _static_140080122693232('path', 'view/alt', econtext=econtext)(_static_140080122692944(econtext, __zt_tmp))
            __attr_alt = __quote(__attr_alt, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_alt is not None):
                __append((' alt="%s"' % __attr_alt))

            # <Symbol value=<DEFAULT> at 7f66f1ea2740> -> __default_140080037852304
            __default_140080037852304 = _DEFAULT_MARKER

            # <Substitution 'view/lang' (22:11)> -> __attr_lang
            __token = 575
            try:
                __zt_tmp = __attrs_140080037853936
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_lang = _static_140080122693232('path', 'view/lang', econtext=econtext)(_static_140080122692944(econtext, __zt_tmp))
            __attr_lang = __quote(__attr_lang, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_lang is not None):
                __append((' lang="%s"' % __attr_lang))

            # <Symbol value=<DEFAULT> at 7f66f1ea2740> -> __default_140080037848320
            __default_140080037848320 = _DEFAULT_MARKER

            # <Substitution 'view/maxlength' (42:22)> -> __attr_maxlength
            __token = 1294
            try:
                __zt_tmp = __attrs_140080037853936
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_maxlength = _static_140080122693232('path', 'view/maxlength', econtext=econtext)(_static_140080122692944(econtext, __zt_tmp))
            __attr_maxlength = __quote(__attr_maxlength, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_maxlength is not None):
                __append((' maxlength="%s"' % __attr_maxlength))

            # <Symbol value=<DEFAULT> at 7f66f1ea2740> -> __default_140080037854848
            __default_140080037854848 = _DEFAULT_MARKER

            # <Substitution 'view/name' (18:15)> -> __attr_name
            __token = 392
            try:
                __zt_tmp = __attrs_140080037853936
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_name = _static_140080122693232('path', 'view/name', econtext=econtext)(_static_140080122692944(econtext, __zt_tmp))
            __attr_name = __quote(__attr_name, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_name is not None):
                __append((' name="%s"' % __attr_name))

            # <Symbol value=<DEFAULT> at 7f66f1ea2740> -> __default_140080037851584
            __default_140080037851584 = _DEFAULT_MARKER

            # <Substitution 'view/size' (41:26)> -> __attr_size
            __token = 1263
            try:
                __zt_tmp = __attrs_140080037853936
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_size = _static_140080122693232('path', 'view/size', econtext=econtext)(_static_140080122692944(econtext, __zt_tmp))
            __attr_size = __quote(__attr_size, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_size is not None):
                __append((' size="%s"' % __attr_size))

            # <Symbol value=<DEFAULT> at 7f66f1ea2740> -> __default_140080037852688
            __default_140080037852688 = _DEFAULT_MARKER

            # <Substitution 'view/tabindex' (34:3)> -> __attr_tabindex
            __token = 1009
            try:
                __zt_tmp = __attrs_140080037853936
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_tabindex = _static_140080122693232('path', 'view/tabindex', econtext=econtext)(_static_140080122692944(econtext, __zt_tmp))
            __attr_tabindex = __quote(__attr_tabindex, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_tabindex is not None):
                __append((' tabindex="%s"' % __attr_tabindex))

            # <Symbol value=<DEFAULT> at 7f66f1ea2740> -> __default_140080037846736
            __default_140080037846736 = _DEFAULT_MARKER

            # <Substitution 'view/title' (21:13)> -> __attr_title
            __token = 548
            try:
                __zt_tmp = __attrs_140080037853936
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_title = _static_140080122693232('path', 'view/title', econtext=econtext)(_static_140080122692944(econtext, __zt_tmp))
            __attr_title = __quote(__attr_title, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_title is not None):
                __append((' title="%s"' % __attr_title))
            __append(' type="password"')

            # <Symbol value=<DEFAULT> at 7f66f1ea2740> -> __default_140080037851440
            __default_140080037851440 = _DEFAULT_MARKER

            # <Substitution 'view/style' (20:14)> -> __attr_style
            __token = 520
            try:
                __zt_tmp = __attrs_140080037853936
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_style = _static_140080122693232('path', 'view/style', econtext=econtext)(_static_140080122692944(econtext, __zt_tmp))
            __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_style is not None):
                __append((' style="%s"' % __attr_style))

            # <Symbol value=<DEFAULT> at 7f66f1ea2740> -> __default_140080037851248
            __default_140080037851248 = _DEFAULT_MARKER

            # <Substitution 'view/onclick' (23:13)> -> __attr_onclick
            __token = 604
            try:
                __zt_tmp = __attrs_140080037853936
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onclick = _static_140080122693232('path', 'view/onclick', econtext=econtext)(_static_140080122692944(econtext, __zt_tmp))
            __attr_onclick = __quote(__attr_onclick, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onclick is not None):
                __append((' onclick="%s"' % __attr_onclick))

            # <Symbol value=<DEFAULT> at 7f66f1ea2740> -> __default_140080037852064
            __default_140080037852064 = _DEFAULT_MARKER

            # <Substitution 'view/ondblclick' (24:15)> -> __attr_ondblclick
            __token = 639
            try:
                __zt_tmp = __attrs_140080037853936
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_ondblclick = _static_140080122693232('path', 'view/ondblclick', econtext=econtext)(_static_140080122692944(econtext, __zt_tmp))
            __attr_ondblclick = __quote(__attr_ondblclick, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_ondblclick is not None):
                __append((' ondblclick="%s"' % __attr_ondblclick))

            # <Symbol value=<DEFAULT> at 7f66f1ea2740> -> __default_140080037846880
            __default_140080037846880 = _DEFAULT_MARKER

            # <Substitution 'view/onmousedown' (25:15)> -> __attr_onmousedown
            __token = 678
            try:
                __zt_tmp = __attrs_140080037853936
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmousedown = _static_140080122693232('path', 'view/onmousedown', econtext=econtext)(_static_140080122692944(econtext, __zt_tmp))
            __attr_onmousedown = __quote(__attr_onmousedown, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmousedown is not None):
                __append((' onmousedown="%s"' % __attr_onmousedown))

            # <Symbol value=<DEFAULT> at 7f66f1ea2740> -> __default_140080037845920
            __default_140080037845920 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseup' (26:12)> -> __attr_onmouseup
            __token = 716
            try:
                __zt_tmp = __attrs_140080037853936
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseup = _static_140080122693232('path', 'view/onmouseup', econtext=econtext)(_static_140080122692944(econtext, __zt_tmp))
            __attr_onmouseup = __quote(__attr_onmouseup, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseup is not None):
                __append((' onmouseup="%s"' % __attr_onmouseup))

            # <Symbol value=<DEFAULT> at 7f66f1ea2740> -> __default_140080037847936
            __default_140080037847936 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseover' (27:13)> -> __attr_onmouseover
            __token = 754
            try:
                __zt_tmp = __attrs_140080037853936
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseover = _static_140080122693232('path', 'view/onmouseover', econtext=econtext)(_static_140080122692944(econtext, __zt_tmp))
            __attr_onmouseover = __quote(__attr_onmouseover, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseover is not None):
                __append((' onmouseover="%s"' % __attr_onmouseover))

            # <Symbol value=<DEFAULT> at 7f66f1ea2740> -> __default_140080037847360
            __default_140080037847360 = _DEFAULT_MARKER

            # <Substitution 'view/onmousemove' (28:12)> -> __attr_onmousemove
            __token = 794
            try:
                __zt_tmp = __attrs_140080037853936
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmousemove = _static_140080122693232('path', 'view/onmousemove', econtext=econtext)(_static_140080122692944(econtext, __zt_tmp))
            __attr_onmousemove = __quote(__attr_onmousemove, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmousemove is not None):
                __append((' onmousemove="%s"' % __attr_onmousemove))

            # <Symbol value=<DEFAULT> at 7f66f1ea2740> -> __default_140080037847648
            __default_140080037847648 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseout' (29:10)> -> __attr_onmouseout
            __token = 833
            try:
                __zt_tmp = __attrs_140080037853936
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseout = _static_140080122693232('path', 'view/onmouseout', econtext=econtext)(_static_140080122692944(econtext, __zt_tmp))
            __attr_onmouseout = __quote(__attr_onmouseout, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseout is not None):
                __append((' onmouseout="%s"' % __attr_onmouseout))

            # <Symbol value=<DEFAULT> at 7f66f1ea2740> -> __default_140080037842800
            __default_140080037842800 = _DEFAULT_MARKER

            # <Substitution 'view/onkeypress' (30:9)> -> __attr_onkeypress
            __token = 871
            try:
                __zt_tmp = __attrs_140080037853936
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeypress = _static_140080122693232('path', 'view/onkeypress', econtext=econtext)(_static_140080122692944(econtext, __zt_tmp))
            __attr_onkeypress = __quote(__attr_onkeypress, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeypress is not None):
                __append((' onkeypress="%s"' % __attr_onkeypress))

            # <Symbol value=<DEFAULT> at 7f66f1ea2740> -> __default_140080037849760
            __default_140080037849760 = _DEFAULT_MARKER

            # <Substitution 'view/onkeydown' (31:7)> -> __attr_onkeydown
            __token = 908
            try:
                __zt_tmp = __attrs_140080037853936
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeydown = _static_140080122693232('path', 'view/onkeydown', econtext=econtext)(_static_140080122692944(econtext, __zt_tmp))
            __attr_onkeydown = __quote(__attr_onkeydown, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeydown is not None):
                __append((' onkeydown="%s"' % __attr_onkeydown))

            # <Symbol value=<DEFAULT> at 7f66f1ea2740> -> __default_140080037849472
            __default_140080037849472 = _DEFAULT_MARKER

            # <Substitution 'view/onkeyup' (32:4)> -> __attr_onkeyup
            __token = 942
            try:
                __zt_tmp = __attrs_140080037853936
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeyup = _static_140080122693232('path', 'view/onkeyup', econtext=econtext)(_static_140080122692944(econtext, __zt_tmp))
            __attr_onkeyup = __quote(__attr_onkeyup, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeyup is not None):
                __append((' onkeyup="%s"' % __attr_onkeyup))

            # <Symbol value=<DEFAULT> at 7f66f1ea2740> -> __default_140080037855136
            __default_140080037855136 = _DEFAULT_MARKER

            # <Boolean 'view/disabled' (33:4)> -> __attr_disabled
            __token = 975
            try:
                __zt_tmp = __attrs_140080037853936
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_disabled = _static_140080122693232('path', 'view/disabled', econtext=econtext)(_static_140080122692944(econtext, __zt_tmp))
            if (__attr_disabled is _DEFAULT_MARKER):
                __attr_disabled = None
            else:
                if __attr_disabled:
                    __attr_disabled = 'disabled'
                else:
                    __attr_disabled = None
            if (__attr_disabled is not None):
                __append((' disabled="%s"' % __attr_disabled))

            # <Symbol value=<DEFAULT> at 7f66f1ea2740> -> __default_140080037854992
            __default_140080037854992 = _DEFAULT_MARKER

            # <Substitution 'view/onfocus' (35:1)> -> __attr_onfocus
            __token = 1042
            try:
                __zt_tmp = __attrs_140080037853936
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onfocus = _static_140080122693232('path', 'view/onfocus', econtext=econtext)(_static_140080122692944(econtext, __zt_tmp))
            __attr_onfocus = __quote(__attr_onfocus, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onfocus is not None):
                __append((' onfocus="%s"' % __attr_onfocus))

            # <Symbol value=<DEFAULT> at 7f66f1ea2740> -> __default_140080037854944
            __default_140080037854944 = _DEFAULT_MARKER

            # <Substitution 'view/onblur' (35:32)> -> __attr_onblur
            __token = 1073
            try:
                __zt_tmp = __attrs_140080037853936
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onblur = _static_140080122693232('path', 'view/onblur', econtext=econtext)(_static_140080122692944(econtext, __zt_tmp))
            __attr_onblur = __quote(__attr_onblur, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onblur is not None):
                __append((' onblur="%s"' % __attr_onblur))

            # <Symbol value=<DEFAULT> at 7f66f1ea2740> -> __default_140080037846976
            __default_140080037846976 = _DEFAULT_MARKER

            # <Substitution 'view/onchange' (37:0)> -> __attr_onchange
            __token = 1105
            try:
                __zt_tmp = __attrs_140080037853936
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onchange = _static_140080122693232('path', 'view/onchange', econtext=econtext)(_static_140080122692944(econtext, __zt_tmp))
            __attr_onchange = __quote(__attr_onchange, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onchange is not None):
                __append((' onchange="%s"' % __attr_onchange))

            # <Symbol value=<DEFAULT> at 7f66f1ea2740> -> __default_140080037850912
            __default_140080037850912 = _DEFAULT_MARKER

            # <Boolean 'view/readonly' (37:34)> -> __attr_readonly
            __token = 1139
            try:
                __zt_tmp = __attrs_140080037853936
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_readonly = _static_140080122693232('path', 'view/readonly', econtext=econtext)(_static_140080122692944(econtext, __zt_tmp))
            if (__attr_readonly is _DEFAULT_MARKER):
                __attr_readonly = None
            else:
                if __attr_readonly:
                    __attr_readonly = 'readonly'
                else:
                    __attr_readonly = None
            if (__attr_readonly is not None):
                __append((' readonly="%s"' % __attr_readonly))

            # <Symbol value=<DEFAULT> at 7f66f1ea2740> -> __default_140080037854080
            __default_140080037854080 = _DEFAULT_MARKER

            # <Substitution 'view/onselect' (40:33)> -> __attr_onselect
            __token = 1233
            try:
                __zt_tmp = __attrs_140080037853936
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onselect = _static_140080122693232('path', 'view/onselect', econtext=econtext)(_static_140080122692944(econtext, __zt_tmp))
            __attr_onselect = __quote(__attr_onselect, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onselect is not None):
                __append((' onselect="%s"' % __attr_onselect))

            # <Symbol value=<DEFAULT> at 7f66f1ea2740> -> __default_140080037851536
            __default_140080037851536 = _DEFAULT_MARKER

            # <Substitution 'view/placeholder' (43:33)> -> __attr_placeholder
            __token = 1332
            try:
                __zt_tmp = __attrs_140080037853936
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_placeholder = _static_140080122693232('path', 'view/placeholder', econtext=econtext)(_static_140080122692944(econtext, __zt_tmp))
            __attr_placeholder = __quote(__attr_placeholder, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_placeholder is not None):
                __append((' placeholder="%s"' % __attr_placeholder))

            # <Symbol value=<DEFAULT> at 7f66f1ea2740> -> __default_140080037850864
            __default_140080037850864 = _DEFAULT_MARKER

            # <Substitution 'view/autocapitalize' (44:39)> -> __attr_autocapitalize
            __token = 1375
            try:
                __zt_tmp = __attrs_140080037853936
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_autocapitalize = _static_140080122693232('path', 'view/autocapitalize', econtext=econtext)(_static_140080122692944(econtext, __zt_tmp))
            __attr_autocapitalize = __quote(__attr_autocapitalize, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_autocapitalize is not None):
                __append((' autocapitalize="%s"' % __attr_autocapitalize))
            __append(' />\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }