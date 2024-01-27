# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/plone/app/discussion/browser/comments.pt'

__tokens = {60: ('view/can_reply', 2, 36), 108: (' view/is_discussion_allowe', 3, 32), 177: ('d view/anonymous_discussion_allow', 4, 40), 245: ('ed view/edit_comment_allo', 5, 31), 310: ('wed view/delete_own_comment_all', 6, 35), 362: ('Anon view/is_anon', 7, 15), 403: ('eview view/can_', 8, 17), 440: ('eplies python:view.get_replies(can', 9, 14), 500: ('replies python:view.has_replies(ca', 10, 17), 567: ('terImage view/show_commen', 11, 23), 613: ('   errors options/state/getErro', 12, 10), 664: ('     wtool context/@@plone_too', 13, 8), 719: (' auth_token context/@@authenticator/t', 14, 12), 809: ('python:isDiscussionAllowed or has_replies', 16, 26), 963: ('python:isAnon and not isAnonymousDiscussionAllowed', 21, 24), 1071: ('view/login_action', 24, 21), 1476: ('has_replies', 36, 24), 1536: ('replies', 38, 41), 1623: ('reply_dict/comment', 42, 21), 1668: (' reply/getI', 43, 25), 1701: ('h reply_dict/depth|python', 44, 19), 1748: ("th python: depth > 10 and '10' or de", 45, 18), 1816: ('url python:view.get_commenter_home_url(username=reply.author_usern', 46, 27), 1914: ('link python:author_home_url and not i', 47, 26), 1980: ('t_url python:view.get_commenter_portrait(reply.author_use', 48, 22), 2066: ("_state python:wtool.getInfoFor(reply, 'review_state', ", 49, 21), 2144: ('canEdit python:view.can_edi', 50, 15), 2197: ('anDelete python:view.can_dele', 51, 16), 2253: ("olorclass python:lambda x: 'state-private' if x=='rejected' else ('state-internal' if x=='spam' else '", 52, 16), 2410: ("python:canReview or review_state == 'published'", 54, 28), 2510: ("python:'comment level-{depth} {state}'.format(depth= depth, state=colorclass(review_state))", 56, 21), 2620: (' comment_i', 57, 17), 2837: ('showCommenterImage', 65, 32), 2928: ('has_author_link', 68, 32), 3003: ('author_home_url', 70, 24), 3231: (' reply/author_nam', 77, 26), 3191: ('portrait_url', 76, 27), 3413: ('not: has_author_link', 83, 34), 3534: (' reply/author_nam', 86, 24), 3496: ('portrait_url', 85, 25), 3756: ('has_author_link', 95, 32), 3831: ('author_home_url', 97, 24), 3882: ('${reply/author_name}', 99, 15), 3884: ('reply/author_name', 99, 17), 3943: ('not: has_author_link', 101, 35), 3965: ('${reply/author_name}', 101, 57), 3967: ('reply/author_name', 101, 59), 4029: ('not: reply/author_name', 103, 35), 4235: ('python:view.format_time(reply.modification_date)', 110, 34), 4519: ('reply/getText', 123, 41), 4738: ('python:isEditCommentAllowed and canEdit', 129, 34), 4961: ('auth_token', 134, 34), 5035: ('string:${reply/absolute_url}/@@edit-comment?_authenticator=${auth_token}', 136, 26), 5393: ('not: auth_token', 145, 37), 5480: ('string:${reply/absolute_url}/@@edit-comment', 147, 31), 5551: (' string:edit-${comment_id', 148, 26), 6112: ('python:canDelete', 165, 34), 6391: ('python:not canDelete and isDeleteOwnCommentAllowed and view.could_delete_own(reply)', 173, 37), 6546: ('string:${reply/absolute_url}/@@delete-own-comment', 175, 31), 6626: (" python:view.can_delete_own(reply) and 'display: inline' or 'display: none", 176, 29), 6728: ('d string:delete-${comment_i', 177, 25), 7421: ('python:canDelete', 194, 37), 7509: ('string:${reply/absolute_url}/@@moderate-delete-comment', 196, 31), 7591: (' string:delete-${comment_id', 197, 26), 8183: ('reply_dict/actions|nothing', 212, 34), 8427: ('canReview', 219, 37), 8479: ('reply_dict/actions|nothing', 220, 41), 8257: ('comment-action action-${action/id}', 215, 29), 8281: ('action/id', 215, 53), 8577: ('string:${reply/absolute_url}/@@transmit-comment', 222, 31), 8654: (' action/i', 223, 28), 8691: ('d string:${action/id}-${comment_i', 224, 25), 8932: ('action/id', 230, 33), 9220: ('${action/title}', 237, 19), 9222: ('action/title', 237, 21), 9507: ('python:isDiscussionAllowed and (isAnon and isAnonymousDiscussionAllowed or userHasReplyPermission)', 248, 33), 9808: ('python: has_replies and not isDiscussionAllowed', 259, 26), 10034: ('python:has_replies and (isAnon and not isAnonymousDiscussionAllowed)', 268, 24), 10185: ('view/login_action', 272, 21), 10646: ('python:isDiscussionAllowed and (isAnon and isAnonymousDiscussionAllowed or userHasReplyPermission)', 286, 24), 10868: ('view/comment_transform_message', 293, 24), 11059: ('view/form/render', 298, 36)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140097338161328 = {'class': 'reply border p-3', 'id': 'commenting', }
_static_140097338159504 = {'class': 'standalone loginbutton btn btn-primary', 'type': 'submit', 'value': 'Log in to add comments', }
_static_140097338157680 = {'class': 'mb-3', 'action': 'view/login_action', }
_static_140097338155712 = {'class': 'reply', }
_static_140097339648720 = {'class': 'discreet', }
_static_140097338153168 = {'class': 'context reply-to-comment-button hide allowMultiSubmit btn btn-primary btn-sm', }
_static_140097338151968 = {'class': 'context btn btn-primary btn-sm', 'name': 'form.button.TransmitComment', 'type': 'submit', }
_static_140097338150240 = {'name': 'workflow_action', 'type': 'hidden', 'value': 'action/id', }
_static_140097338146528 = {'class': 'comment-action action-${action/id}', 'action': '', 'method': 'get', 'name': '', 'id': 'string:${action/id}-${comment_id}', }
_static_140097338144368 = {'class': 'comment-actions actions-workflow d-flex flex-row', }
_static_140097338143696 = {'class': 'destructive btn btn-danger btn-sm', 'name': 'form.button.DeleteComment', 'type': 'submit', 'value': 'Delete', }
_static_140097338140720 = {'class': 'comment-action action-delete', 'action': '', 'method': 'post', 'name': 'delete', 'id': 'string:delete-${comment_id}', }
_static_140097338138320 = {'class': 'destructive btn btn-danger btn-sm', 'name': 'form.button.DeleteComment', 'type': 'submit', 'value': 'Delete', }
_static_140097338134960 = {'class': 'comment-action action-delete', 'action': '', 'method': 'post', 'name': 'delete', 'style': "python:view.can_delete_own(reply) and 'display: inline' or 'display: none'", 'id': 'string:delete-${comment_id}', }
_static_140097338131888 = {'class': 'comment-actions actions-delete', }
_static_140097338113760 = {'class': 'context btn btn-primary btn-sm', 'name': 'form.button.EditComment', 'type': 'submit', 'value': 'Edit', }
_static_140097338111648 = {'class': 'comment-action action-edit', 'action': '', 'method': 'get', 'name': 'edit', 'id': 'string:edit-${comment_id}', }
_static_140097338108720 = {'class': 'pat-plone-modal context comment-action action-edit btn btn-primary btn-sm', 'href': 'string:${reply/absolute_url}/@@edit-comment?_authenticator=${auth_token}', }
_static_140097338106560 = {'class': 'comment-actions actions-edit', }
_static_140097338105072 = {'class': 'd-flex flex-row justify-content-end mb-3', }
_static_140097338102144 = {'class': 'comment-body', }
_static_140097338100896 = {'class': 'text-muted', }
_static_140097337743280 = {'href': '', }
_static_140097337750528 = {'class': 'comment-author', }
_static_140097337752496 = {'alt': '', 'src': 'defaultUser.png', }
_static_140097339914224 = {'alt': '', 'src': 'defaultUser.png', }
_static_140097339911920 = {'href': '', }
_static_140097339912400 = {'class': 'comment-image me-3', }
_static_140097339914320 = {'class': 'd-flex flex-row align-items-center mb-3', }
_static_140097339649488 = {'class': 'comment', 'id': 'comment_id', }
_static_140097342860512 = {'class': 'discussion', }
_static_140097340388688 = {'class': 'btn btn-primary mb-3', 'type': 'submit', 'value': 'Log in to add comments', }
_static_140097340383264 = {'action': 'view/login_action', }
_static_140097339172528 = {'class': 'reply', }
_static_140097339172816 = {'class': 'pat-discussion', }
_static_140097413192176 = __C2ZContextWrapper
_static_140097413192464 = __compile_zt_expr
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

            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097337626576
            __attrs_140097337626576 = _static_140097412968080
            __backup_userHasReplyPermission_140097340068752 = get('userHasReplyPermission', __marker)

            # <Value 'view/can_reply' (2:36)> -> __value
            __token = 60
            try:
                __zt_tmp = __attrs_140097337626576
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('path', 'view/can_reply', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['userHasReplyPermission'] = __value
            __backup_isDiscussionAllowed_140097340066544 = get('isDiscussionAllowed', __marker)

            # <Value 'view/is_discussion_allowed' (3:32)> -> __value
            __token = 108
            try:
                __zt_tmp = __attrs_140097337626576
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('path', 'view/is_discussion_allowed', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['isDiscussionAllowed'] = __value
            __backup_isAnonymousDiscussionAllowed_140097337637952 = get('isAnonymousDiscussionAllowed', __marker)

            # <Value 'view/anonymous_discussion_allowed' (4:40)> -> __value
            __token = 177
            try:
                __zt_tmp = __attrs_140097337626576
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('path', 'view/anonymous_discussion_allowed', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['isAnonymousDiscussionAllowed'] = __value
            __backup_isEditCommentAllowed_140097337627440 = get('isEditCommentAllowed', __marker)

            # <Value 'view/edit_comment_allowed' (5:31)> -> __value
            __token = 245
            try:
                __zt_tmp = __attrs_140097337626576
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('path', 'view/edit_comment_allowed', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['isEditCommentAllowed'] = __value
            __backup_isDeleteOwnCommentAllowed_140097337626864 = get('isDeleteOwnCommentAllowed', __marker)

            # <Value 'view/delete_own_comment_allowed' (6:35)> -> __value
            __token = 310
            try:
                __zt_tmp = __attrs_140097337626576
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('path', 'view/delete_own_comment_allowed', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['isDeleteOwnCommentAllowed'] = __value
            __backup_isAnon_140097337626912 = get('isAnon', __marker)

            # <Value 'view/is_anonymous' (7:15)> -> __value
            __token = 362
            try:
                __zt_tmp = __attrs_140097337626576
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('path', 'view/is_anonymous', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['isAnon'] = __value
            __backup_canReview_140097337630656 = get('canReview', __marker)

            # <Value 'view/can_review' (8:17)> -> __value
            __token = 403
            try:
                __zt_tmp = __attrs_140097337626576
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('path', 'view/can_review', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['canReview'] = __value
            __backup_replies_140097337623168 = get('replies', __marker)

            # <Value 'python:view.get_replies(canReview)' (9:14)> -> __value
            __token = 440
            try:
                __zt_tmp = __attrs_140097337626576
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('python', 'view.get_replies(canReview)', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['replies'] = __value
            __backup_has_replies_140097337636128 = get('has_replies', __marker)

            # <Value 'python:view.has_replies(canReview)' (10:17)> -> __value
            __token = 500
            try:
                __zt_tmp = __attrs_140097337626576
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('python', 'view.has_replies(canReview)', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['has_replies'] = __value
            __backup_showCommenterImage_140097337634880 = get('showCommenterImage', __marker)

            # <Value 'view/show_commenter_image' (11:23)> -> __value
            __token = 567
            try:
                __zt_tmp = __attrs_140097337626576
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('path', 'view/show_commenter_image', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['showCommenterImage'] = __value
            __backup_errors_140097337638240 = get('errors', __marker)

            # <Value 'options/state/getErrors|nothing' (12:10)> -> __value
            __token = 613
            try:
                __zt_tmp = __attrs_140097337626576
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('path', 'options/state/getErrors|nothing', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['errors'] = __value
            __backup_wtool_140097337629216 = get('wtool', __marker)

            # <Value 'context/@@plone_tools/workflow' (13:8)> -> __value
            __token = 664
            try:
                __zt_tmp = __attrs_140097337626576
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('path', 'context/@@plone_tools/workflow', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['wtool'] = __value
            __backup_auth_token_140097337627632 = get('auth_token', __marker)

            # <Value 'context/@@authenticator/token|nothing' (14:12)> -> __value
            __token = 719
            try:
                __zt_tmp = __attrs_140097337626576
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('path', 'context/@@authenticator/token|nothing', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['auth_token'] = __value

            # <Value 'python:isDiscussionAllowed or has_replies' (16:26)> -> __condition
            __token = 809
            try:
                __zt_tmp = __attrs_140097337626576
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140097413192464('python', 'isDiscussionAllowed or has_replies', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_140097339176032 = __i18n_domain
                __i18n_domain = 'plone'
                __append('\n  ')

                # <Static value=<ast.Dict object at 0x7f6af422a7d0> name=None at 7f6af422b8e0> -> __attrs_140097339175888
                __attrs_140097339175888 = _static_140097339172816

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="pat-discussion">\n    ')

                # <Static value=<ast.Dict object at 0x7f6af422a6b0> name=None at 7f6af422ad40> -> __attrs_140097339174736
                __attrs_140097339174736 = _static_140097339172528

                # <Value 'python:isAnon and not isAnonymousDiscussionAllowed' (21:24)> -> __condition
                __token = 963
                try:
                    __zt_tmp = __attrs_140097339174736
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140097413192464('python', 'isAnon and not isAnonymousDiscussionAllowed', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="reply" >\n      ')

                    # <Static value=<ast.Dict object at 0x7f6af4352020> name=None at 7f6af43532b0> -> __attrs_140097340385472
                    __attrs_140097340385472 = _static_140097340383264

                    # <form ... (0:0)
                    # --------------------------------------------------------
                    __append('<form')

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097340387152
                    __default_140097340387152 = _DEFAULT_MARKER

                    # <Substitution 'view/login_action' (24:21)> -> __attr_action
                    __token = 1071
                    try:
                        __zt_tmp = __attrs_140097340385472
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_action = _static_140097413192464('path', 'view/login_action', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    __attr_action = __quote(__attr_action, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_action is not None):
                        __append((' action="%s"' % __attr_action))
                    __append('>\n        ')

                    # <Static value=<ast.Dict object at 0x7f6af4353550> name=None at 7f6af4353370> -> __attrs_140097339546000
                    __attrs_140097339546000 = _static_140097340388688

                    # <button ... (0:0)
                    # --------------------------------------------------------
                    __append('<button class="btn btn-primary mb-3" type="submit"')

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097339545280
                    __default_140097339545280 = _DEFAULT_MARKER

                    # <Translate msgid='label_login_to_add_comments' node=<ast.Constant object at 0x7f6af4284670> at 7f6af42843a0> -> __attr_value
                    __attr_value = 'Log in to add comments'
                    __attr_value = translate('label_login_to_add_comments', default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append(' >')
                    __stream_140097340384848 = []
                    __append_140097340384848 = __stream_140097340384848.append
                    __append_140097340384848('Log in to add comments')
                    __msgid_140097340384848 = __re_whitespace(''.join(__stream_140097340384848)).strip()
                    if 'label_login_to_add_comments':
                        __append(translate('label_login_to_add_comments', mapping=None, default=__msgid_140097340384848, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</button>\n      </form>\n    </div>')
                __append('\n\n    ')

                # <Static value=<ast.Dict object at 0x7f6af45aece0> name=None at 7f6af45ae290> -> __attrs_140097342599472
                __attrs_140097342599472 = _static_140097342860512

                # <Value 'has_replies' (36:24)> -> __condition
                __token = 1476
                try:
                    __zt_tmp = __attrs_140097342599472
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140097413192464('path', 'has_replies', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="discussion" >\n      ')

                    # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097342601392
                    __attrs_140097342601392 = _static_140097412968080
                    __backup_reply_dict_140097339173728 = get('reply_dict', __marker)

                    # <Value 'replies' (38:41)> -> __iterator
                    __token = 1536
                    try:
                        __zt_tmp = __attrs_140097342601392
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_140097413192464('path', 'replies', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    (__iterator, ____index_140097339651552, ) = getname('repeat')('reply_dict', __iterator)
                    econtext['reply_dict'] = None
                    for __item in __iterator:
                        econtext['reply_dict'] = __item
                        __append('\n\n        ')

                        # <Static value=<ast.Dict object at 0x7f6af429edd0> name=None at 7f6af429d7e0> -> __attrs_140097340834816
                        __attrs_140097340834816 = _static_140097339649488
                        __backup_reply_140097365468416 = get('reply', __marker)

                        # <Value 'reply_dict/comment' (42:21)> -> __value
                        __token = 1623
                        try:
                            __zt_tmp = __attrs_140097340834816
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140097413192464('path', 'reply_dict/comment', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        econtext['reply'] = __value
                        __backup_comment_id_140097340390704 = get('comment_id', __marker)

                        # <Value 'reply/getId' (43:25)> -> __value
                        __token = 1668
                        try:
                            __zt_tmp = __attrs_140097340834816
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140097413192464('path', 'reply/getId', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        econtext['comment_id'] = __value
                        __backup_depth_140097339549024 = get('depth', __marker)

                        # <Value 'reply_dict/depth|python:0' (44:19)> -> __value
                        __token = 1701
                        try:
                            __zt_tmp = __attrs_140097340834816
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140097413192464('path', 'reply_dict/depth|python:0', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        econtext['depth'] = __value
                        __backup_depth_140097340835296 = get('depth', __marker)

                        # <Value "python: depth > 10 and '10' or depth" (45:18)> -> __value
                        __token = 1748
                        try:
                            __zt_tmp = __attrs_140097340834816
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140097413192464('python', " depth > 10 and '10' or depth", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        econtext['depth'] = __value
                        __backup_author_home_url_140097340842016 = get('author_home_url', __marker)

                        # <Value 'python:view.get_commenter_home_url(username=reply.author_username)' (46:27)> -> __value
                        __token = 1816
                        try:
                            __zt_tmp = __attrs_140097340834816
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140097413192464('python', 'view.get_commenter_home_url(username=reply.author_username)', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        econtext['author_home_url'] = __value
                        __backup_has_author_link_140097340842640 = get('has_author_link', __marker)

                        # <Value 'python:author_home_url and not isAnon' (47:26)> -> __value
                        __token = 1914
                        try:
                            __zt_tmp = __attrs_140097340834816
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140097413192464('python', 'author_home_url and not isAnon', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        econtext['has_author_link'] = __value
                        __backup_portrait_url_140097340845136 = get('portrait_url', __marker)

                        # <Value 'python:view.get_commenter_portrait(reply.author_username)' (48:22)> -> __value
                        __token = 1980
                        try:
                            __zt_tmp = __attrs_140097340834816
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140097413192464('python', 'view.get_commenter_portrait(reply.author_username)', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        econtext['portrait_url'] = __value
                        __backup_review_state_140097340840288 = get('review_state', __marker)

                        # <Value "python:wtool.getInfoFor(reply, 'review_state', 'none')" (49:21)> -> __value
                        __token = 2066
                        try:
                            __zt_tmp = __attrs_140097340834816
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140097413192464('python', "wtool.getInfoFor(reply, 'review_state', 'none')", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        econtext['review_state'] = __value
                        __backup_canEdit_140097340844656 = get('canEdit', __marker)

                        # <Value 'python:view.can_edit(reply)' (50:15)> -> __value
                        __token = 2144
                        try:
                            __zt_tmp = __attrs_140097340834816
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140097413192464('python', 'view.can_edit(reply)', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        econtext['canEdit'] = __value
                        __backup_canDelete_140097340838128 = get('canDelete', __marker)

                        # <Value 'python:view.can_delete(reply)' (51:16)> -> __value
                        __token = 2197
                        try:
                            __zt_tmp = __attrs_140097340834816
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140097413192464('python', 'view.can_delete(reply)', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        econtext['canDelete'] = __value
                        __backup_colorclass_140097340845808 = get('colorclass', __marker)

                        # <Value "python:lambda x: 'state-private' if x=='rejected' else ('state-internal' if x=='spam' else 'state-'+x)" (52:16)> -> __value
                        __token = 2253
                        try:
                            __zt_tmp = __attrs_140097340834816
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140097413192464('python', "lambda x: 'state-private' if x=='rejected' else ('state-internal' if x=='spam' else 'state-'+x)", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        econtext['colorclass'] = __value

                        # <Value "python:canReview or review_state == 'published'" (54:28)> -> __condition
                        __token = 2410
                        try:
                            __zt_tmp = __attrs_140097340834816
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140097413192464('python', "canReview or review_state == 'published'", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        if __condition:

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append('<div')

                            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097340843024
                            __default_140097340843024 = _DEFAULT_MARKER

                            # <Substitution "python:'comment level-{depth} {state}'.format(depth= depth, state=colorclass(review_state))" (56:21)> -> __attr_class
                            __token = 2510
                            try:
                                __zt_tmp = __attrs_140097340834816
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_class = _static_140097413192464('python', "'comment level-{depth} {state}'.format(depth= depth, state=colorclass(review_state))", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                            __attr_class = __quote(__attr_class, '"', '&quot;', 'comment', _DEFAULT_MARKER)
                            if (__attr_class is not None):
                                __append((' class="%s"' % __attr_class))

                            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097340835680
                            __default_140097340835680 = _DEFAULT_MARKER

                            # <Substitution 'comment_id' (57:17)> -> __attr_id
                            __token = 2620
                            try:
                                __zt_tmp = __attrs_140097340834816
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_id = _static_140097413192464('path', 'comment_id', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                            __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                            if (__attr_id is not None):
                                __append((' id="%s"' % __attr_id))
                            __append(' >\n\n          ')

                            # <Static value=<ast.Dict object at 0x7f6af42df850> name=None at 7f6af42dfdc0> -> __attrs_140097339911152
                            __attrs_140097339911152 = _static_140097339914320

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append('<div class="d-flex flex-row align-items-center mb-3">\n\n            <!-- commenter image -->\n            ')

                            # <Static value=<ast.Dict object at 0x7f6af42df0d0> name=None at 7f6af42df670> -> __attrs_140097339908704
                            __attrs_140097339908704 = _static_140097339912400

                            # <Value 'showCommenterImage' (65:32)> -> __condition
                            __token = 2837
                            try:
                                __zt_tmp = __attrs_140097339908704
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140097413192464('path', 'showCommenterImage', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                            if __condition:

                                # <div ... (0:0)
                                # --------------------------------------------------------
                                __append('<div class="comment-image me-3" >\n              ')

                                # <Static value=<ast.Dict object at 0x7f6af42deef0> name=None at 7f6af42ddcf0> -> __attrs_140097339902992
                                __attrs_140097339902992 = _static_140097339911920

                                # <Value 'has_author_link' (68:32)> -> __condition
                                __token = 2928
                                try:
                                    __zt_tmp = __attrs_140097339902992
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __condition = _static_140097413192464('path', 'has_author_link', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                                if __condition:

                                    # <a ... (0:0)
                                    # --------------------------------------------------------
                                    __append('<a')

                                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097339916240
                                    __default_140097339916240 = _DEFAULT_MARKER

                                    # <Substitution 'author_home_url' (70:24)> -> __attr_href
                                    __token = 3003
                                    try:
                                        __zt_tmp = __attrs_140097339902992
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_href = _static_140097413192464('path', 'author_home_url', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                                    __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                                    if (__attr_href is not None):
                                        __append((' href="%s"' % __attr_href))
                                    __append(' >\n                ')

                                    # <Static value=<ast.Dict object at 0x7f6af42df7f0> name=None at 7f6af42deda0> -> __attrs_140097342750976
                                    __attrs_140097342750976 = _static_140097339914224

                                    # <img ... (0:0)
                                    # --------------------------------------------------------
                                    __append('<img')

                                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097339761296
                                    __default_140097339761296 = _DEFAULT_MARKER

                                    # <Substitution 'reply/author_name' (77:26)> -> __attr_alt
                                    __token = 3231
                                    try:
                                        __zt_tmp = __attrs_140097342750976
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_alt = _static_140097413192464('path', 'reply/author_name', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                                    __attr_alt = __quote(__attr_alt, '"', '&quot;', '', _DEFAULT_MARKER)
                                    if (__attr_alt is not None):
                                        __append((' alt="%s"' % __attr_alt))

                                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097339759424
                                    __default_140097339759424 = _DEFAULT_MARKER

                                    # <Substitution 'portrait_url' (76:27)> -> __attr_src
                                    __token = 3191
                                    try:
                                        __zt_tmp = __attrs_140097342750976
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_src = _static_140097413192464('path', 'portrait_url', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                                    __attr_src = __quote(__attr_src, '"', '&quot;', 'defaultUser.png', _DEFAULT_MARKER)
                                    if (__attr_src is not None):
                                        __append((' src="%s"' % __attr_src))
                                    __append(' />\n              </a>')
                                __append('\n              ')

                                # <Static value=<ast.Dict object at 0x7f6af40cfbb0> name=None at 7f6af40cc700> -> __attrs_140097337744480
                                __attrs_140097337744480 = _static_140097337752496

                                # <Value 'not: has_author_link' (83:34)> -> __condition
                                __token = 3413
                                try:
                                    __zt_tmp = __attrs_140097337744480
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __condition = _static_140097413192464('not', ' has_author_link', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                                if __condition:

                                    # <img ... (0:0)
                                    # --------------------------------------------------------
                                    __append('<img')

                                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097337751968
                                    __default_140097337751968 = _DEFAULT_MARKER

                                    # <Substitution 'reply/author_name' (86:24)> -> __attr_alt
                                    __token = 3534
                                    try:
                                        __zt_tmp = __attrs_140097337744480
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_alt = _static_140097413192464('path', 'reply/author_name', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                                    __attr_alt = __quote(__attr_alt, '"', '&quot;', '', _DEFAULT_MARKER)
                                    if (__attr_alt is not None):
                                        __append((' alt="%s"' % __attr_alt))

                                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097337745056
                                    __default_140097337745056 = _DEFAULT_MARKER

                                    # <Substitution 'portrait_url' (85:25)> -> __attr_src
                                    __token = 3496
                                    try:
                                        __zt_tmp = __attrs_140097337744480
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_src = _static_140097413192464('path', 'portrait_url', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                                    __attr_src = __quote(__attr_src, '"', '&quot;', 'defaultUser.png', _DEFAULT_MARKER)
                                    if (__attr_src is not None):
                                        __append((' src="%s"' % __attr_src))
                                    __append(' />')
                                __append('\n            </div>')
                            __append('\n\n            <!-- commenter name and date -->\n            ')

                            # <Static value=<ast.Dict object at 0x7f6af40cf400> name=None at 7f6af40cc8b0> -> __attrs_140097337748512
                            __attrs_140097337748512 = _static_140097337750528

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append('<div class="comment-author">\n\n              ')

                            # <Static value=<ast.Dict object at 0x7f6af40cd7b0> name=None at 7f6af40cd4b0> -> __attrs_140097337743760
                            __attrs_140097337743760 = _static_140097337743280

                            # <Value 'has_author_link' (95:32)> -> __condition
                            __token = 3756
                            try:
                                __zt_tmp = __attrs_140097337743760
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140097413192464('path', 'has_author_link', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                            if __condition:

                                # <a ... (0:0)
                                # --------------------------------------------------------
                                __append('<a')

                                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097337743424
                                __default_140097337743424 = _DEFAULT_MARKER

                                # <Substitution 'author_home_url' (97:24)> -> __attr_href
                                __token = 3831
                                try:
                                    __zt_tmp = __attrs_140097337743760
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_href = _static_140097413192464('path', 'author_home_url', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                                __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                                if (__attr_href is not None):
                                    __append((' href="%s"' % __attr_href))
                                __append(' >')

                                # <Interpolation value=<Substitution '${reply/author_name}' (99:15)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f6af40cc130> -> __content_140097497049648
                                __token = 3882
                                __token = 3884
                                try:
                                    __zt_tmp = __attrs_140097337743760
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __content_140097497049648 = _static_140097413192464('path', 'reply/author_name', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                                __content_140097497049648 = __quote(__content_140097497049648, '\x00', '&#0;', None, None)
                                __content_140097497049648 = __content_140097497049648
                                if (__content_140097497049648 is None):
                                    pass
                                else:
                                    if (__content_140097497049648 is None):
                                        __content_140097497049648 = None
                                    else:
                                        __tt = type(__content_140097497049648)
                                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                                            __content_140097497049648 = str(__content_140097497049648)
                                        else:
                                            if (__tt is bytes):
                                                __content_140097497049648 = decode(__content_140097497049648)
                                            else:
                                                if (__tt is not str):
                                                    try:
                                                        __content_140097497049648 = __content_140097497049648.__html__
                                                    except get('AttributeError', AttributeError):
                                                        __converted = convert(__content_140097497049648)
                                                        __content_140097497049648 = (str(__content_140097497049648) if (__content_140097497049648 is __converted) else __converted)
                                                    else:
                                                        __content_140097497049648 = __content_140097497049648()
                                if (__content_140097497049648 is not None):
                                    __append(__content_140097497049648)
                                __append('</a>')
                            __append('\n\n              ')

                            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097337753120
                            __attrs_140097337753120 = _static_140097412968080

                            # <Value 'not: has_author_link' (101:35)> -> __condition
                            __token = 3943
                            try:
                                __zt_tmp = __attrs_140097337753120
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140097413192464('not', ' has_author_link', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                            if __condition:

                                # <span ... (0:0)
                                # --------------------------------------------------------
                                __append('<span>')

                                # <Interpolation value=<Substitution '${reply/author_name}' (101:57)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f6af4124070> -> __content_140097497049648
                                __token = 3965
                                __token = 3967
                                try:
                                    __zt_tmp = __attrs_140097337753120
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __content_140097497049648 = _static_140097413192464('path', 'reply/author_name', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                                __content_140097497049648 = __quote(__content_140097497049648, '\x00', '&#0;', None, None)
                                __content_140097497049648 = __content_140097497049648
                                if (__content_140097497049648 is None):
                                    pass
                                else:
                                    if (__content_140097497049648 is None):
                                        __content_140097497049648 = None
                                    else:
                                        __tt = type(__content_140097497049648)
                                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                                            __content_140097497049648 = str(__content_140097497049648)
                                        else:
                                            if (__tt is bytes):
                                                __content_140097497049648 = decode(__content_140097497049648)
                                            else:
                                                if (__tt is not str):
                                                    try:
                                                        __content_140097497049648 = __content_140097497049648.__html__
                                                    except get('AttributeError', AttributeError):
                                                        __converted = convert(__content_140097497049648)
                                                        __content_140097497049648 = (str(__content_140097497049648) if (__content_140097497049648 is __converted) else __converted)
                                                    else:
                                                        __content_140097497049648 = __content_140097497049648()
                                if (__content_140097497049648 is not None):
                                    __append(__content_140097497049648)
                                __append('</span>')
                            __append('\n\n              ')

                            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097338098496
                            __attrs_140097338098496 = _static_140097412968080

                            # <Value 'not: reply/author_name' (103:35)> -> __condition
                            __token = 4029
                            try:
                                __zt_tmp = __attrs_140097338098496
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140097413192464('not', ' reply/author_name', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                            if __condition:

                                # <span ... (0:0)
                                # --------------------------------------------------------
                                __append('<span >')
                                __stream_140097338098016 = []
                                __append_140097338098016 = __stream_140097338098016.append
                                __append_140097338098016('Anonymous')
                                __msgid_140097338098016 = __re_whitespace(''.join(__stream_140097338098016)).strip()
                                if 'label_anonymous':
                                    __append(translate('label_anonymous', mapping=None, default=__msgid_140097338098016, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                                __append('</span>')
                            __append('\n\n              ')

                            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097338099456
                            __attrs_140097338099456 = _static_140097412968080

                            # <br ... (0:0)
                            # --------------------------------------------------------
                            __append('<br />\n\n              ')

                            # <Static value=<ast.Dict object at 0x7f6af4124ca0> name=None at 7f6af4124cd0> -> __attrs_140097338101280
                            __attrs_140097338101280 = _static_140097338100896

                            # <small ... (0:0)
                            # --------------------------------------------------------
                            __append('<small class="text-muted" >')

                            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338100320
                            __default_140097338100320 = _DEFAULT_MARKER

                            # <Value 'python:view.format_time(reply.modification_date)' (110:34)> -> __cache_140097338099840
                            __token = 4235
                            try:
                                __zt_tmp = __attrs_140097338101280
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140097338099840 = _static_140097413192464('python', 'view.format_time(reply.modification_date)', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                            # <BinOp left=<Value 'python:view.format_time(reply.modification_date)' (110:34)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6af4124940> -> __condition
                            __expression = __cache_140097338099840

                            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                __append('\n                      8/23/2001 12:40:44 PM\n              ')
                            else:
                                __content = __cache_140097338099840
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append(__content)
                            __append('</small>\n\n            </div>\n          </div>\n\n\n\n          <!-- comment body -->\n          ')

                            # <Static value=<ast.Dict object at 0x7f6af4125180> name=None at 7f6af41251b0> -> __attrs_140097338102528
                            __attrs_140097338102528 = _static_140097338102144

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append('<div class="comment-body">\n\n            ')

                            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097338104160
                            __attrs_140097338104160 = _static_140097412968080

                            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338103968
                            __default_140097338103968 = _DEFAULT_MARKER

                            # <Value 'reply/getText' (123:41)> -> __cache_140097338103488
                            __token = 4519
                            try:
                                __zt_tmp = __attrs_140097338104160
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140097338103488 = _static_140097413192464('path', 'reply/getText', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                            # <BinOp left=<Value 'reply/getText' (123:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6af4125780> -> __condition
                            __expression = __cache_140097338103488

                            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:

                                # <span ... (0:0)
                                # --------------------------------------------------------
                                __append('<span></span>')
                            else:
                                __content = __cache_140097338103488
                                __content = __convert(__content)
                                if (__content is not None):
                                    __append(__content)
                            __append('\n\n            <!-- comment actions -->\n            ')

                            # <Static value=<ast.Dict object at 0x7f6af4125cf0> name=None at 7f6af4125d20> -> __attrs_140097338105504
                            __attrs_140097338105504 = _static_140097338105072

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append('<div class="d-flex flex-row justify-content-end mb-3">\n\n              ')

                            # <Static value=<ast.Dict object at 0x7f6af41262c0> name=None at 7f6af4126110> -> __attrs_140097338106896
                            __attrs_140097338106896 = _static_140097338106560

                            # <Value 'python:isEditCommentAllowed and canEdit' (129:34)> -> __condition
                            __token = 4738
                            try:
                                __zt_tmp = __attrs_140097338106896
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140097413192464('python', 'isEditCommentAllowed and canEdit', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                            if __condition:

                                # <div ... (0:0)
                                # --------------------------------------------------------
                                __append('<div class="comment-actions actions-edit" >\n\n                <!-- edit -->\n                ')

                                # <Static value=<ast.Dict object at 0x7f6af4126b30> name=None at 7f6af4126b60> -> __attrs_140097338109104
                                __attrs_140097338109104 = _static_140097338108720

                                # <Value 'auth_token' (134:34)> -> __condition
                                __token = 4961
                                try:
                                    __zt_tmp = __attrs_140097338109104
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __condition = _static_140097413192464('path', 'auth_token', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                                if __condition:

                                    # <a ... (0:0)
                                    # --------------------------------------------------------
                                    __append('<a class="pat-plone-modal context comment-action action-edit btn btn-primary btn-sm"')

                                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338108192
                                    __default_140097338108192 = _DEFAULT_MARKER

                                    # <Substitution 'string:${reply/absolute_url}/@@edit-comment?_authenticator=${auth_token}' (136:26)> -> __attr_href
                                    __token = 5035
                                    try:
                                        __zt_tmp = __attrs_140097338109104
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_href = _static_140097413192464('string', '${reply/absolute_url}/@@edit-comment?_authenticator=${auth_token}', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                                    __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                                    if (__attr_href is not None):
                                        __append((' href="%s"' % __attr_href))
                                    __append(' >')
                                    __stream_140097338107856 = []
                                    __append_140097338107856 = __stream_140097338107856.append
                                    __append_140097338107856('Edit')
                                    __msgid_140097338107856 = __re_whitespace(''.join(__stream_140097338107856)).strip()
                                    if 'Edit':
                                        __append(translate('Edit', mapping=None, default=__msgid_140097338107856, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                                    __append('</a>')
                                __append('\n\n                ')

                                # <Static value=<ast.Dict object at 0x7f6af41276a0> name=None at 7f6af41276d0> -> __attrs_140097338112080
                                __attrs_140097338112080 = _static_140097338111648

                                # <Value 'not: auth_token' (145:37)> -> __condition
                                __token = 5393
                                try:
                                    __zt_tmp = __attrs_140097338112080
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __condition = _static_140097413192464('not', ' auth_token', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                                if __condition:

                                    # <form ... (0:0)
                                    # --------------------------------------------------------
                                    __append('<form class="comment-action action-edit"')

                                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338110976
                                    __default_140097338110976 = _DEFAULT_MARKER

                                    # <Substitution 'string:${reply/absolute_url}/@@edit-comment' (147:31)> -> __attr_action
                                    __token = 5480
                                    try:
                                        __zt_tmp = __attrs_140097338112080
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_action = _static_140097413192464('string', '${reply/absolute_url}/@@edit-comment', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                                    __attr_action = __quote(__attr_action, '"', '&quot;', '', _DEFAULT_MARKER)
                                    if (__attr_action is not None):
                                        __append((' action="%s"' % __attr_action))
                                    __append(' method="get" name="edit"')

                                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338110112
                                    __default_140097338110112 = _DEFAULT_MARKER

                                    # <Substitution 'string:edit-${comment_id}' (148:26)> -> __attr_id
                                    __token = 5551
                                    try:
                                        __zt_tmp = __attrs_140097338112080
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_id = _static_140097413192464('string', 'edit-${comment_id}', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                                    if (__attr_id is not None):
                                        __append((' id="%s"' % __attr_id))
                                    __append(' >\n\n                  ')

                                    # <Static value=<ast.Dict object at 0x7f6af4127ee0> name=None at 7f6af4127fd0> -> __attrs_140097338130496
                                    __attrs_140097338130496 = _static_140097338113760

                                    # <button ... (0:0)
                                    # --------------------------------------------------------
                                    __append('<button class="context btn btn-primary btn-sm" name="form.button.EditComment" type="submit"')

                                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338131024
                                    __default_140097338131024 = _DEFAULT_MARKER

                                    # <Translate msgid='label_edit' node=<ast.Constant object at 0x7f6af4127bb0> at 7f6af412c2e0> -> __attr_value
                                    __attr_value = 'Edit'
                                    __attr_value = translate('label_edit', default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                                    if (__attr_value is not None):
                                        __append((' value="%s"' % __attr_value))
                                    __append(' >')
                                    __stream_140097338112848 = []
                                    __append_140097338112848 = __stream_140097338112848.append
                                    __append_140097338112848('Edit')
                                    __msgid_140097338112848 = __re_whitespace(''.join(__stream_140097338112848)).strip()
                                    if 'label_edit':
                                        __append(translate('label_edit', mapping=None, default=__msgid_140097338112848, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                                    __append('</button>\n\n                </form>')
                                __append('\n\n              </div>')
                            __append('\n\n              ')

                            # <Static value=<ast.Dict object at 0x7f6af412c5b0> name=None at 7f6af4127a60> -> __attrs_140097338132224
                            __attrs_140097338132224 = _static_140097338131888

                            # <Value 'python:canDelete' (165:34)> -> __condition
                            __token = 6112
                            try:
                                __zt_tmp = __attrs_140097338132224
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140097413192464('python', 'canDelete', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                            if __condition:

                                # <div ... (0:0)
                                # --------------------------------------------------------
                                __append('<div class="comment-actions actions-delete" >\n\n                <!-- delete own comment -->\n                ')

                                # <Static value=<ast.Dict object at 0x7f6af412d1b0> name=None at 7f6af412d1e0> -> __attrs_140097338135728
                                __attrs_140097338135728 = _static_140097338134960

                                # <Value 'python:not canDelete and isDeleteOwnCommentAllowed and view.could_delete_own(reply)' (173:37)> -> __condition
                                __token = 6391
                                try:
                                    __zt_tmp = __attrs_140097338135728
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __condition = _static_140097413192464('python', 'not canDelete and isDeleteOwnCommentAllowed and view.could_delete_own(reply)', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                                if __condition:

                                    # <form ... (0:0)
                                    # --------------------------------------------------------
                                    __append('<form class="comment-action action-delete"')

                                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338135056
                                    __default_140097338135056 = _DEFAULT_MARKER

                                    # <Substitution 'string:${reply/absolute_url}/@@delete-own-comment' (175:31)> -> __attr_action
                                    __token = 6546
                                    try:
                                        __zt_tmp = __attrs_140097338135728
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_action = _static_140097413192464('string', '${reply/absolute_url}/@@delete-own-comment', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                                    __attr_action = __quote(__attr_action, '"', '&quot;', '', _DEFAULT_MARKER)
                                    if (__attr_action is not None):
                                        __append((' action="%s"' % __attr_action))
                                    __append(' method="post" name="delete"')

                                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338133424
                                    __default_140097338133424 = _DEFAULT_MARKER

                                    # <Substitution "python:view.can_delete_own(reply) and 'display: inline' or 'display: none'" (176:29)> -> __attr_style
                                    __token = 6626
                                    try:
                                        __zt_tmp = __attrs_140097338135728
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_style = _static_140097413192464('python', "view.can_delete_own(reply) and 'display: inline' or 'display: none'", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                                    __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
                                    if (__attr_style is not None):
                                        __append((' style="%s"' % __attr_style))

                                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338135200
                                    __default_140097338135200 = _DEFAULT_MARKER

                                    # <Substitution 'string:delete-${comment_id}' (177:25)> -> __attr_id
                                    __token = 6728
                                    try:
                                        __zt_tmp = __attrs_140097338135728
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_id = _static_140097413192464('string', 'delete-${comment_id}', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                                    if (__attr_id is not None):
                                        __append((' id="%s"' % __attr_id))
                                    __append(' >\n                  ')

                                    # <Static value=<ast.Dict object at 0x7f6af412ded0> name=None at 7f6af412df00> -> __attrs_140097338136592
                                    __attrs_140097338136592 = _static_140097338138320

                                    # <button ... (0:0)
                                    # --------------------------------------------------------
                                    __append('<button class="destructive btn btn-danger btn-sm" name="form.button.DeleteComment" type="submit"')

                                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338137216
                                    __default_140097338137216 = _DEFAULT_MARKER

                                    # <Translate msgid='label_delete' node=<ast.Constant object at 0x7f6af412db40> at 7f6af412db10> -> __attr_value
                                    __attr_value = 'Delete'
                                    __attr_value = translate('label_delete', default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                                    if (__attr_value is not None):
                                        __append((' value="%s"' % __attr_value))
                                    __append(' >')
                                    __stream_140097338136496 = []
                                    __append_140097338136496 = __stream_140097338136496.append
                                    __append_140097338136496('Delete')
                                    __msgid_140097338136496 = __re_whitespace(''.join(__stream_140097338136496)).strip()
                                    if 'label_delete':
                                        __append(translate('label_delete', mapping=None, default=__msgid_140097338136496, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                                    __append('</button>\n                </form>')
                                __append('\n\n                <!-- delete -->\n                ')

                                # <Static value=<ast.Dict object at 0x7f6af412e830> name=None at 7f6af412e860> -> __attrs_140097338141104
                                __attrs_140097338141104 = _static_140097338140720

                                # <Value 'python:canDelete' (194:37)> -> __condition
                                __token = 7421
                                try:
                                    __zt_tmp = __attrs_140097338141104
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __condition = _static_140097413192464('python', 'canDelete', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                                if __condition:

                                    # <form ... (0:0)
                                    # --------------------------------------------------------
                                    __append('<form class="comment-action action-delete"')

                                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338140816
                                    __default_140097338140816 = _DEFAULT_MARKER

                                    # <Substitution 'string:${reply/absolute_url}/@@moderate-delete-comment' (196:31)> -> __attr_action
                                    __token = 7509
                                    try:
                                        __zt_tmp = __attrs_140097338141104
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_action = _static_140097413192464('string', '${reply/absolute_url}/@@moderate-delete-comment', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                                    __attr_action = __quote(__attr_action, '"', '&quot;', '', _DEFAULT_MARKER)
                                    if (__attr_action is not None):
                                        __append((' action="%s"' % __attr_action))
                                    __append(' method="post" name="delete"')

                                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338139232
                                    __default_140097338139232 = _DEFAULT_MARKER

                                    # <Substitution 'string:delete-${comment_id}' (197:26)> -> __attr_id
                                    __token = 7591
                                    try:
                                        __zt_tmp = __attrs_140097338141104
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_id = _static_140097413192464('string', 'delete-${comment_id}', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                                    if (__attr_id is not None):
                                        __append((' id="%s"' % __attr_id))
                                    __append(' >\n                  ')

                                    # <Static value=<ast.Dict object at 0x7f6af412f3d0> name=None at 7f6af412f400> -> __attrs_140097338141968
                                    __attrs_140097338141968 = _static_140097338143696

                                    # <button ... (0:0)
                                    # --------------------------------------------------------
                                    __append('<button class="destructive btn btn-danger btn-sm" name="form.button.DeleteComment" type="submit"')

                                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338142592
                                    __default_140097338142592 = _DEFAULT_MARKER

                                    # <Translate msgid='label_delete' node=<ast.Constant object at 0x7f6af412f040> at 7f6af412f010> -> __attr_value
                                    __attr_value = 'Delete'
                                    __attr_value = translate('label_delete', default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                                    if (__attr_value is not None):
                                        __append((' value="%s"' % __attr_value))
                                    __append(' >')
                                    __stream_140097338141872 = []
                                    __append_140097338141872 = __stream_140097338141872.append
                                    __append_140097338141872('Delete')
                                    __msgid_140097338141872 = __re_whitespace(''.join(__stream_140097338141872)).strip()
                                    if 'label_delete':
                                        __append(translate('label_delete', mapping=None, default=__msgid_140097338141872, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                                    __append('</button>\n                </form>')
                                __append('\n\n              </div>')
                            __append('\n\n              ')

                            # <Static value=<ast.Dict object at 0x7f6af412f670> name=None at 7f6af412f6a0> -> __attrs_140097338144800
                            __attrs_140097338144800 = _static_140097338144368

                            # <Value 'reply_dict/actions|nothing' (212:34)> -> __condition
                            __token = 8183
                            try:
                                __zt_tmp = __attrs_140097338144800
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140097413192464('path', 'reply_dict/actions|nothing', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                            if __condition:

                                # <div ... (0:0)
                                # --------------------------------------------------------
                                __append('<div class="comment-actions actions-workflow d-flex flex-row" >\n\n                ')

                                # <Static value=<ast.Dict object at 0x7f6af412fee0> name=None at 7f6af412ff10> -> __attrs_140097338148464
                                __attrs_140097338148464 = _static_140097338146528

                                # <Value 'canReview' (219:37)> -> __condition
                                __token = 8427
                                try:
                                    __zt_tmp = __attrs_140097338148464
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __condition = _static_140097413192464('path', 'canReview', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                                if __condition:
                                    __backup_action_140097339913504 = get('action', __marker)

                                    # <Value 'reply_dict/actions|nothing' (220:41)> -> __iterator
                                    __token = 8479
                                    try:
                                        __zt_tmp = __attrs_140097338148464
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __iterator = _static_140097413192464('path', 'reply_dict/actions|nothing', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                                    (__iterator, ____index_140097338148800, ) = getname('repeat')('action', __iterator)
                                    econtext['action'] = None
                                    for __item in __iterator:
                                        econtext['action'] = __item

                                        # <form ... (0:0)
                                        # --------------------------------------------------------
                                        __append('<form')

                                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338146720
                                        __default_140097338146720 = _DEFAULT_MARKER

                                        # <Interpolation value=<Substitution 'comment-action action-${action/id}' (215:29)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f6af412fd90> -> __attr_class
                                        __token = 8257
                                        __token = 8281
                                        try:
                                            __zt_tmp = __attrs_140097338148464
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __attr_class = _static_140097413192464('path', 'action/id', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                                        __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                                        __attr_class = ('%s%s' % ('comment-action action-', (__attr_class if (__attr_class is not None) else ''), ))
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

                                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338147408
                                        __default_140097338147408 = _DEFAULT_MARKER

                                        # <Substitution 'string:${reply/absolute_url}/@@transmit-comment' (222:31)> -> __attr_action
                                        __token = 8577
                                        try:
                                            __zt_tmp = __attrs_140097338148464
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __attr_action = _static_140097413192464('string', '${reply/absolute_url}/@@transmit-comment', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                                        __attr_action = __quote(__attr_action, '"', '&quot;', '', _DEFAULT_MARKER)
                                        if (__attr_action is not None):
                                            __append((' action="%s"' % __attr_action))
                                        __append(' method="get"')

                                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338146928
                                        __default_140097338146928 = _DEFAULT_MARKER

                                        # <Substitution 'action/id' (223:28)> -> __attr_name
                                        __token = 8654
                                        try:
                                            __zt_tmp = __attrs_140097338148464
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __attr_name = _static_140097413192464('path', 'action/id', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                                        __attr_name = __quote(__attr_name, '"', '&quot;', '', _DEFAULT_MARKER)
                                        if (__attr_name is not None):
                                            __append((' name="%s"' % __attr_name))

                                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338147936
                                        __default_140097338147936 = _DEFAULT_MARKER

                                        # <Substitution 'string:${action/id}-${comment_id}' (224:25)> -> __attr_id
                                        __token = 8691
                                        try:
                                            __zt_tmp = __attrs_140097338148464
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __attr_id = _static_140097413192464('string', '${action/id}-${comment_id}', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                                        __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                                        if (__attr_id is not None):
                                            __append((' id="%s"' % __attr_id))
                                        __append(' >\n                  ')

                                        # <Static value=<ast.Dict object at 0x7f6af4130d60> name=None at 7f6af4130d90> -> __attrs_140097338150720
                                        __attrs_140097338150720 = _static_140097338150240

                                        # <input ... (0:0)
                                        # --------------------------------------------------------
                                        __append('<input name="workflow_action" type="hidden"')

                                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338149568
                                        __default_140097338149568 = _DEFAULT_MARKER

                                        # <Substitution 'action/id' (230:33)> -> __attr_value
                                        __token = 8932
                                        try:
                                            __zt_tmp = __attrs_140097338150720
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __attr_value = _static_140097413192464('path', 'action/id', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                                        __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                                        if (__attr_value is not None):
                                            __append((' value="%s"' % __attr_value))
                                        __append(' />\n                  ')

                                        # <Static value=<ast.Dict object at 0x7f6af4131420> name=None at 7f6af4131450> -> __attrs_140097338152448
                                        __attrs_140097338152448 = _static_140097338151968

                                        # <button ... (0:0)
                                        # --------------------------------------------------------
                                        __append('<button class="context btn btn-primary btn-sm" name="form.button.TransmitComment" type="submit" >')
                                        __stream_140097338151104 = []
                                        __append_140097338151104 = __stream_140097338151104.append

                                        # <Interpolation value=<Substitution '${action/title}' (237:19)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f6af4131750> -> __content_140097497049648
                                        __token = 9220
                                        __token = 9222
                                        try:
                                            __zt_tmp = __attrs_140097338152448
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __content_140097497049648 = _static_140097413192464('path', 'action/title', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                                        __content_140097497049648 = __quote(__content_140097497049648, '\x00', '&#0;', None, None)
                                        __content_140097497049648 = __content_140097497049648
                                        if (__content_140097497049648 is None):
                                            pass
                                        else:
                                            if (__content_140097497049648 is None):
                                                __content_140097497049648 = None
                                            else:
                                                __tt = type(__content_140097497049648)
                                                if ((__tt is int) or (__tt is float) or (__tt is int)):
                                                    __content_140097497049648 = str(__content_140097497049648)
                                                else:
                                                    if (__tt is bytes):
                                                        __content_140097497049648 = decode(__content_140097497049648)
                                                    else:
                                                        if (__tt is not str):
                                                            try:
                                                                __content_140097497049648 = __content_140097497049648.__html__
                                                            except get('AttributeError', AttributeError):
                                                                __converted = convert(__content_140097497049648)
                                                                __content_140097497049648 = (str(__content_140097497049648) if (__content_140097497049648 is __converted) else __converted)
                                                            else:
                                                                __content_140097497049648 = __content_140097497049648()
                                        if (__content_140097497049648 is not None):
                                            __append_140097338151104(__content_140097497049648)
                                        __msgid_140097338151104 = __re_whitespace(''.join(__stream_140097338151104)).strip()
                                        if __msgid_140097338151104:
                                            __append(translate(__msgid_140097338151104, mapping=None, default=__msgid_140097338151104, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                                        __append('</button>\n                </form>')
                                        ____index_140097338148800 -= 1
                                        if (____index_140097338148800 > 0):
                                            __append('\n                ')
                                    if (__backup_action_140097339913504 is __marker):
                                        del econtext['action']
                                    else:
                                        econtext['action'] = __backup_action_140097339913504
                                __append('\n\n              </div>')
                            __append('\n\n            </div>\n            <!-- end comment actions -->\n\n\n          </div>\n          ')

                            # <Static value=<ast.Dict object at 0x7f6af41318d0> name=None at 7f6af4131900> -> __attrs_140097338153600
                            __attrs_140097338153600 = _static_140097338153168

                            # <Value 'python:isDiscussionAllowed and (isAnon and isAnonymousDiscussionAllowed or userHasReplyPermission)' (248:33)> -> __condition
                            __token = 9507
                            try:
                                __zt_tmp = __attrs_140097338153600
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140097413192464('python', 'isDiscussionAllowed and (isAnon and isAnonymousDiscussionAllowed or userHasReplyPermission)', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                            if __condition:

                                # <button ... (0:0)
                                # --------------------------------------------------------
                                __append('<button class="context reply-to-comment-button hide allowMultiSubmit btn btn-primary btn-sm" >')
                                __stream_140097338148752 = []
                                __append_140097338148752 = __stream_140097338148752.append
                                __append_140097338148752('\n                    Reply\n          ')
                                __msgid_140097338148752 = __re_whitespace(''.join(__stream_140097338148752)).strip()
                                if 'label_reply':
                                    __append(translate('label_reply', mapping=None, default=__msgid_140097338148752, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                                __append('</button>')
                            __append('\n\n        </div>')
                        if (__backup_colorclass_140097340845808 is __marker):
                            del econtext['colorclass']
                        else:
                            econtext['colorclass'] = __backup_colorclass_140097340845808
                        if (__backup_canDelete_140097340838128 is __marker):
                            del econtext['canDelete']
                        else:
                            econtext['canDelete'] = __backup_canDelete_140097340838128
                        if (__backup_canEdit_140097340844656 is __marker):
                            del econtext['canEdit']
                        else:
                            econtext['canEdit'] = __backup_canEdit_140097340844656
                        if (__backup_review_state_140097340840288 is __marker):
                            del econtext['review_state']
                        else:
                            econtext['review_state'] = __backup_review_state_140097340840288
                        if (__backup_portrait_url_140097340845136 is __marker):
                            del econtext['portrait_url']
                        else:
                            econtext['portrait_url'] = __backup_portrait_url_140097340845136
                        if (__backup_has_author_link_140097340842640 is __marker):
                            del econtext['has_author_link']
                        else:
                            econtext['has_author_link'] = __backup_has_author_link_140097340842640
                        if (__backup_author_home_url_140097340842016 is __marker):
                            del econtext['author_home_url']
                        else:
                            econtext['author_home_url'] = __backup_author_home_url_140097340842016
                        if (__backup_depth_140097340835296 is __marker):
                            del econtext['depth']
                        else:
                            econtext['depth'] = __backup_depth_140097340835296
                        if (__backup_depth_140097339549024 is __marker):
                            del econtext['depth']
                        else:
                            econtext['depth'] = __backup_depth_140097339549024
                        if (__backup_comment_id_140097340390704 is __marker):
                            del econtext['comment_id']
                        else:
                            econtext['comment_id'] = __backup_comment_id_140097340390704
                        if (__backup_reply_140097365468416 is __marker):
                            del econtext['reply']
                        else:
                            econtext['reply'] = __backup_reply_140097365468416
                        __append('\n\n      ')
                        ____index_140097339651552 -= 1
                        if (____index_140097339651552 > 0):
                            __append('')
                    if (__backup_reply_dict_140097339173728 is __marker):
                        del econtext['reply_dict']
                    else:
                        econtext['reply_dict'] = __backup_reply_dict_140097339173728
                    __append('\n\n      ')

                    # <Static value=<ast.Dict object at 0x7f6af429ead0> name=None at 7f6af944b310> -> __attrs_140097338154752
                    __attrs_140097338154752 = _static_140097339648720

                    # <Value 'python: has_replies and not isDiscussionAllowed' (259:26)> -> __condition
                    __token = 9808
                    try:
                        __zt_tmp = __attrs_140097338154752
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140097413192464('python', ' has_replies and not isDiscussionAllowed', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    if __condition:

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append('<div class="discreet" >')
                        __stream_140097342600576 = []
                        __append_140097342600576 = __stream_140097342600576.append
                        __append_140097342600576('\n            Commenting has been disabled.\n      ')
                        __msgid_140097342600576 = __re_whitespace(''.join(__stream_140097342600576)).strip()
                        if 'label_commenting_disabled':
                            __append(translate('label_commenting_disabled', mapping=None, default=__msgid_140097342600576, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</div>')
                    __append('\n\n    </div>')
                __append('\n\n    ')

                # <Static value=<ast.Dict object at 0x7f6af41322c0> name=None at 7f6af41322f0> -> __attrs_140097338156096
                __attrs_140097338156096 = _static_140097338155712

                # <Value 'python:has_replies and (isAnon and not isAnonymousDiscussionAllowed)' (268:24)> -> __condition
                __token = 10034
                try:
                    __zt_tmp = __attrs_140097338156096
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140097413192464('python', 'has_replies and (isAnon and not isAnonymousDiscussionAllowed)', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="reply" >\n      ')

                    # <Static value=<ast.Dict object at 0x7f6af4132a70> name=None at 7f6af4132aa0> -> __attrs_140097338158016
                    __attrs_140097338158016 = _static_140097338157680

                    # <form ... (0:0)
                    # --------------------------------------------------------
                    __append('<form class="mb-3"')

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338157200
                    __default_140097338157200 = _DEFAULT_MARKER

                    # <Substitution 'view/login_action' (272:21)> -> __attr_action
                    __token = 10185
                    try:
                        __zt_tmp = __attrs_140097338158016
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_action = _static_140097413192464('path', 'view/login_action', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    __attr_action = __quote(__attr_action, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_action is not None):
                        __append((' action="%s"' % __attr_action))
                    __append(' >\n        ')

                    # <Static value=<ast.Dict object at 0x7f6af4133190> name=None at 7f6af41331c0> -> __attrs_140097338160224
                    __attrs_140097338160224 = _static_140097338159504

                    # <button ... (0:0)
                    # --------------------------------------------------------
                    __append('<button class="standalone loginbutton btn btn-primary" type="submit"')

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338159696
                    __default_140097338159696 = _DEFAULT_MARKER

                    # <Translate msgid='label_login_to_add_comments' node=<ast.Constant object at 0x7f6af4132ef0> at 7f6af4132e60> -> __attr_value
                    __attr_value = 'Log in to add comments'
                    __attr_value = translate('label_login_to_add_comments', default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append(' >')
                    __stream_140097338158592 = []
                    __append_140097338158592 = __stream_140097338158592.append
                    __append_140097338158592('Log in to add comments')
                    __msgid_140097338158592 = __re_whitespace(''.join(__stream_140097338158592)).strip()
                    if 'label_login_to_add_comments':
                        __append(translate('label_login_to_add_comments', mapping=None, default=__msgid_140097338158592, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</button>\n      </form>\n    </div>')
                __append('\n\n    ')

                # <Static value=<ast.Dict object at 0x7f6af41338b0> name=None at 7f6af41338e0> -> __attrs_140097338161520
                __attrs_140097338161520 = _static_140097338161328

                # <Value 'python:isDiscussionAllowed and (isAnon and isAnonymousDiscussionAllowed or userHasReplyPermission)' (286:24)> -> __condition
                __token = 10646
                try:
                    __zt_tmp = __attrs_140097338161520
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140097413192464('python', 'isDiscussionAllowed and (isAnon and isAnonymousDiscussionAllowed or userHasReplyPermission)', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="reply border p-3" id="commenting" >\n\n      ')

                    # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097338162672
                    __attrs_140097338162672 = _static_140097412968080

                    # <fieldset ... (0:0)
                    # --------------------------------------------------------
                    __append('<fieldset>\n\n        ')

                    # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097338163792
                    __attrs_140097338163792 = _static_140097412968080

                    # <legend ... (0:0)
                    # --------------------------------------------------------
                    __append('<legend>')
                    __stream_140097338163312 = []
                    __append_140097338163312 = __stream_140097338163312.append
                    __append_140097338163312('Add comment')
                    __msgid_140097338163312 = __re_whitespace(''.join(__stream_140097338163312)).strip()
                    if 'label_add_comment':
                        __append(translate('label_add_comment', mapping=None, default=__msgid_140097338163312, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</legend>\n\n        ')

                    # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097338165328
                    __attrs_140097338165328 = _static_140097412968080

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append('<p>')

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338164752
                    __default_140097338164752 = _DEFAULT_MARKER

                    # <Value 'view/comment_transform_message' (293:24)> -> __cache_140097338164272
                    __token = 10868
                    try:
                        __zt_tmp = __attrs_140097338165328
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140097338164272 = _static_140097413192464('path', 'view/comment_transform_message', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                    # <BinOp left=<Value 'view/comment_transform_message' (293:24)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6af41344f0> -> __condition
                    __expression = __cache_140097338164272

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n                You can add a comment by filling out the form below. Plain text\n                formatting.\n        ')
                    else:
                        __content = __cache_140097338164272
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</p>\n\n        ')

                    # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097338166864
                    __attrs_140097338166864 = _static_140097412968080

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338166672
                    __default_140097338166672 = _DEFAULT_MARKER

                    # <Value 'view/form/render' (298:36)> -> __cache_140097338166192
                    __token = 11059
                    try:
                        __zt_tmp = __attrs_140097338166864
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140097338166192 = _static_140097413192464('path', 'view/form/render', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                    # <BinOp left=<Value 'view/form/render' (298:36)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6af4134c70> -> __condition
                    __expression = __cache_140097338166192

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append('<div></div>')
                    else:
                        __content = __cache_140097338166192
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('\n\n      </fieldset>\n    </div>')
                __append('\n  </div>\n')
                __i18n_domain = __previous_i18n_domain_140097339176032
            if (__backup_auth_token_140097337627632 is __marker):
                del econtext['auth_token']
            else:
                econtext['auth_token'] = __backup_auth_token_140097337627632
            if (__backup_wtool_140097337629216 is __marker):
                del econtext['wtool']
            else:
                econtext['wtool'] = __backup_wtool_140097337629216
            if (__backup_errors_140097337638240 is __marker):
                del econtext['errors']
            else:
                econtext['errors'] = __backup_errors_140097337638240
            if (__backup_showCommenterImage_140097337634880 is __marker):
                del econtext['showCommenterImage']
            else:
                econtext['showCommenterImage'] = __backup_showCommenterImage_140097337634880
            if (__backup_has_replies_140097337636128 is __marker):
                del econtext['has_replies']
            else:
                econtext['has_replies'] = __backup_has_replies_140097337636128
            if (__backup_replies_140097337623168 is __marker):
                del econtext['replies']
            else:
                econtext['replies'] = __backup_replies_140097337623168
            if (__backup_canReview_140097337630656 is __marker):
                del econtext['canReview']
            else:
                econtext['canReview'] = __backup_canReview_140097337630656
            if (__backup_isAnon_140097337626912 is __marker):
                del econtext['isAnon']
            else:
                econtext['isAnon'] = __backup_isAnon_140097337626912
            if (__backup_isDeleteOwnCommentAllowed_140097337626864 is __marker):
                del econtext['isDeleteOwnCommentAllowed']
            else:
                econtext['isDeleteOwnCommentAllowed'] = __backup_isDeleteOwnCommentAllowed_140097337626864
            if (__backup_isEditCommentAllowed_140097337627440 is __marker):
                del econtext['isEditCommentAllowed']
            else:
                econtext['isEditCommentAllowed'] = __backup_isEditCommentAllowed_140097337627440
            if (__backup_isAnonymousDiscussionAllowed_140097337637952 is __marker):
                del econtext['isAnonymousDiscussionAllowed']
            else:
                econtext['isAnonymousDiscussionAllowed'] = __backup_isAnonymousDiscussionAllowed_140097337637952
            if (__backup_isDiscussionAllowed_140097340066544 is __marker):
                del econtext['isDiscussionAllowed']
            else:
                econtext['isDiscussionAllowed'] = __backup_isDiscussionAllowed_140097340066544
            if (__backup_userHasReplyPermission_140097340068752 is __marker):
                del econtext['userHasReplyPermission']
            else:
                econtext['userHasReplyPermission'] = __backup_userHasReplyPermission_140097340068752
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }