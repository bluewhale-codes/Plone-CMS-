# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/plone/schemaeditor/browser/schema/schema_listing.pt'

__tokens = {312: ('${context/absolute_url}/@@add-field', 9, 11), 314: ('context/absolute_url', 9, 13), 582: ('context/enableFieldsets', 18, 20), 522: ('${context/absolute_url}/@@add-fieldset', 17, 11), 524: ('context/absolute_url', 17, 13), 839: ('context/@@authenticator/authenticator', 26, 36), 1918: ('python:[view] + list(view.groups)', 82, 35), 2019: ('repeat/group/index', 84, 34), 2069: (' python:view.can_delete_fieldset(group', 85, 30), 2188: ('string:fieldset-${fieldset_name}', 88, 23), 2247: (' string:kssattr-fieldset-${fieldset_name', 89, 25), 2328: ("s python:(repeat['group'].start or can_delete) and 'true' or 'fals", 90, 38), 2491: ('python:group.label or view.default_fieldset_label', 95, 31), 2593: ('group_name', 97, 31), 2700: ('delete-fieldset-${fieldset_name}', 101, 17), 2718: ('fieldset_name', 101, 35), 2753: ('${context/absolute_url}/@@delete-fieldset?name=${python:group.__name__}&amp;_authenticator=${context/@@authenticator/token}', 102, 19), 2755: ('context/absolute_url', 102, 21), 2802: ('python:group.__name__', 102, 68), 2846: ('context/@@authenticator/token', 102, 112), 3038: ('group/widgets/errors', 108, 30), 3119: ('errors', 110, 36), 3166: ('errors', 111, 39), 3255: ('not:nocall:error/widget', 114, 32), 3320: ('error/render', 115, 40), 3416: ('group/widgets/values', 119, 38), 3509: ('widget/disabled|nothing', 121, 34), 3568: (' python:view.protected_field(widget.field', 122, 34), 3731: ('python:disabled or protected', 126, 34), 3862: ('disabled', 129, 44), 3991: ("python:widget.__name__.split('.')[0]", 132, 44), 4190: ('widget/field/__name__', 136, 39), 4290: ('python:view.field_type(widget.field)', 138, 42), 4404: ('widget/@@ploneform-render-widget', 140, 50), 4606: ('python:not(disabled or protected)', 145, 34), 4712: ('widget/field/__name__', 147, 35), 4853: ('widget/field/__name__', 152, 39), 4953: ('python:view.field_type(widget.field)', 154, 42), 5212: ('python:view.edit_url(widget.field)', 160, 32), 5307: ('edit_url', 162, 36), 5383: ('edit_url', 164, 28), 5771: ('python:view.delete_url(widget.field)', 172, 34), 5868: ('delete_url', 174, 36), 5946: ('delete_url', 176, 28), 6192: ('widget/@@ploneform-render-widget', 183, 52), 722: ('context/@@ploneform-macros/form', 24, 31), 722: ('context/@@ploneform-macros/form', 24, 31)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from collections import deque as _deque
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140097245719872 = {'style': 'width: 80%', }
_static_140097247254016 = {'class': 'schemaeditor-delete-field btn btn-sm btn-danger ms-1', 'title': 'Delete field', 'data-confirm_msg': 'Are you sure you want to delete this field?', 'href': 'delete_url', }
_static_140097247263376 = {'class': 'fieldSettings pat-plone-modal btn btn-sm btn-secondary', 'href': 'edit_url', }
_static_140097247255792 = {'class': 'fieldControls', }
_static_140097247257328 = {'class': 'fieldLabel', }
_static_140097247258864 = {'class': 'fieldPreview orderable', 'data-field_id': 'widget/field/__name__', }
_static_140097247262512 = {'class': 'disabled-field-overlay', }
_static_140097245760816 = {'class': 'fieldLabel', }
_static_140097245763024 = {'class': 'fieldPreview fieldFromBehavior', }
_static_140097245767344 = {'class': 'field error', }
_static_140097338108672 = {'class': 'btn btn-sm btn-danger', 'id': 'delete-fieldset-${fieldset_name}', 'href': '${context/absolute_url}/@@delete-fieldset?name=${python:group.__name__}&amp;_authenticator=${context/@@authenticator/token}', }
_static_140097247977120 = {'id': 'string:fieldset-${fieldset_name}', 'class': 'string:kssattr-fieldset-${fieldset_name}', 'data-can-add-fields': "python:(repeat['group'].start or can_delete) and 'true' or 'false'", }
_static_140097247978512 = {'type': 'text/css', }
_static_140097247975536 = 'form'
_static_140097412968080 = {}
_static_140097247980288 = {'class': 'pat-plone-modal btn btn-secondary float-end', 'id': 'add-fieldset', 'href': '${context/absolute_url}/@@add-fieldset', }
_static_140097413192176 = __C2ZContextWrapper
_static_140097413192464 = __compile_zt_expr
_static_140097247973616 = {'class': 'pat-plone-modal btn btn-secondary float-end ms-3', 'id': 'add-field', 'href': '${context/absolute_url}/@@add-field', }
_static_140097339902752 = {'class': 'pat-schemaeditor', }

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

            # <Static value=<ast.Dict object at 0x7f6af42dcb20> name=None at 7f6af42ddd20> -> __attrs_140097247970064
            __attrs_140097247970064 = _static_140097339902752
            __previous_i18n_domain_140097247973280 = __i18n_domain
            __i18n_domain = 'plone'

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="pat-schemaeditor" >\n  ')

            # <Static value=<ast.Dict object at 0x7f6aeeb310f0> name=None at 7f6aeeb30a90> -> __attrs_140097247971024
            __attrs_140097247971024 = _static_140097247973616

            # <a ... (0:0)
            # --------------------------------------------------------
            __append('<a class="pat-plone-modal btn btn-secondary float-end ms-3" id="add-field"')

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097247978992
            __default_140097247978992 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution '${context/absolute_url}/@@add-field' (9:11)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f6aeeb32530> -> __attr_href
            __token = 312
            __token = 314
            try:
                __zt_tmp = __attrs_140097247971024
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_140097413192464('path', 'context/absolute_url', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_href = ('%s%s' % ((__attr_href if (__attr_href is not None) else ''), '/@@add-field', ))
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
            __stream_140097247974528 = []
            __append_140097247974528 = __stream_140097247974528.append
            __append_140097247974528('\n     Add new field&hellip;\n  ')
            __msgid_140097247974528 = __re_whitespace(''.join(__stream_140097247974528)).strip()
            if 'add_new_field_hellip':
                __append(translate('add_new_field_hellip', mapping=None, default=__msgid_140097247974528, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</a>\n\n  ')

            # <Static value=<ast.Dict object at 0x7f6aeeb32b00> name=None at 7f6aeeb30be0> -> __attrs_140097247980720
            __attrs_140097247980720 = _static_140097247980288

            # <Value 'context/enableFieldsets' (18:20)> -> __condition
            __token = 582
            try:
                __zt_tmp = __attrs_140097247980720
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140097413192464('path', 'context/enableFieldsets', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            if __condition:

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a class="pat-plone-modal btn btn-secondary float-end" id="add-fieldset"')

                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097247972080
                __default_140097247972080 = _DEFAULT_MARKER

                # <Interpolation value=<Substitution '${context/absolute_url}/@@add-fieldset' (17:11)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f6aeeb30220> -> __attr_href
                __token = 522
                __token = 524
                try:
                    __zt_tmp = __attrs_140097247980720
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_140097413192464('path', 'context/absolute_url', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                __attr_href = ('%s%s' % ((__attr_href if (__attr_href is not None) else ''), '/@@add-fieldset', ))
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
                __stream_140097247977312 = []
                __append_140097247977312 = __stream_140097247977312.append
                __append_140097247977312('\n     Add new fieldset&hellip;\n  ')
                __msgid_140097247977312 = __re_whitespace(''.join(__stream_140097247977312)).strip()
                if 'add_fieldset_hellip':
                    __append(translate('add_fieldset_hellip', mapping=None, default=__msgid_140097247977312, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</a>')
            __append('\n\n  ')

            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097247969536
            __attrs_140097247969536 = _static_140097412968080
            __backup_macroname_140097248095424 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f6aeeb31870> name=None at 7f6aeeb318a0> -> __value
            __value = _static_140097247975536
            econtext['macroname'] = __value

            def __fill_formtop(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097247974192
                __attrs_140097247974192 = _static_140097412968080
                __append('\n      ')

                # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097247978080
                __attrs_140097247978080 = _static_140097412968080

                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097247982928
                __default_140097247982928 = _DEFAULT_MARKER

                # <Value 'context/@@authenticator/authenticator' (26:36)> -> __cache_140097247981632
                __token = 839
                try:
                    __zt_tmp = __attrs_140097247978080
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140097247981632 = _static_140097413192464('path', 'context/@@authenticator/authenticator', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                # <BinOp left=<Value 'context/@@authenticator/authenticator' (26:36)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeeb33d60> -> __condition
                __expression = __cache_140097247981632

                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input />')
                else:
                    __content = __cache_140097247981632
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n      ')

                # <Static value=<ast.Dict object at 0x7f6aeeb32410> name=None at 7f6aeeb330a0> -> __attrs_140097247982160
                __attrs_140097247982160 = _static_140097247978512

                # <style ... (0:0)
                # --------------------------------------------------------
                __append('<style type="text/css">\n  .fieldPreview {\n    background: #eee;\n    padding: 1em 1em 1px 1em;\n    margin: 0.5em 0;\n    -moz-border-radius: 0.5em;\n    position: relative;\n    border: solid 2px #ccc;\n  }\n  .field {\n    clear: left;\n  }\n\n  .fieldFromBehavior {\n    border: dashed 2px #ccc;\n  }\n\n  .fieldFromBehavior .disabled-field-overlay {\n    position: absolute;\n    top: 0;\n    left: 0;\n    height: 100%;\n    width: 100%;\n    z-index: 2;\n    background: #fff;\n    opacity: 0.6;\n  }\n\n  .fieldLabel {\n    float: left;\n    background: #ddd;\n    border-right: solid 1px #fff;\n    border-bottom: solid 1px #fff;\n    -moz-border-radius-bottomright: 0.5em;\n    margin: -1em -1em 0;\n    padding: 0 0.5em;\n    position: relative;\n    z-index: 3;\n  }\n\n  .fieldFromBehavior .fieldLabel {\n    outline-width-top: 0;\n    outline-left: none;\n  }\n\n  .fieldControls {\n    position: absolute;\n    top: 0;\n    right: 1em;\n  }\n      </style>\n    ')
            _slots = econtext['__slot_formtop'] = _deque((__fill_formtop, ))

            def __fill_fields(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097247985472
                __attrs_140097247985472 = _static_140097412968080
                __append('\n\n      ')

                # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097247983312
                __attrs_140097247983312 = _static_140097412968080
                __backup_group_140097247981776 = get('group', __marker)

                # <Value 'python:[view] + list(view.groups)' (82:35)> -> __iterator
                __token = 1918
                try:
                    __zt_tmp = __attrs_140097247983312
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140097413192464('python', '[view] + list(view.groups)', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                (__iterator, ____index_140097247983552, ) = getname('repeat')('group', __iterator)
                econtext['group'] = None
                for __item in __iterator:
                    econtext['group'] = __item
                    __append('\n        ')

                    # <Static value=<ast.Dict object at 0x7f6aeeb31ea0> name=None at 7f6aeeb334c0> -> __attrs_140097338112560
                    __attrs_140097338112560 = _static_140097247977120
                    __backup_fieldset_name_140097247978224 = get('fieldset_name', __marker)

                    # <Value 'repeat/group/index' (84:34)> -> __value
                    __token = 2019
                    try:
                        __zt_tmp = __attrs_140097338112560
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140097413192464('path', 'repeat/group/index', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    econtext['fieldset_name'] = __value
                    __backup_can_delete_140097247984464 = get('can_delete', __marker)

                    # <Value 'python:view.can_delete_fieldset(group)' (85:30)> -> __value
                    __token = 2069
                    try:
                        __zt_tmp = __attrs_140097338112560
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140097413192464('python', 'view.can_delete_fieldset(group)', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    econtext['can_delete'] = __value

                    # <fieldset ... (0:0)
                    # --------------------------------------------------------
                    __append('<fieldset')

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097247981152
                    __default_140097247981152 = _DEFAULT_MARKER

                    # <Substitution 'string:fieldset-${fieldset_name}' (88:23)> -> __attr_id
                    __token = 2188
                    try:
                        __zt_tmp = __attrs_140097338112560
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_id = _static_140097413192464('string', 'fieldset-${fieldset_name}', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_id is not None):
                        __append((' id="%s"' % __attr_id))

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338108720
                    __default_140097338108720 = _DEFAULT_MARKER

                    # <Substitution 'string:kssattr-fieldset-${fieldset_name}' (89:25)> -> __attr_class
                    __token = 2247
                    try:
                        __zt_tmp = __attrs_140097338112560
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_140097413192464('string', 'kssattr-fieldset-${fieldset_name}', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((' class="%s"' % __attr_class))

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338103104
                    __default_140097338103104 = _DEFAULT_MARKER

                    # <Substitution "python:(repeat['group'].start or can_delete) and 'true' or 'false'" (90:38)> -> __attr_data_can_add_fields
                    __token = 2328
                    try:
                        __zt_tmp = __attrs_140097338112560
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_data_can_add_fields = _static_140097413192464('python', "(repeat['group'].start or can_delete) and 'true' or 'false'", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    __attr_data_can_add_fields = __quote(__attr_data_can_add_fields, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_data_can_add_fields is not None):
                        __append((' data-can-add-fields="%s"' % __attr_data_can_add_fields))
                    __append(' >\n\n          ')

                    # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097338113472
                    __attrs_140097338113472 = _static_140097412968080
                    __backup_group_name_140097338099072 = get('group_name', __marker)

                    # <Value 'python:group.label or view.default_fieldset_label' (95:31)> -> __value
                    __token = 2491
                    try:
                        __zt_tmp = __attrs_140097338113472
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140097413192464('python', 'group.label or view.default_fieldset_label', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    econtext['group_name'] = __value

                    # <legend ... (0:0)
                    # --------------------------------------------------------
                    __append('<legend >')

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338100368
                    __default_140097338100368 = _DEFAULT_MARKER

                    # <Value 'group_name' (97:31)> -> __cache_140097338103296
                    __token = 2593
                    try:
                        __zt_tmp = __attrs_140097338113472
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140097338103296 = _static_140097413192464('path', 'group_name', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                    # <BinOp left=<Value 'group_name' (97:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6af4127cd0> -> __condition
                    __expression = __cache_140097338103296

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('Fieldset name')
                    else:
                        __content = __cache_140097338103296
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</legend>')
                    if (__backup_group_name_140097338099072 is __marker):
                        del econtext['group_name']
                    else:
                        econtext['group_name'] = __backup_group_name_140097338099072
                    __append('\n\n          ')

                    # <Static value=<ast.Dict object at 0x7f6af4126b00> name=None at 7f6af4125570> -> __attrs_140097338107136
                    __attrs_140097338107136 = _static_140097338108672

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a class="btn btn-sm btn-danger"')

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338111696
                    __default_140097338111696 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution 'delete-fieldset-${fieldset_name}' (101:17)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f6af41270d0> -> __attr_id
                    __token = 2700
                    __token = 2718
                    try:
                        __zt_tmp = __attrs_140097338107136
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_id = _static_140097413192464('path', 'fieldset_name', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                    __attr_id = ('%s%s' % ('delete-fieldset-', (__attr_id if (__attr_id is not None) else ''), ))
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

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338106608
                    __default_140097338106608 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution '${context/absolute_url}/@@delete-fieldset?name=${python:group.__name__}&amp;_authenticator=${context/@@authenticator/token}' (102:19)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f6af41274c0> -> __attr_href
                    __token = 2753
                    __token = 2755
                    try:
                        __zt_tmp = __attrs_140097338107136
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140097413192464('path', 'context/absolute_url', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                    __token = 2802
                    try:
                        __zt_tmp = __attrs_140097338107136
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href_2800 = _static_140097413192464('python', 'group.__name__', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    __attr_href_2800 = __quote(__attr_href_2800, '"', '&quot;', None, _DEFAULT_MARKER)
                    __token = 2846
                    try:
                        __zt_tmp = __attrs_140097338107136
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href_2844 = _static_140097413192464('path', 'context/@@authenticator/token', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    __attr_href_2844 = __quote(__attr_href_2844, '"', '&quot;', None, _DEFAULT_MARKER)
                    __attr_href = ('%s%s%s%s%s' % ((__attr_href if (__attr_href is not None) else ''), '/@@delete-fieldset?name=', (__attr_href_2800 if (__attr_href_2800 is not None) else ''), '&amp;_authenticator=', (__attr_href_2844 if (__attr_href_2844 is not None) else ''), ))
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
                    __stream_140097338099216 = []
                    __append_140097338099216 = __stream_140097338099216.append
                    __append_140097338099216('Delete fieldset\n          ')
                    __msgid_140097338099216 = __re_whitespace(''.join(__stream_140097338099216)).strip()
                    if 'delete_fieldset_hellip':
                        __append(translate('delete_fieldset_hellip', mapping=None, default=__msgid_140097338099216, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</a>\n\n          ')

                    # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097245759328
                    __attrs_140097245759328 = _static_140097412968080
                    __backup_errors_140097338103056 = get('errors', __marker)

                    # <Value 'group/widgets/errors' (108:30)> -> __value
                    __token = 3038
                    try:
                        __zt_tmp = __attrs_140097245759328
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140097413192464('path', 'group/widgets/errors', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    econtext['errors'] = __value

                    # <Value 'errors' (110:36)> -> __condition
                    __token = 3119
                    try:
                        __zt_tmp = __attrs_140097245759328
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140097413192464('path', 'errors', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    if __condition:
                        __backup_error_140097338100512 = get('error', __marker)

                        # <Value 'errors' (111:39)> -> __iterator
                        __token = 3166
                        try:
                            __zt_tmp = __attrs_140097245759328
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __iterator = _static_140097413192464('path', 'errors', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        (__iterator, ____index_140097245770752, ) = getname('repeat')('error', __iterator)
                        econtext['error'] = None
                        for __item in __iterator:
                            econtext['error'] = __item
                            __append('\n            ')

                            # <Static value=<ast.Dict object at 0x7f6aee9166b0> name=None at 7f6aee916c80> -> __attrs_140097245763888
                            __attrs_140097245763888 = _static_140097245767344

                            # <Value 'not:nocall:error/widget' (114:32)> -> __condition
                            __token = 3255
                            try:
                                __zt_tmp = __attrs_140097245763888
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140097413192464('not', 'nocall:error/widget', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                            if __condition:

                                # <div ... (0:0)
                                # --------------------------------------------------------
                                __append('<div class="field error" >')

                                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097245760672
                                __default_140097245760672 = _DEFAULT_MARKER

                                # <Value 'error/render' (115:40)> -> __cache_140097245762832
                                __token = 3320
                                try:
                                    __zt_tmp = __attrs_140097245763888
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __cache_140097245762832 = _static_140097413192464('path', 'error/render', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                                # <BinOp left=<Value 'error/render' (115:40)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aee916a10> -> __condition
                                __expression = __cache_140097245762832

                                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                                __value = _DEFAULT_MARKER
                                __condition = (__expression is __value)
                                if __condition:
                                    pass
                                else:
                                    __content = __cache_140097245762832
                                    __content = __convert(__content)
                                    if (__content is not None):
                                        __append(__content)
                                __append('</div>')
                            __append('\n          ')
                            ____index_140097245770752 -= 1
                            if (____index_140097245770752 > 0):
                                __append('')
                        if (__backup_error_140097338100512 is __marker):
                            del econtext['error']
                        else:
                            econtext['error'] = __backup_error_140097338100512
                    if (__backup_errors_140097338103056 is __marker):
                        del econtext['errors']
                    else:
                        econtext['errors'] = __backup_errors_140097338103056
                    __append('\n\n          ')

                    # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097245770224
                    __attrs_140097245770224 = _static_140097412968080
                    __backup_widget_140097338107952 = get('widget', __marker)

                    # <Value 'group/widgets/values' (119:38)> -> __iterator
                    __token = 3416
                    try:
                        __zt_tmp = __attrs_140097245770224
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_140097413192464('path', 'group/widgets/values', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    (__iterator, ____index_140097245758752, ) = getname('repeat')('widget', __iterator)
                    econtext['widget'] = None
                    for __item in __iterator:
                        econtext['widget'] = __item
                        __append('\n            ')

                        # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097245760336
                        __attrs_140097245760336 = _static_140097412968080
                        __backup_disabled_140097245765184 = get('disabled', __marker)

                        # <Value 'widget/disabled|nothing' (121:34)> -> __value
                        __token = 3509
                        try:
                            __zt_tmp = __attrs_140097245760336
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140097413192464('path', 'widget/disabled|nothing', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        econtext['disabled'] = __value
                        __backup_protected_140097245772864 = get('protected', __marker)

                        # <Value 'python:view.protected_field(widget.field)' (122:34)> -> __value
                        __token = 3568
                        try:
                            __zt_tmp = __attrs_140097245760336
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140097413192464('python', 'view.protected_field(widget.field)', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        econtext['protected'] = __value
                        __append('\n\n              ')

                        # <Static value=<ast.Dict object at 0x7f6aee9155d0> name=None at 7f6aee9154b0> -> __attrs_140097245764560
                        __attrs_140097245764560 = _static_140097245763024

                        # <Value 'python:disabled or protected' (126:34)> -> __condition
                        __token = 3731
                        try:
                            __zt_tmp = __attrs_140097245764560
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140097413192464('python', 'disabled or protected', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        if __condition:

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append('<div class="fieldPreview fieldFromBehavior" >\n                ')

                            # <Static value=<ast.Dict object at 0x7f6aee914d30> name=None at 7f6aee916650> -> __attrs_140097245771568
                            __attrs_140097245771568 = _static_140097245760816

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append('<div class="fieldLabel">\n                  ')

                            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097245762208
                            __attrs_140097245762208 = _static_140097412968080

                            # <Value 'disabled' (129:44)> -> __condition
                            __token = 3862
                            try:
                                __zt_tmp = __attrs_140097245762208
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140097413192464('path', 'disabled', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                            if __condition:
                                __stream_140097342298752_behavior_name = ''
                                __stream_140097245762400 = []
                                __append_140097245762400 = __stream_140097245762400.append
                                __append_140097245762400('From the\n                    ')
                                __stream_140097342298752_behavior_name = []
                                __append_140097342298752_behavior_name = __stream_140097342298752_behavior_name.append

                                # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097245773776
                                __attrs_140097245773776 = _static_140097412968080

                                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097245770368
                                __default_140097245770368 = _DEFAULT_MARKER

                                # <Value "python:widget.__name__.split('.')[0]" (132:44)> -> __cache_140097245757792
                                __token = 3991
                                try:
                                    __zt_tmp = __attrs_140097245773776
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __cache_140097245757792 = _static_140097413192464('python', "widget.__name__.split('.')[0]", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                                # <BinOp left=<Value "python:widget.__name__.split('.')[0]" (132:44)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aee9158d0> -> __condition
                                __expression = __cache_140097245757792

                                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                                __value = _DEFAULT_MARKER
                                __condition = (__expression is __value)
                                if __condition:
                                    pass
                                else:
                                    __content = __cache_140097245757792
                                    __content = __quote(__content, None, '\xad', None, None)
                                    if (__content is not None):
                                        __append_140097342298752_behavior_name(__content)
                                __append_140097245762400('${behavior_name}')
                                __stream_140097342298752_behavior_name = ''.join(__stream_140097342298752_behavior_name)
                                __append_140097245762400('\n                    behavior:')
                                __msgid_140097245762400 = __re_whitespace(''.join(__stream_140097245762400)).strip()
                                if __msgid_140097245762400:
                                    __append(translate(__msgid_140097245762400, mapping={'behavior_name': __stream_140097342298752_behavior_name, }, default=__msgid_140097245762400, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                            __append('\n                  ')

                            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097247264384
                            __attrs_140097247264384 = _static_140097412968080

                            # <strong ... (0:0)
                            # --------------------------------------------------------
                            __append('<strong>')

                            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097245762544
                            __default_140097245762544 = _DEFAULT_MARKER

                            # <Value 'widget/field/__name__' (136:39)> -> __cache_140097245758944
                            __token = 4190
                            try:
                                __zt_tmp = __attrs_140097247264384
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140097245758944 = _static_140097413192464('path', 'widget/field/__name__', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                            # <BinOp left=<Value 'widget/field/__name__' (136:39)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aee914190> -> __condition
                            __expression = __cache_140097245758944

                            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                pass
                            else:
                                __content = __cache_140097245758944
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append(__content)
                            __append('</strong>\n                 &ndash;\n                  ')

                            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097247253152
                            __attrs_140097247253152 = _static_140097412968080

                            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097247252144
                            __default_140097247252144 = _DEFAULT_MARKER

                            # <Value 'python:view.field_type(widget.field)' (138:42)> -> __cache_140097247251280
                            __token = 4290
                            try:
                                __zt_tmp = __attrs_140097247253152
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140097247251280 = _static_140097413192464('python', 'view.field_type(widget.field)', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                            # <BinOp left=<Value 'python:view.field_type(widget.field)' (138:42)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeea801c0> -> __condition
                            __expression = __cache_140097247251280

                            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                pass
                            else:
                                __content = __cache_140097247251280
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append(__content)
                            __append('\n                </div>\n                ')

                            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097247260112
                            __attrs_140097247260112 = _static_140097412968080

                            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097247250272
                            __default_140097247250272 = _DEFAULT_MARKER

                            # <Value 'widget/@@ploneform-render-widget' (140:50)> -> __cache_140097247249024
                            __token = 4404
                            try:
                                __zt_tmp = __attrs_140097247260112
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140097247249024 = _static_140097413192464('path', 'widget/@@ploneform-render-widget', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                            # <BinOp left=<Value 'widget/@@ploneform-render-widget' (140:50)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeea82020> -> __condition
                            __expression = __cache_140097247249024

                            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                pass
                            else:
                                __content = __cache_140097247249024
                                __content = __convert(__content)
                                if (__content is not None):
                                    __append(__content)
                            __append('\n                ')

                            # <Static value=<ast.Dict object at 0x7f6aeea83730> name=None at 7f6aeea80190> -> __attrs_140097247255264
                            __attrs_140097247255264 = _static_140097247262512

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append('<div class="disabled-field-overlay"></div>\n              </div>')
                        __append('\n\n              ')

                        # <Static value=<ast.Dict object at 0x7f6aeea828f0> name=None at 7f6aeea82170> -> __attrs_140097247255696
                        __attrs_140097247255696 = _static_140097247258864

                        # <Value 'python:not(disabled or protected)' (145:34)> -> __condition
                        __token = 4606
                        try:
                            __zt_tmp = __attrs_140097247255696
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140097413192464('python', 'not(disabled or protected)', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        if __condition:

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append('<div class="fieldPreview orderable"')

                            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097247261648
                            __default_140097247261648 = _DEFAULT_MARKER

                            # <Substitution 'widget/field/__name__' (147:35)> -> __attr_data_field_id
                            __token = 4712
                            try:
                                __zt_tmp = __attrs_140097247255696
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_data_field_id = _static_140097413192464('path', 'widget/field/__name__', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                            __attr_data_field_id = __quote(__attr_data_field_id, '"', '&quot;', None, _DEFAULT_MARKER)
                            if (__attr_data_field_id is not None):
                                __append((' data-field_id="%s"' % __attr_data_field_id))
                            __append(' >\n\n                ')

                            # <Static value=<ast.Dict object at 0x7f6aeea822f0> name=None at 7f6aeea82800> -> __attrs_140097247262224
                            __attrs_140097247262224 = _static_140097247257328

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append('<div class="fieldLabel">\n                  ')

                            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097247255648
                            __attrs_140097247255648 = _static_140097412968080

                            # <strong ... (0:0)
                            # --------------------------------------------------------
                            __append('<strong>')

                            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097247250704
                            __default_140097247250704 = _DEFAULT_MARKER

                            # <Value 'widget/field/__name__' (152:39)> -> __cache_140097247258480
                            __token = 4853
                            try:
                                __zt_tmp = __attrs_140097247255648
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140097247258480 = _static_140097413192464('path', 'widget/field/__name__', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                            # <BinOp left=<Value 'widget/field/__name__' (152:39)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeea83be0> -> __condition
                            __expression = __cache_140097247258480

                            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                pass
                            else:
                                __content = __cache_140097247258480
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append(__content)
                            __append('</strong>\n                 &ndash;\n                  ')

                            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097247259392
                            __attrs_140097247259392 = _static_140097412968080

                            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097247249456
                            __default_140097247249456 = _DEFAULT_MARKER

                            # <Value 'python:view.field_type(widget.field)' (154:42)> -> __cache_140097247260352
                            __token = 4953
                            try:
                                __zt_tmp = __attrs_140097247259392
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140097247260352 = _static_140097413192464('python', 'view.field_type(widget.field)', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                            # <BinOp left=<Value 'python:view.field_type(widget.field)' (154:42)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeea816c0> -> __condition
                            __expression = __cache_140097247260352

                            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                pass
                            else:
                                __content = __cache_140097247260352
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append(__content)
                            __append('\n                </div>\n\n                ')

                            # <Static value=<ast.Dict object at 0x7f6aeea81cf0> name=None at 7f6aeea80490> -> __attrs_140097247253056
                            __attrs_140097247253056 = _static_140097247255792

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append('<div class="fieldControls">\n                  ')

                            # <Static value=<ast.Dict object at 0x7f6aeea83a90> name=None at 7f6aeea807c0> -> __attrs_140097247262800
                            __attrs_140097247262800 = _static_140097247263376
                            __backup_edit_url_140097245763456 = get('edit_url', __marker)

                            # <Value 'python:view.edit_url(widget.field)' (160:32)> -> __value
                            __token = 5212
                            try:
                                __zt_tmp = __attrs_140097247262800
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_140097413192464('python', 'view.edit_url(widget.field)', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                            econtext['edit_url'] = __value

                            # <Value 'edit_url' (162:36)> -> __condition
                            __token = 5307
                            try:
                                __zt_tmp = __attrs_140097247262800
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140097413192464('path', 'edit_url', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                            if __condition:

                                # <a ... (0:0)
                                # --------------------------------------------------------
                                __append('<a class="fieldSettings pat-plone-modal btn btn-sm btn-secondary"')

                                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097247262992
                                __default_140097247262992 = _DEFAULT_MARKER

                                # <Substitution 'edit_url' (164:28)> -> __attr_href
                                __token = 5383
                                try:
                                    __zt_tmp = __attrs_140097247262800
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_href = _static_140097413192464('path', 'edit_url', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                                __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                                if (__attr_href is not None):
                                    __append((' href="%s"' % __attr_href))
                                __append(' >')
                                __stream_140097247257808 = []
                                __append_140097247257808 = __stream_140097247257808.append
                                __append_140097247257808('Settings&hellip;')
                                __msgid_140097247257808 = __re_whitespace(''.join(__stream_140097247257808)).strip()
                                if __msgid_140097247257808:
                                    __append(translate(__msgid_140097247257808, mapping=None, default=__msgid_140097247257808, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                                __append('</a>')
                            if (__backup_edit_url_140097245763456 is __marker):
                                del econtext['edit_url']
                            else:
                                econtext['edit_url'] = __backup_edit_url_140097245763456
                            __append('\n                  ')

                            # <Static value=<ast.Dict object at 0x7f6aeea81600> name=None at 7f6aeea83eb0> -> __attrs_140097245710800
                            __attrs_140097245710800 = _static_140097247254016
                            __backup_delete_url_140097245758656 = get('delete_url', __marker)

                            # <Value 'python:view.delete_url(widget.field)' (172:34)> -> __value
                            __token = 5771
                            try:
                                __zt_tmp = __attrs_140097245710800
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_140097413192464('python', 'view.delete_url(widget.field)', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                            econtext['delete_url'] = __value

                            # <Value 'delete_url' (174:36)> -> __condition
                            __token = 5868
                            try:
                                __zt_tmp = __attrs_140097245710800
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140097413192464('path', 'delete_url', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                            if __condition:

                                # <a ... (0:0)
                                # --------------------------------------------------------
                                __append('<a class="schemaeditor-delete-field btn btn-sm btn-danger ms-1"')

                                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097247250608
                                __default_140097247250608 = _DEFAULT_MARKER

                                # <Translate msgid=None node=<ast.Constant object at 0x7f6aeea82fb0> at 7f6aeea83d90> -> __attr_title
                                __attr_title = 'Delete field'
                                __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                                if (__attr_title is not None):
                                    __append((' title="%s"' % __attr_title))

                                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097247252576
                                __default_140097247252576 = _DEFAULT_MARKER

                                # <Translate msgid=None node=<ast.Constant object at 0x7f6aeea82350> at 7f6aeea81b40> -> __attr_data_confirm_msg
                                __attr_data_confirm_msg = 'Are you sure you want to delete this field?'
                                __attr_data_confirm_msg = translate(__attr_data_confirm_msg, default=__attr_data_confirm_msg, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                                if (__attr_data_confirm_msg is not None):
                                    __append((' data-confirm_msg="%s"' % __attr_data_confirm_msg))

                                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097247249648
                                __default_140097247249648 = _DEFAULT_MARKER

                                # <Substitution 'delete_url' (176:28)> -> __attr_href
                                __token = 5946
                                try:
                                    __zt_tmp = __attrs_140097245710800
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_href = _static_140097413192464('path', 'delete_url', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                                __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                                if (__attr_href is not None):
                                    __append((' href="%s"' % __attr_href))
                                __append(' >&times;</a>')
                            if (__backup_delete_url_140097245758656 is __marker):
                                del econtext['delete_url']
                            else:
                                econtext['delete_url'] = __backup_delete_url_140097245758656
                            __append('\n                </div>\n\n                ')

                            # <Static value=<ast.Dict object at 0x7f6aee90ad40> name=None at 7f6aee90b3a0> -> __attrs_140097245721984
                            __attrs_140097245721984 = _static_140097245719872

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append('<div style="width: 80%">\n                  ')

                            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097245722896
                            __attrs_140097245722896 = _static_140097412968080

                            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097245712528
                            __default_140097245712528 = _DEFAULT_MARKER

                            # <Value 'widget/@@ploneform-render-widget' (183:52)> -> __cache_140097245717760
                            __token = 6192
                            try:
                                __zt_tmp = __attrs_140097245722896
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140097245717760 = _static_140097413192464('path', 'widget/@@ploneform-render-widget', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                            # <BinOp left=<Value 'widget/@@ploneform-render-widget' (183:52)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aee909930> -> __condition
                            __expression = __cache_140097245717760

                            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                pass
                            else:
                                __content = __cache_140097245717760
                                __content = __convert(__content)
                                if (__content is not None):
                                    __append(__content)
                            __append('\n                </div>\n              </div>')
                        __append('\n            ')
                        if (__backup_protected_140097245772864 is __marker):
                            del econtext['protected']
                        else:
                            econtext['protected'] = __backup_protected_140097245772864
                        if (__backup_disabled_140097245765184 is __marker):
                            del econtext['disabled']
                        else:
                            econtext['disabled'] = __backup_disabled_140097245765184
                        __append('\n\n          ')
                        ____index_140097245758752 -= 1
                        if (____index_140097245758752 > 0):
                            __append('')
                    if (__backup_widget_140097338107952 is __marker):
                        del econtext['widget']
                    else:
                        econtext['widget'] = __backup_widget_140097338107952
                    __append('\n\n        </fieldset>')
                    if (__backup_can_delete_140097247984464 is __marker):
                        del econtext['can_delete']
                    else:
                        econtext['can_delete'] = __backup_can_delete_140097247984464
                    if (__backup_fieldset_name_140097247978224 is __marker):
                        del econtext['fieldset_name']
                    else:
                        econtext['fieldset_name'] = __backup_fieldset_name_140097247978224
                    __append('\n      ')
                    ____index_140097247983552 -= 1
                    if (____index_140097247983552 > 0):
                        __append('')
                if (__backup_group_140097247981776 is __marker):
                    del econtext['group']
                else:
                    econtext['group'] = __backup_group_140097247981776
                __append('\n    ')
            _slots = econtext['__slot_fields'] = _deque((__fill_fields, ))

            # <Value 'context/@@ploneform-macros/form' (24:31)> -> __macro
            __token = 722
            try:
                __zt_tmp = __attrs_140097247969536
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140097413192464('path', 'context/@@ploneform-macros/form', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __token = 722
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140097248095424 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140097248095424
            __append('\n</div>')
            __i18n_domain = __previous_i18n_domain_140097247973280
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }