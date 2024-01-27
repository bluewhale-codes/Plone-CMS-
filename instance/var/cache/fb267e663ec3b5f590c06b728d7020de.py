# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/Products/CMFPlone/browser/login/templates/registered_notify_template.pt'

__tokens = {21: ('string:&', 1, 21), 32: (';gt stri', 1, 32), 66: (" member python:options['", 2, 17), 115: ("   reset python:options.get('reset', None) or here.portal_password_reset.requestReset(member", 3, 15), 242: ("from_name python:context.portal_registry['plone.email_f", 4, 24), 346: ('view/encoded_mail_sender', 5, 36), 398: ("python:member.getProperty('email')", 6, 23), 465: ('view/registered_notify_subject', 7, 28), 671: ("python:member.getProperty('fullname')", 14, 26), 763: ('fullname', 15, 52), 875: ('python:member.getUserName()', 18, 57), 990: ("python:view.construct_url(reset['randomstring'])+'?userid='+member.getUserName()", 21, 48), 1162: ("python:\n    context.toLocalizedTime(reset['expires'], long_format=1)", 23, 86), 1376: ('email_from_name', 35, 19)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139764333427296 = __C2ZContextWrapper
_static_139764333427584 = __compile_zt_expr
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

            # <Static value=<ast.Dict object at 0x7f1d6b720f40> name=None at 7f1d6b721270> -> __attrs_139764233264176
            __attrs_139764233264176 = _static_139764333416256
            __backup_lt_139764233262112 = get('lt', __marker)

            # <Value 'string:<' (1:21)> -> __value
            __token = 21
            try:
                __zt_tmp = __attrs_139764233264176
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139764333427584('string', '<', econtext=econtext)(_static_139764333427296(econtext, __zt_tmp))
            econtext['lt'] = __value
            __backup_gt_139764233260816 = get('gt', __marker)

            # <Value 'string:>' (1:32)> -> __value
            __token = 32
            try:
                __zt_tmp = __attrs_139764233264176
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139764333427584('string', '>', econtext=econtext)(_static_139764333427296(econtext, __zt_tmp))
            econtext['gt'] = __value
            __backup_member_139764232966240 = get('member', __marker)

            # <Value "python:options['member']" (2:17)> -> __value
            __token = 66
            try:
                __zt_tmp = __attrs_139764233264176
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139764333427584('python', "options['member']", econtext=econtext)(_static_139764333427296(econtext, __zt_tmp))
            econtext['member'] = __value
            __backup_reset_139764233270320 = get('reset', __marker)

            # <Value "python:options.get('reset', None) or here.portal_password_reset.requestReset(member.getId())" (3:15)> -> __value
            __token = 115
            try:
                __zt_tmp = __attrs_139764233264176
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139764333427584('python', "options.get('reset', None) or here.portal_password_reset.requestReset(member.getId())", econtext=econtext)(_static_139764333427296(econtext, __zt_tmp))
            econtext['reset'] = __value
            __backup_email_from_name_139764233259568 = get('email_from_name', __marker)

            # <Value "python:context.portal_registry['plone.email_from_name']" (4:24)> -> __value
            __token = 242
            try:
                __zt_tmp = __attrs_139764233264176
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139764333427584('python', "context.portal_registry['plone.email_from_name']", econtext=econtext)(_static_139764333427296(econtext, __zt_tmp))
            econtext['email_from_name'] = __value
            __append('From: ')

            # <Static value=<ast.Dict object at 0x7f1d6b720f40> name=None at 7f1d6b721270> -> __attrs_139764243978208
            __attrs_139764243978208 = _static_139764333416256

            # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __default_139764243975040
            __default_139764243975040 = _DEFAULT_MARKER

            # <Value 'view/encoded_mail_sender' (5:36)> -> __cache_139764244952448
            __token = 346
            try:
                __zt_tmp = __attrs_139764243978208
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139764244952448 = _static_139764333427584('path', 'view/encoded_mail_sender', econtext=econtext)(_static_139764333427296(econtext, __zt_tmp))

            # <BinOp left=<Value 'view/encoded_mail_sender' (5:36)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f1d6b6b9c90> at 7f1d662c3a00> -> __condition
            __expression = __cache_139764244952448

            # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span />')
            else:
                __content = __cache_139764244952448
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\nTo: ')

            # <Static value=<ast.Dict object at 0x7f1d6b720f40> name=None at 7f1d6b721270> -> __attrs_139764240985504
            __attrs_139764240985504 = _static_139764333416256

            # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __default_139764243973552
            __default_139764243973552 = _DEFAULT_MARKER

            # <Value "python:member.getProperty('email')" (6:23)> -> __cache_139764243980272
            __token = 398
            try:
                __zt_tmp = __attrs_139764240985504
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139764243980272 = _static_139764333427584('python', "member.getProperty('email')", econtext=econtext)(_static_139764333427296(econtext, __zt_tmp))

            # <BinOp left=<Value "python:member.getProperty('email')" (6:23)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f1d6b6b9c90> at 7f1d661d5a80> -> __condition
            __expression = __cache_139764243980272

            # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span />')
            else:
                __content = __cache_139764243980272
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append('\nSubject: ')

            # <Static value=<ast.Dict object at 0x7f1d6b720f40> name=None at 7f1d6b721270> -> __attrs_139764240979696
            __attrs_139764240979696 = _static_139764333416256

            # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __default_139764240976288
            __default_139764240976288 = _DEFAULT_MARKER

            # <Value 'view/registered_notify_subject' (7:28)> -> __cache_139764240980032
            __token = 465
            try:
                __zt_tmp = __attrs_139764240979696
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139764240980032 = _static_139764333427584('path', 'view/registered_notify_subject', econtext=econtext)(_static_139764333427296(econtext, __zt_tmp))

            # <BinOp left=<Value 'view/registered_notify_subject' (7:28)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f1d6b6b9c90> at 7f1d65ef8130> -> __condition
            __expression = __cache_139764240980032

            # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span />')
            else:
                __content = __cache_139764240980032
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append('\nContent-Type: text/plain\nPrecedence: bulk\n\n')

            # <Static value=<ast.Dict object at 0x7f1d6b720f40> name=None at 7f1d6b721270> -> __attrs_139764240983440
            __attrs_139764240983440 = _static_139764333416256
            __backup_fullname_139764232969360 = get('fullname', __marker)

            # <Value "python:member.getProperty('fullname')" (14:26)> -> __value
            __token = 671
            try:
                __zt_tmp = __attrs_139764240983440
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139764333427584('python', "member.getProperty('fullname')", econtext=econtext)(_static_139764333427296(econtext, __zt_tmp))
            econtext['fullname'] = __value
            __previous_i18n_domain_139764240989536 = __i18n_domain
            __i18n_domain = 'plone'
            __stream_139764244452000_fullname = ''
            __stream_139764244452000_expirationdate = ''
            __stream_139764244452000_set_password = ''
            __stream_139764244452000_member = ''
            __stream_139764240986848 = []
            __append_139764240986848 = __stream_139764240986848.append
            __append_139764240986848('\n    Welcome ')
            __stream_139764244452000_fullname = []
            __append_139764244452000_fullname = __stream_139764244452000_fullname.append

            # <Static value=<ast.Dict object at 0x7f1d6b720f40> name=None at 7f1d6b721270> -> __attrs_139764240986992
            __attrs_139764240986992 = _static_139764333416256

            # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __default_139764240986944
            __default_139764240986944 = _DEFAULT_MARKER

            # <Value 'fullname' (15:52)> -> __cache_139764240980800
            __token = 763
            try:
                __zt_tmp = __attrs_139764240986992
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139764240980800 = _static_139764333427584('path', 'fullname', econtext=econtext)(_static_139764333427296(econtext, __zt_tmp))

            # <BinOp left=<Value 'fullname' (15:52)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f1d6b6b9c90> at 7f1d65efa650> -> __condition
            __expression = __cache_139764240980800

            # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <span ... (0:0)
                # --------------------------------------------------------
                __append_139764244452000_fullname('<span />')
            else:
                __content = __cache_139764240980800
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append_139764244452000_fullname(__content)
            __append_139764240986848('${fullname}')
            __stream_139764244452000_fullname = ''.join(__stream_139764244452000_fullname)
            __append_139764240986848(',\n\n    Your user account has been created.\n  Your username is ')
            __stream_139764244452000_member = []
            __append_139764244452000_member = __stream_139764244452000_member.append

            # <Static value=<ast.Dict object at 0x7f1d6b720f40> name=None at 7f1d6b721270> -> __attrs_139764240984736
            __attrs_139764240984736 = _static_139764333416256

            # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __default_139764240973888
            __default_139764240973888 = _DEFAULT_MARKER

            # <Value 'python:member.getUserName()' (18:57)> -> __cache_139764240978976
            __token = 875
            try:
                __zt_tmp = __attrs_139764240984736
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139764240978976 = _static_139764333427584('python', 'member.getUserName()', econtext=econtext)(_static_139764333427296(econtext, __zt_tmp))

            # <BinOp left=<Value 'python:member.getUserName()' (18:57)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f1d6b6b9c90> at 7f1d65ef8d60> -> __condition
            __expression = __cache_139764240978976

            # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <span ... (0:0)
                # --------------------------------------------------------
                __append_139764244452000_member('<span />')
            else:
                __content = __cache_139764240978976
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append_139764244452000_member(__content)
            __append_139764240986848('${member}')
            __stream_139764244452000_member = ''.join(__stream_139764244452000_member)
            __append_139764240986848('.\n  Please activate it by visiting\n\n    ')
            __stream_139764244452000_set_password = []
            __append_139764244452000_set_password = __stream_139764244452000_set_password.append

            # <Static value=<ast.Dict object at 0x7f1d6b720f40> name=None at 7f1d6b721270> -> __attrs_139764244302768
            __attrs_139764244302768 = _static_139764333416256

            # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __default_139764244315824
            __default_139764244315824 = _DEFAULT_MARKER

            # <Value "python:view.construct_url(reset['randomstring'])+'?userid='+member.getUserName()" (21:48)> -> __cache_139764240984352
            __token = 990
            try:
                __zt_tmp = __attrs_139764244302768
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139764240984352 = _static_139764333427584('python', "view.construct_url(reset['randomstring'])+'?userid='+member.getUserName()", econtext=econtext)(_static_139764333427296(econtext, __zt_tmp))

            # <BinOp left=<Value "python:view.construct_url(reset['randomstring'])+'?userid='+member.getUserName()" (21:48)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f1d6b6b9c90> at 7f1d65ef8670> -> __condition
            __expression = __cache_139764240984352

            # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <span ... (0:0)
                # --------------------------------------------------------
                __append_139764244452000_set_password('<span />')
            else:
                __content = __cache_139764240984352
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append_139764244452000_set_password(__content)
            __append_139764240986848('${set_password}')
            __stream_139764244452000_set_password = ''.join(__stream_139764244452000_set_password)
            __append_139764240986848('\n\n    Please activate your account before ')
            __stream_139764244452000_expirationdate = []
            __append_139764244452000_expirationdate = __stream_139764244452000_expirationdate.append

            # <Static value=<ast.Dict object at 0x7f1d6b720f40> name=None at 7f1d6b721270> -> __attrs_139764244139552
            __attrs_139764244139552 = _static_139764333416256

            # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __default_139764244147712
            __default_139764244147712 = _DEFAULT_MARKER

            # <Value "python:\n    context.toLocalizedTime(reset['expires'], long_format=1)" (23:86)> -> __cache_139764241264896
            __token = 1162
            try:
                __zt_tmp = __attrs_139764244139552
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139764241264896 = _static_139764333427584('python', "\n    context.toLocalizedTime(reset['expires'], long_format=1)", econtext=econtext)(_static_139764333427296(econtext, __zt_tmp))

            # <BinOp left=<Value "python:\n    context.toLocalizedTime(reset['expires'], long_format=1)" (23:86)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f1d6b6b9c90> at 7f1d65f3ecb0> -> __condition
            __expression = __cache_139764241264896

            # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <span ... (0:0)
                # --------------------------------------------------------
                __append_139764244452000_expirationdate('<span />')
            else:
                __content = __cache_139764241264896
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append_139764244452000_expirationdate(__content)
            __append_139764240986848('${expirationdate}')
            __stream_139764244452000_expirationdate = ''.join(__stream_139764244452000_expirationdate)
            __append_139764240986848('\n\n')
            __msgid_139764240986848 = __re_whitespace(''.join(__stream_139764240986848)).strip()
            if 'mailtemplate_registered_user_body':
                __append(translate('mailtemplate_registered_user_body', mapping={'member': __stream_139764244452000_member, 'set_password': __stream_139764244452000_set_password, 'expirationdate': __stream_139764244452000_expirationdate, 'fullname': __stream_139764244452000_fullname, }, default=__msgid_139764240986848, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __i18n_domain = __previous_i18n_domain_139764240989536
            if (__backup_fullname_139764232969360 is __marker):
                del econtext['fullname']
            else:
                econtext['fullname'] = __backup_fullname_139764232969360
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x7f1d6b720f40> name=None at 7f1d6b721270> -> __attrs_139764244139312
            __attrs_139764244139312 = _static_139764333416256
            __previous_i18n_domain_139764244141616 = __i18n_domain
            __i18n_domain = 'plone'
            __stream_139764240986368 = []
            __append_139764240986368 = __stream_139764240986368.append
            __append_139764240986368('\n    With kind regards,\n')
            __msgid_139764240986368 = __re_whitespace(''.join(__stream_139764240986368)).strip()
            if 'greetings':
                __append(translate('greetings', mapping=None, default=__msgid_139764240986368, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __i18n_domain = __previous_i18n_domain_139764244141616
            __append('\n--\n\n')

            # <Static value=<ast.Dict object at 0x7f1d6b720f40> name=None at 7f1d6b721270> -> __attrs_139764244136240
            __attrs_139764244136240 = _static_139764333416256

            # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __default_139764244145984
            __default_139764244145984 = _DEFAULT_MARKER

            # <Value 'email_from_name' (35:19)> -> __cache_139764244140272
            __token = 1376
            try:
                __zt_tmp = __attrs_139764244136240
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139764244140272 = _static_139764333427584('path', 'email_from_name', econtext=econtext)(_static_139764333427296(econtext, __zt_tmp))

            # <BinOp left=<Value 'email_from_name' (35:19)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f1d6b6b9c90> at 7f1d661fd690> -> __condition
            __expression = __cache_139764244140272

            # <Symbol value=<DEFAULT> at 7f1d6b6b9c90> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span />')
            else:
                __content = __cache_139764244140272
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append('\n')
            if (__backup_email_from_name_139764233259568 is __marker):
                del econtext['email_from_name']
            else:
                econtext['email_from_name'] = __backup_email_from_name_139764233259568
            if (__backup_reset_139764233270320 is __marker):
                del econtext['reset']
            else:
                econtext['reset'] = __backup_reset_139764233270320
            if (__backup_member_139764232966240 is __marker):
                del econtext['member']
            else:
                econtext['member'] = __backup_member_139764232966240
            if (__backup_gt_139764233260816 is __marker):
                del econtext['gt']
            else:
                econtext['gt'] = __backup_gt_139764233260816
            if (__backup_lt_139764233262112 is __marker):
                del econtext['lt']
            else:
                econtext['lt'] = __backup_lt_139764233262112
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }