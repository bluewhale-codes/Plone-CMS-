# -*- coding: utf-8 -*-
__filename = '/index_html'

__tokens = {56: ('template/title', 4, 24), 170: ('context/title_or_id', 9, 27), 247: ('template/title', 10, 29), 290: ('template/title', 11, 27), 386: ('template/id', 13, 43)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140097344175024 = {'charset': 'utf-8', }
_static_140097413192176 = __C2ZContextWrapper
_static_140097413192464 = __compile_zt_expr
_static_140097412968080 = {}

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

            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097344174304
            __attrs_140097344174304 = _static_140097412968080

            # <html ... (0:0)
            # --------------------------------------------------------
            __append('<html>\n  ')

            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097344175936
            __attrs_140097344175936 = _static_140097412968080

            # <head ... (0:0)
            # --------------------------------------------------------
            __append('<head>\n    ')

            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097344175456
            __attrs_140097344175456 = _static_140097412968080

            # <title ... (0:0)
            # --------------------------------------------------------
            __append('<title>')

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097344175264
            __default_140097344175264 = _DEFAULT_MARKER

            # <Value 'template/title' (4:24)> -> __cache_140097344172480
            __token = 56
            try:
                __zt_tmp = __attrs_140097344175456
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140097344172480 = _static_140097413192464('path', 'template/title', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

            # <BinOp left=<Value 'template/title' (4:24)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6af46efe50> -> __condition
            __expression = __cache_140097344172480

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                __append('The title')
            else:
                __content = __cache_140097344172480
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append('</title>\n    ')

            # <Static value=<ast.Dict object at 0x7f6af46efbb0> name=None at 7f6af46ef670> -> __attrs_140097344171232
            __attrs_140097344171232 = _static_140097344175024

            # <meta ... (0:0)
            # --------------------------------------------------------
            __append('<meta charset="utf-8" />\n  </head>\n  ')

            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097344356256
            __attrs_140097344356256 = _static_140097412968080

            # <body ... (0:0)
            # --------------------------------------------------------
            __append('<body>\n    \n    ')

            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097344355296
            __attrs_140097344355296 = _static_140097412968080

            # <h2 ... (0:0)
            # --------------------------------------------------------
            __append('<h2>')

            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097344353760
            __attrs_140097344353760 = _static_140097412968080

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097344353952
            __default_140097344353952 = _DEFAULT_MARKER

            # <Value 'context/title_or_id' (9:27)> -> __cache_140097344354432
            __token = 170
            try:
                __zt_tmp = __attrs_140097344353760
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140097344354432 = _static_140097413192464('path', 'context/title_or_id', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

            # <BinOp left=<Value 'context/title_or_id' (9:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6af471b7c0> -> __condition
            __expression = __cache_140097344354432

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span>content title or id</span>')
            else:
                __content = __cache_140097344354432
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append('\n        ')

            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097344352224
            __attrs_140097344352224 = _static_140097412968080

            # <Value 'template/title' (10:29)> -> __condition
            __token = 247
            try:
                __zt_tmp = __attrs_140097344352224
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140097413192464('path', 'template/title', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            if __condition:

                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097344352416
                __default_140097344352416 = _DEFAULT_MARKER

                # <Value 'template/title' (11:27)> -> __cache_140097344352896
                __token = 290
                try:
                    __zt_tmp = __attrs_140097344352224
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140097344352896 = _static_140097413192464('path', 'template/title', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                # <BinOp left=<Value 'template/title' (11:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6af471b1c0> -> __condition
                __expression = __cache_140097344352896

                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>optional template title</span>')
                else:
                    __content = __cache_140097344352896
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
            __append('</h2>\n\n    This is Page Template ')

            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097344350688
            __attrs_140097344350688 = _static_140097412968080

            # <em ... (0:0)
            # --------------------------------------------------------
            __append('<em>')

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097344351264
            __default_140097344351264 = _DEFAULT_MARKER

            # <Value 'template/id' (13:43)> -> __cache_140097344352032
            __token = 386
            try:
                __zt_tmp = __attrs_140097344350688
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140097344352032 = _static_140097413192464('path', 'template/id', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

            # <BinOp left=<Value 'template/id' (13:43)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6af471ad40> -> __condition
            __expression = __cache_140097344352032

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                __append('template id')
            else:
                __content = __cache_140097344352032
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append('</em>.\n  </body>\n</html>')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }