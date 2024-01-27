# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/plone/app/layout/viewlets/path_bar.pt'

__tokens = {96: ('python:view.breadcrumbs', 5, 19), 286: ('${python:view.navigation_root_url}', 12, 43), 288: ('python:view.navigation_root_url', 12, 45), 417: ('breadcrumbs', 15, 34), 494: ('not: repeat/crumb/end', 17, 27), 535: ("${python:crumb['absolute_url']}", 18, 18), 537: ("python:crumb['absolute_url']", 18, 20), 568: ("${python:crumb['Title']}", 18, 51), 570: ("python:crumb['Title']", 18, 53), 704: ('repeat/crumb/end', 21, 27), 731: ("${python:crumb['Title']}", 22, 9), 733: ("python:crumb['Title']", 22, 11)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139867200186320 = {'class': 'breadcrumb-item active', 'aria-current': 'page', }
_static_139867199948256 = {'href': "${python:crumb['absolute_url']}", }
_static_139867199949216 = {'class': 'breadcrumb-item', }
_static_139867362323344 = {}
_static_139867199947056 = {'href': '${python:view.navigation_root_url}', }
_static_139867199949696 = {'class': 'breadcrumb-item', }
_static_139867199955744 = {'class': 'breadcrumb', }
_static_139867199961408 = {'class': 'container', }
_static_139867356405408 = __C2ZContextWrapper
_static_139867356405696 = __compile_zt_expr
_static_139867199949072 = {'id': 'portal-breadcrumbs', 'aria-label': 'breadcrumb', }

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
            __append('\n')

            # <Static value=<ast.Dict object at 0x7f355ec4c910> name=None at 7f355ec4c0d0> -> __attrs_139867199952048
            __attrs_139867199952048 = _static_139867199949072
            __backup_breadcrumbs_139867200189104 = get('breadcrumbs', __marker)

            # <Value 'python:view.breadcrumbs' (5:19)> -> __value
            __token = 96
            try:
                __zt_tmp = __attrs_139867199952048
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139867356405696('python', 'view.breadcrumbs', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            econtext['breadcrumbs'] = __value
            __previous_i18n_domain_139867199957088 = __i18n_domain
            __i18n_domain = 'plone'

            # <nav ... (0:0)
            # --------------------------------------------------------
            __append('<nav id="portal-breadcrumbs"')

            # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867199962272
            __default_139867199962272 = _DEFAULT_MARKER

            # <Translate msgid=None node=<ast.Constant object at 0x7f355ec4d480> at 7f355ec4fdc0> -> __attr_aria_label
            __attr_aria_label = 'breadcrumb'
            __attr_aria_label = translate(__attr_aria_label, default=__attr_aria_label, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
            if (__attr_aria_label is not None):
                __append((' aria-label="%s"' % __attr_aria_label))
            __append(' >\n  ')

            # <Static value=<ast.Dict object at 0x7f355ec4f940> name=None at 7f355ec4fe20> -> __attrs_139867199954448
            __attrs_139867199954448 = _static_139867199961408

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="container">\n    ')

            # <Static value=<ast.Dict object at 0x7f355ec4e320> name=None at 7f355ec4d690> -> __attrs_139867199952672
            __attrs_139867199952672 = _static_139867199955744

            # <ol ... (0:0)
            # --------------------------------------------------------
            __append('<ol class="breadcrumb">\n      ')

            # <Static value=<ast.Dict object at 0x7f355ec4cb80> name=None at 7f355ec4ff40> -> __attrs_139867199946864
            __attrs_139867199946864 = _static_139867199949696

            # <li ... (0:0)
            # --------------------------------------------------------
            __append('<li class="breadcrumb-item">')

            # <Static value=<ast.Dict object at 0x7f355ec4c130> name=None at 7f355ec4ec50> -> __attrs_139867199949168
            __attrs_139867199949168 = _static_139867199947056

            # <a ... (0:0)
            # --------------------------------------------------------
            __append('<a')

            # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867199959248
            __default_139867199959248 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution '${python:view.navigation_root_url}' (12:43)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f355ec4f250> -> __attr_href
            __token = 286
            __token = 288
            try:
                __zt_tmp = __attrs_139867199949168
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_139867356405696('python', 'view.navigation_root_url', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_href = __attr_href
            if (__attr_href is None):
                pass
            else:
                if (__attr_href is _DEFAULT_MARKER):
                    __attr_href = None
                else:
                    __tt = type(__attr_href)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __attr_href = str(__attr_href)
                    else:
                        if (__tt is bytes):
                            __attr_href = decode(__attr_href)
                        else:
                            if (__tt is not str):
                                try:
                                    __attr_href = __attr_href.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__attr_href)
                                    __attr_href = (str(__attr_href) if (__attr_href is __converted) else __converted)
                                else:
                                    __attr_href = __attr_href()
            if (__attr_href is not None):
                __append((' href="%s"' % __attr_href))
            __append(' >')
            __stream_139867199950128 = []
            __append_139867199950128 = __stream_139867199950128.append
            __append_139867199950128('Home')
            __msgid_139867199950128 = __re_whitespace(''.join(__stream_139867199950128)).strip()
            if 'tabs_home':
                __append(translate('tabs_home', mapping=None, default=__msgid_139867199950128, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</a></li>\n      ')

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867199948496
            __attrs_139867199948496 = _static_139867362323344
            __backup_crumb_139867198617584 = get('crumb', __marker)

            # <Value 'breadcrumbs' (15:34)> -> __iterator
            __token = 417
            try:
                __zt_tmp = __attrs_139867199948496
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_139867356405696('path', 'breadcrumbs', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            (__iterator, ____index_139867199952192, ) = getname('repeat')('crumb', __iterator)
            econtext['crumb'] = None
            for __item in __iterator:
                econtext['crumb'] = __item
                __append('\n        ')

                # <Static value=<ast.Dict object at 0x7f355ec4c9a0> name=None at 7f355ec4d120> -> __attrs_139867199947200
                __attrs_139867199947200 = _static_139867199949216

                # <Value 'not: repeat/crumb/end' (17:27)> -> __condition
                __token = 494
                try:
                    __zt_tmp = __attrs_139867199947200
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139867356405696('not', ' repeat/crumb/end', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                if __condition:

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append('<li class="breadcrumb-item" >')

                    # <Static value=<ast.Dict object at 0x7f355ec4c5e0> name=None at 7f355ec4d9c0> -> __attrs_139867200188192
                    __attrs_139867200188192 = _static_139867199948256

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867199949792
                    __default_139867199949792 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution "${python:crumb['absolute_url']}" (18:18)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f355ec4f280> -> __attr_href
                    __token = 535
                    __token = 537
                    try:
                        __zt_tmp = __attrs_139867200188192
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_139867356405696('python', "crumb['absolute_url']", econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                    __attr_href = __attr_href
                    if (__attr_href is None):
                        pass
                    else:
                        if (__attr_href is _DEFAULT_MARKER):
                            __attr_href = None
                        else:
                            __tt = type(__attr_href)
                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                __attr_href = str(__attr_href)
                            else:
                                if (__tt is bytes):
                                    __attr_href = decode(__attr_href)
                                else:
                                    if (__tt is not str):
                                        try:
                                            __attr_href = __attr_href.__html__
                                        except get('AttributeError', AttributeError):
                                            __converted = convert(__attr_href)
                                            __attr_href = (str(__attr_href) if (__attr_href is __converted) else __converted)
                                        else:
                                            __attr_href = __attr_href()
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))
                    __append('>')

                    # <Interpolation value=<Substitution "${python:crumb['Title']}" (18:51)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f355ec86f80> -> __content_139867442113136
                    __token = 568
                    __token = 570
                    try:
                        __zt_tmp = __attrs_139867200188192
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __content_139867442113136 = _static_139867356405696('python', "crumb['Title']", econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
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
                    __append('</a></li>')
                __append('\n        ')

                # <Static value=<ast.Dict object at 0x7f355ec867d0> name=None at 7f355ec85bd0> -> __attrs_139867200190736
                __attrs_139867200190736 = _static_139867200186320

                # <Value 'repeat/crumb/end' (21:27)> -> __condition
                __token = 704
                try:
                    __zt_tmp = __attrs_139867200190736
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139867356405696('path', 'repeat/crumb/end', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                if __condition:

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append('<li class="breadcrumb-item active" aria-current="page" >')

                    # <Interpolation value=<Substitution "${python:crumb['Title']}" (22:9)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f355ec85900> -> __content_139867442113136
                    __token = 731
                    __token = 733
                    try:
                        __zt_tmp = __attrs_139867200190736
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __content_139867442113136 = _static_139867356405696('python', "crumb['Title']", econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
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
                    __append('</li>')
                __append('\n      ')
                ____index_139867199952192 -= 1
                if (____index_139867199952192 > 0):
                    __append('')
            if (__backup_crumb_139867198617584 is __marker):
                del econtext['crumb']
            else:
                econtext['crumb'] = __backup_crumb_139867198617584
            __append('\n    </ol>\n  </div>\n</nav>')
            __i18n_domain = __previous_i18n_domain_139867199957088
            if (__backup_breadcrumbs_139867200189104 is __marker):
                del econtext['breadcrumbs']
            else:
                econtext['breadcrumbs'] = __backup_breadcrumbs_139867200189104
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }