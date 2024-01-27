# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/plone/app/event/portlets/portlet_events.pt'

__tokens = {376: ('view/next_url', 15, 21), 425: ('not:next_link', 17, 23), 482: ('next_link', 19, 16), 688: ('view/thumb_scale', 29, 24), 752: ('view/events', 31, 33), 850: ('repeat/item/odd', 34, 23), 896: (' item/ur', 35, 29), 935: ('  item/descripti', 36, 28), 982: ('   item/ti', 37, 27), 1023: ('ion item/loca', 38, 26), 1067: ("mage python:getattr(item.context.aq_base, 'image', ", 39, 25), 1194: ("python:'portletItem odd' if oddrow else 'portletItem even'", 42, 22), 1385: ('item/context/@@images|nothing', 48, 23), 1487: ('item_url', 51, 22), 1519: (' item_desc', 52, 22), 1598: ('item_hasimage', 55, 35), 1679: ("python:scale.scale('image', scale=thumb_scale).tag(css_class='float-end thumb-'+thumb_scale)", 57, 31), 1840: ('img_tag', 59, 44), 1923: ('item_title', 62, 33), 2059: ('python:view.formatted_date(item)', 65, 43), 2191: ('item/timezone', 68, 25), 2263: ('tz', 70, 35), 2321: ('tz', 72, 38), 2436: ('item_location', 75, 35), 2531: ('item_location', 78, 39), 2833: ('view/prev_url', 89, 21), 2883: ('prev_link', 91, 24), 2936: ('prev_link', 93, 16), 3140: ('view/next_url', 101, 21), 3208: ('next_link', 104, 16)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140533345622896 = {'class': 'p-6 tile upcoming-events', 'href': 'next_link', }
_static_140533345620640 = {'class': 'p-6 tile previous-events', 'href': 'prev_link', }
_static_140533345584704 = {'class': 'card-footer portletFooter d-flex justify-content-around', }
_static_140533345599008 = {'class': 'location', }
_static_140533345597472 = {'class': 'timezone', }
_static_140533345594928 = {'class': 'portletItemDetails', }
_static_140533345588832 = {'class': 'tile', 'href': '#', 'title': 'item_descr', }
_static_140533345585328 = {'class': 'portletItem', }
_static_140533416833664 = {}
_static_140533346014864 = {'class': 'card-body portletContent', }
_static_140533417024992 = __C2ZContextWrapper
_static_140533417025280 = __compile_zt_expr
_static_140533346015632 = {'class': 'tile', 'href': '', }
_static_140533346025088 = {'class': 'card-header portletHeader', }
_static_140533346019712 = {'class': 'card portlet portletEvents', }
_static_140533346018896 = {'xmlns': 'http://www.w3.org/1999/xhtml', }

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

            # <Static value=<ast.Dict object at 0x7fd0782b2650> name=None at 7fd0782b12d0> -> __attrs_140533346012704
            __attrs_140533346012704 = _static_140533346018896
            __append('\n\n  ')

            # <Static value=<ast.Dict object at 0x7fd0782b2980> name=None at 7fd0782b2aa0> -> __attrs_140533346014528
            __attrs_140533346014528 = _static_140533346019712
            __previous_i18n_domain_140533346015584 = __i18n_domain
            __i18n_domain = 'plone'

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="card portlet portletEvents" >\n\n    ')

            # <Static value=<ast.Dict object at 0x7fd0782b3e80> name=None at 7fd0782b3d30> -> __attrs_140533346012512
            __attrs_140533346012512 = _static_140533346025088

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="card-header portletHeader">\n      ')

            # <Static value=<ast.Dict object at 0x7fd0782b1990> name=None at 7fd0782b0370> -> __attrs_140533346024272
            __attrs_140533346024272 = _static_140533346015632
            __backup_next_link_140533346017648 = get('next_link', __marker)

            # <Value 'view/next_url' (15:21)> -> __value
            __token = 376
            try:
                __zt_tmp = __attrs_140533346024272
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140533417025280('path', 'view/next_url', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
            econtext['next_link'] = __value

            # <Negate value=<Value 'not:next_link' (17:23)> at 7fd0782b2c20> -> __cache_140533346020384

            # <Value 'not:next_link' (17:23)> -> __cache_140533346020384
            __token = 425
            try:
                __zt_tmp = __attrs_140533346024272
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140533346020384 = _static_140533417025280('not', 'next_link', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
            __cache_140533346020384 = not __cache_140533346020384
            __condition = __cache_140533346020384
            if __condition:

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a class="tile"')

                # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533346013232
                __default_140533346013232 = _DEFAULT_MARKER

                # <Substitution 'next_link' (19:16)> -> __attr_href
                __token = 482
                try:
                    __zt_tmp = __attrs_140533346024272
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_140533417025280('path', 'next_link', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((' href="%s"' % __attr_href))
                __append(' >')
            __stream_140533346023168 = []
            __append_140533346023168 = __stream_140533346023168.append
            __append_140533346023168('\n          Upcoming Events\n      ')
            __msgid_140533346023168 = __re_whitespace(''.join(__stream_140533346023168)).strip()
            if 'box_events':
                __append(translate('box_events', mapping=None, default=__msgid_140533346023168, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __condition = __cache_140533346020384
            if __condition:
                __append('</a>')
            if (__backup_next_link_140533346017648 is __marker):
                del econtext['next_link']
            else:
                econtext['next_link'] = __backup_next_link_140533346017648
            __append('\n    </div>\n\n    ')

            # <Static value=<ast.Dict object at 0x7fd0782b1690> name=None at 7fd0782b3580> -> __attrs_140533348694720
            __attrs_140533348694720 = _static_140533346014864

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="card-body portletContent">\n      ')

            # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533402218464
            __attrs_140533402218464 = _static_140533416833664
            __backup_thumb_scale_140533346023744 = get('thumb_scale', __marker)

            # <Value 'view/thumb_scale' (29:24)> -> __value
            __token = 688
            try:
                __zt_tmp = __attrs_140533402218464
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140533417025280('path', 'view/thumb_scale', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
            econtext['thumb_scale'] = __value

            # <ul ... (0:0)
            # --------------------------------------------------------
            __append('<ul>\n        ')

            # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533345584080
            __attrs_140533345584080 = _static_140533416833664
            __backup_item_140533346021872 = get('item', __marker)

            # <Value 'view/events' (31:33)> -> __iterator
            __token = 752
            try:
                __zt_tmp = __attrs_140533345584080
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140533417025280('path', 'view/events', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
            (__iterator, ____index_140533345584416, ) = getname('repeat')('item', __iterator)
            econtext['item'] = None
            for __item in __iterator:
                econtext['item'] = __item
                __append('\n          ')

                # <Static value=<ast.Dict object at 0x7fd0782488b0> name=None at 7fd0782488e0> -> __attrs_140533345586192
                __attrs_140533345586192 = _static_140533345585328
                __backup_oddrow_140533345583504 = get('oddrow', __marker)

                # <Value 'repeat/item/odd' (34:23)> -> __value
                __token = 850
                try:
                    __zt_tmp = __attrs_140533345586192
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140533417025280('path', 'repeat/item/odd', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                econtext['oddrow'] = __value
                __backup_item_url_140533345584224 = get('item_url', __marker)

                # <Value 'item/url' (35:29)> -> __value
                __token = 896
                try:
                    __zt_tmp = __attrs_140533345586192
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140533417025280('path', 'item/url', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                econtext['item_url'] = __value
                __backup_item_descr_140533345584320 = get('item_descr', __marker)

                # <Value 'item/description' (36:28)> -> __value
                __token = 935
                try:
                    __zt_tmp = __attrs_140533345586192
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140533417025280('path', 'item/description', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                econtext['item_descr'] = __value
                __backup_item_title_140533345586000 = get('item_title', __marker)

                # <Value 'item/title' (37:27)> -> __value
                __token = 982
                try:
                    __zt_tmp = __attrs_140533345586192
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140533417025280('path', 'item/title', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                econtext['item_title'] = __value
                __backup_item_location_140533345586048 = get('item_location', __marker)

                # <Value 'item/location' (38:26)> -> __value
                __token = 1023
                try:
                    __zt_tmp = __attrs_140533345586192
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140533417025280('path', 'item/location', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                econtext['item_location'] = __value
                __backup_item_hasimage_140533345586096 = get('item_hasimage', __marker)

                # <Value "python:getattr(item.context.aq_base, 'image', None)" (39:25)> -> __value
                __token = 1067
                try:
                    __zt_tmp = __attrs_140533345586192
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140533417025280('python', "getattr(item.context.aq_base, 'image', None)", econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                econtext['item_hasimage'] = __value

                # <li ... (0:0)
                # --------------------------------------------------------
                __append('<li')

                # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533345584944
                __default_140533345584944 = _DEFAULT_MARKER

                # <Substitution "python:'portletItem odd' if oddrow else 'portletItem even'" (42:22)> -> __attr_class
                __token = 1194
                try:
                    __zt_tmp = __attrs_140533345586192
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_class = _static_140533417025280('python', "'portletItem odd' if oddrow else 'portletItem even'", econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                __attr_class = __quote(__attr_class, '"', '&quot;', 'portletItem', _DEFAULT_MARKER)
                if (__attr_class is not None):
                    __append((' class="%s"' % __attr_class))
                __append(' >\n            ')

                # <Static value=<ast.Dict object at 0x7fd078249660> name=None at 7fd078249690> -> __attrs_140533345589552
                __attrs_140533345589552 = _static_140533345588832
                __backup_scale_140533345586288 = get('scale', __marker)

                # <Value 'item/context/@@images|nothing' (48:23)> -> __value
                __token = 1385
                try:
                    __zt_tmp = __attrs_140533345589552
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140533417025280('path', 'item/context/@@images|nothing', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                econtext['scale'] = __value

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a class="tile"')

                # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533345588304
                __default_140533345588304 = _DEFAULT_MARKER

                # <Substitution 'item_url' (51:22)> -> __attr_href
                __token = 1487
                try:
                    __zt_tmp = __attrs_140533345589552
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_140533417025280('path', 'item_url', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', '#', _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((' href="%s"' % __attr_href))

                # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533345589024
                __default_140533345589024 = _DEFAULT_MARKER

                # <Substitution 'item_descr' (52:22)> -> __attr_title
                __token = 1519
                try:
                    __zt_tmp = __attrs_140533345589552
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_title = _static_140533417025280('path', 'item_descr', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_title is not None):
                    __append((' title="%s"' % __attr_title))
                __append(' >\n              ')

                # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533345590800
                __attrs_140533345590800 = _static_140533416833664

                # <Value 'item_hasimage' (55:35)> -> __condition
                __token = 1598
                try:
                    __zt_tmp = __attrs_140533345590800
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140533417025280('path', 'item_hasimage', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>\n                ')

                    # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533345592624
                    __attrs_140533345592624 = _static_140533416833664
                    __backup_img_tag_140533345590128 = get('img_tag', __marker)

                    # <Value "python:scale.scale('image', scale=thumb_scale).tag(css_class='float-end thumb-'+thumb_scale)" (57:31)> -> __value
                    __token = 1679
                    try:
                        __zt_tmp = __attrs_140533345592624
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140533417025280('python', "scale.scale('image', scale=thumb_scale).tag(css_class='float-end thumb-'+thumb_scale)", econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                    econtext['img_tag'] = __value

                    # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533345592432
                    __default_140533345592432 = _DEFAULT_MARKER

                    # <Value 'img_tag' (59:44)> -> __cache_140533345591952
                    __token = 1840
                    try:
                        __zt_tmp = __attrs_140533345592624
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140533345591952 = _static_140533417025280('path', 'img_tag', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))

                    # <BinOp left=<Value 'img_tag' (59:44)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fd07c5afbe0> at 7fd07824a350> -> __condition
                    __expression = __cache_140533345591952

                    # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <img ... (0:0)
                        # --------------------------------------------------------
                        __append('<img />')
                    else:
                        __content = __cache_140533345591952
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    if (__backup_img_tag_140533345590128 is __marker):
                        del econtext['img_tag']
                    else:
                        econtext['img_tag'] = __backup_img_tag_140533345590128
                    __append('\n              </span>')
                __append('\n              ')

                # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533345594208
                __attrs_140533345594208 = _static_140533416833664

                # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533345594016
                __default_140533345594016 = _DEFAULT_MARKER

                # <Value 'item_title' (62:33)> -> __cache_140533345593536
                __token = 1923
                try:
                    __zt_tmp = __attrs_140533345594208
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140533345593536 = _static_140533417025280('path', 'item_title', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))

                # <BinOp left=<Value 'item_title' (62:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fd07c5afbe0> at 7fd07824a980> -> __condition
                __expression = __cache_140533345593536

                # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>Some Event</span>')
                else:
                    __content = __cache_140533345593536
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('\n            </a>')
                if (__backup_scale_140533345586288 is __marker):
                    del econtext['scale']
                else:
                    econtext['scale'] = __backup_scale_140533345586288
                __append('\n            ')

                # <Static value=<ast.Dict object at 0x7fd07824ae30> name=None at 7fd07824ae60> -> __attrs_140533345595360
                __attrs_140533345595360 = _static_140533345594928

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span class="portletItemDetails">\n              ')

                # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533345596896
                __attrs_140533345596896 = _static_140533416833664

                # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533345596704
                __default_140533345596704 = _DEFAULT_MARKER

                # <Value 'python:view.formatted_date(item)' (65:43)> -> __cache_140533345596176
                __token = 2059
                try:
                    __zt_tmp = __attrs_140533345596896
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140533345596176 = _static_140533417025280('python', 'view.formatted_date(item)', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))

                # <BinOp left=<Value 'python:view.formatted_date(item)' (65:43)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fd07c5afbe0> at 7fd07824b400> -> __condition
                __expression = __cache_140533345596176

                # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140533345596176
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n              ')

                # <Static value=<ast.Dict object at 0x7fd07824b820> name=None at 7fd07824b850> -> __attrs_140533345597952
                __attrs_140533345597952 = _static_140533345597472
                __backup_tz_140533345589696 = get('tz', __marker)

                # <Value 'item/timezone' (68:25)> -> __value
                __token = 2191
                try:
                    __zt_tmp = __attrs_140533345597952
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140533417025280('path', 'item/timezone', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                econtext['tz'] = __value

                # <Value 'tz' (70:35)> -> __condition
                __token = 2263
                try:
                    __zt_tmp = __attrs_140533345597952
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140533417025280('path', 'tz', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span class="timezone" >\n                (')

                    # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533345616272
                    __attrs_140533345616272 = _static_140533416833664

                    # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533345616080
                    __default_140533345616080 = _DEFAULT_MARKER

                    # <Value 'tz' (72:38)> -> __cache_140533345599152
                    __token = 2321
                    try:
                        __zt_tmp = __attrs_140533345616272
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140533345599152 = _static_140533417025280('path', 'tz', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))

                    # <BinOp left=<Value 'tz' (72:38)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fd07c5afbe0> at 7fd07824bf70> -> __condition
                    __expression = __cache_140533345599152

                    # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('TZ')
                    else:
                        __content = __cache_140533345599152
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(')\n              </span>')
                if (__backup_tz_140533345589696 is __marker):
                    del econtext['tz']
                else:
                    econtext['tz'] = __backup_tz_140533345589696
                __append('\n              ')

                # <Static value=<ast.Dict object at 0x7fd07824be20> name=None at 7fd07824bdc0> -> __attrs_140533345617184
                __attrs_140533345617184 = _static_140533345599008

                # <Value 'item_location' (75:35)> -> __condition
                __token = 2436
                try:
                    __zt_tmp = __attrs_140533345617184
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140533417025280('path', 'item_location', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span class="location" >\n                 &mdash;\n                ')

                    # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533345618960
                    __attrs_140533345618960 = _static_140533416833664

                    # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533345618480
                    __default_140533345618480 = _DEFAULT_MARKER

                    # <Value 'item_location' (78:39)> -> __cache_140533345618000
                    __token = 2531
                    try:
                        __zt_tmp = __attrs_140533345618960
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140533345618000 = _static_140533417025280('path', 'item_location', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))

                    # <BinOp left=<Value 'item_location' (78:39)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fd07c5afbe0> at 7fd078250910> -> __condition
                    __expression = __cache_140533345618000

                    # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('Location')
                    else:
                        __content = __cache_140533345618000
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('\n              </span>')
                __append('\n            </span>\n          </li>')
                if (__backup_item_hasimage_140533345586096 is __marker):
                    del econtext['item_hasimage']
                else:
                    econtext['item_hasimage'] = __backup_item_hasimage_140533345586096
                if (__backup_item_location_140533345586048 is __marker):
                    del econtext['item_location']
                else:
                    econtext['item_location'] = __backup_item_location_140533345586048
                if (__backup_item_title_140533345586000 is __marker):
                    del econtext['item_title']
                else:
                    econtext['item_title'] = __backup_item_title_140533345586000
                if (__backup_item_descr_140533345584320 is __marker):
                    del econtext['item_descr']
                else:
                    econtext['item_descr'] = __backup_item_descr_140533345584320
                if (__backup_item_url_140533345584224 is __marker):
                    del econtext['item_url']
                else:
                    econtext['item_url'] = __backup_item_url_140533345584224
                if (__backup_oddrow_140533345583504 is __marker):
                    del econtext['oddrow']
                else:
                    econtext['oddrow'] = __backup_oddrow_140533345583504
                __append('\n        ')
                ____index_140533345584416 -= 1
                if (____index_140533345584416 > 0):
                    __append('')
            if (__backup_item_140533346021872 is __marker):
                del econtext['item']
            else:
                econtext['item'] = __backup_item_140533346021872
            __append('\n      </ul>')
            if (__backup_thumb_scale_140533346023744 is __marker):
                del econtext['thumb_scale']
            else:
                econtext['thumb_scale'] = __backup_thumb_scale_140533346023744
            __append('\n    </div>\n\n    ')

            # <Static value=<ast.Dict object at 0x7fd078248640> name=None at 7fd0782490f0> -> __attrs_140533345618768
            __attrs_140533345618768 = _static_140533345584704

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="card-footer portletFooter d-flex justify-content-around">\n      ')

            # <Static value=<ast.Dict object at 0x7fd0782512a0> name=None at 7fd0782512d0> -> __attrs_140533345621120
            __attrs_140533345621120 = _static_140533345620640
            __backup_prev_link_140533346017312 = get('prev_link', __marker)

            # <Value 'view/prev_url' (89:21)> -> __value
            __token = 2833
            try:
                __zt_tmp = __attrs_140533345621120
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140533417025280('path', 'view/prev_url', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
            econtext['prev_link'] = __value

            # <Value 'prev_link' (91:24)> -> __condition
            __token = 2883
            try:
                __zt_tmp = __attrs_140533345621120
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140533417025280('path', 'prev_link', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
            if __condition:

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a class="p-6 tile previous-events"')

                # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533345620112
                __default_140533345620112 = _DEFAULT_MARKER

                # <Substitution 'prev_link' (93:16)> -> __attr_href
                __token = 2936
                try:
                    __zt_tmp = __attrs_140533345621120
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_140533417025280('path', 'prev_link', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((' href="%s"' % __attr_href))
                __append(' >')
                __stream_140533345619728 = []
                __append_140533345619728 = __stream_140533345619728.append
                __append_140533345619728('\n        Previous events&hellip;\n      ')
                __msgid_140533345619728 = __re_whitespace(''.join(__stream_140533345619728)).strip()
                if 'box_previous_events':
                    __append(translate('box_previous_events', mapping=None, default=__msgid_140533345619728, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</a>')
            if (__backup_prev_link_140533346017312 is __marker):
                del econtext['prev_link']
            else:
                econtext['prev_link'] = __backup_prev_link_140533346017312
            __append('\n      ')

            # <Static value=<ast.Dict object at 0x7fd078251b70> name=None at 7fd078251ba0> -> __attrs_140533345623376
            __attrs_140533345623376 = _static_140533345622896
            __backup_next_link_140533345585952 = get('next_link', __marker)

            # <Value 'view/next_url' (101:21)> -> __value
            __token = 3140
            try:
                __zt_tmp = __attrs_140533345623376
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140533417025280('path', 'view/next_url', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
            econtext['next_link'] = __value

            # <a ... (0:0)
            # --------------------------------------------------------
            __append('<a class="p-6 tile upcoming-events"')

            # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533345622368
            __default_140533345622368 = _DEFAULT_MARKER

            # <Substitution 'next_link' (104:16)> -> __attr_href
            __token = 3208
            try:
                __zt_tmp = __attrs_140533345623376
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_140533417025280('path', 'next_link', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((' href="%s"' % __attr_href))
            __append(' >')
            __stream_140533345621984 = []
            __append_140533345621984 = __stream_140533345621984.append
            __append_140533345621984('\n        Upcoming events&hellip;\n      ')
            __msgid_140533345621984 = __re_whitespace(''.join(__stream_140533345621984)).strip()
            if 'box_upcoming_events':
                __append(translate('box_upcoming_events', mapping=None, default=__msgid_140533345621984, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</a>')
            if (__backup_next_link_140533345585952 is __marker):
                del econtext['next_link']
            else:
                econtext['next_link'] = __backup_next_link_140533345585952
            __append('\n    </div>\n\n  </div>')
            __i18n_domain = __previous_i18n_domain_140533346015584
            __append('\n\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }