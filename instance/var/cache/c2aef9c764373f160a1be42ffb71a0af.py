# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/plone/app/dexterity/browser/container.pt'

__tokens = {476: ('view/widgets/values|nothing', 15, 34), 542: ("python:widget.__name__ not in ('IBasic.title', 'IBasic.description', 'title', 'description',)", 16, 36), 685: ('widget/@@ploneform-render-widget', 17, 47), 803: ('view/groups|nothing', 21, 36), 882: ("python:''.join((group.prefix, 'groups.', group.__name__)).replace('.', '-')", 23, 23), 1020: ('group/label', 26, 31), 1083: ('group/widgets/values', 27, 40), 1153: ('widget/@@ploneform-render-widget', 28, 47), 1434: ('nocall:context/folder_listing', 37, 28), 1501: (' view/macros/listing|view/index/macros/listin', 38, 36), 1613: ('listing_macro', 40, 40), 1613: ('listing_macro', 40, 40), 247: ('context/@@main_template/macros/master', 6, 23), 247: ('context/@@main_template/macros/master', 6, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from collections import deque as _deque
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140533345719040 = 'master'
_static_140533343896288 = 'listing_macro'
_static_140533343908144 = {'id': 'folder-listing', }
_static_140533343900608 = {'id': "python:''.join((group.prefix, 'groups.', group.__name__)).replace('.', '-')", }
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

            # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533345715776
            __attrs_140533345715776 = _static_140533416833664
            __append('\n\n        ')

            # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533343897824
            __attrs_140533343897824 = _static_140533416833664
            __backup_widget_140533345714576 = get('widget', __marker)

            # <Value 'view/widgets/values|nothing' (15:34)> -> __iterator
            __token = 476
            try:
                __zt_tmp = __attrs_140533343897824
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140533417025280('path', 'view/widgets/values|nothing', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
            (__iterator, ____index_140533343895616, ) = getname('repeat')('widget', __iterator)
            econtext['widget'] = None
            for __item in __iterator:
                econtext['widget'] = __item
                __append('\n          ')

                # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533343895952
                __attrs_140533343895952 = _static_140533416833664

                # <Value "python:widget.__name__ not in ('IBasic.title', 'IBasic.description', 'title', 'description',)" (16:36)> -> __condition
                __token = 542
                try:
                    __zt_tmp = __attrs_140533343895952
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140533417025280('python', "widget.__name__ not in ('IBasic.title', 'IBasic.description', 'title', 'description',)", econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                if __condition:
                    __append('\n            ')

                    # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533343908000
                    __attrs_140533343908000 = _static_140533416833664

                    # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533343899696
                    __default_140533343899696 = _DEFAULT_MARKER

                    # <Value 'widget/@@ploneform-render-widget' (17:47)> -> __cache_140533343898688
                    __token = 685
                    try:
                        __zt_tmp = __attrs_140533343908000
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140533343898688 = _static_140533417025280('path', 'widget/@@ploneform-render-widget', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))

                    # <BinOp left=<Value 'widget/@@ploneform-render-widget' (17:47)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fd07c5afbe0> at 7fd0780acc70> -> __condition
                    __expression = __cache_140533343898688

                    # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140533343898688
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('\n          ')
                __append('\n        ')
                ____index_140533343895616 -= 1
                if (____index_140533343895616 > 0):
                    __append('')
            if (__backup_widget_140533345714576 is __marker):
                del econtext['widget']
            else:
                econtext['widget'] = __backup_widget_140533345714576
            __append('\n\n        ')

            # <Static value=<ast.Dict object at 0x7fd0780ad3c0> name=None at 7fd0780ad6c0> -> __attrs_140533343902384
            __attrs_140533343902384 = _static_140533343900608
            __backup_group_140533343910880 = get('group', __marker)

            # <Value 'view/groups|nothing' (21:36)> -> __iterator
            __token = 803
            try:
                __zt_tmp = __attrs_140533343902384
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140533417025280('path', 'view/groups|nothing', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
            (__iterator, ____index_140533343910208, ) = getname('repeat')('group', __iterator)
            econtext['group'] = None
            for __item in __iterator:
                econtext['group'] = __item

                # <fieldset ... (0:0)
                # --------------------------------------------------------
                __append('<fieldset')

                # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533343911168
                __default_140533343911168 = _DEFAULT_MARKER

                # <Substitution "python:''.join((group.prefix, 'groups.', group.__name__)).replace('.', '-')" (23:23)> -> __attr_id
                __token = 882
                try:
                    __zt_tmp = __attrs_140533343902384
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_id = _static_140533417025280('python', "''.join((group.prefix, 'groups.', group.__name__)).replace('.', '-')", econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_id is not None):
                    __append((' id="%s"' % __attr_id))
                __append(' >\n          ')

                # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533343900992
                __attrs_140533343900992 = _static_140533416833664

                # <legend ... (0:0)
                # --------------------------------------------------------
                __append('<legend>')

                # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533343897248
                __default_140533343897248 = _DEFAULT_MARKER

                # <Value 'group/label' (26:31)> -> __cache_140533343896528
                __token = 1020
                try:
                    __zt_tmp = __attrs_140533343900992
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140533343896528 = _static_140533417025280('path', 'group/label', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))

                # <BinOp left=<Value 'group/label' (26:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fd07c5afbe0> at 7fd0780ac970> -> __condition
                __expression = __cache_140533343896528

                # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140533343896528
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</legend>\n          ')

                # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533343900032
                __attrs_140533343900032 = _static_140533416833664
                __backup_widget_140533343910832 = get('widget', __marker)

                # <Value 'group/widgets/values' (27:40)> -> __iterator
                __token = 1083
                try:
                    __zt_tmp = __attrs_140533343900032
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140533417025280('path', 'group/widgets/values', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                (__iterator, ____index_140533343898832, ) = getname('repeat')('widget', __iterator)
                econtext['widget'] = None
                for __item in __iterator:
                    econtext['widget'] = __item
                    __append('\n            ')

                    # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533343905984
                    __attrs_140533343905984 = _static_140533416833664

                    # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533343896912
                    __default_140533343896912 = _DEFAULT_MARKER

                    # <Value 'widget/@@ploneform-render-widget' (28:47)> -> __cache_140533343903920
                    __token = 1153
                    try:
                        __zt_tmp = __attrs_140533343905984
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140533343903920 = _static_140533417025280('path', 'widget/@@ploneform-render-widget', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))

                    # <BinOp left=<Value 'widget/@@ploneform-render-widget' (28:47)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fd07c5afbe0> at 7fd0780aeb90> -> __condition
                    __expression = __cache_140533343903920

                    # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140533343903920
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('\n          ')
                    ____index_140533343898832 -= 1
                    if (____index_140533343898832 > 0):
                        __append('')
                if (__backup_widget_140533343910832 is __marker):
                    del econtext['widget']
                else:
                    econtext['widget'] = __backup_widget_140533343910832
                __append('\n        </fieldset>')
                ____index_140533343910208 -= 1
                if (____index_140533343910208 > 0):
                    __append('\n        ')
            if (__backup_group_140533343910880 is __marker):
                del econtext['group']
            else:
                econtext['group'] = __backup_group_140533343910880
            __append('\n\n        ')

            # <Static value=<ast.Dict object at 0x7fd0780af130> name=None at 7fd0780ae860> -> __attrs_140533343911504
            __attrs_140533343911504 = _static_140533343908144

            # <fieldset ... (0:0)
            # --------------------------------------------------------
            __append('<fieldset id="folder-listing">\n          ')

            # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533343906464
            __attrs_140533343906464 = _static_140533416833664
            __previous_i18n_domain_140533343903152 = __i18n_domain
            __i18n_domain = 'plone'

            # <legend ... (0:0)
            # --------------------------------------------------------
            __append('<legend >')
            __stream_140533343908768 = []
            __append_140533343908768 = __stream_140533343908768.append
            __append_140533343908768('Contents')
            __msgid_140533343908768 = __re_whitespace(''.join(__stream_140533343908768)).strip()
            if __msgid_140533343908768:
                __append(translate(__msgid_140533343908768, mapping=None, default=__msgid_140533343908768, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</legend>')
            __i18n_domain = __previous_i18n_domain_140533343903152
            __append('\n          ')

            # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533343902336
            __attrs_140533343902336 = _static_140533416833664
            __backup_view_140533345720720 = get('view', __marker)

            # <Value 'nocall:context/folder_listing' (37:28)> -> __value
            __token = 1434
            try:
                __zt_tmp = __attrs_140533343902336
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140533417025280('nocall', 'context/folder_listing', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
            econtext['view'] = __value
            __backup_listing_macro_140533345717024 = get('listing_macro', __marker)

            # <Value 'view/macros/listing|view/index/macros/listing' (38:36)> -> __value
            __token = 1501
            try:
                __zt_tmp = __attrs_140533343902336
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140533417025280('path', 'view/macros/listing|view/index/macros/listing', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
            econtext['listing_macro'] = __value
            __append('\n            ')

            # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533343908432
            __attrs_140533343908432 = _static_140533416833664
            __backup_macroname_140533378396544 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7fd0780ac2e0> name=None at 7fd0780af520> -> __value
            __value = _static_140533343896288
            econtext['macroname'] = __value

            # <Value 'listing_macro' (40:40)> -> __macro
            __token = 1613
            try:
                __zt_tmp = __attrs_140533343908432
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140533417025280('path', 'listing_macro', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
            __token = 1613
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140533378396544 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140533378396544
            __append('\n          ')
            if (__backup_listing_macro_140533345717024 is __marker):
                del econtext['listing_macro']
            else:
                econtext['listing_macro'] = __backup_listing_macro_140533345717024
            if (__backup_view_140533345720720 is __marker):
                del econtext['view']
            else:
                econtext['view'] = __backup_view_140533345720720
            __append('\n        </fieldset>\n\n      ')
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

            # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533345720192
            __attrs_140533345720192 = _static_140533416833664
            __previous_i18n_domain_140533345719520 = __i18n_domain
            __i18n_domain = 'plone'
            __backup_macroname_140533375518336 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7fd078269300> name=None at 7fd0782693f0> -> __value
            __value = _static_140533345719040
            econtext['macroname'] = __value

            def __fill_content_core(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533345716304
                __attrs_140533345716304 = _static_140533416833664
                __append('\n      ')
                __token = None
                render_content_core(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append('\n    ')
            _slots = econtext['__slot_content_core'] = _deque((__fill_content_core, ))

            # <Value 'context/@@main_template/macros/master' (6:23)> -> __macro
            __token = 247
            try:
                __zt_tmp = __attrs_140533345720192
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140533417025280('path', 'context/@@main_template/macros/master', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
            __token = 247
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140533375518336 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140533375518336
            __i18n_domain = __previous_i18n_domain_140533345719520
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_content_core': render_content_core, 'render': render, }