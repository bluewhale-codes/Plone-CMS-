# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/plone/app/dexterity/browser/overview.pt'

__tokens = {238: ('view/widgets/title/@@ploneform-render-widget', 6, 38), 325: ('view/widgets/description/@@ploneform-render-widget', 7, 38), 410: ("python:'filter_content_types' in view.fields", 9, 29), 592: ('nocall:view/widgets/filter_content_types', 12, 27), 658: (' context/valu', 13, 24), 989: ('context/name', 21, 28), 1033: (" python:'checked' if 'none' in value else Non", 22, 30), 1395: ('context/name', 31, 28), 1439: (" python:'checked' if 'all' in value else Non", 32, 30), 1803: ('context/name', 41, 28), 1847: (" python:'checked' if 'some' in value else Non", 42, 30), 2082: ('view/widgets/allowed_content_types/render', 46, 48), 737: ('context/@@ploneform-render-widget/widget-wrapper', 15, 43), 737: ('context/@@ploneform-render-widget/widget-wrapper', 15, 43), 86: ('context/@@ploneform-macros/titlelessform', 2, 27), 86: ('context/@@ploneform-macros/titlelessform', 2, 27)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from collections import deque as _deque
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140097340073792 = {'type': 'radio', 'value': 'some', 'name': 'context/name', 'checked': "python:'checked' if 'some' in value else None", }
_static_140097245754464 = {'type': 'radio', 'value': 'all', 'name': 'context/name', 'checked': "python:'checked' if 'all' in value else None", }
_static_140097245744336 = {'type': 'radio', 'value': 'none', 'name': 'context/name', 'checked': "python:'checked' if 'none' in value else None", }
_static_140097338290000 = 'widget-wrapper'
_static_140097413192176 = __C2ZContextWrapper
_static_140097413192464 = __compile_zt_expr
_static_140097245745296 = 'titlelessform'
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

            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097245745584
            __attrs_140097245745584 = _static_140097412968080
            __previous_i18n_domain_140097245756576 = __i18n_domain
            __i18n_domain = 'plone'
            __backup_macroname_140097247102080 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f6aee911090> name=None at 7f6aee9120b0> -> __value
            __value = _static_140097245745296
            econtext['macroname'] = __value

            def __fill_fields(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097245746304
                __attrs_140097245746304 = _static_140097412968080
                __append('\n    ')

                # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097339909712
                __attrs_140097339909712 = _static_140097412968080

                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097245756480
                __default_140097245756480 = _DEFAULT_MARKER

                # <Value 'view/widgets/title/@@ploneform-render-widget' (6:38)> -> __cache_140097245742512
                __token = 238
                try:
                    __zt_tmp = __attrs_140097339909712
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140097245742512 = _static_140097413192464('path', 'view/widgets/title/@@ploneform-render-widget', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                # <BinOp left=<Value 'view/widgets/title/@@ploneform-render-widget' (6:38)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aee913d60> -> __condition
                __expression = __cache_140097245742512

                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140097245742512
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n    ')

                # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097340075568
                __attrs_140097340075568 = _static_140097412968080

                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097340075472
                __default_140097340075472 = _DEFAULT_MARKER

                # <Value 'view/widgets/description/@@ploneform-render-widget' (7:38)> -> __cache_140097339910480
                __token = 325
                try:
                    __zt_tmp = __attrs_140097340075568
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140097339910480 = _static_140097413192464('path', 'view/widgets/description/@@ploneform-render-widget', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                # <BinOp left=<Value 'view/widgets/description/@@ploneform-render-widget' (7:38)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6af42dcbb0> -> __condition
                __expression = __cache_140097339910480

                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140097339910480
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n\n    ')

                # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097340079696
                __attrs_140097340079696 = _static_140097412968080

                # <Value "python:'filter_content_types' in view.fields" (9:29)> -> __condition
                __token = 410
                try:
                    __zt_tmp = __attrs_140097340079696
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140097413192464('python', "'filter_content_types' in view.fields", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                if __condition:

                    # <fieldset ... (0:0)
                    # --------------------------------------------------------
                    __append('<fieldset>\n      ')

                    # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097342770576
                    __attrs_140097342770576 = _static_140097412968080

                    # <legend ... (0:0)
                    # --------------------------------------------------------
                    __append('<legend>')
                    __stream_140097339905536 = []
                    __append_140097339905536 = __stream_140097339905536.append
                    __append_140097339905536('Contained items')
                    __msgid_140097339905536 = __re_whitespace(''.join(__stream_140097339905536)).strip()
                    if 'label_contained_items':
                        __append(translate('label_contained_items', mapping=None, default=__msgid_140097339905536, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</legend>\n      ')

                    # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097338289040
                    __attrs_140097338289040 = _static_140097412968080
                    __backup_context_140097247475600 = get('context', __marker)

                    # <Value 'nocall:view/widgets/filter_content_types' (12:27)> -> __value
                    __token = 592
                    try:
                        __zt_tmp = __attrs_140097338289040
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140097413192464('nocall', 'view/widgets/filter_content_types', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    econtext['context'] = __value
                    __backup_value_140097247586688 = get('value', __marker)

                    # <Value 'context/value' (13:24)> -> __value
                    __token = 658
                    try:
                        __zt_tmp = __attrs_140097338289040
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140097413192464('path', 'context/value', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    econtext['value'] = __value
                    __append('\n        ')

                    # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097338286352
                    __attrs_140097338286352 = _static_140097412968080
                    __backup_macroname_140097247718336 = get('macroname', __marker)

                    # <Static value=<ast.Constant object at 0x7f6af4152f50> name=None at 7f6af41509a0> -> __value
                    __value = _static_140097338290000
                    econtext['macroname'] = __value

                    def __fill_widget(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                        getname = econtext.get_name
                        get = econtext.get

                        # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097245745536
                        __attrs_140097245745536 = _static_140097412968080
                        __append('\n            ')

                        # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097245746352
                        __attrs_140097245746352 = _static_140097412968080

                        # <label ... (0:0)
                        # --------------------------------------------------------
                        __append('<label>\n              ')

                        # <Static value=<ast.Dict object at 0x7f6aee910cd0> name=None at 7f6aee912cb0> -> __attrs_140097245741648
                        __attrs_140097245741648 = _static_140097245744336

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input type="radio" value="none"')

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097245756624
                        __default_140097245756624 = _DEFAULT_MARKER

                        # <Substitution 'context/name' (21:28)> -> __attr_name
                        __token = 989
                        try:
                            __zt_tmp = __attrs_140097245741648
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_name = _static_140097413192464('path', 'context/name', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_name is not None):
                            __append((' name="%s"' % __attr_name))

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097245750624
                        __default_140097245750624 = _DEFAULT_MARKER

                        # <Boolean "python:'checked' if 'none' in value else None" (22:30)> -> __attr_checked
                        __token = 1033
                        try:
                            __zt_tmp = __attrs_140097245741648
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_checked = _static_140097413192464('python', "'checked' if 'none' in value else None", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        if (__attr_checked is _DEFAULT_MARKER):
                            __attr_checked = None
                        else:
                            if __attr_checked:
                                __attr_checked = 'checked'
                            else:
                                __attr_checked = None
                        if (__attr_checked is not None):
                            __append((' checked="%s"' % __attr_checked))
                        __append(' />\n              ')

                        # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097245752400
                        __attrs_140097245752400 = _static_140097412968080
                        __stream_140097245748560 = []
                        __append_140097245748560 = __stream_140097245748560.append
                        __append_140097245748560('No content types')
                        __msgid_140097245748560 = __re_whitespace(''.join(__stream_140097245748560)).strip()
                        if 'label_no_content_types':
                            __append(translate('label_no_content_types', mapping=None, default=__msgid_140097245748560, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('\n            </label>')

                        # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097245745200
                        __attrs_140097245745200 = _static_140097412968080

                        # <br ... (0:0)
                        # --------------------------------------------------------
                        __append('<br />\n            ')

                        # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097245741168
                        __attrs_140097245741168 = _static_140097412968080

                        # <label ... (0:0)
                        # --------------------------------------------------------
                        __append('<label>\n              ')

                        # <Static value=<ast.Dict object at 0x7f6aee913460> name=None at 7f6aee910790> -> __attrs_140097245748512
                        __attrs_140097245748512 = _static_140097245754464

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input type="radio" value="all"')

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097245752592
                        __default_140097245752592 = _DEFAULT_MARKER

                        # <Substitution 'context/name' (31:28)> -> __attr_name
                        __token = 1395
                        try:
                            __zt_tmp = __attrs_140097245748512
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_name = _static_140097413192464('path', 'context/name', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_name is not None):
                            __append((' name="%s"' % __attr_name))

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097245742608
                        __default_140097245742608 = _DEFAULT_MARKER

                        # <Boolean "python:'checked' if 'all' in value else None" (32:30)> -> __attr_checked
                        __token = 1439
                        try:
                            __zt_tmp = __attrs_140097245748512
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_checked = _static_140097413192464('python', "'checked' if 'all' in value else None", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        if (__attr_checked is _DEFAULT_MARKER):
                            __attr_checked = None
                        else:
                            if __attr_checked:
                                __attr_checked = 'checked'
                            else:
                                __attr_checked = None
                        if (__attr_checked is not None):
                            __append((' checked="%s"' % __attr_checked))
                        __append(' />\n              ')

                        # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097340073888
                        __attrs_140097340073888 = _static_140097412968080
                        __stream_140097245751152 = []
                        __append_140097245751152 = __stream_140097245751152.append
                        __append_140097245751152('All content types')
                        __msgid_140097245751152 = __re_whitespace(''.join(__stream_140097245751152)).strip()
                        if 'label_all_content_types':
                            __append(translate('label_all_content_types', mapping=None, default=__msgid_140097245751152, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('\n            </label>')

                        # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097340068560
                        __attrs_140097340068560 = _static_140097412968080

                        # <br ... (0:0)
                        # --------------------------------------------------------
                        __append('<br />\n            ')

                        # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097340064000
                        __attrs_140097340064000 = _static_140097412968080

                        # <label ... (0:0)
                        # --------------------------------------------------------
                        __append('<label>\n              ')

                        # <Static value=<ast.Dict object at 0x7f6af4306740> name=None at 7f6af4307a00> -> __attrs_140097340065680
                        __attrs_140097340065680 = _static_140097340073792

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input type="radio" value="some"')

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097340071776
                        __default_140097340071776 = _DEFAULT_MARKER

                        # <Substitution 'context/name' (41:28)> -> __attr_name
                        __token = 1803
                        try:
                            __zt_tmp = __attrs_140097340065680
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_name = _static_140097413192464('path', 'context/name', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_name is not None):
                            __append((' name="%s"' % __attr_name))

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097340074800
                        __default_140097340074800 = _DEFAULT_MARKER

                        # <Boolean "python:'checked' if 'some' in value else None" (42:30)> -> __attr_checked
                        __token = 1847
                        try:
                            __zt_tmp = __attrs_140097340065680
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_checked = _static_140097413192464('python', "'checked' if 'some' in value else None", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        if (__attr_checked is _DEFAULT_MARKER):
                            __attr_checked = None
                        else:
                            if __attr_checked:
                                __attr_checked = 'checked'
                            else:
                                __attr_checked = None
                        if (__attr_checked is not None):
                            __append((' checked="%s"' % __attr_checked))
                        __append(' />\n              ')

                        # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097340077200
                        __attrs_140097340077200 = _static_140097412968080
                        __stream_140097340072832 = []
                        __append_140097340072832 = __stream_140097340072832.append
                        __append_140097340072832('Some content types:')
                        __msgid_140097340072832 = __re_whitespace(''.join(__stream_140097340072832)).strip()
                        if 'label_some_content_types':
                            __append(translate('label_some_content_types', mapping=None, default=__msgid_140097340072832, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('\n              ')

                        # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097340072112
                        __attrs_140097340072112 = _static_140097412968080

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097340069520
                        __default_140097340069520 = _DEFAULT_MARKER

                        # <Value 'view/widgets/allowed_content_types/render' (46:48)> -> __cache_140097340073072
                        __token = 2082
                        try:
                            __zt_tmp = __attrs_140097340072112
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140097340073072 = _static_140097413192464('path', 'view/widgets/allowed_content_types/render', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                        # <BinOp left=<Value 'view/widgets/allowed_content_types/render' (46:48)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6af4305180> -> __condition
                        __expression = __cache_140097340073072

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140097340073072
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        __append('\n            </label>\n          ')
                    _slots = econtext['__slot_widget'] = _deque((__fill_widget, ))

                    # <Value 'context/@@ploneform-render-widget/widget-wrapper' (15:43)> -> __macro
                    __token = 737
                    try:
                        __zt_tmp = __attrs_140097338286352
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __macro = _static_140097413192464('path', 'context/@@ploneform-render-widget/widget-wrapper', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    __token = 737
                    __m = __macro.include
                    __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                    econtext.update(rcontext)
                    if (__backup_macroname_140097247718336 is __marker):
                        del econtext['macroname']
                    else:
                        econtext['macroname'] = __backup_macroname_140097247718336
                    __append('\n      ')
                    if (__backup_value_140097247586688 is __marker):
                        del econtext['value']
                    else:
                        econtext['value'] = __backup_value_140097247586688
                    if (__backup_context_140097247475600 is __marker):
                        del econtext['context']
                    else:
                        econtext['context'] = __backup_context_140097247475600
                    __append('\n    </fieldset>')
                __append('\n\n  ')
            _slots = econtext['__slot_fields'] = _deque((__fill_fields, ))

            # <Value 'context/@@ploneform-macros/titlelessform' (2:27)> -> __macro
            __token = 86
            try:
                __zt_tmp = __attrs_140097245745584
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140097413192464('path', 'context/@@ploneform-macros/titlelessform', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __token = 86
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140097247102080 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140097247102080
            __i18n_domain = __previous_i18n_domain_140097245756576
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }