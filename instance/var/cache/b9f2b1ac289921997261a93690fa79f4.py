# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/Products/CMFPlone/browser/login/templates/mail_password_response.pt'

__tokens = {261: ('context/@@main_template/macros/master', 6, 23), 261: ('context/@@main_template/macros/master', 6, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from collections import deque as _deque
from sys import exc_info as _exc_info

_static_139764333427296 = __C2ZContextWrapper
_static_139764333427584 = __compile_zt_expr
_static_139764233264656 = {'class': 'documentDescription', }
_static_139764233273152 = {'class': 'documentFirstHeading', }
_static_139764233385392 = 'master'
_static_139764333416256 = {}

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

            # <Static value=<ast.Dict object at 0x7f1d6b720f40> name=None at 7f1d6b721270> -> __attrs_139764233271136
            __attrs_139764233271136 = _static_139764333416256
            __append('\n\n\n')
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

            # <Static value=<ast.Dict object at 0x7f1d6b720f40> name=None at 7f1d6b721270> -> __attrs_139764233384336
            __attrs_139764233384336 = _static_139764333416256
            __previous_i18n_domain_139764233371856 = __i18n_domain
            __i18n_domain = 'plone'
            __backup_macroname_139764231924032 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f1d657bb5b0> name=None at 7f1d657b9960> -> __value
            __value = _static_139764233385392
            econtext['macroname'] = __value

            def __fill_content_title(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7f1d6b720f40> name=None at 7f1d6b721270> -> __attrs_139764233267968
                __attrs_139764233267968 = _static_139764333416256
                __append('\n    ')

                # <Static value=<ast.Dict object at 0x7f1d6579ff40> name=None at 7f1d6579cd60> -> __attrs_139764233269408
                __attrs_139764233269408 = _static_139764233273152

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append('<h1 class="documentFirstHeading">')
                __stream_139764233265424 = []
                __append_139764233265424 = __stream_139764233265424.append
                __append_139764233265424('Password reset confirmation sent')
                __msgid_139764233265424 = __re_whitespace(''.join(__stream_139764233265424)).strip()
                if 'heading_sent_password':
                    __append(translate('heading_sent_password', mapping=None, default=__msgid_139764233265424, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</h1>\n')
            _slots = econtext['__slot_content_title'] = _deque((__fill_content_title, ))

            def __fill_content_description(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7f1d6b720f40> name=None at 7f1d6b721270> -> __attrs_139764233257792
                __attrs_139764233257792 = _static_139764333416256
                __append('\n    ')

                # <Static value=<ast.Dict object at 0x7f1d6579de10> name=None at 7f1d6579db70> -> __attrs_139764233263360
                __attrs_139764233263360 = _static_139764233264656

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="documentDescription">')
                __stream_139764233257360 = []
                __append_139764233257360 = __stream_139764233257360.append
                __append_139764233257360('\n        Your password reset request has been mailed. It should arrive in your\n        mailbox shortly. When you receive the message, visit the address it\n        contains to reset your password.\n    ')
                __msgid_139764233257360 = __re_whitespace(''.join(__stream_139764233257360)).strip()
                if 'description_sent_password':
                    __append(translate('description_sent_password', mapping=None, default=__msgid_139764233257360, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</div>\n')
            _slots = econtext['__slot_content_description'] = _deque((__fill_content_description, ))

            def __fill_content_core(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7f1d6b720f40> name=None at 7f1d6b721270> -> __attrs_139764233270560
                __attrs_139764233270560 = _static_139764333416256
                __append('\n')
                __token = None
                render_content_core(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append('\n')
            _slots = econtext['__slot_content_core'] = _deque((__fill_content_core, ))

            # <Value 'context/@@main_template/macros/master' (6:23)> -> __macro
            __token = 261
            try:
                __zt_tmp = __attrs_139764233384336
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_139764333427584('path', 'context/@@main_template/macros/master', econtext=econtext)(_static_139764333427296(econtext, __zt_tmp))
            __token = 261
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139764231924032 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139764231924032
            __i18n_domain = __previous_i18n_domain_139764233371856
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_content_core': render_content_core, 'render': render, }