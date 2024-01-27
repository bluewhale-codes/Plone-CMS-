# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/plone/app/layout/viewlets/document_contributors.pt'

__tokens = {109: ('context/Contributors', 4, 24), 161: (' context/@@plone_portal_state/navigation_root_ur', 5, 30), 247: ('contributors', 7, 24), 445: ('contributors', 16, 27), 508: ('python: view.get_url_path(user_id)', 18, 25), 568: (' python:view.get_fullname(user_id', 19, 24), 766: ('url_path', 23, 24), 706: ('${navigation_root_url}/${url_path}', 22, 15), 708: ('navigation_root_url', 22, 17), 731: ('url_path', 22, 40), 783: ('${fullname}', 24, 7), 785: ('fullname', 24, 9), 899: ('not:url_path', 26, 27), 920: ('${fullname}', 27, 7), 922: ('fullname', 27, 9)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139867200559792 = {'class': 'badge rounded-pill bg-light text-dark fw-normal fs-6', }
_static_139867200561760 = {'class': 'badge rounded-pill bg-light text-dark fw-normal fs-6', 'href': '${navigation_root_url}/${url_path}', }
_static_139867362323344 = {}
_static_139867200562624 = {'class': 'section-heading', }
_static_139867356405408 = __C2ZContextWrapper
_static_139867356405696 = __compile_zt_expr
_static_139867200562816 = {'class': 'text-muted', 'id': 'section-contributors', }

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

            # <Static value=<ast.Dict object at 0x7f355ece2680> name=None at 7f355ece3460> -> __attrs_139867200563872
            __attrs_139867200563872 = _static_139867200562816
            __backup_contributors_139867200095664 = get('contributors', __marker)

            # <Value 'context/Contributors' (4:24)> -> __value
            __token = 109
            try:
                __zt_tmp = __attrs_139867200563872
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139867356405696('path', 'context/Contributors', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            econtext['contributors'] = __value
            __backup_navigation_root_url_139867199396384 = get('navigation_root_url', __marker)

            # <Value 'context/@@plone_portal_state/navigation_root_url' (5:30)> -> __value
            __token = 161
            try:
                __zt_tmp = __attrs_139867200563872
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139867356405696('path', 'context/@@plone_portal_state/navigation_root_url', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            econtext['navigation_root_url'] = __value

            # <Value 'contributors' (7:24)> -> __condition
            __token = 247
            try:
                __zt_tmp = __attrs_139867200563872
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_139867356405696('path', 'contributors', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_139867200566176 = __i18n_domain
                __i18n_domain = 'plone'

                # <section ... (0:0)
                # --------------------------------------------------------
                __append('<section class="text-muted" id="section-contributors" >\n\n  ')

                # <Static value=<ast.Dict object at 0x7f355ece25c0> name=None at 7f355ece3c10> -> __attrs_139867200558640
                __attrs_139867200558640 = _static_139867200562624

                # <header ... (0:0)
                # --------------------------------------------------------
                __append('<header class="section-heading" >')
                __stream_139867200554896 = []
                __append_139867200554896 = __stream_139867200554896.append
                __append_139867200554896('\n      Contributors\n  ')
                __msgid_139867200554896 = __re_whitespace(''.join(__stream_139867200554896)).strip()
                if 'section_contributors_heading':
                    __append(translate('section_contributors_heading', mapping=None, default=__msgid_139867200554896, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</header>\n  ')

                # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867200553840
                __attrs_139867200553840 = _static_139867362323344
                __backup_user_id_139867199510592 = get('user_id', __marker)

                # <Value 'contributors' (16:27)> -> __iterator
                __token = 445
                try:
                    __zt_tmp = __attrs_139867200553840
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_139867356405696('path', 'contributors', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                (__iterator, ____index_139867200564304, ) = getname('repeat')('user_id', __iterator)
                econtext['user_id'] = None
                for __item in __iterator:
                    econtext['user_id'] = __item
                    __append('\n    ')

                    # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867200558688
                    __attrs_139867200558688 = _static_139867362323344
                    __backup_url_path_139867202241680 = get('url_path', __marker)

                    # <Value 'python: view.get_url_path(user_id)' (18:25)> -> __value
                    __token = 508
                    try:
                        __zt_tmp = __attrs_139867200558688
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_139867356405696('python', ' view.get_url_path(user_id)', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                    econtext['url_path'] = __value
                    __backup_fullname_139867200290048 = get('fullname', __marker)

                    # <Value 'python:view.get_fullname(user_id)' (19:24)> -> __value
                    __token = 568
                    try:
                        __zt_tmp = __attrs_139867200558688
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_139867356405696('python', 'view.get_fullname(user_id)', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                    econtext['fullname'] = __value
                    __append('\n      ')

                    # <Static value=<ast.Dict object at 0x7f355ece2260> name=None at 7f355ece21d0> -> __attrs_139867200553312
                    __attrs_139867200553312 = _static_139867200561760

                    # <Value 'url_path' (23:24)> -> __condition
                    __token = 766
                    try:
                        __zt_tmp = __attrs_139867200553312
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_139867356405696('path', 'url_path', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                    if __condition:

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append('<a class="badge rounded-pill bg-light text-dark fw-normal fs-6"')

                        # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867200558064
                        __default_139867200558064 = _DEFAULT_MARKER

                        # <Interpolation value=<Substitution '${navigation_root_url}/${url_path}' (22:15)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f355ece2470> -> __attr_href
                        __token = 706
                        __token = 708
                        try:
                            __zt_tmp = __attrs_139867200553312
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_139867356405696('path', 'navigation_root_url', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                        __token = 731
                        try:
                            __zt_tmp = __attrs_139867200553312
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href_729 = _static_139867356405696('path', 'url_path', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                        __attr_href_729 = __quote(__attr_href_729, '"', '&quot;', None, _DEFAULT_MARKER)
                        __attr_href = ('%s%s%s' % ((__attr_href if (__attr_href is not None) else ''), '/', (__attr_href_729 if (__attr_href_729 is not None) else ''), ))
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

                        # <Interpolation value=<Substitution '${fullname}' (24:7)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f355ece23e0> -> __content_139867442113136
                        __token = 783
                        __token = 785
                        try:
                            __zt_tmp = __attrs_139867200553312
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __content_139867442113136 = _static_139867356405696('path', 'fullname', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
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
                        __append('</a>')
                    __append('\n      ')

                    # <Static value=<ast.Dict object at 0x7f355ece1ab0> name=None at 7f355ece1ff0> -> __attrs_139867200562768
                    __attrs_139867200562768 = _static_139867200559792

                    # <Value 'not:url_path' (26:27)> -> __condition
                    __token = 899
                    try:
                        __zt_tmp = __attrs_139867200562768
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_139867356405696('not', 'url_path', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="badge rounded-pill bg-light text-dark fw-normal fs-6" >')

                        # <Interpolation value=<Substitution '${fullname}' (27:7)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f355ece0190> -> __content_139867442113136
                        __token = 920
                        __token = 922
                        try:
                            __zt_tmp = __attrs_139867200562768
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __content_139867442113136 = _static_139867356405696('path', 'fullname', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
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
                        __append('</span>')
                    __append('\n    ')
                    if (__backup_fullname_139867200290048 is __marker):
                        del econtext['fullname']
                    else:
                        econtext['fullname'] = __backup_fullname_139867200290048
                    if (__backup_url_path_139867202241680 is __marker):
                        del econtext['url_path']
                    else:
                        econtext['url_path'] = __backup_url_path_139867202241680
                    __append('\n  ')
                    ____index_139867200564304 -= 1
                    if (____index_139867200564304 > 0):
                        __append('')
                if (__backup_user_id_139867199510592 is __marker):
                    del econtext['user_id']
                else:
                    econtext['user_id'] = __backup_user_id_139867199510592
                __append('\n\n</section>')
                __i18n_domain = __previous_i18n_domain_139867200566176
            if (__backup_navigation_root_url_139867199396384 is __marker):
                del econtext['navigation_root_url']
            else:
                econtext['navigation_root_url'] = __backup_navigation_root_url_139867199396384
            if (__backup_contributors_139867200095664 is __marker):
                del econtext['contributors']
            else:
                econtext['contributors'] = __backup_contributors_139867200095664
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }