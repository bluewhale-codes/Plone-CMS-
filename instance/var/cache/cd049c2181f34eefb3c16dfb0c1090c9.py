# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/plone/app/portlets/portlets/navigation_recurse.pt'

__tokens = {583: ('context/@@plone_portal_state/portal', 16, 23), 647: (' portal/@@image_scal', 17, 27), 720: ('children', 20, 30), 782: ('node/show_children', 22, 28), 829: (' node/childre', 23, 27), 871: ('  node/getU', 24, 26), 911: ('rl node/getRemote', 25, 25), 957: ('rl  node/useRemoteUrl | not', 26, 24), 1013: ('     node/portal', 27, 23), 1058: ('      nod', 28, 22), 1096: ('       item/', 29, 21), 1137: ('nt      node/cur', 30, 20), 1182: ('ath      node/curr', 31, 19), 1229: ("ss        python:' navTreeCurrentNode' if is_curre", 32, 18), 1308: ("tr_class   python:' navTreeItemInPath' if is_in_p", 33, 17), 1386: ("older_class python:' navTreeFolderish' if show_chil", 34, 16), 1488: ('python:bottomLevel &lt;= 0 or level &lt;= botto', 36, 25), 1588: ('string:navTreeItem visualNoMarker${li_class}${li_extr_class}${li_folder_class} section-${node/normalized_id}', 38, 18), 1779: ('string:state-${node/normalized_review_state}', 43, 32), 1861: (" python:'contenttype-%s' % normalizeString(item_type) if not supress_icon else '", 44, 36), 1974: ("s python:'%s navTreeCurrentItem' % item_class if is_current else item_cla", 45, 30), 2125: ('python:item_remote_url if use_remote_url else item_url', 49, 21), 2201: (' node/Descriptio', 50, 20), 2239: ('s string:${item_class}${li_class}${li_extr_class}${li_folder_class} ${item_type_clas', 51, 19), 2381: ("python: not supress_icon and item_type != 'File'", 54, 37), 2476: ("python:icons.tag(f'contenttype/{normalizeString(item_type)}')", 55, 45), 2592: ("python: not supress_icon and item_type == 'File'", 58, 37), 2687: ("python:icons.tag(f'mimetype-{item.mime_type}')", 59, 45), 2783: ('python:has_thumb and thumb_scale', 62, 32), 2857: ("python:image_scale.tag(item, 'image', scale=thumb_scale, css_class='float-end thumb-'+thumb_scale)", 63, 40), 3004: ('node/Title', 66, 31), 3093: ('children', 68, 35), 3135: ('python: children and show_children and bottomLevel and level &lt; bottomLevel or bottomLevel =', 69, 31), 3291: ('string:navTree navTreeLevel${level}', 71, 24), 3403: ('python:view.recurse(children=children, level=level+1, bottomLevel=bottomLevel)', 74, 43), 41: ('options/level | python:0', 2, 20), 89: (' options/children | nothin', 3, 22), 142: ('l options/bottomLevel | nothi', 4, 24), 202: ('   view/data/no_ic', 5, 27), 251: ('b   view/data/no_th', 6, 26), 297: ('cale view/thumb_', 7, 21), 334: ('icons nocall:context/@@iconre', 8, 14), 394: ('String nocall: context/plone_utils/normaliz', 9, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140097252733856 = {'class': 'string:navTree navTreeLevel${level}', }
_static_140097342775808 = {'href': 'python:item_remote_url if use_remote_url else item_url', 'title': 'node/Description', 'class': 'string:${item_class}${li_class}${li_extr_class}${li_folder_class} ${item_type_class}', }
_static_140097339173632 = {'class': 'string:navTreeItem visualNoMarker${li_class}${li_extr_class}${li_folder_class} section-${node/normalized_id}', }
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

    def render_nav_main(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097364939664
            __attrs_140097364939664 = _static_140097412968080
            __backup_portal_140097339069856 = get('portal', __marker)

            # <Value 'context/@@plone_portal_state/portal' (16:23)> -> __value
            __token = 583
            try:
                __zt_tmp = __attrs_140097364939664
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('path', 'context/@@plone_portal_state/portal', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['portal'] = __value
            __backup_image_scale_140097364943744 = get('image_scale', __marker)

            # <Value 'portal/@@image_scale' (17:27)> -> __value
            __token = 647
            try:
                __zt_tmp = __attrs_140097364939664
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('path', 'portal/@@image_scale', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['image_scale'] = __value
            __append('\n    ')

            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097339172048
            __attrs_140097339172048 = _static_140097412968080
            __backup_node_140097339164848 = get('node', __marker)

            # <Value 'children' (20:30)> -> __iterator
            __token = 720
            try:
                __zt_tmp = __attrs_140097339172048
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140097413192464('path', 'children', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            (__iterator, ____index_140097339172000, ) = getname('repeat')('node', __iterator)
            econtext['node'] = None
            for __item in __iterator:
                econtext['node'] = __item
                __append('\n      ')

                # <Static value=<ast.Dict object at 0x7f6af422ab00> name=None at 7f6af4229ff0> -> __attrs_140097339177136
                __attrs_140097339177136 = _static_140097339173632
                __backup_show_children_140097339175264 = get('show_children', __marker)

                # <Value 'node/show_children' (22:28)> -> __value
                __token = 782
                try:
                    __zt_tmp = __attrs_140097339177136
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140097413192464('path', 'node/show_children', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                econtext['show_children'] = __value
                __backup_children_140097339172960 = get('children', __marker)

                # <Value 'node/children' (23:27)> -> __value
                __token = 829
                try:
                    __zt_tmp = __attrs_140097339177136
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140097413192464('path', 'node/children', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                econtext['children'] = __value
                __backup_item_url_140097339175024 = get('item_url', __marker)

                # <Value 'node/getURL' (24:26)> -> __value
                __token = 871
                try:
                    __zt_tmp = __attrs_140097339177136
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140097413192464('path', 'node/getURL', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                econtext['item_url'] = __value
                __backup_item_remote_url_140097339173488 = get('item_remote_url', __marker)

                # <Value 'node/getRemoteUrl' (25:25)> -> __value
                __token = 911
                try:
                    __zt_tmp = __attrs_140097339177136
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140097413192464('path', 'node/getRemoteUrl', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                econtext['item_remote_url'] = __value
                __backup_use_remote_url_140097339174112 = get('use_remote_url', __marker)

                # <Value 'node/useRemoteUrl | nothing' (26:24)> -> __value
                __token = 957
                try:
                    __zt_tmp = __attrs_140097339177136
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140097413192464('path', 'node/useRemoteUrl | nothing', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                econtext['use_remote_url'] = __value
                __backup_item_type_140097339174544 = get('item_type', __marker)

                # <Value 'node/portal_type' (27:23)> -> __value
                __token = 1013
                try:
                    __zt_tmp = __attrs_140097339177136
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140097413192464('path', 'node/portal_type', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                econtext['item_type'] = __value
                __backup_item_140097339176656 = get('item', __marker)

                # <Value 'node/item' (28:22)> -> __value
                __token = 1058
                try:
                    __zt_tmp = __attrs_140097339177136
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140097413192464('path', 'node/item', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                econtext['item'] = __value
                __backup_has_thumb_140097339175888 = get('has_thumb', __marker)

                # <Value 'item/getIcon' (29:21)> -> __value
                __token = 1096
                try:
                    __zt_tmp = __attrs_140097339177136
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140097413192464('path', 'item/getIcon', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                econtext['has_thumb'] = __value
                __backup_is_current_140097339172768 = get('is_current', __marker)

                # <Value 'node/currentItem' (30:20)> -> __value
                __token = 1137
                try:
                    __zt_tmp = __attrs_140097339177136
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140097413192464('path', 'node/currentItem', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                econtext['is_current'] = __value
                __backup_is_in_path_140097339171904 = get('is_in_path', __marker)

                # <Value 'node/currentParent' (31:19)> -> __value
                __token = 1182
                try:
                    __zt_tmp = __attrs_140097339177136
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140097413192464('path', 'node/currentParent', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                econtext['is_in_path'] = __value
                __backup_li_class_140097339163600 = get('li_class', __marker)

                # <Value "python:' navTreeCurrentNode' if is_current else ''" (32:18)> -> __value
                __token = 1229
                try:
                    __zt_tmp = __attrs_140097339177136
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140097413192464('python', "' navTreeCurrentNode' if is_current else ''", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                econtext['li_class'] = __value
                __backup_li_extr_class_140097339177184 = get('li_extr_class', __marker)

                # <Value "python:' navTreeItemInPath' if is_in_path else ''" (33:17)> -> __value
                __token = 1308
                try:
                    __zt_tmp = __attrs_140097339177136
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140097413192464('python', "' navTreeItemInPath' if is_in_path else ''", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                econtext['li_extr_class'] = __value
                __backup_li_folder_class_140097342773168 = get('li_folder_class', __marker)

                # <Value "python:' navTreeFolderish' if show_children else ''" (34:16)> -> __value
                __token = 1386
                try:
                    __zt_tmp = __attrs_140097339177136
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140097413192464('python', "' navTreeFolderish' if show_children else ''", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                econtext['li_folder_class'] = __value

                # <Value 'python:bottomLevel <= 0 or level <= bottomLevel' (36:25)> -> __condition
                __token = 1488
                try:
                    __zt_tmp = __attrs_140097339177136
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140097413192464('python', 'bottomLevel <= 0 or level <= bottomLevel', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                if __condition:

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append('<li')

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097339163408
                    __default_140097339163408 = _DEFAULT_MARKER

                    # <Substitution 'string:navTreeItem visualNoMarker${li_class}${li_extr_class}${li_folder_class} section-${node/normalized_id}' (38:18)> -> __attr_class
                    __token = 1588
                    try:
                        __zt_tmp = __attrs_140097339177136
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_140097413192464('string', 'navTreeItem visualNoMarker${li_class}${li_extr_class}${li_folder_class} section-${node/normalized_id}', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((' class="%s"' % __attr_class))
                    __append(' >\n\n        ')

                    # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097342775568
                    __attrs_140097342775568 = _static_140097412968080
                    __backup_item_class_140097342776432 = get('item_class', __marker)

                    # <Value 'string:state-${node/normalized_review_state}' (43:32)> -> __value
                    __token = 1779
                    try:
                        __zt_tmp = __attrs_140097342775568
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140097413192464('string', 'state-${node/normalized_review_state}', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    econtext['item_class'] = __value
                    __backup_item_type_class_140097342768464 = get('item_type_class', __marker)

                    # <Value "python:'contenttype-%s' % normalizeString(item_type) if not supress_icon else ''" (44:36)> -> __value
                    __token = 1861
                    try:
                        __zt_tmp = __attrs_140097342775568
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140097413192464('python', "'contenttype-%s' % normalizeString(item_type) if not supress_icon else ''", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    econtext['item_type_class'] = __value
                    __backup_item_class_140097337742944 = get('item_class', __marker)

                    # <Value "python:'%s navTreeCurrentItem' % item_class if is_current else item_class" (45:30)> -> __value
                    __token = 1974
                    try:
                        __zt_tmp = __attrs_140097342775568
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140097413192464('python', "'%s navTreeCurrentItem' % item_class if is_current else item_class", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    econtext['item_class'] = __value
                    __append('\n\n          ')

                    # <Static value=<ast.Dict object at 0x7f6af459a200> name=None at 7f6af4599150> -> __attrs_140097252729536
                    __attrs_140097252729536 = _static_140097342775808

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252726656
                    __default_140097252726656 = _DEFAULT_MARKER

                    # <Substitution 'python:item_remote_url if use_remote_url else item_url' (49:21)> -> __attr_href
                    __token = 2125
                    try:
                        __zt_tmp = __attrs_140097252729536
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140097413192464('python', 'item_remote_url if use_remote_url else item_url', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252725888
                    __default_140097252725888 = _DEFAULT_MARKER

                    # <Substitution 'node/Description' (50:20)> -> __attr_title
                    __token = 2201
                    try:
                        __zt_tmp = __attrs_140097252729536
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_title = _static_140097413192464('path', 'node/Description', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_title is not None):
                        __append((' title="%s"' % __attr_title))

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252732224
                    __default_140097252732224 = _DEFAULT_MARKER

                    # <Substitution 'string:${item_class}${li_class}${li_extr_class}${li_folder_class} ${item_type_class}' (51:19)> -> __attr_class
                    __token = 2239
                    try:
                        __zt_tmp = __attrs_140097252729536
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_140097413192464('string', '${item_class}${li_class}${li_extr_class}${li_folder_class} ${item_type_class}', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((' class="%s"' % __attr_class))
                    __append('>\n\n            ')

                    # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097252734432
                    __attrs_140097252734432 = _static_140097412968080

                    # <Value "python: not supress_icon and item_type != 'File'" (54:37)> -> __condition
                    __token = 2381
                    try:
                        __zt_tmp = __attrs_140097252734432
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140097413192464('python', " not supress_icon and item_type != 'File'", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    if __condition:

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252734720
                        __default_140097252734720 = _DEFAULT_MARKER

                        # <Value "python:icons.tag(f'contenttype/{normalizeString(item_type)}')" (55:45)> -> __cache_140097252736640
                        __token = 2476
                        try:
                            __zt_tmp = __attrs_140097252734432
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140097252736640 = _static_140097413192464('python', "icons.tag(f'contenttype/{normalizeString(item_type)}')", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                        # <BinOp left=<Value "python:icons.tag(f'contenttype/{normalizeString(item_type)}')" (55:45)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeefbb8b0> -> __condition
                        __expression = __cache_140097252736640

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140097252736640
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                    __append('\n\n            ')

                    # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097252736880
                    __attrs_140097252736880 = _static_140097412968080

                    # <Value "python: not supress_icon and item_type == 'File'" (58:37)> -> __condition
                    __token = 2592
                    try:
                        __zt_tmp = __attrs_140097252736880
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140097413192464('python', " not supress_icon and item_type == 'File'", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    if __condition:

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252731936
                        __default_140097252731936 = _DEFAULT_MARKER

                        # <Value "python:icons.tag(f'mimetype-{item.mime_type}')" (59:45)> -> __cache_140097252735776
                        __token = 2687
                        try:
                            __zt_tmp = __attrs_140097252736880
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140097252735776 = _static_140097413192464('python', "icons.tag(f'mimetype-{item.mime_type}')", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                        # <BinOp left=<Value "python:icons.tag(f'mimetype-{item.mime_type}')" (59:45)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeefbb9d0> -> __condition
                        __expression = __cache_140097252735776

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140097252735776
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                    __append('\n\n            ')

                    # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097252732272
                    __attrs_140097252732272 = _static_140097412968080

                    # <Value 'python:has_thumb and thumb_scale' (62:32)> -> __condition
                    __token = 2783
                    try:
                        __zt_tmp = __attrs_140097252732272
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140097413192464('python', 'has_thumb and thumb_scale', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    if __condition:

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252731360
                        __default_140097252731360 = _DEFAULT_MARKER

                        # <Value "python:image_scale.tag(item, 'image', scale=thumb_scale, css_class='float-end thumb-'+thumb_scale)" (63:40)> -> __cache_140097252731168
                        __token = 2857
                        try:
                            __zt_tmp = __attrs_140097252732272
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140097252731168 = _static_140097413192464('python', "image_scale.tag(item, 'image', scale=thumb_scale, css_class='float-end thumb-'+thumb_scale)", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                        # <BinOp left=<Value "python:image_scale.tag(item, 'image', scale=thumb_scale, css_class='float-end thumb-'+thumb_scale)" (63:40)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeefb9d80> -> __condition
                        __expression = __cache_140097252731168

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <img ... (0:0)
                            # --------------------------------------------------------
                            __append('<img />')
                        else:
                            __content = __cache_140097252731168
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                    __append('\n\n            ')

                    # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097252730976
                    __attrs_140097252730976 = _static_140097412968080

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252725840
                    __default_140097252725840 = _DEFAULT_MARKER

                    # <Value 'node/Title' (66:31)> -> __cache_140097252732512
                    __token = 3004
                    try:
                        __zt_tmp = __attrs_140097252730976
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140097252732512 = _static_140097413192464('path', 'node/Title', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                    # <BinOp left=<Value 'node/Title' (66:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeefb9090> -> __condition
                    __expression = __cache_140097252732512

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>Selected Item Title</span>')
                    else:
                        __content = __cache_140097252732512
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('\n          </a>\n          ')

                    # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097252730016
                    __attrs_140097252730016 = _static_140097412968080

                    # <Value 'children' (68:35)> -> __condition
                    __token = 3093
                    try:
                        __zt_tmp = __attrs_140097252730016
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140097413192464('path', 'children', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    if __condition:
                        __append('\n            ')

                        # <Static value=<ast.Dict object at 0x7f6aeefbb3a0> name=None at 7f6aeefbb370> -> __attrs_140097252729200
                        __attrs_140097252729200 = _static_140097252733856

                        # <Value 'python: children and show_children and bottomLevel and level < bottomLevel or bottomLevel == 0' (69:31)> -> __condition
                        __token = 3135
                        try:
                            __zt_tmp = __attrs_140097252729200
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140097413192464('python', ' children and show_children and bottomLevel and level < bottomLevel or bottomLevel == 0', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        if __condition:

                            # <ul ... (0:0)
                            # --------------------------------------------------------
                            __append('<ul')

                            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252733904
                            __default_140097252733904 = _DEFAULT_MARKER

                            # <Substitution 'string:navTree navTreeLevel${level}' (71:24)> -> __attr_class
                            __token = 3291
                            try:
                                __zt_tmp = __attrs_140097252729200
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_class = _static_140097413192464('string', 'navTree navTreeLevel${level}', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                            if (__attr_class is not None):
                                __append((' class="%s"' % __attr_class))
                            __append(' >\n              ')

                            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097252724256
                            __attrs_140097252724256 = _static_140097412968080

                            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252726272
                            __default_140097252726272 = _DEFAULT_MARKER

                            # <Value 'python:view.recurse(children=children, level=level+1, bottomLevel=bottomLevel)' (74:43)> -> __cache_140097252725216
                            __token = 3403
                            try:
                                __zt_tmp = __attrs_140097252724256
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140097252725216 = _static_140097413192464('python', 'view.recurse(children=children, level=level+1, bottomLevel=bottomLevel)', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                            # <BinOp left=<Value 'python:view.recurse(children=children, level=level+1, bottomLevel=bottomLevel)' (74:43)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeefb90f0> -> __condition
                            __expression = __cache_140097252725216

                            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:

                                # <span ... (0:0)
                                # --------------------------------------------------------
                                __append('<span></span>')
                            else:
                                __content = __cache_140097252725216
                                __content = __convert(__content)
                                if (__content is not None):
                                    __append(__content)
                            __append('\n            </ul>')
                        __append('\n          ')
                    __append('\n\n        ')
                    if (__backup_item_class_140097337742944 is __marker):
                        del econtext['item_class']
                    else:
                        econtext['item_class'] = __backup_item_class_140097337742944
                    if (__backup_item_type_class_140097342768464 is __marker):
                        del econtext['item_type_class']
                    else:
                        econtext['item_type_class'] = __backup_item_type_class_140097342768464
                    if (__backup_item_class_140097342776432 is __marker):
                        del econtext['item_class']
                    else:
                        econtext['item_class'] = __backup_item_class_140097342776432
                    __append('\n      </li>')
                if (__backup_li_folder_class_140097342773168 is __marker):
                    del econtext['li_folder_class']
                else:
                    econtext['li_folder_class'] = __backup_li_folder_class_140097342773168
                if (__backup_li_extr_class_140097339177184 is __marker):
                    del econtext['li_extr_class']
                else:
                    econtext['li_extr_class'] = __backup_li_extr_class_140097339177184
                if (__backup_li_class_140097339163600 is __marker):
                    del econtext['li_class']
                else:
                    econtext['li_class'] = __backup_li_class_140097339163600
                if (__backup_is_in_path_140097339171904 is __marker):
                    del econtext['is_in_path']
                else:
                    econtext['is_in_path'] = __backup_is_in_path_140097339171904
                if (__backup_is_current_140097339172768 is __marker):
                    del econtext['is_current']
                else:
                    econtext['is_current'] = __backup_is_current_140097339172768
                if (__backup_has_thumb_140097339175888 is __marker):
                    del econtext['has_thumb']
                else:
                    econtext['has_thumb'] = __backup_has_thumb_140097339175888
                if (__backup_item_140097339176656 is __marker):
                    del econtext['item']
                else:
                    econtext['item'] = __backup_item_140097339176656
                if (__backup_item_type_140097339174544 is __marker):
                    del econtext['item_type']
                else:
                    econtext['item_type'] = __backup_item_type_140097339174544
                if (__backup_use_remote_url_140097339174112 is __marker):
                    del econtext['use_remote_url']
                else:
                    econtext['use_remote_url'] = __backup_use_remote_url_140097339174112
                if (__backup_item_remote_url_140097339173488 is __marker):
                    del econtext['item_remote_url']
                else:
                    econtext['item_remote_url'] = __backup_item_remote_url_140097339173488
                if (__backup_item_url_140097339175024 is __marker):
                    del econtext['item_url']
                else:
                    econtext['item_url'] = __backup_item_url_140097339175024
                if (__backup_children_140097339172960 is __marker):
                    del econtext['children']
                else:
                    econtext['children'] = __backup_children_140097339172960
                if (__backup_show_children_140097339175264 is __marker):
                    del econtext['show_children']
                else:
                    econtext['show_children'] = __backup_show_children_140097339175264
                __append('\n    ')
                ____index_140097339172000 -= 1
                if (____index_140097339172000 > 0):
                    __append('')
            if (__backup_node_140097339164848 is __marker):
                del econtext['node']
            else:
                econtext['node'] = __backup_node_140097339164848
            __append('\n  ')
            if (__backup_image_scale_140097364943744 is __marker):
                del econtext['image_scale']
            else:
                econtext['image_scale'] = __backup_image_scale_140097364943744
            if (__backup_portal_140097339069856 is __marker):
                del econtext['portal']
            else:
                econtext['portal'] = __backup_portal_140097339069856
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


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

            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097339074800
            __attrs_140097339074800 = _static_140097412968080
            __backup_level_140097344089552 = get('level', __marker)

            # <Value 'options/level | python:0' (2:20)> -> __value
            __token = 41
            try:
                __zt_tmp = __attrs_140097339074800
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('path', 'options/level | python:0', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['level'] = __value
            __backup_children_140097344080768 = get('children', __marker)

            # <Value 'options/children | nothing' (3:22)> -> __value
            __token = 89
            try:
                __zt_tmp = __attrs_140097339074800
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('path', 'options/children | nothing', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['children'] = __value
            __backup_bottomLevel_140097344090800 = get('bottomLevel', __marker)

            # <Value 'options/bottomLevel | nothing' (4:24)> -> __value
            __token = 142
            try:
                __zt_tmp = __attrs_140097339074800
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('path', 'options/bottomLevel | nothing', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['bottomLevel'] = __value
            __backup_supress_icon_140097339075088 = get('supress_icon', __marker)

            # <Value 'view/data/no_icons' (5:27)> -> __value
            __token = 202
            try:
                __zt_tmp = __attrs_140097339074800
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('path', 'view/data/no_icons', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['supress_icon'] = __value
            __backup_supress_thumb_140097339067600 = get('supress_thumb', __marker)

            # <Value 'view/data/no_thumbs' (6:26)> -> __value
            __token = 251
            try:
                __zt_tmp = __attrs_140097339074800
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('path', 'view/data/no_thumbs', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['supress_thumb'] = __value
            __backup_thumb_scale_140097339073120 = get('thumb_scale', __marker)

            # <Value 'view/thumb_scale' (7:21)> -> __value
            __token = 297
            try:
                __zt_tmp = __attrs_140097339074800
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('path', 'view/thumb_scale', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['thumb_scale'] = __value
            __backup_icons_140097339072736 = get('icons', __marker)

            # <Value 'nocall:context/@@iconresolver' (8:14)> -> __value
            __token = 334
            try:
                __zt_tmp = __attrs_140097339074800
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('nocall', 'context/@@iconresolver', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['icons'] = __value
            __backup_normalizeString_140097339073504 = get('normalizeString', __marker)

            # <Value 'nocall: context/plone_utils/normalizeString' (9:23)> -> __value
            __token = 394
            try:
                __zt_tmp = __attrs_140097339074800
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('nocall', ' context/plone_utils/normalizeString', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['normalizeString'] = __value
            __previous_i18n_domain_140097364943648 = __i18n_domain
            __i18n_domain = 'plone'
            __append('\n\n  ')
            __token = None
            render_nav_main(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n')
            __i18n_domain = __previous_i18n_domain_140097364943648
            if (__backup_normalizeString_140097339073504 is __marker):
                del econtext['normalizeString']
            else:
                econtext['normalizeString'] = __backup_normalizeString_140097339073504
            if (__backup_icons_140097339072736 is __marker):
                del econtext['icons']
            else:
                econtext['icons'] = __backup_icons_140097339072736
            if (__backup_thumb_scale_140097339073120 is __marker):
                del econtext['thumb_scale']
            else:
                econtext['thumb_scale'] = __backup_thumb_scale_140097339073120
            if (__backup_supress_thumb_140097339067600 is __marker):
                del econtext['supress_thumb']
            else:
                econtext['supress_thumb'] = __backup_supress_thumb_140097339067600
            if (__backup_supress_icon_140097339075088 is __marker):
                del econtext['supress_icon']
            else:
                econtext['supress_icon'] = __backup_supress_icon_140097339075088
            if (__backup_bottomLevel_140097344090800 is __marker):
                del econtext['bottomLevel']
            else:
                econtext['bottomLevel'] = __backup_bottomLevel_140097344090800
            if (__backup_children_140097344080768 is __marker):
                del econtext['children']
            else:
                econtext['children'] = __backup_children_140097344080768
            if (__backup_level_140097344089552 is __marker):
                del econtext['level']
            else:
                econtext['level'] = __backup_level_140097344089552
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_nav_main': render_nav_main, 'render': render, }