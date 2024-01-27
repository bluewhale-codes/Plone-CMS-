# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/plone/app/contentrules/browser/templates/manage-assignments.pt'

__tokens = {449: ("python:context.restrictedTraverse('@@iconresolver')", 18, 24), 711: ('string:${context/portal_url}/++resource++manage-contentrules.css', 27, 19), 863: ('not:view/globally_enabled', 32, 26), 1228: ('string:${portal_url}/@@rules-controlpanel', 42, 20), 1730: ('context/Title', 58, 28), 1883: ('view/has_rules', 65, 33), 2082: ('view/type_name', 69, 33), 2217: ('not:view/has_rules', 73, 33), 2433: ('view/type_name', 77, 33), 2689: ('string:${portal_url}/@@rules-controlpanel', 85, 24), 3208: ('view/acquired_rules', 104, 34), 3280: ('acquired_rules', 106, 32), 3836: ('acquired_rules', 120, 42), 3923: ('repeat/rule/odd', 122, 33), 4039: ("python:oddrow and 'even' or 'odd'", 125, 32), 4266: ('rule/url', 131, 38), 4359: ('rule/title', 133, 49), 4481: ('rule/trigger', 135, 49), 4648: ('rule/description', 138, 43), 4915: ('rule/enabled', 144, 49), 4986: ("python:icons.tag('check-circle-fill', tag_class='text-success', tag_alt='Active')", 145, 57), 5475: ('view/assignable_rules', 158, 36), 5549: ('assignable_rules', 160, 32), 5943: ('string:${view/view_url}', 170, 29), 6277: ('assignable_rules', 179, 46), 6436: ('rule/id', 182, 38), 6339: ('rule/title', 180, 43), 7231: ('view/assigned_rules', 207, 35), 7305: ('assigned_rules', 209, 33), 7383: ('view/view_url', 211, 27), 7772: ('view/type_name', 220, 41), 8789: ('assigned_rules', 245, 42), 8876: ('repeat/rule/odd', 247, 33), 8992: ("python:oddrow and 'even' or 'odd'", 250, 32), 9288: ('rule/id', 257, 39), 9529: ('rule/url', 264, 38), 9622: ('rule/title', 266, 49), 9744: ('rule/trigger', 268, 49), 9911: ('rule/description', 271, 43), 10214: ('not:repeat/rule/start', 278, 42), 10315: ('string:${view/view_url}?operation=move_up&amp;rule_id=${rule', 280, 34), 10546: ("python:icons.tag('caret-up-fill', tag_class='', tag_alt='')", 284, 59), 10726: ('not:repeat/rule/end', 287, 42), 10825: ('string:${view/view_url}?operation=move_down&amp;rule_id=${rule', 289, 34), 11058: ("python:icons.tag('caret-down-fill', tag_class='', tag_alt='')", 293, 59), 11289: ('rule/bubbles', 297, 49), 11360: ("python:icons.tag('check-circle-fill', tag_class='text-success', tag_alt='Active')", 298, 57), 11689: ('rule/enabled', 303, 49), 11760: ("python:icons.tag('check-circle-fill', tag_class='text-success', tag_alt='Active')", 304, 57), 12089: ('rule/global_enabled', 309, 49), 12167: ("python:icons.tag('check-circle-fill', tag_class='text-success', tag_alt='Active')", 310, 57), 247: ('context/main_template/macros/master', 6, 23), 247: ('context/main_template/macros/master', 6, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from collections import deque as _deque
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139764233955088 = {'class': 'destructive btn btn-danger', 'name': 'form.button.Delete', 'type': 'submit', 'value': 'Unassign', }
_static_139764233952688 = {'class': 'standalone btn btn-primary', 'name': 'form.button.NoBubble', 'type': 'submit', 'value': 'Disable apply to subfolders', }
_static_139764233950288 = {'class': 'standalone btn btn-primary', 'name': 'form.button.Bubble', 'type': 'submit', 'value': 'Apply to subfolders', }
_static_139764233947984 = {'class': 'standalone btn btn-primary', 'name': 'form.button.Disable', 'type': 'submit', 'value': 'Disable', }
_static_139764233879456 = {'class': 'context btn btn-primary', 'name': 'form.button.Enable', 'type': 'submit', 'value': 'Enable', }
_static_139764233848720 = {'class': 'formControls', }
_static_139764233876576 = {'alt': 'alt', }
_static_139764233873984 = {'class': 'checker listingCheckbox', }
_static_139764233873840 = {'alt': 'alt', }
_static_139764233871200 = {'class': 'checker listingCheckbox', }
_static_139764233871056 = {'alt': 'alt', }
_static_139764233869760 = {'class': 'checker listingCheckbox', }
_static_139764233867072 = {'title': 'Move down', 'href': 'string:${view/view_url}?operation=move_down&rule_id=${rule/id}', }
_static_139764233863024 = {'title': 'Move up', 'href': 'string:${view/view_url}?operation=move_up&rule_id=${rule/id}', }
_static_139764233862064 = {'class': 'text-center', }
_static_139764233859760 = {'class': 'trigger', }
_static_139764233856112 = {'href': 'rule/url', }
_static_139764233852224 = {'name': 'rule_ids:list', 'type': 'checkbox', 'value': 'rule/id', }
_static_139764233849104 = {'class': "python:oddrow and 'even' or 'odd'", }
_static_139764233845872 = {'class': 'smallcolumn', }
_static_139764233844528 = {'class': 'smallcolumn', }
_static_139764233843184 = {'class': 'smallcolumn', }
_static_139764233841840 = {'class': 'smallcolumn', }
_static_139764233838096 = {'class': 'smallcolumn', }
_static_139764233834880 = {'class': 'table listing nosort', }
_static_139764233832960 = {'class': 'mb-3', 'method': 'post', 'action': 'view/view_url', }
_static_139764233811952 = {'class': 'clearfix', }
_static_139764233813920 = {'class': 'context btn btn-primary', 'name': 'form.button.AddAssignment', 'type': 'submit', 'value': 'Add', }
_static_139764233811280 = {'class': 'col-auto', }
_static_139764233810656 = {'value': 'rule/id', }
_static_139764233808304 = {'class': 'form-select', 'id': 'select-rules', 'name': 'rule_id', 'size': '1', }
_static_139764233805520 = {'class': 'col-auto', }
_static_139764233803984 = {'class': 'row row-cols-auto g-3 align-items-center', 'method': 'post', 'action': 'string:${view/view_url}', }
_static_139764233802256 = {'class': 'col-form-label', }
_static_139764233788656 = {'class': 'mb-4', 'id': 'assignable-content-rules', }
_static_139764233799664 = {'alt': 'alt', }
_static_139764233798320 = {'class': 'checker', }
_static_139764233795952 = {'class': 'trigger', }
_static_139764233792304 = {'href': 'rule/url', }
_static_139764233787840 = {'class': "python:oddrow and 'even' or 'odd'", }
_static_139764233784672 = {'class': 'smallcolumn', }
_static_139764234910784 = {'class': 'table listing nosort', }
_static_139764234906752 = {'class': 'active', }
_static_139764234907952 = {'id': 'content-core', }
_static_139764234908672 = {'href': 'string:${portal_url}/@@rules-controlpanel', }
_static_139764235468864 = {'class': 'lead', }
_static_139764235477552 = {'class': 'documentFirstHeading', }
_static_139764235483648 = {'id': 'content', }
_static_139764235484944 = {'href': '', }
_static_139764234856688 = {'class': 'alert alert-info', }
_static_139764234849872 = {'href': '++resource++manage-contentrules.css', 'media': 'all', 'rel': 'stylesheet', 'type': 'text/css', }
_static_139764333427296 = __C2ZContextWrapper
_static_139764333427584 = __compile_zt_expr
_static_139764234743440 = 'master'
_static_139764333416256 = {}

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

            # <Static value=<ast.Dict object at 0x7f1d6b720f40> name=None at 7f1d6b721270> -> __attrs_139764234738880
            __attrs_139764234738880 = _static_139764333416256
            __previous_i18n_domain_139764234736864 = __i18n_domain
            __i18n_domain = 'plone'
            __backup_macroname_139764237808576 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f1d65906e90> name=None at 7f1d659044f0> -> __value
            __value = _static_139764234743440
            econtext['macroname'] = __value

            def __fill_body(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7f1d6b720f40> name=None at 7f1d6b721270> -> __attrs_139764234846416
                __attrs_139764234846416 = _static_139764333416256
                __backup_icons_139764239314768 = get('icons', __marker)

                # <Value "python:context.restrictedTraverse('@@iconresolver')" (18:24)> -> __value
                __token = 449
                try:
                    __zt_tmp = __attrs_139764234846416
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139764333427584('python', "context.restrictedTraverse('@@iconresolver')", econtext=econtext)(_static_139764333427296(econtext, __zt_tmp))
                econtext['icons'] = __value
                __append('\n\n      ')

                # <Static value=<ast.Dict object at 0x7f1d65920e50> name=None at 7f1d65923070> -> __attrs_139764234854672
                __attrs_139764234854672 = _static_139764234849872

                # <link ... (0:0)
                # --------------------------------------------------------
                __append('<link')

                # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __default_139764234846944
                __default_139764234846944 = _DEFAULT_MARKER

                # <Substitution 'string:${context/portal_url}/++resource++manage-contentrules.css' (27:19)> -> __attr_href
                __token = 711
                try:
                    __zt_tmp = __attrs_139764234854672
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_139764333427584('string', '${context/portal_url}/++resource++manage-contentrules.css', econtext=econtext)(_static_139764333427296(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', '++resource++manage-contentrules.css', _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((' href="%s"' % __attr_href))
                __append(' media="all" rel="stylesheet" type="text/css" />\n\n      ')

                # <Static value=<ast.Dict object at 0x7f1d659228f0> name=None at 7f1d65923e80> -> __attrs_139764235482400
                __attrs_139764235482400 = _static_139764234856688

                # <Value 'not:view/globally_enabled' (32:26)> -> __condition
                __token = 863
                try:
                    __zt_tmp = __attrs_139764235482400
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139764333427584('not', 'view/globally_enabled', econtext=econtext)(_static_139764333427296(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="alert alert-info" >\n        ')

                    # <Static value=<ast.Dict object at 0x7f1d6b720f40> name=None at 7f1d6b721270> -> __attrs_139764235479088
                    __attrs_139764235479088 = _static_139764333416256

                    # <strong ... (0:0)
                    # --------------------------------------------------------
                    __append('<strong>')
                    __stream_139764235482976 = []
                    __append_139764235482976 = __stream_139764235482976.append
                    __append_139764235482976('\n            Info\n        ')
                    __msgid_139764235482976 = __re_whitespace(''.join(__stream_139764235482976)).strip()
                    if __msgid_139764235482976:
                        __append(translate(__msgid_139764235482976, mapping=None, default=__msgid_139764235482976, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</strong>\n        ')

                    # <Static value=<ast.Dict object at 0x7f1d6b720f40> name=None at 7f1d6b721270> -> __attrs_139764235480672
                    __attrs_139764235480672 = _static_139764333416256

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>')
                    __stream_139764244451104_controlpanel_link = ''
                    __stream_139764235481920 = []
                    __append_139764235481920 = __stream_139764235481920.append
                    __append_139764235481920('\n            Content rules are disabled globally. No assigned rules will execute\n            until they are re-enabled. Use the\n          ')
                    __stream_139764244451104_controlpanel_link = []
                    __append_139764244451104_controlpanel_link = __stream_139764244451104_controlpanel_link.append

                    # <Static value=<ast.Dict object at 0x7f1d659bbf10> name=None at 7f1d659bb580> -> __attrs_139764235483312
                    __attrs_139764235483312 = _static_139764235484944

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append_139764244451104_controlpanel_link('<a')

                    # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __default_139764235483072
                    __default_139764235483072 = _DEFAULT_MARKER

                    # <Substitution 'string:${portal_url}/@@rules-controlpanel' (42:20)> -> __attr_href
                    __token = 1228
                    try:
                        __zt_tmp = __attrs_139764235483312
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_139764333427584('string', '${portal_url}/@@rules-controlpanel', econtext=econtext)(_static_139764333427296(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append_139764244451104_controlpanel_link((' href="%s"' % __attr_href))
                    __append_139764244451104_controlpanel_link(' >')
                    __stream_139764235481200 = []
                    __append_139764235481200 = __stream_139764235481200.append
                    __append_139764235481200('\n                content rules control panel\n          ')
                    __msgid_139764235481200 = __re_whitespace(''.join(__stream_139764235481200)).strip()
                    if 'contentrules_control_panel':
                        __append_139764244451104_controlpanel_link(translate('contentrules_control_panel', mapping=None, default=__msgid_139764235481200, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append_139764244451104_controlpanel_link('</a>')
                    __append_139764235481920('${controlpanel_link}')
                    __stream_139764244451104_controlpanel_link = ''.join(__stream_139764244451104_controlpanel_link)
                    __append_139764235481920('to enable them again.\n        ')
                    __msgid_139764235481920 = __re_whitespace(''.join(__stream_139764235481920)).strip()
                    if 'warning_contentrules_disabled':
                        __append(translate('warning_contentrules_disabled', mapping={'controlpanel_link': __stream_139764244451104_controlpanel_link, }, default=__msgid_139764235481920, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</span>\n      </div>')
                __append('\n\n      ')

                # <Static value=<ast.Dict object at 0x7f1d659bba00> name=None at 7f1d659bba30> -> __attrs_139764235484656
                __attrs_139764235484656 = _static_139764235483648

                # <article ... (0:0)
                # --------------------------------------------------------
                __append('<article id="content">\n        ')

                # <Static value=<ast.Dict object at 0x7f1d6b720f40> name=None at 7f1d6b721270> -> __attrs_139764235479712
                __attrs_139764235479712 = _static_139764333416256

                # <header ... (0:0)
                # --------------------------------------------------------
                __append('<header>\n          ')

                # <Static value=<ast.Dict object at 0x7f1d659ba230> name=None at 7f1d659ba380> -> __attrs_139764235469968
                __attrs_139764235469968 = _static_139764235477552

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append('<h1 class="documentFirstHeading" >')
                __stream_139764244455136_context = ''
                __stream_139764235478176 = []
                __append_139764235478176 = __stream_139764235478176.append
                __append_139764235478176('\n                Content rules for\n            ')
                __stream_139764244455136_context = []
                __append_139764244455136_context = __stream_139764244455136_context.append

                # <Static value=<ast.Dict object at 0x7f1d6b720f40> name=None at 7f1d6b721270> -> __attrs_139764235475824
                __attrs_139764235475824 = _static_139764333416256

                # <q ... (0:0)
                # --------------------------------------------------------
                __append_139764244455136_context('<q >')

                # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __default_139764235477168
                __default_139764235477168 = _DEFAULT_MARKER

                # <Value 'context/Title' (58:28)> -> __cache_139764235470832
                __token = 1730
                try:
                    __zt_tmp = __attrs_139764235475824
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_139764235470832 = _static_139764333427584('path', 'context/Title', econtext=econtext)(_static_139764333427296(econtext, __zt_tmp))

                # <BinOp left=<Value 'context/Title' (58:28)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f1d6b6b9c90> at 7f1d659b8790> -> __condition
                __expression = __cache_139764235470832

                # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append_139764244455136_context('title')
                else:
                    __content = __cache_139764235470832
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append_139764244455136_context(__content)
                __append_139764244455136_context('</q>')
                __append_139764235478176('${context}')
                __stream_139764244455136_context = ''.join(__stream_139764244455136_context)
                __append_139764235478176('\n          ')
                __msgid_139764235478176 = __re_whitespace(''.join(__stream_139764235478176)).strip()
                if 'title_contentrules_assigned':
                    __append(translate('title_contentrules_assigned', mapping={'context': __stream_139764244455136_context, }, default=__msgid_139764235478176, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</h1>\n\n          ')

                # <Static value=<ast.Dict object at 0x7f1d659b8040> name=None at 7f1d659b80a0> -> __attrs_139764235473232
                __attrs_139764235473232 = _static_139764235468864

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="lead">\n\n            ')

                # <Static value=<ast.Dict object at 0x7f1d6b720f40> name=None at 7f1d6b721270> -> __attrs_139764235472464
                __attrs_139764235472464 = _static_139764333416256

                # <Value 'view/has_rules' (65:33)> -> __condition
                __token = 1883
                try:
                    __zt_tmp = __attrs_139764235472464
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139764333427584('path', 'view/has_rules', econtext=econtext)(_static_139764333427296(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span >')
                    __stream_139764244452000_type_name = ''
                    __stream_139764235472992 = []
                    __append_139764235472992 = __stream_139764235472992.append
                    __append_139764235472992('\n                    The following content rules are active in this\n              ')
                    __stream_139764244452000_type_name = []
                    __append_139764244452000_type_name = __stream_139764244452000_type_name.append

                    # <Static value=<ast.Dict object at 0x7f1d6b720f40> name=None at 7f1d6b721270> -> __attrs_139764234896624
                    __attrs_139764234896624 = _static_139764333416256

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append_139764244452000_type_name('<span >')

                    # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __default_139764235469584
                    __default_139764235469584 = _DEFAULT_MARKER

                    # <Value 'view/type_name' (69:33)> -> __cache_139764235471600
                    __token = 2082
                    try:
                        __zt_tmp = __attrs_139764234896624
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139764235471600 = _static_139764333427584('path', 'view/type_name', econtext=econtext)(_static_139764333427296(econtext, __zt_tmp))

                    # <BinOp left=<Value 'view/type_name' (69:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f1d6b6b9c90> at 7f1d659b8ca0> -> __condition
                    __expression = __cache_139764235471600

                    # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_139764235471600
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append_139764244452000_type_name(__content)
                    __append_139764244452000_type_name('</span>')
                    __append_139764235472992('${type_name}')
                    __stream_139764244452000_type_name = ''.join(__stream_139764244452000_type_name)
                    __append_139764235472992('.\n            ')
                    __msgid_139764235472992 = __re_whitespace(''.join(__stream_139764235472992)).strip()
                    if 'description_contentrules_assigned':
                        __append(translate('description_contentrules_assigned', mapping={'type_name': __stream_139764244452000_type_name, }, default=__msgid_139764235472992, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</span>')
                __append('\n            ')

                # <Static value=<ast.Dict object at 0x7f1d6b720f40> name=None at 7f1d6b721270> -> __attrs_139764234910928
                __attrs_139764234910928 = _static_139764333416256

                # <Value 'not:view/has_rules' (73:33)> -> __condition
                __token = 2217
                try:
                    __zt_tmp = __attrs_139764234910928
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139764333427584('not', 'view/has_rules', econtext=econtext)(_static_139764333427296(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span >')
                    __stream_139764244452000_type_name = ''
                    __stream_139764234900944 = []
                    __append_139764234900944 = __stream_139764234900944.append
                    __append_139764234900944('\n                    There are currently no active content rules in this\n              ')
                    __stream_139764244452000_type_name = []
                    __append_139764244452000_type_name = __stream_139764244452000_type_name.append

                    # <Static value=<ast.Dict object at 0x7f1d6b720f40> name=None at 7f1d6b721270> -> __attrs_139764234910496
                    __attrs_139764234910496 = _static_139764333416256

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append_139764244452000_type_name('<span >')

                    # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __default_139764234903344
                    __default_139764234903344 = _DEFAULT_MARKER

                    # <Value 'view/type_name' (77:33)> -> __cache_139764234903008
                    __token = 2433
                    try:
                        __zt_tmp = __attrs_139764234910496
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139764234903008 = _static_139764333427584('path', 'view/type_name', econtext=econtext)(_static_139764333427296(econtext, __zt_tmp))

                    # <BinOp left=<Value 'view/type_name' (77:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f1d6b6b9c90> at 7f1d6592fd60> -> __condition
                    __expression = __cache_139764234903008

                    # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_139764234903008
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append_139764244452000_type_name(__content)
                    __append_139764244452000_type_name('</span>')
                    __append_139764234900944('${type_name}')
                    __stream_139764244452000_type_name = ''.join(__stream_139764244452000_type_name)
                    __append_139764234900944('.\n            ')
                    __msgid_139764234900944 = __re_whitespace(''.join(__stream_139764234900944)).strip()
                    if 'description_contentrules_assigned_norules':
                        __append(translate('description_contentrules_assigned_norules', mapping={'type_name': __stream_139764244452000_type_name, }, default=__msgid_139764234900944, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</span>')
                __append('\n\n            ')

                # <Static value=<ast.Dict object at 0x7f1d6b720f40> name=None at 7f1d6b721270> -> __attrs_139764234907328
                __attrs_139764234907328 = _static_139764333416256

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span>')
                __stream_139764244452000_controlpanel_link = ''
                __stream_139764234907664 = []
                __append_139764234907664 = __stream_139764234907664.append
                __append_139764234907664('\n                    Use the\n              ')
                __stream_139764244452000_controlpanel_link = []
                __append_139764244452000_controlpanel_link = __stream_139764244452000_controlpanel_link.append

                # <Static value=<ast.Dict object at 0x7f1d6592f400> name=None at 7f1d6592fb80> -> __attrs_139764234904784
                __attrs_139764234904784 = _static_139764234908672

                # <a ... (0:0)
                # --------------------------------------------------------
                __append_139764244452000_controlpanel_link('<a')

                # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __default_139764234905120
                __default_139764234905120 = _DEFAULT_MARKER

                # <Substitution 'string:${portal_url}/@@rules-controlpanel' (85:24)> -> __attr_href
                __token = 2689
                try:
                    __zt_tmp = __attrs_139764234904784
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_139764333427584('string', '${portal_url}/@@rules-controlpanel', econtext=econtext)(_static_139764333427296(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append_139764244452000_controlpanel_link((' href="%s"' % __attr_href))
                __append_139764244452000_controlpanel_link(' >')
                __stream_139764234905696 = []
                __append_139764234905696 = __stream_139764234905696.append
                __append_139764234905696('\n                        content rules control panel\n              ')
                __msgid_139764234905696 = __re_whitespace(''.join(__stream_139764234905696)).strip()
                if 'contentrules_control_panel':
                    __append_139764244452000_controlpanel_link(translate('contentrules_control_panel', mapping=None, default=__msgid_139764234905696, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append_139764244452000_controlpanel_link('</a>')
                __append_139764234907664('${controlpanel_link}')
                __stream_139764244452000_controlpanel_link = ''.join(__stream_139764244452000_controlpanel_link)
                __append_139764234907664('\n                    to create new rules or delete or modify existing ones.\n            ')
                __msgid_139764234907664 = __re_whitespace(''.join(__stream_139764234907664)).strip()
                if 'contentrules_controlpanel_link':
                    __append(translate('contentrules_controlpanel_link', mapping={'controlpanel_link': __stream_139764244452000_controlpanel_link, }, default=__msgid_139764234907664, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</span>\n\n\n          </div>\n\n\n        </header>\n\n        ')

                # <Static value=<ast.Dict object at 0x7f1d6592f130> name=None at 7f1d6592c3d0> -> __attrs_139764234900560
                __attrs_139764234900560 = _static_139764234907952

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div id="content-core">\n          ')

                # <Static value=<ast.Dict object at 0x7f1d6592ec80> name=None at 7f1d6592cf10> -> __attrs_139764234905216
                __attrs_139764234905216 = _static_139764234906752

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="active">\n            ')

                # <Static value=<ast.Dict object at 0x7f1d6b720f40> name=None at 7f1d6b721270> -> __attrs_139764234896144
                __attrs_139764234896144 = _static_139764333416256
                __backup_acquired_rules_139764234847664 = get('acquired_rules', __marker)

                # <Value 'view/acquired_rules' (104:34)> -> __value
                __token = 3208
                try:
                    __zt_tmp = __attrs_139764234896144
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139764333427584('path', 'view/acquired_rules', econtext=econtext)(_static_139764333427296(econtext, __zt_tmp))
                econtext['acquired_rules'] = __value

                # <Value 'acquired_rules' (106:32)> -> __condition
                __token = 3280
                try:
                    __zt_tmp = __attrs_139764234896144
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139764333427584('path', 'acquired_rules', econtext=econtext)(_static_139764333427296(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div >\n              ')

                    # <Static value=<ast.Dict object at 0x7f1d6592fc40> name=None at 7f1d6592f0a0> -> __attrs_139764234905888
                    __attrs_139764234905888 = _static_139764234910784

                    # <table ... (0:0)
                    # --------------------------------------------------------
                    __append('<table class="table listing nosort">\n                ')

                    # <Static value=<ast.Dict object at 0x7f1d6b720f40> name=None at 7f1d6b721270> -> __attrs_139764233781696
                    __attrs_139764233781696 = _static_139764333416256

                    # <thead ... (0:0)
                    # --------------------------------------------------------
                    __append('<thead>\n                  ')

                    # <Static value=<ast.Dict object at 0x7f1d6b720f40> name=None at 7f1d6b721270> -> __attrs_139764233782656
                    __attrs_139764233782656 = _static_139764333416256

                    # <tr ... (0:0)
                    # --------------------------------------------------------
                    __append('<tr>\n                    ')

                    # <Static value=<ast.Dict object at 0x7f1d6b720f40> name=None at 7f1d6b721270> -> __attrs_139764233783712
                    __attrs_139764233783712 = _static_139764333416256

                    # <th ... (0:0)
                    # --------------------------------------------------------
                    __append('<th>')
                    __stream_139764233783232 = []
                    __append_139764233783232 = __stream_139764233783232.append
                    __append_139764233783232('\n                                    Content rules from parent folders\n                    ')
                    __msgid_139764233783232 = __re_whitespace(''.join(__stream_139764233783232)).strip()
                    if 'label_contentrules_from_parent':
                        __append(translate('label_contentrules_from_parent', mapping=None, default=__msgid_139764233783232, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</th>\n                    ')

                    # <Static value=<ast.Dict object at 0x7f1d6581cd60> name=None at 7f1d6581cd90> -> __attrs_139764233785056
                    __attrs_139764233785056 = _static_139764233784672

                    # <th ... (0:0)
                    # --------------------------------------------------------
                    __append('<th class="smallcolumn" >')
                    __stream_139764233784192 = []
                    __append_139764233784192 = __stream_139764233784192.append
                    __append_139764233784192('Active')
                    __msgid_139764233784192 = __re_whitespace(''.join(__stream_139764233784192)).strip()
                    if 'label_contentrules_active':
                        __append(translate('label_contentrules_active', mapping=None, default=__msgid_139764233784192, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</th>\n                  </tr>\n                </thead>\n                ')

                    # <Static value=<ast.Dict object at 0x7f1d6b720f40> name=None at 7f1d6b721270> -> __attrs_139764233785728
                    __attrs_139764233785728 = _static_139764333416256

                    # <tbody ... (0:0)
                    # --------------------------------------------------------
                    __append('<tbody>\n                  ')

                    # <Static value=<ast.Dict object at 0x7f1d6b720f40> name=None at 7f1d6b721270> -> __attrs_139764233786592
                    __attrs_139764233786592 = _static_139764333416256
                    __backup_rule_139764234861632 = get('rule', __marker)

                    # <Value 'acquired_rules' (120:42)> -> __iterator
                    __token = 3836
                    try:
                        __zt_tmp = __attrs_139764233786592
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_139764333427584('path', 'acquired_rules', econtext=econtext)(_static_139764333427296(econtext, __zt_tmp))
                    (__iterator, ____index_139764233786832, ) = getname('repeat')('rule', __iterator)
                    econtext['rule'] = None
                    for __item in __iterator:
                        econtext['rule'] = __item
                        __append('\n                    ')

                        # <Static value=<ast.Dict object at 0x7f1d6581d9c0> name=None at 7f1d6581d7e0> -> __attrs_139764233788368
                        __attrs_139764233788368 = _static_139764233787840
                        __backup_oddrow_139764234851504 = get('oddrow', __marker)

                        # <Value 'repeat/rule/odd' (122:33)> -> __value
                        __token = 3923
                        try:
                            __zt_tmp = __attrs_139764233788368
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_139764333427584('path', 'repeat/rule/odd', econtext=econtext)(_static_139764333427296(econtext, __zt_tmp))
                        econtext['oddrow'] = __value

                        # <tr ... (0:0)
                        # --------------------------------------------------------
                        __append('<tr')

                        # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __default_139764233787408
                        __default_139764233787408 = _DEFAULT_MARKER

                        # <Substitution "python:oddrow and 'even' or 'odd'" (125:32)> -> __attr_class
                        __token = 4039
                        try:
                            __zt_tmp = __attrs_139764233788368
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_class = _static_139764333427584('python', "oddrow and 'even' or 'odd'", econtext=econtext)(_static_139764333427296(econtext, __zt_tmp))
                        __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_class is not None):
                            __append((' class="%s"' % __attr_class))
                        __append(' >\n                      ')

                        # <Static value=<ast.Dict object at 0x7f1d6b720f40> name=None at 7f1d6b721270> -> __attrs_139764233789520
                        __attrs_139764233789520 = _static_139764333416256

                        # <td ... (0:0)
                        # --------------------------------------------------------
                        __append('<td>\n                        ')

                        # <Static value=<ast.Dict object at 0x7f1d6b720f40> name=None at 7f1d6b721270> -> __attrs_139764233790480
                        __attrs_139764233790480 = _static_139764333416256

                        # <dl ... (0:0)
                        # --------------------------------------------------------
                        __append('<dl>\n                          ')

                        # <Static value=<ast.Dict object at 0x7f1d6b720f40> name=None at 7f1d6b721270> -> __attrs_139764233791440
                        __attrs_139764233791440 = _static_139764333416256

                        # <dt ... (0:0)
                        # --------------------------------------------------------
                        __append('<dt>')

                        # <Static value=<ast.Dict object at 0x7f1d6581eb30> name=None at 7f1d6581eb60> -> __attrs_139764233792832
                        __attrs_139764233792832 = _static_139764233792304

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append('<a')

                        # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __default_139764233792112
                        __default_139764233792112 = _DEFAULT_MARKER

                        # <Substitution 'rule/url' (131:38)> -> __attr_href
                        __token = 4266
                        try:
                            __zt_tmp = __attrs_139764233792832
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_139764333427584('path', 'rule/url', econtext=econtext)(_static_139764333427296(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((' href="%s"' % __attr_href))
                        __append('>\n                              ')

                        # <Static value=<ast.Dict object at 0x7f1d6b720f40> name=None at 7f1d6b721270> -> __attrs_139764233794464
                        __attrs_139764233794464 = _static_139764333416256

                        # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __default_139764233794272
                        __default_139764233794272 = _DEFAULT_MARKER

                        # <Value 'rule/title' (133:49)> -> __cache_139764233793792
                        __token = 4359
                        try:
                            __zt_tmp = __attrs_139764233794464
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_139764233793792 = _static_139764333427584('path', 'rule/title', econtext=econtext)(_static_139764333427296(econtext, __zt_tmp))

                        # <BinOp left=<Value 'rule/title' (133:49)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f1d6b6b9c90> at 7f1d6581f1c0> -> __condition
                        __expression = __cache_139764233793792

                        # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span></span>')
                        else:
                            __content = __cache_139764233793792
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('\n                              (')

                        # <Static value=<ast.Dict object at 0x7f1d6581f970> name=None at 7f1d6581f9a0> -> __attrs_139764233796336
                        __attrs_139764233796336 = _static_139764233795952

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="trigger" >')

                        # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __default_139764233795376
                        __default_139764233795376 = _DEFAULT_MARKER

                        # <Value 'rule/trigger' (135:49)> -> __cache_139764233794896
                        __token = 4481
                        try:
                            __zt_tmp = __attrs_139764233796336
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_139764233794896 = _static_139764333427584('path', 'rule/trigger', econtext=econtext)(_static_139764333427296(econtext, __zt_tmp))

                        # <BinOp left=<Value 'rule/trigger' (135:49)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f1d6b6b9c90> at 7f1d6581f610> -> __condition
                        __expression = __cache_139764233794896

                        # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('trigger')
                        else:
                            __content = __cache_139764233794896
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</span>)</a></dt>\n                          ')

                        # <Static value=<ast.Dict object at 0x7f1d6b720f40> name=None at 7f1d6b721270> -> __attrs_139764233797584
                        __attrs_139764233797584 = _static_139764333416256

                        # <dd ... (0:0)
                        # --------------------------------------------------------
                        __append('<dd>')

                        # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __default_139764233797008
                        __default_139764233797008 = _DEFAULT_MARKER

                        # <Value 'rule/description' (138:43)> -> __cache_139764233792928
                        __token = 4648
                        try:
                            __zt_tmp = __attrs_139764233797584
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_139764233792928 = _static_139764333427584('path', 'rule/description', econtext=econtext)(_static_139764333427296(econtext, __zt_tmp))

                        # <BinOp left=<Value 'rule/description' (138:43)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f1d6b6b9c90> at 7f1d6581fc70> -> __condition
                        __expression = __cache_139764233792928

                        # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('\n                                                Rule Description.\n                          ')
                        else:
                            __content = __cache_139764233792928
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</dd>\n                        </dl>\n                      </td>\n                      ')

                        # <Static value=<ast.Dict object at 0x7f1d658202b0> name=None at 7f1d658202e0> -> __attrs_139764233798704
                        __attrs_139764233798704 = _static_139764233798320

                        # <td ... (0:0)
                        # --------------------------------------------------------
                        __append('<td class="checker">\n                        ')

                        # <Static value=<ast.Dict object at 0x7f1d658207f0> name=None at 7f1d65820820> -> __attrs_139764233800816
                        __attrs_139764233800816 = _static_139764233799664

                        # <Value 'rule/enabled' (144:49)> -> __condition
                        __token = 4915
                        try:
                            __zt_tmp = __attrs_139764233800816
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_139764333427584('path', 'rule/enabled', econtext=econtext)(_static_139764333427296(econtext, __zt_tmp))
                        if __condition:

                            # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __default_139764233800624
                            __default_139764233800624 = _DEFAULT_MARKER

                            # <Value "python:icons.tag('check-circle-fill', tag_class='text-success', tag_alt='Active')" (145:57)> -> __cache_139764233800144
                            __token = 4986
                            try:
                                __zt_tmp = __attrs_139764233800816
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_139764233800144 = _static_139764333427584('python', "icons.tag('check-circle-fill', tag_class='text-success', tag_alt='Active')", econtext=econtext)(_static_139764333427296(econtext, __zt_tmp))

                            # <BinOp left=<Value "python:icons.tag('check-circle-fill', tag_class='text-success', tag_alt='Active')" (145:57)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f1d6b6b9c90> at 7f1d65820a90> -> __condition
                            __expression = __cache_139764233800144

                            # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                pass
                            else:
                                __content = __cache_139764233800144
                                __content = __convert(__content)
                                if (__content is not None):
                                    __append(__content)
                        __append('\n                      </td>\n                    </tr>')
                        if (__backup_oddrow_139764234851504 is __marker):
                            del econtext['oddrow']
                        else:
                            econtext['oddrow'] = __backup_oddrow_139764234851504
                        __append('\n                  ')
                        ____index_139764233786832 -= 1
                        if (____index_139764233786832 > 0):
                            __append('')
                    if (__backup_rule_139764234861632 is __marker):
                        del econtext['rule']
                    else:
                        econtext['rule'] = __backup_rule_139764234861632
                    __append('\n                </tbody>\n              </table>\n            </div>')
                if (__backup_acquired_rules_139764234847664 is __marker):
                    del econtext['acquired_rules']
                else:
                    econtext['acquired_rules'] = __backup_acquired_rules_139764234847664
                __append('\n\n            ')

                # <Static value=<ast.Dict object at 0x7f1d6581dcf0> name=None at 7f1d6581dde0> -> __attrs_139764233799760
                __attrs_139764233799760 = _static_139764233788656
                __backup_assignable_rules_139764234852032 = get('assignable_rules', __marker)

                # <Value 'view/assignable_rules' (158:36)> -> __value
                __token = 5475
                try:
                    __zt_tmp = __attrs_139764233799760
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139764333427584('path', 'view/assignable_rules', econtext=econtext)(_static_139764333427296(econtext, __zt_tmp))
                econtext['assignable_rules'] = __value

                # <Value 'assignable_rules' (160:32)> -> __condition
                __token = 5549
                try:
                    __zt_tmp = __attrs_139764233799760
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139764333427584('path', 'assignable_rules', econtext=econtext)(_static_139764333427296(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="mb-4" id="assignable-content-rules" >\n              ')

                    # <Static value=<ast.Dict object at 0x7f1d65821210> name=None at 7f1d65821240> -> __attrs_139764233802688
                    __attrs_139764233802688 = _static_139764233802256

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="col-form-label" >')
                    __stream_139764233801824 = []
                    __append_139764233801824 = __stream_139764233801824.append
                    __append_139764233801824('\n                        Available content rules:\n              ')
                    __msgid_139764233801824 = __re_whitespace(''.join(__stream_139764233801824)).strip()
                    if 'contentrules_available_rules':
                        __append(translate('contentrules_available_rules', mapping=None, default=__msgid_139764233801824, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</div>\n              ')

                    # <Static value=<ast.Dict object at 0x7f1d658218d0> name=None at 7f1d65821900> -> __attrs_139764233804560
                    __attrs_139764233804560 = _static_139764233803984

                    # <form ... (0:0)
                    # --------------------------------------------------------
                    __append('<form class="row row-cols-auto g-3 align-items-center" method="post"')

                    # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __default_139764233803216
                    __default_139764233803216 = _DEFAULT_MARKER

                    # <Substitution 'string:${view/view_url}' (170:29)> -> __attr_action
                    __token = 5943
                    try:
                        __zt_tmp = __attrs_139764233804560
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_action = _static_139764333427584('string', '${view/view_url}', econtext=econtext)(_static_139764333427296(econtext, __zt_tmp))
                    __attr_action = __quote(__attr_action, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_action is not None):
                        __append((' action="%s"' % __attr_action))
                    __append(' >\n                ')

                    # <Static value=<ast.Dict object at 0x7f1d65821ed0> name=None at 7f1d65821f00> -> __attrs_139764233805904
                    __attrs_139764233805904 = _static_139764233805520

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="col-auto">\n                  ')

                    # <Static value=<ast.Dict object at 0x7f1d658229b0> name=None at 7f1d658229e0> -> __attrs_139764233807056
                    __attrs_139764233807056 = _static_139764233808304

                    # <select ... (0:0)
                    # --------------------------------------------------------
                    __append('<select class="form-select" id="select-rules" name="rule_id" size="1" >\n                    ')

                    # <Static value=<ast.Dict object at 0x7f1d6b720f40> name=None at 7f1d6b721270> -> __attrs_139764233808832
                    __attrs_139764233808832 = _static_139764333416256
                    __backup_rule_139764234859664 = get('rule', __marker)

                    # <Value 'assignable_rules' (179:46)> -> __iterator
                    __token = 6277
                    try:
                        __zt_tmp = __attrs_139764233808832
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_139764333427584('path', 'assignable_rules', econtext=econtext)(_static_139764333427296(econtext, __zt_tmp))
                    (__iterator, ____index_139764233809072, ) = getname('repeat')('rule', __iterator)
                    econtext['rule'] = None
                    for __item in __iterator:
                        econtext['rule'] = __item
                        __append('\n                      ')

                        # <Static value=<ast.Dict object at 0x7f1d658232e0> name=None at 7f1d65823310> -> __attrs_139764233811184
                        __attrs_139764233811184 = _static_139764233810656

                        # <option ... (0:0)
                        # --------------------------------------------------------
                        __append('<option')

                        # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __default_139764233810320
                        __default_139764233810320 = _DEFAULT_MARKER

                        # <Substitution 'rule/id' (182:38)> -> __attr_value
                        __token = 6436
                        try:
                            __zt_tmp = __attrs_139764233811184
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_value = _static_139764333427584('path', 'rule/id', econtext=econtext)(_static_139764333427296(econtext, __zt_tmp))
                        __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_value is not None):
                            __append((' value="%s"' % __attr_value))
                        __append(' >')

                        # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __default_139764233810080
                        __default_139764233810080 = _DEFAULT_MARKER

                        # <Value 'rule/title' (180:43)> -> __cache_139764233809600
                        __token = 6339
                        try:
                            __zt_tmp = __attrs_139764233811184
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_139764233809600 = _static_139764333427584('path', 'rule/title', econtext=econtext)(_static_139764333427296(econtext, __zt_tmp))

                        # <BinOp left=<Value 'rule/title' (180:43)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f1d6b6b9c90> at 7f1d65822f80> -> __condition
                        __expression = __cache_139764233809600

                        # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('Addable rule name')
                        else:
                            __content = __cache_139764233809600
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</option>\n                    ')
                        ____index_139764233809072 -= 1
                        if (____index_139764233809072 > 0):
                            __append('')
                    if (__backup_rule_139764234859664 is __marker):
                        del econtext['rule']
                    else:
                        econtext['rule'] = __backup_rule_139764234859664
                    __append('\n                  </select>\n                </div>\n\n                ')

                    # <Static value=<ast.Dict object at 0x7f1d65823550> name=None at 7f1d65823640> -> __attrs_139764233811856
                    __attrs_139764233811856 = _static_139764233811280

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="col-auto">\n                  ')

                    # <Static value=<ast.Dict object at 0x7f1d65823fa0> name=None at 7f1d65823fd0> -> __attrs_139764233830464
                    __attrs_139764233830464 = _static_139764233813920

                    # <button ... (0:0)
                    # --------------------------------------------------------
                    __append('<button class="context btn btn-primary" name="form.button.AddAssignment" type="submit"')

                    # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __default_139764233812768
                    __default_139764233812768 = _DEFAULT_MARKER

                    # <Translate msgid='label_add' node=<ast.Constant object at 0x7f1d65823c10> at 7f1d65823bb0> -> __attr_value
                    __attr_value = 'Add'
                    __attr_value = translate('label_add', default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append(' >')
                    __stream_139764233812432 = []
                    __append_139764233812432 = __stream_139764233812432.append
                    __append_139764233812432('Add')
                    __msgid_139764233812432 = __re_whitespace(''.join(__stream_139764233812432)).strip()
                    if 'label_add':
                        __append(translate('label_add', mapping=None, default=__msgid_139764233812432, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</button>\n                </div>\n              </form>\n            </div>')
                if (__backup_assignable_rules_139764234852032 is __marker):
                    del econtext['assignable_rules']
                else:
                    econtext['assignable_rules'] = __backup_assignable_rules_139764234852032
                __append('\n\n\n            ')

                # <Static value=<ast.Dict object at 0x7f1d658237f0> name=None at 7f1d658238e0> -> __attrs_139764233831712
                __attrs_139764233831712 = _static_139764233811952

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="clearfix"></div>\n\n            ')

                # <Static value=<ast.Dict object at 0x7f1d65828a00> name=None at 7f1d65828a30> -> __attrs_139764233833488
                __attrs_139764233833488 = _static_139764233832960
                __backup_assigned_rules_139764234857696 = get('assigned_rules', __marker)

                # <Value 'view/assigned_rules' (207:35)> -> __value
                __token = 7231
                try:
                    __zt_tmp = __attrs_139764233833488
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139764333427584('path', 'view/assigned_rules', econtext=econtext)(_static_139764333427296(econtext, __zt_tmp))
                econtext['assigned_rules'] = __value

                # <Value 'assigned_rules' (209:33)> -> __condition
                __token = 7305
                try:
                    __zt_tmp = __attrs_139764233833488
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139764333427584('path', 'assigned_rules', econtext=econtext)(_static_139764333427296(econtext, __zt_tmp))
                if __condition:

                    # <form ... (0:0)
                    # --------------------------------------------------------
                    __append('<form class="mb-3" method="post"')

                    # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __default_139764233832288
                    __default_139764233832288 = _DEFAULT_MARKER

                    # <Substitution 'view/view_url' (211:27)> -> __attr_action
                    __token = 7383
                    try:
                        __zt_tmp = __attrs_139764233833488
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_action = _static_139764333427584('path', 'view/view_url', econtext=econtext)(_static_139764333427296(econtext, __zt_tmp))
                    __attr_action = __quote(__attr_action, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_action is not None):
                        __append((' action="%s"' % __attr_action))
                    __append(' >\n              ')

                    # <Static value=<ast.Dict object at 0x7f1d65829180> name=None at 7f1d65829000> -> __attrs_139764233835216
                    __attrs_139764233835216 = _static_139764233834880

                    # <table ... (0:0)
                    # --------------------------------------------------------
                    __append('<table class="table listing nosort">\n                ')

                    # <Static value=<ast.Dict object at 0x7f1d6b720f40> name=None at 7f1d6b721270> -> __attrs_139764233836176
                    __attrs_139764233836176 = _static_139764333416256

                    # <thead ... (0:0)
                    # --------------------------------------------------------
                    __append('<thead>\n                  ')

                    # <Static value=<ast.Dict object at 0x7f1d6b720f40> name=None at 7f1d6b721270> -> __attrs_139764233837136
                    __attrs_139764233837136 = _static_139764333416256

                    # <tr ... (0:0)
                    # --------------------------------------------------------
                    __append('<tr>\n                    ')

                    # <Static value=<ast.Dict object at 0x7f1d65829e10> name=None at 7f1d65829e40> -> __attrs_139764233838480
                    __attrs_139764233838480 = _static_139764233838096

                    # <th ... (0:0)
                    # --------------------------------------------------------
                    __append('<th class="smallcolumn">&nbsp;</th>\n                    ')

                    # <Static value=<ast.Dict object at 0x7f1d6b720f40> name=None at 7f1d6b721270> -> __attrs_139764233839440
                    __attrs_139764233839440 = _static_139764333416256

                    # <th ... (0:0)
                    # --------------------------------------------------------
                    __append('<th>')
                    __stream_139764244448864_content_type = ''
                    __stream_139764233838960 = []
                    __append_139764233838960 = __stream_139764233838960.append
                    __append_139764233838960('\n                                    Active content rules in this\n                      ')
                    __stream_139764244448864_content_type = []
                    __append_139764244448864_content_type = __stream_139764244448864_content_type.append

                    # <Static value=<ast.Dict object at 0x7f1d6b720f40> name=None at 7f1d6b721270> -> __attrs_139764233841072
                    __attrs_139764233841072 = _static_139764333416256

                    # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __default_139764233840880
                    __default_139764233840880 = _DEFAULT_MARKER

                    # <Value 'view/type_name' (220:41)> -> __cache_139764233840400
                    __token = 7772
                    try:
                        __zt_tmp = __attrs_139764233841072
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139764233840400 = _static_139764333427584('path', 'view/type_name', econtext=econtext)(_static_139764333427296(econtext, __zt_tmp))

                    # <BinOp left=<Value 'view/type_name' (220:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f1d6b6b9c90> at 7f1d6582a7d0> -> __condition
                    __expression = __cache_139764233840400

                    # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append_139764244448864_content_type('<span ></span>')
                    else:
                        __content = __cache_139764233840400
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append_139764244448864_content_type(__content)
                    __append_139764233838960('${content_type}')
                    __stream_139764244448864_content_type = ''.join(__stream_139764244448864_content_type)
                    __append_139764233838960('\n                    ')
                    __msgid_139764233838960 = __re_whitespace(''.join(__stream_139764233838960)).strip()
                    if 'label_contentrules_active_assignments':
                        __append(translate('label_contentrules_active_assignments', mapping={'content_type': __stream_139764244448864_content_type, }, default=__msgid_139764233838960, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</th>\n                    ')

                    # <Static value=<ast.Dict object at 0x7f1d6582acb0> name=None at 7f1d6582ace0> -> __attrs_139764233842224
                    __attrs_139764233842224 = _static_139764233841840

                    # <th ... (0:0)
                    # --------------------------------------------------------
                    __append('<th class="smallcolumn">\n                                    &nbsp;\n                    </th>\n                    ')

                    # <Static value=<ast.Dict object at 0x7f1d6582b1f0> name=None at 7f1d6582b220> -> __attrs_139764233843568
                    __attrs_139764233843568 = _static_139764233843184

                    # <th ... (0:0)
                    # --------------------------------------------------------
                    __append('<th class="smallcolumn" >')
                    __stream_139764233842704 = []
                    __append_139764233842704 = __stream_139764233842704.append
                    __append_139764233842704('\n                                    Applies to subfolders?\n                    ')
                    __msgid_139764233842704 = __re_whitespace(''.join(__stream_139764233842704)).strip()
                    if 'label_contentrules_subfolders':
                        __append(translate('label_contentrules_subfolders', mapping=None, default=__msgid_139764233842704, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</th>\n                    ')

                    # <Static value=<ast.Dict object at 0x7f1d6582b730> name=None at 7f1d6582b760> -> __attrs_139764233844912
                    __attrs_139764233844912 = _static_139764233844528

                    # <th ... (0:0)
                    # --------------------------------------------------------
                    __append('<th class="smallcolumn" >')
                    __stream_139764233844048 = []
                    __append_139764233844048 = __stream_139764233844048.append
                    __append_139764233844048('\n                                    Enabled here?\n                    ')
                    __msgid_139764233844048 = __re_whitespace(''.join(__stream_139764233844048)).strip()
                    if 'label_contentrules_assignment_enabled':
                        __append(translate('label_contentrules_assignment_enabled', mapping=None, default=__msgid_139764233844048, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</th>\n                    ')

                    # <Static value=<ast.Dict object at 0x7f1d6582bc70> name=None at 7f1d6582bca0> -> __attrs_139764233846256
                    __attrs_139764233846256 = _static_139764233845872

                    # <th ... (0:0)
                    # --------------------------------------------------------
                    __append('<th class="smallcolumn" >')
                    __stream_139764233845392 = []
                    __append_139764233845392 = __stream_139764233845392.append
                    __append_139764233845392('\n                                    Enabled?\n                    ')
                    __msgid_139764233845392 = __re_whitespace(''.join(__stream_139764233845392)).strip()
                    if 'label_contentrules_rule_enabled_question':
                        __append(translate('label_contentrules_rule_enabled_question', mapping=None, default=__msgid_139764233845392, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</th>\n                  </tr>\n                </thead>\n                ')

                    # <Static value=<ast.Dict object at 0x7f1d6b720f40> name=None at 7f1d6b721270> -> __attrs_139764233846992
                    __attrs_139764233846992 = _static_139764333416256

                    # <tbody ... (0:0)
                    # --------------------------------------------------------
                    __append('<tbody>\n                  ')

                    # <Static value=<ast.Dict object at 0x7f1d6b720f40> name=None at 7f1d6b721270> -> __attrs_139764233847856
                    __attrs_139764233847856 = _static_139764333416256
                    __backup_rule_139764234861056 = get('rule', __marker)

                    # <Value 'assigned_rules' (245:42)> -> __iterator
                    __token = 8789
                    try:
                        __zt_tmp = __attrs_139764233847856
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_139764333427584('path', 'assigned_rules', econtext=econtext)(_static_139764333427296(econtext, __zt_tmp))
                    (__iterator, ____index_139764233848096, ) = getname('repeat')('rule', __iterator)
                    econtext['rule'] = None
                    for __item in __iterator:
                        econtext['rule'] = __item
                        __append('\n                    ')

                        # <Static value=<ast.Dict object at 0x7f1d6582c910> name=None at 7f1d6582c730> -> __attrs_139764233849632
                        __attrs_139764233849632 = _static_139764233849104
                        __backup_oddrow_139764234853280 = get('oddrow', __marker)

                        # <Value 'repeat/rule/odd' (247:33)> -> __value
                        __token = 8876
                        try:
                            __zt_tmp = __attrs_139764233849632
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_139764333427584('path', 'repeat/rule/odd', econtext=econtext)(_static_139764333427296(econtext, __zt_tmp))
                        econtext['oddrow'] = __value

                        # <tr ... (0:0)
                        # --------------------------------------------------------
                        __append('<tr')

                        # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __default_139764233848672
                        __default_139764233848672 = _DEFAULT_MARKER

                        # <Substitution "python:oddrow and 'even' or 'odd'" (250:32)> -> __attr_class
                        __token = 8992
                        try:
                            __zt_tmp = __attrs_139764233849632
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_class = _static_139764333427584('python', "oddrow and 'even' or 'odd'", econtext=econtext)(_static_139764333427296(econtext, __zt_tmp))
                        __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_class is not None):
                            __append((' class="%s"' % __attr_class))
                        __append(' >\n                      ')

                        # <Static value=<ast.Dict object at 0x7f1d6b720f40> name=None at 7f1d6b721270> -> __attrs_139764233850784
                        __attrs_139764233850784 = _static_139764333416256

                        # <td ... (0:0)
                        # --------------------------------------------------------
                        __append('<td>\n                        ')

                        # <Static value=<ast.Dict object at 0x7f1d6582d540> name=None at 7f1d6582d570> -> __attrs_139764233852656
                        __attrs_139764233852656 = _static_139764233852224

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input name="rule_ids:list" type="checkbox"')

                        # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __default_139764233851360
                        __default_139764233851360 = _DEFAULT_MARKER

                        # <Substitution 'rule/id' (257:39)> -> __attr_value
                        __token = 9288
                        try:
                            __zt_tmp = __attrs_139764233852656
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_value = _static_139764333427584('path', 'rule/id', econtext=econtext)(_static_139764333427296(econtext, __zt_tmp))
                        __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_value is not None):
                            __append((' value="%s"' % __attr_value))
                        __append(' />\n                      </td>\n                      ')

                        # <Static value=<ast.Dict object at 0x7f1d6b720f40> name=None at 7f1d6b721270> -> __attrs_139764233853328
                        __attrs_139764233853328 = _static_139764333416256

                        # <td ... (0:0)
                        # --------------------------------------------------------
                        __append('<td>\n                        ')

                        # <Static value=<ast.Dict object at 0x7f1d6b720f40> name=None at 7f1d6b721270> -> __attrs_139764233854288
                        __attrs_139764233854288 = _static_139764333416256

                        # <dl ... (0:0)
                        # --------------------------------------------------------
                        __append('<dl>\n                          ')

                        # <Static value=<ast.Dict object at 0x7f1d6b720f40> name=None at 7f1d6b721270> -> __attrs_139764233855248
                        __attrs_139764233855248 = _static_139764333416256

                        # <dt ... (0:0)
                        # --------------------------------------------------------
                        __append('<dt>')

                        # <Static value=<ast.Dict object at 0x7f1d6582e470> name=None at 7f1d6582e4a0> -> __attrs_139764233856640
                        __attrs_139764233856640 = _static_139764233856112

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append('<a')

                        # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __default_139764233855920
                        __default_139764233855920 = _DEFAULT_MARKER

                        # <Substitution 'rule/url' (264:38)> -> __attr_href
                        __token = 9529
                        try:
                            __zt_tmp = __attrs_139764233856640
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_139764333427584('path', 'rule/url', econtext=econtext)(_static_139764333427296(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((' href="%s"' % __attr_href))
                        __append('>\n                              ')

                        # <Static value=<ast.Dict object at 0x7f1d6b720f40> name=None at 7f1d6b721270> -> __attrs_139764233858272
                        __attrs_139764233858272 = _static_139764333416256

                        # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __default_139764233858080
                        __default_139764233858080 = _DEFAULT_MARKER

                        # <Value 'rule/title' (266:49)> -> __cache_139764233857600
                        __token = 9622
                        try:
                            __zt_tmp = __attrs_139764233858272
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_139764233857600 = _static_139764333427584('path', 'rule/title', econtext=econtext)(_static_139764333427296(econtext, __zt_tmp))

                        # <BinOp left=<Value 'rule/title' (266:49)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f1d6b6b9c90> at 7f1d6582eb00> -> __condition
                        __expression = __cache_139764233857600

                        # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span></span>')
                        else:
                            __content = __cache_139764233857600
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('\n                              (')

                        # <Static value=<ast.Dict object at 0x7f1d6582f2b0> name=None at 7f1d6582f2e0> -> __attrs_139764233860144
                        __attrs_139764233860144 = _static_139764233859760

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="trigger" >')

                        # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __default_139764233859184
                        __default_139764233859184 = _DEFAULT_MARKER

                        # <Value 'rule/trigger' (268:49)> -> __cache_139764233858704
                        __token = 9744
                        try:
                            __zt_tmp = __attrs_139764233860144
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_139764233858704 = _static_139764333427584('path', 'rule/trigger', econtext=econtext)(_static_139764333427296(econtext, __zt_tmp))

                        # <BinOp left=<Value 'rule/trigger' (268:49)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f1d6b6b9c90> at 7f1d6582ef50> -> __condition
                        __expression = __cache_139764233858704

                        # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('trigger')
                        else:
                            __content = __cache_139764233858704
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</span>)</a></dt>\n                          ')

                        # <Static value=<ast.Dict object at 0x7f1d6b720f40> name=None at 7f1d6b721270> -> __attrs_139764233861392
                        __attrs_139764233861392 = _static_139764333416256

                        # <dd ... (0:0)
                        # --------------------------------------------------------
                        __append('<dd>')

                        # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __default_139764233860816
                        __default_139764233860816 = _DEFAULT_MARKER

                        # <Value 'rule/description' (271:43)> -> __cache_139764233856736
                        __token = 9911
                        try:
                            __zt_tmp = __attrs_139764233861392
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_139764233856736 = _static_139764333427584('path', 'rule/description', econtext=econtext)(_static_139764333427296(econtext, __zt_tmp))

                        # <BinOp left=<Value 'rule/description' (271:43)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f1d6b6b9c90> at 7f1d6582f5b0> -> __condition
                        __expression = __cache_139764233856736

                        # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('\n                                            Rule Description.\n                          ')
                        else:
                            __content = __cache_139764233856736
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</dd>\n                        </dl>\n                      </td>\n                      ')

                        # <Static value=<ast.Dict object at 0x7f1d6582fbb0> name=None at 7f1d6582fbe0> -> __attrs_139764233862448
                        __attrs_139764233862448 = _static_139764233862064

                        # <td ... (0:0)
                        # --------------------------------------------------------
                        __append('<td class="text-center">\n                        ')

                        # <Static value=<ast.Dict object at 0x7f1d6582ff70> name=None at 7f1d6582ffa0> -> __attrs_139764233864528
                        __attrs_139764233864528 = _static_139764233863024

                        # <Value 'not:repeat/rule/start' (278:42)> -> __condition
                        __token = 10214
                        try:
                            __zt_tmp = __attrs_139764233864528
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_139764333427584('not', 'repeat/rule/start', econtext=econtext)(_static_139764333427296(econtext, __zt_tmp))
                        if __condition:

                            # <a ... (0:0)
                            # --------------------------------------------------------
                            __append('<a')

                            # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __default_139764233863520
                            __default_139764233863520 = _DEFAULT_MARKER

                            # <Translate msgid=None node=<ast.Constant object at 0x7f1d65830190> at 7f1d65830220> -> __attr_title
                            __attr_title = 'Move up'
                            __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                            if (__attr_title is not None):
                                __append((' title="%s"' % __attr_title))

                            # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __default_139764233864000
                            __default_139764233864000 = _DEFAULT_MARKER

                            # <Substitution 'string:${view/view_url}?operation=move_up&rule_id=${rule/id}' (280:34)> -> __attr_href
                            __token = 10315
                            try:
                                __zt_tmp = __attrs_139764233864528
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_href = _static_139764333427584('string', '${view/view_url}?operation=move_up&rule_id=${rule/id}', econtext=econtext)(_static_139764333427296(econtext, __zt_tmp))
                            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                            if (__attr_href is not None):
                                __append((' href="%s"' % __attr_href))
                            __append(' >\n                          ')

                            # <Static value=<ast.Dict object at 0x7f1d6b720f40> name=None at 7f1d6b721270> -> __attrs_139764233866160
                            __attrs_139764233866160 = _static_139764333416256

                            # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __default_139764233865968
                            __default_139764233865968 = _DEFAULT_MARKER

                            # <Value "python:icons.tag('caret-up-fill', tag_class='', tag_alt='')" (284:59)> -> __cache_139764233865488
                            __token = 10546
                            try:
                                __zt_tmp = __attrs_139764233866160
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_139764233865488 = _static_139764333427584('python', "icons.tag('caret-up-fill', tag_class='', tag_alt='')", econtext=econtext)(_static_139764333427296(econtext, __zt_tmp))

                            # <BinOp left=<Value "python:icons.tag('caret-up-fill', tag_class='', tag_alt='')" (284:59)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f1d6b6b9c90> at 7f1d658309d0> -> __condition
                            __expression = __cache_139764233865488

                            # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                pass
                            else:
                                __content = __cache_139764233865488
                                __content = __convert(__content)
                                if (__content is not None):
                                    __append(__content)
                            __append('\n                        </a>')
                        __append('\n                        ')

                        # <Static value=<ast.Dict object at 0x7f1d65830f40> name=None at 7f1d65830f70> -> __attrs_139764233867696
                        __attrs_139764233867696 = _static_139764233867072

                        # <Value 'not:repeat/rule/end' (287:42)> -> __condition
                        __token = 10726
                        try:
                            __zt_tmp = __attrs_139764233867696
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_139764333427584('not', 'repeat/rule/end', econtext=econtext)(_static_139764333427296(econtext, __zt_tmp))
                        if __condition:

                            # <a ... (0:0)
                            # --------------------------------------------------------
                            __append('<a')

                            # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __default_139764233866592
                            __default_139764233866592 = _DEFAULT_MARKER

                            # <Translate msgid=None node=<ast.Constant object at 0x7f1d65830df0> at 7f1d65830e20> -> __attr_title
                            __attr_title = 'Move down'
                            __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                            if (__attr_title is not None):
                                __append((' title="%s"' % __attr_title))

                            # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __default_139764233867168
                            __default_139764233867168 = _DEFAULT_MARKER

                            # <Substitution 'string:${view/view_url}?operation=move_down&rule_id=${rule/id}' (289:34)> -> __attr_href
                            __token = 10825
                            try:
                                __zt_tmp = __attrs_139764233867696
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_href = _static_139764333427584('string', '${view/view_url}?operation=move_down&rule_id=${rule/id}', econtext=econtext)(_static_139764333427296(econtext, __zt_tmp))
                            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                            if (__attr_href is not None):
                                __append((' href="%s"' % __attr_href))
                            __append(' >\n                          ')

                            # <Static value=<ast.Dict object at 0x7f1d6b720f40> name=None at 7f1d6b721270> -> __attrs_139764233869328
                            __attrs_139764233869328 = _static_139764333416256

                            # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __default_139764233869136
                            __default_139764233869136 = _DEFAULT_MARKER

                            # <Value "python:icons.tag('caret-down-fill', tag_class='', tag_alt='')" (293:59)> -> __cache_139764233868656
                            __token = 11058
                            try:
                                __zt_tmp = __attrs_139764233869328
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_139764233868656 = _static_139764333427584('python', "icons.tag('caret-down-fill', tag_class='', tag_alt='')", econtext=econtext)(_static_139764333427296(econtext, __zt_tmp))

                            # <BinOp left=<Value "python:icons.tag('caret-down-fill', tag_class='', tag_alt='')" (293:59)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f1d6b6b9c90> at 7f1d65831630> -> __condition
                            __expression = __cache_139764233868656

                            # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                pass
                            else:
                                __content = __cache_139764233868656
                                __content = __convert(__content)
                                if (__content is not None):
                                    __append(__content)
                            __append('\n                        </a>')
                        __append('\n                      </td>\n                      ')

                        # <Static value=<ast.Dict object at 0x7f1d658319c0> name=None at 7f1d65831510> -> __attrs_139764233870096
                        __attrs_139764233870096 = _static_139764233869760

                        # <td ... (0:0)
                        # --------------------------------------------------------
                        __append('<td class="checker listingCheckbox">\n                        ')

                        # <Static value=<ast.Dict object at 0x7f1d65831ed0> name=None at 7f1d65831f00> -> __attrs_139764233872208
                        __attrs_139764233872208 = _static_139764233871056

                        # <Value 'rule/bubbles' (297:49)> -> __condition
                        __token = 11289
                        try:
                            __zt_tmp = __attrs_139764233872208
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_139764333427584('path', 'rule/bubbles', econtext=econtext)(_static_139764333427296(econtext, __zt_tmp))
                        if __condition:

                            # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __default_139764233872016
                            __default_139764233872016 = _DEFAULT_MARKER

                            # <Value "python:icons.tag('check-circle-fill', tag_class='text-success', tag_alt='Active')" (298:57)> -> __cache_139764233871536
                            __token = 11360
                            try:
                                __zt_tmp = __attrs_139764233872208
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_139764233871536 = _static_139764333427584('python', "icons.tag('check-circle-fill', tag_class='text-success', tag_alt='Active')", econtext=econtext)(_static_139764333427296(econtext, __zt_tmp))

                            # <BinOp left=<Value "python:icons.tag('check-circle-fill', tag_class='text-success', tag_alt='Active')" (298:57)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f1d6b6b9c90> at 7f1d65832170> -> __condition
                            __expression = __cache_139764233871536

                            # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                pass
                            else:
                                __content = __cache_139764233871536
                                __content = __convert(__content)
                                if (__content is not None):
                                    __append(__content)
                        __append('\n                      </td>\n                      ')

                        # <Static value=<ast.Dict object at 0x7f1d65831f60> name=None at 7f1d65831db0> -> __attrs_139764233872880
                        __attrs_139764233872880 = _static_139764233871200

                        # <td ... (0:0)
                        # --------------------------------------------------------
                        __append('<td class="checker listingCheckbox">\n                        ')

                        # <Static value=<ast.Dict object at 0x7f1d658329b0> name=None at 7f1d658329e0> -> __attrs_139764233874992
                        __attrs_139764233874992 = _static_139764233873840

                        # <Value 'rule/enabled' (303:49)> -> __condition
                        __token = 11689
                        try:
                            __zt_tmp = __attrs_139764233874992
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_139764333427584('path', 'rule/enabled', econtext=econtext)(_static_139764333427296(econtext, __zt_tmp))
                        if __condition:

                            # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __default_139764233874800
                            __default_139764233874800 = _DEFAULT_MARKER

                            # <Value "python:icons.tag('check-circle-fill', tag_class='text-success', tag_alt='Active')" (304:57)> -> __cache_139764233874320
                            __token = 11760
                            try:
                                __zt_tmp = __attrs_139764233874992
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_139764233874320 = _static_139764333427584('python', "icons.tag('check-circle-fill', tag_class='text-success', tag_alt='Active')", econtext=econtext)(_static_139764333427296(econtext, __zt_tmp))

                            # <BinOp left=<Value "python:icons.tag('check-circle-fill', tag_class='text-success', tag_alt='Active')" (304:57)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f1d6b6b9c90> at 7f1d65832c50> -> __condition
                            __expression = __cache_139764233874320

                            # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                pass
                            else:
                                __content = __cache_139764233874320
                                __content = __convert(__content)
                                if (__content is not None):
                                    __append(__content)
                        __append('\n                      </td>\n                      ')

                        # <Static value=<ast.Dict object at 0x7f1d65832a40> name=None at 7f1d65832890> -> __attrs_139764233875616
                        __attrs_139764233875616 = _static_139764233873984

                        # <td ... (0:0)
                        # --------------------------------------------------------
                        __append('<td class="checker listingCheckbox">\n                        ')

                        # <Static value=<ast.Dict object at 0x7f1d65833460> name=None at 7f1d65833490> -> __attrs_139764233877728
                        __attrs_139764233877728 = _static_139764233876576

                        # <Value 'rule/global_enabled' (309:49)> -> __condition
                        __token = 12089
                        try:
                            __zt_tmp = __attrs_139764233877728
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_139764333427584('path', 'rule/global_enabled', econtext=econtext)(_static_139764333427296(econtext, __zt_tmp))
                        if __condition:

                            # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __default_139764233877536
                            __default_139764233877536 = _DEFAULT_MARKER

                            # <Value "python:icons.tag('check-circle-fill', tag_class='text-success', tag_alt='Active')" (310:57)> -> __cache_139764233877056
                            __token = 12167
                            try:
                                __zt_tmp = __attrs_139764233877728
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_139764233877056 = _static_139764333427584('python', "icons.tag('check-circle-fill', tag_class='text-success', tag_alt='Active')", econtext=econtext)(_static_139764333427296(econtext, __zt_tmp))

                            # <BinOp left=<Value "python:icons.tag('check-circle-fill', tag_class='text-success', tag_alt='Active')" (310:57)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f1d6b6b9c90> at 7f1d65833700> -> __condition
                            __expression = __cache_139764233877056

                            # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                pass
                            else:
                                __content = __cache_139764233877056
                                __content = __convert(__content)
                                if (__content is not None):
                                    __append(__content)
                        __append('\n                      </td>\n                    </tr>')
                        if (__backup_oddrow_139764234853280 is __marker):
                            del econtext['oddrow']
                        else:
                            econtext['oddrow'] = __backup_oddrow_139764234853280
                        __append('\n                  ')
                        ____index_139764233848096 -= 1
                        if (____index_139764233848096 > 0):
                            __append('')
                    if (__backup_rule_139764234861056 is __marker):
                        del econtext['rule']
                    else:
                        econtext['rule'] = __backup_rule_139764234861056
                    __append('\n                </tbody>\n              </table>\n\n              ')

                    # <Static value=<ast.Dict object at 0x7f1d6582c790> name=None at 7f1d6582cc40> -> __attrs_139764233876912
                    __attrs_139764233876912 = _static_139764233848720

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="formControls">\n                ')

                    # <Static value=<ast.Dict object at 0x7f1d65833fa0> name=None at 7f1d65833fd0> -> __attrs_139764233945680
                    __attrs_139764233945680 = _static_139764233879456

                    # <button ... (0:0)
                    # --------------------------------------------------------
                    __append('<button class="context btn btn-primary" name="form.button.Enable" type="submit"')

                    # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __default_139764233945152
                    __default_139764233945152 = _DEFAULT_MARKER

                    # <Translate msgid='label_enable' node=<ast.Constant object at 0x7f1d65833be0> at 7f1d65833bb0> -> __attr_value
                    __attr_value = 'Enable'
                    __attr_value = translate('label_enable', default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append(' >')
                    __stream_139764233878208 = []
                    __append_139764233878208 = __stream_139764233878208.append
                    __append_139764233878208('Enable')
                    __msgid_139764233878208 = __re_whitespace(''.join(__stream_139764233878208)).strip()
                    if 'label_enable':
                        __append(translate('label_enable', mapping=None, default=__msgid_139764233878208, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</button>\n                ')

                    # <Static value=<ast.Dict object at 0x7f1d65844b50> name=None at 7f1d65844b80> -> __attrs_139764233946256
                    __attrs_139764233946256 = _static_139764233947984

                    # <button ... (0:0)
                    # --------------------------------------------------------
                    __append('<button class="standalone btn btn-primary" name="form.button.Disable" type="submit"')

                    # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __default_139764233946880
                    __default_139764233946880 = _DEFAULT_MARKER

                    # <Translate msgid='label_disable' node=<ast.Constant object at 0x7f1d658447c0> at 7f1d65844790> -> __attr_value
                    __attr_value = 'Disable'
                    __attr_value = translate('label_disable', default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append(' >')
                    __stream_139764233946160 = []
                    __append_139764233946160 = __stream_139764233946160.append
                    __append_139764233946160('Disable')
                    __msgid_139764233946160 = __re_whitespace(''.join(__stream_139764233946160)).strip()
                    if 'label_disable':
                        __append(translate('label_disable', mapping=None, default=__msgid_139764233946160, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</button>\n                ')

                    # <Static value=<ast.Dict object at 0x7f1d65845450> name=None at 7f1d65845480> -> __attrs_139764233950384
                    __attrs_139764233950384 = _static_139764233950288

                    # <button ... (0:0)
                    # --------------------------------------------------------
                    __append('<button class="standalone btn btn-primary" name="form.button.Bubble" type="submit"')

                    # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __default_139764233949184
                    __default_139764233949184 = _DEFAULT_MARKER

                    # <Translate msgid='label_apply_to_subfolders' node=<ast.Constant object at 0x7f1d658450c0> at 7f1d65845090> -> __attr_value
                    __attr_value = 'Apply to subfolders'
                    __attr_value = translate('label_apply_to_subfolders', default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append(' >')
                    __stream_139764233948512 = []
                    __append_139764233948512 = __stream_139764233948512.append
                    __append_139764233948512('Apply to subfolders')
                    __msgid_139764233948512 = __re_whitespace(''.join(__stream_139764233948512)).strip()
                    if 'label_apply_to_subfolders':
                        __append(translate('label_apply_to_subfolders', mapping=None, default=__msgid_139764233948512, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</button>\n                ')

                    # <Static value=<ast.Dict object at 0x7f1d65845db0> name=None at 7f1d65845de0> -> __attrs_139764233952784
                    __attrs_139764233952784 = _static_139764233952688

                    # <button ... (0:0)
                    # --------------------------------------------------------
                    __append('<button class="standalone btn btn-primary" name="form.button.NoBubble" type="submit"')

                    # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __default_139764233951584
                    __default_139764233951584 = _DEFAULT_MARKER

                    # <Translate msgid='label_disable_apply_to_subfolders' node=<ast.Constant object at 0x7f1d65845a20> at 7f1d658459f0> -> __attr_value
                    __attr_value = 'Disable apply to subfolders'
                    __attr_value = translate('label_disable_apply_to_subfolders', default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append(' >')
                    __stream_139764233950864 = []
                    __append_139764233950864 = __stream_139764233950864.append
                    __append_139764233950864('Disable apply to subfolders')
                    __msgid_139764233950864 = __re_whitespace(''.join(__stream_139764233950864)).strip()
                    if 'label_disable_apply_to_subfolders':
                        __append(translate('label_disable_apply_to_subfolders', mapping=None, default=__msgid_139764233950864, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</button>\n                ')

                    # <Static value=<ast.Dict object at 0x7f1d65846710> name=None at 7f1d65846740> -> __attrs_139764233953360
                    __attrs_139764233953360 = _static_139764233955088

                    # <button ... (0:0)
                    # --------------------------------------------------------
                    __append('<button class="destructive btn btn-danger" name="form.button.Delete" type="submit"')

                    # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __default_139764233953984
                    __default_139764233953984 = _DEFAULT_MARKER

                    # <Translate msgid='label_unassign' node=<ast.Constant object at 0x7f1d65846380> at 7f1d65846350> -> __attr_value
                    __attr_value = 'Unassign'
                    __attr_value = translate('label_unassign', default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append(' >')
                    __stream_139764233953264 = []
                    __append_139764233953264 = __stream_139764233953264.append
                    __append_139764233953264('Unassign')
                    __msgid_139764233953264 = __re_whitespace(''.join(__stream_139764233953264)).strip()
                    if 'label_unassign':
                        __append(translate('label_unassign', mapping=None, default=__msgid_139764233953264, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</button>\n              </div>\n            </form>')
                if (__backup_assigned_rules_139764234857696 is __marker):
                    del econtext['assigned_rules']
                else:
                    econtext['assigned_rules'] = __backup_assigned_rules_139764234857696
                __append('\n          </div>\n        </div>\n\n      </article>\n\n    ')
                if (__backup_icons_139764239314768 is __marker):
                    del econtext['icons']
                else:
                    econtext['icons'] = __backup_icons_139764239314768
            _slots = econtext['__slot_body'] = _deque((__fill_body, ))

            # <Value 'context/main_template/macros/master' (6:23)> -> __macro
            __token = 247
            try:
                __zt_tmp = __attrs_139764234738880
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_139764333427584('path', 'context/main_template/macros/master', econtext=econtext)(_static_139764333427296(econtext, __zt_tmp))
            __token = 247
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139764237808576 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139764237808576
            __i18n_domain = __previous_i18n_domain_139764234736864
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }