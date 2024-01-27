# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/plone/app/dexterity/browser/tabbed_forms.pt'

__tokens = {432: ('context/global_statusmessage/macros/portal_message', 13, 30), 432: ('context/global_statusmessage/macros/portal_message', 13, 30), 594: ('context/Title', 17, 65), 647: ('python:context.__name__', 18, 35), 777: ('view/tabs', 22, 30), 997: (" python: 'nav-link ' + ('active' if tab[0] == view.label else ''", 28, 22), 929: ("python:context.absolute_url() + '/' + tab[1]", 27, 22), 860: ('python:tab[0]', 25, 28), 1217: ('view/contents|view/render', 35, 42), 231: ('here/prefs_main_template/macros/master', 5, 23), 231: ('here/prefs_main_template/macros/master', 5, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from collections import deque as _deque
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140097252388304 = {'id': 'content-core', }
_static_140097252388976 = {'class': 'nav-link', 'href': "python:context.absolute_url() + '/' + tab[1]", }
_static_140097252389264 = {'class': 'nav-item', }
_static_140097252383456 = {'class': 'nav nav-tabs', }
_static_140097248371008 = {'class': 'documentFirstHeading', }
_static_140097413192176 = __C2ZContextWrapper
_static_140097413192464 = __compile_zt_expr
_static_140097248366640 = 'portal_message'
_static_140097248373744 = {'class': 'mb-4', }
_static_140097248377104 = 'master'
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

            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097248369568
            __attrs_140097248369568 = _static_140097412968080
            __previous_i18n_domain_140097248364336 = __i18n_domain
            __i18n_domain = 'plone.z3cform'
            __backup_macroname_140097252364416 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f6aeeb93910> name=None at 7f6aeeb917e0> -> __value
            __value = _static_140097248377104
            econtext['macroname'] = __value

            def __fill_prefs_configlet_main(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097248362608
                __attrs_140097248362608 = _static_140097412968080
                __append('\n\n      ')

                # <Static value=<ast.Dict object at 0x7f6aeeb92bf0> name=None at 7f6aeeb92b90> -> __attrs_140097248376912
                __attrs_140097248376912 = _static_140097248373744

                # <header ... (0:0)
                # --------------------------------------------------------
                __append('<header class="mb-4">\n\n        ')

                # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097248375088
                __attrs_140097248375088 = _static_140097412968080
                __backup_macroname_140097247511936 = get('macroname', __marker)

                # <Static value=<ast.Constant object at 0x7f6aeeb91030> name=None at 7f6aeeb91930> -> __value
                __value = _static_140097248366640
                econtext['macroname'] = __value

                # <Value 'context/global_statusmessage/macros/portal_message' (13:30)> -> __macro
                __token = 432
                try:
                    __zt_tmp = __attrs_140097248375088
                except get('NameError', NameError):
                    __zt_tmp = None

                __macro = _static_140097413192464('path', 'context/global_statusmessage/macros/portal_message', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                __token = 432
                __m = __macro.include
                __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                if (__backup_macroname_140097247511936 is __marker):
                    del econtext['macroname']
                else:
                    econtext['macroname'] = __backup_macroname_140097247511936
                __append('\n\n        ')

                # <Static value=<ast.Dict object at 0x7f6aeeb92140> name=None at 7f6aeeb91b40> -> __attrs_140097248364624
                __attrs_140097248364624 = _static_140097248371008

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append('<h1 class="documentFirstHeading">')

                # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097252383600
                __attrs_140097252383600 = _static_140097412968080

                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252385328
                __default_140097252385328 = _DEFAULT_MARKER

                # <Value 'context/Title' (17:65)> -> __cache_140097252377888
                __token = 594
                try:
                    __zt_tmp = __attrs_140097252383600
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140097252377888 = _static_140097413192464('path', 'context/Title', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                # <BinOp left=<Value 'context/Title' (17:65)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeef656c0> -> __condition
                __expression = __cache_140097252377888

                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140097252377888
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('\n          (')

                # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097252382640
                __attrs_140097252382640 = _static_140097412968080

                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252387392
                __default_140097252387392 = _DEFAULT_MARKER

                # <Value 'python:context.__name__' (18:35)> -> __cache_140097252386576
                __token = 647
                try:
                    __zt_tmp = __attrs_140097252382640
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140097252386576 = _static_140097413192464('python', 'context.__name__', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                # <BinOp left=<Value 'python:context.__name__' (18:35)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeef673a0> -> __condition
                __expression = __cache_140097252386576

                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140097252386576
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append(')</h1>\n\n        ')

                # <Static value=<ast.Dict object at 0x7f6aeef65ae0> name=None at 7f6aeef66e30> -> __attrs_140097252386624
                __attrs_140097252386624 = _static_140097252383456

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append('<ul class="nav nav-tabs">\n          ')

                # <Static value=<ast.Dict object at 0x7f6aeef67190> name=None at 7f6aeef65510> -> __attrs_140097252377024
                __attrs_140097252377024 = _static_140097252389264
                __backup_tab_140097252215440 = get('tab', __marker)

                # <Value 'view/tabs' (22:30)> -> __iterator
                __token = 777
                try:
                    __zt_tmp = __attrs_140097252377024
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140097413192464('path', 'view/tabs', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                (__iterator, ____index_140097252383072, ) = getname('repeat')('tab', __iterator)
                econtext['tab'] = None
                for __item in __iterator:
                    econtext['tab'] = __item

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append('<li class="nav-item" >\n            ')

                    # <Static value=<ast.Dict object at 0x7f6aeef67070> name=None at 7f6aeef641f0> -> __attrs_140097252391712
                    __attrs_140097252391712 = _static_140097252388976

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252382736
                    __default_140097252382736 = _DEFAULT_MARKER

                    # <Substitution "python: 'nav-link ' + ('active' if tab[0] == view.label else '')" (28:22)> -> __attr_class
                    __token = 997
                    try:
                        __zt_tmp = __attrs_140097252391712
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_140097413192464('python', " 'nav-link ' + ('active' if tab[0] == view.label else '')", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', 'nav-link', _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((' class="%s"' % __attr_class))

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252392192
                    __default_140097252392192 = _DEFAULT_MARKER

                    # <Substitution "python:context.absolute_url() + '/' + tab[1]" (27:22)> -> __attr_href
                    __token = 929
                    try:
                        __zt_tmp = __attrs_140097252391712
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140097413192464('python', "context.absolute_url() + '/' + tab[1]", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))
                    __append(' >')

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252391856
                    __default_140097252391856 = _DEFAULT_MARKER

                    # <Value 'python:tab[0]' (25:28)> -> __cache_140097252385808
                    __token = 860
                    try:
                        __zt_tmp = __attrs_140097252391712
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140097252385808 = _static_140097413192464('python', 'tab[0]', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                    # <BinOp left=<Value 'python:tab[0]' (25:28)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeef66620> -> __condition
                    __expression = __cache_140097252385808

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140097252385808
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</a>\n          </li>')
                    ____index_140097252383072 -= 1
                    if (____index_140097252383072 > 0):
                        __append('\n          ')
                if (__backup_tab_140097252215440 is __marker):
                    del econtext['tab']
                else:
                    econtext['tab'] = __backup_tab_140097252215440
                __append('\n        </ul>\n      </header>\n      ')

                # <Static value=<ast.Dict object at 0x7f6aeef66dd0> name=None at 7f6aeef65f60> -> __attrs_140097252380576
                __attrs_140097252380576 = _static_140097252388304

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div id="content-core">\n        ')

                # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097252385760
                __attrs_140097252385760 = _static_140097412968080

                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252380720
                __default_140097252380720 = _DEFAULT_MARKER

                # <Value 'view/contents|view/render' (35:42)> -> __cache_140097252378608
                __token = 1217
                try:
                    __zt_tmp = __attrs_140097252385760
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140097252378608 = _static_140097413192464('path', 'view/contents|view/render', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                # <BinOp left=<Value 'view/contents|view/render' (35:42)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeef66ad0> -> __condition
                __expression = __cache_140097252378608

                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140097252378608
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n      </div>\n\n    ')
            _slots = econtext['__slot_prefs_configlet_main'] = _deque((__fill_prefs_configlet_main, ))

            # <Value 'here/prefs_main_template/macros/master' (5:23)> -> __macro
            __token = 231
            try:
                __zt_tmp = __attrs_140097248369568
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140097413192464('path', 'here/prefs_main_template/macros/master', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __token = 231
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140097252364416 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140097252364416
            __i18n_domain = __previous_i18n_domain_140097248364336
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }