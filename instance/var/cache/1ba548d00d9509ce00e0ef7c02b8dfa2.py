# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/plone/app/z3cform/templates/widget.pt'

__tokens = {331: ('nocall:context', 6, 14), 359: (' python:widget.erro', 7, 12), 398: ("s python:error and ' error' or ", 8, 17), 450: ("es python: (None, '', [], ('', '', '', '00', '00', ''), ('', '', '", 9, 17), 536: ("ass python: (widget.value in empty_values) and ' empty' o", 10, 15), 12: ("mb-3 field fieldname-${python:widget.name} widget-mode-${python:widget.mode}${error_class}${empty_class} ${python:getattr(widget, 'wrapper_css_class', False) or False}", 1, 12), 35: ('python:widget.name', 1, 35), 69: ('python:widget.mode', 1, 69), 90: ('error_class', 1, 90), 104: ('empty_class', 1, 104), 119: ("python:getattr(widget, 'wrapper_css_class', False) or False", 1, 119), 190: ('formfield-${python:widget.id}', 2, 9), 202: ('python:widget.id', 2, 21), 283: ('${widget/name}', 4, 21), 285: ('widget/name', 4, 23), 720: ("python: widget.mode == 'input' and widget.label", 16, 24), 675: ('${python:widget.id}', 15, 14), 677: ('python:widget.id', 15, 16), 796: ('python:widget.label', 18, 23), 943: ('python:widget.required', 24, 25), 1106: ("python: widget.mode == 'display' and widget.label", 29, 20), 1184: ('python:widget.label', 31, 23), 1348: ('python:widget.render()', 38, 32), 1444: ("python: getattr(widget, 'description', widget.field.description)", 43, 21), 1541: ("python:description and widget.mode == 'input'", 45, 22), 1618: ('description', 46, 30), 1708: ('error', 52, 22), 1745: ('python:error.render() or False', 53, 30)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140097252585632 = {'class': 'form-text', }
_static_140097248066096 = {'type': 'text', }
_static_140097248061440 = {'class': 'widget-label form-label d-block', }
_static_140097248064560 = {'class': 'required', 'title': 'Required', }
_static_140097412968080 = {}
_static_140097248062064 = {'class': 'form-label', 'for': '${python:widget.id}', }
_static_140097413192176 = __C2ZContextWrapper
_static_140097413192464 = __compile_zt_expr
_static_140097248055344 = {'class': "mb-3 field fieldname-${python:widget.name} widget-mode-${python:widget.mode}${error_class}${empty_class} ${python:getattr(widget, 'wrapper_css_class', False) or False}", 'id': 'formfield-${python:widget.id}', 'data-fieldname': '${widget/name}', }

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

    def render_widget_wrapper(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __slot_widget = econtext['__slot_widget'].pop()
        except:
            __slot_widget = None

        try:
            getname = econtext.get_name
            get = econtext.get

            # <Static value=<ast.Dict object at 0x7f6aeeb45030> name=None at 7f6aeeb44fa0> -> __attrs_140097248052128
            __attrs_140097248052128 = _static_140097248055344
            __backup_widget_140097247587408 = get('widget', __marker)

            # <Value 'nocall:context' (6:14)> -> __value
            __token = 331
            try:
                __zt_tmp = __attrs_140097248052128
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('nocall', 'context', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['widget'] = __value
            __backup_error_140097252541200 = get('error', __marker)

            # <Value 'python:widget.error' (7:12)> -> __value
            __token = 359
            try:
                __zt_tmp = __attrs_140097248052128
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('python', 'widget.error', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['error'] = __value
            __backup_error_class_140097245753840 = get('error_class', __marker)

            # <Value "python:error and ' error' or ''" (8:17)> -> __value
            __token = 398
            try:
                __zt_tmp = __attrs_140097248052128
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('python', "error and ' error' or ''", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['error_class'] = __value
            __backup_empty_values_140097245766144 = get('empty_values', __marker)

            # <Value "python: (None, '', [], ('', '', '', '00', '00', ''), ('', '', ''))" (9:17)> -> __value
            __token = 450
            try:
                __zt_tmp = __attrs_140097248052128
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('python', " (None, '', [], ('', '', '', '00', '00', ''), ('', '', ''))", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['empty_values'] = __value
            __backup_empty_class_140097252359568 = get('empty_class', __marker)

            # <Value "python: (widget.value in empty_values) and ' empty' or ''" (10:15)> -> __value
            __token = 536
            try:
                __zt_tmp = __attrs_140097248052128
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('python', " (widget.value in empty_values) and ' empty' or ''", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['empty_class'] = __value
            __previous_i18n_domain_140097248056736 = __i18n_domain
            __i18n_domain = 'plone'

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div')

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097248054528
            __default_140097248054528 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution "mb-3 field fieldname-${python:widget.name} widget-mode-${python:widget.mode}${error_class}${empty_class} ${python:getattr(widget, 'wrapper_css_class', False) or False}" (1:12)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f6aeeb44ca0> -> __attr_class
            __token = 12
            __token = 35
            try:
                __zt_tmp = __attrs_140097248052128
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_140097413192464('python', 'widget.name', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
            __token = 69
            try:
                __zt_tmp = __attrs_140097248052128
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class_67 = _static_140097413192464('python', 'widget.mode', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_class_67 = __quote(__attr_class_67, '"', '&quot;', None, _DEFAULT_MARKER)
            __token = 90
            try:
                __zt_tmp = __attrs_140097248052128
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class_88 = _static_140097413192464('path', 'error_class', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_class_88 = __quote(__attr_class_88, '"', '&quot;', None, _DEFAULT_MARKER)
            __token = 104
            try:
                __zt_tmp = __attrs_140097248052128
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class_102 = _static_140097413192464('path', 'empty_class', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_class_102 = __quote(__attr_class_102, '"', '&quot;', None, _DEFAULT_MARKER)
            __token = 119
            try:
                __zt_tmp = __attrs_140097248052128
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class_117 = _static_140097413192464('python', "getattr(widget, 'wrapper_css_class', False) or False", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_class_117 = __quote(__attr_class_117, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_class = ('%s%s%s%s%s%s%s%s' % ('mb-3 field fieldname-', (__attr_class if (__attr_class is not None) else ''), ' widget-mode-', (__attr_class_67 if (__attr_class_67 is not None) else ''), (__attr_class_88 if (__attr_class_88 is not None) else ''), (__attr_class_102 if (__attr_class_102 is not None) else ''), ' ', (__attr_class_117 if (__attr_class_117 is not None) else ''), ))
            if (__attr_class is None):
                pass
            else:
                if (__attr_class is _DEFAULT_MARKER):
                    __attr_class = None
                else:
                    __tt = type(__attr_class)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __attr_class = str(__attr_class)
                    else:
                        if (__tt is bytes):
                            __attr_class = decode(__attr_class)
                        else:
                            if (__tt is not str):
                                try:
                                    __attr_class = __attr_class.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__attr_class)
                                    __attr_class = (str(__attr_class) if (__attr_class is __converted) else __converted)
                                else:
                                    __attr_class = __attr_class()
            if (__attr_class is not None):
                __append((' class="%s"' % __attr_class))

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097248051600
            __default_140097248051600 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution 'formfield-${python:widget.id}' (2:9)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f6aeeb44b50> -> __attr_id
            __token = 190
            __token = 202
            try:
                __zt_tmp = __attrs_140097248052128
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_140097413192464('python', 'widget.id', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_id = ('%s%s' % ('formfield-', (__attr_id if (__attr_id is not None) else ''), ))
            if (__attr_id is None):
                pass
            else:
                if (__attr_id is _DEFAULT_MARKER):
                    __attr_id = None
                else:
                    __tt = type(__attr_id)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __attr_id = str(__attr_id)
                    else:
                        if (__tt is bytes):
                            __attr_id = decode(__attr_id)
                        else:
                            if (__tt is not str):
                                try:
                                    __attr_id = __attr_id.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__attr_id)
                                    __attr_id = (str(__attr_id) if (__attr_id is __converted) else __converted)
                                else:
                                    __attr_id = __attr_id()
            if (__attr_id is not None):
                __append((' id="%s"' % __attr_id))

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097248051552
            __default_140097248051552 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution '${widget/name}' (4:21)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f6aeeb44220> -> __attr_data_fieldname
            __token = 283
            __token = 285
            try:
                __zt_tmp = __attrs_140097248052128
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_data_fieldname = _static_140097413192464('path', 'widget/name', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_data_fieldname = __quote(__attr_data_fieldname, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_data_fieldname = __attr_data_fieldname
            if (__attr_data_fieldname is None):
                pass
            else:
                if (__attr_data_fieldname is _DEFAULT_MARKER):
                    __attr_data_fieldname = None
                else:
                    __tt = type(__attr_data_fieldname)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __attr_data_fieldname = str(__attr_data_fieldname)
                    else:
                        if (__tt is bytes):
                            __attr_data_fieldname = decode(__attr_data_fieldname)
                        else:
                            if (__tt is not str):
                                try:
                                    __attr_data_fieldname = __attr_data_fieldname.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__attr_data_fieldname)
                                    __attr_data_fieldname = (str(__attr_data_fieldname) if (__attr_data_fieldname is __converted) else __converted)
                                else:
                                    __attr_data_fieldname = __attr_data_fieldname()
            if (__attr_data_fieldname is not None):
                __append((' data-fieldname="%s"' % __attr_data_fieldname))
            __append(' >\n  ')

            # <Static value=<ast.Dict object at 0x7f6aeeb46a70> name=None at 7f6aeeb46a10> -> __attrs_140097248061584
            __attrs_140097248061584 = _static_140097248062064

            # <Value "python: widget.mode == 'input' and widget.label" (16:24)> -> __condition
            __token = 720
            try:
                __zt_tmp = __attrs_140097248061584
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140097413192464('python', " widget.mode == 'input' and widget.label", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            if __condition:

                # <label ... (0:0)
                # --------------------------------------------------------
                __append('<label class="form-label"')

                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097248057936
                __default_140097248057936 = _DEFAULT_MARKER

                # <Interpolation value=<Substitution '${python:widget.id}' (15:14)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f6aeeb46e90> -> __attr_for
                __token = 675
                __token = 677
                try:
                    __zt_tmp = __attrs_140097248061584
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_for = _static_140097413192464('python', 'widget.id', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                __attr_for = __quote(__attr_for, '"', '&quot;', None, _DEFAULT_MARKER)
                __attr_for = __attr_for
                if (__attr_for is None):
                    pass
                else:
                    if (__attr_for is _DEFAULT_MARKER):
                        __attr_for = None
                    else:
                        __tt = type(__attr_for)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __attr_for = str(__attr_for)
                        else:
                            if (__tt is bytes):
                                __attr_for = decode(__attr_for)
                            else:
                                if (__tt is not str):
                                    try:
                                        __attr_for = __attr_for.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__attr_for)
                                        __attr_for = (str(__attr_for) if (__attr_for is __converted) else __converted)
                                    else:
                                        __attr_for = __attr_for()
                if (__attr_for is not None):
                    __append((' for="%s"' % __attr_for))
                __append(' >\n    ')

                # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097248063600
                __attrs_140097248063600 = _static_140097412968080

                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097248063696
                __default_140097248063696 = _DEFAULT_MARKER

                # <Value 'python:widget.label' (18:23)> -> __cache_140097248063024
                __token = 796
                try:
                    __zt_tmp = __attrs_140097248063600
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140097248063024 = _static_140097413192464('python', 'widget.label', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                # <BinOp left=<Value 'python:widget.label' (18:23)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeeb46ef0> -> __condition
                __expression = __cache_140097248063024

                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span >label</span>')
                else:
                    __content = __cache_140097248063024
                    __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('\n\n    ')

                # <Static value=<ast.Dict object at 0x7f6aeeb47430> name=None at 7f6aeeb47d30> -> __attrs_140097248059664
                __attrs_140097248059664 = _static_140097248064560

                # <Value 'python:widget.required' (24:25)> -> __condition
                __token = 943
                try:
                    __zt_tmp = __attrs_140097248059664
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140097413192464('python', 'widget.required', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span class="required"')

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097248059232
                    __default_140097248059232 = _DEFAULT_MARKER

                    # <Translate msgid='title_required' node=<ast.Constant object at 0x7f6aeeb47c40> at 7f6aeeb47d00> -> __attr_title
                    __attr_title = 'Required'
                    __attr_title = translate('title_required', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    if (__attr_title is not None):
                        __append((' title="%s"' % __attr_title))
                    __append(' ></span>')
                __append('\n  </label>')
            __append('\n  ')

            # <Static value=<ast.Dict object at 0x7f6aeeb46800> name=None at 7f6aeeb47460> -> __attrs_140097248065328
            __attrs_140097248065328 = _static_140097248061440

            # <Value "python: widget.mode == 'display' and widget.label" (29:20)> -> __condition
            __token = 1106
            try:
                __zt_tmp = __attrs_140097248065328
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140097413192464('python', " widget.mode == 'display' and widget.label", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            if __condition:

                # <b ... (0:0)
                # --------------------------------------------------------
                __append('<b class="widget-label form-label d-block" >\n    ')

                # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097248061056
                __attrs_140097248061056 = _static_140097412968080

                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097248053328
                __default_140097248053328 = _DEFAULT_MARKER

                # <Value 'python:widget.label' (31:23)> -> __cache_140097248057984
                __token = 1184
                try:
                    __zt_tmp = __attrs_140097248061056
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140097248057984 = _static_140097413192464('python', 'widget.label', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                # <BinOp left=<Value 'python:widget.label' (31:23)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeeb45840> -> __condition
                __expression = __cache_140097248057984

                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span >label</span>')
                else:
                    __content = __cache_140097248057984
                    __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('\n  </b>')
            __append('\n\n  ')
            if (__slot_widget is None):

                # <Static value=<ast.Dict object at 0x7f6aeeb47a30> name=None at 7f6aeeb47a00> -> __attrs_140097248057696
                __attrs_140097248057696 = _static_140097248066096

                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097248057792
                __default_140097248057792 = _DEFAULT_MARKER

                # <Value 'python:widget.render()' (38:32)> -> __cache_140097248059760
                __token = 1348
                try:
                    __zt_tmp = __attrs_140097248057696
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140097248059760 = _static_140097413192464('python', 'widget.render()', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                # <BinOp left=<Value 'python:widget.render()' (38:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeeb47b20> -> __condition
                __expression = __cache_140097248059760

                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input type="text" />')
                else:
                    __content = __cache_140097248059760
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
            else:
                __slot_widget(__stream, econtext.copy(), rcontext)
            __append('\n\n  ')

            # <Static value=<ast.Dict object at 0x7f6aeef970a0> name=None at 7f6aeef941f0> -> __attrs_140097252578480
            __attrs_140097252578480 = _static_140097252585632
            __backup_description_140097251878864 = get('description', __marker)

            # <Value "python: getattr(widget, 'description', widget.field.description)" (43:21)> -> __value
            __token = 1444
            try:
                __zt_tmp = __attrs_140097252578480
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('python', " getattr(widget, 'description', widget.field.description)", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['description'] = __value

            # <Value "python:description and widget.mode == 'input'" (45:22)> -> __condition
            __token = 1541
            try:
                __zt_tmp = __attrs_140097252578480
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140097413192464('python', "description and widget.mode == 'input'", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="form-text" >')

                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252587696
                __default_140097252587696 = _DEFAULT_MARKER

                # <Value 'description' (46:30)> -> __cache_140097252577136
                __token = 1618
                try:
                    __zt_tmp = __attrs_140097252578480
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140097252577136 = _static_140097413192464('path', 'description', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                # <BinOp left=<Value 'description' (46:30)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeef96530> -> __condition
                __expression = __cache_140097252577136

                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('\n      help text\n  ')
                else:
                    __content = __cache_140097252577136
                    __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('</div>')
            if (__backup_description_140097251878864 is __marker):
                del econtext['description']
            else:
                econtext['description'] = __backup_description_140097251878864
            __append('\n\n  ')

            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097252582176
            __attrs_140097252582176 = _static_140097412968080

            # <Value 'error' (52:22)> -> __condition
            __token = 1708
            try:
                __zt_tmp = __attrs_140097252582176
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140097413192464('path', 'error', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            if __condition:

                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252575216
                __default_140097252575216 = _DEFAULT_MARKER

                # <Value 'python:error.render() or False' (53:30)> -> __cache_140097252581840
                __token = 1745
                try:
                    __zt_tmp = __attrs_140097252582176
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140097252581840 = _static_140097413192464('python', 'error.render() or False', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                # <BinOp left=<Value 'python:error.render() or False' (53:30)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeef94220> -> __condition
                __expression = __cache_140097252581840

                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div >\n        Error\n  </div>')
                else:
                    __content = __cache_140097252581840
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
            __append('\n\n</div>')
            __i18n_domain = __previous_i18n_domain_140097248056736
            if (__backup_empty_class_140097252359568 is __marker):
                del econtext['empty_class']
            else:
                econtext['empty_class'] = __backup_empty_class_140097252359568
            if (__backup_empty_values_140097245766144 is __marker):
                del econtext['empty_values']
            else:
                econtext['empty_values'] = __backup_empty_values_140097245766144
            if (__backup_error_class_140097245753840 is __marker):
                del econtext['error_class']
            else:
                econtext['error_class'] = __backup_error_class_140097245753840
            if (__backup_error_140097252541200 is __marker):
                del econtext['error']
            else:
                econtext['error'] = __backup_error_140097252541200
            if (__backup_widget_140097247587408 is __marker):
                del econtext['widget']
            else:
                econtext['widget'] = __backup_widget_140097247587408
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
            __token = None
            render_widget_wrapper(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_widget_wrapper': render_widget_wrapper, 'render': render, }