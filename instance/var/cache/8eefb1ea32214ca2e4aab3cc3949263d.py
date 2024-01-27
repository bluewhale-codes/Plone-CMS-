# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/plone/app/dexterity/browser/typesformwrapper.pt'

__tokens = {509: ('view/label', 14, 25), 613: ('view/contents', 17, 39), 247: ('here/prefs_main_template/macros/master', 6, 23), 247: ('here/prefs_main_template/macros/master', 6, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from collections import deque as _deque
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140097339916144 = 'master'
_static_140097252663280 = {'id': 'skel-contents', }
_static_140097413192176 = __C2ZContextWrapper
_static_140097413192464 = __compile_zt_expr
_static_140097252655168 = {'class': 'documentFirstHeading', }
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

    def render_main(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097252660256
            __attrs_140097252660256 = _static_140097412968080
            __append('\n        ')

            # <Static value=<ast.Dict object at 0x7f6aeefa8040> name=None at 7f6aeefaada0> -> __attrs_140097252667840
            __attrs_140097252667840 = _static_140097252655168

            # <h1 ... (0:0)
            # --------------------------------------------------------
            __append('<h1 class="documentFirstHeading" >')

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252669280
            __default_140097252669280 = _DEFAULT_MARKER

            # <Value 'view/label' (14:25)> -> __cache_140097252664912
            __token = 509
            try:
                __zt_tmp = __attrs_140097252667840
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140097252664912 = _static_140097413192464('path', 'view/label', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

            # <BinOp left=<Value 'view/label' (14:25)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeefa8730> -> __condition
            __expression = __cache_140097252664912

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                __append('Title')
            else:
                __content = __cache_140097252664912
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append('</h1>\n        ')

            # <Static value=<ast.Dict object at 0x7f6aeefa9ff0> name=None at 7f6aeefa95d0> -> __attrs_140097252656560
            __attrs_140097252656560 = _static_140097252663280

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div id="skel-contents">\n          ')

            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097252657040
            __attrs_140097252657040 = _static_140097412968080

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252663568
            __default_140097252663568 = _DEFAULT_MARKER

            # <Value 'view/contents' (17:39)> -> __cache_140097252661408
            __token = 613
            try:
                __zt_tmp = __attrs_140097252657040
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140097252661408 = _static_140097413192464('path', 'view/contents', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

            # <BinOp left=<Value 'view/contents' (17:39)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeefa8b50> -> __condition
            __expression = __cache_140097252661408

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span></span>')
            else:
                __content = __cache_140097252661408
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n        </div>\n      ')
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

            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097339908992
            __attrs_140097339908992 = _static_140097412968080
            __previous_i18n_domain_140097339914176 = __i18n_domain
            __i18n_domain = 'plone'
            __backup_macroname_140097246822784 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f6af42dff70> name=None at 7f6af42df700> -> __value
            __value = _static_140097339916144
            econtext['macroname'] = __value

            def __fill_prefs_configlet_main(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097339907888
                __attrs_140097339907888 = _static_140097412968080
                __append('\n      ')
                __token = None
                render_main(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append('\n    ')
            _slots = econtext['__slot_prefs_configlet_main'] = _deque((__fill_prefs_configlet_main, ))

            # <Value 'here/prefs_main_template/macros/master' (6:23)> -> __macro
            __token = 247
            try:
                __zt_tmp = __attrs_140097339908992
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140097413192464('path', 'here/prefs_main_template/macros/master', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __token = 247
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140097246822784 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140097246822784
            __i18n_domain = __previous_i18n_domain_140097339914176
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_main': render_main, 'render': render, }