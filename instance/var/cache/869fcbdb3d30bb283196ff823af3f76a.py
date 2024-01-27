# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/plone/app/layout/viewlets/membertools.pt'

__tokens = {78: ('here/@@plone_context_state/is_toolbar_visible', 3, 23), 138: (' view/anonymou', 4, 13), 182: ('python:not isAnon and not toolbar_visible', 6, 20), 441: ('python:view.user_actions and not view.anonymous', 16, 22), 618: ('view/homelink_url', 22, 14), 677: ('view/user_name', 25, 25), 872: ('view/user_actions', 32, 29), 933: ('string:membertools-${action/id}', 34, 15), 1122: ('action/href', 41, 18), 1154: (' action/link_target|nothin', 42, 19), 1062: ('action/title', 39, 24)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139867200368848 = {'class': 'dropdown-item', 'href': '', 'target': 'action/link_target|nothing', }
_static_139867200357136 = {'id': 'string:membertools-${action/id}', }
_static_139867200507376 = {'class': 'dropdown-menu', 'aria-labelledby': 'dropdownMenu', 'role': 'menu', }
_static_139867200511504 = {'class': 'caret', }
_static_139867362323344 = {}
_static_139867200514672 = {'class': 'dropdown-toggle', 'id': 'user-name', 'data-bs-toggle': 'dropdown', 'href': 'view/homelink_url', }
_static_139867200518608 = {'class': 'dropdown dropdown-menu-end', 'id': 'portal-membertools', }
_static_139867200515728 = {'class': 'hiddenStructure', }
_static_139867356405408 = __C2ZContextWrapper
_static_139867356405696 = __compile_zt_expr
_static_139867200513376 = {'id': 'portal-membertools-wrapper', }

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

            # <Static value=<ast.Dict object at 0x7f355ecd6560> name=None at 7f355ecd4af0> -> __attrs_139867200512560
            __attrs_139867200512560 = _static_139867200513376
            __backup_toolbar_visible_139867200097536 = get('toolbar_visible', __marker)

            # <Value 'here/@@plone_context_state/is_toolbar_visible' (3:23)> -> __value
            __token = 78
            try:
                __zt_tmp = __attrs_139867200512560
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139867356405696('path', 'here/@@plone_context_state/is_toolbar_visible', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            econtext['toolbar_visible'] = __value
            __backup_isAnon_139867202370576 = get('isAnon', __marker)

            # <Value 'view/anonymous' (4:13)> -> __value
            __token = 138
            try:
                __zt_tmp = __attrs_139867200512560
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139867356405696('path', 'view/anonymous', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            econtext['isAnon'] = __value

            # <Value 'python:not isAnon and not toolbar_visible' (6:20)> -> __condition
            __token = 182
            try:
                __zt_tmp = __attrs_139867200512560
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_139867356405696('python', 'not isAnon and not toolbar_visible', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_139867200518080 = __i18n_domain
                __i18n_domain = 'plone'

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div id="portal-membertools-wrapper" >\n\n  ')

                # <Static value=<ast.Dict object at 0x7f355ecd6e90> name=None at 7f355ecd6e30> -> __attrs_139867200517936
                __attrs_139867200517936 = _static_139867200515728

                # <p ... (0:0)
                # --------------------------------------------------------
                __append('<p class="hiddenStructure" >')
                __stream_139867200517984 = []
                __append_139867200517984 = __stream_139867200517984.append
                __append_139867200517984('Member tools')
                __msgid_139867200517984 = __re_whitespace(''.join(__stream_139867200517984)).strip()
                if 'heading_member_tools':
                    __append(translate('heading_member_tools', mapping=None, default=__msgid_139867200517984, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</p>\n\n  ')

                # <Static value=<ast.Dict object at 0x7f355ecd79d0> name=None at 7f355ecd7880> -> __attrs_139867200518656
                __attrs_139867200518656 = _static_139867200518608

                # <Value 'python:view.user_actions and not view.anonymous' (16:22)> -> __condition
                __token = 441
                try:
                    __zt_tmp = __attrs_139867200518656
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139867356405696('python', 'view.user_actions and not view.anonymous', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="dropdown dropdown-menu-end" id="portal-membertools" >\n    ')

                    # <Static value=<ast.Dict object at 0x7f355ecd6a70> name=None at 7f355ecd58a0> -> __attrs_139867200518896
                    __attrs_139867200518896 = _static_139867200514672

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a class="dropdown-toggle" id="user-name" data-bs-toggle="dropdown"')

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867200513280
                    __default_139867200513280 = _DEFAULT_MARKER

                    # <Substitution 'view/homelink_url' (22:14)> -> __attr_href
                    __token = 618
                    try:
                        __zt_tmp = __attrs_139867200518896
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_139867356405696('path', 'view/homelink_url', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))
                    __append(' >\n      ')

                    # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867200506032
                    __attrs_139867200506032 = _static_139867362323344

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867200510208
                    __default_139867200510208 = _DEFAULT_MARKER

                    # <Value 'view/user_name' (25:25)> -> __cache_139867200510688
                    __token = 677
                    try:
                        __zt_tmp = __attrs_139867200506032
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139867200510688 = _static_139867356405696('path', 'view/user_name', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))

                    # <BinOp left=<Value 'view/user_name' (25:25)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f3568756860> at 7f355ecd6bf0> -> __condition
                    __expression = __cache_139867200510688

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>John</span>')
                    else:
                        __content = __cache_139867200510688
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('\n      ')

                    # <Static value=<ast.Dict object at 0x7f355ecd5e10> name=None at 7f355ecd5e40> -> __attrs_139867200507184
                    __attrs_139867200507184 = _static_139867200511504

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span class="caret"></span>\n    </a>\n    ')

                    # <Static value=<ast.Dict object at 0x7f355ecd4df0> name=None at 7f355ecd4670> -> __attrs_139867200505408
                    __attrs_139867200505408 = _static_139867200507376

                    # <ul ... (0:0)
                    # --------------------------------------------------------
                    __append('<ul class="dropdown-menu" aria-labelledby="dropdownMenu" role="menu" >\n      ')

                    # <Static value=<ast.Dict object at 0x7f355ecb0310> name=None at 7f355ecb23b0> -> __attrs_139867200357184
                    __attrs_139867200357184 = _static_139867200357136
                    __backup_action_139867202356176 = get('action', __marker)

                    # <Value 'view/user_actions' (32:29)> -> __iterator
                    __token = 872
                    try:
                        __zt_tmp = __attrs_139867200357184
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_139867356405696('path', 'view/user_actions', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                    (__iterator, ____index_139867200360352, ) = getname('repeat')('action', __iterator)
                    econtext['action'] = None
                    for __item in __iterator:
                        econtext['action'] = __item

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li')

                        # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867200367024
                        __default_139867200367024 = _DEFAULT_MARKER

                        # <Substitution 'string:membertools-${action/id}' (34:15)> -> __attr_id
                        __token = 933
                        try:
                            __zt_tmp = __attrs_139867200357184
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_id = _static_139867356405696('string', 'membertools-${action/id}', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                        __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_id is not None):
                            __append((' id="%s"' % __attr_id))
                        __append(' >\n        ')

                        # <Static value=<ast.Dict object at 0x7f355ecb30d0> name=None at 7f355ecb30a0> -> __attrs_139867200356656
                        __attrs_139867200356656 = _static_139867200368848

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append('<a class="dropdown-item"')

                        # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867200370768
                        __default_139867200370768 = _DEFAULT_MARKER

                        # <Substitution 'action/href' (41:18)> -> __attr_href
                        __token = 1122
                        try:
                            __zt_tmp = __attrs_139867200356656
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_139867356405696('path', 'action/href', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((' href="%s"' % __attr_href))

                        # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867200372544
                        __default_139867200372544 = _DEFAULT_MARKER

                        # <Substitution 'action/link_target|nothing' (42:19)> -> __attr_target
                        __token = 1154
                        try:
                            __zt_tmp = __attrs_139867200356656
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_target = _static_139867356405696('path', 'action/link_target|nothing', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                        __attr_target = __quote(__attr_target, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_target is not None):
                            __append((' target="%s"' % __attr_target))
                        __append(' >')

                        # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867200367888
                        __default_139867200367888 = _DEFAULT_MARKER

                        # <Value 'action/title' (39:24)> -> __cache_139867200368320
                        __token = 1062
                        try:
                            __zt_tmp = __attrs_139867200356656
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_139867200368320 = _static_139867356405696('path', 'action/title', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))

                        # <BinOp left=<Value 'action/title' (39:24)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f3568756860> at 7f355ecb2b30> -> __condition
                        __expression = __cache_139867200368320

                        # <Symbol value=<DEFAULT> at 7f3568756860> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('\n                  action title\n        ')
                        else:
                            __content = __cache_139867200368320
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</a>\n      </li>')
                        ____index_139867200360352 -= 1
                        if (____index_139867200360352 > 0):
                            __append('\n      ')
                    if (__backup_action_139867202356176 is __marker):
                        del econtext['action']
                    else:
                        econtext['action'] = __backup_action_139867202356176
                    __append('\n    </ul>\n  </div>')
                __append('\n\n</div>')
                __i18n_domain = __previous_i18n_domain_139867200518080
            if (__backup_isAnon_139867202370576 is __marker):
                del econtext['isAnon']
            else:
                econtext['isAnon'] = __backup_isAnon_139867202370576
            if (__backup_toolbar_visible_139867200097536 is __marker):
                del econtext['toolbar_visible']
            else:
                econtext['toolbar_visible'] = __backup_toolbar_visible_139867200097536
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }