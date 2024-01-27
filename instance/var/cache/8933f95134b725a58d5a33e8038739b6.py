# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/plone/app/layout/viewlets/toolbar.pt'

__tokens = {94: ('view/context_state', 4, 25), 130: (" python:context.restrictedTraverse('@@iconresolver'", 5, 16), 206: ('r python: view.get_personal_bar', 6, 22), 261: ('os view/toolbar_posit', 7, 20), 322: ('context_state/is_toolbar_visible', 9, 24), 680: ("python:icons.tag('arrow-bar-left')", 25, 41), 875: ("python:icons.tag('arrow-bar-right')", 31, 41), 1033: ('view/base_render', 37, 23), 1084: ('toolbar_main', 39, 23), 1137: ('toolbar_main', 41, 33), 1295: ('personal_bar/user_actions', 46, 24), 1191: ("personaltools-wrapper nav ${python:'dropend' if toolbar_pos == 'side' else ''}", 45, 16), 1219: ("python:'dropend' if toolbar_pos == 'side' else ''", 45, 44), 1546: ('personal_bar/homelink_url', 55, 16), 1633: ("python:icons.tag('toolbar-action/personaltools', tag_class='')", 58, 41), 1763: ('personal_bar/user_name', 60, 27), 2000: ('${personal_bar/user_name}', 69, 38), 2002: ('personal_bar/user_name', 69, 40), 2076: ('personal_bar/user_actions', 71, 31), 2193: ('action', 74, 15), 2269: ("python:icons.tag(action.get('icon', 'dot'), tag_class='')", 77, 41), 2372: ('action/title', 78, 41)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139867199455776 = set([])
_static_139867199459280 = set(['readonly', 'noresize', 'checked', 'declare', 'selected', 'defer', 'multiple', 'nowrap', 'ismap', 'noshade', 'compact', 'disabled', ])
_static_139867199007248 = {'class': 'nav-link dropdown-item', }
_static_139867199007536 = {'class': 'dropdown-header', }
_static_139867199011904 = {'class': 'dropdown-menu', 'id': 'collapse-personaltools', 'aria-labelledby': 'personaltools-menulink', }
_static_139867199006192 = {'class': 'toolbar-label', }
_static_139867202255840 = {'class': 'nav-link dropdown-toggle', 'id': 'personaltools-menulink', 'aria-expanded': 'false', 'data-bs-offset': '0,0', 'data-bs-toggle': 'dropdown', 'href': 'personal_bar/homelink_url', }
_static_139867202241200 = {'class': "personaltools-wrapper nav ${python:'dropend' if toolbar_pos == 'side' else ''}", }
_static_139867202246960 = {'class': 'nav flex-column plone-toolbar-main', }
_static_139867202247200 = {'class': 'toolbar-expand', 'aria-label': 'Pin', }
_static_139867362323344 = {}
_static_139867199160768 = {'class': 'toolbar-collapse', 'aria-label': 'Unpin', }
_static_139867199161200 = {'class': 'toolbar-header nav', }
_static_139867199163504 = {'class': 'pat-toolbar', 'id': 'edit-zone', 'role': 'toolbar', 'data-bs-scroll': 'true', }
_static_139867356405408 = __C2ZContextWrapper
_static_139867356405696 = __compile_zt_expr
_static_139867199173344 = {'id': 'edit-bar', 'role': 'toolbar', }

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

            # <Static value=<ast.Dict object at 0x7f355eb8f2e0> name=None at 7f355eb8f160> -> __attrs_139867199172672
            __attrs_139867199172672 = _static_139867199173344
            __backup_context_state_139867202218704 = get('context_state', __marker)

            # <Value 'view/context_state' (4:25)> -> __value
            __token = 94
            try:
                __zt_tmp = __attrs_139867199172672
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139867356405696('path', 'view/context_state', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            econtext['context_state'] = __value
            __backup_icons_139867202216832 = get('icons', __marker)

            # <Value "python:context.restrictedTraverse('@@iconresolver')" (5:16)> -> __value
            __token = 130
            try:
                __zt_tmp = __attrs_139867199172672
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139867356405696('python', "context.restrictedTraverse('@@iconresolver')", econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            econtext['icons'] = __value
            __backup_personal_bar_139867202500640 = get('personal_bar', __marker)

            # <Value 'python: view.get_personal_bar()' (6:22)> -> __value
            __token = 206
            try:
                __zt_tmp = __attrs_139867199172672
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139867356405696('python', ' view.get_personal_bar()', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            econtext['personal_bar'] = __value
            __backup_toolbar_pos_139867202237584 = get('toolbar_pos', __marker)

            # <Value 'view/toolbar_position' (7:20)> -> __value
            __token = 261
            try:
                __zt_tmp = __attrs_139867199172672
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139867356405696('path', 'view/toolbar_position', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            econtext['toolbar_pos'] = __value

            # <Value 'context_state/is_toolbar_visible' (9:24)> -> __condition
            __token = 322
            try:
                __zt_tmp = __attrs_139867199172672
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_139867356405696('path', 'context_state/is_toolbar_visible', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_139867199161632 = __i18n_domain
                __i18n_domain = 'plone'

                # <section ... (0:0)
                # --------------------------------------------------------
                __append('<section id="edit-bar" role="toolbar" >\n\n\n  ')

                # <Static value=<ast.Dict object at 0x7f355eb8cc70> name=None at 7f355eb8d300> -> __attrs_139867199164944
                __attrs_139867199164944 = _static_139867199163504

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="pat-toolbar" id="edit-zone" role="toolbar" data-bs-scroll="true" >\n\n    ')

                # <Static value=<ast.Dict object at 0x7f355eb8c370> name=None at 7f355eb8c6d0> -> __attrs_139867199172144
                __attrs_139867199172144 = _static_139867199161200

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="toolbar-header nav">\n      ')

                # <Static value=<ast.Dict object at 0x7f355eb8c1c0> name=None at 7f355eb8c790> -> __attrs_139867199163312
                __attrs_139867199163312 = _static_139867199160768

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a class="toolbar-collapse"')

                # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867199160432
                __default_139867199160432 = _DEFAULT_MARKER

                # <Translate msgid=None node=<ast.Constant object at 0x7f355eb8d870> at 7f355eb8e530> -> __attr_aria_label
                __attr_aria_label = 'Unpin'
                __attr_aria_label = translate(__attr_aria_label, default=__attr_aria_label, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                if (__attr_aria_label is not None):
                    __append((' aria-label="%s"' % __attr_aria_label))
                __append(' >\n        ')

                # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867202248016
                __attrs_139867202248016 = _static_139867362323344

                # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867202252576
                __default_139867202252576 = _DEFAULT_MARKER

                # <Value "python:icons.tag('arrow-bar-left')" (25:41)> -> __cache_139867202254400
                __token = 680
                try:
                    __zt_tmp = __attrs_139867202248016
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_139867202254400 = _static_139867356405696('python', "icons.tag('arrow-bar-left')", econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))

                # <BinOp left=<Value "python:icons.tag('arrow-bar-left')" (25:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f3568756860> at 7f355ee7e140> -> __condition
                __expression = __cache_139867202254400

                # <Symbol value=<DEFAULT> at 7f3568756860> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_139867202254400
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n      </a>\n      ')

                # <Static value=<ast.Dict object at 0x7f355ee7da20> name=None at 7f355ee7ee60> -> __attrs_139867202253632
                __attrs_139867202253632 = _static_139867202247200

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a class="toolbar-expand"')

                # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867202255504
                __default_139867202255504 = _DEFAULT_MARKER

                # <Translate msgid=None node=<ast.Constant object at 0x7f355ee7ded0> at 7f355ee7ea70> -> __attr_aria_label
                __attr_aria_label = 'Pin'
                __attr_aria_label = translate(__attr_aria_label, default=__attr_aria_label, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                if (__attr_aria_label is not None):
                    __append((' aria-label="%s"' % __attr_aria_label))
                __append(' >\n        ')

                # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867202254064
                __attrs_139867202254064 = _static_139867362323344

                # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867202242640
                __default_139867202242640 = _DEFAULT_MARKER

                # <Value "python:icons.tag('arrow-bar-right')" (31:41)> -> __cache_139867202242736
                __token = 875
                try:
                    __zt_tmp = __attrs_139867202254064
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_139867202242736 = _static_139867356405696('python', "icons.tag('arrow-bar-right')", econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))

                # <BinOp left=<Value "python:icons.tag('arrow-bar-right')" (31:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f3568756860> at 7f355ee7d900> -> __condition
                __expression = __cache_139867202242736

                # <Symbol value=<DEFAULT> at 7f3568756860> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_139867202242736
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n      </a>\n    </div>\n\n    ')

                # <Static value=<ast.Dict object at 0x7f355ee7d930> name=None at 7f355ee7c3d0> -> __attrs_139867202248496
                __attrs_139867202248496 = _static_139867202246960
                __backup_toolbar_main_139867202218272 = get('toolbar_main', __marker)

                # <Value 'view/base_render' (37:23)> -> __value
                __token = 1033
                try:
                    __zt_tmp = __attrs_139867202248496
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139867356405696('path', 'view/base_render', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                econtext['toolbar_main'] = __value

                # <Value 'toolbar_main' (39:23)> -> __condition
                __token = 1084
                try:
                    __zt_tmp = __attrs_139867202248496
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139867356405696('path', 'toolbar_main', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                if __condition:

                    # <ul ... (0:0)
                    # --------------------------------------------------------
                    __append('<ul class="nav flex-column plone-toolbar-main" >\n      ')

                    # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867202254784
                    __attrs_139867202254784 = _static_139867362323344

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867202256368
                    __default_139867202256368 = _DEFAULT_MARKER

                    # <Value 'toolbar_main' (41:33)> -> __cache_139867202253536
                    __token = 1137
                    try:
                        __zt_tmp = __attrs_139867202254784
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139867202253536 = _static_139867356405696('path', 'toolbar_main', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))

                    # <BinOp left=<Value 'toolbar_main' (41:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f3568756860> at 7f355ee7db40> -> __condition
                    __expression = __cache_139867202253536

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li>\n      </li>')
                    else:
                        __content = __cache_139867202253536
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('\n    </ul>')
                if (__backup_toolbar_main_139867202218272 is __marker):
                    del econtext['toolbar_main']
                else:
                    econtext['toolbar_main'] = __backup_toolbar_main_139867202218272
                __append('\n\n    ')

                # <Static value=<ast.Dict object at 0x7f355ee7c2b0> name=None at 7f355ee7d6c0> -> __attrs_139867202255360
                __attrs_139867202255360 = _static_139867202241200

                # <Value 'personal_bar/user_actions' (46:24)> -> __condition
                __token = 1295
                try:
                    __zt_tmp = __attrs_139867202255360
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139867356405696('path', 'personal_bar/user_actions', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div')

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867202249456
                    __default_139867202249456 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution "personaltools-wrapper nav ${python:'dropend' if toolbar_pos == 'side' else ''}" (45:16)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f355ee7cbb0> -> __attr_class
                    __token = 1191
                    __token = 1219
                    try:
                        __zt_tmp = __attrs_139867202255360
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_139867356405696('python', "'dropend' if toolbar_pos == 'side' else ''", econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    __attr_class = ('%s%s' % ('personaltools-wrapper nav ', (__attr_class if (__attr_class is not None) else ''), ))
                    if (__attr_class is None):
                        pass
                    else:
                        if (__attr_class is _DEFAULT_MARKER):
                            __attr_class = None
                        else:
                            __tt = type(__attr_class)
                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                __attr_class = str(__attr_class)
                            else:
                                if (__tt is bytes):
                                    __attr_class = decode(__attr_class)
                                else:
                                    if (__tt is not str):
                                        try:
                                            __attr_class = __attr_class.__html__
                                        except get('AttributeError', AttributeError):
                                            __converted = convert(__attr_class)
                                            __attr_class = (str(__attr_class) if (__attr_class is __converted) else __converted)
                                        else:
                                            __attr_class = __attr_class()
                    if (__attr_class is not None):
                        __append((' class="%s"' % __attr_class))
                    __append(' >\n\n      ')

                    # <Static value=<ast.Dict object at 0x7f355ee7fbe0> name=None at 7f355ee7e920> -> __attrs_139867202248640
                    __attrs_139867202248640 = _static_139867202255840

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a class="nav-link dropdown-toggle" id="personaltools-menulink" aria-expanded="false" data-bs-offset="0,0" data-bs-toggle="dropdown"')

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867202248208
                    __default_139867202248208 = _DEFAULT_MARKER

                    # <Substitution 'personal_bar/homelink_url' (55:16)> -> __attr_href
                    __token = 1546
                    try:
                        __zt_tmp = __attrs_139867202248640
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_139867356405696('path', 'personal_bar/homelink_url', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))
                    __append(' >\n        ')

                    # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867199011376
                    __attrs_139867199011376 = _static_139867362323344

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867199009840
                    __default_139867199009840 = _DEFAULT_MARKER

                    # <Value "python:icons.tag('toolbar-action/personaltools', tag_class='')" (58:41)> -> __cache_139867199012768
                    __token = 1633
                    try:
                        __zt_tmp = __attrs_139867199011376
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139867199012768 = _static_139867356405696('python', "icons.tag('toolbar-action/personaltools', tag_class='')", econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))

                    # <BinOp left=<Value "python:icons.tag('toolbar-action/personaltools', tag_class='')" (58:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f3568756860> at 7f355eb66740> -> __condition
                    __expression = __cache_139867199012768

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_139867199012768
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('\n        ')

                    # <Static value=<ast.Dict object at 0x7f355eb665f0> name=None at 7f355eb64040> -> __attrs_139867199007920
                    __attrs_139867199007920 = _static_139867199006192

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span class="toolbar-label" >')

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867199010464
                    __default_139867199010464 = _DEFAULT_MARKER

                    # <Value 'personal_bar/user_name' (60:27)> -> __cache_139867199004704
                    __token = 1763
                    try:
                        __zt_tmp = __attrs_139867199007920
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139867199004704 = _static_139867356405696('path', 'personal_bar/user_name', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))

                    # <BinOp left=<Value 'personal_bar/user_name' (60:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f3568756860> at 7f355eb664a0> -> __condition
                    __expression = __cache_139867199004704

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('User')
                    else:
                        __content = __cache_139867199004704
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</span>\n      </a>\n\n      ')

                    # <Static value=<ast.Dict object at 0x7f355eb67c40> name=None at 7f355eb65b40> -> __attrs_139867199009504
                    __attrs_139867199009504 = _static_139867199011904

                    # <ul ... (0:0)
                    # --------------------------------------------------------
                    __append('<ul class="dropdown-menu" id="collapse-personaltools" aria-labelledby="personaltools-menulink" >\n        ')

                    # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867199005040
                    __attrs_139867199005040 = _static_139867362323344

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append('<li>\n          ')

                    # <Static value=<ast.Dict object at 0x7f355eb66b30> name=None at 7f355eb64070> -> __attrs_139867199011616
                    __attrs_139867199011616 = _static_139867199007536

                    # <h6 ... (0:0)
                    # --------------------------------------------------------
                    __append('<h6 class="dropdown-header">')

                    # <Interpolation value=<Substitution '${personal_bar/user_name}' (69:38)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f355eb67fd0> -> __content_139867442113136
                    __token = 2000
                    __token = 2002
                    try:
                        __zt_tmp = __attrs_139867199011616
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __content_139867442113136 = _static_139867356405696('path', 'personal_bar/user_name', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                    __content_139867442113136 = __quote(__content_139867442113136, '\x00', '&#0;', None, None)
                    __content_139867442113136 = __content_139867442113136
                    if (__content_139867442113136 is None):
                        pass
                    else:
                        if (__content_139867442113136 is None):
                            __content_139867442113136 = None
                        else:
                            __tt = type(__content_139867442113136)
                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                __content_139867442113136 = str(__content_139867442113136)
                            else:
                                if (__tt is bytes):
                                    __content_139867442113136 = decode(__content_139867442113136)
                                else:
                                    if (__tt is not str):
                                        try:
                                            __content_139867442113136 = __content_139867442113136.__html__
                                        except get('AttributeError', AttributeError):
                                            __converted = convert(__content_139867442113136)
                                            __content_139867442113136 = (str(__content_139867442113136) if (__content_139867442113136 is __converted) else __converted)
                                        else:
                                            __content_139867442113136 = __content_139867442113136()
                    if (__content_139867442113136 is not None):
                        __append(__content_139867442113136)
                    __append('</h6>\n        </li>\n        ')

                    # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867199002496
                    __attrs_139867199002496 = _static_139867362323344
                    __backup_action_139867199168832 = get('action', __marker)

                    # <Value 'personal_bar/user_actions' (71:31)> -> __iterator
                    __token = 2076
                    try:
                        __zt_tmp = __attrs_139867199002496
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_139867356405696('path', 'personal_bar/user_actions', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                    (__iterator, ____index_139867199012288, ) = getname('repeat')('action', __iterator)
                    econtext['action'] = None
                    for __item in __iterator:
                        econtext['action'] = __item

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li>\n          ')

                        # <Static value=<ast.Dict object at 0x7f355eb66a10> name=None at 7f355eb65870> -> __attrs_139867199012720
                        __attrs_139867199012720 = _static_139867199007248

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append('<a')

                        # <Value 'action' (74:15)> -> __cache_139867199008592
                        __token = 2193
                        try:
                            __zt_tmp = __attrs_139867199012720
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_139867199008592 = _static_139867356405696('path', 'action', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                        if ('class' not in __chain(__cache_139867199008592)):
                            __append(' class="nav-link dropdown-item"')
                        __attr_139867199007680 = __cache_139867199008592
                        for (name, value, ) in __attr_139867199007680.items():
                            if (name in _static_139867199459280):
                                if not bool(value):
                                    continue
                                value = name
                            if ((name not in _static_139867199455776) and (value is not None)):
                                if (name in _static_139867199459280):
                                    if not bool(value):
                                        continue
                                    value = name
                                __append((((((' ' + name) + '=') + '"') + __quote(value, '"', '&quot;', None, None)) + '"'))
                        __append(' >\n            ')

                        # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867199001968
                        __attrs_139867199001968 = _static_139867362323344

                        # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867199007728
                        __default_139867199007728 = _DEFAULT_MARKER

                        # <Value "python:icons.tag(action.get('icon', 'dot'), tag_class='')" (77:41)> -> __cache_139867199010080
                        __token = 2269
                        try:
                            __zt_tmp = __attrs_139867199001968
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_139867199010080 = _static_139867356405696('python', "icons.tag(action.get('icon', 'dot'), tag_class='')", econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))

                        # <BinOp left=<Value "python:icons.tag(action.get('icon', 'dot'), tag_class='')" (77:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f3568756860> at 7f355eb66290> -> __condition
                        __expression = __cache_139867199010080

                        # <Symbol value=<DEFAULT> at 7f3568756860> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_139867199010080
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        __append('\n            ')

                        # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867198998080
                        __attrs_139867198998080 = _static_139867362323344

                        # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867199002592
                        __default_139867199002592 = _DEFAULT_MARKER

                        # <Value 'action/title' (78:41)> -> __cache_139867199001344
                        __token = 2372
                        try:
                            __zt_tmp = __attrs_139867198998080
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_139867199001344 = _static_139867356405696('path', 'action/title', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))

                        # <BinOp left=<Value 'action/title' (78:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f3568756860> at 7f355eb67d00> -> __condition
                        __expression = __cache_139867199001344

                        # <Symbol value=<DEFAULT> at 7f3568756860> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('\n              action title\n            ')
                        else:
                            __content = __cache_139867199001344
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('\n          </a>\n        </li>')
                        ____index_139867199012288 -= 1
                        if (____index_139867199012288 > 0):
                            __append('\n        ')
                    if (__backup_action_139867199168832 is __marker):
                        del econtext['action']
                    else:
                        econtext['action'] = __backup_action_139867199168832
                    __append('\n      </ul>\n\n    </div>')
                __append('\n  </div>\n</section>')
                __i18n_domain = __previous_i18n_domain_139867199161632
            if (__backup_toolbar_pos_139867202237584 is __marker):
                del econtext['toolbar_pos']
            else:
                econtext['toolbar_pos'] = __backup_toolbar_pos_139867202237584
            if (__backup_personal_bar_139867202500640 is __marker):
                del econtext['personal_bar']
            else:
                econtext['personal_bar'] = __backup_personal_bar_139867202500640
            if (__backup_icons_139867202216832 is __marker):
                del econtext['icons']
            else:
                econtext['icons'] = __backup_icons_139867202216832
            if (__backup_context_state_139867202218704 is __marker):
                del econtext['context_state']
            else:
                econtext['context_state'] = __backup_context_state_139867202218704
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }