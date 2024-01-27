# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/plone/app/layout/viewlets/contentviews.pt'

__tokens = {61: ('context/@@plone', 2, 30), 131: ('ploneview/showToolbar', 4, 33), 240: ('view/tabSet1', 9, 23), 302: ('python: view.menu_template(actions=actions)', 11, 32), 460: ('provider:plone.contentmenu', 17, 32), 600: ('view/tabSet2', 23, 23), 662: ('python: view.menu_template(actions=actions)', 25, 32)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139867199506992 = {'class': 'border-top my-2', }
_static_139867199510880 = {'class': 'border-top my-2', }
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

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867199516208
            __attrs_139867199516208 = _static_139867362323344
            __backup_ploneview_139867202227312 = get('ploneview', __marker)

            # <Value 'context/@@plone' (2:30)> -> __value
            __token = 61
            try:
                __zt_tmp = __attrs_139867199516208
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139867356405696('path', 'context/@@plone', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            econtext['ploneview'] = __value

            # <Value 'ploneview/showToolbar' (4:33)> -> __condition
            __token = 131
            try:
                __zt_tmp = __attrs_139867199516208
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_139867356405696('path', 'ploneview/showToolbar', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_139867199516640 = __i18n_domain
                __i18n_domain = 'plone'
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867199517408
                __attrs_139867199517408 = _static_139867362323344
                __backup_actions_139867202237776 = get('actions', __marker)

                # <Value 'view/tabSet1' (9:23)> -> __value
                __token = 240
                try:
                    __zt_tmp = __attrs_139867199517408
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139867356405696('path', 'view/tabSet1', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                econtext['actions'] = __value
                __append('\n    ')

                # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867199511408
                __attrs_139867199511408 = _static_139867362323344

                # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867199508864
                __default_139867199508864 = _DEFAULT_MARKER

                # <Value 'python: view.menu_template(actions=actions)' (11:32)> -> __cache_139867199511936
                __token = 302
                try:
                    __zt_tmp = __attrs_139867199511408
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_139867199511936 = _static_139867356405696('python', ' view.menu_template(actions=actions)', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))

                # <BinOp left=<Value 'python: view.menu_template(actions=actions)' (11:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f3568756860> at 7f355ebe1c30> -> __condition
                __expression = __cache_139867199511936

                # <Symbol value=<DEFAULT> at 7f3568756860> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div></div>')
                else:
                    __content = __cache_139867199511936
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n  ')
                if (__backup_actions_139867202237776 is __marker):
                    del econtext['actions']
                else:
                    econtext['actions'] = __backup_actions_139867202237776
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x7f355ebe1960> name=None at 7f355ebe19c0> -> __attrs_139867199510304
                __attrs_139867199510304 = _static_139867199510880

                # <li ... (0:0)
                # --------------------------------------------------------
                __append('<li class="border-top my-2"></li>\n\n  ')

                # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867199509824
                __attrs_139867199509824 = _static_139867362323344
                __append('\n    ')

                # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867199507328
                __attrs_139867199507328 = _static_139867362323344

                # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867199506416
                __default_139867199506416 = _DEFAULT_MARKER

                # <Value 'provider:plone.contentmenu' (17:32)> -> __cache_139867199507568
                __token = 460
                try:
                    __zt_tmp = __attrs_139867199507328
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_139867199507568 = _static_139867356405696('provider', 'plone.contentmenu', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))

                # <BinOp left=<Value 'provider:plone.contentmenu' (17:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f3568756860> at 7f355ebe0dc0> -> __condition
                __expression = __cache_139867199507568

                # <Symbol value=<DEFAULT> at 7f3568756860> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div></div>')
                else:
                    __content = __cache_139867199507568
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n  \n\n  ')

                # <Static value=<ast.Dict object at 0x7f355ebe0a30> name=None at 7f355ebe0b50> -> __attrs_139867199504688
                __attrs_139867199504688 = _static_139867199506992

                # <li ... (0:0)
                # --------------------------------------------------------
                __append('<li class="border-top my-2"></li>\n\n  ')

                # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867199505840
                __attrs_139867199505840 = _static_139867362323344
                __backup_actions_139867202231152 = get('actions', __marker)

                # <Value 'view/tabSet2' (23:23)> -> __value
                __token = 600
                try:
                    __zt_tmp = __attrs_139867199505840
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139867356405696('path', 'view/tabSet2', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                econtext['actions'] = __value
                __append('\n    ')

                # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867199508480
                __attrs_139867199508480 = _static_139867362323344

                # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867199508384
                __default_139867199508384 = _DEFAULT_MARKER

                # <Value 'python: view.menu_template(actions=actions)' (25:32)> -> __cache_139867199515680
                __token = 662
                try:
                    __zt_tmp = __attrs_139867199508480
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_139867199515680 = _static_139867356405696('python', ' view.menu_template(actions=actions)', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))

                # <BinOp left=<Value 'python: view.menu_template(actions=actions)' (25:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f3568756860> at 7f355ebe1150> -> __condition
                __expression = __cache_139867199515680

                # <Symbol value=<DEFAULT> at 7f3568756860> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div></div>')
                else:
                    __content = __cache_139867199515680
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n  ')
                if (__backup_actions_139867202231152 is __marker):
                    del econtext['actions']
                else:
                    econtext['actions'] = __backup_actions_139867202231152
                __append('\n\n')
                __i18n_domain = __previous_i18n_domain_139867199516640
            if (__backup_ploneview_139867202227312 is __marker):
                del econtext['ploneview']
            else:
                econtext['ploneview'] = __backup_ploneview_139867202227312
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }