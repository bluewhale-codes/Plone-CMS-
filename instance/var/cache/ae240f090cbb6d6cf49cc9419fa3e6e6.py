# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/plone/batching/batch_macros.pt'

__tokens = {344: ('batch|nothing', 11, 23), 389: (' batchformkeys|nothin', 12, 30), 518: ('nocall:context/@@batchnavigation', 17, 45), 627: ('python:batchnavigation(batch, batchformkeys)', 19, 46)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140533349003808 = {'xmlns': 'http://www.w3.org/1999/xhtml', }
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

    def render_navigation(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533343882880
            __attrs_140533343882880 = _static_140533416833664
            __backup_batch_140533344866208 = get('batch', __marker)

            # <Value 'batch|nothing' (11:23)> -> __value
            __token = 344
            try:
                __zt_tmp = __attrs_140533343882880
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140533417025280('path', 'batch|nothing', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
            econtext['batch'] = __value
            __backup_batchformkeys_140533344517856 = get('batchformkeys', __marker)

            # <Value 'batchformkeys|nothing' (12:30)> -> __value
            __token = 389
            try:
                __zt_tmp = __attrs_140533343882880
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140533417025280('path', 'batchformkeys|nothing', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
            econtext['batchformkeys'] = __value
            __append('\n\n      ')

            # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533343890176
            __attrs_140533343890176 = _static_140533416833664
            __backup_batchnavigation_140533344560480 = get('batchnavigation', __marker)

            # <Value 'nocall:context/@@batchnavigation' (17:45)> -> __value
            __token = 518
            try:
                __zt_tmp = __attrs_140533343890176
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140533417025280('nocall', 'context/@@batchnavigation', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
            econtext['batchnavigation'] = __value

            # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533343880240
            __default_140533343880240 = _DEFAULT_MARKER

            # <Value 'python:batchnavigation(batch, batchformkeys)' (19:46)> -> __cache_140533343880384
            __token = 627
            try:
                __zt_tmp = __attrs_140533343890176
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140533343880384 = _static_140533417025280('python', 'batchnavigation(batch, batchformkeys)', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))

            # <BinOp left=<Value 'python:batchnavigation(batch, batchformkeys)' (19:46)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fd07c5afbe0> at 7fd0780a8700> -> __condition
            __expression = __cache_140533343880384

            # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140533343880384
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            if (__backup_batchnavigation_140533344560480 is __marker):
                del econtext['batchnavigation']
            else:
                econtext['batchnavigation'] = __backup_batchnavigation_140533344560480
            __append('\n\n    ')
            if (__backup_batchformkeys_140533344517856 is __marker):
                del econtext['batchformkeys']
            else:
                econtext['batchformkeys'] = __backup_batchformkeys_140533344517856
            if (__backup_batch_140533344866208 is __marker):
                del econtext['batch']
            else:
                econtext['batch'] = __backup_batch_140533344866208
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


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

            # <Static value=<ast.Dict object at 0x7fd07858b220> name=None at 7fd078589ea0> -> __attrs_140533348998672
            __attrs_140533348998672 = _static_140533349003808
            __previous_i18n_domain_140533348999632 = __i18n_domain
            __i18n_domain = 'plone'

            # <html ... (0:0)
            # --------------------------------------------------------
            __append('<html xmlns="http://www.w3.org/1999/xhtml" >\n  ')

            # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533343888784
            __attrs_140533343888784 = _static_140533416833664

            # <body ... (0:0)
            # --------------------------------------------------------
            __append('<body>\n\n    ')
            __token = None
            render_navigation(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n\n  </body>\n</html>')
            __i18n_domain = __previous_i18n_domain_140533348999632
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_navigation': render_navigation, 'render': render, }