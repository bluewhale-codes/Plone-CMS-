# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/plone/app/event/browser/formatted_date.pt'

__tokens = {278: ('view/date_dict', 10, 20), 313: (' date_dict/whole_da', 11, 19), 352: ('d date_dict/open_e', 12, 17), 450: ('not:date_dict/same_day', 17, 37), 620: ('date_dict/start_iso', 22, 20), 757: ('date_dict/start_date', 27, 29), 835: ('not:whole_day', 28, 38), 984: ('date_dict/start_time', 30, 31), 1165: ('date_dict/end_iso', 37, 20), 1298: ('date_dict/end_date', 42, 29), 1372: ('not:whole_day', 43, 38), 1521: ('date_dict/end_time', 45, 31), 1673: ('date_dict/same_day', 51, 32), 1725: ('whole_day', 52, 31), 1764: ('date_dict/start_date', 53, 27), 1888: ('python:open_end and not whole_day', 57, 31), 2056: ('date_dict/start_date', 61, 27), 2279: ('date_dict/start_iso', 68, 22), 2204: ('date_dict/start_time', 66, 27), 2439: ('python:not (whole_day or open_end)', 74, 29), 2598: ('date_dict/start_date', 78, 27), 2821: ('date_dict/start_iso', 85, 22), 2746: ('date_dict/start_time', 83, 27), 3067: ('date_dict/end_iso', 94, 22), 2994: ('date_dict/end_time', 92, 27)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140533259042288 = {'class': 'dtend', 'title': 'date_dict/end_iso', }
_static_140533259039888 = {'class': 'dtstart', 'title': 'date_dict/start_iso', }
_static_140533259037440 = {'class': 'datedisplay', }
_static_140533259035856 = {'class': 'dtstart', 'title': 'date_dict/start_iso', }
_static_140533259035520 = {'class': 'datedisplay', }
_static_140533258709664 = {'class': 'explain', }
_static_140533258706400 = {'class': 'dtend', 'title': 'date_dict/end_iso', }
_static_140533258702032 = {'class': 'explain', }
_static_140533258708752 = {'class': 'dtstart', 'title': 'date_dict/start_iso', }
_static_140533417024992 = __C2ZContextWrapper
_static_140533417025280 = __compile_zt_expr
_static_140533416833664 = {}
_static_140533428184272 = {'xmlns': 'http://www.w3.org/1999/xhtml', 'lang': 'en', 'xml:lang': 'en', }

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

            # <Static value=<ast.Dict object at 0x7fd07d10e4d0> name=None at 7fd07d10d300> -> __attrs_140533344626640
            __attrs_140533344626640 = _static_140533428184272
            __previous_i18n_domain_140533344619776 = __i18n_domain
            __i18n_domain = 'plone'
            __append('\n  ')

            # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533426803936
            __attrs_140533426803936 = _static_140533416833664
            __backup_date_dict_140533344565328 = get('date_dict', __marker)

            # <Value 'view/date_dict' (10:20)> -> __value
            __token = 278
            try:
                __zt_tmp = __attrs_140533426803936
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140533417025280('path', 'view/date_dict', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
            econtext['date_dict'] = __value
            __backup_whole_day_140533344794272 = get('whole_day', __marker)

            # <Value 'date_dict/whole_day' (11:19)> -> __value
            __token = 313
            try:
                __zt_tmp = __attrs_140533426803936
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140533417025280('path', 'date_dict/whole_day', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
            econtext['whole_day'] = __value
            __backup_open_end_140533344517856 = get('open_end', __marker)

            # <Value 'date_dict/open_end' (12:17)> -> __value
            __token = 352
            try:
                __zt_tmp = __attrs_140533426803936
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140533417025280('path', 'date_dict/open_end', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
            econtext['open_end'] = __value
            __append('\n\n    ')

            # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533258699680
            __attrs_140533258699680 = _static_140533416833664

            # <Value 'not:date_dict/same_day' (17:37)> -> __condition
            __token = 450
            try:
                __zt_tmp = __attrs_140533258699680
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140533417025280('not', 'date_dict/same_day', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
            if __condition:
                __stream_140533255980640_enddate = ''
                __stream_140533255980640_startdate = ''
                __stream_140533344297232 = []
                __append_140533344297232 = __stream_140533344297232.append
                __append_140533344297232('\n      ')
                __stream_140533255980640_startdate = []
                __append_140533255980640_startdate = __stream_140533255980640_startdate.append

                # <Static value=<ast.Dict object at 0x7fd072f6e710> name=None at 7fd072f6cac0> -> __attrs_140533258703520
                __attrs_140533258703520 = _static_140533258708752

                # <abbr ... (0:0)
                # --------------------------------------------------------
                __append_140533255980640_startdate('<abbr class="dtstart"')

                # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533258699248
                __default_140533258699248 = _DEFAULT_MARKER

                # <Substitution 'date_dict/start_iso' (22:20)> -> __attr_title
                __token = 620
                try:
                    __zt_tmp = __attrs_140533258703520
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_title = _static_140533417025280('path', 'date_dict/start_iso', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_title is not None):
                    __append_140533255980640_startdate((' title="%s"' % __attr_title))
                __append_140533255980640_startdate(' >\n        ')

                # <Static value=<ast.Dict object at 0x7fd072f6ccd0> name=None at 7fd072f6c730> -> __attrs_140533258699728
                __attrs_140533258699728 = _static_140533258702032

                # <span ... (0:0)
                # --------------------------------------------------------
                __append_140533255980640_startdate('<span class="explain">\n          ')

                # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533258706064
                __attrs_140533258706064 = _static_140533416833664

                # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533258699920
                __default_140533258699920 = _DEFAULT_MARKER

                # <Value 'date_dict/start_date' (27:29)> -> __cache_140533258709232
                __token = 757
                try:
                    __zt_tmp = __attrs_140533258706064
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140533258709232 = _static_140533417025280('path', 'date_dict/start_date', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))

                # <BinOp left=<Value 'date_dict/start_date' (27:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fd07c5afbe0> at 7fd072f6c190> -> __condition
                __expression = __cache_140533258709232

                # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append_140533255980640_startdate('<span>Start Date</span>')
                else:
                    __content = __cache_140533258709232
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append_140533255980640_startdate(__content)
                __append_140533255980640_startdate('\n          ')

                # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533258700544
                __attrs_140533258700544 = _static_140533416833664

                # <Value 'not:whole_day' (28:38)> -> __condition
                __token = 835
                try:
                    __zt_tmp = __attrs_140533258700544
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140533417025280('not', 'whole_day', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                if __condition:
                    __append_140533255980640_startdate('\n            ')

                    # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533258701168
                    __attrs_140533258701168 = _static_140533416833664
                    __stream_140533258701648 = []
                    __append_140533258701648 = __stream_140533258701648.append
                    __msgid_140533258701648 = __re_whitespace(''.join(__stream_140533258701648)).strip()
                    if 'event_when_differentday_optional_word_between_date_and_time':
                        __append_140533255980640_startdate(translate('event_when_differentday_optional_word_between_date_and_time', mapping=None, default=__msgid_140533258701648, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append_140533255980640_startdate('\n            ')

                    # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533258705392
                    __attrs_140533258705392 = _static_140533416833664

                    # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533258701024
                    __default_140533258701024 = _DEFAULT_MARKER

                    # <Value 'date_dict/start_time' (30:31)> -> __cache_140533258707312
                    __token = 984
                    try:
                        __zt_tmp = __attrs_140533258705392
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140533258707312 = _static_140533417025280('path', 'date_dict/start_time', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))

                    # <BinOp left=<Value 'date_dict/start_time' (30:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fd07c5afbe0> at 7fd072f6e320> -> __condition
                    __expression = __cache_140533258707312

                    # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append_140533255980640_startdate('<span>Start Time</span>')
                    else:
                        __content = __cache_140533258707312
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append_140533255980640_startdate(__content)
                    __append_140533255980640_startdate('\n          ')
                __append_140533255980640_startdate('\n        </span>\n      </abbr>')
                __append_140533344297232('${startdate}')
                __stream_140533255980640_startdate = ''.join(__stream_140533255980640_startdate)
                __append_140533344297232('\n    to\n      ')
                __stream_140533255980640_enddate = []
                __append_140533255980640_enddate = __stream_140533255980640_enddate.append

                # <Static value=<ast.Dict object at 0x7fd072f6dde0> name=None at 7fd072f6cc40> -> __attrs_140533258710288
                __attrs_140533258710288 = _static_140533258706400

                # <abbr ... (0:0)
                # --------------------------------------------------------
                __append_140533255980640_enddate('<abbr class="dtend"')

                # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533258706592
                __default_140533258706592 = _DEFAULT_MARKER

                # <Substitution 'date_dict/end_iso' (37:20)> -> __attr_title
                __token = 1165
                try:
                    __zt_tmp = __attrs_140533258710288
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_title = _static_140533417025280('path', 'date_dict/end_iso', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_title is not None):
                    __append_140533255980640_enddate((' title="%s"' % __attr_title))
                __append_140533255980640_enddate(' >\n        ')

                # <Static value=<ast.Dict object at 0x7fd072f6eaa0> name=None at 7fd072f6ea70> -> __attrs_140533258704864
                __attrs_140533258704864 = _static_140533258709664

                # <span ... (0:0)
                # --------------------------------------------------------
                __append_140533255980640_enddate('<span class="explain">\n          ')

                # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533258702224
                __attrs_140533258702224 = _static_140533416833664

                # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533258712112
                __default_140533258712112 = _DEFAULT_MARKER

                # <Value 'date_dict/end_date' (42:29)> -> __cache_140533258711680
                __token = 1298
                try:
                    __zt_tmp = __attrs_140533258702224
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140533258711680 = _static_140533417025280('path', 'date_dict/end_date', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))

                # <BinOp left=<Value 'date_dict/end_date' (42:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fd07c5afbe0> at 7fd072f6f250> -> __condition
                __expression = __cache_140533258711680

                # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append_140533255980640_enddate('<span>End Date</span>')
                else:
                    __content = __cache_140533258711680
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append_140533255980640_enddate(__content)
                __append_140533255980640_enddate('\n          ')

                # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533258714896
                __attrs_140533258714896 = _static_140533416833664

                # <Value 'not:whole_day' (43:38)> -> __condition
                __token = 1372
                try:
                    __zt_tmp = __attrs_140533258714896
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140533417025280('not', 'whole_day', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                if __condition:
                    __append_140533255980640_enddate('\n            ')

                    # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533258712976
                    __attrs_140533258712976 = _static_140533416833664
                    __stream_140533258713072 = []
                    __append_140533258713072 = __stream_140533258713072.append
                    __msgid_140533258713072 = __re_whitespace(''.join(__stream_140533258713072)).strip()
                    if 'event_when_differentday_optional_word_between_date_and_time':
                        __append_140533255980640_enddate(translate('event_when_differentday_optional_word_between_date_and_time', mapping=None, default=__msgid_140533258713072, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append_140533255980640_enddate('\n            ')

                    # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533259030720
                    __attrs_140533259030720 = _static_140533416833664

                    # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533259031200
                    __default_140533259031200 = _DEFAULT_MARKER

                    # <Value 'date_dict/end_time' (45:31)> -> __cache_140533345591376
                    __token = 1521
                    try:
                        __zt_tmp = __attrs_140533259030720
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140533345591376 = _static_140533417025280('path', 'date_dict/end_time', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))

                    # <BinOp left=<Value 'date_dict/end_time' (45:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fd07c5afbe0> at 7fd078249c60> -> __condition
                    __expression = __cache_140533345591376

                    # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append_140533255980640_enddate('<span>End Time</span>')
                    else:
                        __content = __cache_140533345591376
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append_140533255980640_enddate(__content)
                    __append_140533255980640_enddate('\n          ')
                __append_140533255980640_enddate('\n        </span>\n      </abbr>')
                __append_140533344297232('${enddate}')
                __stream_140533255980640_enddate = ''.join(__stream_140533255980640_enddate)
                __append_140533344297232('\n    ')
                __msgid_140533344297232 = __re_whitespace(''.join(__stream_140533344297232)).strip()
                if 'event_when_differentday':
                    __append(translate('event_when_differentday', mapping={'startdate': __stream_140533255980640_startdate, 'enddate': __stream_140533255980640_enddate, }, default=__msgid_140533344297232, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('\n\n    ')

            # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533258712736
            __attrs_140533258712736 = _static_140533416833664

            # <Value 'date_dict/same_day' (51:32)> -> __condition
            __token = 1673
            try:
                __zt_tmp = __attrs_140533258712736
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140533417025280('path', 'date_dict/same_day', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
            if __condition:
                __append('\n      ')

                # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533259030960
                __attrs_140533259030960 = _static_140533416833664

                # <Value 'whole_day' (52:31)> -> __condition
                __token = 1725
                try:
                    __zt_tmp = __attrs_140533259030960
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140533417025280('path', 'whole_day', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                if __condition:
                    __append('\n        ')

                    # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533259028320
                    __attrs_140533259028320 = _static_140533416833664

                    # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533259028560
                    __default_140533259028560 = _DEFAULT_MARKER

                    # <Value 'date_dict/start_date' (53:27)> -> __cache_140533259027552
                    __token = 1764
                    try:
                        __zt_tmp = __attrs_140533259028320
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140533259027552 = _static_140533417025280('path', 'date_dict/start_date', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))

                    # <BinOp left=<Value 'date_dict/start_date' (53:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fd07c5afbe0> at 7fd072fbce20> -> __condition
                    __expression = __cache_140533259027552

                    # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span ></span>')
                    else:
                        __content = __cache_140533259027552
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('\n      ')
                __append('\n      ')

                # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533259026880
                __attrs_140533259026880 = _static_140533416833664

                # <Value 'python:open_end and not whole_day' (57:31)> -> __condition
                __token = 1888
                try:
                    __zt_tmp = __attrs_140533259026880
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140533417025280('python', 'open_end and not whole_day', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                if __condition:
                    __stream_140533255985120_date = ''
                    __stream_140533255985120_starttime = ''
                    __stream_140533259031104 = []
                    __append_140533259031104 = __stream_140533259031104.append
                    __append_140533259031104('\n        ')
                    __stream_140533255985120_date = []
                    __append_140533255985120_date = __stream_140533255985120_date.append

                    # <Static value=<ast.Dict object at 0x7fd072fbe380> name=None at 7fd072fbd390> -> __attrs_140533259034656
                    __attrs_140533259034656 = _static_140533259035520

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append_140533255985120_date('<span class="datedisplay" >')

                    # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533259029856
                    __default_140533259029856 = _DEFAULT_MARKER

                    # <Value 'date_dict/start_date' (61:27)> -> __cache_140533259029520
                    __token = 2056
                    try:
                        __zt_tmp = __attrs_140533259034656
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140533259029520 = _static_140533417025280('path', 'date_dict/start_date', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))

                    # <BinOp left=<Value 'date_dict/start_date' (61:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fd07c5afbe0> at 7fd072fbcc70> -> __condition
                    __expression = __cache_140533259029520

                    # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append_140533255985120_date('Start Date')
                    else:
                        __content = __cache_140533259029520
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append_140533255985120_date(__content)
                    __append_140533255985120_date('</span>')
                    __append_140533259031104('${date}')
                    __stream_140533255985120_date = ''.join(__stream_140533255985120_date)
                    __append_140533259031104('\n      from\n        ')
                    __stream_140533255985120_starttime = []
                    __append_140533255985120_starttime = __stream_140533255985120_starttime.append

                    # <Static value=<ast.Dict object at 0x7fd072fbe4d0> name=None at 7fd072fbdbd0> -> __attrs_140533259034320
                    __attrs_140533259034320 = _static_140533259035856

                    # <abbr ... (0:0)
                    # --------------------------------------------------------
                    __append_140533255985120_starttime('<abbr class="dtstart"')

                    # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533259035568
                    __default_140533259035568 = _DEFAULT_MARKER

                    # <Substitution 'date_dict/start_iso' (68:22)> -> __attr_title
                    __token = 2279
                    try:
                        __zt_tmp = __attrs_140533259034320
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_title = _static_140533417025280('path', 'date_dict/start_iso', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                    __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_title is not None):
                        __append_140533255985120_starttime((' title="%s"' % __attr_title))
                    __append_140533255985120_starttime(' >')

                    # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533259035664
                    __default_140533259035664 = _DEFAULT_MARKER

                    # <Value 'date_dict/start_time' (66:27)> -> __cache_140533259036960
                    __token = 2204
                    try:
                        __zt_tmp = __attrs_140533259034320
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140533259036960 = _static_140533417025280('path', 'date_dict/start_time', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))

                    # <BinOp left=<Value 'date_dict/start_time' (66:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fd07c5afbe0> at 7fd072fbe500> -> __condition
                    __expression = __cache_140533259036960

                    # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append_140533255985120_starttime('Start Time\n        ')
                    else:
                        __content = __cache_140533259036960
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append_140533255985120_starttime(__content)
                    __append_140533255985120_starttime('</abbr>')
                    __append_140533259031104('${starttime}')
                    __stream_140533255985120_starttime = ''.join(__stream_140533255985120_starttime)
                    __append_140533259031104('\n      ')
                    __msgid_140533259031104 = __re_whitespace(''.join(__stream_140533259031104)).strip()
                    if 'event_when_sameday_openend':
                        __append(translate('event_when_sameday_openend', mapping={'starttime': __stream_140533255985120_starttime, 'date': __stream_140533255985120_date, }, default=__msgid_140533259031104, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('\n      ')

                # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533259032016
                __attrs_140533259032016 = _static_140533416833664

                # <Value 'python:not (whole_day or open_end)' (74:29)> -> __condition
                __token = 2439
                try:
                    __zt_tmp = __attrs_140533259032016
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140533417025280('python', 'not (whole_day or open_end)', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                if __condition:
                    __stream_140533255985120_endtime = ''
                    __stream_140533255985120_date = ''
                    __stream_140533255985120_starttime = ''
                    __stream_140533259027936 = []
                    __append_140533259027936 = __stream_140533259027936.append
                    __append_140533259027936('\n        ')
                    __stream_140533255985120_date = []
                    __append_140533255985120_date = __stream_140533255985120_date.append

                    # <Static value=<ast.Dict object at 0x7fd072fbeb00> name=None at 7fd072fbeb30> -> __attrs_140533259037824
                    __attrs_140533259037824 = _static_140533259037440

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append_140533255985120_date('<span class="datedisplay" >')

                    # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533259032592
                    __default_140533259032592 = _DEFAULT_MARKER

                    # <Value 'date_dict/start_date' (78:27)> -> __cache_140533259031968
                    __token = 2598
                    try:
                        __zt_tmp = __attrs_140533259037824
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140533259031968 = _static_140533417025280('path', 'date_dict/start_date', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))

                    # <BinOp left=<Value 'date_dict/start_date' (78:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fd07c5afbe0> at 7fd072fbc0a0> -> __condition
                    __expression = __cache_140533259031968

                    # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append_140533255985120_date('Start Date')
                    else:
                        __content = __cache_140533259031968
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append_140533255985120_date(__content)
                    __append_140533255985120_date('</span>')
                    __append_140533259027936('${date}')
                    __stream_140533255985120_date = ''.join(__stream_140533255985120_date)
                    __append_140533259027936('\n      from\n        ')
                    __stream_140533255985120_starttime = []
                    __append_140533255985120_starttime = __stream_140533255985120_starttime.append

                    # <Static value=<ast.Dict object at 0x7fd072fbf490> name=None at 7fd072fbf4c0> -> __attrs_140533259040224
                    __attrs_140533259040224 = _static_140533259039888

                    # <abbr ... (0:0)
                    # --------------------------------------------------------
                    __append_140533255985120_starttime('<abbr class="dtstart"')

                    # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533259039408
                    __default_140533259039408 = _DEFAULT_MARKER

                    # <Substitution 'date_dict/start_iso' (85:22)> -> __attr_title
                    __token = 2821
                    try:
                        __zt_tmp = __attrs_140533259040224
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_title = _static_140533417025280('path', 'date_dict/start_iso', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                    __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_title is not None):
                        __append_140533255985120_starttime((' title="%s"' % __attr_title))
                    __append_140533255985120_starttime(' >')

                    # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533259038880
                    __default_140533259038880 = _DEFAULT_MARKER

                    # <Value 'date_dict/start_time' (83:27)> -> __cache_140533259038400
                    __token = 2746
                    try:
                        __zt_tmp = __attrs_140533259040224
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140533259038400 = _static_140533417025280('path', 'date_dict/start_time', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))

                    # <BinOp left=<Value 'date_dict/start_time' (83:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fd07c5afbe0> at 7fd072fbef80> -> __condition
                    __expression = __cache_140533259038400

                    # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append_140533255985120_starttime('Start Time\n        ')
                    else:
                        __content = __cache_140533259038400
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append_140533255985120_starttime(__content)
                    __append_140533255985120_starttime('</abbr>')
                    __append_140533259027936('${starttime}')
                    __stream_140533255985120_starttime = ''.join(__stream_140533255985120_starttime)
                    __append_140533259027936('\n      to\n        ')
                    __stream_140533255985120_endtime = []
                    __append_140533255985120_endtime = __stream_140533255985120_endtime.append

                    # <Static value=<ast.Dict object at 0x7fd072fbfdf0> name=None at 7fd072fbfe20> -> __attrs_140533259042624
                    __attrs_140533259042624 = _static_140533259042288

                    # <abbr ... (0:0)
                    # --------------------------------------------------------
                    __append_140533255985120_endtime('<abbr class="dtend"')

                    # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533259041808
                    __default_140533259041808 = _DEFAULT_MARKER

                    # <Substitution 'date_dict/end_iso' (94:22)> -> __attr_title
                    __token = 3067
                    try:
                        __zt_tmp = __attrs_140533259042624
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_title = _static_140533417025280('path', 'date_dict/end_iso', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                    __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_title is not None):
                        __append_140533255985120_endtime((' title="%s"' % __attr_title))
                    __append_140533255985120_endtime(' >')

                    # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533259041280
                    __default_140533259041280 = _DEFAULT_MARKER

                    # <Value 'date_dict/end_time' (92:27)> -> __cache_140533259040800
                    __token = 2994
                    try:
                        __zt_tmp = __attrs_140533259042624
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140533259040800 = _static_140533417025280('path', 'date_dict/end_time', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))

                    # <BinOp left=<Value 'date_dict/end_time' (92:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fd07c5afbe0> at 7fd072fbf8e0> -> __condition
                    __expression = __cache_140533259040800

                    # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append_140533255985120_endtime('End Time\n        ')
                    else:
                        __content = __cache_140533259040800
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append_140533255985120_endtime(__content)
                    __append_140533255985120_endtime('</abbr>')
                    __append_140533259027936('${endtime}')
                    __stream_140533255985120_endtime = ''.join(__stream_140533255985120_endtime)
                    __append_140533259027936('\n      ')
                    __msgid_140533259027936 = __re_whitespace(''.join(__stream_140533259027936)).strip()
                    if 'event_when_sameday':
                        __append(translate('event_when_sameday', mapping={'starttime': __stream_140533255985120_starttime, 'date': __stream_140533255985120_date, 'endtime': __stream_140533255985120_endtime, }, default=__msgid_140533259027936, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('\n    ')
            __append('\n\n  ')
            if (__backup_open_end_140533344517856 is __marker):
                del econtext['open_end']
            else:
                econtext['open_end'] = __backup_open_end_140533344517856
            if (__backup_whole_day_140533344794272 is __marker):
                del econtext['whole_day']
            else:
                econtext['whole_day'] = __backup_whole_day_140533344794272
            if (__backup_date_dict_140533344565328 is __marker):
                del econtext['date_dict']
            else:
                econtext['date_dict'] = __backup_date_dict_140533344565328
            __append('\n')
            __i18n_domain = __previous_i18n_domain_140533344619776
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }