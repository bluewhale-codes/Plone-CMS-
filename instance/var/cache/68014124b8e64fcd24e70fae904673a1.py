# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/plone/app/contenttypes/browser/templates/newsitem.pt'

__tokens = {519: ("python: getattr(context, 'table_of_contents', False)", 15, 32), 718: ("python:getattr(context, 'text', None)", 21, 30), 904: ("python: toc and 'pat-autotoc' or ''", 24, 23), 795: ('python:context.text.output_relative_to(view.context)', 22, 38), 247: ('context/@@main_template/macros/master', 6, 23), 247: ('context/@@main_template/macros/master', 6, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from collections import deque as _deque
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140097247589568 = 'master'
_static_140097338167536 = {'id': 'parent-fieldname-text', 'class': "python: toc and 'pat-autotoc' or ''", }
_static_140097247590816 = {'id': 'section-text', }
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

    def render_content_core(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097247590192
            __attrs_140097247590192 = _static_140097412968080
            __backup_toc_140097342594864 = get('toc', __marker)

            # <Value "python: getattr(context, 'table_of_contents', False)" (15:32)> -> __value
            __token = 519
            try:
                __zt_tmp = __attrs_140097247590192
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('python', " getattr(context, 'table_of_contents', False)", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['toc'] = __value
            __append('\n\n        ')

            # <Static value=<ast.Dict object at 0x7f6aeead39a0> name=None at 7f6aeead1450> -> __attrs_140097247578480
            __attrs_140097247578480 = _static_140097247590816

            # <section ... (0:0)
            # --------------------------------------------------------
            __append('<section id="section-text">\n          ')

            # <Static value=<ast.Dict object at 0x7f6af41350f0> name=None at 7f6af41341c0> -> __attrs_140097372459488
            __attrs_140097372459488 = _static_140097338167536

            # <Value "python:getattr(context, 'text', None)" (21:30)> -> __condition
            __token = 718
            try:
                __zt_tmp = __attrs_140097372459488
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140097413192464('python', "getattr(context, 'text', None)", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div id="parent-fieldname-text"')

                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338130592
                __default_140097338130592 = _DEFAULT_MARKER

                # <Substitution "python: toc and 'pat-autotoc' or ''" (24:23)> -> __attr_class
                __token = 904
                try:
                    __zt_tmp = __attrs_140097372459488
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_class = _static_140097413192464('python', " toc and 'pat-autotoc' or ''", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_class is not None):
                    __append((' class="%s"' % __attr_class))
                __append(' >')

                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097247581072
                __default_140097247581072 = _DEFAULT_MARKER

                # <Value 'python:context.text.output_relative_to(view.context)' (22:38)> -> __cache_140097247578816
                __token = 795
                try:
                    __zt_tmp = __attrs_140097372459488
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140097247578816 = _static_140097413192464('python', 'context.text.output_relative_to(view.context)', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                # <BinOp left=<Value 'python:context.text.output_relative_to(view.context)' (22:38)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeead2380> -> __condition
                __expression = __cache_140097247578816

                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('\n      Text\n          ')
                else:
                    __content = __cache_140097247578816
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('</div>')
            __append('\n        </section>\n\n      ')
            if (__backup_toc_140097342594864 is __marker):
                del econtext['toc']
            else:
                econtext['toc'] = __backup_toc_140097342594864
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

            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097247578624
            __attrs_140097247578624 = _static_140097412968080
            __previous_i18n_domain_140097247576656 = __i18n_domain
            __i18n_domain = 'plone'
            __backup_macroname_140097248048704 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f6aeead34c0> name=None at 7f6aeead3700> -> __value
            __value = _static_140097247589568
            econtext['macroname'] = __value

            def __fill_content_core(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097247577472
                __attrs_140097247577472 = _static_140097412968080
                __append('\n      ')
                __token = None
                render_content_core(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append('\n    ')
            _slots = econtext['__slot_content_core'] = _deque((__fill_content_core, ))

            # <Value 'context/@@main_template/macros/master' (6:23)> -> __macro
            __token = 247
            try:
                __zt_tmp = __attrs_140097247578624
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140097413192464('path', 'context/@@main_template/macros/master', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __token = 247
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140097248048704 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140097248048704
            __i18n_domain = __previous_i18n_domain_140097247576656
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_content_core': render_content_core, 'render': render, }