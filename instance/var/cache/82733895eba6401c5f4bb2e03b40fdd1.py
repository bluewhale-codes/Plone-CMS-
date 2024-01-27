# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/plone/app/z3cform/templates/singlecheckboxbool_display.pt'

__tokens = {158: ('view/id', 6, 13), 182: (' view/klas', 7, 15), 209: ('e view/sty', 8, 14), 236: ('le view/ti', 9, 13), 262: ('ang view/', 10, 11), 290: ('lick view/on', 11, 13), 324: ('click view/ondb', 12, 15), 362: ('sedown view/onmo', 13, 15), 399: ('mouseup view/o', 14, 12), 436: ('ouseover view/on', 15, 13), 475: ('mousemove view/o', 16, 12), 513: ('onmouseout view', 17, 10), 550: (' onkeypress vie', 18, 9), 586: ('   onkeydown v', 19, 7), 619: ('      onkeyu', 20, 4), 681: ("python:view.displayValue[0] if view.displayValue else ''", 22, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140533416833664 = {}
_static_140533417024992 = __C2ZContextWrapper
_static_140533417025280 = __compile_zt_expr
_static_140533346152800 = {'id': 'view/id', 'class': 'view/klass', 'style': 'view/style', 'title': 'view/title', 'lang': 'view/lang', 'onclick': 'view/onclick', 'ondblclick': 'view/ondblclick', 'onmousedown': 'view/onmousedown', 'onmouseup': 'view/onmouseup', 'onmouseover': 'view/onmouseover', 'onmousemove': 'view/onmousemove', 'onmouseout': 'view/onmouseout', 'onkeypress': 'view/onkeypress', 'onkeydown': 'view/onkeydown', 'onkeyup': 'view/onkeyup', }
_static_140533345624480 = {'xmlns': 'http://www.w3.org/1999/xhtml', }

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

            # <Static value=<ast.Dict object at 0x7fd0782521a0> name=None at 7fd0782515a0> -> __attrs_140533346149920
            __attrs_140533346149920 = _static_140533345624480
            __append('\n  ')

            # <Static value=<ast.Dict object at 0x7fd0782d3160> name=None at 7fd0782d02b0> -> __attrs_140533343939088
            __attrs_140533343939088 = _static_140533346152800

            # <span ... (0:0)
            # --------------------------------------------------------
            __append('<span')

            # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533343941152
            __default_140533343941152 = _DEFAULT_MARKER

            # <Substitution 'view/id' (6:13)> -> __attr_id
            __token = 158
            try:
                __zt_tmp = __attrs_140533343939088
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_140533417025280('path', 'view/id', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_id is not None):
                __append((' id="%s"' % __attr_id))

            # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533343940912
            __default_140533343940912 = _DEFAULT_MARKER

            # <Substitution 'view/klass' (7:15)> -> __attr_class
            __token = 182
            try:
                __zt_tmp = __attrs_140533343939088
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_140533417025280('path', 'view/klass', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((' class="%s"' % __attr_class))

            # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533343931120
            __default_140533343931120 = _DEFAULT_MARKER

            # <Substitution 'view/style' (8:14)> -> __attr_style
            __token = 209
            try:
                __zt_tmp = __attrs_140533343939088
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_style = _static_140533417025280('path', 'view/style', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
            __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_style is not None):
                __append((' style="%s"' % __attr_style))

            # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533343943024
            __default_140533343943024 = _DEFAULT_MARKER

            # <Substitution 'view/title' (9:13)> -> __attr_title
            __token = 236
            try:
                __zt_tmp = __attrs_140533343939088
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_title = _static_140533417025280('path', 'view/title', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
            __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_title is not None):
                __append((' title="%s"' % __attr_title))

            # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533343929488
            __default_140533343929488 = _DEFAULT_MARKER

            # <Substitution 'view/lang' (10:11)> -> __attr_lang
            __token = 262
            try:
                __zt_tmp = __attrs_140533343939088
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_lang = _static_140533417025280('path', 'view/lang', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
            __attr_lang = __quote(__attr_lang, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_lang is not None):
                __append((' lang="%s"' % __attr_lang))

            # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533343941776
            __default_140533343941776 = _DEFAULT_MARKER

            # <Substitution 'view/onclick' (11:13)> -> __attr_onclick
            __token = 290
            try:
                __zt_tmp = __attrs_140533343939088
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onclick = _static_140533417025280('path', 'view/onclick', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
            __attr_onclick = __quote(__attr_onclick, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onclick is not None):
                __append((' onclick="%s"' % __attr_onclick))

            # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533343933088
            __default_140533343933088 = _DEFAULT_MARKER

            # <Substitution 'view/ondblclick' (12:15)> -> __attr_ondblclick
            __token = 324
            try:
                __zt_tmp = __attrs_140533343939088
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_ondblclick = _static_140533417025280('path', 'view/ondblclick', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
            __attr_ondblclick = __quote(__attr_ondblclick, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_ondblclick is not None):
                __append((' ondblclick="%s"' % __attr_ondblclick))

            # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533343929200
            __default_140533343929200 = _DEFAULT_MARKER

            # <Substitution 'view/onmousedown' (13:15)> -> __attr_onmousedown
            __token = 362
            try:
                __zt_tmp = __attrs_140533343939088
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmousedown = _static_140533417025280('path', 'view/onmousedown', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
            __attr_onmousedown = __quote(__attr_onmousedown, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmousedown is not None):
                __append((' onmousedown="%s"' % __attr_onmousedown))

            # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533343932704
            __default_140533343932704 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseup' (14:12)> -> __attr_onmouseup
            __token = 399
            try:
                __zt_tmp = __attrs_140533343939088
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseup = _static_140533417025280('path', 'view/onmouseup', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
            __attr_onmouseup = __quote(__attr_onmouseup, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseup is not None):
                __append((' onmouseup="%s"' % __attr_onmouseup))

            # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533343935104
            __default_140533343935104 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseover' (15:13)> -> __attr_onmouseover
            __token = 436
            try:
                __zt_tmp = __attrs_140533343939088
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseover = _static_140533417025280('path', 'view/onmouseover', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
            __attr_onmouseover = __quote(__attr_onmouseover, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseover is not None):
                __append((' onmouseover="%s"' % __attr_onmouseover))

            # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533343932128
            __default_140533343932128 = _DEFAULT_MARKER

            # <Substitution 'view/onmousemove' (16:12)> -> __attr_onmousemove
            __token = 475
            try:
                __zt_tmp = __attrs_140533343939088
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmousemove = _static_140533417025280('path', 'view/onmousemove', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
            __attr_onmousemove = __quote(__attr_onmousemove, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmousemove is not None):
                __append((' onmousemove="%s"' % __attr_onmousemove))

            # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533343938992
            __default_140533343938992 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseout' (17:10)> -> __attr_onmouseout
            __token = 513
            try:
                __zt_tmp = __attrs_140533343939088
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseout = _static_140533417025280('path', 'view/onmouseout', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
            __attr_onmouseout = __quote(__attr_onmouseout, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseout is not None):
                __append((' onmouseout="%s"' % __attr_onmouseout))

            # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533343944320
            __default_140533343944320 = _DEFAULT_MARKER

            # <Substitution 'view/onkeypress' (18:9)> -> __attr_onkeypress
            __token = 550
            try:
                __zt_tmp = __attrs_140533343939088
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeypress = _static_140533417025280('path', 'view/onkeypress', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
            __attr_onkeypress = __quote(__attr_onkeypress, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeypress is not None):
                __append((' onkeypress="%s"' % __attr_onkeypress))

            # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533343929296
            __default_140533343929296 = _DEFAULT_MARKER

            # <Substitution 'view/onkeydown' (19:7)> -> __attr_onkeydown
            __token = 586
            try:
                __zt_tmp = __attrs_140533343939088
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeydown = _static_140533417025280('path', 'view/onkeydown', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
            __attr_onkeydown = __quote(__attr_onkeydown, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeydown is not None):
                __append((' onkeydown="%s"' % __attr_onkeydown))

            # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533343940336
            __default_140533343940336 = _DEFAULT_MARKER

            # <Substitution 'view/onkeyup' (20:4)> -> __attr_onkeyup
            __token = 619
            try:
                __zt_tmp = __attrs_140533343939088
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeyup = _static_140533417025280('path', 'view/onkeyup', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
            __attr_onkeyup = __quote(__attr_onkeyup, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeyup is not None):
                __append((' onkeyup="%s"' % __attr_onkeyup))
            __append('>\n    ')

            # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533343935344
            __attrs_140533343935344 = _static_140533416833664

            # <span ... (0:0)
            # --------------------------------------------------------
            __append('<span>')

            # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533343928528
            __default_140533343928528 = _DEFAULT_MARKER

            # <Value "python:view.displayValue[0] if view.displayValue else ''" (22:23)> -> __cache_140533343935440
            __token = 681
            try:
                __zt_tmp = __attrs_140533343935344
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140533343935440 = _static_140533417025280('python', "view.displayValue[0] if view.displayValue else ''", econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))

            # <BinOp left=<Value "python:view.displayValue[0] if view.displayValue else ''" (22:23)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fd07c5afbe0> at 7fd0780b7eb0> -> __condition
            __expression = __cache_140533343935440

            # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140533343935440
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append('</span>\n  </span>\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }