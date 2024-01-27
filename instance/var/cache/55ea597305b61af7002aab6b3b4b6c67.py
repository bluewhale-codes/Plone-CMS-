# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/plone/app/z3cform/templates/macros.pt'

__tokens = {383: ('view/label | nothing', 15, 27), 430: ('view/label', 16, 25), 644: ('view/status', 25, 29), 688: (" python:view.widgets.errors or status == getattr(view, 'formErrorsMessage', None", 26, 31), 798: ('s view/widgets/erro', 27, 27), 846: ('ns nocall: context/@@iconresol', 28, 25), 938: ('python: status', 30, 35), 1109: ('python:not (has_error or errors)', 34, 30), 1200: ("python:icons.tag('plone-statusmessage-info', tag_alt='Info', tag_class='statusmessage-icon mb-1 me-2')", 36, 45), 1438: ('status | nothing', 40, 41), 1746: ('python:has_error or errors', 48, 30), 1831: ("python:icons.tag('plone-statusmessage-error', tag_alt='Error', tag_class='statusmessage-icon mb-1 me-2')", 50, 45), 2071: ('status | nothing', 54, 41), 2289: ("python:[e for e in errors if not getattr(e, 'widget', None)]", 60, 32), 2428: ('errors', 63, 44), 2474: ('not:nocall:error/widget', 64, 37), 2544: ('error/render', 65, 45), 3000: ('view/groups | nothing', 81, 23), 3048: (' view/form_name | nothin', 82, 25), 3100: ('s view/css_class | strin', 83, 25), 3164: ('el view/default_fieldset_label | form_n', 84, 36), 3240: ('ing view/enable_form_tabbing | python:', 85, 32), 3320: ('tion view/enable_unload_protection|python', 86, 36), 3396: ("ction python:enable_unload_protection and 'pat-formunload", 87, 28), 3487: ('ofocus view/enable_autofocus|pyth', 88, 26), 3547: ("tofocus python:enable_autofocus and 'pat-formau", 89, 18), 3622: ("lidation python:'pat-validation' if not view.ignoreRequiredOnExtrac", 90, 18), 3717: ('as_groups python:bo', 91, 17), 3766: ("rm_tabbing python:(has_groups and enable_form_tabbing) and 'enableFormTabbing pat-aut", 92, 18), 3887: ('fault_label python:has_groups and default_fieldset_label and len(v', 93, 23), 3989: ('iew_name_raw python:view.__name__ or request.getURL().s', 94, 22), 4076: ("orm_view_name python:'-'.join(['view', 'name'] + [x for x in form_view_name_raw.spli", 95, 17), 4332: ('s string:rowlike $unload_protection $autofocus $validation $form_tabbing $form_class $form_view_name_raw $form_view_na', 100, 20), 4246: ('view/action|request/getURL', 98, 23), 4532: ('thod view/method|string', 103, 18), 4297: (' view/enctyp', 99, 23), 4470: ('id view', 101, 16), 4499: ('ame form_', 102, 17), 4827: ('request/fieldset | python:None', 113, 38), 4914: ('python:has_groups and enable_form_tabbing and current_fieldset is not None', 115, 34), 5053: ('current_fieldset', 117, 27), 9329: ('view/enableCSRFProtection|nothing', 224, 36), 9408: ('context/@@authenticator/authenticator', 225, 44), 5280: ('show_default_label|nothing', 124, 47), 5346: (' has_groups|nothin', 125, 38), 5494: ('not:show_default_label', 130, 38), 5574: ('show_default_label', 133, 39), 5725: ('string:fieldsetlegend-default', 136, 29), 5631: ('default_fieldset_label', 134, 37), 6419: ('has_groups', 152, 36), 6474: ('groups', 153, 43), 6581: ('nocall:context/@@plone/normalizeString', 156, 44), 6663: (' group/labe', 157, 42), 6717: ("e python:getattr(group, '__name__', False) or getattr(group.label, 'default', False) or fieldset_lab", 158, 40), 6860: ('me python:normalizeString(fieldset_na', 159, 39), 7004: ('string:fieldset-${fieldset_name}', 162, 31), 7071: (' string:kssattr-fieldset-${fieldset_name', 163, 33), 7154: ('t fieldset_na', 164, 40), 7259: ('fieldset_label', 168, 41), 7404: ('string:fieldsetlegend-${fieldset_name}', 171, 31), 7314: ('fieldset_label', 169, 39), 7630: ('group/description|nothing', 177, 41), 7716: ('group_description', 179, 36), 7779: ('group_description', 180, 44), 8015: ('group/widgets/errors', 187, 38), 8112: ('errors', 189, 44), 8167: ('errors', 190, 47), 8280: ('not:nocall:error/widget', 193, 40), 8353: ('error/render', 194, 48), 8501: ('nocall:group', 199, 36), 8591: ('context/@@ploneform-macros/widget_rendering', 201, 44), 8591: ('context/@@ploneform-macros/widget_rendering', 201, 44), 5928: ('python:view.widgets.values()', 141, 46), 6134: ('widget/@@ploneform-render-widget', 144, 59), 9012: ('view/actions/values|nothing', 215, 34), 9099: ('view/actions/values', 217, 42), 9169: ('action/render', 218, 48)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140097338202464 = {'xmlns': 'http://www.w3.org/1999/xhtml', }
_static_140097248374560 = {'class': 'formControls', }
_static_140097248365680 = 'widget_rendering'
_static_140097248365104 = {'class': 'field error', }
_static_140097338370288 = {'id': 'string:fieldsetlegend-${fieldset_name}', }
_static_140097372459296 = {'id': 'string:fieldset-${fieldset_name}', 'class': 'string:kssattr-fieldset-${fieldset_name}', 'data-fieldset': 'fieldset_name', }
_static_140097252803584 = {'id': 'string:fieldsetlegend-default', }
_static_140097252817888 = {'id': 'fieldset-default', }
_static_140097252229024 = {'name': 'fieldset', 'type': 'hidden', 'value': 'current_fieldset', }
_static_140097338264160 = {'class': 'rowlike enableUnloadProtection', 'action': '.', 'method': 'post', 'data-pat-autotoc': 'levels: legend; section: fieldset; className: autotabs', 'enctype': 'view/enctype', 'id': 'view/id', 'name': 'form_name', }
_static_140097338270880 = {'class': 'mt-2 field error', }
_static_140097338268528 = {'class': 'content', }
_static_140097338271024 = {'alt': 'alt', }
_static_140097338268912 = {'class': 'portalMessage statusmessage statusmessage-error alert alert-danger', 'role': 'alert', }
_static_140097338261664 = {'class': 'content', }
_static_140097338263776 = {'alt': 'alt', }
_static_140097338272368 = {'class': 'portalMessage statusmessage statusmessage-info alert alert-info', 'role': 'alert', }
_static_140097413192176 = __C2ZContextWrapper
_static_140097413192464 = __compile_zt_expr
_static_140097412968080 = {}
_static_140097338204336 = {'class': 'form', }

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

    def render_form(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __slot_title = econtext['__slot_title'].pop()
        except:
            __slot_title = None

        try:
            getname = econtext.get_name
            get = econtext.get

            # <Static value=<ast.Dict object at 0x7f6af413e0b0> name=None at 7f6af413f640> -> __attrs_140097338212016
            __attrs_140097338212016 = _static_140097338204336

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="form" >\n\n      ')
            if (__slot_title is None):

                # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097338202512
                __attrs_140097338202512 = _static_140097412968080
                __append('\n        ')

                # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097339163504
                __attrs_140097339163504 = _static_140097412968080

                # <Value 'view/label | nothing' (15:27)> -> __condition
                __token = 383
                try:
                    __zt_tmp = __attrs_140097339163504
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140097413192464('path', 'view/label | nothing', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                if __condition:

                    # <h3 ... (0:0)
                    # --------------------------------------------------------
                    __append('<h3 >')

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338196224
                    __default_140097338196224 = _DEFAULT_MARKER

                    # <Value 'view/label' (16:25)> -> __cache_140097338203040
                    __token = 430
                    try:
                        __zt_tmp = __attrs_140097339163504
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140097338203040 = _static_140097413192464('path', 'view/label', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                    # <BinOp left=<Value 'view/label' (16:25)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6af413e440> -> __condition
                    __expression = __cache_140097338203040

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140097338203040
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</h3>')
                __append('\n      ')
            else:
                __slot_title(__stream, econtext.copy(), rcontext)
            __append('\n\n      ')
            __token = None
            render_titlelessform(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n    </div>')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_titlelessform(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __slot_fields = econtext['__slot_fields'].pop()
        except:
            __slot_fields = None

        try:
            __slot_formtop = econtext['__slot_formtop'].pop()
        except:
            __slot_formtop = None

        try:
            __slot_formbottom = econtext['__slot_formbottom'].pop()
        except:
            __slot_formbottom = None

        try:
            __slot_belowfields = econtext['__slot_belowfields'].pop()
        except:
            __slot_belowfields = None

        try:
            __slot_actions = econtext['__slot_actions'].pop()
        except:
            __slot_actions = None

        try:
            getname = econtext.get_name
            get = econtext.get

            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097339173776
            __attrs_140097339173776 = _static_140097412968080
            __previous_i18n_domain_140097339172144 = __i18n_domain
            __i18n_domain = 'plone'
            __append('\n\n        ')

            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097339172336
            __attrs_140097339172336 = _static_140097412968080
            __backup_status_140097245754512 = get('status', __marker)

            # <Value 'view/status' (25:29)> -> __value
            __token = 644
            try:
                __zt_tmp = __attrs_140097339172336
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('path', 'view/status', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['status'] = __value
            __backup_has_error_140097245708640 = get('has_error', __marker)

            # <Value "python:view.widgets.errors or status == getattr(view, 'formErrorsMessage', None)" (26:31)> -> __value
            __token = 688
            try:
                __zt_tmp = __attrs_140097339172336
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('python', "view.widgets.errors or status == getattr(view, 'formErrorsMessage', None)", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['has_error'] = __value
            __backup_errors_140097252541584 = get('errors', __marker)

            # <Value 'view/widgets/errors' (27:27)> -> __value
            __token = 798
            try:
                __zt_tmp = __attrs_140097339172336
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('path', 'view/widgets/errors', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['errors'] = __value
            __backup_icons_140097247588848 = get('icons', __marker)

            # <Value 'nocall: context/@@iconresolver' (28:25)> -> __value
            __token = 846
            try:
                __zt_tmp = __attrs_140097339172336
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('nocall', ' context/@@iconresolver', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['icons'] = __value

            # <Value 'python: status' (30:35)> -> __condition
            __token = 938
            try:
                __zt_tmp = __attrs_140097339172336
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140097413192464('python', ' status', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            if __condition:
                __append('\n          ')

                # <Static value=<ast.Dict object at 0x7f6af414ea70> name=None at 7f6af414f6a0> -> __attrs_140097338277216
                __attrs_140097338277216 = _static_140097338272368

                # <Value 'python:not (has_error or errors)' (34:30)> -> __condition
                __token = 1109
                try:
                    __zt_tmp = __attrs_140097338277216
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140097413192464('python', 'not (has_error or errors)', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="portalMessage statusmessage statusmessage-info alert alert-info" role="alert" >\n            ')

                    # <Static value=<ast.Dict object at 0x7f6af414c8e0> name=None at 7f6af414d660> -> __attrs_140097338267280
                    __attrs_140097338267280 = _static_140097338263776

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338277408
                    __default_140097338277408 = _DEFAULT_MARKER

                    # <Value "python:icons.tag('plone-statusmessage-info', tag_alt='Info', tag_class='statusmessage-icon mb-1 me-2')" (36:45)> -> __cache_140097338266944
                    __token = 1200
                    try:
                        __zt_tmp = __attrs_140097338267280
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140097338266944 = _static_140097413192464('python', "icons.tag('plone-statusmessage-info', tag_alt='Info', tag_class='statusmessage-icon mb-1 me-2')", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                    # <BinOp left=<Value "python:icons.tag('plone-statusmessage-info', tag_alt='Info', tag_class='statusmessage-icon mb-1 me-2')" (36:45)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6af414d000> -> __condition
                    __expression = __cache_140097338266944

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140097338266944
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('\n            ')

                    # <Static value=<ast.Dict object at 0x7f6af414c0a0> name=None at 7f6af414ef50> -> __attrs_140097338261616
                    __attrs_140097338261616 = _static_140097338261664

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338269536
                    __default_140097338269536 = _DEFAULT_MARKER

                    # <Value 'status | nothing' (40:41)> -> __cache_140097338264496
                    __token = 1438
                    try:
                        __zt_tmp = __attrs_140097338261616
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140097338264496 = _static_140097413192464('path', 'status | nothing', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                    # <BinOp left=<Value 'status | nothing' (40:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6af414f790> -> __condition
                    __expression = __cache_140097338264496

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="content" >\n                              The info status message.\n            </span>')
                    else:
                        __content = __cache_140097338264496
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('\n          </div>')
                __append('\n          ')

                # <Static value=<ast.Dict object at 0x7f6af414dcf0> name=None at 7f6af414fd90> -> __attrs_140097338276736
                __attrs_140097338276736 = _static_140097338268912

                # <Value 'python:has_error or errors' (48:30)> -> __condition
                __token = 1746
                try:
                    __zt_tmp = __attrs_140097338276736
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140097413192464('python', 'has_error or errors', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="portalMessage statusmessage statusmessage-error alert alert-danger" role="alert" >\n            ')

                    # <Static value=<ast.Dict object at 0x7f6af414e530> name=None at 7f6af414ff70> -> __attrs_140097338271264
                    __attrs_140097338271264 = _static_140097338271024

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338266224
                    __default_140097338266224 = _DEFAULT_MARKER

                    # <Value "python:icons.tag('plone-statusmessage-error', tag_alt='Error', tag_class='statusmessage-icon mb-1 me-2')" (50:45)> -> __cache_140097338268816
                    __token = 1831
                    try:
                        __zt_tmp = __attrs_140097338271264
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140097338268816 = _static_140097413192464('python', "icons.tag('plone-statusmessage-error', tag_alt='Error', tag_class='statusmessage-icon mb-1 me-2')", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                    # <BinOp left=<Value "python:icons.tag('plone-statusmessage-error', tag_alt='Error', tag_class='statusmessage-icon mb-1 me-2')" (50:45)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6af414c100> -> __condition
                    __expression = __cache_140097338268816

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140097338268816
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('\n            ')

                    # <Static value=<ast.Dict object at 0x7f6af414db70> name=None at 7f6af414ee90> -> __attrs_140097338266560
                    __attrs_140097338266560 = _static_140097338268528

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338268624
                    __default_140097338268624 = _DEFAULT_MARKER

                    # <Value 'status | nothing' (54:41)> -> __cache_140097338270928
                    __token = 2071
                    try:
                        __zt_tmp = __attrs_140097338266560
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140097338270928 = _static_140097413192464('path', 'status | nothing', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                    # <BinOp left=<Value 'status | nothing' (54:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6af414d420> -> __condition
                    __expression = __cache_140097338270928

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="content" >\n                              The error status message.\n            </span>')
                    else:
                        __content = __cache_140097338270928
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('\n            ')

                    # <Static value=<ast.Dict object at 0x7f6af414e4a0> name=None at 7f6af414d8d0> -> __attrs_140097338276256
                    __attrs_140097338276256 = _static_140097338270880

                    # <Value "python:[e for e in errors if not getattr(e, 'widget', None)]" (60:32)> -> __condition
                    __token = 2289
                    try:
                        __zt_tmp = __attrs_140097338276256
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140097413192464('python', "[e for e in errors if not getattr(e, 'widget', None)]", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    if __condition:

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append('<div class="mt-2 field error" >\n              ')

                        # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097252221152
                        __attrs_140097252221152 = _static_140097412968080

                        # <ul ... (0:0)
                        # --------------------------------------------------------
                        __append('<ul>\n                ')

                        # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097252223120
                        __attrs_140097252223120 = _static_140097412968080
                        __backup_error_140097342194112 = get('error', __marker)

                        # <Value 'errors' (63:44)> -> __iterator
                        __token = 2428
                        try:
                            __zt_tmp = __attrs_140097252223120
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __iterator = _static_140097413192464('path', 'errors', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        (__iterator, ____index_140097252219088, ) = getname('repeat')('error', __iterator)
                        econtext['error'] = None
                        for __item in __iterator:
                            econtext['error'] = __item
                            __append('\n                  ')

                            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097252215680
                            __attrs_140097252215680 = _static_140097412968080

                            # <Value 'not:nocall:error/widget' (64:37)> -> __condition
                            __token = 2474
                            try:
                                __zt_tmp = __attrs_140097252215680
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140097413192464('not', 'nocall:error/widget', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                            if __condition:

                                # <li ... (0:0)
                                # --------------------------------------------------------
                                __append('<li >')

                                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252215968
                                __default_140097252215968 = _DEFAULT_MARKER

                                # <Value 'error/render' (65:45)> -> __cache_140097252217792
                                __token = 2544
                                try:
                                    __zt_tmp = __attrs_140097252215680
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __cache_140097252217792 = _static_140097413192464('path', 'error/render', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                                # <BinOp left=<Value 'error/render' (65:45)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeef3c610> -> __condition
                                __expression = __cache_140097252217792

                                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                                __value = _DEFAULT_MARKER
                                __condition = (__expression is __value)
                                if __condition:
                                    __append('\n                                        Error\n                  ')
                                else:
                                    __content = __cache_140097252217792
                                    __content = __convert(__content)
                                    if (__content is not None):
                                        __append(__content)
                                __append('</li>')
                            __append('\n                ')
                            ____index_140097252219088 -= 1
                            if (____index_140097252219088 > 0):
                                __append('')
                        if (__backup_error_140097342194112 is __marker):
                            del econtext['error']
                        else:
                            econtext['error'] = __backup_error_140097342194112
                        __append('\n              </ul>\n            </div>')
                    __append('\n          </div>')
                __append('\n        ')
            if (__backup_icons_140097247588848 is __marker):
                del econtext['icons']
            else:
                econtext['icons'] = __backup_icons_140097247588848
            if (__backup_errors_140097252541584 is __marker):
                del econtext['errors']
            else:
                econtext['errors'] = __backup_errors_140097252541584
            if (__backup_has_error_140097245708640 is __marker):
                del econtext['has_error']
            else:
                econtext['has_error'] = __backup_has_error_140097245708640
            if (__backup_status_140097245754512 is __marker):
                del econtext['status']
            else:
                econtext['status'] = __backup_status_140097245754512
            __append('\n\n\n        ')

            # <Static value=<ast.Dict object at 0x7f6af414ca60> name=None at 7f6af414ccd0> -> __attrs_140097252227344
            __attrs_140097252227344 = _static_140097338264160
            __backup_groups_140097245720784 = get('groups', __marker)

            # <Value 'view/groups | nothing' (81:23)> -> __value
            __token = 3000
            try:
                __zt_tmp = __attrs_140097252227344
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('path', 'view/groups | nothing', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['groups'] = __value
            __backup_form_name_140097252550896 = get('form_name', __marker)

            # <Value 'view/form_name | nothing' (82:25)> -> __value
            __token = 3048
            try:
                __zt_tmp = __attrs_140097252227344
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('path', 'view/form_name | nothing', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['form_name'] = __value
            __backup_form_class_140097245718768 = get('form_class', __marker)

            # <Value 'view/css_class | string:' (83:25)> -> __value
            __token = 3100
            try:
                __zt_tmp = __attrs_140097252227344
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('path', 'view/css_class | string:', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['form_class'] = __value
            __backup_default_fieldset_label_140097338112608 = get('default_fieldset_label', __marker)

            # <Value 'view/default_fieldset_label | form_name' (84:36)> -> __value
            __token = 3164
            try:
                __zt_tmp = __attrs_140097252227344
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('path', 'view/default_fieldset_label | form_name', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['default_fieldset_label'] = __value
            __backup_enable_form_tabbing_140097338363472 = get('enable_form_tabbing', __marker)

            # <Value 'view/enable_form_tabbing | python:True' (85:32)> -> __value
            __token = 3240
            try:
                __zt_tmp = __attrs_140097252227344
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('path', 'view/enable_form_tabbing | python:True', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['enable_form_tabbing'] = __value
            __backup_enable_unload_protection_140097252058560 = get('enable_unload_protection', __marker)

            # <Value 'view/enable_unload_protection|python:True' (86:36)> -> __value
            __token = 3320
            try:
                __zt_tmp = __attrs_140097252227344
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('path', 'view/enable_unload_protection|python:True', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['enable_unload_protection'] = __value
            __backup_unload_protection_140097248364864 = get('unload_protection', __marker)

            # <Value "python:enable_unload_protection and 'pat-formunloadalert'" (87:28)> -> __value
            __token = 3396
            try:
                __zt_tmp = __attrs_140097252227344
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('python', "enable_unload_protection and 'pat-formunloadalert'", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['unload_protection'] = __value
            __backup_enable_autofocus_140097245714208 = get('enable_autofocus', __marker)

            # <Value 'view/enable_autofocus|python:True' (88:26)> -> __value
            __token = 3487
            try:
                __zt_tmp = __attrs_140097252227344
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('path', 'view/enable_autofocus|python:True', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['enable_autofocus'] = __value
            __backup_autofocus_140097247465136 = get('autofocus', __marker)

            # <Value "python:enable_autofocus and 'pat-formautofocus'" (89:18)> -> __value
            __token = 3547
            try:
                __zt_tmp = __attrs_140097252227344
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('python', "enable_autofocus and 'pat-formautofocus'", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['autofocus'] = __value
            __backup_validation_140097252584336 = get('validation', __marker)

            # <Value "python:'pat-validation' if not view.ignoreRequiredOnExtract else ''" (90:18)> -> __value
            __token = 3622
            try:
                __zt_tmp = __attrs_140097252227344
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('python', "'pat-validation' if not view.ignoreRequiredOnExtract else ''", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['validation'] = __value
            __backup_has_groups_140097340076720 = get('has_groups', __marker)

            # <Value 'python:bool(groups)' (91:17)> -> __value
            __token = 3717
            try:
                __zt_tmp = __attrs_140097252227344
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('python', 'bool(groups)', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['has_groups'] = __value
            __backup_form_tabbing_140097340066688 = get('form_tabbing', __marker)

            # <Value "python:(has_groups and enable_form_tabbing) and 'enableFormTabbing pat-autotoc' or ''" (92:18)> -> __value
            __token = 3766
            try:
                __zt_tmp = __attrs_140097252227344
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('python', "(has_groups and enable_form_tabbing) and 'enableFormTabbing pat-autotoc' or ''", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['form_tabbing'] = __value
            __backup_show_default_label_140097340068800 = get('show_default_label', __marker)

            # <Value 'python:has_groups and default_fieldset_label and len(view.widgets)' (93:23)> -> __value
            __token = 3887
            try:
                __zt_tmp = __attrs_140097252227344
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('python', 'has_groups and default_fieldset_label and len(view.widgets)', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['show_default_label'] = __value
            __backup_form_view_name_raw_140097245771184 = get('form_view_name_raw', __marker)

            # <Value "python:view.__name__ or request.getURL().split('/')[-1]" (94:22)> -> __value
            __token = 3989
            try:
                __zt_tmp = __attrs_140097252227344
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('python', "view.__name__ or request.getURL().split('/')[-1]", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['form_view_name_raw'] = __value
            __backup_form_view_name_140097245766240 = get('form_view_name', __marker)

            # <Value "python:'-'.join(['view', 'name'] + [x for x in form_view_name_raw.split('++') if x])" (95:17)> -> __value
            __token = 4076
            try:
                __zt_tmp = __attrs_140097252227344
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('python', "'-'.join(['view', 'name'] + [x for x in form_view_name_raw.split('++') if x])", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['form_view_name'] = __value

            # <form ... (0:0)
            # --------------------------------------------------------
            __append('<form')

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252222016
            __default_140097252222016 = _DEFAULT_MARKER

            # <Substitution 'string:rowlike $unload_protection $autofocus $validation $form_tabbing $form_class $form_view_name_raw $form_view_name' (100:20)> -> __attr_class
            __token = 4332
            try:
                __zt_tmp = __attrs_140097252227344
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_140097413192464('string', 'rowlike $unload_protection $autofocus $validation $form_tabbing $form_class $form_view_name_raw $form_view_name', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', 'rowlike enableUnloadProtection', _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((' class="%s"' % __attr_class))

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252226336
            __default_140097252226336 = _DEFAULT_MARKER

            # <Substitution 'view/action|request/getURL' (98:23)> -> __attr_action
            __token = 4246
            try:
                __zt_tmp = __attrs_140097252227344
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_action = _static_140097413192464('path', 'view/action|request/getURL', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_action = __quote(__attr_action, '"', '&quot;', '.', _DEFAULT_MARKER)
            if (__attr_action is not None):
                __append((' action="%s"' % __attr_action))

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252222640
            __default_140097252222640 = _DEFAULT_MARKER

            # <Substitution 'view/method|string:post' (103:18)> -> __attr_method
            __token = 4532
            try:
                __zt_tmp = __attrs_140097252227344
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_method = _static_140097413192464('path', 'view/method|string:post', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_method = __quote(__attr_method, '"', '&quot;', 'post', _DEFAULT_MARKER)
            if (__attr_method is not None):
                __append((' method="%s"' % __attr_method))
            __append(' data-pat-autotoc="levels: legend; section: fieldset; className: autotabs"')

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252221824
            __default_140097252221824 = _DEFAULT_MARKER

            # <Substitution 'view/enctype' (99:23)> -> __attr_enctype
            __token = 4297
            try:
                __zt_tmp = __attrs_140097252227344
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_enctype = _static_140097413192464('path', 'view/enctype', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_enctype = __quote(__attr_enctype, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_enctype is not None):
                __append((' enctype="%s"' % __attr_enctype))

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252225904
            __default_140097252225904 = _DEFAULT_MARKER

            # <Substitution 'view/id' (101:16)> -> __attr_id
            __token = 4470
            try:
                __zt_tmp = __attrs_140097252227344
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_140097413192464('path', 'view/id', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_id is not None):
                __append((' id="%s"' % __attr_id))

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252225232
            __default_140097252225232 = _DEFAULT_MARKER

            # <Substitution 'form_name' (102:17)> -> __attr_name
            __token = 4499
            try:
                __zt_tmp = __attrs_140097252227344
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_name = _static_140097413192464('path', 'form_name', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_name is not None):
                __append((' name="%s"' % __attr_name))
            __append(' >\n\n          ')
            if (__slot_formtop is None):

                # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097252219760
                __attrs_140097252219760 = _static_140097412968080
            else:
                __slot_formtop(__stream, econtext.copy(), rcontext)
            __append('\n\n          ')
            if (__slot_fields is None):

                # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097252227968
                __attrs_140097252227968 = _static_140097412968080
                __append('\n            ')

                # <Static value=<ast.Dict object at 0x7f6aeef3ffa0> name=None at 7f6aeef3fc10> -> __attrs_140097252809776
                __attrs_140097252809776 = _static_140097252229024
                __backup_current_fieldset_140097247577904 = get('current_fieldset', __marker)

                # <Value 'request/fieldset | python:None' (113:38)> -> __value
                __token = 4827
                try:
                    __zt_tmp = __attrs_140097252809776
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140097413192464('path', 'request/fieldset | python:None', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                econtext['current_fieldset'] = __value

                # <Value 'python:has_groups and enable_form_tabbing and current_fieldset is not None' (115:34)> -> __condition
                __token = 4914
                try:
                    __zt_tmp = __attrs_140097252809776
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140097413192464('python', 'has_groups and enable_form_tabbing and current_fieldset is not None', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                if __condition:

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input name="fieldset" type="hidden"')

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252816304
                    __default_140097252816304 = _DEFAULT_MARKER

                    # <Substitution 'current_fieldset' (117:27)> -> __attr_value
                    __token = 5053
                    try:
                        __zt_tmp = __attrs_140097252809776
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_140097413192464('path', 'current_fieldset', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append(' />')
                if (__backup_current_fieldset_140097247577904 is __marker):
                    del econtext['current_fieldset']
                else:
                    econtext['current_fieldset'] = __backup_current_fieldset_140097247577904
                __append('\n\n            <!-- Default fieldset -->\n            ')
                __token = None
                render_fields(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append('\n          ')
            else:
                __slot_fields(__stream, econtext.copy(), rcontext)
            __append('\n\n          ')
            if (__slot_belowfields is None):

                # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097252812368
                __attrs_140097252812368 = _static_140097412968080
            else:
                __slot_belowfields(__stream, econtext.copy(), rcontext)
            __append('\n\n          ')
            if (__slot_actions is None):

                # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097252816880
                __attrs_140097252816880 = _static_140097412968080
                __append('\n            ')
                __token = None
                render_actions(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append('\n          ')
            else:
                __slot_actions(__stream, econtext.copy(), rcontext)
            __append('\n\n          ')

            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097248373024
            __attrs_140097248373024 = _static_140097412968080

            # <Value 'view/enableCSRFProtection|nothing' (224:36)> -> __condition
            __token = 9329
            try:
                __zt_tmp = __attrs_140097248373024
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140097413192464('path', 'view/enableCSRFProtection|nothing', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            if __condition:

                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097248371248
                __default_140097248371248 = _DEFAULT_MARKER

                # <Value 'context/@@authenticator/authenticator' (225:44)> -> __cache_140097248369520
                __token = 9408
                try:
                    __zt_tmp = __attrs_140097248373024
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140097248369520 = _static_140097413192464('path', 'context/@@authenticator/authenticator', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                # <BinOp left=<Value 'context/@@authenticator/authenticator' (225:44)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeeb91300> -> __condition
                __expression = __cache_140097248369520

                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140097248369520
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
            __append('\n          ')
            if (__slot_formbottom is None):

                # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097248367216
                __attrs_140097248367216 = _static_140097412968080
            else:
                __slot_formbottom(__stream, econtext.copy(), rcontext)
            __append('\n\n        </form>')
            if (__backup_form_view_name_140097245766240 is __marker):
                del econtext['form_view_name']
            else:
                econtext['form_view_name'] = __backup_form_view_name_140097245766240
            if (__backup_form_view_name_raw_140097245771184 is __marker):
                del econtext['form_view_name_raw']
            else:
                econtext['form_view_name_raw'] = __backup_form_view_name_raw_140097245771184
            if (__backup_show_default_label_140097340068800 is __marker):
                del econtext['show_default_label']
            else:
                econtext['show_default_label'] = __backup_show_default_label_140097340068800
            if (__backup_form_tabbing_140097340066688 is __marker):
                del econtext['form_tabbing']
            else:
                econtext['form_tabbing'] = __backup_form_tabbing_140097340066688
            if (__backup_has_groups_140097340076720 is __marker):
                del econtext['has_groups']
            else:
                econtext['has_groups'] = __backup_has_groups_140097340076720
            if (__backup_validation_140097252584336 is __marker):
                del econtext['validation']
            else:
                econtext['validation'] = __backup_validation_140097252584336
            if (__backup_autofocus_140097247465136 is __marker):
                del econtext['autofocus']
            else:
                econtext['autofocus'] = __backup_autofocus_140097247465136
            if (__backup_enable_autofocus_140097245714208 is __marker):
                del econtext['enable_autofocus']
            else:
                econtext['enable_autofocus'] = __backup_enable_autofocus_140097245714208
            if (__backup_unload_protection_140097248364864 is __marker):
                del econtext['unload_protection']
            else:
                econtext['unload_protection'] = __backup_unload_protection_140097248364864
            if (__backup_enable_unload_protection_140097252058560 is __marker):
                del econtext['enable_unload_protection']
            else:
                econtext['enable_unload_protection'] = __backup_enable_unload_protection_140097252058560
            if (__backup_enable_form_tabbing_140097338363472 is __marker):
                del econtext['enable_form_tabbing']
            else:
                econtext['enable_form_tabbing'] = __backup_enable_form_tabbing_140097338363472
            if (__backup_default_fieldset_label_140097338112608 is __marker):
                del econtext['default_fieldset_label']
            else:
                econtext['default_fieldset_label'] = __backup_default_fieldset_label_140097338112608
            if (__backup_form_class_140097245718768 is __marker):
                del econtext['form_class']
            else:
                econtext['form_class'] = __backup_form_class_140097245718768
            if (__backup_form_name_140097252550896 is __marker):
                del econtext['form_name']
            else:
                econtext['form_name'] = __backup_form_name_140097252550896
            if (__backup_groups_140097245720784 is __marker):
                del econtext['groups']
            else:
                econtext['groups'] = __backup_groups_140097245720784
            __append('\n      ')
            __i18n_domain = __previous_i18n_domain_140097339172144
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_fields(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097252814960
            __attrs_140097252814960 = _static_140097412968080
            __backup_show_default_label_140097247587408 = get('show_default_label', __marker)

            # <Value 'show_default_label|nothing' (124:47)> -> __value
            __token = 5280
            try:
                __zt_tmp = __attrs_140097252814960
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('path', 'show_default_label|nothing', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['show_default_label'] = __value
            __backup_has_groups_140097252588368 = get('has_groups', __marker)

            # <Value 'has_groups|nothing' (125:38)> -> __value
            __token = 5346
            try:
                __zt_tmp = __attrs_140097252814960
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('path', 'has_groups|nothing', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['has_groups'] = __value
            __append('\n\n              ')

            # <Static value=<ast.Dict object at 0x7f6aeefcfbe0> name=None at 7f6aeefcd300> -> __attrs_140097252816208
            __attrs_140097252816208 = _static_140097252817888

            # <Negate value=<Value 'not:show_default_label' (130:38)> at 7f6aeefcf340> -> __cache_140097252815680

            # <Value 'not:show_default_label' (130:38)> -> __cache_140097252815680
            __token = 5494
            try:
                __zt_tmp = __attrs_140097252816208
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140097252815680 = _static_140097413192464('not', 'show_default_label', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __cache_140097252815680 = not __cache_140097252815680
            __condition = __cache_140097252815680
            if __condition:

                # <fieldset ... (0:0)
                # --------------------------------------------------------
                __append('<fieldset id="fieldset-default" >')
            __append('\n\n                ')

            # <Static value=<ast.Dict object at 0x7f6aeefcc400> name=None at 7f6aeefcfb20> -> __attrs_140097252815104
            __attrs_140097252815104 = _static_140097252803584

            # <Value 'show_default_label' (133:39)> -> __condition
            __token = 5574
            try:
                __zt_tmp = __attrs_140097252815104
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140097413192464('path', 'show_default_label', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            if __condition:

                # <legend ... (0:0)
                # --------------------------------------------------------
                __append('<legend')

                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252805312
                __default_140097252805312 = _DEFAULT_MARKER

                # <Substitution 'string:fieldsetlegend-default' (136:29)> -> __attr_id
                __token = 5725
                try:
                    __zt_tmp = __attrs_140097252815104
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_id = _static_140097413192464('string', 'fieldsetlegend-default', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_id is not None):
                    __append((' id="%s"' % __attr_id))
                __append(' >')

                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252816688
                __default_140097252816688 = _DEFAULT_MARKER

                # <Value 'default_fieldset_label' (134:37)> -> __cache_140097252806752
                __token = 5631
                try:
                    __zt_tmp = __attrs_140097252815104
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140097252806752 = _static_140097413192464('path', 'default_fieldset_label', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                # <BinOp left=<Value 'default_fieldset_label' (134:37)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeefce4a0> -> __condition
                __expression = __cache_140097252806752

                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('Form name')
                else:
                    __content = __cache_140097252806752
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</legend>')
            __append('\n\n                ')
            __token = None
            render_widget_rendering(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n              ')
            __condition = __cache_140097252815680
            if __condition:
                __append('</fieldset>')
            __append('\n\n              <!-- Secondary fieldsets -->\n              ')

            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097252808528
            __attrs_140097252808528 = _static_140097412968080

            # <Value 'has_groups' (152:36)> -> __condition
            __token = 6419
            try:
                __zt_tmp = __attrs_140097252808528
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140097413192464('path', 'has_groups', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            if __condition:
                __backup_group_140097247588464 = get('group', __marker)

                # <Value 'groups' (153:43)> -> __iterator
                __token = 6474
                try:
                    __zt_tmp = __attrs_140097252808528
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140097413192464('path', 'groups', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                (__iterator, ____index_140097252811984, ) = getname('repeat')('group', __iterator)
                econtext['group'] = None
                for __item in __iterator:
                    econtext['group'] = __item
                    __append('\n                ')

                    # <Static value=<ast.Dict object at 0x7f6af61e9120> name=None at 7f6af61e91e0> -> __attrs_140097252052128
                    __attrs_140097252052128 = _static_140097372459296
                    __backup_normalizeString_140097247584288 = get('normalizeString', __marker)

                    # <Value 'nocall:context/@@plone/normalizeString' (156:44)> -> __value
                    __token = 6581
                    try:
                        __zt_tmp = __attrs_140097252052128
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140097413192464('nocall', 'context/@@plone/normalizeString', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    econtext['normalizeString'] = __value
                    __backup_fieldset_label_140097245753840 = get('fieldset_label', __marker)

                    # <Value 'group/label' (157:42)> -> __value
                    __token = 6663
                    try:
                        __zt_tmp = __attrs_140097252052128
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140097413192464('path', 'group/label', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    econtext['fieldset_label'] = __value
                    __backup_fieldset_name_140097338097920 = get('fieldset_name', __marker)

                    # <Value "python:getattr(group, '__name__', False) or getattr(group.label, 'default', False) or fieldset_label" (158:40)> -> __value
                    __token = 6717
                    try:
                        __zt_tmp = __attrs_140097252052128
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140097413192464('python', "getattr(group, '__name__', False) or getattr(group.label, 'default', False) or fieldset_label", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    econtext['fieldset_name'] = __value
                    __backup_fieldset_name_140097252541200 = get('fieldset_name', __marker)

                    # <Value 'python:normalizeString(fieldset_name)' (159:39)> -> __value
                    __token = 6860
                    try:
                        __zt_tmp = __attrs_140097252052128
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140097413192464('python', 'normalizeString(fieldset_name)', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    econtext['fieldset_name'] = __value

                    # <fieldset ... (0:0)
                    # --------------------------------------------------------
                    __append('<fieldset')

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252804160
                    __default_140097252804160 = _DEFAULT_MARKER

                    # <Substitution 'string:fieldset-${fieldset_name}' (162:31)> -> __attr_id
                    __token = 7004
                    try:
                        __zt_tmp = __attrs_140097252052128
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_id = _static_140097413192464('string', 'fieldset-${fieldset_name}', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_id is not None):
                        __append((' id="%s"' % __attr_id))

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338166240
                    __default_140097338166240 = _DEFAULT_MARKER

                    # <Substitution 'string:kssattr-fieldset-${fieldset_name}' (163:33)> -> __attr_class
                    __token = 7071
                    try:
                        __zt_tmp = __attrs_140097252052128
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_140097413192464('string', 'kssattr-fieldset-${fieldset_name}', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((' class="%s"' % __attr_class))

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338176848
                    __default_140097338176848 = _DEFAULT_MARKER

                    # <Substitution 'fieldset_name' (164:40)> -> __attr_data_fieldset
                    __token = 7154
                    try:
                        __zt_tmp = __attrs_140097252052128
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_data_fieldset = _static_140097413192464('path', 'fieldset_name', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    __attr_data_fieldset = __quote(__attr_data_fieldset, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_data_fieldset is not None):
                        __append((' data-fieldset="%s"' % __attr_data_fieldset))
                    __append(' >\n\n                  ')

                    # <Static value=<ast.Dict object at 0x7f6af41668f0> name=None at 7f6af41642e0> -> __attrs_140097338367504
                    __attrs_140097338367504 = _static_140097338370288

                    # <Value 'fieldset_label' (168:41)> -> __condition
                    __token = 7259
                    try:
                        __zt_tmp = __attrs_140097338367504
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140097413192464('path', 'fieldset_label', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    if __condition:

                        # <legend ... (0:0)
                        # --------------------------------------------------------
                        __append('<legend')

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338366784
                        __default_140097338366784 = _DEFAULT_MARKER

                        # <Substitution 'string:fieldsetlegend-${fieldset_name}' (171:31)> -> __attr_id
                        __token = 7404
                        try:
                            __zt_tmp = __attrs_140097338367504
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_id = _static_140097413192464('string', 'fieldsetlegend-${fieldset_name}', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_id is not None):
                            __append((' id="%s"' % __attr_id))
                        __append(' >')

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097339755392
                        __default_140097339755392 = _DEFAULT_MARKER

                        # <Value 'fieldset_label' (169:39)> -> __cache_140097402068496
                        __token = 7314
                        try:
                            __zt_tmp = __attrs_140097338367504
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140097402068496 = _static_140097413192464('path', 'fieldset_label', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                        # <BinOp left=<Value 'fieldset_label' (169:39)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6af7e24e80> -> __condition
                        __expression = __cache_140097402068496

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('Form name')
                        else:
                            __content = __cache_140097402068496
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</legend>')
                    __append('\n\n                  ')

                    # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097248378592
                    __attrs_140097248378592 = _static_140097412968080
                    __backup_group_description_140097245762304 = get('group_description', __marker)

                    # <Value 'group/description|nothing' (177:41)> -> __value
                    __token = 7630
                    try:
                        __zt_tmp = __attrs_140097248378592
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140097413192464('path', 'group/description|nothing', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    econtext['group_description'] = __value

                    # <Value 'group_description' (179:36)> -> __condition
                    __token = 7716
                    try:
                        __zt_tmp = __attrs_140097248378592
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140097413192464('path', 'group_description', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    if __condition:

                        # <p ... (0:0)
                        # --------------------------------------------------------
                        __append('<p >')

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097248376864
                        __default_140097248376864 = _DEFAULT_MARKER

                        # <Value 'group_description' (180:44)> -> __cache_140097248365824
                        __token = 7779
                        try:
                            __zt_tmp = __attrs_140097248378592
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140097248365824 = _static_140097413192464('path', 'group_description', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                        # <BinOp left=<Value 'group_description' (180:44)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeeb93af0> -> __condition
                        __expression = __cache_140097248365824

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('\n                                          Description\n                  ')
                        else:
                            __content = __cache_140097248365824
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        __append('</p>')
                    if (__backup_group_description_140097245762304 is __marker):
                        del econtext['group_description']
                    else:
                        econtext['group_description'] = __backup_group_description_140097245762304
                    __append('\n\n                  ')

                    # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097248363520
                    __attrs_140097248363520 = _static_140097412968080
                    __backup_errors_140097245760048 = get('errors', __marker)

                    # <Value 'group/widgets/errors' (187:38)> -> __value
                    __token = 8015
                    try:
                        __zt_tmp = __attrs_140097248363520
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140097413192464('path', 'group/widgets/errors', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    econtext['errors'] = __value

                    # <Value 'errors' (189:44)> -> __condition
                    __token = 8112
                    try:
                        __zt_tmp = __attrs_140097248363520
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140097413192464('path', 'errors', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    if __condition:
                        __backup_error_140097252359568 = get('error', __marker)

                        # <Value 'errors' (190:47)> -> __iterator
                        __token = 8167
                        try:
                            __zt_tmp = __attrs_140097248363520
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __iterator = _static_140097413192464('path', 'errors', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        (__iterator, ____index_140097248365200, ) = getname('repeat')('error', __iterator)
                        econtext['error'] = None
                        for __item in __iterator:
                            econtext['error'] = __item
                            __append('\n                    ')

                            # <Static value=<ast.Dict object at 0x7f6aeeb90a30> name=None at 7f6aeeb906a0> -> __attrs_140097248375184
                            __attrs_140097248375184 = _static_140097248365104

                            # <Value 'not:nocall:error/widget' (193:40)> -> __condition
                            __token = 8280
                            try:
                                __zt_tmp = __attrs_140097248375184
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140097413192464('not', 'nocall:error/widget', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                            if __condition:

                                # <div ... (0:0)
                                # --------------------------------------------------------
                                __append('<div class="field error" >')

                                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097248377920
                                __default_140097248377920 = _DEFAULT_MARKER

                                # <Value 'error/render' (194:48)> -> __cache_140097248370768
                                __token = 8353
                                try:
                                    __zt_tmp = __attrs_140097248375184
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __cache_140097248370768 = _static_140097413192464('path', 'error/render', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                                # <BinOp left=<Value 'error/render' (194:48)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeeb90fd0> -> __condition
                                __expression = __cache_140097248370768

                                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                                __value = _DEFAULT_MARKER
                                __condition = (__expression is __value)
                                if __condition:
                                    pass
                                else:
                                    __content = __cache_140097248370768
                                    __content = __convert(__content)
                                    if (__content is not None):
                                        __append(__content)
                                __append('</div>')
                            __append('\n                  ')
                            ____index_140097248365200 -= 1
                            if (____index_140097248365200 > 0):
                                __append('')
                        if (__backup_error_140097252359568 is __marker):
                            del econtext['error']
                        else:
                            econtext['error'] = __backup_error_140097252359568
                    if (__backup_errors_140097245760048 is __marker):
                        del econtext['errors']
                    else:
                        econtext['errors'] = __backup_errors_140097245760048
                    __append('\n\n                  ')

                    # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097248373264
                    __attrs_140097248373264 = _static_140097412968080
                    __backup_view_140097245766144 = get('view', __marker)

                    # <Value 'nocall:group' (199:36)> -> __value
                    __token = 8501
                    try:
                        __zt_tmp = __attrs_140097248373264
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140097413192464('nocall', 'group', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    econtext['view'] = __value
                    __append('\n                    ')

                    # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097248369472
                    __attrs_140097248369472 = _static_140097412968080
                    __backup_macroname_140097245958720 = get('macroname', __marker)

                    # <Static value=<ast.Constant object at 0x7f6aeeb90c70> name=None at 7f6aeeb905e0> -> __value
                    __value = _static_140097248365680
                    econtext['macroname'] = __value

                    # <Value 'context/@@ploneform-macros/widget_rendering' (201:44)> -> __macro
                    __token = 8591
                    try:
                        __zt_tmp = __attrs_140097248369472
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __macro = _static_140097413192464('path', 'context/@@ploneform-macros/widget_rendering', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    __token = 8591
                    __m = __macro.include
                    __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                    econtext.update(rcontext)
                    if (__backup_macroname_140097245958720 is __marker):
                        del econtext['macroname']
                    else:
                        econtext['macroname'] = __backup_macroname_140097245958720
                    __append('\n                  ')
                    if (__backup_view_140097245766144 is __marker):
                        del econtext['view']
                    else:
                        econtext['view'] = __backup_view_140097245766144
                    __append('\n\n                </fieldset>')
                    if (__backup_fieldset_name_140097252541200 is __marker):
                        del econtext['fieldset_name']
                    else:
                        econtext['fieldset_name'] = __backup_fieldset_name_140097252541200
                    if (__backup_fieldset_name_140097338097920 is __marker):
                        del econtext['fieldset_name']
                    else:
                        econtext['fieldset_name'] = __backup_fieldset_name_140097338097920
                    if (__backup_fieldset_label_140097245753840 is __marker):
                        del econtext['fieldset_label']
                    else:
                        econtext['fieldset_label'] = __backup_fieldset_label_140097245753840
                    if (__backup_normalizeString_140097247584288 is __marker):
                        del econtext['normalizeString']
                    else:
                        econtext['normalizeString'] = __backup_normalizeString_140097247584288
                    __append('\n              ')
                    ____index_140097252811984 -= 1
                    if (____index_140097252811984 > 0):
                        __append('')
                if (__backup_group_140097247588464 is __marker):
                    del econtext['group']
                else:
                    econtext['group'] = __backup_group_140097247588464
            __append('\n\n            ')
            if (__backup_has_groups_140097252588368 is __marker):
                del econtext['has_groups']
            else:
                econtext['has_groups'] = __backup_has_groups_140097252588368
            if (__backup_show_default_label_140097247587408 is __marker):
                del econtext['show_default_label']
            else:
                econtext['show_default_label'] = __backup_show_default_label_140097247587408
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_widget_rendering(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __slot_field = econtext['__slot_field'].pop()
        except:
            __slot_field = None

        try:
            getname = econtext.get_name
            get = econtext.get

            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097252811264
            __attrs_140097252811264 = _static_140097412968080
            __append('\n                  ')

            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097252802624
            __attrs_140097252802624 = _static_140097412968080
            __backup_widget_140097340376736 = get('widget', __marker)

            # <Value 'python:view.widgets.values()' (141:46)> -> __iterator
            __token = 5928
            try:
                __zt_tmp = __attrs_140097252802624
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140097413192464('python', 'view.widgets.values()', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            (__iterator, ____index_140097252807472, ) = getname('repeat')('widget', __iterator)
            econtext['widget'] = None
            for __item in __iterator:
                econtext['widget'] = __item
                __append('\n                    ')
                if (__slot_field is None):

                    # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097252814576
                    __attrs_140097252814576 = _static_140097412968080
                    __append('\n                      ')
                    __token = None
                    render_field(__stream, econtext.copy(), rcontext, __i18n_domain)
                    econtext.update(rcontext)
                    __append('\n                    ')
                else:
                    __slot_field(__stream, econtext.copy(), rcontext)
                __append('\n                  ')
                ____index_140097252807472 -= 1
                if (____index_140097252807472 > 0):
                    __append('')
            if (__backup_widget_140097340376736 is __marker):
                del econtext['widget']
            else:
                econtext['widget'] = __backup_widget_140097340376736
            __append('\n                ')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_field(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097252812752
            __attrs_140097252812752 = _static_140097412968080
            __append('\n                        ')

            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097338132176
            __attrs_140097338132176 = _static_140097412968080

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252808240
            __default_140097252808240 = _DEFAULT_MARKER

            # <Value 'widget/@@ploneform-render-widget' (144:59)> -> __cache_140097252809680
            __token = 6134
            try:
                __zt_tmp = __attrs_140097338132176
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140097252809680 = _static_140097413192464('path', 'widget/@@ploneform-render-widget', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

            # <BinOp left=<Value 'widget/@@ploneform-render-widget' (144:59)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeefcfac0> -> __condition
            __expression = __cache_140097252809680

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140097252809680
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n                      ')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_actions(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097248370336
            __attrs_140097248370336 = _static_140097412968080
            __append('\n              ')

            # <Static value=<ast.Dict object at 0x7f6aeeb92f20> name=None at 7f6aeeb90ee0> -> __attrs_140097248363472
            __attrs_140097248363472 = _static_140097248374560

            # <Value 'view/actions/values|nothing' (215:34)> -> __condition
            __token = 9012
            try:
                __zt_tmp = __attrs_140097248363472
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140097413192464('path', 'view/actions/values|nothing', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="formControls" >\n                ')

                # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097248364048
                __attrs_140097248364048 = _static_140097412968080
                __backup_action_140097252588848 = get('action', __marker)

                # <Value 'view/actions/values' (217:42)> -> __iterator
                __token = 9099
                try:
                    __zt_tmp = __attrs_140097248364048
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140097413192464('path', 'view/actions/values', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                (__iterator, ____index_140097248370960, ) = getname('repeat')('action', __iterator)
                econtext['action'] = None
                for __item in __iterator:
                    econtext['action'] = __item
                    __append('\n                  ')

                    # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097248363568
                    __attrs_140097248363568 = _static_140097412968080

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097248366448
                    __default_140097248366448 = _DEFAULT_MARKER

                    # <Value 'action/render' (218:48)> -> __cache_140097248364432
                    __token = 9169
                    try:
                        __zt_tmp = __attrs_140097248363568
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140097248364432 = _static_140097413192464('path', 'action/render', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                    # <BinOp left=<Value 'action/render' (218:48)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeeb90be0> -> __condition
                    __expression = __cache_140097248364432

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input />')
                    else:
                        __content = __cache_140097248364432
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('\n                ')
                    ____index_140097248370960 -= 1
                    if (____index_140097248370960 > 0):
                        __append('')
                if (__backup_action_140097252588848 is __marker):
                    del econtext['action']
                else:
                    econtext['action'] = __backup_action_140097252588848
                __append('\n              </div>')
            __append('\n            ')
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

            # <Static value=<ast.Dict object at 0x7f6af413d960> name=None at 7f6af413df00> -> __attrs_140097338202752
            __attrs_140097338202752 = _static_140097338202464
            __previous_i18n_domain_140097338199776 = __i18n_domain
            __i18n_domain = 'plone'

            # <html ... (0:0)
            # --------------------------------------------------------
            __append('<html xmlns="http://www.w3.org/1999/xhtml" >\n\n  ')

            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097338209424
            __attrs_140097338209424 = _static_140097412968080

            # <body ... (0:0)
            # --------------------------------------------------------
            __append('<body>\n\n    ')
            __token = None
            render_form(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n  </body>\n</html>')
            __i18n_domain = __previous_i18n_domain_140097338199776
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_form': render_form, 'render_titlelessform': render_titlelessform, 'render_fields': render_fields, 'render_widget_rendering': render_widget_rendering, 'render_field': render_field, 'render_actions': render_actions, 'render': render, }