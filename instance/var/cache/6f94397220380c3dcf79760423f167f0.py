# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/plone/app/workflow/browser/sharing.pt'

__tokens = {4298: ('view/roles', 120, 41), 4346: (' python:len(available_roles) + ', 121, 36), 4417: ('s view/role_settin', 122, 37), 4739: ('python:len(role_settings) &gt', 130, 39), 4989: ('available_roles', 135, 43), 5045: ('role/title', 136, 39), 5383: ('role_settings', 145, 47), 5475: ("python:entry['type'] == 'group'", 147, 37), 5544: (' entry/disabled | python:Fals', 148, 36), 5609: ('w repeat/entry/o', 149, 33), 5661: ("ky python:entry['id'] in view.STI", 150, 32), 5804: ("python:oddrow and 'odd' or 'even'", 153, 34), 6018: ('entry/id', 158, 36), 6135: ('is_group', 161, 51), 6204: ("python:icons.tag('people', tag_alt='Group')", 162, 59), 6329: ('not: is_group', 164, 51), 6403: ("python:icons.tag('person', tag_alt='User')", 165, 59), 6520: ("python:not is_group or not can_view_groups or entry.get('id') == 'AuthenticatedUsers'", 168, 43), 6689: ('string:${portal_url}/@@usergroup-groupmembership?groupname=${entry/id}', 170, 36), 6871: ('sticky', 173, 51), 6929: ('entry/title', 174, 49), 7046: ('not:sticky', 176, 54), 7108: ('entry/title', 177, 49), 7341: ('(${entry/id})', 181, 60), 7344: ('entry/id', 181, 63), 7624: ('not:disabled', 188, 48), 7729: ('entry/id', 190, 41), 7959: ('not:disabled', 195, 48), 8064: ('entry/type', 197, 41), 8267: ('available_roles', 202, 45), 8406: ("python:entry['roles'][role['id']]", 205, 50), 8534: ("python:entry_role == 'global'", 207, 53), 8626: ("python:icons.tag('globe', tag_alt='Global')", 208, 61), 8755: ("python:entry_role == 'acquired'", 210, 53), 8849: ("python:icons.tag('diagram-2', tag_alt='Inherited')", 211, 61), 8982: ('python:entry_role in (True, False)', 213, 50), 9274: ('string:entries.role_${role/id}:records', 218, 44), 9360: (" python:entry_role and 'checked' or Non", 219, 46), 9448: ('d python:disabled or No', 220, 46), 292: ('context/@@plone_context_state', 15, 32), 353: (' context/@@plone_portal_stat', 16, 30), 407: ('l portal_state/port', 17, 23), 456: ('rl portal_state/portal_', 18, 26), 514: ('ion nocall:context/portal_membership/checkPermis', 19, 30), 597: ("oups python:checkPermission('Plone Site Setup: Users and Groups', po", 20, 29), 841: ('context_state/is_default_page', 28, 30), 1345: ('context_state/folder', 40, 26), 1444: ('string:${folder/absolute_url}/sharing', 43, 24), 1840: ('context/Title', 55, 28), 2182: ('not:ajax_load', 66, 30), 2235: ('provider:plone.abovecontentbody', 67, 38), 2463: ('string:${context/absolute_url}/@@sharing', 74, 27), 3067: ('${request/search_term|nothing}', 91, 30), 3069: ('request/search_term|nothing', 91, 32), 3687: ('string:${context/absolute_url}/@@sharing', 106, 27), 9898: ('view/can_edit_inherit', 234, 34), 10349: ("python:view.inherited() and 'checked' or None", 244, 35), 11244: ("python:icons.tag('diagram-2', tag_alt='Inherited')", 260, 53), 11518: ("python:icons.tag('globe', tag_alt='Global')", 264, 53), 12336: ('context/@@authenticator/authenticator', 282, 44), 82: ('context/main_template/macros/master', 3, 23), 82: ('context/main_template/macros/master', 3, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from collections import deque as _deque
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140478190747312 = {'class': 'btn btn-secondary', 'name': 'form.button.Cancel', 'type': 'submit', }
_static_140478190746160 = {'class': 'btn btn-primary', 'id': 'sharing-save-button', 'name': 'form.button.Save', 'type': 'submit', }
_static_140478190741408 = {'class': 'form-text text-muted', }
_static_140478190740304 = {'class': 'form-check-label', 'for': 'inherit', }
_static_140478190738432 = {'class': 'form-check-input single-checkbox-bool-widget bool-field', 'id': 'inherit', 'checked': 'checked', 'name': 'inherit:boolean', 'type': 'checkbox', 'value': '1', }
_static_140478190735696 = {'class': 'form-check', }
_static_140478190674624 = {'class': 'mb-3', 'id': 'field-inherit', }
_static_140478190662176 = {'id': 'user-group-sharing-container', }
_static_140478190661024 = {'name': 'form.submitted:boolean', 'type': 'hidden', 'value': 'True', }
_static_140478190659248 = {'method': 'post', 'action': 'string:${context/absolute_url}/@@sharing', }
_static_140478190657712 = {'class': 'btn btn-primary', 'id': 'sharing-search-button', 'name': 'form.button.Search', 'type': 'submit', 'value': 'Search', }
_static_140478190655936 = {'class': 'form-control', 'id': 'sharing-user-group-search', 'name': 'search_term', 'placeholder': 'Search for user or group', 'size': '30', 'title': 'Search for user or group', 'type': 'text', 'value': '${request/search_term|nothing}', }
_static_140478190651424 = {'class': 'mb-3', }
_static_140478190650320 = {'name': 'form.submitted:boolean', 'type': 'hidden', 'value': 'True', }
_static_140478190631856 = {'class': 'form-inline pb-4 pt-3', 'method': 'post', 'action': 'string:${context/absolute_url}/@@sharing', }
_static_140478190630032 = {'id': 'content-core', }
_static_140478190627152 = {'class': 'documentDescription', }
_static_140478190624128 = {'class': 'documentFirstHeading', }
_static_140478190622832 = {'class': 'alert-link', 'href': 'string:${folder/absolute_url}/sharing', }
_static_140478190618896 = {'class': 'alert alert-info', 'role': 'alert', }
_static_140478190304608 = {'id': 'content', }
_static_140478191589056 = 'master'
_static_140478190734112 = {'class': 'noborder', 'type': 'checkbox', 'value': 'True', 'name': 'string:entries.role_${role/id}:records', 'checked': "python:entry_role and 'checked' or None", 'disabled': 'python:disabled or None', }
_static_140478190709744 = {'class': 'listingCheckbox', }
_static_140478190708448 = {'name': 'entries.type:records', 'type': 'hidden', 'value': 'entry/type', }
_static_140478190706576 = {'name': 'entries.id:records', 'type': 'hidden', 'value': 'entry/id', }
_static_140478190705472 = {'class': 'text-muted', 'condition': 'entry/id|nothing', }
_static_140478190681872 = {'href': 'string:${portal_url}/@@usergroup-groupmembership?groupname=${entry/id}', }
_static_140478190678080 = {'class': 'text-left', 'title': 'entry/id', }
_static_140478190675008 = {'class': "python:oddrow and 'odd' or 'even'", }
_static_140478190672464 = {'id': 'user-group-sharing-settings', }
_static_140478190671216 = {'class': 'nosort', }
_static_140478190669248 = {'class': 'text-left', }
_static_140478276897232 = {}
_static_140478190666464 = {'id': 'user-group-sharing-head', }
_static_140478276908272 = __C2ZContextWrapper
_static_140478276908560 = __compile_zt_expr
_static_140478190663856 = {'class': 'table table-responsive table-bordered table-striped text-center', 'id': 'user-group-sharing', 'summary': 'Current sharing permissions', }

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

    def render_user_group_sharing(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<ast.Dict object at 0x7fc3a0a738b0> name=None at 7fc3a0a738e0> -> __attrs_140478190664624
            __attrs_140478190664624 = _static_140478190663856
            __backup_available_roles_140478190620720 = get('available_roles', __marker)

            # <Value 'view/roles' (120:41)> -> __value
            __token = 4298
            try:
                __zt_tmp = __attrs_140478190664624
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140478276908560('path', 'view/roles', econtext=econtext)(_static_140478276908272(econtext, __zt_tmp))
            econtext['available_roles'] = __value
            __backup_num_columns_140478190619568 = get('num_columns', __marker)

            # <Value 'python:len(available_roles) + 1' (121:36)> -> __value
            __token = 4346
            try:
                __zt_tmp = __attrs_140478190664624
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140478276908560('python', 'len(available_roles) + 1', econtext=econtext)(_static_140478276908272(econtext, __zt_tmp))
            econtext['num_columns'] = __value
            __backup_role_settings_140478190623360 = get('role_settings', __marker)

            # <Value 'view/role_settings' (122:37)> -> __value
            __token = 4417
            try:
                __zt_tmp = __attrs_140478190664624
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140478276908560('path', 'view/role_settings', econtext=econtext)(_static_140478276908272(econtext, __zt_tmp))
            econtext['role_settings'] = __value

            # <table ... (0:0)
            # --------------------------------------------------------
            __append('<table class="table table-responsive table-bordered table-striped text-center" id="user-group-sharing"')

            # <Symbol value=<DEFAULT> at 7fc3a5c49720> -> __default_140478190664096
            __default_140478190664096 = _DEFAULT_MARKER

            # <Translate msgid='summary_assigned_roles' node=<ast.Constant object at 0x7fc3a0a735e0> at 7fc3a0a735b0> -> __attr_summary
            __attr_summary = 'Current sharing permissions'
            __attr_summary = translate('summary_assigned_roles', default=__attr_summary, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
            if (__attr_summary is not None):
                __append((' summary="%s"' % __attr_summary))
            __append(' >\n\n                  ')
            __token = None
            render_user_group_sharing_head(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n\n                  ')
            __token = None
            render_user_group_sharing_settings(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n                </table>')
            if (__backup_role_settings_140478190623360 is __marker):
                del econtext['role_settings']
            else:
                econtext['role_settings'] = __backup_role_settings_140478190623360
            if (__backup_num_columns_140478190619568 is __marker):
                del econtext['num_columns']
            else:
                econtext['num_columns'] = __backup_num_columns_140478190619568
            if (__backup_available_roles_140478190620720 is __marker):
                del econtext['available_roles']
            else:
                econtext['available_roles'] = __backup_available_roles_140478190620720
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_user_group_sharing_head(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<ast.Dict object at 0x7fc3a0a742e0> name=None at 7fc3a0a74160> -> __attrs_140478190666800
            __attrs_140478190666800 = _static_140478190666464

            # <thead ... (0:0)
            # --------------------------------------------------------
            __append('<thead id="user-group-sharing-head" >\n                    ')

            # <Static value=<ast.Dict object at 0x7fc3a5cb09d0> name=None at 7fc3a5cb0d00> -> __attrs_140478190667904
            __attrs_140478190667904 = _static_140478276897232

            # <Value 'python:len(role_settings) > 0' (130:39)> -> __condition
            __token = 4739
            try:
                __zt_tmp = __attrs_140478190667904
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140478276908560('python', 'len(role_settings) > 0', econtext=econtext)(_static_140478276908272(econtext, __zt_tmp))
            if __condition:

                # <tr ... (0:0)
                # --------------------------------------------------------
                __append('<tr>\n                      ')

                # <Static value=<ast.Dict object at 0x7fc3a0a74dc0> name=None at 7fc3a0a74df0> -> __attrs_140478190669632
                __attrs_140478190669632 = _static_140478190669248

                # <th ... (0:0)
                # --------------------------------------------------------
                __append('<th class="text-left" >')
                __stream_140478190668768 = []
                __append_140478190668768 = __stream_140478190668768.append
                __append_140478190668768('Name')
                __msgid_140478190668768 = __re_whitespace(''.join(__stream_140478190668768)).strip()
                if 'label_name':
                    __append(translate('label_name', mapping=None, default=__msgid_140478190668768, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</th>\n                      ')

                # <Static value=<ast.Dict object at 0x7fc3a0a75570> name=None at 7fc3a0a755a0> -> __attrs_140478190671600
                __attrs_140478190671600 = _static_140478190671216
                __backup_role_140478190668096 = get('role', __marker)

                # <Value 'available_roles' (135:43)> -> __iterator
                __token = 4989
                try:
                    __zt_tmp = __attrs_140478190671600
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140478276908560('path', 'available_roles', econtext=econtext)(_static_140478276908272(econtext, __zt_tmp))
                (__iterator, ____index_140478190671888, ) = getname('repeat')('role', __iterator)
                econtext['role'] = None
                for __item in __iterator:
                    econtext['role'] = __item

                    # <th ... (0:0)
                    # --------------------------------------------------------
                    __append('<th class="nosort" >')

                    # <Symbol value=<DEFAULT> at 7fc3a5c49720> -> __default_140478190670640
                    __default_140478190670640 = _DEFAULT_MARKER

                    # <Value 'role/title' (136:39)> -> __cache_140478190670160
                    __token = 5045
                    try:
                        __zt_tmp = __attrs_140478190671600
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140478190670160 = _static_140478276908560('path', 'role/title', econtext=econtext)(_static_140478276908272(econtext, __zt_tmp))

                    # <BinOp left=<Value 'role/title' (136:39)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fc3a5c49720> at 7fc3a0a75210> -> __condition
                    __expression = __cache_140478190670160

                    # <Symbol value=<DEFAULT> at 7fc3a5c49720> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140478190670160
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</th>')
                    ____index_140478190671888 -= 1
                    if (____index_140478190671888 > 0):
                        __append('\n                      ')
                if (__backup_role_140478190668096 is __marker):
                    del econtext['role']
                else:
                    econtext['role'] = __backup_role_140478190668096
                __append('\n                    </tr>')
            __append('\n                  </thead>')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_user_group_sharing_settings(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<ast.Dict object at 0x7fc3a0a75a50> name=None at 7fc3a0a757e0> -> __attrs_140478190672800
            __attrs_140478190672800 = _static_140478190672464

            # <tbody ... (0:0)
            # --------------------------------------------------------
            __append('<tbody id="user-group-sharing-settings" >\n                    ')

            # <Static value=<ast.Dict object at 0x7fc3a5cb09d0> name=None at 7fc3a5cb0d00> -> __attrs_140478190673760
            __attrs_140478190673760 = _static_140478276897232
            __backup_entry_140478190664768 = get('entry', __marker)

            # <Value 'role_settings' (145:47)> -> __iterator
            __token = 5383
            try:
                __zt_tmp = __attrs_140478190673760
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140478276908560('path', 'role_settings', econtext=econtext)(_static_140478276908272(econtext, __zt_tmp))
            (__iterator, ____index_140478190674000, ) = getname('repeat')('entry', __iterator)
            econtext['entry'] = None
            for __item in __iterator:
                econtext['entry'] = __item
                __append('\n                      ')

                # <Static value=<ast.Dict object at 0x7fc3a0a76440> name=None at 7fc3a0a76260> -> __attrs_140478190675584
                __attrs_140478190675584 = _static_140478190675008
                __backup_is_group_140478190667088 = get('is_group', __marker)

                # <Value "python:entry['type'] == 'group'" (147:37)> -> __value
                __token = 5475
                try:
                    __zt_tmp = __attrs_140478190675584
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140478276908560('python', "entry['type'] == 'group'", econtext=econtext)(_static_140478276908272(econtext, __zt_tmp))
                econtext['is_group'] = __value
                __backup_disabled_140478190668480 = get('disabled', __marker)

                # <Value 'entry/disabled | python:False' (148:36)> -> __value
                __token = 5544
                try:
                    __zt_tmp = __attrs_140478190675584
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140478276908560('path', 'entry/disabled | python:False', econtext=econtext)(_static_140478276908272(econtext, __zt_tmp))
                econtext['disabled'] = __value
                __backup_oddrow_140478190669968 = get('oddrow', __marker)

                # <Value 'repeat/entry/odd' (149:33)> -> __value
                __token = 5609
                try:
                    __zt_tmp = __attrs_140478190675584
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140478276908560('path', 'repeat/entry/odd', econtext=econtext)(_static_140478276908272(econtext, __zt_tmp))
                econtext['oddrow'] = __value
                __backup_sticky_140478190671792 = get('sticky', __marker)

                # <Value "python:entry['id'] in view.STICKY" (150:32)> -> __value
                __token = 5661
                try:
                    __zt_tmp = __attrs_140478190675584
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140478276908560('python', "entry['id'] in view.STICKY", econtext=econtext)(_static_140478276908272(econtext, __zt_tmp))
                econtext['sticky'] = __value

                # <tr ... (0:0)
                # --------------------------------------------------------
                __append('<tr')

                # <Symbol value=<DEFAULT> at 7fc3a5c49720> -> __default_140478190674576
                __default_140478190674576 = _DEFAULT_MARKER

                # <Substitution "python:oddrow and 'odd' or 'even'" (153:34)> -> __attr_class
                __token = 5804
                try:
                    __zt_tmp = __attrs_140478190675584
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_class = _static_140478276908560('python', "oddrow and 'odd' or 'even'", econtext=econtext)(_static_140478276908272(econtext, __zt_tmp))
                __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_class is not None):
                    __append((' class="%s"' % __attr_class))
                __append(' >\n                        ')

                # <Static value=<ast.Dict object at 0x7fc3a0a77040> name=None at 7fc3a0a76ce0> -> __attrs_140478190678272
                __attrs_140478190678272 = _static_140478190678080

                # <td ... (0:0)
                # --------------------------------------------------------
                __append('<td class="text-left"')

                # <Symbol value=<DEFAULT> at 7fc3a5c49720> -> __default_140478190677600
                __default_140478190677600 = _DEFAULT_MARKER

                # <Substitution 'entry/id' (158:36)> -> __attr_title
                __token = 6018
                try:
                    __zt_tmp = __attrs_140478190678272
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_title = _static_140478276908560('path', 'entry/id', econtext=econtext)(_static_140478276908272(econtext, __zt_tmp))
                __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_title is not None):
                    __append((' title="%s"' % __attr_title))
                __append(' >\n                          ')

                # <Static value=<ast.Dict object at 0x7fc3a5cb09d0> name=None at 7fc3a5cb0d00> -> __attrs_140478190679808
                __attrs_140478190679808 = _static_140478276897232

                # <Value 'is_group' (161:51)> -> __condition
                __token = 6135
                try:
                    __zt_tmp = __attrs_140478190679808
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140478276908560('path', 'is_group', econtext=econtext)(_static_140478276908272(econtext, __zt_tmp))
                if __condition:

                    # <Symbol value=<DEFAULT> at 7fc3a5c49720> -> __default_140478190679616
                    __default_140478190679616 = _DEFAULT_MARKER

                    # <Value "python:icons.tag('people', tag_alt='Group')" (162:59)> -> __cache_140478190679088
                    __token = 6204
                    try:
                        __zt_tmp = __attrs_140478190679808
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140478190679088 = _static_140478276908560('python', "icons.tag('people', tag_alt='Group')", econtext=econtext)(_static_140478276908272(econtext, __zt_tmp))

                    # <BinOp left=<Value "python:icons.tag('people', tag_alt='Group')" (162:59)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fc3a5c49720> at 7fc3a0a77520> -> __condition
                    __expression = __cache_140478190679088

                    # <Symbol value=<DEFAULT> at 7fc3a5c49720> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140478190679088
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                __append('\n                          ')

                # <Static value=<ast.Dict object at 0x7fc3a5cb09d0> name=None at 7fc3a5cb0d00> -> __attrs_140478190681152
                __attrs_140478190681152 = _static_140478276897232

                # <Value 'not: is_group' (164:51)> -> __condition
                __token = 6329
                try:
                    __zt_tmp = __attrs_140478190681152
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140478276908560('not', ' is_group', econtext=econtext)(_static_140478276908272(econtext, __zt_tmp))
                if __condition:

                    # <Symbol value=<DEFAULT> at 7fc3a5c49720> -> __default_140478190680960
                    __default_140478190680960 = _DEFAULT_MARKER

                    # <Value "python:icons.tag('person', tag_alt='User')" (165:59)> -> __cache_140478190680432
                    __token = 6403
                    try:
                        __zt_tmp = __attrs_140478190681152
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140478190680432 = _static_140478276908560('python', "icons.tag('person', tag_alt='User')", econtext=econtext)(_static_140478276908272(econtext, __zt_tmp))

                    # <BinOp left=<Value "python:icons.tag('person', tag_alt='User')" (165:59)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fc3a5c49720> at 7fc3a0a77a60> -> __condition
                    __expression = __cache_140478190680432

                    # <Symbol value=<DEFAULT> at 7fc3a5c49720> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140478190680432
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                __append('\n\n                          ')

                # <Static value=<ast.Dict object at 0x7fc3a0a77f10> name=None at 7fc3a0a77f40> -> __attrs_140478190699376
                __attrs_140478190699376 = _static_140478190681872

                # <Negate value=<Value "python:not is_group or not can_view_groups or entry.get('id') == 'AuthenticatedUsers'" (168:43)> at 7fc3a0a7c190> -> __cache_140478190698896

                # <Value "python:not is_group or not can_view_groups or entry.get('id') == 'AuthenticatedUsers'" (168:43)> -> __cache_140478190698896
                __token = 6520
                try:
                    __zt_tmp = __attrs_140478190699376
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140478190698896 = _static_140478276908560('python', "not is_group or not can_view_groups or entry.get('id') == 'AuthenticatedUsers'", econtext=econtext)(_static_140478276908272(econtext, __zt_tmp))
                __cache_140478190698896 = not __cache_140478190698896
                __condition = __cache_140478190698896
                if __condition:

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 7fc3a5c49720> -> __default_140478190681344
                    __default_140478190681344 = _DEFAULT_MARKER

                    # <Substitution 'string:${portal_url}/@@usergroup-groupmembership?groupname=${entry/id}' (170:36)> -> __attr_href
                    __token = 6689
                    try:
                        __zt_tmp = __attrs_140478190699376
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140478276908560('string', '${portal_url}/@@usergroup-groupmembership?groupname=${entry/id}', econtext=econtext)(_static_140478276908272(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))
                    __append(' >')
                __append('\n                            ')

                # <Static value=<ast.Dict object at 0x7fc3a5cb09d0> name=None at 7fc3a5cb0d00> -> __attrs_140478190700240
                __attrs_140478190700240 = _static_140478276897232

                # <Value 'sticky' (173:51)> -> __condition
                __token = 6871
                try:
                    __zt_tmp = __attrs_140478190700240
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140478276908560('path', 'sticky', econtext=econtext)(_static_140478276908272(econtext, __zt_tmp))
                if __condition:
                    __append('\n                              ')

                    # <Static value=<ast.Dict object at 0x7fc3a5cb09d0> name=None at 7fc3a5cb0d00> -> __attrs_140478190702160
                    __attrs_140478190702160 = _static_140478276897232

                    # <Symbol value=<DEFAULT> at 7fc3a5c49720> -> __default_140478190701968
                    __default_140478190701968 = _DEFAULT_MARKER

                    # <Value 'entry/title' (174:49)> -> __cache_140478190701488
                    __token = 6929
                    try:
                        __zt_tmp = __attrs_140478190702160
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140478190701488 = _static_140478276908560('path', 'entry/title', econtext=econtext)(_static_140478276908272(econtext, __zt_tmp))

                    # <BinOp left=<Value 'entry/title' (174:49)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fc3a5c49720> at 7fc3a0a7cc70> -> __condition
                    __expression = __cache_140478190701488

                    # <Symbol value=<DEFAULT> at 7fc3a5c49720> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span></span>')
                    else:
                        __content = __cache_140478190701488
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('\n                            ')
                __append('\n                            ')

                # <Static value=<ast.Dict object at 0x7fc3a5cb09d0> name=None at 7fc3a5cb0d00> -> __attrs_140478190702448
                __attrs_140478190702448 = _static_140478276897232

                # <Value 'not:sticky' (176:54)> -> __condition
                __token = 7046
                try:
                    __zt_tmp = __attrs_140478190702448
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140478276908560('not', 'sticky', econtext=econtext)(_static_140478276908272(econtext, __zt_tmp))
                if __condition:
                    __append('\n                              ')

                    # <Static value=<ast.Dict object at 0x7fc3a5cb09d0> name=None at 7fc3a5cb0d00> -> __attrs_140478190704272
                    __attrs_140478190704272 = _static_140478276897232

                    # <Symbol value=<DEFAULT> at 7fc3a5c49720> -> __default_140478190704080
                    __default_140478190704080 = _DEFAULT_MARKER

                    # <Value 'entry/title' (177:49)> -> __cache_140478190703600
                    __token = 7108
                    try:
                        __zt_tmp = __attrs_140478190704272
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140478190703600 = _static_140478276908560('path', 'entry/title', econtext=econtext)(_static_140478276908272(econtext, __zt_tmp))

                    # <BinOp left=<Value 'entry/title' (177:49)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fc3a5c49720> at 7fc3a0a7d4b0> -> __condition
                    __expression = __cache_140478190703600

                    # <Symbol value=<DEFAULT> at 7fc3a5c49720> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span></span>')
                    else:
                        __content = __cache_140478190703600
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('\n                              ')

                    # <Static value=<ast.Dict object at 0x7fc3a0a7db40> name=None at 7fc3a0a7db70> -> __attrs_140478190705664
                    __attrs_140478190705664 = _static_140478190705472

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span class="text-muted" condition="entry/id|nothing" >')

                    # <Interpolation value=<Substitution '\n                                                            (${entry/id})\n                              ' (180:31)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fc3a0a7dd50> -> __content_140478360922672
                    __token = 7341
                    __token = 7344
                    try:
                        __zt_tmp = __attrs_140478190705664
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __content_140478360922672 = _static_140478276908560('path', 'entry/id', econtext=econtext)(_static_140478276908272(econtext, __zt_tmp))
                    __content_140478360922672 = __quote(__content_140478360922672, '\x00', '&#0;', None, None)
                    __content_140478360922672 = ('%s%s%s' % ('\n                                                            (', (__content_140478360922672 if (__content_140478360922672 is not None) else ''), ')\n                              ', ))
                    if (__content_140478360922672 is None):
                        pass
                    else:
                        if (__content_140478360922672 is None):
                            __content_140478360922672 = None
                        else:
                            __tt = type(__content_140478360922672)
                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                __content_140478360922672 = str(__content_140478360922672)
                            else:
                                if (__tt is bytes):
                                    __content_140478360922672 = decode(__content_140478360922672)
                                else:
                                    if (__tt is not str):
                                        try:
                                            __content_140478360922672 = __content_140478360922672.__html__
                                        except get('AttributeError', AttributeError):
                                            __converted = convert(__content_140478360922672)
                                            __content_140478360922672 = (str(__content_140478360922672) if (__content_140478360922672 is __converted) else __converted)
                                        else:
                                            __content_140478360922672 = __content_140478360922672()
                    if (__content_140478360922672 is not None):
                        __append(__content_140478360922672)
                    __append('</span>\n                            ')
                __append('\n                          ')
                __condition = __cache_140478190698896
                if __condition:
                    __append('</a>')
                __append('\n\n                          ')

                # <Static value=<ast.Dict object at 0x7fc3a0a7df90> name=None at 7fc3a0a7dfc0> -> __attrs_140478190707056
                __attrs_140478190707056 = _static_140478190706576

                # <Value 'not:disabled' (188:48)> -> __condition
                __token = 7624
                try:
                    __zt_tmp = __attrs_140478190707056
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140478276908560('not', 'disabled', econtext=econtext)(_static_140478276908272(econtext, __zt_tmp))
                if __condition:

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input name="entries.id:records" type="hidden"')

                    # <Symbol value=<DEFAULT> at 7fc3a5c49720> -> __default_140478190700000
                    __default_140478190700000 = _DEFAULT_MARKER

                    # <Substitution 'entry/id' (190:41)> -> __attr_value
                    __token = 7729
                    try:
                        __zt_tmp = __attrs_140478190707056
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_140478276908560('path', 'entry/id', econtext=econtext)(_static_140478276908272(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append(' />')
                __append('\n                          ')

                # <Static value=<ast.Dict object at 0x7fc3a0a7e6e0> name=None at 7fc3a0a7e710> -> __attrs_140478190708928
                __attrs_140478190708928 = _static_140478190708448

                # <Value 'not:disabled' (195:48)> -> __condition
                __token = 7959
                try:
                    __zt_tmp = __attrs_140478190708928
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140478276908560('not', 'disabled', econtext=econtext)(_static_140478276908272(econtext, __zt_tmp))
                if __condition:

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input name="entries.type:records" type="hidden"')

                    # <Symbol value=<DEFAULT> at 7fc3a5c49720> -> __default_140478190707776
                    __default_140478190707776 = _DEFAULT_MARKER

                    # <Substitution 'entry/type' (197:41)> -> __attr_value
                    __token = 8064
                    try:
                        __zt_tmp = __attrs_140478190708928
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_140478276908560('path', 'entry/type', econtext=econtext)(_static_140478276908272(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append(' />')
                __append('\n                        </td>\n                        ')

                # <Static value=<ast.Dict object at 0x7fc3a0a7ebf0> name=None at 7fc3a0a7ec20> -> __attrs_140478190710176
                __attrs_140478190710176 = _static_140478190709744
                __backup_role_140478190675824 = get('role', __marker)

                # <Value 'available_roles' (202:45)> -> __iterator
                __token = 8267
                try:
                    __zt_tmp = __attrs_140478190710176
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140478276908560('path', 'available_roles', econtext=econtext)(_static_140478276908272(econtext, __zt_tmp))
                (__iterator, ____index_140478190710416, ) = getname('repeat')('role', __iterator)
                econtext['role'] = None
                for __item in __iterator:
                    econtext['role'] = __item

                    # <td ... (0:0)
                    # --------------------------------------------------------
                    __append('<td class="listingCheckbox" >\n                          ')

                    # <Static value=<ast.Dict object at 0x7fc3a5cb09d0> name=None at 7fc3a5cb0d00> -> __attrs_140478190711328
                    __attrs_140478190711328 = _static_140478276897232
                    __backup_entry_role_140478190676832 = get('entry_role', __marker)

                    # <Value "python:entry['roles'][role['id']]" (205:50)> -> __value
                    __token = 8406
                    try:
                        __zt_tmp = __attrs_140478190711328
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140478276908560('python', "entry['roles'][role['id']]", econtext=econtext)(_static_140478276908272(econtext, __zt_tmp))
                    econtext['entry_role'] = __value
                    __append('\n                            ')

                    # <Static value=<ast.Dict object at 0x7fc3a5cb09d0> name=None at 7fc3a5cb0d00> -> __attrs_140478190712960
                    __attrs_140478190712960 = _static_140478276897232

                    # <Value "python:entry_role == 'global'" (207:53)> -> __condition
                    __token = 8534
                    try:
                        __zt_tmp = __attrs_140478190712960
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140478276908560('python', "entry_role == 'global'", econtext=econtext)(_static_140478276908272(econtext, __zt_tmp))
                    if __condition:

                        # <Symbol value=<DEFAULT> at 7fc3a5c49720> -> __default_140478190712768
                        __default_140478190712768 = _DEFAULT_MARKER

                        # <Value "python:icons.tag('globe', tag_alt='Global')" (208:61)> -> __cache_140478190712240
                        __token = 8626
                        try:
                            __zt_tmp = __attrs_140478190712960
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140478190712240 = _static_140478276908560('python', "icons.tag('globe', tag_alt='Global')", econtext=econtext)(_static_140478276908272(econtext, __zt_tmp))

                        # <BinOp left=<Value "python:icons.tag('globe', tag_alt='Global')" (208:61)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fc3a5c49720> at 7fc3a0a7f6a0> -> __condition
                        __expression = __cache_140478190712240

                        # <Symbol value=<DEFAULT> at 7fc3a5c49720> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140478190712240
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                    __append('\n                            ')

                    # <Static value=<ast.Dict object at 0x7fc3a5cb09d0> name=None at 7fc3a5cb0d00> -> __attrs_140478190714256
                    __attrs_140478190714256 = _static_140478276897232

                    # <Value "python:entry_role == 'acquired'" (210:53)> -> __condition
                    __token = 8755
                    try:
                        __zt_tmp = __attrs_140478190714256
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140478276908560('python', "entry_role == 'acquired'", econtext=econtext)(_static_140478276908272(econtext, __zt_tmp))
                    if __condition:

                        # <Symbol value=<DEFAULT> at 7fc3a5c49720> -> __default_140478190714064
                        __default_140478190714064 = _DEFAULT_MARKER

                        # <Value "python:icons.tag('diagram-2', tag_alt='Inherited')" (211:61)> -> __cache_140478190713584
                        __token = 8849
                        try:
                            __zt_tmp = __attrs_140478190714256
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140478190713584 = _static_140478276908560('python', "icons.tag('diagram-2', tag_alt='Inherited')", econtext=econtext)(_static_140478276908272(econtext, __zt_tmp))

                        # <BinOp left=<Value "python:icons.tag('diagram-2', tag_alt='Inherited')" (211:61)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fc3a5c49720> at 7fc3a0a7fbb0> -> __condition
                        __expression = __cache_140478190713584

                        # <Symbol value=<DEFAULT> at 7fc3a5c49720> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140478190713584
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                    __append('\n                            ')

                    # <Static value=<ast.Dict object at 0x7fc3a5cb09d0> name=None at 7fc3a5cb0d00> -> __attrs_140478190731424
                    __attrs_140478190731424 = _static_140478276897232

                    # <Value 'python:entry_role in (True, False)' (213:50)> -> __condition
                    __token = 8982
                    try:
                        __zt_tmp = __attrs_140478190731424
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140478276908560('python', 'entry_role in (True, False)', econtext=econtext)(_static_140478276908272(econtext, __zt_tmp))
                    if __condition:
                        __append('\n                              ')

                        # <Static value=<ast.Dict object at 0x7fc3a0a84b20> name=None at 7fc3a0a84b50> -> __attrs_140478190734880
                        __attrs_140478190734880 = _static_140478190734112

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input class="noborder" type="checkbox" value="True"')

                        # <Symbol value=<DEFAULT> at 7fc3a5c49720> -> __default_140478190733008
                        __default_140478190733008 = _DEFAULT_MARKER

                        # <Substitution 'string:entries.role_${role/id}:records' (218:44)> -> __attr_name
                        __token = 9274
                        try:
                            __zt_tmp = __attrs_140478190734880
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_name = _static_140478276908560('string', 'entries.role_${role/id}:records', econtext=econtext)(_static_140478276908272(econtext, __zt_tmp))
                        __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_name is not None):
                            __append((' name="%s"' % __attr_name))

                        # <Symbol value=<DEFAULT> at 7fc3a5c49720> -> __default_140478190732528
                        __default_140478190732528 = _DEFAULT_MARKER

                        # <Boolean "python:entry_role and 'checked' or None" (219:46)> -> __attr_checked
                        __token = 9360
                        try:
                            __zt_tmp = __attrs_140478190734880
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_checked = _static_140478276908560('python', "entry_role and 'checked' or None", econtext=econtext)(_static_140478276908272(econtext, __zt_tmp))
                        if (__attr_checked is _DEFAULT_MARKER):
                            __attr_checked = None
                        else:
                            if __attr_checked:
                                __attr_checked = 'checked'
                            else:
                                __attr_checked = None
                        if (__attr_checked is not None):
                            __append((' checked="%s"' % __attr_checked))

                        # <Symbol value=<DEFAULT> at 7fc3a5c49720> -> __default_140478190734448
                        __default_140478190734448 = _DEFAULT_MARKER

                        # <Boolean 'python:disabled or None' (220:46)> -> __attr_disabled
                        __token = 9448
                        try:
                            __zt_tmp = __attrs_140478190734880
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_disabled = _static_140478276908560('python', 'disabled or None', econtext=econtext)(_static_140478276908272(econtext, __zt_tmp))
                        if (__attr_disabled is _DEFAULT_MARKER):
                            __attr_disabled = None
                        else:
                            if __attr_disabled:
                                __attr_disabled = 'disabled'
                            else:
                                __attr_disabled = None
                        if (__attr_disabled is not None):
                            __append((' disabled="%s"' % __attr_disabled))
                        __append(' />\n                            ')
                    __append('\n                          ')
                    if (__backup_entry_role_140478190676832 is __marker):
                        del econtext['entry_role']
                    else:
                        econtext['entry_role'] = __backup_entry_role_140478190676832
                    __append('\n                        </td>')
                    ____index_140478190710416 -= 1
                    if (____index_140478190710416 > 0):
                        __append('\n                        ')
                if (__backup_role_140478190675824 is __marker):
                    del econtext['role']
                else:
                    econtext['role'] = __backup_role_140478190675824
                __append('\n                      </tr>')
                if (__backup_sticky_140478190671792 is __marker):
                    del econtext['sticky']
                else:
                    econtext['sticky'] = __backup_sticky_140478190671792
                if (__backup_oddrow_140478190669968 is __marker):
                    del econtext['oddrow']
                else:
                    econtext['oddrow'] = __backup_oddrow_140478190669968
                if (__backup_disabled_140478190668480 is __marker):
                    del econtext['disabled']
                else:
                    econtext['disabled'] = __backup_disabled_140478190668480
                if (__backup_is_group_140478190667088 is __marker):
                    del econtext['is_group']
                else:
                    econtext['is_group'] = __backup_is_group_140478190667088
                __append('\n                    ')
                ____index_140478190674000 -= 1
                if (____index_140478190674000 > 0):
                    __append('')
            if (__backup_entry_140478190664768 is __marker):
                del econtext['entry']
            else:
                econtext['entry'] = __backup_entry_140478190664768
            __append('\n                  </tbody>')
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

            # <Static value=<ast.Dict object at 0x7fc3a5cb09d0> name=None at 7fc3a5cb0d00> -> __attrs_140478228936496
            __attrs_140478228936496 = _static_140478276897232
            __previous_i18n_domain_140478191510304 = __i18n_domain
            __i18n_domain = 'plone'
            __backup_macroname_140478262251136 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7fc3a0b556c0> name=None at 7fc3a0b54be0> -> __value
            __value = _static_140478191589056
            econtext['macroname'] = __value

            def __fill_body(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7fc3a5cb09d0> name=None at 7fc3a5cb0d00> -> __attrs_140478190302160
                __attrs_140478190302160 = _static_140478276897232
                __backup_context_state_140478191509152 = get('context_state', __marker)

                # <Value 'context/@@plone_context_state' (15:32)> -> __value
                __token = 292
                try:
                    __zt_tmp = __attrs_140478190302160
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140478276908560('path', 'context/@@plone_context_state', econtext=econtext)(_static_140478276908272(econtext, __zt_tmp))
                econtext['context_state'] = __value
                __backup_portal_state_140478191510160 = get('portal_state', __marker)

                # <Value 'context/@@plone_portal_state' (16:30)> -> __value
                __token = 353
                try:
                    __zt_tmp = __attrs_140478190302160
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140478276908560('path', 'context/@@plone_portal_state', econtext=econtext)(_static_140478276908272(econtext, __zt_tmp))
                econtext['portal_state'] = __value
                __backup_portal_140478190300624 = get('portal', __marker)

                # <Value 'portal_state/portal' (17:23)> -> __value
                __token = 407
                try:
                    __zt_tmp = __attrs_140478190302160
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140478276908560('path', 'portal_state/portal', econtext=econtext)(_static_140478276908272(econtext, __zt_tmp))
                econtext['portal'] = __value
                __backup_portal_url_140478190302064 = get('portal_url', __marker)

                # <Value 'portal_state/portal_url' (18:26)> -> __value
                __token = 456
                try:
                    __zt_tmp = __attrs_140478190302160
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140478276908560('path', 'portal_state/portal_url', econtext=econtext)(_static_140478276908272(econtext, __zt_tmp))
                econtext['portal_url'] = __value
                __backup_checkPermission_140478190302208 = get('checkPermission', __marker)

                # <Value 'nocall:context/portal_membership/checkPermission' (19:30)> -> __value
                __token = 514
                try:
                    __zt_tmp = __attrs_140478190302160
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140478276908560('nocall', 'context/portal_membership/checkPermission', econtext=econtext)(_static_140478276908272(econtext, __zt_tmp))
                econtext['checkPermission'] = __value
                __backup_can_view_groups_140478190302256 = get('can_view_groups', __marker)

                # <Value "python:checkPermission('Plone Site Setup: Users and Groups', portal)" (20:29)> -> __value
                __token = 597
                try:
                    __zt_tmp = __attrs_140478190302160
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140478276908560('python', "checkPermission('Plone Site Setup: Users and Groups', portal)", econtext=econtext)(_static_140478276908272(econtext, __zt_tmp))
                econtext['can_view_groups'] = __value
                __append('\n\n      ')

                # <Static value=<ast.Dict object at 0x7fc3a0a1bd60> name=None at 7fc3a0a1bd90> -> __attrs_140478190304992
                __attrs_140478190304992 = _static_140478190304608

                # <article ... (0:0)
                # --------------------------------------------------------
                __append('<article id="content">\n        ')

                # <Static value=<ast.Dict object at 0x7fc3a5cb09d0> name=None at 7fc3a5cb0d00> -> __attrs_140478190617360
                __attrs_140478190617360 = _static_140478276897232

                # <header ... (0:0)
                # --------------------------------------------------------
                __append('<header>\n          ')

                # <Static value=<ast.Dict object at 0x7fc3a0a68910> name=None at 7fc3a0a68580> -> __attrs_140478190618992
                __attrs_140478190618992 = _static_140478190618896

                # <Value 'context_state/is_default_page' (28:30)> -> __condition
                __token = 841
                try:
                    __zt_tmp = __attrs_140478190618992
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140478276908560('path', 'context_state/is_default_page', econtext=econtext)(_static_140478276908272(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="alert alert-info" role="alert" >\n            ')

                    # <Static value=<ast.Dict object at 0x7fc3a5cb09d0> name=None at 7fc3a5cb0d00> -> __attrs_140478190620336
                    __attrs_140478190620336 = _static_140478276897232

                    # <strong ... (0:0)
                    # --------------------------------------------------------
                    __append('<strong>')
                    __stream_140478190619856 = []
                    __append_140478190619856 = __stream_140478190619856.append
                    __append_140478190619856('\n                        Info\n            ')
                    __msgid_140478190619856 = __re_whitespace(''.join(__stream_140478190619856)).strip()
                    if __msgid_140478190619856:
                        __append(translate(__msgid_140478190619856, mapping=None, default=__msgid_140478190619856, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</strong>\n            ')

                    # <Static value=<ast.Dict object at 0x7fc3a5cb09d0> name=None at 7fc3a5cb0d00> -> __attrs_140478190621296
                    __attrs_140478190621296 = _static_140478276897232
                    __stream_140478192216416_go_here = ''
                    __stream_140478190620912 = []
                    __append_140478190620912 = __stream_140478190620912.append
                    __append_140478190620912('\n                        You are adjusting the sharing privileges for a default view in a container.\n                        To adjust them for the entire container,\n              ')
                    __stream_140478192216416_go_here = []
                    __append_140478192216416_go_here = __stream_140478192216416_go_here.append

                    # <Static value=<ast.Dict object at 0x7fc3a0a69870> name=None at 7fc3a0a698a0> -> __attrs_140478190623312
                    __attrs_140478190623312 = _static_140478190622832
                    __backup_folder_140478190619184 = get('folder', __marker)

                    # <Value 'context_state/folder' (40:26)> -> __value
                    __token = 1345
                    try:
                        __zt_tmp = __attrs_140478190623312
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140478276908560('path', 'context_state/folder', econtext=econtext)(_static_140478276908272(econtext, __zt_tmp))
                    econtext['folder'] = __value

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append_140478192216416_go_here('<a class="alert-link"')

                    # <Symbol value=<DEFAULT> at 7fc3a5c49720> -> __default_140478190622304
                    __default_140478190622304 = _DEFAULT_MARKER

                    # <Substitution 'string:${folder/absolute_url}/sharing' (43:24)> -> __attr_href
                    __token = 1444
                    try:
                        __zt_tmp = __attrs_140478190623312
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140478276908560('string', '${folder/absolute_url}/sharing', econtext=econtext)(_static_140478276908272(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append_140478192216416_go_here((' href="%s"' % __attr_href))
                    __append_140478192216416_go_here(' >')
                    __stream_140478190621872 = []
                    __append_140478190621872 = __stream_140478190621872.append
                    __append_140478190621872('go here')
                    __msgid_140478190621872 = __re_whitespace(''.join(__stream_140478190621872)).strip()
                    if 'help_sharing_go_here':
                        __append_140478192216416_go_here(translate('help_sharing_go_here', mapping=None, default=__msgid_140478190621872, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append_140478192216416_go_here('</a>')
                    if (__backup_folder_140478190619184 is __marker):
                        del econtext['folder']
                    else:
                        econtext['folder'] = __backup_folder_140478190619184
                    __append_140478190620912('${go_here}')
                    __stream_140478192216416_go_here = ''.join(__stream_140478192216416_go_here)
                    __append_140478190620912('.\n            ')
                    __msgid_140478190620912 = __re_whitespace(''.join(__stream_140478190620912)).strip()
                    if 'help_sharing_page_default_page':
                        __append(translate('help_sharing_page_default_page', mapping={'go_here': __stream_140478192216416_go_here, }, default=__msgid_140478190620912, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('\n          </div>')
                __append('\n\n          ')

                # <Static value=<ast.Dict object at 0x7fc3a0a69d80> name=None at 7fc3a0a69180> -> __attrs_140478190624464
                __attrs_140478190624464 = _static_140478190624128

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append('<h1 class="documentFirstHeading" >')
                __stream_140478191976736_folder = ''
                __stream_140478190621104 = []
                __append_140478190621104 = __stream_140478190621104.append
                __append_140478190621104('\n                    Sharing for\n            ')
                __stream_140478191976736_folder = []
                __append_140478191976736_folder = __stream_140478191976736_folder.append

                # <Static value=<ast.Dict object at 0x7fc3a5cb09d0> name=None at 7fc3a5cb0d00> -> __attrs_140478190626144
                __attrs_140478190626144 = _static_140478276897232

                # <q ... (0:0)
                # --------------------------------------------------------
                __append_140478191976736_folder('<q >')

                # <Symbol value=<DEFAULT> at 7fc3a5c49720> -> __default_140478190625568
                __default_140478190625568 = _DEFAULT_MARKER

                # <Value 'context/Title' (55:28)> -> __cache_140478190625088
                __token = 1840
                try:
                    __zt_tmp = __attrs_140478190626144
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140478190625088 = _static_140478276908560('path', 'context/Title', econtext=econtext)(_static_140478276908272(econtext, __zt_tmp))

                # <BinOp left=<Value 'context/Title' (55:28)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fc3a5c49720> at 7fc3a0a6a200> -> __condition
                __expression = __cache_140478190625088

                # <Symbol value=<DEFAULT> at 7fc3a5c49720> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append_140478191976736_folder('title')
                else:
                    __content = __cache_140478190625088
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append_140478191976736_folder(__content)
                __append_140478191976736_folder('</q>')
                __append_140478190621104('${folder}')
                __stream_140478191976736_folder = ''.join(__stream_140478191976736_folder)
                __append_140478190621104('\n          ')
                __msgid_140478190621104 = __re_whitespace(''.join(__stream_140478190621104)).strip()
                if 'heading_currently_assigned_shares':
                    __append(translate('heading_currently_assigned_shares', mapping={'folder': __stream_140478191976736_folder, }, default=__msgid_140478190621104, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</h1>\n\n          ')

                # <Static value=<ast.Dict object at 0x7fc3a0a6a950> name=None at 7fc3a0a6a7d0> -> __attrs_140478190627488
                __attrs_140478190627488 = _static_140478190627152

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="documentDescription" >')
                __stream_140478190626624 = []
                __append_140478190626624 = __stream_140478190626624.append
                __append_140478190626624('\n                    You can control who can view and edit your item using the list below.\n          ')
                __msgid_140478190626624 = __re_whitespace(''.join(__stream_140478190626624)).strip()
                if 'description_sharing_control':
                    __append(translate('description_sharing_control', mapping=None, default=__msgid_140478190626624, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</div>\n\n          ')

                # <Static value=<ast.Dict object at 0x7fc3a5cb09d0> name=None at 7fc3a5cb0d00> -> __attrs_140478190629072
                __attrs_140478190629072 = _static_140478276897232

                # <Value 'not:ajax_load' (66:30)> -> __condition
                __token = 2182
                try:
                    __zt_tmp = __attrs_140478190629072
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140478276908560('not', 'ajax_load', econtext=econtext)(_static_140478276908272(econtext, __zt_tmp))
                if __condition:

                    # <Symbol value=<DEFAULT> at 7fc3a5c49720> -> __default_140478190628880
                    __default_140478190628880 = _DEFAULT_MARKER

                    # <Value 'provider:plone.abovecontentbody' (67:38)> -> __cache_140478190628400
                    __token = 2235
                    try:
                        __zt_tmp = __attrs_140478190629072
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140478190628400 = _static_140478276908560('provider', 'plone.abovecontentbody', econtext=econtext)(_static_140478276908272(econtext, __zt_tmp))

                    # <BinOp left=<Value 'provider:plone.abovecontentbody' (67:38)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fc3a5c49720> at 7fc3a0a6aef0> -> __condition
                    __expression = __cache_140478190628400

                    # <Symbol value=<DEFAULT> at 7fc3a5c49720> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append('<div ></div>')
                    else:
                        __content = __cache_140478190628400
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                __append('\n\n          ')

                # <Static value=<ast.Dict object at 0x7fc3a0a6b490> name=None at 7fc3a0a6b4c0> -> __attrs_140478190630416
                __attrs_140478190630416 = _static_140478190630032

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div id="content-core">\n            ')

                # <Static value=<ast.Dict object at 0x7fc3a0a6bbb0> name=None at 7fc3a0a6bbe0> -> __attrs_140478190632480
                __attrs_140478190632480 = _static_140478190631856

                # <form ... (0:0)
                # --------------------------------------------------------
                __append('<form class="form-inline pb-4 pt-3" method="post"')

                # <Symbol value=<DEFAULT> at 7fc3a5c49720> -> __default_140478190630992
                __default_140478190630992 = _DEFAULT_MARKER

                # <Substitution 'string:${context/absolute_url}/@@sharing' (74:27)> -> __attr_action
                __token = 2463
                try:
                    __zt_tmp = __attrs_140478190632480
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_action = _static_140478276908560('string', '${context/absolute_url}/@@sharing', econtext=econtext)(_static_140478276908272(econtext, __zt_tmp))
                __attr_action = __quote(__attr_action, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_action is not None):
                    __append((' action="%s"' % __attr_action))
                __append(' >\n\n              ')

                # <Static value=<ast.Dict object at 0x7fc3a0a703d0> name=None at 7fc3a0a70400> -> __attrs_140478190650656
                __attrs_140478190650656 = _static_140478190650320

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input name="form.submitted:boolean" type="hidden" value="True" />\n\n              ')

                # <Static value=<ast.Dict object at 0x7fc3a0a70820> name=None at 7fc3a0a70850> -> __attrs_140478190651808
                __attrs_140478190651808 = _static_140478190651424

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="mb-3">\n                ')

                # <Static value=<ast.Dict object at 0x7fc3a0a719c0> name=None at 7fc3a0a719f0> -> __attrs_140478190652960
                __attrs_140478190652960 = _static_140478190655936

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input class="form-control" id="sharing-user-group-search" name="search_term"')

                # <Symbol value=<DEFAULT> at 7fc3a5c49720> -> __default_140478190654928
                __default_140478190654928 = _DEFAULT_MARKER

                # <Translate msgid=None node=<ast.Constant object at 0x7fc3a0a713f0> at 7fc3a0a71660> -> __attr_placeholder
                __attr_placeholder = 'Search for user or group'
                __attr_placeholder = translate(__attr_placeholder, default=__attr_placeholder, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                if (__attr_placeholder is not None):
                    __append((' placeholder="%s"' % __attr_placeholder))
                __append(' size="30"')

                # <Symbol value=<DEFAULT> at 7fc3a5c49720> -> __default_140478190654064
                __default_140478190654064 = _DEFAULT_MARKER

                # <Translate msgid=None node=<ast.Constant object at 0x7fc3a0a71450> at 7fc3a0a71420> -> __attr_title
                __attr_title = 'Search for user or group'
                __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                if (__attr_title is not None):
                    __append((' title="%s"' % __attr_title))
                __append(' type="text"')

                # <Symbol value=<DEFAULT> at 7fc3a5c49720> -> __default_140478190653536
                __default_140478190653536 = _DEFAULT_MARKER

                # <Interpolation value=<Substitution '${request/search_term|nothing}' (91:30)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fc3a0a710f0> -> __attr_value
                __token = 3067
                __token = 3069
                try:
                    __zt_tmp = __attrs_140478190652960
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_140478276908560('path', 'request/search_term|nothing', econtext=econtext)(_static_140478276908272(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                __attr_value = __attr_value
                if (__attr_value is None):
                    pass
                else:
                    if (__attr_value is _DEFAULT_MARKER):
                        __attr_value = None
                    else:
                        __tt = type(__attr_value)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __attr_value = str(__attr_value)
                        else:
                            if (__tt is bytes):
                                __attr_value = decode(__attr_value)
                            else:
                                if (__tt is not str):
                                    try:
                                        __attr_value = __attr_value.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__attr_value)
                                        __attr_value = (str(__attr_value) if (__attr_value is __converted) else __converted)
                                    else:
                                        __attr_value = __attr_value()
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append(' />\n                ')

                # <Static value=<ast.Dict object at 0x7fc3a0a720b0> name=None at 7fc3a0a720e0> -> __attrs_140478190658144
                __attrs_140478190658144 = _static_140478190657712

                # <button ... (0:0)
                # --------------------------------------------------------
                __append('<button class="btn btn-primary" id="sharing-search-button" name="form.button.Search" type="submit"')

                # <Symbol value=<DEFAULT> at 7fc3a5c49720> -> __default_140478190656320
                __default_140478190656320 = _DEFAULT_MARKER

                # <Translate msgid='label_search' node=<ast.Constant object at 0x7fc3a0a71c30> at 7fc3a0a71c00> -> __attr_value
                __attr_value = 'Search'
                __attr_value = translate('label_search', default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append(' >')
                __stream_140478190652432 = []
                __append_140478190652432 = __stream_140478190652432.append
                __append_140478190652432('Search')
                __msgid_140478190652432 = __re_whitespace(''.join(__stream_140478190652432)).strip()
                if 'label_search':
                    __append(translate('label_search', mapping=None, default=__msgid_140478190652432, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</button>\n              </div>\n            </form>\n            ')

                # <Static value=<ast.Dict object at 0x7fc3a0a726b0> name=None at 7fc3a0a726e0> -> __attrs_140478190659632
                __attrs_140478190659632 = _static_140478190659248

                # <form ... (0:0)
                # --------------------------------------------------------
                __append('<form method="post"')

                # <Symbol value=<DEFAULT> at 7fc3a5c49720> -> __default_140478190658720
                __default_140478190658720 = _DEFAULT_MARKER

                # <Substitution 'string:${context/absolute_url}/@@sharing' (106:27)> -> __attr_action
                __token = 3687
                try:
                    __zt_tmp = __attrs_140478190659632
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_action = _static_140478276908560('string', '${context/absolute_url}/@@sharing', econtext=econtext)(_static_140478276908272(econtext, __zt_tmp))
                __attr_action = __quote(__attr_action, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_action is not None):
                    __append((' action="%s"' % __attr_action))
                __append(' >\n\n              ')

                # <Static value=<ast.Dict object at 0x7fc3a0a72da0> name=None at 7fc3a0a72dd0> -> __attrs_140478190661360
                __attrs_140478190661360 = _static_140478190661024

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input name="form.submitted:boolean" type="hidden" value="True" />\n              ')

                # <Static value=<ast.Dict object at 0x7fc3a0a73220> name=None at 7fc3a0a73070> -> __attrs_140478190662512
                __attrs_140478190662512 = _static_140478190662176

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div id="user-group-sharing-container">\n                ')
                __token = None
                render_user_group_sharing(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append('\n              </div>\n\n              ')

                # <Static value=<ast.Dict object at 0x7fc3a0a762c0> name=None at 7fc3a0a75cc0> -> __attrs_140478190711568
                __attrs_140478190711568 = _static_140478190674624

                # <Value 'view/can_edit_inherit' (234:34)> -> __condition
                __token = 9898
                try:
                    __zt_tmp = __attrs_140478190711568
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140478276908560('path', 'view/can_edit_inherit', econtext=econtext)(_static_140478276908272(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="mb-3" id="field-inherit" >\n                ')

                    # <Static value=<ast.Dict object at 0x7fc3a0a85150> name=None at 7fc3a0a85180> -> __attrs_140478190736080
                    __attrs_140478190736080 = _static_140478190735696

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="form-check">\n                  ')

                    # <Static value=<ast.Dict object at 0x7fc3a0a85c00> name=None at 7fc3a0a85c30> -> __attrs_140478190738912
                    __attrs_140478190738912 = _static_140478190738432

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input class="form-check-input single-checkbox-bool-widget bool-field" id="inherit"')

                    # <Symbol value=<DEFAULT> at 7fc3a5c49720> -> __default_140478190737472
                    __default_140478190737472 = _DEFAULT_MARKER

                    # <Boolean "python:view.inherited() and 'checked' or None" (244:35)> -> __attr_checked
                    __token = 10349
                    try:
                        __zt_tmp = __attrs_140478190738912
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_checked = _static_140478276908560('python', "view.inherited() and 'checked' or None", econtext=econtext)(_static_140478276908272(econtext, __zt_tmp))
                    if (__attr_checked is _DEFAULT_MARKER):
                        __attr_checked = 'checked'
                    else:
                        if __attr_checked:
                            __attr_checked = 'checked'
                        else:
                            __attr_checked = None
                    if (__attr_checked is not None):
                        __append((' checked="%s"' % __attr_checked))
                    __append(' name="inherit:boolean" type="checkbox" value="1" />\n                  ')

                    # <Static value=<ast.Dict object at 0x7fc3a0a86350> name=None at 7fc3a0a85fc0> -> __attrs_140478190740400
                    __attrs_140478190740400 = _static_140478190740304

                    # <label ... (0:0)
                    # --------------------------------------------------------
                    __append('<label class="form-check-label" for="inherit" >')
                    __stream_140478190739296 = []
                    __append_140478190739296 = __stream_140478190739296.append
                    __append_140478190739296('\n                                    Inherit permissions from higher levels\n                  ')
                    __msgid_140478190739296 = __re_whitespace(''.join(__stream_140478190739296)).strip()
                    if 'label_inherit_local_roles':
                        __append(translate('label_inherit_local_roles', mapping=None, default=__msgid_140478190739296, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</label>\n                  ')

                    # <Static value=<ast.Dict object at 0x7fc3a0a867a0> name=None at 7fc3a0a86620> -> __attrs_140478190741744
                    __attrs_140478190741744 = _static_140478190741408

                    # <small ... (0:0)
                    # --------------------------------------------------------
                    __append('<small class="form-text text-muted" >')
                    __stream_140478192215968_image_link_icon = ''
                    __stream_140478192215968_image_confirm_icon = ''
                    __stream_140478190740880 = []
                    __append_140478190740880 = __stream_140478190740880.append
                    __append_140478190740880('\n                                    By default, permissions from the container of this item are inherited.\n                                    If you disable this, only the explicitly defined sharing permissions will\n                                    be valid.\n                                    In the overview, the symbol\n                    ')
                    __stream_140478192215968_image_link_icon = []
                    __append_140478192215968_image_link_icon = __stream_140478192215968_image_link_icon.append

                    # <Static value=<ast.Dict object at 0x7fc3a5cb09d0> name=None at 7fc3a5cb0d00> -> __attrs_140478190743184
                    __attrs_140478190743184 = _static_140478276897232

                    # <Symbol value=<DEFAULT> at 7fc3a5c49720> -> __default_140478190742992
                    __default_140478190742992 = _DEFAULT_MARKER

                    # <Value "python:icons.tag('diagram-2', tag_alt='Inherited')" (260:53)> -> __cache_140478190742512
                    __token = 11244
                    try:
                        __zt_tmp = __attrs_140478190743184
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140478190742512 = _static_140478276908560('python', "icons.tag('diagram-2', tag_alt='Inherited')", econtext=econtext)(_static_140478276908272(econtext, __zt_tmp))

                    # <BinOp left=<Value "python:icons.tag('diagram-2', tag_alt='Inherited')" (260:53)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fc3a5c49720> at 7fc3a0a86cb0> -> __condition
                    __expression = __cache_140478190742512

                    # <Symbol value=<DEFAULT> at 7fc3a5c49720> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140478190742512
                        __content = __convert(__content)
                        if (__content is not None):
                            __append_140478192215968_image_link_icon(__content)
                    __append_140478190740880('${image_link_icon}')
                    __stream_140478192215968_image_link_icon = ''.join(__stream_140478192215968_image_link_icon)
                    __append_140478190740880('\n                                    indicates an inherited value. Similarly, the symbol\n                    ')
                    __stream_140478192215968_image_confirm_icon = []
                    __append_140478192215968_image_confirm_icon = __stream_140478192215968_image_confirm_icon.append

                    # <Static value=<ast.Dict object at 0x7fc3a5cb09d0> name=None at 7fc3a5cb0d00> -> __attrs_140478190744384
                    __attrs_140478190744384 = _static_140478276897232

                    # <Symbol value=<DEFAULT> at 7fc3a5c49720> -> __default_140478190744192
                    __default_140478190744192 = _DEFAULT_MARKER

                    # <Value "python:icons.tag('globe', tag_alt='Global')" (264:53)> -> __cache_140478190743664
                    __token = 11518
                    try:
                        __zt_tmp = __attrs_140478190744384
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140478190743664 = _static_140478276908560('python', "icons.tag('globe', tag_alt='Global')", econtext=econtext)(_static_140478276908272(econtext, __zt_tmp))

                    # <BinOp left=<Value "python:icons.tag('globe', tag_alt='Global')" (264:53)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fc3a5c49720> at 7fc3a0a87160> -> __condition
                    __expression = __cache_140478190743664

                    # <Symbol value=<DEFAULT> at 7fc3a5c49720> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140478190743664
                        __content = __convert(__content)
                        if (__content is not None):
                            __append_140478192215968_image_confirm_icon(__content)
                    __append_140478190740880('${image_confirm_icon}')
                    __stream_140478192215968_image_confirm_icon = ''.join(__stream_140478192215968_image_confirm_icon)
                    __append_140478190740880('\n                                    indicates a global role, which is managed by the site administrator.\n                  ')
                    __msgid_140478190740880 = __re_whitespace(''.join(__stream_140478190740880)).strip()
                    if 'help_inherit_local_roles':
                        __append(translate('help_inherit_local_roles', mapping={'image_confirm_icon': __stream_140478192215968_image_confirm_icon, 'image_link_icon': __stream_140478192215968_image_link_icon, }, default=__msgid_140478190740880, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</small>\n                </div>\n              </div>')
                __append('\n              ')

                # <Static value=<ast.Dict object at 0x7fc3a0a87a30> name=None at 7fc3a0a87a60> -> __attrs_140478190744768
                __attrs_140478190744768 = _static_140478190746160

                # <button ... (0:0)
                # --------------------------------------------------------
                __append('<button class="btn btn-primary" id="sharing-save-button" name="form.button.Save" type="submit" >')
                __stream_140478190741840 = []
                __append_140478190741840 = __stream_140478190741840.append
                __append_140478190741840('Save')
                __msgid_140478190741840 = __re_whitespace(''.join(__stream_140478190741840)).strip()
                if 'label_save':
                    __append(translate('label_save', mapping=None, default=__msgid_140478190741840, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</button>\n              ')

                # <Static value=<ast.Dict object at 0x7fc3a0a87eb0> name=None at 7fc3a0a87ee0> -> __attrs_140478190780624
                __attrs_140478190780624 = _static_140478190747312

                # <button ... (0:0)
                # --------------------------------------------------------
                __append('<button class="btn btn-secondary" name="form.button.Cancel" type="submit" >')
                __stream_140478190746448 = []
                __append_140478190746448 = __stream_140478190746448.append
                __append_140478190746448('Cancel')
                __msgid_140478190746448 = __re_whitespace(''.join(__stream_140478190746448)).strip()
                if 'label_cancel':
                    __append(translate('label_cancel', mapping=None, default=__msgid_140478190746448, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</button>\n              ')

                # <Static value=<ast.Dict object at 0x7fc3a5cb09d0> name=None at 7fc3a5cb0d00> -> __attrs_140478190782160
                __attrs_140478190782160 = _static_140478276897232

                # <Symbol value=<DEFAULT> at 7fc3a5c49720> -> __default_140478190781968
                __default_140478190781968 = _DEFAULT_MARKER

                # <Value 'context/@@authenticator/authenticator' (282:44)> -> __cache_140478190781440
                __token = 12336
                try:
                    __zt_tmp = __attrs_140478190782160
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140478190781440 = _static_140478276908560('path', 'context/@@authenticator/authenticator', econtext=econtext)(_static_140478276908272(econtext, __zt_tmp))

                # <BinOp left=<Value 'context/@@authenticator/authenticator' (282:44)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fc3a5c49720> at 7fc3a0a904f0> -> __condition
                __expression = __cache_140478190781440

                # <Symbol value=<DEFAULT> at 7fc3a5c49720> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input />')
                else:
                    __content = __cache_140478190781440
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n            </form>\n          </div>\n        </header>\n      </article>\n    ')
                if (__backup_can_view_groups_140478190302256 is __marker):
                    del econtext['can_view_groups']
                else:
                    econtext['can_view_groups'] = __backup_can_view_groups_140478190302256
                if (__backup_checkPermission_140478190302208 is __marker):
                    del econtext['checkPermission']
                else:
                    econtext['checkPermission'] = __backup_checkPermission_140478190302208
                if (__backup_portal_url_140478190302064 is __marker):
                    del econtext['portal_url']
                else:
                    econtext['portal_url'] = __backup_portal_url_140478190302064
                if (__backup_portal_140478190300624 is __marker):
                    del econtext['portal']
                else:
                    econtext['portal'] = __backup_portal_140478190300624
                if (__backup_portal_state_140478191510160 is __marker):
                    del econtext['portal_state']
                else:
                    econtext['portal_state'] = __backup_portal_state_140478191510160
                if (__backup_context_state_140478191509152 is __marker):
                    del econtext['context_state']
                else:
                    econtext['context_state'] = __backup_context_state_140478191509152
            _slots = econtext['__slot_body'] = _deque((__fill_body, ))

            # <Value 'context/main_template/macros/master' (3:23)> -> __macro
            __token = 82
            try:
                __zt_tmp = __attrs_140478228936496
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140478276908560('path', 'context/main_template/macros/master', econtext=econtext)(_static_140478276908272(econtext, __zt_tmp))
            __token = 82
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140478262251136 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140478262251136
            __i18n_domain = __previous_i18n_domain_140478191510304
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_user_group_sharing': render_user_group_sharing, 'render_user_group_sharing_head': render_user_group_sharing_head, 'render_user_group_sharing_settings': render_user_group_sharing_settings, 'render': render, }