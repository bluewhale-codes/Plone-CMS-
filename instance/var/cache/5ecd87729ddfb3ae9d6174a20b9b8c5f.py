# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/plone/app/z3cform/templates/radio_input.pt'

__tokens = {170: ('view/items', 6, 24), 256: ("python:view.renderForValue(item['value'])", 9, 34), 423: ('item/id', 14, 17), 366: ('item/label', 12, 24), 592: ('string:${view/name}-empty-marker', 22, 16)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139906200866480 = {'name': 'field-empty-marker', 'type': 'hidden', 'value': '1', }
_static_139906200864944 = {'class': 'form-check-label', 'for': 'item/id', }
_static_139906200845424 = {'class': 'form-check-input', }
_static_139906490555248 = __C2ZContextWrapper
_static_139906490555536 = __compile_zt_expr
_static_139906200843840 = {'class': 'form-check', }
_static_139906200842592 = {'xmlns': 'http://www.w3.org/1999/xhtml', }

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

            # <Static value=<ast.Dict object at 0x7f3e73673160> name=None at 7f3e73672fb0> -> __attrs_139906200842832
            __attrs_139906200842832 = _static_139906200842592
            __append('\n  ')

            # <Static value=<ast.Dict object at 0x7f3e73673640> name=None at 7f3e73673670> -> __attrs_139906200844224
            __attrs_139906200844224 = _static_139906200843840
            __backup_item_139906200842112 = get('item', __marker)

            # <Value 'view/items' (6:24)> -> __iterator
            __token = 170
            try:
                __zt_tmp = __attrs_139906200844224
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_139906490555536('path', 'view/items', econtext=econtext)(_static_139906490555248(econtext, __zt_tmp))
            (__iterator, ____index_139906200844560, ) = getname('repeat')('item', __iterator)
            econtext['item'] = None
            for __item in __iterator:
                econtext['item'] = __item

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="form-check" >\n    ')

                # <Static value=<ast.Dict object at 0x7f3e73673c70> name=None at 7f3e73673ca0> -> __attrs_139906200862928
                __attrs_139906200862928 = _static_139906200845424

                # <Symbol value=<DEFAULT> at 7f3e84a07cd0> -> __default_139906200846288
                __default_139906200846288 = _DEFAULT_MARKER

                # <Value "python:view.renderForValue(item['value'])" (9:34)> -> __cache_139906200845760
                __token = 256
                try:
                    __zt_tmp = __attrs_139906200862928
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_139906200845760 = _static_139906490555536('python', "view.renderForValue(item['value'])", econtext=econtext)(_static_139906490555248(econtext, __zt_tmp))

                # <BinOp left=<Value "python:view.renderForValue(item['value'])" (9:34)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f3e84a07cd0> at 7f3e73673eb0> -> __condition
                __expression = __cache_139906200845760

                # <Symbol value=<DEFAULT> at 7f3e84a07cd0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input class="form-check-input" />')
                else:
                    __content = __cache_139906200845760
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n    ')

                # <Static value=<ast.Dict object at 0x7f3e736788b0> name=None at 7f3e73678520> -> __attrs_139906200865184
                __attrs_139906200865184 = _static_139906200864944

                # <label ... (0:0)
                # --------------------------------------------------------
                __append('<label class="form-check-label"')

                # <Symbol value=<DEFAULT> at 7f3e84a07cd0> -> __default_139906200864416
                __default_139906200864416 = _DEFAULT_MARKER

                # <Substitution 'item/id' (14:17)> -> __attr_for
                __token = 423
                try:
                    __zt_tmp = __attrs_139906200865184
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_for = _static_139906490555536('path', 'item/id', econtext=econtext)(_static_139906490555248(econtext, __zt_tmp))
                __attr_for = __quote(__attr_for, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_for is not None):
                    __append((' for="%s"' % __attr_for))
                __append(' >')

                # <Symbol value=<DEFAULT> at 7f3e84a07cd0> -> __default_139906200863840
                __default_139906200863840 = _DEFAULT_MARKER

                # <Value 'item/label' (12:24)> -> __cache_139906200863360
                __token = 366
                try:
                    __zt_tmp = __attrs_139906200865184
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_139906200863360 = _static_139906490555536('path', 'item/label', econtext=econtext)(_static_139906490555248(econtext, __zt_tmp))

                # <BinOp left=<Value 'item/label' (12:24)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f3e84a07cd0> at 7f3e73678340> -> __condition
                __expression = __cache_139906200863360

                # <Symbol value=<DEFAULT> at 7f3e84a07cd0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('Label')
                else:
                    __content = __cache_139906200863360
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</label>\n  </div>')
                ____index_139906200844560 -= 1
                if (____index_139906200844560 > 0):
                    __append('\n  ')
            if (__backup_item_139906200842112 is __marker):
                del econtext['item']
            else:
                econtext['item'] = __backup_item_139906200842112
            __append('\n  ')

            # <Static value=<ast.Dict object at 0x7f3e73678eb0> name=None at 7f3e73678ee0> -> __attrs_139906200867056
            __attrs_139906200867056 = _static_139906200866480

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input')

            # <Symbol value=<DEFAULT> at 7f3e84a07cd0> -> __default_139906200866000
            __default_139906200866000 = _DEFAULT_MARKER

            # <Substitution 'string:${view/name}-empty-marker' (22:16)> -> __attr_name
            __token = 592
            try:
                __zt_tmp = __attrs_139906200867056
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_name = _static_139906490555536('string', '${view/name}-empty-marker', econtext=econtext)(_static_139906490555248(econtext, __zt_tmp))
            __attr_name = __quote(__attr_name, '"', '&quot;', 'field-empty-marker', _DEFAULT_MARKER)
            if (__attr_name is not None):
                __append((' name="%s"' % __attr_name))
            __append(' type="hidden" value="1" />\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }