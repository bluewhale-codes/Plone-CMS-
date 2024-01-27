# -*- coding: utf-8 -*-
__filename = 'login_form'

__tokens = {166: ('string:${here/absolute_url}/login', 11, 33), 291: ('request/came_from | string:', 14, 35)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139867308865280 = {'type': 'submit', 'value': ' Log In ', }
_static_139867308855728 = {'colspan': '2', }
_static_139867308854720 = {'type': 'password', 'name': '__ac_password', 'size': '30', }
_static_139867308863456 = {'type': 'text', 'name': '__ac_name', 'size': '30', }
_static_139867308417584 = {'cellpadding': '2', }
_static_139867308422432 = {'type': 'hidden', 'name': 'came_from', 'value': '', }
_static_139867356405408 = __C2ZContextWrapper
_static_139867356405696 = __compile_zt_expr
_static_139867308416048 = {'method': 'post', 'action': '', }
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

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867308605104
            __attrs_139867308605104 = _static_139867362323344

            # <html ... (0:0)
            # --------------------------------------------------------
            __append('<html>\n  ')

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867308420848
            __attrs_139867308420848 = _static_139867362323344

            # <head ... (0:0)
            # --------------------------------------------------------
            __append('<head>\n    ')

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867308420320
            __attrs_139867308420320 = _static_139867362323344

            # <title ... (0:0)
            # --------------------------------------------------------
            __append('<title> Login Form </title>\n  </head>\n\n  ')

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867308420368
            __attrs_139867308420368 = _static_139867362323344

            # <body ... (0:0)
            # --------------------------------------------------------
            __append('<body>\n\n    ')

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867308417200
            __attrs_139867308417200 = _static_139867362323344

            # <h3 ... (0:0)
            # --------------------------------------------------------
            __append('<h3> Please log in </h3>\n\n    ')

            # <Static value=<ast.Dict object at 0x7f35653bdc30> name=None at 7f35653bdf00> -> __attrs_139867308419120
            __attrs_139867308419120 = _static_139867308416048

            # <form ... (0:0)
            # --------------------------------------------------------
            __append('<form method="post"')

            # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867308415136
            __default_139867308415136 = _DEFAULT_MARKER

            # <Substitution 'string:${here/absolute_url}/login' (11:33)> -> __attr_action
            __token = 166
            try:
                __zt_tmp = __attrs_139867308419120
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_action = _static_139867356405696('string', '${here/absolute_url}/login', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            __attr_action = __quote(__attr_action, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_action is not None):
                __append((' action="%s"' % __attr_action))
            __append('>\n\n      ')

            # <Static value=<ast.Dict object at 0x7f35653bf520> name=None at 7f35653bfca0> -> __attrs_139867308417296
            __attrs_139867308417296 = _static_139867308422432

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input type="hidden" name="came_from"')

            # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867308409088
            __default_139867308409088 = _DEFAULT_MARKER

            # <Substitution 'request/came_from | string:' (14:35)> -> __attr_value
            __token = 291
            try:
                __zt_tmp = __attrs_139867308417296
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_value = _static_139867356405696('path', 'request/came_from | string:', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            __attr_value = __quote(__attr_value, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_value is not None):
                __append((' value="%s"' % __attr_value))
            __append('/>\n      ')

            # <Static value=<ast.Dict object at 0x7f35653be230> name=None at 7f35653bf0a0> -> __attrs_139867308415808
            __attrs_139867308415808 = _static_139867308417584

            # <table ... (0:0)
            # --------------------------------------------------------
            __append('<table cellpadding="2">\n        ')

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867308423248
            __attrs_139867308423248 = _static_139867362323344

            # <tr ... (0:0)
            # --------------------------------------------------------
            __append('<tr>\n          ')

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867308420176
            __attrs_139867308420176 = _static_139867362323344

            # <td ... (0:0)
            # --------------------------------------------------------
            __append('<td>')

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867308415760
            __attrs_139867308415760 = _static_139867362323344

            # <b ... (0:0)
            # --------------------------------------------------------
            __append('<b>Login:</b> </td>\n          ')

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867308867536
            __attrs_139867308867536 = _static_139867362323344

            # <td ... (0:0)
            # --------------------------------------------------------
            __append('<td>')

            # <Static value=<ast.Dict object at 0x7f356542afe0> name=None at 7f356542ab30> -> __attrs_139867308867248
            __attrs_139867308867248 = _static_139867308863456

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input type="text" name="__ac_name" size="30" /></td>\n        </tr>\n        ')

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867308862496
            __attrs_139867308862496 = _static_139867362323344

            # <tr ... (0:0)
            # --------------------------------------------------------
            __append('<tr>\n          ')

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867308861776
            __attrs_139867308861776 = _static_139867362323344

            # <td ... (0:0)
            # --------------------------------------------------------
            __append('<td>')

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867308864704
            __attrs_139867308864704 = _static_139867362323344

            # <b ... (0:0)
            # --------------------------------------------------------
            __append('<b>Password:</b></td>\n          ')

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867308863696
            __attrs_139867308863696 = _static_139867362323344

            # <td ... (0:0)
            # --------------------------------------------------------
            __append('<td>')

            # <Static value=<ast.Dict object at 0x7f3565428dc0> name=None at 7f356542add0> -> __attrs_139867308852512
            __attrs_139867308852512 = _static_139867308854720

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input type="password" name="__ac_password" size="30" /></td>\n        </tr>\n        ')

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867308858512
            __attrs_139867308858512 = _static_139867362323344

            # <tr ... (0:0)
            # --------------------------------------------------------
            __append('<tr>\n          ')

            # <Static value=<ast.Dict object at 0x7f35654291b0> name=None at 7f35654299c0> -> __attrs_139867308860048
            __attrs_139867308860048 = _static_139867308855728

            # <td ... (0:0)
            # --------------------------------------------------------
            __append('<td colspan="2">\n            ')

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867308865664
            __attrs_139867308865664 = _static_139867362323344

            # <br ... (0:0)
            # --------------------------------------------------------
            __append('<br />\n            ')

            # <Static value=<ast.Dict object at 0x7f356542b700> name=None at 7f3565429750> -> __attrs_139867308858416
            __attrs_139867308858416 = _static_139867308865280

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input type="submit" value=" Log In " />\n          </td>\n        </tr>\n      </table>\n\n    </form>\n\n  </body>\n\n</html>')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }