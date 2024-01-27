# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/plone/app/layout/viewlets/anontools.pt'

__tokens = {47: ('python:view.user_actions and view.anonymous', 2, 20), 181: ('view/user_actions', 6, 27), 296: ('action', 11, 11), 245: ('action/title', 9, 22)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139867199949840 = set([])
_static_139867199959056 = set(['readonly', 'noresize', 'checked', 'declare', 'selected', 'defer', 'multiple', 'nowrap', 'ismap', 'noshade', 'compact', 'disabled', ])
_static_139867200525056 = {'href': '', }
_static_139867200531392 = {'class': 'list-inline-item', }
_static_139867200529904 = {'class': 'list-inline', }
_static_139867356405408 = __C2ZContextWrapper
_static_139867356405696 = __compile_zt_expr
_static_139867200529616 = {'id': 'portal-anontools', }

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

            # <Static value=<ast.Dict object at 0x7f355ecda4d0> name=None at 7f355ecda380> -> __attrs_139867200521216
            __attrs_139867200521216 = _static_139867200529616

            # <Value 'python:view.user_actions and view.anonymous' (2:20)> -> __condition
            __token = 47
            try:
                __zt_tmp = __attrs_139867200521216
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_139867356405696('python', 'view.user_actions and view.anonymous', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div id="portal-anontools" >\n  ')

                # <Static value=<ast.Dict object at 0x7f355ecda5f0> name=None at 7f355ecda920> -> __attrs_139867200525728
                __attrs_139867200525728 = _static_139867200529904

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append('<ul class="list-inline">\n    ')

                # <Static value=<ast.Dict object at 0x7f355ecdabc0> name=None at 7f355ecd85e0> -> __attrs_139867200522272
                __attrs_139867200522272 = _static_139867200531392
                __backup_action_139867199165520 = get('action', __marker)

                # <Value 'view/user_actions' (6:27)> -> __iterator
                __token = 181
                try:
                    __zt_tmp = __attrs_139867200522272
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_139867356405696('path', 'view/user_actions', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                (__iterator, ____index_139867200522080, ) = getname('repeat')('action', __iterator)
                econtext['action'] = None
                for __item in __iterator:
                    econtext['action'] = __item

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append('<li class="list-inline-item" >\n      ')

                    # <Static value=<ast.Dict object at 0x7f355ecd9300> name=None at 7f355ecd9270> -> __attrs_139867200520928
                    __attrs_139867200520928 = _static_139867200525056

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Value 'action' (11:11)> -> __cache_139867200530960
                    __token = 296
                    try:
                        __zt_tmp = __attrs_139867200520928
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139867200530960 = _static_139867356405696('path', 'action', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                    if ('href' not in __chain(__cache_139867200530960)):
                        __append(' href=""')
                    __attr_139867200524816 = __cache_139867200530960
                    for (name, value, ) in __attr_139867200524816.items():
                        if (name in _static_139867199959056):
                            if not bool(value):
                                continue
                            value = name
                        if ((name not in _static_139867199949840) and (value is not None)):
                            if (name in _static_139867199959056):
                                if not bool(value):
                                    continue
                                value = name
                            __append((((((' ' + name) + '=') + '"') + __quote(value, '"', '&quot;', None, None)) + '"'))
                    __append(' >')

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867200526400
                    __default_139867200526400 = _DEFAULT_MARKER

                    # <Value 'action/title' (9:22)> -> __cache_139867200523904
                    __token = 245
                    try:
                        __zt_tmp = __attrs_139867200520928
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139867200523904 = _static_139867356405696('path', 'action/title', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))

                    # <BinOp left=<Value 'action/title' (9:22)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f3568756860> at 7f355ecd8fd0> -> __condition
                    __expression = __cache_139867200523904

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n          action title\n      ')
                    else:
                        __content = __cache_139867200523904
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</a>\n    </li>')
                    ____index_139867200522080 -= 1
                    if (____index_139867200522080 > 0):
                        __append('\n    ')
                if (__backup_action_139867199165520 is __marker):
                    del econtext['action']
                else:
                    econtext['action'] = __backup_action_139867199165520
                __append('\n  </ul>\n</div>')
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }