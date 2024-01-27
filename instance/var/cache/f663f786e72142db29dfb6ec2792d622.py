# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/plone/app/layout/viewlets/keywords.pt'

__tokens = {75: ('context/Subject|nothing', 3, 22), 120: (' nocall:modules/Products.PythonScripts.standard/url_quot', 4, 20), 214: ('categories', 6, 24), 481: ('categories', 18, 37), 627: ('python:url_quote(category)', 23, 21), 708: ('string:${context/@@plone_portal_state/navigation_root_url}/@@search?Subject%3Alist=${quotedCat}', 26, 16), 851: ('category', 29, 27)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139867200039056 = {'class': 'btn btn-sm btn-outline-primary', 'href': '#', 'rel': 'nofollow', }
_static_139867362323344 = {}
_static_139867200037040 = {'class': 'card-title section-heading d-none', }
_static_139867200030560 = {'class': 'viewlet keywords-viewlet', }
_static_139867356405408 = __C2ZContextWrapper
_static_139867356405696 = __compile_zt_expr
_static_139867200035120 = {'id': 'section-category', }

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

            # <Static value=<ast.Dict object at 0x7f355ec61930> name=None at 7f355ec62b90> -> __attrs_139867200033824
            __attrs_139867200033824 = _static_139867200035120
            __backup_categories_139867198606160 = get('categories', __marker)

            # <Value 'context/Subject|nothing' (3:22)> -> __value
            __token = 75
            try:
                __zt_tmp = __attrs_139867200033824
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139867356405696('path', 'context/Subject|nothing', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            econtext['categories'] = __value
            __backup_url_quote_139867199166816 = get('url_quote', __marker)

            # <Value 'nocall:modules/Products.PythonScripts.standard/url_quote' (4:20)> -> __value
            __token = 120
            try:
                __zt_tmp = __attrs_139867200033824
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139867356405696('nocall', 'modules/Products.PythonScripts.standard/url_quote', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            econtext['url_quote'] = __value

            # <Value 'categories' (6:24)> -> __condition
            __token = 214
            try:
                __zt_tmp = __attrs_139867200033824
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_139867356405696('path', 'categories', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_139867200040544 = __i18n_domain
                __i18n_domain = 'plone'

                # <section ... (0:0)
                # --------------------------------------------------------
                __append('<section id="section-category" >\n\n  ')

                # <Static value=<ast.Dict object at 0x7f355ec60760> name=None at 7f355ec60c70> -> __attrs_139867200037568
                __attrs_139867200037568 = _static_139867200030560

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="viewlet keywords-viewlet">\n\n    ')

                # <Static value=<ast.Dict object at 0x7f355ec620b0> name=None at 7f355ec62530> -> __attrs_139867200030752
                __attrs_139867200030752 = _static_139867200037040

                # <header ... (0:0)
                # --------------------------------------------------------
                __append('<header class="card-title section-heading d-none" >')
                __stream_139867200030896 = []
                __append_139867200030896 = __stream_139867200030896.append
                __append_139867200030896('\n      Keywords\n    ')
                __msgid_139867200030896 = __re_whitespace(''.join(__stream_139867200030896)).strip()
                if 'section_keywords_heading':
                    __append(translate('section_keywords_heading', mapping=None, default=__msgid_139867200030896, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</header>\n\n    ')

                # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867200044864
                __attrs_139867200044864 = _static_139867362323344
                __backup_category_139867199510592 = get('category', __marker)

                # <Value 'categories' (18:37)> -> __iterator
                __token = 481
                try:
                    __zt_tmp = __attrs_139867200044864
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_139867356405696('path', 'categories', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                (__iterator, ____index_139867200034304, ) = getname('repeat')('category', __iterator)
                econtext['category'] = None
                for __item in __iterator:
                    econtext['category'] = __item
                    __append('\n      ')

                    # <Static value=<ast.Dict object at 0x7f355ec62890> name=None at 7f355ec61de0> -> __attrs_139867200040496
                    __attrs_139867200040496 = _static_139867200039056
                    __backup_quotedCat_139867202366544 = get('quotedCat', __marker)

                    # <Value 'python:url_quote(category)' (23:21)> -> __value
                    __token = 627
                    try:
                        __zt_tmp = __attrs_139867200040496
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_139867356405696('python', 'url_quote(category)', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                    econtext['quotedCat'] = __value

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a class="btn btn-sm btn-outline-primary"')

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867200039680
                    __default_139867200039680 = _DEFAULT_MARKER

                    # <Substitution 'string:${context/@@plone_portal_state/navigation_root_url}/@@search?Subject%3Alist=${quotedCat}' (26:16)> -> __attr_href
                    __token = 708
                    try:
                        __zt_tmp = __attrs_139867200040496
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_139867356405696('string', '${context/@@plone_portal_state/navigation_root_url}/@@search?Subject%3Alist=${quotedCat}', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '#', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))
                    __append(' rel="nofollow" >\n        ')

                    # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867200040160
                    __attrs_139867200040160 = _static_139867362323344

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>')

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867200036368
                    __default_139867200036368 = _DEFAULT_MARKER

                    # <Value 'category' (29:27)> -> __cache_139867200029600
                    __token = 851
                    try:
                        __zt_tmp = __attrs_139867200040160
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139867200029600 = _static_139867356405696('path', 'category', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))

                    # <BinOp left=<Value 'category' (29:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f3568756860> at 7f355ec609d0> -> __condition
                    __expression = __cache_139867200029600

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_139867200029600
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</span>\n      </a>')
                    if (__backup_quotedCat_139867202366544 is __marker):
                        del econtext['quotedCat']
                    else:
                        econtext['quotedCat'] = __backup_quotedCat_139867202366544
                    __append('\n    ')
                    ____index_139867200034304 -= 1
                    if (____index_139867200034304 > 0):
                        __append('')
                if (__backup_category_139867199510592 is __marker):
                    del econtext['category']
                else:
                    econtext['category'] = __backup_category_139867199510592
                __append('\n\n  </div>\n\n</section>')
                __i18n_domain = __previous_i18n_domain_139867200040544
            if (__backup_url_quote_139867199166816 is __marker):
                del econtext['url_quote']
            else:
                econtext['url_quote'] = __backup_url_quote_139867199166816
            if (__backup_categories_139867198606160 is __marker):
                del econtext['categories']
            else:
                econtext['categories'] = __backup_categories_139867198606160
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }