# -*- coding: utf-8 -*-
__filename = 'index_html'

__tokens = {56: ('template/title', 4, 24), 170: ('context/title_or_id', 9, 27), 247: ('template/title', 10, 29), 290: ('template/title', 11, 27), 386: ('template/id', 13, 43)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139867308416768 = {'charset': 'utf-8', }
_static_139867356405408 = __C2ZContextWrapper
_static_139867356405696 = __compile_zt_expr
_static_139867362323344 = {}

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
            __append('<!DOCTYPE html>\n')

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867308409472
            __attrs_139867308409472 = _static_139867362323344

            # <html ... (0:0)
            # --------------------------------------------------------
            __append('<html>\n  ')

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867308411440
            __attrs_139867308411440 = _static_139867362323344

            # <head ... (0:0)
            # --------------------------------------------------------
            __append('<head>\n    ')

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867308415760
            __attrs_139867308415760 = _static_139867362323344

            # <title ... (0:0)
            # --------------------------------------------------------
            __append('<title>')

            # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867308415232
            __default_139867308415232 = _DEFAULT_MARKER

            # <Value 'template/title' (4:24)> -> __cache_139867308413408
            __token = 56
            try:
                __zt_tmp = __attrs_139867308415760
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139867308413408 = _static_139867356405696('path', 'template/title', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))

            # <BinOp left=<Value 'template/title' (4:24)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f3568756860> at 7f35653bcfa0> -> __condition
            __expression = __cache_139867308413408

            # <Symbol value=<DEFAULT> at 7f3568756860> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                __append('The title')
            else:
                __content = __cache_139867308413408
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append('</title>\n    ')

            # <Static value=<ast.Dict object at 0x7f35653bdf00> name=None at 7f35653bdf30> -> __attrs_139867308417248
            __attrs_139867308417248 = _static_139867308416768

            # <meta ... (0:0)
            # --------------------------------------------------------
            __append('<meta charset="utf-8" />\n  </head>\n  ')

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867308417872
            __attrs_139867308417872 = _static_139867362323344

            # <body ... (0:0)
            # --------------------------------------------------------
            __append('<body>\n    \n    ')

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867308418784
            __attrs_139867308418784 = _static_139867362323344

            # <h2 ... (0:0)
            # --------------------------------------------------------
            __append('<h2>')

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867308420320
            __attrs_139867308420320 = _static_139867362323344

            # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867308420128
            __default_139867308420128 = _DEFAULT_MARKER

            # <Value 'context/title_or_id' (9:27)> -> __cache_139867308419648
            __token = 170
            try:
                __zt_tmp = __attrs_139867308420320
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139867308419648 = _static_139867356405696('path', 'context/title_or_id', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))

            # <BinOp left=<Value 'context/title_or_id' (9:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f3568756860> at 7f35653beb00> -> __condition
            __expression = __cache_139867308419648

            # <Symbol value=<DEFAULT> at 7f3568756860> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span>content title or id</span>')
            else:
                __content = __cache_139867308419648
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append('\n        ')

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867308421856
            __attrs_139867308421856 = _static_139867362323344

            # <Value 'template/title' (10:29)> -> __condition
            __token = 247
            try:
                __zt_tmp = __attrs_139867308421856
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_139867356405696('path', 'template/title', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            if __condition:

                # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867308421664
                __default_139867308421664 = _DEFAULT_MARKER

                # <Value 'template/title' (11:27)> -> __cache_139867308421184
                __token = 290
                try:
                    __zt_tmp = __attrs_139867308421856
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_139867308421184 = _static_139867356405696('path', 'template/title', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))

                # <BinOp left=<Value 'template/title' (11:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f3568756860> at 7f35653bf100> -> __condition
                __expression = __cache_139867308421184

                # <Symbol value=<DEFAULT> at 7f3568756860> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>optional template title</span>')
                else:
                    __content = __cache_139867308421184
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
            __append('</h2>\n\n    This is Page Template ')

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867308423392
            __attrs_139867308423392 = _static_139867362323344

            # <em ... (0:0)
            # --------------------------------------------------------
            __append('<em>')

            # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867308422816
            __default_139867308422816 = _DEFAULT_MARKER

            # <Value 'template/id' (13:43)> -> __cache_139867308422048
            __token = 386
            try:
                __zt_tmp = __attrs_139867308423392
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139867308422048 = _static_139867356405696('path', 'template/id', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))

            # <BinOp left=<Value 'template/id' (13:43)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f3568756860> at 7f35653bf580> -> __condition
            __expression = __cache_139867308422048

            # <Symbol value=<DEFAULT> at 7f3568756860> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                __append('template id')
            else:
                __content = __cache_139867308422048
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append('</em>.\n  </body>\n</html>')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }