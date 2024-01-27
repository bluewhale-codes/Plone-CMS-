# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/plone/app/textfield/widget_textarea_display.pt'

__tokens = {138: ("python:getattr(view.field, 'output_mime_type', None) == 'text/x-html-safe'", 4, 23), 339: (' view/klas', 12, 15), 315: ('view/id', 11, 13), 366: ('e view/sty', 13, 14), 393: ('le view/ti', 14, 13), 419: ('ang view/', 15, 11), 447: ('lick view/on', 16, 13), 481: ('click view/ondb', 17, 15), 519: ('sedown view/onmo', 18, 15), 556: ('mouseup view/o', 19, 12), 593: ('ouseover view/on', 20, 13), 632: ('mousemove view/o', 21, 12), 670: ('onmouseout view', 22, 10), 707: (' onkeypress vie', 23, 9), 743: ('   onkeydown v', 24, 7), 776: ('      onkeyu', 25, 4), 839: ('view/value', 27, 25), 877: ('safe_structure', 27, 63), 929: ('view/value', 28, 36), 971: ('not: safe_structure', 29, 30), 1018: ('view/value', 30, 26)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140097412968080 = {}
_static_140097252669760 = {'class': '', 'id': '', 'style': 'view/style', 'title': 'view/title', 'lang': 'view/lang', 'onclick': 'view/onclick', 'ondblclick': 'view/ondblclick', 'onmousedown': 'view/onmousedown', 'onmouseup': 'view/onmouseup', 'onmouseover': 'view/onmouseover', 'onmousemove': 'view/onmousemove', 'onmouseout': 'view/onmouseout', 'onkeypress': 'view/onkeypress', 'onkeydown': 'view/onkeydown', 'onkeyup': 'view/onkeyup', }
_static_140097413192176 = __C2ZContextWrapper
_static_140097413192464 = __compile_zt_expr
_static_140097252658048 = {'xmlns': 'http://www.w3.org/1999/xhtml', }

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

            # <Static value=<ast.Dict object at 0x7f6aeefa8b80> name=None at 7f6aeefa9060> -> __attrs_140097252656992
            __attrs_140097252656992 = _static_140097252658048
            __backup_safe_structure_140097247475120 = get('safe_structure', __marker)

            # <Value "python:getattr(view.field, 'output_mime_type', None) == 'text/x-html-safe'" (4:23)> -> __value
            __token = 138
            try:
                __zt_tmp = __attrs_140097252656992
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('python', "getattr(view.field, 'output_mime_type', None) == 'text/x-html-safe'", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['safe_structure'] = __value
            __append('\n  ')

            # <Static value=<ast.Dict object at 0x7f6aeefab940> name=None at 7f6aeefabcd0> -> __attrs_140097252669328
            __attrs_140097252669328 = _static_140097252669760

            # <span ... (0:0)
            # --------------------------------------------------------
            __append('<span')

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252657568
            __default_140097252657568 = _DEFAULT_MARKER

            # <Substitution 'view/klass' (12:15)> -> __attr_class
            __token = 339
            try:
                __zt_tmp = __attrs_140097252669328
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_140097413192464('path', 'view/klass', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((' class="%s"' % __attr_class))

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252661264
            __default_140097252661264 = _DEFAULT_MARKER

            # <Substitution 'view/id' (11:13)> -> __attr_id
            __token = 315
            try:
                __zt_tmp = __attrs_140097252669328
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_140097413192464('path', 'view/id', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_id is not None):
                __append((' id="%s"' % __attr_id))

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252658384
            __default_140097252658384 = _DEFAULT_MARKER

            # <Substitution 'view/style' (13:14)> -> __attr_style
            __token = 366
            try:
                __zt_tmp = __attrs_140097252669328
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_style = _static_140097413192464('path', 'view/style', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_style is not None):
                __append((' style="%s"' % __attr_style))

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252663040
            __default_140097252663040 = _DEFAULT_MARKER

            # <Substitution 'view/title' (14:13)> -> __attr_title
            __token = 393
            try:
                __zt_tmp = __attrs_140097252669328
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_title = _static_140097413192464('path', 'view/title', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_title is not None):
                __append((' title="%s"' % __attr_title))

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252659392
            __default_140097252659392 = _DEFAULT_MARKER

            # <Substitution 'view/lang' (15:11)> -> __attr_lang
            __token = 419
            try:
                __zt_tmp = __attrs_140097252669328
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_lang = _static_140097413192464('path', 'view/lang', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_lang = __quote(__attr_lang, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_lang is not None):
                __append((' lang="%s"' % __attr_lang))

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252661504
            __default_140097252661504 = _DEFAULT_MARKER

            # <Substitution 'view/onclick' (16:13)> -> __attr_onclick
            __token = 447
            try:
                __zt_tmp = __attrs_140097252669328
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onclick = _static_140097413192464('path', 'view/onclick', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_onclick = __quote(__attr_onclick, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onclick is not None):
                __append((' onclick="%s"' % __attr_onclick))

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252668320
            __default_140097252668320 = _DEFAULT_MARKER

            # <Substitution 'view/ondblclick' (17:15)> -> __attr_ondblclick
            __token = 481
            try:
                __zt_tmp = __attrs_140097252669328
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_ondblclick = _static_140097413192464('path', 'view/ondblclick', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_ondblclick = __quote(__attr_ondblclick, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_ondblclick is not None):
                __append((' ondblclick="%s"' % __attr_ondblclick))

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252665632
            __default_140097252665632 = _DEFAULT_MARKER

            # <Substitution 'view/onmousedown' (18:15)> -> __attr_onmousedown
            __token = 519
            try:
                __zt_tmp = __attrs_140097252669328
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmousedown = _static_140097413192464('path', 'view/onmousedown', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_onmousedown = __quote(__attr_onmousedown, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmousedown is not None):
                __append((' onmousedown="%s"' % __attr_onmousedown))

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252663664
            __default_140097252663664 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseup' (19:12)> -> __attr_onmouseup
            __token = 556
            try:
                __zt_tmp = __attrs_140097252669328
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseup = _static_140097413192464('path', 'view/onmouseup', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_onmouseup = __quote(__attr_onmouseup, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseup is not None):
                __append((' onmouseup="%s"' % __attr_onmouseup))

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252666448
            __default_140097252666448 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseover' (20:13)> -> __attr_onmouseover
            __token = 593
            try:
                __zt_tmp = __attrs_140097252669328
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseover = _static_140097413192464('path', 'view/onmouseover', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_onmouseover = __quote(__attr_onmouseover, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseover is not None):
                __append((' onmouseover="%s"' % __attr_onmouseover))

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252661552
            __default_140097252661552 = _DEFAULT_MARKER

            # <Substitution 'view/onmousemove' (21:12)> -> __attr_onmousemove
            __token = 632
            try:
                __zt_tmp = __attrs_140097252669328
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmousemove = _static_140097413192464('path', 'view/onmousemove', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_onmousemove = __quote(__attr_onmousemove, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmousemove is not None):
                __append((' onmousemove="%s"' % __attr_onmousemove))

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252659104
            __default_140097252659104 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseout' (22:10)> -> __attr_onmouseout
            __token = 670
            try:
                __zt_tmp = __attrs_140097252669328
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseout = _static_140097413192464('path', 'view/onmouseout', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_onmouseout = __quote(__attr_onmouseout, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseout is not None):
                __append((' onmouseout="%s"' % __attr_onmouseout))

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252664048
            __default_140097252664048 = _DEFAULT_MARKER

            # <Substitution 'view/onkeypress' (23:9)> -> __attr_onkeypress
            __token = 707
            try:
                __zt_tmp = __attrs_140097252669328
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeypress = _static_140097413192464('path', 'view/onkeypress', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_onkeypress = __quote(__attr_onkeypress, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeypress is not None):
                __append((' onkeypress="%s"' % __attr_onkeypress))

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252668848
            __default_140097252668848 = _DEFAULT_MARKER

            # <Substitution 'view/onkeydown' (24:7)> -> __attr_onkeydown
            __token = 743
            try:
                __zt_tmp = __attrs_140097252669328
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeydown = _static_140097413192464('path', 'view/onkeydown', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_onkeydown = __quote(__attr_onkeydown, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeydown is not None):
                __append((' onkeydown="%s"' % __attr_onkeydown))

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252667744
            __default_140097252667744 = _DEFAULT_MARKER

            # <Substitution 'view/onkeyup' (25:4)> -> __attr_onkeyup
            __token = 776
            try:
                __zt_tmp = __attrs_140097252669328
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeyup = _static_140097413192464('path', 'view/onkeyup', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_onkeyup = __quote(__attr_onkeyup, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeyup is not None):
                __append((' onkeyup="%s"' % __attr_onkeyup))
            __append(' >')

            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097252669568
            __attrs_140097252669568 = _static_140097412968080

            # <Value 'view/value' (27:25)> -> __condition
            __token = 839
            try:
                __zt_tmp = __attrs_140097252669568
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140097413192464('path', 'view/value', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            if __condition:

                # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097252661648
                __attrs_140097252661648 = _static_140097412968080

                # <Value 'safe_structure' (27:63)> -> __condition
                __token = 877
                try:
                    __zt_tmp = __attrs_140097252661648
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140097413192464('path', 'safe_structure', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                if __condition:

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252667168
                    __default_140097252667168 = _DEFAULT_MARKER

                    # <Value 'view/value' (28:36)> -> __cache_140097252657808
                    __token = 929
                    try:
                        __zt_tmp = __attrs_140097252661648
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140097252657808 = _static_140097413192464('path', 'view/value', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                    # <BinOp left=<Value 'view/value' (28:36)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeefa82b0> -> __condition
                    __expression = __cache_140097252657808

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140097252657808
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)

                # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097252666976
                __attrs_140097252666976 = _static_140097412968080

                # <Value 'not: safe_structure' (29:30)> -> __condition
                __token = 971
                try:
                    __zt_tmp = __attrs_140097252666976
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140097413192464('not', ' safe_structure', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                if __condition:

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252671344
                    __default_140097252671344 = _DEFAULT_MARKER

                    # <Value 'view/value' (30:26)> -> __cache_140097252661360
                    __token = 1018
                    try:
                        __zt_tmp = __attrs_140097252666976
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140097252661360 = _static_140097413192464('path', 'view/value', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                    # <BinOp left=<Value 'view/value' (30:26)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeefa8250> -> __condition
                    __expression = __cache_140097252661360

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140097252661360
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
            __append('</span>\n')
            if (__backup_safe_structure_140097247475120 is __marker):
                del econtext['safe_structure']
            else:
                econtext['safe_structure'] = __backup_safe_structure_140097247475120
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }