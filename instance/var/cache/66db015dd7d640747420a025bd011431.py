# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/plone/app/layout/viewlets/document_byline.pt'

__tokens = {53: ('view/show', 2, 24), 154: ('here/creators', 6, 30), 206: (' context/@@plone_portal_state/navigation_root_ur', 7, 37), 306: ('python:creator_ids and view.show_about()', 9, 31), 427: ('creator_ids', 12, 29), 493: ('python: view.get_url_path(user_id)', 14, 27), 555: (' python:view.get_fullname(user_id', 15, 26), 761: ('url_path', 19, 26), 699: ('${navigation_root_url}/${url_path}', 18, 17), 701: ('navigation_root_url', 18, 19), 724: ('url_path', 18, 42), 780: ('${fullname}', 20, 9), 782: ('fullname', 20, 11), 900: ('not:url_path', 22, 29), 923: ('${fullname}', 23, 9), 925: ('fullname', 23, 11), 1053: ('view/pub_date', 30, 25), 1091: (' context/ModificationDat', 31, 23), 1154: ('e python:view.show_modification_date', 32, 36), 1271: ('published', 35, 25), 1373: ('python:context.toLocalizedTime(published)', 38, 25), 1452: ('show_modification_date', 38, 104), 1561: ('show_modification_date', 42, 25), 1698: ('python:context.toLocalizedTime(modified)', 47, 25), 1828: ('view/isExpired', 53, 30)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139867200363904 = {'class': 'state-expired', }
_static_139867199948544 = {'class': 'documentModified', }
_static_139867199955984 = {'class': 'documentPublished', }
_static_139867199961312 = {'class': 'badge rounded-pill bg-light text-dark fw-normal fs-6', }
_static_139867202242160 = {'class': 'badge rounded-pill bg-light text-dark fw-normal fs-6', 'href': '${navigation_root_url}/${url_path}', }
_static_139867362323344 = {}
_static_139867356405408 = __C2ZContextWrapper
_static_139867356405696 = __compile_zt_expr
_static_139867202250032 = {'id': 'section-byline', }

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

            # <Static value=<ast.Dict object at 0x7f355ee7e530> name=None at 7f355ee7f820> -> __attrs_139867202249792
            __attrs_139867202249792 = _static_139867202250032

            # <Value 'view/show' (2:24)> -> __condition
            __token = 53
            try:
                __zt_tmp = __attrs_139867202249792
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_139867356405696('path', 'view/show', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_139867202247008 = __i18n_domain
                __i18n_domain = 'plone'

                # <section ... (0:0)
                # --------------------------------------------------------
                __append('<section id="section-byline" >\n  ')

                # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867202245856
                __attrs_139867202245856 = _static_139867362323344
                __backup_creator_ids_139867202251232 = get('creator_ids', __marker)

                # <Value 'here/creators' (6:30)> -> __value
                __token = 154
                try:
                    __zt_tmp = __attrs_139867202245856
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139867356405696('path', 'here/creators', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                econtext['creator_ids'] = __value
                __backup_navigation_root_url_139867202243504 = get('navigation_root_url', __marker)

                # <Value 'context/@@plone_portal_state/navigation_root_url' (7:37)> -> __value
                __token = 206
                try:
                    __zt_tmp = __attrs_139867202245856
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139867356405696('path', 'context/@@plone_portal_state/navigation_root_url', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                econtext['navigation_root_url'] = __value

                # <Value 'python:creator_ids and view.show_about()' (9:31)> -> __condition
                __token = 306
                try:
                    __zt_tmp = __attrs_139867202245856
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139867356405696('python', 'creator_ids and view.show_about()', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                if __condition:
                    __append('\n    ')

                    # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867202253296
                    __attrs_139867202253296 = _static_139867362323344
                    __stream_139867202256800 = []
                    __append_139867202256800 = __stream_139867202256800.append
                    __append_139867202256800('by')
                    __msgid_139867202256800 = __re_whitespace(''.join(__stream_139867202256800)).strip()
                    if __msgid_139867202256800:
                        __append(translate(__msgid_139867202256800, mapping=None, default=__msgid_139867202256800, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('\n    ')

                    # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867202242784
                    __attrs_139867202242784 = _static_139867362323344
                    __backup_user_id_139867202256272 = get('user_id', __marker)

                    # <Value 'creator_ids' (12:29)> -> __iterator
                    __token = 427
                    try:
                        __zt_tmp = __attrs_139867202242784
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_139867356405696('path', 'creator_ids', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                    (__iterator, ____index_139867202248400, ) = getname('repeat')('user_id', __iterator)
                    econtext['user_id'] = None
                    for __item in __iterator:
                        econtext['user_id'] = __item
                        __append('\n      ')

                        # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867202252624
                        __attrs_139867202252624 = _static_139867362323344
                        __backup_url_path_139867202247680 = get('url_path', __marker)

                        # <Value 'python: view.get_url_path(user_id)' (14:27)> -> __value
                        __token = 493
                        try:
                            __zt_tmp = __attrs_139867202252624
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_139867356405696('python', ' view.get_url_path(user_id)', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                        econtext['url_path'] = __value
                        __backup_fullname_139867202242640 = get('fullname', __marker)

                        # <Value 'python:view.get_fullname(user_id)' (15:26)> -> __value
                        __token = 555
                        try:
                            __zt_tmp = __attrs_139867202252624
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_139867356405696('python', 'view.get_fullname(user_id)', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                        econtext['fullname'] = __value
                        __append('\n        ')

                        # <Static value=<ast.Dict object at 0x7f355ee7c670> name=None at 7f355ee7f370> -> __attrs_139867199962272
                        __attrs_139867199962272 = _static_139867202242160

                        # <Value 'url_path' (19:26)> -> __condition
                        __token = 761
                        try:
                            __zt_tmp = __attrs_139867199962272
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_139867356405696('path', 'url_path', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                        if __condition:

                            # <a ... (0:0)
                            # --------------------------------------------------------
                            __append('<a class="badge rounded-pill bg-light text-dark fw-normal fs-6"')

                            # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867199962992
                            __default_139867199962992 = _DEFAULT_MARKER

                            # <Interpolation value=<Substitution '${navigation_root_url}/${url_path}' (18:17)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f355ec4da50> -> __attr_href
                            __token = 699
                            __token = 701
                            try:
                                __zt_tmp = __attrs_139867199962272
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_href = _static_139867356405696('path', 'navigation_root_url', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                            __token = 724
                            try:
                                __zt_tmp = __attrs_139867199962272
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_href_722 = _static_139867356405696('path', 'url_path', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                            __attr_href_722 = __quote(__attr_href_722, '"', '&quot;', None, _DEFAULT_MARKER)
                            __attr_href = ('%s%s%s' % ((__attr_href if (__attr_href is not None) else ''), '/', (__attr_href_722 if (__attr_href_722 is not None) else ''), ))
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

                            # <Interpolation value=<Substitution '${fullname}' (20:9)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f355ec4feb0> -> __content_139867442113136
                            __token = 780
                            __token = 782
                            try:
                                __zt_tmp = __attrs_139867199962272
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
                        __append('\n        ')

                        # <Static value=<ast.Dict object at 0x7f355ec4f8e0> name=None at 7f355ec4e800> -> __attrs_139867199954016
                        __attrs_139867199954016 = _static_139867199961312

                        # <Value 'not:url_path' (22:29)> -> __condition
                        __token = 900
                        try:
                            __zt_tmp = __attrs_139867199954016
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_139867356405696('not', 'url_path', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span class="badge rounded-pill bg-light text-dark fw-normal fs-6" >')

                            # <Interpolation value=<Substitution '${fullname}' (23:9)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f355ec4d810> -> __content_139867442113136
                            __token = 923
                            __token = 925
                            try:
                                __zt_tmp = __attrs_139867199954016
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
                        __append('\n      ')
                        if (__backup_fullname_139867202242640 is __marker):
                            del econtext['fullname']
                        else:
                            econtext['fullname'] = __backup_fullname_139867202242640
                        if (__backup_url_path_139867202247680 is __marker):
                            del econtext['url_path']
                        else:
                            econtext['url_path'] = __backup_url_path_139867202247680
                        __append('\n    ')
                        ____index_139867202248400 -= 1
                        if (____index_139867202248400 > 0):
                            __append('')
                    if (__backup_user_id_139867202256272 is __marker):
                        del econtext['user_id']
                    else:
                        econtext['user_id'] = __backup_user_id_139867202256272
                    __append('\n    &mdash;\n  ')
                if (__backup_navigation_root_url_139867202243504 is __marker):
                    del econtext['navigation_root_url']
                else:
                    econtext['navigation_root_url'] = __backup_navigation_root_url_139867202243504
                if (__backup_creator_ids_139867202251232 is __marker):
                    del econtext['creator_ids']
                else:
                    econtext['creator_ids'] = __backup_creator_ids_139867202251232
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867202244368
                __attrs_139867202244368 = _static_139867362323344
                __backup_published_139867202252000 = get('published', __marker)

                # <Value 'view/pub_date' (30:25)> -> __value
                __token = 1053
                try:
                    __zt_tmp = __attrs_139867202244368
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139867356405696('path', 'view/pub_date', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                econtext['published'] = __value
                __backup_modified_139867202250848 = get('modified', __marker)

                # <Value 'context/ModificationDate' (31:23)> -> __value
                __token = 1091
                try:
                    __zt_tmp = __attrs_139867202244368
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139867356405696('path', 'context/ModificationDate', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                econtext['modified'] = __value
                __backup_show_modification_date_139867202241680 = get('show_modification_date', __marker)

                # <Value 'python:view.show_modification_date()' (32:36)> -> __value
                __token = 1154
                try:
                    __zt_tmp = __attrs_139867202244368
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139867356405696('python', 'view.show_modification_date()', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                econtext['show_modification_date'] = __value
                __append('\n    ')

                # <Static value=<ast.Dict object at 0x7f355ec4e410> name=None at 7f355ec4e1d0> -> __attrs_139867199951760
                __attrs_139867199951760 = _static_139867199955984

                # <Value 'published' (35:25)> -> __condition
                __token = 1271
                try:
                    __zt_tmp = __attrs_139867199951760
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139867356405696('path', 'published', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span class="documentPublished" >\n      ')

                    # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867199962944
                    __attrs_139867199962944 = _static_139867362323344

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>')
                    __stream_139867199949504 = []
                    __append_139867199949504 = __stream_139867199949504.append
                    __append_139867199949504('published')
                    __msgid_139867199949504 = __re_whitespace(''.join(__stream_139867199949504)).strip()
                    if 'box_published':
                        __append(translate('box_published', mapping=None, default=__msgid_139867199949504, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</span>\n      ')

                    # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867199949840
                    __attrs_139867199949840 = _static_139867362323344

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>')

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867199957952
                    __default_139867199957952 = _DEFAULT_MARKER

                    # <Value 'python:context.toLocalizedTime(published)' (38:25)> -> __cache_139867199954688
                    __token = 1373
                    try:
                        __zt_tmp = __attrs_139867199949840
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139867199954688 = _static_139867356405696('python', 'context.toLocalizedTime(published)', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))

                    # <BinOp left=<Value 'python:context.toLocalizedTime(published)' (38:25)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f3568756860> at 7f355ec4c340> -> __condition
                    __expression = __cache_139867199954688

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('Published')
                    else:
                        __content = __cache_139867199954688
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</span>')

                    # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867199948976
                    __attrs_139867199948976 = _static_139867362323344

                    # <Value 'show_modification_date' (38:104)> -> __condition
                    __token = 1452
                    try:
                        __zt_tmp = __attrs_139867199948976
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_139867356405696('path', 'show_modification_date', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                    if __condition:
                        __append(',')
                    __append('\n    </span>')
                __append('\n\n    ')

                # <Static value=<ast.Dict object at 0x7f355ec4c700> name=None at 7f355ec4ddb0> -> __attrs_139867199959056
                __attrs_139867199959056 = _static_139867199948544

                # <Value 'show_modification_date' (42:25)> -> __condition
                __token = 1561
                try:
                    __zt_tmp = __attrs_139867199959056
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139867356405696('path', 'show_modification_date', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span class="documentModified" >\n      ')

                    # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867199958096
                    __attrs_139867199958096 = _static_139867362323344

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>')
                    __stream_139867199954544 = []
                    __append_139867199954544 = __stream_139867199954544.append
                    __append_139867199954544('\n      last modified\n      ')
                    __msgid_139867199954544 = __re_whitespace(''.join(__stream_139867199954544)).strip()
                    if 'box_last_modified':
                        __append(translate('box_last_modified', mapping=None, default=__msgid_139867199954544, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</span>\n      ')

                    # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867200367024
                    __attrs_139867200367024 = _static_139867362323344

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>')

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867200365680
                    __default_139867200365680 = _DEFAULT_MARKER

                    # <Value 'python:context.toLocalizedTime(modified)' (47:25)> -> __cache_139867200367648
                    __token = 1698
                    try:
                        __zt_tmp = __attrs_139867200367024
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139867200367648 = _static_139867356405696('python', 'context.toLocalizedTime(modified)', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))

                    # <BinOp left=<Value 'python:context.toLocalizedTime(modified)' (47:25)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f3568756860> at 7f355ecb2650> -> __condition
                    __expression = __cache_139867200367648

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n      Modified\n      ')
                    else:
                        __content = __cache_139867200367648
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</span>\n    </span>')
                __append('\n  ')
                if (__backup_show_modification_date_139867202241680 is __marker):
                    del econtext['show_modification_date']
                else:
                    econtext['show_modification_date'] = __backup_show_modification_date_139867202241680
                if (__backup_modified_139867202250848 is __marker):
                    del econtext['modified']
                else:
                    econtext['modified'] = __backup_modified_139867202250848
                if (__backup_published_139867202252000 is __marker):
                    del econtext['published']
                else:
                    econtext['published'] = __backup_published_139867202252000
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867200367216
                __attrs_139867200367216 = _static_139867362323344

                # <Value 'view/isExpired' (53:30)> -> __condition
                __token = 1828
                try:
                    __zt_tmp = __attrs_139867200367216
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139867356405696('path', 'view/isExpired', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                if __condition:
                    __append('\n    &mdash;\n    ')

                    # <Static value=<ast.Dict object at 0x7f355ecb1d80> name=None at 7f355ecb2d70> -> __attrs_139867200364048
                    __attrs_139867200364048 = _static_139867200363904

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span class="state-expired" >')
                    __stream_139867200365488 = []
                    __append_139867200365488 = __stream_139867200365488.append
                    __append_139867200365488('expired')
                    __msgid_139867200365488 = __re_whitespace(''.join(__stream_139867200365488)).strip()
                    if 'time_expired':
                        __append(translate('time_expired', mapping=None, default=__msgid_139867200365488, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</span>\n  ')
                __append('\n\n</section>')
                __i18n_domain = __previous_i18n_domain_139867202247008
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }