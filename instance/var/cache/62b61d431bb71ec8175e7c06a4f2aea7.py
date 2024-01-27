# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/plone/app/z3cform/templates/email_input.pt'

__tokens = {516: ("ss python:'form-control {0}{1}'.format(view.klass, view.error and ' is-invalid' or ", 22, 14), 401: ('view/id', 19, 14), 1323: ('lt;\n          ', 43, 21), 1293: ('eadonly;', 42, 26), 672: (' lang vie', 25, 10), 1419: ('/size;\n       ', 46, 20), 425: (' view/nam', 20, 15), 1388: ('/onselect', 45, 24), 617: ('yle view/s', 23, 13), 1134: ('          tab', 38, 1), 645: ('itle view/', 24, 12), 1069: ('          ', 36, 0), 455: ("d python:view.required and 'required' or No", 21, 18), 701: ('nclick view/', 26, 12), 736: ('blclick view/on', 27, 14), 775: ('ousedown view/on', 28, 14), 813: ('onmouseup view', 29, 11), 851: ('nmouseover view/', 30, 12), 891: ('onmousemove view', 31, 11), 930: ('  onmouseout vi', 32, 9), 968: ('   onkeypress v', 33, 8), 1005: ('     onkeydown', 34, 6), 1039: ('        onke', 35, 3), 1100: ('         disa', 37, 2), 1167: ('\n           ', 38, 34), 1198: ('s;\n        ', 39, 30), 1230: (';\n           ', 40, 29), 1264: ('e;\n          ', 41, 32), 1358: ('skey;\n       ', 44, 31), 1457: ('ngth;\n          ', 47, 31), 1500: ('er;\n           auto', 48, 37)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139906490555248 = __C2ZContextWrapper
_static_139906490555536 = __compile_zt_expr
_static_139906201334832 = {'class': '', 'id': '', 'accesskey': '', 'alt': '', 'lang': '', 'maxlength': '', 'name': '', 'size': '', 'style': '', 'tabindex': '', 'title': '', 'type': 'email', 'value': '', 'required': "python:view.required and 'required' or None", 'onclick': 'view/onclick', 'ondblclick': 'view/ondblclick', 'onmousedown': 'view/onmousedown', 'onmouseup': 'view/onmouseup', 'onmouseover': 'view/onmouseover', 'onmousemove': 'view/onmousemove', 'onmouseout': 'view/onmouseout', 'onkeypress': 'view/onkeypress', 'onkeydown': 'view/onkeydown', 'onkeyup': 'view/onkeyup', 'disabled': 'view/disabled', 'onfocus': 'view/onfocus', 'onblur': 'view/onblur', 'onchange': 'view/onchange', 'readonly': 'view/readonly', 'onselect': 'view/onselect', 'placeholder': 'view/placeholder', 'autocapitalize': 'view/autocapitalize', }
_static_139906201325808 = {'xmlns': 'http://www.w3.org/1999/xhtml', }

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

            # <Static value=<ast.Dict object at 0x7f3e736e90f0> name=None at 7f3e736e98a0> -> __attrs_139906201322592
            __attrs_139906201322592 = _static_139906201325808
            __append('\n  ')

            # <Static value=<ast.Dict object at 0x7f3e736eb430> name=None at 7f3e736eb4f0> -> __attrs_139906200933504
            __attrs_139906200933504 = _static_139906201334832

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input')

            # <Symbol value=<DEFAULT> at 7f3e84a07cd0> -> __default_139906201325280
            __default_139906201325280 = _DEFAULT_MARKER

            # <Substitution "python:'form-control {0}{1}'.format(view.klass, view.error and ' is-invalid' or '')" (22:14)> -> __attr_class
            __token = 516
            try:
                __zt_tmp = __attrs_139906200933504
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_139906490555536('python', "'form-control {0}{1}'.format(view.klass, view.error and ' is-invalid' or '')", econtext=econtext)(_static_139906490555248(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((' class="%s"' % __attr_class))

            # <Symbol value=<DEFAULT> at 7f3e84a07cd0> -> __default_139906201326912
            __default_139906201326912 = _DEFAULT_MARKER

            # <Substitution 'view/id' (19:14)> -> __attr_id
            __token = 401
            try:
                __zt_tmp = __attrs_139906200933504
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_139906490555536('path', 'view/id', econtext=econtext)(_static_139906490555248(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_id is not None):
                __append((' id="%s"' % __attr_id))

            # <Symbol value=<DEFAULT> at 7f3e84a07cd0> -> __default_139906201323312
            __default_139906201323312 = _DEFAULT_MARKER

            # <Substitution 'view/accesskey' (43:21)> -> __attr_accesskey
            __token = 1323
            try:
                __zt_tmp = __attrs_139906200933504
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_accesskey = _static_139906490555536('path', 'view/accesskey', econtext=econtext)(_static_139906490555248(econtext, __zt_tmp))
            __attr_accesskey = __quote(__attr_accesskey, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_accesskey is not None):
                __append((' accesskey="%s"' % __attr_accesskey))

            # <Symbol value=<DEFAULT> at 7f3e84a07cd0> -> __default_139906201333920
            __default_139906201333920 = _DEFAULT_MARKER

            # <Substitution 'view/alt' (42:26)> -> __attr_alt
            __token = 1293
            try:
                __zt_tmp = __attrs_139906200933504
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_alt = _static_139906490555536('path', 'view/alt', econtext=econtext)(_static_139906490555248(econtext, __zt_tmp))
            __attr_alt = __quote(__attr_alt, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_alt is not None):
                __append((' alt="%s"' % __attr_alt))

            # <Symbol value=<DEFAULT> at 7f3e84a07cd0> -> __default_139906201333440
            __default_139906201333440 = _DEFAULT_MARKER

            # <Substitution 'view/lang' (25:10)> -> __attr_lang
            __token = 672
            try:
                __zt_tmp = __attrs_139906200933504
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_lang = _static_139906490555536('path', 'view/lang', econtext=econtext)(_static_139906490555248(econtext, __zt_tmp))
            __attr_lang = __quote(__attr_lang, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_lang is not None):
                __append((' lang="%s"' % __attr_lang))

            # <Symbol value=<DEFAULT> at 7f3e84a07cd0> -> __default_139906201333392
            __default_139906201333392 = _DEFAULT_MARKER

            # <Substitution 'view/maxlength' (46:20)> -> __attr_maxlength
            __token = 1419
            try:
                __zt_tmp = __attrs_139906200933504
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_maxlength = _static_139906490555536('path', 'view/maxlength', econtext=econtext)(_static_139906490555248(econtext, __zt_tmp))
            __attr_maxlength = __quote(__attr_maxlength, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_maxlength is not None):
                __append((' maxlength="%s"' % __attr_maxlength))

            # <Symbol value=<DEFAULT> at 7f3e84a07cd0> -> __default_139906201335744
            __default_139906201335744 = _DEFAULT_MARKER

            # <Substitution 'view/name' (20:15)> -> __attr_name
            __token = 425
            try:
                __zt_tmp = __attrs_139906200933504
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_name = _static_139906490555536('path', 'view/name', econtext=econtext)(_static_139906490555248(econtext, __zt_tmp))
            __attr_name = __quote(__attr_name, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_name is not None):
                __append((' name="%s"' % __attr_name))

            # <Symbol value=<DEFAULT> at 7f3e84a07cd0> -> __default_139906201323552
            __default_139906201323552 = _DEFAULT_MARKER

            # <Substitution 'view/size' (45:24)> -> __attr_size
            __token = 1388
            try:
                __zt_tmp = __attrs_139906200933504
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_size = _static_139906490555536('path', 'view/size', econtext=econtext)(_static_139906490555248(econtext, __zt_tmp))
            __attr_size = __quote(__attr_size, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_size is not None):
                __append((' size="%s"' % __attr_size))

            # <Symbol value=<DEFAULT> at 7f3e84a07cd0> -> __default_139906201326624
            __default_139906201326624 = _DEFAULT_MARKER

            # <Substitution 'view/style' (23:13)> -> __attr_style
            __token = 617
            try:
                __zt_tmp = __attrs_139906200933504
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_style = _static_139906490555536('path', 'view/style', econtext=econtext)(_static_139906490555248(econtext, __zt_tmp))
            __attr_style = __quote(__attr_style, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_style is not None):
                __append((' style="%s"' % __attr_style))

            # <Symbol value=<DEFAULT> at 7f3e84a07cd0> -> __default_139906201326576
            __default_139906201326576 = _DEFAULT_MARKER

            # <Substitution 'view/tabindex' (38:1)> -> __attr_tabindex
            __token = 1134
            try:
                __zt_tmp = __attrs_139906200933504
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_tabindex = _static_139906490555536('path', 'view/tabindex', econtext=econtext)(_static_139906490555248(econtext, __zt_tmp))
            __attr_tabindex = __quote(__attr_tabindex, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_tabindex is not None):
                __append((' tabindex="%s"' % __attr_tabindex))

            # <Symbol value=<DEFAULT> at 7f3e84a07cd0> -> __default_139906201322256
            __default_139906201322256 = _DEFAULT_MARKER

            # <Substitution 'view/title' (24:12)> -> __attr_title
            __token = 645
            try:
                __zt_tmp = __attrs_139906200933504
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_title = _static_139906490555536('path', 'view/title', econtext=econtext)(_static_139906490555248(econtext, __zt_tmp))
            __attr_title = __quote(__attr_title, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_title is not None):
                __append((' title="%s"' % __attr_title))
            __append(' type="email"')

            # <Symbol value=<DEFAULT> at 7f3e84a07cd0> -> __default_139906201327104
            __default_139906201327104 = _DEFAULT_MARKER

            # <Substitution 'view/value' (36:0)> -> __attr_value
            __token = 1069
            try:
                __zt_tmp = __attrs_139906200933504
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_value = _static_139906490555536('path', 'view/value', econtext=econtext)(_static_139906490555248(econtext, __zt_tmp))
            __attr_value = __quote(__attr_value, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_value is not None):
                __append((' value="%s"' % __attr_value))

            # <Symbol value=<DEFAULT> at 7f3e84a07cd0> -> __default_139906200929424
            __default_139906200929424 = _DEFAULT_MARKER

            # <Substitution "python:view.required and 'required' or None" (21:18)> -> __attr_required
            __token = 455
            try:
                __zt_tmp = __attrs_139906200933504
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_required = _static_139906490555536('python', "view.required and 'required' or None", econtext=econtext)(_static_139906490555248(econtext, __zt_tmp))
            __attr_required = __quote(__attr_required, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_required is not None):
                __append((' required="%s"' % __attr_required))

            # <Symbol value=<DEFAULT> at 7f3e84a07cd0> -> __default_139906200939600
            __default_139906200939600 = _DEFAULT_MARKER

            # <Substitution 'view/onclick' (26:12)> -> __attr_onclick
            __token = 701
            try:
                __zt_tmp = __attrs_139906200933504
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onclick = _static_139906490555536('path', 'view/onclick', econtext=econtext)(_static_139906490555248(econtext, __zt_tmp))
            __attr_onclick = __quote(__attr_onclick, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onclick is not None):
                __append((' onclick="%s"' % __attr_onclick))

            # <Symbol value=<DEFAULT> at 7f3e84a07cd0> -> __default_139906200937728
            __default_139906200937728 = _DEFAULT_MARKER

            # <Substitution 'view/ondblclick' (27:14)> -> __attr_ondblclick
            __token = 736
            try:
                __zt_tmp = __attrs_139906200933504
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_ondblclick = _static_139906490555536('path', 'view/ondblclick', econtext=econtext)(_static_139906490555248(econtext, __zt_tmp))
            __attr_ondblclick = __quote(__attr_ondblclick, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_ondblclick is not None):
                __append((' ondblclick="%s"' % __attr_ondblclick))

            # <Symbol value=<DEFAULT> at 7f3e84a07cd0> -> __default_139906200937824
            __default_139906200937824 = _DEFAULT_MARKER

            # <Substitution 'view/onmousedown' (28:14)> -> __attr_onmousedown
            __token = 775
            try:
                __zt_tmp = __attrs_139906200933504
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmousedown = _static_139906490555536('path', 'view/onmousedown', econtext=econtext)(_static_139906490555248(econtext, __zt_tmp))
            __attr_onmousedown = __quote(__attr_onmousedown, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmousedown is not None):
                __append((' onmousedown="%s"' % __attr_onmousedown))

            # <Symbol value=<DEFAULT> at 7f3e84a07cd0> -> __default_139906200937248
            __default_139906200937248 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseup' (29:11)> -> __attr_onmouseup
            __token = 813
            try:
                __zt_tmp = __attrs_139906200933504
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseup = _static_139906490555536('path', 'view/onmouseup', econtext=econtext)(_static_139906490555248(econtext, __zt_tmp))
            __attr_onmouseup = __quote(__attr_onmouseup, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseup is not None):
                __append((' onmouseup="%s"' % __attr_onmouseup))

            # <Symbol value=<DEFAULT> at 7f3e84a07cd0> -> __default_139906200929952
            __default_139906200929952 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseover' (30:12)> -> __attr_onmouseover
            __token = 851
            try:
                __zt_tmp = __attrs_139906200933504
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseover = _static_139906490555536('path', 'view/onmouseover', econtext=econtext)(_static_139906490555248(econtext, __zt_tmp))
            __attr_onmouseover = __quote(__attr_onmouseover, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseover is not None):
                __append((' onmouseover="%s"' % __attr_onmouseover))

            # <Symbol value=<DEFAULT> at 7f3e84a07cd0> -> __default_139906200930384
            __default_139906200930384 = _DEFAULT_MARKER

            # <Substitution 'view/onmousemove' (31:11)> -> __attr_onmousemove
            __token = 891
            try:
                __zt_tmp = __attrs_139906200933504
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmousemove = _static_139906490555536('path', 'view/onmousemove', econtext=econtext)(_static_139906490555248(econtext, __zt_tmp))
            __attr_onmousemove = __quote(__attr_onmousemove, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmousemove is not None):
                __append((' onmousemove="%s"' % __attr_onmousemove))

            # <Symbol value=<DEFAULT> at 7f3e84a07cd0> -> __default_139906200933888
            __default_139906200933888 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseout' (32:9)> -> __attr_onmouseout
            __token = 930
            try:
                __zt_tmp = __attrs_139906200933504
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseout = _static_139906490555536('path', 'view/onmouseout', econtext=econtext)(_static_139906490555248(econtext, __zt_tmp))
            __attr_onmouseout = __quote(__attr_onmouseout, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseout is not None):
                __append((' onmouseout="%s"' % __attr_onmouseout))

            # <Symbol value=<DEFAULT> at 7f3e84a07cd0> -> __default_139906200943920
            __default_139906200943920 = _DEFAULT_MARKER

            # <Substitution 'view/onkeypress' (33:8)> -> __attr_onkeypress
            __token = 968
            try:
                __zt_tmp = __attrs_139906200933504
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeypress = _static_139906490555536('path', 'view/onkeypress', econtext=econtext)(_static_139906490555248(econtext, __zt_tmp))
            __attr_onkeypress = __quote(__attr_onkeypress, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeypress is not None):
                __append((' onkeypress="%s"' % __attr_onkeypress))

            # <Symbol value=<DEFAULT> at 7f3e84a07cd0> -> __default_139906200932400
            __default_139906200932400 = _DEFAULT_MARKER

            # <Substitution 'view/onkeydown' (34:6)> -> __attr_onkeydown
            __token = 1005
            try:
                __zt_tmp = __attrs_139906200933504
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeydown = _static_139906490555536('path', 'view/onkeydown', econtext=econtext)(_static_139906490555248(econtext, __zt_tmp))
            __attr_onkeydown = __quote(__attr_onkeydown, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeydown is not None):
                __append((' onkeydown="%s"' % __attr_onkeydown))

            # <Symbol value=<DEFAULT> at 7f3e84a07cd0> -> __default_139906200937920
            __default_139906200937920 = _DEFAULT_MARKER

            # <Substitution 'view/onkeyup' (35:3)> -> __attr_onkeyup
            __token = 1039
            try:
                __zt_tmp = __attrs_139906200933504
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeyup = _static_139906490555536('path', 'view/onkeyup', econtext=econtext)(_static_139906490555248(econtext, __zt_tmp))
            __attr_onkeyup = __quote(__attr_onkeyup, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeyup is not None):
                __append((' onkeyup="%s"' % __attr_onkeyup))

            # <Symbol value=<DEFAULT> at 7f3e84a07cd0> -> __default_139906200938112
            __default_139906200938112 = _DEFAULT_MARKER

            # <Boolean 'view/disabled' (37:2)> -> __attr_disabled
            __token = 1100
            try:
                __zt_tmp = __attrs_139906200933504
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

            # <Symbol value=<DEFAULT> at 7f3e84a07cd0> -> __default_139906200940272
            __default_139906200940272 = _DEFAULT_MARKER

            # <Substitution 'view/onfocus' (38:34)> -> __attr_onfocus
            __token = 1167
            try:
                __zt_tmp = __attrs_139906200933504
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onfocus = _static_139906490555536('path', 'view/onfocus', econtext=econtext)(_static_139906490555248(econtext, __zt_tmp))
            __attr_onfocus = __quote(__attr_onfocus, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onfocus is not None):
                __append((' onfocus="%s"' % __attr_onfocus))

            # <Symbol value=<DEFAULT> at 7f3e84a07cd0> -> __default_139906200940224
            __default_139906200940224 = _DEFAULT_MARKER

            # <Substitution 'view/onblur' (39:30)> -> __attr_onblur
            __token = 1198
            try:
                __zt_tmp = __attrs_139906200933504
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onblur = _static_139906490555536('path', 'view/onblur', econtext=econtext)(_static_139906490555248(econtext, __zt_tmp))
            __attr_onblur = __quote(__attr_onblur, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onblur is not None):
                __append((' onblur="%s"' % __attr_onblur))

            # <Symbol value=<DEFAULT> at 7f3e84a07cd0> -> __default_139906200940800
            __default_139906200940800 = _DEFAULT_MARKER

            # <Substitution 'view/onchange' (40:29)> -> __attr_onchange
            __token = 1230
            try:
                __zt_tmp = __attrs_139906200933504
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onchange = _static_139906490555536('path', 'view/onchange', econtext=econtext)(_static_139906490555248(econtext, __zt_tmp))
            __attr_onchange = __quote(__attr_onchange, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onchange is not None):
                __append((' onchange="%s"' % __attr_onchange))

            # <Symbol value=<DEFAULT> at 7f3e84a07cd0> -> __default_139906200928944
            __default_139906200928944 = _DEFAULT_MARKER

            # <Boolean 'view/readonly' (41:32)> -> __attr_readonly
            __token = 1264
            try:
                __zt_tmp = __attrs_139906200933504
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

            # <Symbol value=<DEFAULT> at 7f3e84a07cd0> -> __default_139906200934512
            __default_139906200934512 = _DEFAULT_MARKER

            # <Substitution 'view/onselect' (44:31)> -> __attr_onselect
            __token = 1358
            try:
                __zt_tmp = __attrs_139906200933504
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onselect = _static_139906490555536('path', 'view/onselect', econtext=econtext)(_static_139906490555248(econtext, __zt_tmp))
            __attr_onselect = __quote(__attr_onselect, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onselect is not None):
                __append((' onselect="%s"' % __attr_onselect))

            # <Symbol value=<DEFAULT> at 7f3e84a07cd0> -> __default_139906200934272
            __default_139906200934272 = _DEFAULT_MARKER

            # <Substitution 'view/placeholder' (47:31)> -> __attr_placeholder
            __token = 1457
            try:
                __zt_tmp = __attrs_139906200933504
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_placeholder = _static_139906490555536('path', 'view/placeholder', econtext=econtext)(_static_139906490555248(econtext, __zt_tmp))
            __attr_placeholder = __quote(__attr_placeholder, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_placeholder is not None):
                __append((' placeholder="%s"' % __attr_placeholder))

            # <Symbol value=<DEFAULT> at 7f3e84a07cd0> -> __default_139906200933840
            __default_139906200933840 = _DEFAULT_MARKER

            # <Substitution 'view/autocapitalize' (48:37)> -> __attr_autocapitalize
            __token = 1500
            try:
                __zt_tmp = __attrs_139906200933504
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_autocapitalize = _static_139906490555536('path', 'view/autocapitalize', econtext=econtext)(_static_139906490555248(econtext, __zt_tmp))
            __attr_autocapitalize = __quote(__attr_autocapitalize, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_autocapitalize is not None):
                __append((' autocapitalize="%s"' % __attr_autocapitalize))
            __append(' />\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }