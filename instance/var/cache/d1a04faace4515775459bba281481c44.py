# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/plone/app/i18n/locales/browser/languageselector.pt'

__tokens = {29: ('view/available', 1, 29), 118: ('view/showFlags', 4, 18), 151: (' view/language', 5, 17), 183: ('l context/@@plone_context_state/view_u', 6, 15), 241: ('rl view/portal_', 7, 16), 271: ("ons python:context.restrictedTraverse('@@iconresolv", 8, 10), 371: ('languages', 11, 31), 423: ('lang/code', 13, 17), 454: (' lang/selecte', 14, 20), 490: ('s string:language-${cod', 15, 20), 534: ("nt python: selected and 'currentLanguage ' or", 16, 17), 641: ('string:${current}${codeclass}', 19, 18), 753: ('lang/flag|nothing', 24, 18), 789: (' lang/native|lang/nam', 25, 17), 833: ('g python:showFlags and fl', 26, 20), 921: ('string:${here_url}?set_language=${code}', 29, 18), 980: (' nam', 30, 18), 1041: ('showflag', 33, 31), 1092: ("python:icons.tag(flag, tag_class='plone-icon-flag')", 34, 40), 1204: ('not: showflag', 36, 34), 1251: ('name', 37, 32)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139867200503968 = {'href': '', 'title': 'name', }
_static_139867200505936 = {'class': 'string:${current}${codeclass}', }
_static_139867200511984 = {'id': 'portal-languageselector', }
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

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867200513328
            __attrs_139867200513328 = _static_139867362323344

            # <Value 'view/available' (1:29)> -> __condition
            __token = 29
            try:
                __zt_tmp = __attrs_139867200513328
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_139867356405696('path', 'view/available', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            if __condition:
                __append('\n  ')

                # <Static value=<ast.Dict object at 0x7f355ecd5ff0> name=None at 7f355ecd5ba0> -> __attrs_139867200511552
                __attrs_139867200511552 = _static_139867200511984
                __backup_showFlags_139867199461104 = get('showFlags', __marker)

                # <Value 'view/showFlags' (4:18)> -> __value
                __token = 118
                try:
                    __zt_tmp = __attrs_139867200511552
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139867356405696('path', 'view/showFlags', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                econtext['showFlags'] = __value
                __backup_languages_139867200097536 = get('languages', __marker)

                # <Value 'view/languages' (5:17)> -> __value
                __token = 151
                try:
                    __zt_tmp = __attrs_139867200511552
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139867356405696('path', 'view/languages', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                econtext['languages'] = __value
                __backup_here_url_139867199312976 = get('here_url', __marker)

                # <Value 'context/@@plone_context_state/view_url' (6:15)> -> __value
                __token = 183
                try:
                    __zt_tmp = __attrs_139867200511552
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139867356405696('path', 'context/@@plone_context_state/view_url', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                econtext['here_url'] = __value
                __backup_portal_url_139867200183680 = get('portal_url', __marker)

                # <Value 'view/portal_url' (7:16)> -> __value
                __token = 241
                try:
                    __zt_tmp = __attrs_139867200511552
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139867356405696('path', 'view/portal_url', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                econtext['portal_url'] = __value
                __backup_icons_139867202220192 = get('icons', __marker)

                # <Value "python:context.restrictedTraverse('@@iconresolver')" (8:10)> -> __value
                __token = 271
                try:
                    __zt_tmp = __attrs_139867200511552
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139867356405696('python', "context.restrictedTraverse('@@iconresolver')", econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                econtext['icons'] = __value

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append('<ul id="portal-languageselector" >\n    ')

                # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867200514768
                __attrs_139867200514768 = _static_139867362323344
                __backup_lang_139867200504640 = get('lang', __marker)

                # <Value 'languages' (11:31)> -> __iterator
                __token = 371
                try:
                    __zt_tmp = __attrs_139867200514768
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_139867356405696('path', 'languages', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                (__iterator, ____index_139867200508960, ) = getname('repeat')('lang', __iterator)
                econtext['lang'] = None
                for __item in __iterator:
                    econtext['lang'] = __item
                    __append('\n      ')

                    # <Static value=<ast.Dict object at 0x7f355ecd4850> name=None at 7f355ecd7c10> -> __attrs_139867200518608
                    __attrs_139867200518608 = _static_139867200505936
                    __backup_code_139867200516352 = get('code', __marker)

                    # <Value 'lang/code' (13:17)> -> __value
                    __token = 423
                    try:
                        __zt_tmp = __attrs_139867200518608
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_139867356405696('path', 'lang/code', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                    econtext['code'] = __value
                    __backup_selected_139867200515488 = get('selected', __marker)

                    # <Value 'lang/selected' (14:20)> -> __value
                    __token = 454
                    try:
                        __zt_tmp = __attrs_139867200518608
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_139867356405696('path', 'lang/selected', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                    econtext['selected'] = __value
                    __backup_codeclass_139867200283376 = get('codeclass', __marker)

                    # <Value 'string:language-${code}' (15:20)> -> __value
                    __token = 490
                    try:
                        __zt_tmp = __attrs_139867200518608
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_139867356405696('string', 'language-${code}', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                    econtext['codeclass'] = __value
                    __backup_current_139867199160384 = get('current', __marker)

                    # <Value "python: selected and 'currentLanguage ' or ''" (16:17)> -> __value
                    __token = 534
                    try:
                        __zt_tmp = __attrs_139867200518608
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_139867356405696('python', " selected and 'currentLanguage ' or ''", econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                    econtext['current'] = __value

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append('<li')

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867200518176
                    __default_139867200518176 = _DEFAULT_MARKER

                    # <Substitution 'string:${current}${codeclass}' (19:18)> -> __attr_class
                    __token = 641
                    try:
                        __zt_tmp = __attrs_139867200518608
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_139867356405696('string', '${current}${codeclass}', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((' class="%s"' % __attr_class))
                    __append(' >\n        ')

                    # <Static value=<ast.Dict object at 0x7f355ecd40a0> name=None at 7f355ecd4880> -> __attrs_139867200505744
                    __attrs_139867200505744 = _static_139867200503968
                    __backup_flag_139867199506512 = get('flag', __marker)

                    # <Value 'lang/flag|nothing' (24:18)> -> __value
                    __token = 753
                    try:
                        __zt_tmp = __attrs_139867200505744
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_139867356405696('path', 'lang/flag|nothing', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                    econtext['flag'] = __value
                    __backup_name_139867200516688 = get('name', __marker)

                    # <Value 'lang/native|lang/name' (25:17)> -> __value
                    __token = 789
                    try:
                        __zt_tmp = __attrs_139867200505744
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_139867356405696('path', 'lang/native|lang/name', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                    econtext['name'] = __value
                    __backup_showflag_139867200520048 = get('showflag', __marker)

                    # <Value 'python:showFlags and flag' (26:20)> -> __value
                    __token = 833
                    try:
                        __zt_tmp = __attrs_139867200505744
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_139867356405696('python', 'showFlags and flag', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                    econtext['showflag'] = __value

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867200515392
                    __default_139867200515392 = _DEFAULT_MARKER

                    # <Substitution 'string:${here_url}?set_language=${code}' (29:18)> -> __attr_href
                    __token = 921
                    try:
                        __zt_tmp = __attrs_139867200505744
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_139867356405696('string', '${here_url}?set_language=${code}', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867200509632
                    __default_139867200509632 = _DEFAULT_MARKER

                    # <Substitution 'name' (30:18)> -> __attr_title
                    __token = 980
                    try:
                        __zt_tmp = __attrs_139867200505744
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_title = _static_139867356405696('path', 'name', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                    __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_title is not None):
                        __append((' title="%s"' % __attr_title))
                    __append(' >\n          ')

                    # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867200509200
                    __attrs_139867200509200 = _static_139867362323344

                    # <Value 'showflag' (33:31)> -> __condition
                    __token = 1041
                    try:
                        __zt_tmp = __attrs_139867200509200
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_139867356405696('path', 'showflag', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                    if __condition:
                        __append('\n            ')

                        # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867198608704
                        __attrs_139867198608704 = _static_139867362323344

                        # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867198615232
                        __default_139867198615232 = _DEFAULT_MARKER

                        # <Value "python:icons.tag(flag, tag_class='plone-icon-flag')" (34:40)> -> __cache_139867198608896
                        __token = 1092
                        try:
                            __zt_tmp = __attrs_139867198608704
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_139867198608896 = _static_139867356405696('python', "icons.tag(flag, tag_class='plone-icon-flag')", econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))

                        # <BinOp left=<Value "python:icons.tag(flag, tag_class='plone-icon-flag')" (34:40)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f3568756860> at 7f355eb05db0> -> __condition
                        __expression = __cache_139867198608896

                        # <Symbol value=<DEFAULT> at 7f3568756860> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <img ... (0:0)
                            # --------------------------------------------------------
                            __append('<img />')
                        else:
                            __content = __cache_139867198608896
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        __append('\n          ')
                    __append('\n          ')

                    # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867198619168
                    __attrs_139867198619168 = _static_139867362323344

                    # <Value 'not: showflag' (36:34)> -> __condition
                    __token = 1204
                    try:
                        __zt_tmp = __attrs_139867198619168
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_139867356405696('not', ' showflag', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                    if __condition:

                        # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867198619120
                        __default_139867198619120 = _DEFAULT_MARKER

                        # <Value 'name' (37:32)> -> __cache_139867198616528
                        __token = 1251
                        try:
                            __zt_tmp = __attrs_139867198619168
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_139867198616528 = _static_139867356405696('path', 'name', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))

                        # <BinOp left=<Value 'name' (37:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f3568756860> at 7f355eb065f0> -> __condition
                        __expression = __cache_139867198616528

                        # <Symbol value=<DEFAULT> at 7f3568756860> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('language name')
                        else:
                            __content = __cache_139867198616528
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                    __append('\n        </a>')
                    if (__backup_showflag_139867200520048 is __marker):
                        del econtext['showflag']
                    else:
                        econtext['showflag'] = __backup_showflag_139867200520048
                    if (__backup_name_139867200516688 is __marker):
                        del econtext['name']
                    else:
                        econtext['name'] = __backup_name_139867200516688
                    if (__backup_flag_139867199506512 is __marker):
                        del econtext['flag']
                    else:
                        econtext['flag'] = __backup_flag_139867199506512
                    __append('\n      </li>')
                    if (__backup_current_139867199160384 is __marker):
                        del econtext['current']
                    else:
                        econtext['current'] = __backup_current_139867199160384
                    if (__backup_codeclass_139867200283376 is __marker):
                        del econtext['codeclass']
                    else:
                        econtext['codeclass'] = __backup_codeclass_139867200283376
                    if (__backup_selected_139867200515488 is __marker):
                        del econtext['selected']
                    else:
                        econtext['selected'] = __backup_selected_139867200515488
                    if (__backup_code_139867200516352 is __marker):
                        del econtext['code']
                    else:
                        econtext['code'] = __backup_code_139867200516352
                    __append('\n    ')
                    ____index_139867200508960 -= 1
                    if (____index_139867200508960 > 0):
                        __append('')
                if (__backup_lang_139867200504640 is __marker):
                    del econtext['lang']
                else:
                    econtext['lang'] = __backup_lang_139867200504640
                __append('\n  </ul>')
                if (__backup_icons_139867202220192 is __marker):
                    del econtext['icons']
                else:
                    econtext['icons'] = __backup_icons_139867202220192
                if (__backup_portal_url_139867200183680 is __marker):
                    del econtext['portal_url']
                else:
                    econtext['portal_url'] = __backup_portal_url_139867200183680
                if (__backup_here_url_139867199312976 is __marker):
                    del econtext['here_url']
                else:
                    econtext['here_url'] = __backup_here_url_139867199312976
                if (__backup_languages_139867200097536 is __marker):
                    del econtext['languages']
                else:
                    econtext['languages'] = __backup_languages_139867200097536
                if (__backup_showFlags_139867199461104 is __marker):
                    del econtext['showFlags']
                else:
                    econtext['showFlags'] = __backup_showFlags_139867199461104
                __append('\n')
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }