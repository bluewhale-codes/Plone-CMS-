# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/plone/app/event/browser/event_listing.pt'

__tokens = {2344: ('view/events', 74, 25), 2391: (' nocall: context/@@plone/toLocalizedTim', 75, 34), 2511: ('batch', 80, 36), 2757: ('python:view.date_speller(data.start)', 86, 32), 2998: ('data/start/isoformat', 93, 35), 3160: ('data/end/isoformat', 97, 35), 3482: ('data/location', 105, 39), 3749: ('string:${startf/month_name}', 112, 36), 3989: ('string:${startf/day}', 117, 37), 4133: ("python:startf['wkday_name']", 120, 39), 4509: ('data/url', 131, 30), 4695: ('data/title', 136, 41), 4892: ('python:view.formatted_date(data)', 141, 53), 5076: ('data/description', 146, 36), 5128: ('data/description', 147, 34), 5302: ('context/batch_macros/macros/navigation', 159, 32), 5302: ('context/batch_macros/macros/navigation', 159, 32), 462: ('view/header_string', 14, 33), 583: ('header/main', 18, 29), 623: ('header/main', 19, 27), 707: ('request/mode|string:future', 23, 18), 759: (' view/show_filte', 24, 24), 882: ('show_filter', 27, 31), 960: ("python:mode=='past'", 29, 31), 1124: ('view/mode_future_url', 34, 24), 1326: ("python:mode=='future'", 40, 31), 1490: ('view/mode_past_url', 45, 24), 1851: ('view/ical_url', 56, 22), 2108: ('header/sub', 66, 25), 2143: ('header/sub', 67, 23), 247: ('context/main_template/macros/master', 6, 23), 247: ('context/main_template/macros/master', 6, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from collections import deque as _deque
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140533344548752 = {'class': 'mode_ical nav-link', 'href': '', 'title': 'Download this event in iCal format', }
_static_140533344437296 = {'class': 'nav-item', }
_static_140533344545920 = {'class': 'mode_past nav-link', 'href': '', }
_static_140533349004576 = {'class': 'nav-item', }
_static_140533349000496 = {'class': 'mode_future nav-link', 'href': '', }
_static_140533344436336 = {'class': 'nav-item', }
_static_140533344446416 = {'class': 'mode_selector nav justify-content-end', }
_static_140533344448144 = {'class': 'documentFirstHeading', }
_static_140533344451888 = 'master'
_static_140533344538912 = 'navigation'
_static_140533344601760 = {'class': 'description', 'itemprop': 'description', }
_static_140533344605552 = {'class': 'documentByLine', }
_static_140533344606704 = {'class': 'summary', 'itemprop': 'name', }
_static_140533344609680 = {'class': 'url', 'href': '', 'itemprop': 'url', }
_static_140533344608096 = {'class': 'tileHeadline', }
_static_140533344613184 = {'class': 'cal_info clearfix', }
_static_140533344613712 = {'class': 'cal_wkday card-text', }
_static_140533344615440 = {'class': 'cal_day card-title fs-1 m-0', }
_static_140533343884704 = {'class': 'card-body d-flex flex-column p-2', }
_static_140533343884800 = {'class': 'cal_month card-header p-2', }
_static_140533343894736 = {'class': 'cal_date card me-3 flex-shrink-0 text-center', }
_static_140533343884368 = {'itemprop': 'address', }
_static_140533343887200 = {'class': 'location', 'itemprop': 'location', 'itemscope': '', 'itemtype': 'http://schema.org/Place', }
_static_140533343888688 = {'class': 'dtend', 'itemprop': 'endDate', }
_static_140533343886816 = {'class': 'dtstart', 'itemprop': 'startDate', }
_static_140533344538672 = {'class': 'hiddenStructure', }
_static_140533344537136 = {'class': 'vevent tileItem d-flex align-items-start mb-3', 'itemscope': '', 'itemtype': 'https://schema.org/Event', }
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

            # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533344542320
            __attrs_140533344542320 = _static_140533416833664
            __append('\n        ')

            # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533344543376
            __attrs_140533344543376 = _static_140533416833664
            __backup_batch_140533344444112 = get('batch', __marker)

            # <Value 'view/events' (74:25)> -> __value
            __token = 2344
            try:
                __zt_tmp = __attrs_140533344543376
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140533417025280('path', 'view/events', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
            econtext['batch'] = __value
            __backup_toLocalizedTime_140533344447040 = get('toLocalizedTime', __marker)

            # <Value 'nocall: context/@@plone/toLocalizedTime' (75:34)> -> __value
            __token = 2391
            try:
                __zt_tmp = __attrs_140533344543376
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140533417025280('nocall', ' context/@@plone/toLocalizedTime', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
            econtext['toLocalizedTime'] = __value
            __append('\n\n          ')

            # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533344544192
            __attrs_140533344544192 = _static_140533416833664

            # <section ... (0:0)
            # --------------------------------------------------------
            __append('<section>\n\n            ')

            # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533344539152
            __attrs_140533344539152 = _static_140533416833664
            __backup_data_140533344450304 = get('data', __marker)

            # <Value 'batch' (80:36)> -> __iterator
            __token = 2511
            try:
                __zt_tmp = __attrs_140533344539152
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140533417025280('path', 'batch', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
            (__iterator, ____index_140533344535408, ) = getname('repeat')('data', __iterator)
            econtext['data'] = None
            for __item in __iterator:
                econtext['data'] = __item
                __append('\n\n              ')

                # <Static value=<ast.Dict object at 0x7fd078148a30> name=None at 7fd078148130> -> __attrs_140533344538048
                __attrs_140533344538048 = _static_140533344537136
                __backup_startf_140533344449824 = get('startf', __marker)

                # <Value 'python:view.date_speller(data.start)' (86:32)> -> __value
                __token = 2757
                try:
                    __zt_tmp = __attrs_140533344538048
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140533417025280('python', 'view.date_speller(data.start)', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                econtext['startf'] = __value

                # <article ... (0:0)
                # --------------------------------------------------------
                __append('<article class="vevent tileItem d-flex align-items-start mb-3" itemscope itemtype="https://schema.org/Event" >\n\n                ')

                # <Static value=<ast.Dict object at 0x7fd078149030> name=None at 7fd078148610> -> __attrs_140533343885856
                __attrs_140533343885856 = _static_140533344538672

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append('<ul class="hiddenStructure">\n                  ')

                # <Static value=<ast.Dict object at 0x7fd0780a9de0> name=None at 7fd0780aa9e0> -> __attrs_140533343891952
                __attrs_140533343891952 = _static_140533343886816

                # <li ... (0:0)
                # --------------------------------------------------------
                __append('<li class="dtstart" itemprop="startDate" >')

                # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533343880432
                __default_140533343880432 = _DEFAULT_MARKER

                # <Value 'data/start/isoformat' (93:35)> -> __cache_140533343889216
                __token = 2998
                try:
                    __zt_tmp = __attrs_140533343891952
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140533343889216 = _static_140533417025280('path', 'data/start/isoformat', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))

                # <BinOp left=<Value 'data/start/isoformat' (93:35)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fd07c5afbe0> at 7fd0780aaaa0> -> __condition
                __expression = __cache_140533343889216

                # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('end')
                else:
                    __content = __cache_140533343889216
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</li>\n                  ')

                # <Static value=<ast.Dict object at 0x7fd0780aa530> name=None at 7fd0780a8910> -> __attrs_140533343886336
                __attrs_140533343886336 = _static_140533343888688

                # <li ... (0:0)
                # --------------------------------------------------------
                __append('<li class="dtend" itemprop="endDate" >')

                # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533343892096
                __default_140533343892096 = _DEFAULT_MARKER

                # <Value 'data/end/isoformat' (97:35)> -> __cache_140533343881632
                __token = 3160
                try:
                    __zt_tmp = __attrs_140533343886336
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140533343881632 = _static_140533417025280('path', 'data/end/isoformat', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))

                # <BinOp left=<Value 'data/end/isoformat' (97:35)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fd07c5afbe0> at 7fd0780aa3b0> -> __condition
                __expression = __cache_140533343881632

                # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('end')
                else:
                    __content = __cache_140533343881632
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</li>\n                  ')

                # <Static value=<ast.Dict object at 0x7fd0780a9f60> name=None at 7fd0780a93c0> -> __attrs_140533343888256
                __attrs_140533343888256 = _static_140533343887200

                # <li ... (0:0)
                # --------------------------------------------------------
                __append('<li class="location" itemprop="location" itemscope itemtype="http://schema.org/Place" >\n                    ')

                # <Static value=<ast.Dict object at 0x7fd0780a9450> name=None at 7fd0780ab970> -> __attrs_140533343892576
                __attrs_140533343892576 = _static_140533343884368

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span itemprop="address" >')

                # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533343889840
                __default_140533343889840 = _DEFAULT_MARKER

                # <Value 'data/location' (105:39)> -> __cache_140533343894400
                __token = 3482
                try:
                    __zt_tmp = __attrs_140533343892576
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140533343894400 = _static_140533417025280('path', 'data/location', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))

                # <BinOp left=<Value 'data/location' (105:39)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fd07c5afbe0> at 7fd0780ab8b0> -> __condition
                __expression = __cache_140533343894400

                # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('location')
                else:
                    __content = __cache_140533343894400
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</span>\n                  </li>\n                </ul>\n\n                ')

                # <Static value=<ast.Dict object at 0x7fd0780abcd0> name=None at 7fd0780a9f90> -> __attrs_140533343888880
                __attrs_140533343888880 = _static_140533343894736

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="cal_date card me-3 flex-shrink-0 text-center">\n                  ')

                # <Static value=<ast.Dict object at 0x7fd0780a9600> name=None at 7fd0780ab0a0> -> __attrs_140533343885616
                __attrs_140533343885616 = _static_140533343884800

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="cal_month card-header p-2" >')

                # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533343884752
                __default_140533343884752 = _DEFAULT_MARKER

                # <Value 'string:${startf/month_name}' (112:36)> -> __cache_140533343883168
                __token = 3749
                try:
                    __zt_tmp = __attrs_140533343885616
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140533343883168 = _static_140533417025280('string', '${startf/month_name}', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))

                # <BinOp left=<Value 'string:${startf/month_name}' (112:36)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fd07c5afbe0> at 7fd0780a9f00> -> __condition
                __expression = __cache_140533343883168

                # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('Oct.\n                  ')
                else:
                    __content = __cache_140533343883168
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</div>\n                  ')

                # <Static value=<ast.Dict object at 0x7fd0780a95a0> name=None at 7fd0780a96c0> -> __attrs_140533343889696
                __attrs_140533343889696 = _static_140533343884704

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="card-body d-flex flex-column p-2">\n                    ')

                # <Static value=<ast.Dict object at 0x7fd07815bc10> name=None at 7fd07815ace0> -> __attrs_140533344616400
                __attrs_140533344616400 = _static_140533344615440

                # <h3 ... (0:0)
                # --------------------------------------------------------
                __append('<h3 class="cal_day card-title fs-1 m-0" >')

                # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533344604688
                __default_140533344604688 = _DEFAULT_MARKER

                # <Value 'string:${startf/day}' (117:37)> -> __cache_140533344615776
                __token = 3989
                try:
                    __zt_tmp = __attrs_140533344616400
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140533344615776 = _static_140533417025280('string', '${startf/day}', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))

                # <BinOp left=<Value 'string:${startf/day}' (117:37)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fd07c5afbe0> at 7fd07815a3e0> -> __condition
                __expression = __cache_140533344615776

                # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('15')
                else:
                    __content = __cache_140533344615776
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</h3>\n                    ')

                # <Static value=<ast.Dict object at 0x7fd07815b550> name=None at 7fd07815b790> -> __attrs_140533344614864
                __attrs_140533344614864 = _static_140533344613712

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span class="cal_wkday card-text" >')

                # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533344604592
                __default_140533344604592 = _DEFAULT_MARKER

                # <Value "python:startf['wkday_name']" (120:39)> -> __cache_140533344613856
                __token = 4133
                try:
                    __zt_tmp = __attrs_140533344614864
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140533344613856 = _static_140533417025280('python', "startf['wkday_name']", econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))

                # <BinOp left=<Value "python:startf['wkday_name']" (120:39)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fd07c5afbe0> at 7fd07815b040> -> __condition
                __expression = __cache_140533344613856

                # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('Tue')
                else:
                    __content = __cache_140533344613856
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</span>\n                  </div>\n                </div>\n\n                ')

                # <Static value=<ast.Dict object at 0x7fd07815b340> name=None at 7fd07815b2b0> -> __attrs_140533344613328
                __attrs_140533344613328 = _static_140533344613184

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="cal_info clearfix">\n                  ')

                # <Static value=<ast.Dict object at 0x7fd078159f60> name=None at 7fd078159720> -> __attrs_140533344600320
                __attrs_140533344600320 = _static_140533344608096

                # <h2 ... (0:0)
                # --------------------------------------------------------
                __append('<h2 class="tileHeadline">\n                    ')

                # <Static value=<ast.Dict object at 0x7fd07815a590> name=None at 7fd07815a8c0> -> __attrs_140533344609488
                __attrs_140533344609488 = _static_140533344609680

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a class="url"')

                # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533344610160
                __default_140533344610160 = _DEFAULT_MARKER

                # <Substitution 'data/url' (131:30)> -> __attr_href
                __token = 4509
                try:
                    __zt_tmp = __attrs_140533344609488
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_140533417025280('path', 'data/url', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((' href="%s"' % __attr_href))
                __append(' itemprop="url" >\n                      ')

                # <Static value=<ast.Dict object at 0x7fd0781599f0> name=None at 7fd078159de0> -> __attrs_140533344606800
                __attrs_140533344606800 = _static_140533344606704

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span class="summary" itemprop="name" >')

                # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533344600464
                __default_140533344600464 = _DEFAULT_MARKER

                # <Value 'data/title' (136:41)> -> __cache_140533344608432
                __token = 4695
                try:
                    __zt_tmp = __attrs_140533344606800
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140533344608432 = _static_140533417025280('path', 'data/title', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))

                # <BinOp left=<Value 'data/title' (136:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fd07c5afbe0> at 7fd078159fc0> -> __condition
                __expression = __cache_140533344608432

                # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('Title')
                else:
                    __content = __cache_140533344608432
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</span>\n                    </a>\n                  </h2>\n                  ')

                # <Static value=<ast.Dict object at 0x7fd078159570> name=None at 7fd0781589a0> -> __attrs_140533344604880
                __attrs_140533344604880 = _static_140533344605552

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="documentByLine">\n                    ')

                # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533344602576
                __attrs_140533344602576 = _static_140533416833664

                # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533344604208
                __default_140533344604208 = _DEFAULT_MARKER

                # <Value 'python:view.formatted_date(data)' (141:53)> -> __cache_140533344603536
                __token = 4892
                try:
                    __zt_tmp = __attrs_140533344602576
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140533344603536 = _static_140533417025280('python', 'view.formatted_date(data)', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))

                # <BinOp left=<Value 'python:view.formatted_date(data)' (141:53)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fd07c5afbe0> at 7fd078158f70> -> __condition
                __expression = __cache_140533344603536

                # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140533344603536
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n                  </div>\n\n                  ')

                # <Static value=<ast.Dict object at 0x7fd0781586a0> name=None at 7fd0781584c0> -> __attrs_140533344601520
                __attrs_140533344601520 = _static_140533344601760

                # <Value 'data/description' (146:36)> -> __condition
                __token = 5076
                try:
                    __zt_tmp = __attrs_140533344601520
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140533417025280('path', 'data/description', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                if __condition:

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append('<p class="description" itemprop="description" >')

                    # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533344600704
                    __default_140533344600704 = _DEFAULT_MARKER

                    # <Value 'data/description' (147:34)> -> __cache_140533344605696
                    __token = 5128
                    try:
                        __zt_tmp = __attrs_140533344601520
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140533344605696 = _static_140533417025280('path', 'data/description', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))

                    # <BinOp left=<Value 'data/description' (147:34)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fd07c5afbe0> at 7fd078158c10> -> __condition
                    __expression = __cache_140533344605696

                    # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140533344605696
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</p>')
                __append('\n\n\n                </div>\n\n              </article>')
                if (__backup_startf_140533344449824 is __marker):
                    del econtext['startf']
                else:
                    econtext['startf'] = __backup_startf_140533344449824
                __append('\n\n            ')
                ____index_140533344535408 -= 1
                if (____index_140533344535408 > 0):
                    __append('')
            if (__backup_data_140533344450304 is __marker):
                del econtext['data']
            else:
                econtext['data'] = __backup_data_140533344450304
            __append('\n\n          </section>\n\n          ')

            # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533344601808
            __attrs_140533344601808 = _static_140533416833664
            __backup_macroname_140533258183232 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7fd078149120> name=None at 7fd078148310> -> __value
            __value = _static_140533344538912
            econtext['macroname'] = __value

            # <Value 'context/batch_macros/macros/navigation' (159:32)> -> __macro
            __token = 5302
            try:
                __zt_tmp = __attrs_140533344601808
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140533417025280('path', 'context/batch_macros/macros/navigation', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
            __token = 5302
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140533258183232 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140533258183232
            __append('\n\n        ')
            if (__backup_toLocalizedTime_140533344447040 is __marker):
                del econtext['toLocalizedTime']
            else:
                econtext['toLocalizedTime'] = __backup_toLocalizedTime_140533344447040
            if (__backup_batch_140533344444112 is __marker):
                del econtext['batch']
            else:
                econtext['batch'] = __backup_batch_140533344444112
            __append('\n      ')
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

            # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533344451936
            __attrs_140533344451936 = _static_140533416833664
            __previous_i18n_domain_140533344441664 = __i18n_domain
            __i18n_domain = 'plone'
            __backup_macroname_140533255157184 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7fd078133d30> name=None at 7fd078133ee0> -> __value
            __value = _static_140533344451888
            econtext['macroname'] = __value

            def __fill_content_title(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533344440224
                __attrs_140533344440224 = _static_140533416833664
                __backup_header_140533344442432 = get('header', __marker)

                # <Value 'view/header_string' (14:33)> -> __value
                __token = 462
                try:
                    __zt_tmp = __attrs_140533344440224
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140533417025280('path', 'view/header_string', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                econtext['header'] = __value
                __append('\n      ')

                # <Static value=<ast.Dict object at 0x7fd078132e90> name=None at 7fd078132260> -> __attrs_140533344448960
                __attrs_140533344448960 = _static_140533344448144

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append('<h1 class="documentFirstHeading">\n        ')

                # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533344442864
                __attrs_140533344442864 = _static_140533416833664

                # <Value 'header/main' (18:29)> -> __condition
                __token = 583
                try:
                    __zt_tmp = __attrs_140533344442864
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140533417025280('path', 'header/main', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                if __condition:

                    # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533344443200
                    __default_140533344443200 = _DEFAULT_MARKER

                    # <Value 'header/main' (19:27)> -> __cache_140533344443008
                    __token = 623
                    try:
                        __zt_tmp = __attrs_140533344442864
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140533344443008 = _static_140533417025280('path', 'header/main', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))

                    # <BinOp left=<Value 'header/main' (19:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fd07c5afbe0> at 7fd078132b90> -> __condition
                    __expression = __cache_140533344443008

                    # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span ></span>')
                    else:
                        __content = __cache_140533344443008
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                __append('\n      </h1>\n      ')

                # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533344446224
                __attrs_140533344446224 = _static_140533416833664
                __backup_mode_140533344441088 = get('mode', __marker)

                # <Value 'request/mode|string:future' (23:18)> -> __value
                __token = 707
                try:
                    __zt_tmp = __attrs_140533344446224
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140533417025280('path', 'request/mode|string:future', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                econtext['mode'] = __value
                __backup_show_filter_140533344445792 = get('show_filter', __marker)

                # <Value 'view/show_filter' (24:24)> -> __value
                __token = 759
                try:
                    __zt_tmp = __attrs_140533344446224
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140533417025280('path', 'view/show_filter', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                econtext['show_filter'] = __value

                # <nav ... (0:0)
                # --------------------------------------------------------
                __append('<nav>\n        ')

                # <Static value=<ast.Dict object at 0x7fd0781327d0> name=None at 7fd078132770> -> __attrs_140533344446512
                __attrs_140533344446512 = _static_140533344446416

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append('<ul class="mode_selector nav justify-content-end">\n          ')

                # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533344438976
                __attrs_140533344438976 = _static_140533416833664

                # <Value 'show_filter' (27:31)> -> __condition
                __token = 882
                try:
                    __zt_tmp = __attrs_140533344438976
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140533417025280('path', 'show_filter', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                if __condition:
                    __append('\n            ')

                    # <Static value=<ast.Dict object at 0x7fd078130070> name=None at 7fd078130490> -> __attrs_140533344438352
                    __attrs_140533344438352 = _static_140533344436336

                    # <Value "python:mode=='past'" (29:31)> -> __condition
                    __token = 960
                    try:
                        __zt_tmp = __attrs_140533344438352
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140533417025280('python', "mode=='past'", econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                    if __condition:

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li class="nav-item" >\n              ')

                        # <Static value=<ast.Dict object at 0x7fd07858a530> name=None at 7fd078588040> -> __attrs_140533348995552
                        __attrs_140533348995552 = _static_140533349000496

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append('<a class="mode_future nav-link"')

                        # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533348991568
                        __default_140533348991568 = _DEFAULT_MARKER

                        # <Substitution 'view/mode_future_url' (34:24)> -> __attr_href
                        __token = 1124
                        try:
                            __zt_tmp = __attrs_140533348995552
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_140533417025280('path', 'view/mode_future_url', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((' href="%s"' % __attr_href))
                        __append(' >')
                        __stream_140533349001408 = []
                        __append_140533349001408 = __stream_140533349001408.append
                        __append_140533349001408('Upcoming')
                        __msgid_140533349001408 = __re_whitespace(''.join(__stream_140533349001408)).strip()
                        if 'mode_future_link':
                            __append(translate('mode_future_link', mapping=None, default=__msgid_140533349001408, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</a>\n            </li>')
                    __append('\n            ')

                    # <Static value=<ast.Dict object at 0x7fd07858b520> name=None at 7fd07858b490> -> __attrs_140533349004624
                    __attrs_140533349004624 = _static_140533349004576

                    # <Value "python:mode=='future'" (40:31)> -> __condition
                    __token = 1326
                    try:
                        __zt_tmp = __attrs_140533349004624
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140533417025280('python', "mode=='future'", econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                    if __condition:

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li class="nav-item" >\n              ')

                        # <Static value=<ast.Dict object at 0x7fd07814ac80> name=None at 7fd07814a080> -> __attrs_140533344548992
                        __attrs_140533344548992 = _static_140533344545920

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append('<a class="mode_past nav-link"')

                        # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533344543088
                        __default_140533344543088 = _DEFAULT_MARKER

                        # <Substitution 'view/mode_past_url' (45:24)> -> __attr_href
                        __token = 1490
                        try:
                            __zt_tmp = __attrs_140533344548992
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_140533417025280('path', 'view/mode_past_url', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((' href="%s"' % __attr_href))
                        __append(' >')
                        __stream_140533344537280 = []
                        __append_140533344537280 = __stream_140533344537280.append
                        __append_140533344537280('Past')
                        __msgid_140533344537280 = __re_whitespace(''.join(__stream_140533344537280)).strip()
                        if 'mode_past_link':
                            __append(translate('mode_past_link', mapping=None, default=__msgid_140533344537280, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</a>\n            </li>')
                    __append('\n          ')
                __append('\n          ')

                # <Static value=<ast.Dict object at 0x7fd078130430> name=None at 7fd078588d60> -> __attrs_140533344550144
                __attrs_140533344550144 = _static_140533344437296

                # <li ... (0:0)
                # --------------------------------------------------------
                __append('<li class="nav-item">\n            ')

                # <Static value=<ast.Dict object at 0x7fd07814b790> name=None at 7fd07814bc40> -> __attrs_140533344546688
                __attrs_140533344546688 = _static_140533344548752

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a class="mode_ical nav-link"')

                # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533344548272
                __default_140533344548272 = _DEFAULT_MARKER

                # <Substitution 'view/ical_url' (56:22)> -> __attr_href
                __token = 1851
                try:
                    __zt_tmp = __attrs_140533344546688
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_140533417025280('path', 'view/ical_url', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((' href="%s"' % __attr_href))

                # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533344545728
                __default_140533344545728 = _DEFAULT_MARKER

                # <Translate msgid='title_add_to_ical' node=<ast.Constant object at 0x7fd07814b5e0> at 7fd078149c90> -> __attr_title
                __attr_title = 'Download this event in iCal format'
                __attr_title = translate('title_add_to_ical', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                if (__attr_title is not None):
                    __append((' title="%s"' % __attr_title))
                __append(' >\n              ')

                # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533344544288
                __attrs_140533344544288 = _static_140533416833664

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span>')
                __stream_140533344545008 = []
                __append_140533344545008 = __stream_140533344545008.append
                __append_140533344545008('iCal')
                __msgid_140533344545008 = __re_whitespace(''.join(__stream_140533344545008)).strip()
                if 'label_add_to_ical':
                    __append(translate('label_add_to_ical', mapping=None, default=__msgid_140533344545008, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</span>\n            </a>\n\n          </li>\n        </ul>\n      </nav>')
                if (__backup_show_filter_140533344445792 is __marker):
                    del econtext['show_filter']
                else:
                    econtext['show_filter'] = __backup_show_filter_140533344445792
                if (__backup_mode_140533344441088 is __marker):
                    del econtext['mode']
                else:
                    econtext['mode'] = __backup_mode_140533344441088
                __append('\n      ')

                # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533344542992
                __attrs_140533344542992 = _static_140533416833664

                # <Value 'header/sub' (66:25)> -> __condition
                __token = 2108
                try:
                    __zt_tmp = __attrs_140533344542992
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140533417025280('path', 'header/sub', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                if __condition:

                    # <h2 ... (0:0)
                    # --------------------------------------------------------
                    __append('<h2 >')

                    # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533344540832
                    __default_140533344540832 = _DEFAULT_MARKER

                    # <Value 'header/sub' (67:23)> -> __cache_140533344549520
                    __token = 2143
                    try:
                        __zt_tmp = __attrs_140533344542992
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140533344549520 = _static_140533417025280('path', 'header/sub', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))

                    # <BinOp left=<Value 'header/sub' (67:23)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fd07c5afbe0> at 7fd07814af50> -> __condition
                    __expression = __cache_140533344549520

                    # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140533344549520
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</h2>')
                __append('\n    ')
                if (__backup_header_140533344442432 is __marker):
                    del econtext['header']
                else:
                    econtext['header'] = __backup_header_140533344442432
            _slots = econtext['__slot_content_title'] = _deque((__fill_content_title, ))

            def __fill_content_core(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533344541216
                __attrs_140533344541216 = _static_140533416833664
                __append('\n      ')
                __token = None
                render_content_core(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append('\n    ')
            _slots = econtext['__slot_content_core'] = _deque((__fill_content_core, ))

            # <Value 'context/main_template/macros/master' (6:23)> -> __macro
            __token = 247
            try:
                __zt_tmp = __attrs_140533344451936
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140533417025280('path', 'context/main_template/macros/master', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
            __token = 247
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140533255157184 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140533255157184
            __i18n_domain = __previous_i18n_domain_140533344441664
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_content_core': render_content_core, 'render': render, }