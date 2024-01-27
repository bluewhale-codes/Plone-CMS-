# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/plone/app/dexterity/browser/folder_listing.pt'

__tokens = {558: ('view/batch', 17, 31), 632: ('batch', 19, 36), 6274: ('context/batch_macros/macros/navigation', 127, 36), 6274: ('context/batch_macros/macros/navigation', 127, 36), 6482: ('not: view/batch', 133, 32), 6529: ('view/no_items_message', 134, 30), 836: ('batch', 24, 41), 938: ('item/getObject', 27, 35), 993: (' item/getUR', 28, 39), 1044: ('d item/get', 29, 37), 1097: ('le item/Ti', 30, 39), 1156: ('ion item/Descrip', 31, 44), 1214: ('type item/Porta', 32, 36), 1275: ('ified item/Modificati', 33, 39), 1341: ('reated item/Creat', 34, 37), 1406: ("e_class python:'contenttype-' + view.normalizeString(it", 35, 39), 1507: ('wf_state item/rev', 36, 36), 1576: ("ate_class python:'state-' + view.normalizeString(item", 37, 41), 1674: ('em_creator i', 38, 33), 1728: ("  item_link python:item_type in view.use_view_action and item_url+'/view'", 39, 29), 1848: ('em_has_image python', 40, 33), 5924: ('item_description', 116, 42), 5982: ('item_description', 117, 40), 2214: ('item_type', 47, 40), 2373: ('item_link', 51, 38), 2522: ('item_has_image', 54, 50), 2632: ('string:$item_url/@@images/image/tile', 56, 42), 2934: ('item_link', 62, 38), 2983: (' string:$item_type_class $item_wf_state_class ur', 63, 38), 3071: ('e item_ty', 64, 37), 2817: ('python: item_title or item_id', 60, 44), 3442: ('view/show_about', 73, 53), 3600: ('python:view.pas_member.info(item_creator)', 76, 51), 3705: (' author/usernam', 77, 62), 3783: ('m string:?author=${author/usernam', 78, 60), 3879: ("id python:'/' in creator_short_f", 79, 59), 3967: ('_id python:(creator_short_form, creator_long_form)[creator_is_ope', 80, 51), 4139: ('item_creator', 82, 57), 4416: ('not:author', 87, 53), 4530: ('string:${view/navigation_root_url}/author/${item_creator}', 89, 46), 4344: ('author/name_or_id', 86, 52), 5135: ('python:view.toLocalizedTime(item_modified,long_format=1)', 101, 53), 5482: ('nothing', 107, 56), 247: ('context/@@main_template/macros/master', 6, 23), 247: ('context/@@main_template/macros/master', 6, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from collections import deque as _deque
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140533348694624 = 'master'
_static_140533345865920 = {'href': 'string:${view/navigation_root_url}/author/${item_creator}', }
_static_140533345866352 = {'class': 'documentByLine', }
_static_140533343892768 = {'href': 'item_link', 'class': 'string:$item_type_class $item_wf_state_class url', 'title': 'item_type', }
_static_140533343889312 = {'class': 'image-tile', 'src': 'string:$item_url/@@images/image/tile', }
_static_140533343886960 = {'href': 'item_link', }
_static_140533343881248 = {'class': 'summary', 'title': 'item_type', }
_static_140533345863280 = {'class': 'description discreet', }
_static_140533343883552 = {'class': 'entry', }
_static_140533344129072 = {'class': 'discreet', }
_static_140533344468272 = 'navigation'
_static_140533344453488 = {'class': 'entries', }
_static_140533417024992 = __C2ZContextWrapper
_static_140533417025280 = __compile_zt_expr
_static_140533416833664 = {}

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

    def render_content_core(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533343895952
            __attrs_140533343895952 = _static_140533416833664
            __append('\n\n        ')
            __token = None
            render_listing(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n\n      ')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_listing(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __slot_no_items_in_listing = econtext['__slot_no_items_in_listing'].pop()
        except:
            __slot_no_items_in_listing = None

        try:
            __slot_entries = econtext['__slot_entries'].pop()
        except:
            __slot_entries = None

        try:
            getname = econtext.get_name
            get = econtext.get

            # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533344466496
            __attrs_140533344466496 = _static_140533416833664
            __append('\n          ')

            # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533344455360
            __attrs_140533344455360 = _static_140533416833664
            __backup_batch_140533343903584 = get('batch', __marker)

            # <Value 'view/batch' (17:31)> -> __value
            __token = 558
            try:
                __zt_tmp = __attrs_140533344455360
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140533417025280('path', 'view/batch', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
            econtext['batch'] = __value
            __append('\n            ')

            # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533344456992
            __attrs_140533344456992 = _static_140533416833664

            # <Value 'batch' (19:36)> -> __condition
            __token = 632
            try:
                __zt_tmp = __attrs_140533344456992
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140533417025280('path', 'batch', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
            if __condition:
                __append('\n              ')
                if (__slot_entries is None):

                    # <Static value=<ast.Dict object at 0x7fd078134370> name=None at 7fd078134310> -> __attrs_140533344454016
                    __attrs_140533344454016 = _static_140533344453488

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="entries" >\n                ')
                    __token = None
                    render_entries(__stream, econtext.copy(), rcontext, __i18n_domain)
                    econtext.update(rcontext)
                    __append('\n              </div>')
                else:
                    __slot_entries(__stream, econtext.copy(), rcontext)
                __append('\n\n              ')

                # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533344458096
                __attrs_140533344458096 = _static_140533416833664
                __backup_macroname_140533255699200 = get('macroname', __marker)

                # <Static value=<ast.Constant object at 0x7fd078137d30> name=None at 7fd0781348b0> -> __value
                __value = _static_140533344468272
                econtext['macroname'] = __value

                # <Value 'context/batch_macros/macros/navigation' (127:36)> -> __macro
                __token = 6274
                try:
                    __zt_tmp = __attrs_140533344458096
                except get('NameError', NameError):
                    __zt_tmp = None

                __macro = _static_140533417025280('path', 'context/batch_macros/macros/navigation', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                __token = 6274
                __m = __macro.include
                __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                if (__backup_macroname_140533255699200 is __marker):
                    del econtext['macroname']
                else:
                    econtext['macroname'] = __backup_macroname_140533255699200
                __append('\n\n            ')
            __append('\n\n            ')
            if (__slot_no_items_in_listing is None):

                # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533343882016
                __attrs_140533343882016 = _static_140533416833664
                __append('\n              ')

                # <Static value=<ast.Dict object at 0x7fd0780e5030> name=None at 7fd0780e6590> -> __attrs_140533344125808
                __attrs_140533344125808 = _static_140533344129072

                # <Value 'not: view/batch' (133:32)> -> __condition
                __token = 6482
                try:
                    __zt_tmp = __attrs_140533344125808
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140533417025280('not', ' view/batch', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                if __condition:

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append('<p class="discreet" >')

                    # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533344130896
                    __default_140533344130896 = _DEFAULT_MARKER

                    # <Value 'view/no_items_message' (134:30)> -> __cache_140533344127056
                    __token = 6529
                    try:
                        __zt_tmp = __attrs_140533344125808
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140533344127056 = _static_140533417025280('path', 'view/no_items_message', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))

                    # <BinOp left=<Value 'view/no_items_message' (134:30)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fd07c5afbe0> at 7fd0780e7e80> -> __condition
                    __expression = __cache_140533344127056

                    # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n          There are currently no items in this folder.\n              ')
                    else:
                        __content = __cache_140533344127056
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</p>')
                __append('\n            ')
            else:
                __slot_no_items_in_listing(__stream, econtext.copy(), rcontext)
            __append('\n\n          ')
            if (__backup_batch_140533343903584 is __marker):
                del econtext['batch']
            else:
                econtext['batch'] = __backup_batch_140533343903584
            __append('\n        ')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_entries(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __slot_entry = econtext['__slot_entry'].pop()
        except:
            __slot_entry = None

        try:
            getname = econtext.get_name
            get = econtext.get

            # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533344454256
            __attrs_140533344454256 = _static_140533416833664
            __backup_item_140533344454064 = get('item', __marker)

            # <Value 'batch' (24:41)> -> __iterator
            __token = 836
            try:
                __zt_tmp = __attrs_140533344454256
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140533417025280('path', 'batch', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
            (__iterator, ____index_140533344459008, ) = getname('repeat')('item', __iterator)
            econtext['item'] = None
            for __item in __iterator:
                econtext['item'] = __item
                __append('\n                  ')

                # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533344455936
                __attrs_140533344455936 = _static_140533416833664
                __backup_obj_140533344454400 = get('obj', __marker)

                # <Value 'item/getObject' (27:35)> -> __value
                __token = 938
                try:
                    __zt_tmp = __attrs_140533344455936
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140533417025280('path', 'item/getObject', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                econtext['obj'] = __value
                __backup_item_url_140533344455744 = get('item_url', __marker)

                # <Value 'item/getURL' (28:39)> -> __value
                __token = 993
                try:
                    __zt_tmp = __attrs_140533344455936
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140533417025280('path', 'item/getURL', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                econtext['item_url'] = __value
                __backup_item_id_140533344458960 = get('item_id', __marker)

                # <Value 'item/getId' (29:37)> -> __value
                __token = 1044
                try:
                    __zt_tmp = __attrs_140533344455936
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140533417025280('path', 'item/getId', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                econtext['item_id'] = __value
                __backup_item_title_140533344454160 = get('item_title', __marker)

                # <Value 'item/Title' (30:39)> -> __value
                __token = 1097
                try:
                    __zt_tmp = __attrs_140533344455936
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140533417025280('path', 'item/Title', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                econtext['item_title'] = __value
                __backup_item_description_140533344458048 = get('item_description', __marker)

                # <Value 'item/Description' (31:44)> -> __value
                __token = 1156
                try:
                    __zt_tmp = __attrs_140533344455936
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140533417025280('path', 'item/Description', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                econtext['item_description'] = __value
                __backup_item_type_140533344452816 = get('item_type', __marker)

                # <Value 'item/PortalType' (32:36)> -> __value
                __token = 1214
                try:
                    __zt_tmp = __attrs_140533344455936
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140533417025280('path', 'item/PortalType', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                econtext['item_type'] = __value
                __backup_item_modified_140533344455504 = get('item_modified', __marker)

                # <Value 'item/ModificationDate' (33:39)> -> __value
                __token = 1275
                try:
                    __zt_tmp = __attrs_140533344455936
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140533417025280('path', 'item/ModificationDate', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                econtext['item_modified'] = __value
                __backup_item_created_140533344457328 = get('item_created', __marker)

                # <Value 'item/CreationDate' (34:37)> -> __value
                __token = 1341
                try:
                    __zt_tmp = __attrs_140533344455936
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140533417025280('path', 'item/CreationDate', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                econtext['item_created'] = __value
                __backup_item_type_class_140533344468608 = get('item_type_class', __marker)

                # <Value "python:'contenttype-' + view.normalizeString(item_type)" (35:39)> -> __value
                __token = 1406
                try:
                    __zt_tmp = __attrs_140533344455936
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140533417025280('python', "'contenttype-' + view.normalizeString(item_type)", econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                econtext['item_type_class'] = __value
                __backup_item_wf_state_140533344467600 = get('item_wf_state', __marker)

                # <Value 'item/review_state' (36:36)> -> __value
                __token = 1507
                try:
                    __zt_tmp = __attrs_140533344455936
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140533417025280('path', 'item/review_state', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                econtext['item_wf_state'] = __value
                __backup_item_wf_state_class_140533344452960 = get('item_wf_state_class', __marker)

                # <Value "python:'state-' + view.normalizeString(item_wf_state)" (37:41)> -> __value
                __token = 1576
                try:
                    __zt_tmp = __attrs_140533344455936
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140533417025280('python', "'state-' + view.normalizeString(item_wf_state)", econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                econtext['item_wf_state_class'] = __value
                __backup_item_creator_140533344461120 = get('item_creator', __marker)

                # <Value 'item/Creator' (38:33)> -> __value
                __token = 1674
                try:
                    __zt_tmp = __attrs_140533344455936
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140533417025280('path', 'item/Creator', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                econtext['item_creator'] = __value
                __backup_item_link_140533344456800 = get('item_link', __marker)

                # <Value "python:item_type in view.use_view_action and item_url+'/view' or item_url" (39:29)> -> __value
                __token = 1728
                try:
                    __zt_tmp = __attrs_140533344455936
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140533417025280('python', "item_type in view.use_view_action and item_url+'/view' or item_url", econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                econtext['item_link'] = __value
                __backup_item_has_image_140533344456848 = get('item_has_image', __marker)

                # <Value 'python:item.getIcon' (40:33)> -> __value
                __token = 1848
                try:
                    __zt_tmp = __attrs_140533344455936
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140533417025280('python', 'item.getIcon', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                econtext['item_has_image'] = __value
                __append('\n                    ')
                if (__slot_entry is None):

                    # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533343883120
                    __attrs_140533343883120 = _static_140533416833664
                    __append('\n                      ')

                    # <Static value=<ast.Dict object at 0x7fd0780a9120> name=None at 7fd0780aada0> -> __attrs_140533343886816
                    __attrs_140533343886816 = _static_140533343883552

                    # <article ... (0:0)
                    # --------------------------------------------------------
                    __append('<article class="entry">\n                        ')
                    __token = None
                    render_listitem(__stream, econtext.copy(), rcontext, __i18n_domain)
                    econtext.update(rcontext)
                    __append('\n                        ')

                    # <Static value=<ast.Dict object at 0x7fd07828c670> name=None at 7fd07828f220> -> __attrs_140533344131232
                    __attrs_140533344131232 = _static_140533345863280

                    # <Value 'item_description' (116:42)> -> __condition
                    __token = 5924
                    try:
                        __zt_tmp = __attrs_140533344131232
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140533417025280('path', 'item_description', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                    if __condition:

                        # <p ... (0:0)
                        # --------------------------------------------------------
                        __append('<p class="description discreet" >')

                        # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533345875184
                        __default_140533345875184 = _DEFAULT_MARKER

                        # <Value 'item_description' (117:40)> -> __cache_140533343890944
                        __token = 5982
                        try:
                            __zt_tmp = __attrs_140533344131232
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140533343890944 = _static_140533417025280('path', 'item_description', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))

                        # <BinOp left=<Value 'item_description' (117:40)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fd07c5afbe0> at 7fd0780a89a0> -> __condition
                        __expression = __cache_140533343890944

                        # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('\n                    description\n                        ')
                        else:
                            __content = __cache_140533343890944
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</p>')
                    __append('\n                      </article>\n                    ')
                else:
                    __slot_entry(__stream, econtext.copy(), rcontext)
                __append('\n                  ')
                if (__backup_item_has_image_140533344456848 is __marker):
                    del econtext['item_has_image']
                else:
                    econtext['item_has_image'] = __backup_item_has_image_140533344456848
                if (__backup_item_link_140533344456800 is __marker):
                    del econtext['item_link']
                else:
                    econtext['item_link'] = __backup_item_link_140533344456800
                if (__backup_item_creator_140533344461120 is __marker):
                    del econtext['item_creator']
                else:
                    econtext['item_creator'] = __backup_item_creator_140533344461120
                if (__backup_item_wf_state_class_140533344452960 is __marker):
                    del econtext['item_wf_state_class']
                else:
                    econtext['item_wf_state_class'] = __backup_item_wf_state_class_140533344452960
                if (__backup_item_wf_state_140533344467600 is __marker):
                    del econtext['item_wf_state']
                else:
                    econtext['item_wf_state'] = __backup_item_wf_state_140533344467600
                if (__backup_item_type_class_140533344468608 is __marker):
                    del econtext['item_type_class']
                else:
                    econtext['item_type_class'] = __backup_item_type_class_140533344468608
                if (__backup_item_created_140533344457328 is __marker):
                    del econtext['item_created']
                else:
                    econtext['item_created'] = __backup_item_created_140533344457328
                if (__backup_item_modified_140533344455504 is __marker):
                    del econtext['item_modified']
                else:
                    econtext['item_modified'] = __backup_item_modified_140533344455504
                if (__backup_item_type_140533344452816 is __marker):
                    del econtext['item_type']
                else:
                    econtext['item_type'] = __backup_item_type_140533344452816
                if (__backup_item_description_140533344458048 is __marker):
                    del econtext['item_description']
                else:
                    econtext['item_description'] = __backup_item_description_140533344458048
                if (__backup_item_title_140533344454160 is __marker):
                    del econtext['item_title']
                else:
                    econtext['item_title'] = __backup_item_title_140533344454160
                if (__backup_item_id_140533344458960 is __marker):
                    del econtext['item_id']
                else:
                    econtext['item_id'] = __backup_item_id_140533344458960
                if (__backup_item_url_140533344455744 is __marker):
                    del econtext['item_url']
                else:
                    econtext['item_url'] = __backup_item_url_140533344455744
                if (__backup_obj_140533344454400 is __marker):
                    del econtext['obj']
                else:
                    econtext['obj'] = __backup_obj_140533344454400
                __append('\n                ')
                ____index_140533344459008 -= 1
                if (____index_140533344459008 > 0):
                    __append('')
            if (__backup_item_140533344454064 is __marker):
                del econtext['item']
            else:
                econtext['item'] = __backup_item_140533344454064
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_listitem(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533343887488
            __attrs_140533343887488 = _static_140533416833664

            # <header ... (0:0)
            # --------------------------------------------------------
            __append('<header>\n                          ')

            # <Static value=<ast.Dict object at 0x7fd0780a8820> name=None at 7fd0780a8bb0> -> __attrs_140533343880624
            __attrs_140533343880624 = _static_140533343881248

            # <span ... (0:0)
            # --------------------------------------------------------
            __append('<span class="summary"')

            # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533343880480
            __default_140533343880480 = _DEFAULT_MARKER

            # <Substitution 'item_type' (47:40)> -> __attr_title
            __token = 2214
            try:
                __zt_tmp = __attrs_140533343880624
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_title = _static_140533417025280('path', 'item_type', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
            __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_title is not None):
                __append((' title="%s"' % __attr_title))
            __append(' >\n                            ')

            # <Static value=<ast.Dict object at 0x7fd0780a9e70> name=None at 7fd0780aa650> -> __attrs_140533343894736
            __attrs_140533343894736 = _static_140533343886960

            # <a ... (0:0)
            # --------------------------------------------------------
            __append('<a')

            # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533343888592
            __default_140533343888592 = _DEFAULT_MARKER

            # <Substitution 'item_link' (51:38)> -> __attr_href
            __token = 2373
            try:
                __zt_tmp = __attrs_140533343894736
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_140533417025280('path', 'item_link', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((' href="%s"' % __attr_href))
            __append('>\n                              ')

            # <Static value=<ast.Dict object at 0x7fd0780aa7a0> name=None at 7fd0780a8fa0> -> __attrs_140533343886144
            __attrs_140533343886144 = _static_140533343889312

            # <Value 'item_has_image' (54:50)> -> __condition
            __token = 2522
            try:
                __zt_tmp = __attrs_140533343886144
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140533417025280('path', 'item_has_image', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
            if __condition:

                # <img ... (0:0)
                # --------------------------------------------------------
                __append('<img class="image-tile"')

                # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533343893728
                __default_140533343893728 = _DEFAULT_MARKER

                # <Substitution 'string:$item_url/@@images/image/tile' (56:42)> -> __attr_src
                __token = 2632
                try:
                    __zt_tmp = __attrs_140533343886144
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_src = _static_140533417025280('string', '$item_url/@@images/image/tile', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                __attr_src = __quote(__attr_src, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_src is not None):
                    __append((' src="%s"' % __attr_src))
                __append(' />')
            __append('\n                            </a>\n                            ')

            # <Static value=<ast.Dict object at 0x7fd0780ab520> name=None at 7fd0780ab940> -> __attrs_140533343885424
            __attrs_140533343885424 = _static_140533343892768

            # <a ... (0:0)
            # --------------------------------------------------------
            __append('<a')

            # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533343881776
            __default_140533343881776 = _DEFAULT_MARKER

            # <Substitution 'item_link' (62:38)> -> __attr_href
            __token = 2934
            try:
                __zt_tmp = __attrs_140533343885424
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_140533417025280('path', 'item_link', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((' href="%s"' % __attr_href))

            # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533343889072
            __default_140533343889072 = _DEFAULT_MARKER

            # <Substitution 'string:$item_type_class $item_wf_state_class url' (63:38)> -> __attr_class
            __token = 2983
            try:
                __zt_tmp = __attrs_140533343885424
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_140533417025280('string', '$item_type_class $item_wf_state_class url', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((' class="%s"' % __attr_class))

            # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533343879376
            __default_140533343879376 = _DEFAULT_MARKER

            # <Substitution 'item_type' (64:37)> -> __attr_title
            __token = 3071
            try:
                __zt_tmp = __attrs_140533343885424
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_title = _static_140533417025280('path', 'item_type', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
            __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_title is not None):
                __append((' title="%s"' % __attr_title))
            __append(' >')

            # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533343882112
            __default_140533343882112 = _DEFAULT_MARKER

            # <Value 'python: item_title or item_id' (60:44)> -> __cache_140533343880528
            __token = 2817
            try:
                __zt_tmp = __attrs_140533343885424
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140533343880528 = _static_140533417025280('python', ' item_title or item_id', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))

            # <BinOp left=<Value 'python: item_title or item_id' (60:44)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fd07c5afbe0> at 7fd0780a97b0> -> __condition
            __expression = __cache_140533343880528

            # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                __append('\n\n                             Item Title\n                            ')
            else:
                __content = __cache_140533343880528
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append('</a>\n                          </span>\n                          ')
            __token = None
            render_document_byline(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n                        </header>')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_document_byline(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __slot_description_slot = econtext['__slot_description_slot'].pop()
        except:
            __slot_description_slot = None

        try:
            getname = econtext.get_name
            get = econtext.get

            # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533343892240
            __attrs_140533343892240 = _static_140533416833664
            __append('\n                            ')

            # <Static value=<ast.Dict object at 0x7fd07828d270> name=None at 7fd07828d4b0> -> __attrs_140533345863808
            __attrs_140533345863808 = _static_140533345866352

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="documentByLine">\n                              ')

            # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533345864240
            __attrs_140533345864240 = _static_140533416833664

            # <Value 'view/show_about' (73:53)> -> __condition
            __token = 3442
            try:
                __zt_tmp = __attrs_140533345864240
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140533417025280('path', 'view/show_about', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
            if __condition:
                __append('\n                          &mdash;\n                                ')

                # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533345871536
                __attrs_140533345871536 = _static_140533416833664
                __backup_author_140533343883840 = get('author', __marker)

                # <Value 'python:view.pas_member.info(item_creator)' (76:51)> -> __value
                __token = 3600
                try:
                    __zt_tmp = __attrs_140533345871536
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140533417025280('python', 'view.pas_member.info(item_creator)', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                econtext['author'] = __value
                __backup_creator_short_form_140533343887152 = get('creator_short_form', __marker)

                # <Value 'author/username' (77:62)> -> __value
                __token = 3705
                try:
                    __zt_tmp = __attrs_140533345871536
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140533417025280('path', 'author/username', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                econtext['creator_short_form'] = __value
                __backup_creator_long_form_140533345875520 = get('creator_long_form', __marker)

                # <Value 'string:?author=${author/username}' (78:60)> -> __value
                __token = 3783
                try:
                    __zt_tmp = __attrs_140533345871536
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140533417025280('string', '?author=${author/username}', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                econtext['creator_long_form'] = __value
                __backup_creator_is_openid_140533345871296 = get('creator_is_openid', __marker)

                # <Value "python:'/' in creator_short_form" (79:59)> -> __value
                __token = 3879
                try:
                    __zt_tmp = __attrs_140533345871536
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140533417025280('python', "'/' in creator_short_form", econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                econtext['creator_is_openid'] = __value
                __backup_creator_id_140533345871056 = get('creator_id', __marker)

                # <Value 'python:(creator_short_form, creator_long_form)[creator_is_openid]' (80:51)> -> __value
                __token = 3967
                try:
                    __zt_tmp = __attrs_140533345871536
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140533417025280('python', '(creator_short_form, creator_long_form)[creator_is_openid]', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                econtext['creator_id'] = __value

                # <Value 'item_creator' (82:57)> -> __condition
                __token = 4139
                try:
                    __zt_tmp = __attrs_140533345871536
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140533417025280('path', 'item_creator', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                if __condition:
                    __append('\n                                  ')

                    # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533345865728
                    __attrs_140533345865728 = _static_140533416833664

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>')
                    __stream_140533347602432_author = ''
                    __stream_140533345866208 = []
                    __append_140533345866208 = __stream_140533345866208.append
                    __append_140533345866208('\n                            by\n                                    ')
                    __stream_140533347602432_author = []
                    __append_140533347602432_author = __stream_140533347602432_author.append

                    # <Static value=<ast.Dict object at 0x7fd07828d0c0> name=None at 7fd07828e1a0> -> __attrs_140533345872544
                    __attrs_140533345872544 = _static_140533345865920

                    # <Negate value=<Value 'not:author' (87:53)> at 7fd07828ead0> -> __cache_140533345872592

                    # <Value 'not:author' (87:53)> -> __cache_140533345872592
                    __token = 4416
                    try:
                        __zt_tmp = __attrs_140533345872544
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140533345872592 = _static_140533417025280('not', 'author', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                    __cache_140533345872592 = not __cache_140533345872592
                    __condition = __cache_140533345872592
                    if __condition:

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append_140533347602432_author('<a')

                        # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533345866496
                        __default_140533345866496 = _DEFAULT_MARKER

                        # <Substitution 'string:${view/navigation_root_url}/author/${item_creator}' (89:46)> -> __attr_href
                        __token = 4530
                        try:
                            __zt_tmp = __attrs_140533345872544
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_140533417025280('string', '${view/navigation_root_url}/author/${item_creator}', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append_140533347602432_author((' href="%s"' % __attr_href))
                        __append_140533347602432_author(' >')

                    # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533345873504
                    __default_140533345873504 = _DEFAULT_MARKER

                    # <Value 'author/name_or_id' (86:52)> -> __cache_140533345868656
                    __token = 4344
                    try:
                        __zt_tmp = __attrs_140533345872544
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140533345868656 = _static_140533417025280('path', 'author/name_or_id', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))

                    # <BinOp left=<Value 'author/name_or_id' (86:52)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fd07c5afbe0> at 7fd07828e170> -> __condition
                    __expression = __cache_140533345868656

                    # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append_140533347602432_author('\n                              Bob Dobalina\n                                    ')
                    else:
                        __content = __cache_140533345868656
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append_140533347602432_author(__content)
                    __condition = __cache_140533345872592
                    if __condition:
                        __append_140533347602432_author('</a>')
                    __append_140533345866208('${author}')
                    __stream_140533347602432_author = ''.join(__stream_140533347602432_author)
                    __append_140533345866208('\n                                  ')
                    __msgid_140533345866208 = __re_whitespace(''.join(__stream_140533345866208)).strip()
                    if 'label_by_author':
                        __append(translate('label_by_author', mapping={'author': __stream_140533347602432_author, }, default=__msgid_140533345866208, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</span>\n                                ')
                if (__backup_creator_id_140533345871056 is __marker):
                    del econtext['creator_id']
                else:
                    econtext['creator_id'] = __backup_creator_id_140533345871056
                if (__backup_creator_is_openid_140533345871296 is __marker):
                    del econtext['creator_is_openid']
                else:
                    econtext['creator_is_openid'] = __backup_creator_is_openid_140533345871296
                if (__backup_creator_long_form_140533345875520 is __marker):
                    del econtext['creator_long_form']
                else:
                    econtext['creator_long_form'] = __backup_creator_long_form_140533345875520
                if (__backup_creator_short_form_140533343887152 is __marker):
                    del econtext['creator_short_form']
                else:
                    econtext['creator_short_form'] = __backup_creator_short_form_140533343887152
                if (__backup_author_140533343883840 is __marker):
                    del econtext['author']
                else:
                    econtext['author'] = __backup_author_140533343883840
                __append('\n\n                                ')

                # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533345869664
                __attrs_140533345869664 = _static_140533416833664
                __append('\n                            &mdash;\n                                  ')

                # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533345868080
                __attrs_140533345868080 = _static_140533416833664
                __stream_140533345869856 = []
                __append_140533345869856 = __stream_140533345869856.append
                __append_140533345869856('last modified')
                __msgid_140533345869856 = __re_whitespace(''.join(__stream_140533345869856)).strip()
                if 'box_last_modified':
                    __append(translate('box_last_modified', mapping=None, default=__msgid_140533345869856, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('\n                                  ')

                # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533345867120
                __attrs_140533345867120 = _static_140533416833664

                # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533345862176
                __default_140533345862176 = _DEFAULT_MARKER

                # <Value 'python:view.toLocalizedTime(item_modified,long_format=1)' (101:53)> -> __cache_140533345872688
                __token = 5135
                try:
                    __zt_tmp = __attrs_140533345867120
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140533345872688 = _static_140533417025280('python', 'view.toLocalizedTime(item_modified,long_format=1)', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))

                # <BinOp left=<Value 'python:view.toLocalizedTime(item_modified,long_format=1)' (101:53)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fd07c5afbe0> at 7fd07828c790> -> __condition
                __expression = __cache_140533345872688

                # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>\n                              August 16, 2001 at 23:35:59\n                                  </span>')
                else:
                    __content = __cache_140533345872688
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('\n                                \n\n                                ')
                if (__slot_description_slot is None):

                    # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533344127392
                    __attrs_140533344127392 = _static_140533416833664
                    __append('\n                                  ')

                    # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533344138384
                    __attrs_140533344138384 = _static_140533416833664

                    # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533344132192
                    __default_140533344132192 = _DEFAULT_MARKER

                    # <Value 'nothing' (107:56)> -> __cache_140533344128688
                    __token = 5482
                    try:
                        __zt_tmp = __attrs_140533344138384
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140533344128688 = _static_140533417025280('path', 'nothing', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))

                    # <BinOp left=<Value 'nothing' (107:56)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fd07c5afbe0> at 7fd0780e57e0> -> __condition
                    __expression = __cache_140533344128688

                    # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n                              Place custom listing info for custom types here\n                                  ')
                    else:
                        __content = __cache_140533344128688
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('\n                                ')
                else:
                    __slot_description_slot(__stream, econtext.copy(), rcontext)
                __append('\n                              ')
            __append('\n                            </div>\n                          ')
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

            # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533348695008
            __attrs_140533348695008 = _static_140533416833664
            __previous_i18n_domain_140533343906896 = __i18n_domain
            __i18n_domain = 'plone'
            __backup_macroname_140533256850816 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7fd07853fa60> name=None at 7fd07853f7f0> -> __value
            __value = _static_140533348694624
            econtext['macroname'] = __value

            def __fill_content_core(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533343901904
                __attrs_140533343901904 = _static_140533416833664
                __append('\n      ')
                __token = None
                render_content_core(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append('\n    ')
            _slots = econtext['__slot_content_core'] = _deque((__fill_content_core, ))

            # <Value 'context/@@main_template/macros/master' (6:23)> -> __macro
            __token = 247
            try:
                __zt_tmp = __attrs_140533348695008
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140533417025280('path', 'context/@@main_template/macros/master', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
            __token = 247
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140533256850816 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140533256850816
            __i18n_domain = __previous_i18n_domain_140533343906896
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_content_core': render_content_core, 'render_listing': render_listing, 'render_entries': render_entries, 'render_listitem': render_listitem, 'render_document_byline': render_document_byline, 'render': render, }