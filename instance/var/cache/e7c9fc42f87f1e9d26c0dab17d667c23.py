# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/Products/GenericSetup/browser/components.pt'

__tokens = {27: ('context/manage_page_header', 1, 27), 99: ('context/manage_tabs', 2, 27), 161: ('view/form_template', 4, 30), 212: ('context/manage_page_footer', 6, 27)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

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

            # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533346312272
            __attrs_140533346312272 = _static_140533416833664

            # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533346311744
            __default_140533346311744 = _DEFAULT_MARKER

            # <Value 'context/manage_page_header' (1:27)> -> __cache_140533346312896
            __token = 27
            try:
                __zt_tmp = __attrs_140533346312272
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140533346312896 = _static_140533417025280('path', 'context/manage_page_header', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))

            # <BinOp left=<Value 'context/manage_page_header' (1:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fd07c5afbe0> at 7fd0782f9d80> -> __condition
            __expression = __cache_140533346312896

            # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append('<h1>PAGE HEADER</h1>')
            else:
                __content = __cache_140533346312896
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n')

            # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533346314960
            __attrs_140533346314960 = _static_140533416833664

            # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533346315152
            __default_140533346315152 = _DEFAULT_MARKER

            # <Value 'context/manage_tabs' (2:27)> -> __cache_140533346312848
            __token = 99
            try:
                __zt_tmp = __attrs_140533346314960
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140533346312848 = _static_140533417025280('path', 'context/manage_tabs', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))

            # <BinOp left=<Value 'context/manage_tabs' (2:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fd07c5afbe0> at 7fd0782fb790> -> __condition
            __expression = __cache_140533346312848

            # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <h2 ... (0:0)
                # --------------------------------------------------------
                __append('<h2>TABS</h2>')
            else:
                __content = __cache_140533346312848
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533346313808
            __attrs_140533346313808 = _static_140533416833664

            # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533346314480
            __default_140533346314480 = _DEFAULT_MARKER

            # <Value 'view/form_template' (4:30)> -> __cache_140533346308480
            __token = 161
            try:
                __zt_tmp = __attrs_140533346313808
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140533346308480 = _static_140533417025280('path', 'view/form_template', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))

            # <BinOp left=<Value 'view/form_template' (4:30)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fd07c5afbe0> at 7fd0782fa6b0> -> __condition
            __expression = __cache_140533346308480

            # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140533346308480
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533346087408
            __attrs_140533346087408 = _static_140533416833664

            # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533346319856
            __default_140533346319856 = _DEFAULT_MARKER

            # <Value 'context/manage_page_footer' (6:27)> -> __cache_140533346319520
            __token = 212
            try:
                __zt_tmp = __attrs_140533346087408
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140533346319520 = _static_140533417025280('path', 'context/manage_page_footer', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))

            # <BinOp left=<Value 'context/manage_page_footer' (6:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fd07c5afbe0> at 7fd0782fbc40> -> __condition
            __expression = __cache_140533346319520

            # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append('<h1>PAGE FOOTER</h1>')
            else:
                __content = __cache_140533346319520
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }