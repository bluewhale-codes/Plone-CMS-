# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/Products/CMFPlone/browser/login/templates/login.pt'

__tokens = {569: ('view/label | nothing', 18, 29), 1091: ('context/@@ploneform-macros/titlelessform', 31, 37), 1091: ('context/@@ploneform-macros/titlelessform', 31, 37), 1219: ('context/@@plone_portal_state', 34, 43), 1289: (' portal_state/portal_ur', 35, 40), 1503: ('string:${portal_url}/@@login-help', 38, 62), 1655: ('python:view.self_registration_enabled()', 40, 36), 1854: ('string:${portal_url}/@@register', 42, 60), 287: ('here/main_template/macros/master', 7, 23), 287: ('here/main_template/macros/master', 7, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from collections import deque as _deque
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140080037459328 = 'master'
_static_140080037695872 = {'href': '@@register', 'class': 'emph', }
_static_140080037691984 = {'href': '@@login-help', }
_static_140080037688320 = {'class': 'footer mt-4', }
_static_140080037686736 = 'titlelessform'
_static_140080037684720 = {'class': 'alert alert-danger pat-cookietrigger', 'style': 'display:none', }
_static_140080037682896 = {'id': 'login-form', }
_static_140080122692944 = __C2ZContextWrapper
_static_140080122693232 = __compile_zt_expr
_static_140080037681744 = {'class': 'card-title h5', }
_static_140080037679680 = {'class': 'card-body', }
_static_140080037678288 = {'class': 'card', }
_static_140080037676896 = {'class': 'login-wrapper', }
_static_140080122452464 = {}

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

            # <Static value=<ast.Dict object at 0x7f66f1f059f0> name=None at 7f66f1f05d20> -> __attrs_140080037675792
            __attrs_140080037675792 = _static_140080122452464
            __append('\n\n      ')

            # <Static value=<ast.Dict object at 0x7f66ece2c760> name=None at 7f66ece2c790> -> __attrs_140080037677280
            __attrs_140080037677280 = _static_140080037676896

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="login-wrapper">\n\n        ')

            # <Static value=<ast.Dict object at 0x7f66ece2ccd0> name=None at 7f66ece2cd00> -> __attrs_140080037678672
            __attrs_140080037678672 = _static_140080037678288

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="card">\n          ')

            # <Static value=<ast.Dict object at 0x7f66ece2d240> name=None at 7f66ece2d270> -> __attrs_140080037680064
            __attrs_140080037680064 = _static_140080037679680

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="card-body">\n            ')

            # <Static value=<ast.Dict object at 0x7f66ece2da50> name=None at 7f66ece2da80> -> __attrs_140080037682128
            __attrs_140080037682128 = _static_140080037681744

            # <h1 ... (0:0)
            # --------------------------------------------------------
            __append('<h1 class="card-title h5">')

            # <Symbol value=<DEFAULT> at 7f66f1ea2740> -> __default_140080037681168
            __default_140080037681168 = _DEFAULT_MARKER

            # <Value 'view/label | nothing' (18:29)> -> __cache_140080037680688
            __token = 569
            try:
                __zt_tmp = __attrs_140080037682128
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140080037680688 = _static_140080122693232('path', 'view/label | nothing', econtext=econtext)(_static_140080122692944(econtext, __zt_tmp))

            # <BinOp left=<Value 'view/label | nothing' (18:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f66f1ea2740> at 7f66ece2d6f0> -> __condition
            __expression = __cache_140080037680688

            # <Symbol value=<DEFAULT> at 7f66f1ea2740> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140080037680688
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append('</h1>\n\n            ')

            # <Static value=<ast.Dict object at 0x7f66ece2ded0> name=None at 7f66ece2df00> -> __attrs_140080037683280
            __attrs_140080037683280 = _static_140080037682896

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div id="login-form">\n\n              ')

            # <Static value=<ast.Dict object at 0x7f66ece2e5f0> name=None at 7f66ece2e620> -> __attrs_140080037684912
            __attrs_140080037684912 = _static_140080037684720

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="alert alert-danger pat-cookietrigger" style="display:none">\n                ')

            # <Static value=<ast.Dict object at 0x7f66f1f059f0> name=None at 7f66f1f05d20> -> __attrs_140080037686016
            __attrs_140080037686016 = _static_140080122452464

            # <strong ... (0:0)
            # --------------------------------------------------------
            __append('<strong>')
            __stream_140080037685536 = []
            __append_140080037685536 = __stream_140080037685536.append
            __append_140080037685536('\n                  Error\n                ')
            __msgid_140080037685536 = __re_whitespace(''.join(__stream_140080037685536)).strip()
            if __msgid_140080037685536:
                __append(translate(__msgid_140080037685536, mapping=None, default=__msgid_140080037685536, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</strong>\n                ')

            # <Static value=<ast.Dict object at 0x7f66f1f059f0> name=None at 7f66f1f05d20> -> __attrs_140080037686976
            __attrs_140080037686976 = _static_140080122452464
            __stream_140080037686592 = []
            __append_140080037686592 = __stream_140080037686592.append
            __append_140080037686592('\n                  Cookies are not enabled. You must enable cookies before you can log in.\n                ')
            __msgid_140080037686592 = __re_whitespace(''.join(__stream_140080037686592)).strip()
            if 'enable_cookies_message_before_login':
                __append(translate('enable_cookies_message_before_login', mapping=None, default=__msgid_140080037686592, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('\n              </div>\n              ')

            # <Static value=<ast.Dict object at 0x7f66f1f059f0> name=None at 7f66f1f05d20> -> __attrs_140080037687552
            __attrs_140080037687552 = _static_140080122452464
            __backup_macroname_140080119073152 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f66ece2edd0> name=None at 7f66ece2ef20> -> __value
            __value = _static_140080037686736
            econtext['macroname'] = __value

            # <Value 'context/@@ploneform-macros/titlelessform' (31:37)> -> __macro
            __token = 1091
            try:
                __zt_tmp = __attrs_140080037687552
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140080122693232('path', 'context/@@ploneform-macros/titlelessform', econtext=econtext)(_static_140080122692944(econtext, __zt_tmp))
            __token = 1091
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140080119073152 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140080119073152
            __append('\n\n              ')

            # <Static value=<ast.Dict object at 0x7f66ece2f400> name=None at 7f66ece2f430> -> __attrs_140080037688704
            __attrs_140080037688704 = _static_140080037688320
            __backup_portal_state_140080037679008 = get('portal_state', __marker)

            # <Value 'context/@@plone_portal_state' (34:43)> -> __value
            __token = 1219
            try:
                __zt_tmp = __attrs_140080037688704
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140080122693232('path', 'context/@@plone_portal_state', econtext=econtext)(_static_140080122692944(econtext, __zt_tmp))
            econtext['portal_state'] = __value
            __backup_portal_url_140080037680400 = get('portal_url', __marker)

            # <Value 'portal_state/portal_url' (35:40)> -> __value
            __token = 1289
            try:
                __zt_tmp = __attrs_140080037688704
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140080122693232('path', 'portal_state/portal_url', econtext=econtext)(_static_140080122692944(econtext, __zt_tmp))
            econtext['portal_url'] = __value

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="footer mt-4">\n                ')

            # <Static value=<ast.Dict object at 0x7f66f1f059f0> name=None at 7f66f1f05d20> -> __attrs_140080037690096
            __attrs_140080037690096 = _static_140080122452464

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div>\n                  ')

            # <Static value=<ast.Dict object at 0x7f66f1f059f0> name=None at 7f66f1f05d20> -> __attrs_140080037691104
            __attrs_140080037691104 = _static_140080122452464
            __stream_140080037690720 = []
            __append_140080037690720 = __stream_140080037690720.append
            __append_140080037690720('Trouble logging in?')
            __msgid_140080037690720 = __re_whitespace(''.join(__stream_140080037690720)).strip()
            if 'trouble_logging_in':
                __append(translate('trouble_logging_in', mapping=None, default=__msgid_140080037690720, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('\n                  ')

            # <Static value=<ast.Dict object at 0x7f66ece30250> name=None at 7f66ece30280> -> __attrs_140080037692608
            __attrs_140080037692608 = _static_140080037691984

            # <a ... (0:0)
            # --------------------------------------------------------
            __append('<a')

            # <Symbol value=<DEFAULT> at 7f66f1ea2740> -> __default_140080037692080
            __default_140080037692080 = _DEFAULT_MARKER

            # <Substitution 'string:${portal_url}/@@login-help' (38:62)> -> __attr_href
            __token = 1503
            try:
                __zt_tmp = __attrs_140080037692608
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_140080122693232('string', '${portal_url}/@@login-help', econtext=econtext)(_static_140080122692944(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', '@@login-help', _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((' href="%s"' % __attr_href))
            __append('>')
            __stream_140080037690864 = []
            __append_140080037690864 = __stream_140080037690864.append
            __append_140080037690864('Get help')
            __msgid_140080037690864 = __re_whitespace(''.join(__stream_140080037690864)).strip()
            if 'footer_login_link_get_help':
                __append(translate('footer_login_link_get_help', mapping=None, default=__msgid_140080037690864, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</a>.\n                </div>\n                ')

            # <Static value=<ast.Dict object at 0x7f66f1f059f0> name=None at 7f66f1f05d20> -> __attrs_140080037693376
            __attrs_140080037693376 = _static_140080122452464

            # <Value 'python:view.self_registration_enabled()' (40:36)> -> __condition
            __token = 1655
            try:
                __zt_tmp = __attrs_140080037693376
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140080122693232('python', 'view.self_registration_enabled()', econtext=econtext)(_static_140080122692944(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div>\n                  ')

                # <Static value=<ast.Dict object at 0x7f66f1f059f0> name=None at 7f66f1f05d20> -> __attrs_140080037694528
                __attrs_140080037694528 = _static_140080122452464
                __stream_140080037694144 = []
                __append_140080037694144 = __stream_140080037694144.append
                __append_140080037694144('Need an account?')
                __msgid_140080037694144 = __re_whitespace(''.join(__stream_140080037694144)).strip()
                if 'need_an_account':
                    __append(translate('need_an_account', mapping=None, default=__msgid_140080037694144, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('\n                  ')

                # <Static value=<ast.Dict object at 0x7f66ece31180> name=None at 7f66ece30e50> -> __attrs_140080037696112
                __attrs_140080037696112 = _static_140080037695872

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a')

                # <Symbol value=<DEFAULT> at 7f66f1ea2740> -> __default_140080037695584
                __default_140080037695584 = _DEFAULT_MARKER

                # <Substitution 'string:${portal_url}/@@register' (42:60)> -> __attr_href
                __token = 1854
                try:
                    __zt_tmp = __attrs_140080037696112
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_140080122693232('string', '${portal_url}/@@register', econtext=econtext)(_static_140080122692944(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', '@@register', _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((' href="%s"' % __attr_href))
                __append(' class="emph">')
                __stream_140080037694288 = []
                __append_140080037694288 = __stream_140080037694288.append
                __append_140080037694288('Sign up here')
                __msgid_140080037694288 = __re_whitespace(''.join(__stream_140080037694288)).strip()
                if 'footer_login_link_signup':
                    __append(translate('footer_login_link_signup', mapping=None, default=__msgid_140080037694288, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</a>.\n                </div>')
            __append('\n              </div>')
            if (__backup_portal_url_140080037680400 is __marker):
                del econtext['portal_url']
            else:
                econtext['portal_url'] = __backup_portal_url_140080037680400
            if (__backup_portal_state_140080037679008 is __marker):
                del econtext['portal_state']
            else:
                econtext['portal_state'] = __backup_portal_state_140080037679008
            __append('\n\n            </div>\n\n          </div>\n        </div>\n\n      </div>\n\n    ')
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

            # <Static value=<ast.Dict object at 0x7f66f1f059f0> name=None at 7f66f1f05d20> -> __attrs_140080037459664
            __attrs_140080037459664 = _static_140080122452464
            __previous_i18n_domain_140080037459808 = __i18n_domain
            __i18n_domain = 'plone'
            __backup_macroname_140080117085184 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f66ecdf7580> name=None at 7f66ecdf75b0> -> __value
            __value = _static_140080037459328
            econtext['macroname'] = __value

            def __fill_main(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7f66f1f059f0> name=None at 7f66f1f05d20> -> __attrs_140080037461728
                __attrs_140080037461728 = _static_140080122452464
                __append('\n    ')
                __token = None
                render_main(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append('\n  ')
            _slots = econtext['__slot_main'] = _deque((__fill_main, ))

            # <Value 'here/main_template/macros/master' (7:23)> -> __macro
            __token = 287
            try:
                __zt_tmp = __attrs_140080037459664
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140080122693232('path', 'here/main_template/macros/master', econtext=econtext)(_static_140080122692944(econtext, __zt_tmp))
            __token = 287
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140080117085184 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140080117085184
            __i18n_domain = __previous_i18n_domain_140080037459808
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_main': render_main, 'render': render, }