# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/Products/GenericSetup/browser/components_form.pt'

__tokens = {18: ('view/status', 1, 18), 95: ('request/ACTUAL_URL', 4, 29), 208: ('view/adapter/body', 7, 25)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140533346336976 = {'type': 'submit', 'name': 'apply', 'value': 'Apply', }
_static_140533346336928 = {'name': 'body', 'cols': '60', 'rows': '24', 'style': 'width: 600px;', }
_static_140533346343936 = {'action': '.', 'method': 'post', }
_static_140533417024992 = __C2ZContextWrapper
_static_140533417025280 = __compile_zt_expr
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

            # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533346346096
            __attrs_140533346346096 = _static_140533416833664

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div>')

            # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533346346768
            __default_140533346346768 = _DEFAULT_MARKER

            # <Value 'view/status' (1:18)> -> __cache_140533346349648
            __token = 18
            try:
                __zt_tmp = __attrs_140533346346096
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140533346349648 = _static_140533417025280('path', 'view/status', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))

            # <BinOp left=<Value 'view/status' (1:18)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fd07c5afbe0> at 7fd078303220> -> __condition
            __expression = __cache_140533346349648

            # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140533346349648
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append('</div>\n\n')

            # <Static value=<ast.Dict object at 0x7fd078301c00> name=None at 7fd0783022f0> -> __attrs_140533346343744
            __attrs_140533346343744 = _static_140533346343936

            # <form ... (0:0)
            # --------------------------------------------------------
            __append('<form')

            # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533346343408
            __default_140533346343408 = _DEFAULT_MARKER

            # <Substitution 'request/ACTUAL_URL' (4:29)> -> __attr_action
            __token = 95
            try:
                __zt_tmp = __attrs_140533346343744
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_action = _static_140533417025280('path', 'request/ACTUAL_URL', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
            __attr_action = __quote(__attr_action, '"', '&quot;', '.', _DEFAULT_MARKER)
            if (__attr_action is not None):
                __append((' action="%s"' % __attr_action))
            __append(' method="post">\n\n  ')

            # <Static value=<ast.Dict object at 0x7fd0783000a0> name=None at 7fd078300d00> -> __attrs_140533346337264
            __attrs_140533346337264 = _static_140533346336928

            # <textarea ... (0:0)
            # --------------------------------------------------------
            __append('<textarea name="body" cols="60" rows="24" style="width: 600px;">')

            # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533346342736
            __default_140533346342736 = _DEFAULT_MARKER

            # <Value 'view/adapter/body' (7:25)> -> __cache_140533346347632
            __token = 208
            try:
                __zt_tmp = __attrs_140533346337264
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140533346347632 = _static_140533417025280('path', 'view/adapter/body', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))

            # <BinOp left=<Value 'view/adapter/body' (7:25)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fd07c5afbe0> at 7fd078300310> -> __condition
            __expression = __cache_140533346347632

            # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140533346347632
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append('</textarea>\n\n  ')

            # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533346338416
            __attrs_140533346338416 = _static_140533416833664

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div>\n    ')

            # <Static value=<ast.Dict object at 0x7fd0783000d0> name=None at 7fd0783017b0> -> __attrs_140533346342496
            __attrs_140533346342496 = _static_140533346336976

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input type="submit" name="apply" value="Apply" />\n  </div>\n\n</form>\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }