# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/plone/app/dexterity/browser/types_listing_row.pt'

__tokens = {38: ('view/getCombinedWidgets', 2, 18), 82: (' context/@@plone_portal_state/porta', 3, 19), 138: ('t portal/@@plone_layo', 4, 18), 184: ('es view/getNiceTit', 5, 21), 243: ('tups', 7, 23), 285: ('python:tup[0].error', 11, 14), 317: (' repeat/tup/inde', 12, 11), 352: ('e nocall: context/@@plone/normalizeStri', 13, 16), 440: ("python:'field' + (error and ' error' or '') + (tup[0].__name__ == 'view_item_count' and ' count' or '')", 16, 14), 587: ('tup', 19, 30), 651: ('python:view.context.context.link(view.getContent(), widget.field.__name__)', 25, 16), 753: (" python:'contenttype-' + normalize(view.getContent().id", 26, 26), 845: ("python:widget.mode == 'input' or link is None", 28, 23), 934: ('link', 30, 16), 956: (' string:$item_type_clas', 31, 16), 1058: ('not:error', 36, 28), 1109: ('error', 38, 30), 1154: ('error/render', 39, 38), 1255: ('widget/render', 42, 40)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140097247467872 = {'type': 'text', }
_static_140097247463600 = {'class': 'error', }
_static_140097247471424 = {'href': '', 'class': 'string:$item_type_class', }
_static_140097247474640 = {'class': "python:'field' + (error and ' error' or '') + (tup[0].__name__ == 'view_item_count' and ' count' or '')", }
_static_140097413192176 = __C2ZContextWrapper
_static_140097413192464 = __compile_zt_expr
_static_140097412968080 = {}

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

            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097344095568
            __attrs_140097344095568 = _static_140097412968080
            __backup_tups_140097342776768 = get('tups', __marker)

            # <Value 'view/getCombinedWidgets' (2:18)> -> __value
            __token = 38
            try:
                __zt_tmp = __attrs_140097344095568
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('path', 'view/getCombinedWidgets', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['tups'] = __value
            __backup_portal_140097342775280 = get('portal', __marker)

            # <Value 'context/@@plone_portal_state/portal' (3:19)> -> __value
            __token = 82
            try:
                __zt_tmp = __attrs_140097344095568
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('path', 'context/@@plone_portal_state/portal', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['portal'] = __value
            __backup_layout_140097252390176 = get('layout', __marker)

            # <Value 'portal/@@plone_layout' (4:18)> -> __value
            __token = 138
            try:
                __zt_tmp = __attrs_140097344095568
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('path', 'portal/@@plone_layout', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['layout'] = __value
            __backup_niceTitles_140097342770480 = get('niceTitles', __marker)

            # <Value 'view/getNiceTitles' (5:21)> -> __value
            __token = 184
            try:
                __zt_tmp = __attrs_140097344095568
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('path', 'view/getNiceTitles', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['niceTitles'] = __value
            __backup_tup_140097342771152 = get('tup', __marker)

            # <Value 'tups' (7:23)> -> __iterator
            __token = 243
            try:
                __zt_tmp = __attrs_140097344095568
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140097413192464('path', 'tups', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            (__iterator, ____index_140097247476800, ) = getname('repeat')('tup', __iterator)
            econtext['tup'] = None
            for __item in __iterator:
                econtext['tup'] = __item
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x7f6aeeab73d0> name=None at 7f6aeeab7370> -> __attrs_140097247474256
                __attrs_140097247474256 = _static_140097247474640
                __backup_error_140097342775328 = get('error', __marker)

                # <Value 'python:tup[0].error' (11:14)> -> __value
                __token = 285
                try:
                    __zt_tmp = __attrs_140097247474256
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140097413192464('python', 'tup[0].error', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                econtext['error'] = __value
                __backup_idx_140097342767312 = get('idx', __marker)

                # <Value 'repeat/tup/index' (12:11)> -> __value
                __token = 317
                try:
                    __zt_tmp = __attrs_140097247474256
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140097413192464('path', 'repeat/tup/index', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                econtext['idx'] = __value
                __backup_normalize_140097342773024 = get('normalize', __marker)

                # <Value 'nocall: context/@@plone/normalizeString' (13:16)> -> __value
                __token = 352
                try:
                    __zt_tmp = __attrs_140097247474256
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140097413192464('nocall', ' context/@@plone/normalizeString', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                econtext['normalize'] = __value

                # <td ... (0:0)
                # --------------------------------------------------------
                __append('<td')

                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097247475216
                __default_140097247475216 = _DEFAULT_MARKER

                # <Substitution "python:'field' + (error and ' error' or '') + (tup[0].__name__ == 'view_item_count' and ' count' or '')" (16:14)> -> __attr_class
                __token = 440
                try:
                    __zt_tmp = __attrs_140097247474256
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_class = _static_140097413192464('python', "'field' + (error and ' error' or '') + (tup[0].__name__ == 'view_item_count' and ' count' or '')", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_class is not None):
                    __append((' class="%s"' % __attr_class))
                __append(' >\n    ')

                # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097247472672
                __attrs_140097247472672 = _static_140097412968080
                __backup_widget_140097342774464 = get('widget', __marker)

                # <Value 'tup' (19:30)> -> __iterator
                __token = 587
                try:
                    __zt_tmp = __attrs_140097247472672
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140097413192464('path', 'tup', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                (__iterator, ____index_140097247472912, ) = getname('repeat')('widget', __iterator)
                econtext['widget'] = None
                for __item in __iterator:
                    econtext['widget'] = __item
                    __append('\n\n\n\n      ')

                    # <Static value=<ast.Dict object at 0x7f6aeeab6740> name=None at 7f6aeeab6770> -> __attrs_140097247463216
                    __attrs_140097247463216 = _static_140097247471424
                    __backup_link_140097342774992 = get('link', __marker)

                    # <Value 'python:view.context.context.link(view.getContent(), widget.field.__name__)' (25:16)> -> __value
                    __token = 651
                    try:
                        __zt_tmp = __attrs_140097247463216
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140097413192464('python', 'view.context.context.link(view.getContent(), widget.field.__name__)', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    econtext['link'] = __value
                    __backup_item_type_class_140097342770384 = get('item_type_class', __marker)

                    # <Value "python:'contenttype-' + normalize(view.getContent().id)" (26:26)> -> __value
                    __token = 753
                    try:
                        __zt_tmp = __attrs_140097247463216
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140097413192464('python', "'contenttype-' + normalize(view.getContent().id)", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    econtext['item_type_class'] = __value

                    # <Negate value=<Value "python:widget.mode == 'input' or link is None" (28:23)> at 7f6aeeab6f20> -> __cache_140097247473440

                    # <Value "python:widget.mode == 'input' or link is None" (28:23)> -> __cache_140097247473440
                    __token = 845
                    try:
                        __zt_tmp = __attrs_140097247463216
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140097247473440 = _static_140097413192464('python', "widget.mode == 'input' or link is None", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    __cache_140097247473440 = not __cache_140097247473440
                    __condition = __cache_140097247473440
                    if __condition:

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append('<a')

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097247471232
                        __default_140097247471232 = _DEFAULT_MARKER

                        # <Substitution 'link' (30:16)> -> __attr_href
                        __token = 934
                        try:
                            __zt_tmp = __attrs_140097247463216
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_140097413192464('path', 'link', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((' href="%s"' % __attr_href))

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097247471952
                        __default_140097247471952 = _DEFAULT_MARKER

                        # <Substitution 'string:$item_type_class' (31:16)> -> __attr_class
                        __token = 956
                        try:
                            __zt_tmp = __attrs_140097247463216
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_class = _static_140097413192464('string', '$item_type_class', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_class is not None):
                            __append((' class="%s"' % __attr_class))
                        __append(' >')
                    __append('\n\n        ')

                    # <Static value=<ast.Dict object at 0x7f6aeeab48b0> name=None at 7f6aeeab4a30> -> __attrs_140097247464800
                    __attrs_140097247464800 = _static_140097247463600

                    # <Negate value=<Value 'not:error' (36:28)> at 7f6aeeab4ac0> -> __cache_140097247464128

                    # <Value 'not:error' (36:28)> -> __cache_140097247464128
                    __token = 1058
                    try:
                        __zt_tmp = __attrs_140097247464800
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140097247464128 = _static_140097413192464('not', 'error', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    __cache_140097247464128 = not __cache_140097247464128
                    __condition = __cache_140097247464128
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="error" >')
                    __append('\n          ')

                    # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097247467440
                    __attrs_140097247467440 = _static_140097412968080

                    # <Value 'error' (38:30)> -> __condition
                    __token = 1109
                    try:
                        __zt_tmp = __attrs_140097247467440
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140097413192464('path', 'error', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    if __condition:

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097247468688
                        __default_140097247468688 = _DEFAULT_MARKER

                        # <Value 'error/render' (39:38)> -> __cache_140097247469072
                        __token = 1154
                        try:
                            __zt_tmp = __attrs_140097247467440
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140097247469072 = _static_140097413192464('path', 'error/render', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                        # <BinOp left=<Value 'error/render' (39:38)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeeab4fa0> -> __condition
                        __expression = __cache_140097247469072

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append('<div ></div>')
                        else:
                            __content = __cache_140097247469072
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                    __append('\n          ')

                    # <Static value=<ast.Dict object at 0x7f6aeeab5960> name=None at 7f6aeeab5f00> -> __attrs_140097247461440
                    __attrs_140097247461440 = _static_140097247467872

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097247462976
                    __default_140097247462976 = _DEFAULT_MARKER

                    # <Value 'widget/render' (42:40)> -> __cache_140097247468832
                    __token = 1255
                    try:
                        __zt_tmp = __attrs_140097247461440
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140097247468832 = _static_140097413192464('path', 'widget/render', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                    # <BinOp left=<Value 'widget/render' (42:40)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeeab5c00> -> __condition
                    __expression = __cache_140097247468832

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input type="text" />')
                    else:
                        __content = __cache_140097247468832
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('\n        ')
                    __condition = __cache_140097247464128
                    if __condition:
                        __append('</span>')
                    __append('\n\n      ')
                    __condition = __cache_140097247473440
                    if __condition:
                        __append('</a>')
                    if (__backup_item_type_class_140097342770384 is __marker):
                        del econtext['item_type_class']
                    else:
                        econtext['item_type_class'] = __backup_item_type_class_140097342770384
                    if (__backup_link_140097342774992 is __marker):
                        del econtext['link']
                    else:
                        econtext['link'] = __backup_link_140097342774992
                    __append('\n    ')
                    ____index_140097247472912 -= 1
                    if (____index_140097247472912 > 0):
                        __append('')
                if (__backup_widget_140097342774464 is __marker):
                    del econtext['widget']
                else:
                    econtext['widget'] = __backup_widget_140097342774464
                __append('\n\n  </td>')
                if (__backup_normalize_140097342773024 is __marker):
                    del econtext['normalize']
                else:
                    econtext['normalize'] = __backup_normalize_140097342773024
                if (__backup_idx_140097342767312 is __marker):
                    del econtext['idx']
                else:
                    econtext['idx'] = __backup_idx_140097342767312
                if (__backup_error_140097342775328 is __marker):
                    del econtext['error']
                else:
                    econtext['error'] = __backup_error_140097342775328
                __append('\n')
                ____index_140097247476800 -= 1
                if (____index_140097247476800 > 0):
                    __append('')
            if (__backup_tup_140097342771152 is __marker):
                del econtext['tup']
            else:
                econtext['tup'] = __backup_tup_140097342771152
            if (__backup_niceTitles_140097342770480 is __marker):
                del econtext['niceTitles']
            else:
                econtext['niceTitles'] = __backup_niceTitles_140097342770480
            if (__backup_layout_140097252390176 is __marker):
                del econtext['layout']
            else:
                econtext['layout'] = __backup_layout_140097252390176
            if (__backup_portal_140097342775280 is __marker):
                del econtext['portal']
            else:
                econtext['portal'] = __backup_portal_140097342775280
            if (__backup_tups_140097342776768 is __marker):
                del econtext['tups']
            else:
                econtext['tups'] = __backup_tups_140097342776768
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }