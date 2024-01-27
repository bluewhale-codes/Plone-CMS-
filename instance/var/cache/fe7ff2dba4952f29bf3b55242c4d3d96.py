# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/Products/CMFPlone/browser/templates/author.pt'

__tokens = {1088: ('context/@@plone_portal_state/navigation_root_url', 27, 43), 1178: (' context/@@plone_context_state/object_ur', 28, 40), 1258: ('l context/@@plone_portal_state/port', 29, 37), 1345: ('ss view/email_from_addr', 30, 48), 1408: ('hor view/au', 31, 35), 1461: ('name view/use', 32, 36), 1516: ('not: author', 34, 33), 1998: ('view/is_owner', 50, 32), 2043: (' view/is_anonymou', 51, 30), 2096: ('o author/info | nothi', 52, 33), 2151: ('it author/portrait | noth', 53, 30), 2213: ('nfo view/member_', 54, 32), 1958: ('author', 49, 35), 2271: ('context/global_statusmessage/macros/portal_message', 56, 34), 2271: ('context/global_statusmessage/macros/portal_message', 56, 34), 2662: ('portrait/absolute_url', 67, 40), 2772: ('authorinfo/fullname', 69, 35), 2826: ('authorinfo/fullname', 70, 33), 2987: ('not: authorinfo/fullname', 75, 35), 3046: ('username', 76, 33), 3162: ('not:isOwner', 80, 52), 3247: ('isOwner', 81, 71), 3333: ('${portal_url}/author/${view/member_info/url}', 83, 29), 3335: ('portal_url', 83, 31), 3356: ('view/member_info/url', 83, 52), 3485: ('${portal_url}/@@personal-information', 85, 46), 3487: ('portal_url', 85, 48), 3696: ('authorinfo/description', 90, 36), 3927: ('authorinfo/location', 96, 51), 4109: ('authorinfo/location', 99, 49), 4420: ('authorinfo/language', 106, 51), 4670: ('authorinfo/language', 111, 45), 4943: ('python:view.home_folder(username)', 119, 40), 5063: ('python:view.home_folder(username).absolute_url()', 121, 48), 5353: ("python: not view.home_folder(username) and authorinfo['home_page']", 127, 40), 5548: ('authorinfo/home_page', 130, 48), 5821: ('python:not email_from_address', 136, 55), 6231: ("python:not isAnon and not member_info.get('email', None)", 144, 50), 6725: ("python:email_from_address and authorinfo['has_email']", 153, 52), 6849: ('isAnon', 155, 67), 6941: ('string:$portal_url/login', 157, 51), 7436: ("python: not isOwner and not isAnon and member_info.get('email', None)", 169, 52), 7868: ('nocall:view/feedback_form', 177, 66), 7960: (' nocall:for', 178, 65), 8031: ('form/@@ploneform-macros/titlelessform', 179, 56), 8031: ('form/@@ploneform-macros/titlelessform', 179, 56), 8369: ('view/author_content', 187, 49), 8428: ('author_content', 188, 37), 10118: ('string:$here_url/search?Creator=${username}&amp;sort_on=created&amp;sort_order', 222, 50), 10416: ("python:authorinfo['fullname'] or username", 225, 82), 9274: ('author_content', 204, 55), 9385: ('item/date', 206, 55), 9716: ('item/url', 212, 64), 9782: ('item/title', 213, 56), 408: ("python:request.set('disable_border',1)", 11, 35), 495: (" python:request.set('disable_plone.leftcolumn',1", 12, 47), 592: ("o python:request.set('disable_plone.rightcolumn',", 13, 46), 261: ('context/@@main_template/macros/master', 6, 23), 261: ('context/@@main_template/macros/master', 6, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from collections import deque as _deque
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140066154068384 = 'master'
_static_140066151552272 = {'href': '', }
_static_140066151549296 = {'style': 'white-space: nowrap', }
_static_140066151524592 = {'class': 'table', 'summary': 'Lists content written by an author grouped by content type', }
_static_140066151554144 = {'href': '', }
_static_140066151520704 = 'titlelessform'
_static_140066151518256 = {'class': 'discreet', }
_static_140066151515712 = {'class': 'btn btn-secondary', 'type': 'submit', 'value': 'Log in to send feedback', }
_static_140066151513776 = {'action': 'string:$portal_url/login', }
_static_140066151512192 = {'class': 'formControls', }
_static_140066151510272 = {'class': 'discreet', }
_static_140066151508256 = {'class': 'discreet', }
_static_140066151506096 = {'href': '#', 'rel': 'nofollow', }
_static_140066151502928 = {'href': '#', }
_static_140066154214592 = {'class': 'visualClear', }
_static_140066154213488 = {'class': 'discreet', }
_static_140066154212144 = {'id': 'content-core', }
_static_140066154210944 = {'class': 'documentDescription', }
_static_140066154209024 = {'class': 'nav-link', 'href': '${portal_url}/@@personal-information', }
_static_140066154207104 = {'class': 'nav-link active', 'href': '${portal_url}/author/${view/member_info/url}', }
_static_140066154205088 = {'class': 'autotoc-nav nav nav-tabs', }
_static_140066154869232 = {'class': 'autotabs', }
_static_140066153624864 = {'class': 'documentFirstHeading', }
_static_140066153621792 = {'class': 'documentFirstHeading', }
_static_140066153627312 = {'src': '', 'alt': 'User portrait picture', 'class': 'portraitPhoto', }
_static_140066154927712 = {'id': 'content', }
_static_140066154933664 = 'portal_message'
_static_140066153763728 = {'id': 'content', }
_static_140066153760272 = {'class': 'portalMessage error', 'role': 'alert', }
_static_140066241369456 = __C2ZContextWrapper
_static_140066241369744 = __compile_zt_expr
_static_140066241178128 = {}

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

    def render_main(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<ast.Dict object at 0x7f63b68cea10> name=None at 7f63b68ced40> -> __attrs_140066153901856
            __attrs_140066153901856 = _static_140066241178128
            __backup_portal_url_140066154059600 = get('portal_url', __marker)

            # <Value 'context/@@plone_portal_state/navigation_root_url' (27:43)> -> __value
            __token = 1088
            try:
                __zt_tmp = __attrs_140066153901856
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140066241369744('path', 'context/@@plone_portal_state/navigation_root_url', econtext=econtext)(_static_140066241369456(econtext, __zt_tmp))
            econtext['portal_url'] = __value
            __backup_here_url_140066154066272 = get('here_url', __marker)

            # <Value 'context/@@plone_context_state/object_url' (28:40)> -> __value
            __token = 1178
            try:
                __zt_tmp = __attrs_140066153901856
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140066241369744('path', 'context/@@plone_context_state/object_url', econtext=econtext)(_static_140066241369456(econtext, __zt_tmp))
            econtext['here_url'] = __value
            __backup_portal_140066154061376 = get('portal', __marker)

            # <Value 'context/@@plone_portal_state/portal' (29:37)> -> __value
            __token = 1258
            try:
                __zt_tmp = __attrs_140066153901856
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140066241369744('path', 'context/@@plone_portal_state/portal', econtext=econtext)(_static_140066241369456(econtext, __zt_tmp))
            econtext['portal'] = __value
            __backup_email_from_address_140066153898496 = get('email_from_address', __marker)

            # <Value 'view/email_from_address' (30:48)> -> __value
            __token = 1345
            try:
                __zt_tmp = __attrs_140066153901856
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140066241369744('path', 'view/email_from_address', econtext=econtext)(_static_140066241369456(econtext, __zt_tmp))
            econtext['email_from_address'] = __value
            __backup_author_140066153899408 = get('author', __marker)

            # <Value 'view/author' (31:35)> -> __value
            __token = 1408
            try:
                __zt_tmp = __attrs_140066153901856
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140066241369744('path', 'view/author', econtext=econtext)(_static_140066241369456(econtext, __zt_tmp))
            econtext['author'] = __value
            __backup_username_140066153901808 = get('username', __marker)

            # <Value 'view/username' (32:36)> -> __value
            __token = 1461
            try:
                __zt_tmp = __attrs_140066153901856
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140066241369744('path', 'view/username', econtext=econtext)(_static_140066241369456(econtext, __zt_tmp))
            econtext['username'] = __value
            __append('\n\n        ')

            # <Static value=<ast.Dict object at 0x7f63b68cea10> name=None at 7f63b68ced40> -> __attrs_140066153763536
            __attrs_140066153763536 = _static_140066241178128

            # <Value 'not: author' (34:33)> -> __condition
            __token = 1516
            try:
                __zt_tmp = __attrs_140066153763536
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140066241369744('not', ' author', econtext=econtext)(_static_140066241369456(econtext, __zt_tmp))
            if __condition:
                __append('\n            ')

                # <Static value=<ast.Dict object at 0x7f63b1570610> name=None at 7f63b1570520> -> __attrs_140066153759120
                __attrs_140066153759120 = _static_140066153760272

                # <dl ... (0:0)
                # --------------------------------------------------------
                __append('<dl class="portalMessage error" role="alert">\n                ')

                # <Static value=<ast.Dict object at 0x7f63b68cea10> name=None at 7f63b68ced40> -> __attrs_140066153768192
                __attrs_140066153768192 = _static_140066241178128

                # <dt ... (0:0)
                # --------------------------------------------------------
                __append('<dt>')
                __stream_140066153767136 = []
                __append_140066153767136 = __stream_140066153767136.append
                __append_140066153767136('\n                    Error\n                ')
                __msgid_140066153767136 = __re_whitespace(''.join(__stream_140066153767136)).strip()
                if __msgid_140066153767136:
                    __append(translate(__msgid_140066153767136, mapping=None, default=__msgid_140066153767136, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</dt>\n                ')

                # <Static value=<ast.Dict object at 0x7f63b68cea10> name=None at 7f63b68ced40> -> __attrs_140066153763392
                __attrs_140066153763392 = _static_140066241178128

                # <dd ... (0:0)
                # --------------------------------------------------------
                __append('<dd>')
                __stream_140066153764832 = []
                __append_140066153764832 = __stream_140066153764832.append
                __append_140066153764832('\n                    No user by that name.\n                ')
                __msgid_140066153764832 = __re_whitespace(''.join(__stream_140066153764832)).strip()
                if 'text_no_user_by_name':
                    __append(translate('text_no_user_by_name', mapping=None, default=__msgid_140066153764832, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</dd>\n            </dl>\n            ')

                # <Static value=<ast.Dict object at 0x7f63b1571390> name=None at 7f63b1571420> -> __attrs_140066153761280
                __attrs_140066153761280 = _static_140066153763728

                # <article ... (0:0)
                # --------------------------------------------------------
                __append('<article id="content">\n                &nbsp;\n            </article>\n        ')
            __append('\n\n\n        ')

            # <Static value=<ast.Dict object at 0x7f63b68cea10> name=None at 7f63b68ced40> -> __attrs_140066226569072
            __attrs_140066226569072 = _static_140066241178128
            __backup_isOwner_140066153899360 = get('isOwner', __marker)

            # <Value 'view/is_owner' (50:32)> -> __value
            __token = 1998
            try:
                __zt_tmp = __attrs_140066226569072
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140066241369744('path', 'view/is_owner', econtext=econtext)(_static_140066241369456(econtext, __zt_tmp))
            econtext['isOwner'] = __value
            __backup_isAnon_140066153899264 = get('isAnon', __marker)

            # <Value 'view/is_anonymous' (51:30)> -> __value
            __token = 2043
            try:
                __zt_tmp = __attrs_140066226569072
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140066241369744('path', 'view/is_anonymous', econtext=econtext)(_static_140066241369456(econtext, __zt_tmp))
            econtext['isAnon'] = __value
            __backup_authorinfo_140066153763152 = get('authorinfo', __marker)

            # <Value 'author/info | nothing' (52:33)> -> __value
            __token = 2096
            try:
                __zt_tmp = __attrs_140066226569072
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140066241369744('path', 'author/info | nothing', econtext=econtext)(_static_140066241369456(econtext, __zt_tmp))
            econtext['authorinfo'] = __value
            __backup_portrait_140066153765648 = get('portrait', __marker)

            # <Value 'author/portrait | nothing' (53:30)> -> __value
            __token = 2151
            try:
                __zt_tmp = __attrs_140066226569072
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140066241369744('path', 'author/portrait | nothing', econtext=econtext)(_static_140066241369456(econtext, __zt_tmp))
            econtext['portrait'] = __value
            __backup_member_info_140066153763680 = get('member_info', __marker)

            # <Value 'view/member_info' (54:32)> -> __value
            __token = 2213
            try:
                __zt_tmp = __attrs_140066226569072
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140066241369744('path', 'view/member_info', econtext=econtext)(_static_140066241369456(econtext, __zt_tmp))
            econtext['member_info'] = __value

            # <Value 'author' (49:35)> -> __condition
            __token = 1958
            try:
                __zt_tmp = __attrs_140066226569072
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140066241369744('path', 'author', econtext=econtext)(_static_140066241369456(econtext, __zt_tmp))
            if __condition:
                __append('\n\n            ')

                # <Static value=<ast.Dict object at 0x7f63b68cea10> name=None at 7f63b68ced40> -> __attrs_140066154932944
                __attrs_140066154932944 = _static_140066241178128
                __backup_macroname_140066222660288 = get('macroname', __marker)

                # <Static value=<ast.Constant object at 0x7f63b168eda0> name=None at 7f63b168c760> -> __value
                __value = _static_140066154933664
                econtext['macroname'] = __value

                # <Value 'context/global_statusmessage/macros/portal_message' (56:34)> -> __macro
                __token = 2271
                try:
                    __zt_tmp = __attrs_140066154932944
                except get('NameError', NameError):
                    __zt_tmp = None

                __macro = _static_140066241369744('path', 'context/global_statusmessage/macros/portal_message', econtext=econtext)(_static_140066241369456(econtext, __zt_tmp))
                __token = 2271
                __m = __macro.include
                __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                if (__backup_macroname_140066222660288 is __marker):
                    del econtext['macroname']
                else:
                    econtext['macroname'] = __backup_macroname_140066222660288
                __append('\n\n            ')

                # <Static value=<ast.Dict object at 0x7f63b168d660> name=None at 7f63b168d360> -> __attrs_140066154929920
                __attrs_140066154929920 = _static_140066154927712

                # <article ... (0:0)
                # --------------------------------------------------------
                __append('<article id="content">\n                <!-- Author information -->\n\n                ')

                # <Static value=<ast.Dict object at 0x7f63b154feb0> name=None at 7f63b154f490> -> __attrs_140066153625440
                __attrs_140066153625440 = _static_140066153627312

                # <img ... (0:0)
                # --------------------------------------------------------
                __append('<img')

                # <Symbol value=<DEFAULT> at 7f63b6853d30> -> __default_140066153627408
                __default_140066153627408 = _DEFAULT_MARKER

                # <Substitution 'portrait/absolute_url' (67:40)> -> __attr_src
                __token = 2662
                try:
                    __zt_tmp = __attrs_140066153625440
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_src = _static_140066241369744('path', 'portrait/absolute_url', econtext=econtext)(_static_140066241369456(econtext, __zt_tmp))
                __attr_src = __quote(__attr_src, '"', '&quot;', '', _DEFAULT_MARKER)
                if (__attr_src is not None):
                    __append((' src="%s"' % __attr_src))

                # <Symbol value=<DEFAULT> at 7f63b6853d30> -> __default_140066153625872
                __default_140066153625872 = _DEFAULT_MARKER

                # <Translate msgid=None node=<ast.Constant object at 0x7f63b154cee0> at 7f63b154ef20> -> __attr_alt
                __attr_alt = 'User portrait picture'
                __attr_alt = translate(__attr_alt, default=__attr_alt, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                if (__attr_alt is not None):
                    __append((' alt="%s"' % __attr_alt))
                __append(' class="portraitPhoto" />\n                ')

                # <Static value=<ast.Dict object at 0x7f63b154e920> name=None at 7f63b154d660> -> __attrs_140066153611904
                __attrs_140066153611904 = _static_140066153621792

                # <Value 'authorinfo/fullname' (69:35)> -> __condition
                __token = 2772
                try:
                    __zt_tmp = __attrs_140066153611904
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140066241369744('path', 'authorinfo/fullname', econtext=econtext)(_static_140066241369456(econtext, __zt_tmp))
                if __condition:

                    # <h1 ... (0:0)
                    # --------------------------------------------------------
                    __append('<h1 class="documentFirstHeading">')

                    # <Symbol value=<DEFAULT> at 7f63b6853d30> -> __default_140066153624480
                    __default_140066153624480 = _DEFAULT_MARKER

                    # <Value 'authorinfo/fullname' (70:33)> -> __cache_140066153611328
                    __token = 2826
                    try:
                        __zt_tmp = __attrs_140066153611904
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140066153611328 = _static_140066241369744('path', 'authorinfo/fullname', econtext=econtext)(_static_140066241369456(econtext, __zt_tmp))

                    # <BinOp left=<Value 'authorinfo/fullname' (70:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f63b6853d30> at 7f63b154ebc0> -> __condition
                    __expression = __cache_140066153611328

                    # <Symbol value=<DEFAULT> at 7f63b6853d30> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n                    Author name\n                ')
                    else:
                        __content = __cache_140066153611328
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</h1>')
                __append('\n\n                ')

                # <Static value=<ast.Dict object at 0x7f63b154f520> name=None at 7f63b154d180> -> __attrs_140066153623808
                __attrs_140066153623808 = _static_140066153624864

                # <Value 'not: authorinfo/fullname' (75:35)> -> __condition
                __token = 2987
                try:
                    __zt_tmp = __attrs_140066153623808
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140066241369744('not', ' authorinfo/fullname', econtext=econtext)(_static_140066241369456(econtext, __zt_tmp))
                if __condition:

                    # <h1 ... (0:0)
                    # --------------------------------------------------------
                    __append('<h1 class="documentFirstHeading">')

                    # <Symbol value=<DEFAULT> at 7f63b6853d30> -> __default_140066153613392
                    __default_140066153613392 = _DEFAULT_MARKER

                    # <Value 'username' (76:33)> -> __cache_140066153624288
                    __token = 3046
                    try:
                        __zt_tmp = __attrs_140066153623808
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140066153624288 = _static_140066241369744('path', 'username', econtext=econtext)(_static_140066241369456(econtext, __zt_tmp))

                    # <BinOp left=<Value 'username' (76:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f63b6853d30> at 7f63b154ece0> -> __condition
                    __expression = __cache_140066153624288

                    # <Symbol value=<DEFAULT> at 7f63b6853d30> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n                    Author ID\n                ')
                    else:
                        __content = __cache_140066153624288
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</h1>')
                __append('\n\n                ')

                # <Static value=<ast.Dict object at 0x7f63b167f1f0> name=None at 7f63b167d900> -> __attrs_140066154615792
                __attrs_140066154615792 = _static_140066154869232

                # <Negate value=<Value 'not:isOwner' (80:52)> at 7f63b1523d60> -> __cache_140066153446752

                # <Value 'not:isOwner' (80:52)> -> __cache_140066153446752
                __token = 3162
                try:
                    __zt_tmp = __attrs_140066154615792
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140066153446752 = _static_140066241369744('not', 'isOwner', econtext=econtext)(_static_140066241369456(econtext, __zt_tmp))
                __cache_140066153446752 = not __cache_140066153446752
                __condition = __cache_140066153446752
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="autotabs">')
                __append('\n                  ')

                # <Static value=<ast.Dict object at 0x7f63b15dcfa0> name=None at 7f63b15dc220> -> __attrs_140066154205424
                __attrs_140066154205424 = _static_140066154205088

                # <Value 'isOwner' (81:71)> -> __condition
                __token = 3247
                try:
                    __zt_tmp = __attrs_140066154205424
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140066241369744('path', 'isOwner', econtext=econtext)(_static_140066241369456(econtext, __zt_tmp))
                if __condition:

                    # <nav ... (0:0)
                    # --------------------------------------------------------
                    __append('<nav class="autotoc-nav nav nav-tabs">\n                    ')

                    # <Static value=<ast.Dict object at 0x7f63b15dd780> name=None at 7f63b15dd7b0> -> __attrs_140066154207584
                    __attrs_140066154207584 = _static_140066154207104

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a class="nav-link active"')

                    # <Symbol value=<DEFAULT> at 7f63b6853d30> -> __default_140066154206480
                    __default_140066154206480 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution '${portal_url}/author/${view/member_info/url}' (83:29)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f63b15dd5a0> -> __attr_href
                    __token = 3333
                    __token = 3335
                    try:
                        __zt_tmp = __attrs_140066154207584
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140066241369744('path', 'portal_url', econtext=econtext)(_static_140066241369456(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                    __token = 3356
                    try:
                        __zt_tmp = __attrs_140066154207584
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href_3354 = _static_140066241369744('path', 'view/member_info/url', econtext=econtext)(_static_140066241369456(econtext, __zt_tmp))
                    __attr_href_3354 = __quote(__attr_href_3354, '"', '&quot;', None, _DEFAULT_MARKER)
                    __attr_href = ('%s%s%s' % ((__attr_href if (__attr_href is not None) else ''), '/author/', (__attr_href_3354 if (__attr_href_3354 is not None) else ''), ))
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
                    __append('>')
                    __stream_140066154206240 = []
                    __append_140066154206240 = __stream_140066154206240.append
                    __append_140066154206240('View')
                    __msgid_140066154206240 = __re_whitespace(''.join(__stream_140066154206240)).strip()
                    if 'label_view':
                        __append(translate('label_view', mapping=None, default=__msgid_140066154206240, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</a>\n                    ')

                    # <Static value=<ast.Dict object at 0x7f63b15ddf00> name=None at 7f63b15ddf30> -> __attrs_140066154209456
                    __attrs_140066154209456 = _static_140066154209024

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a class="nav-link"')

                    # <Symbol value=<DEFAULT> at 7f63b6853d30> -> __default_140066154208400
                    __default_140066154208400 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution '${portal_url}/@@personal-information' (85:46)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f63b15ddd50> -> __attr_href
                    __token = 3485
                    __token = 3487
                    try:
                        __zt_tmp = __attrs_140066154209456
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140066241369744('path', 'portal_url', econtext=econtext)(_static_140066241369456(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                    __attr_href = ('%s%s' % ((__attr_href if (__attr_href is not None) else ''), '/@@personal-information', ))
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
                    __append('>')
                    __stream_140066154208112 = []
                    __append_140066154208112 = __stream_140066154208112.append
                    __append_140066154208112('Edit')
                    __msgid_140066154208112 = __re_whitespace(''.join(__stream_140066154208112)).strip()
                    if 'label_edit':
                        __append(translate('label_edit', mapping=None, default=__msgid_140066154208112, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</a>\n                  </nav>')
                __append('\n\n                  ')

                # <Static value=<ast.Dict object at 0x7f63b15de680> name=None at 7f63b15de500> -> __attrs_140066154211280
                __attrs_140066154211280 = _static_140066154210944

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="documentDescription">')

                # <Symbol value=<DEFAULT> at 7f63b6853d30> -> __default_140066154210320
                __default_140066154210320 = _DEFAULT_MARKER

                # <Value 'authorinfo/description' (90:36)> -> __cache_140066154209840
                __token = 3696
                try:
                    __zt_tmp = __attrs_140066154211280
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140066154209840 = _static_140066241369744('path', 'authorinfo/description', econtext=econtext)(_static_140066241369456(econtext, __zt_tmp))

                # <BinOp left=<Value 'authorinfo/description' (90:36)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f63b6853d30> at 7f63b15de2f0> -> __condition
                __expression = __cache_140066154209840

                # <Symbol value=<DEFAULT> at 7f63b6853d30> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('\n                      Author description.\n                  ')
                else:
                    __content = __cache_140066154209840
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</div>\n\n                  ')

                # <Static value=<ast.Dict object at 0x7f63b15deb30> name=None at 7f63b15deb60> -> __attrs_140066154212528
                __attrs_140066154212528 = _static_140066154212144

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div id="content-core">\n                      ')

                # <Static value=<ast.Dict object at 0x7f63b15df070> name=None at 7f63b15df0a0> -> __attrs_140066154213872
                __attrs_140066154213872 = _static_140066154213488

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="discreet">\n                          ')

                # <Static value=<ast.Dict object at 0x7f63b68cea10> name=None at 7f63b68ced40> -> __attrs_140066154214832
                __attrs_140066154214832 = _static_140066241178128

                # <Value 'authorinfo/location' (96:51)> -> __condition
                __token = 3927
                try:
                    __zt_tmp = __attrs_140066154214832
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140066241369744('path', 'authorinfo/location', econtext=econtext)(_static_140066241369456(econtext, __zt_tmp))
                if __condition:
                    __stream_140066154092288_location = ''
                    __stream_140066154214448 = []
                    __append_140066154214448 = __stream_140066154214448.append
                    __append_140066154214448('\n                              Location:\n                              ')
                    __stream_140066154092288_location = []
                    __append_140066154092288_location = __stream_140066154092288_location.append

                    # <Static value=<ast.Dict object at 0x7f63b68cea10> name=None at 7f63b68ced40> -> __attrs_140066154216608
                    __attrs_140066154216608 = _static_140066241178128

                    # <Symbol value=<DEFAULT> at 7f63b6853d30> -> __default_140066154216128
                    __default_140066154216128 = _DEFAULT_MARKER

                    # <Value 'authorinfo/location' (99:49)> -> __cache_140066154215648
                    __token = 4109
                    try:
                        __zt_tmp = __attrs_140066154216608
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140066154215648 = _static_140066241369744('path', 'authorinfo/location', econtext=econtext)(_static_140066241369456(econtext, __zt_tmp))

                    # <BinOp left=<Value 'authorinfo/location' (99:49)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f63b6853d30> at 7f63b15df9a0> -> __condition
                    __expression = __cache_140066154215648

                    # <Symbol value=<DEFAULT> at 7f63b6853d30> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append_140066154092288_location('\n                                  Some location\n                              ')
                    else:
                        __content = __cache_140066154215648
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append_140066154092288_location(__content)
                    __append_140066154214448('${location}')
                    __stream_140066154092288_location = ''.join(__stream_140066154092288_location)
                    __append_140066154214448('\n                          ')
                    __msgid_140066154214448 = __re_whitespace(''.join(__stream_140066154214448)).strip()
                    if 'text_location':
                        __append(translate('text_location', mapping={'location': __stream_140066154092288_location, }, default=__msgid_140066154214448, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('\n\n                          ')

                # <Static value=<ast.Dict object at 0x7f63b68cea10> name=None at 7f63b68ced40> -> __attrs_140066154216416
                __attrs_140066154216416 = _static_140066241178128

                # <Value 'authorinfo/language' (106:51)> -> __condition
                __token = 4420
                try:
                    __zt_tmp = __attrs_140066154216416
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140066241369744('path', 'authorinfo/language', econtext=econtext)(_static_140066241369456(econtext, __zt_tmp))
                if __condition:
                    __append('\n                          &mdash;\n                          ')

                    # <Static value=<ast.Dict object at 0x7f63b68cea10> name=None at 7f63b68ced40> -> __attrs_140066151498464
                    __attrs_140066151498464 = _static_140066241178128

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>')
                    __stream_140066151497984 = []
                    __append_140066151497984 = __stream_140066151497984.append
                    __append_140066151497984('\n                              Main Language:\n                          ')
                    __msgid_140066151497984 = __re_whitespace(''.join(__stream_140066151497984)).strip()
                    if 'label_main_language':
                        __append(translate('label_main_language', mapping=None, default=__msgid_140066151497984, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</span>\n                          ')

                    # <Static value=<ast.Dict object at 0x7f63b68cea10> name=None at 7f63b68ced40> -> __attrs_140066151500000
                    __attrs_140066151500000 = _static_140066241178128

                    # <Symbol value=<DEFAULT> at 7f63b6853d30> -> __default_140066151499808
                    __default_140066151499808 = _DEFAULT_MARKER

                    # <Value 'authorinfo/language' (111:45)> -> __cache_140066151499328
                    __token = 4670
                    try:
                        __zt_tmp = __attrs_140066151500000
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140066151499328 = _static_140066241369744('path', 'authorinfo/language', econtext=econtext)(_static_140066241369456(econtext, __zt_tmp))

                    # <BinOp left=<Value 'authorinfo/language' (111:45)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f63b6853d30> at 7f63b1348700> -> __condition
                    __expression = __cache_140066151499328

                    # <Symbol value=<DEFAULT> at 7f63b6853d30> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>\n                            Some language\n                          </span>')
                    else:
                        __content = __cache_140066151499328
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('\n                          ')
                __append('\n                      </div>\n\n                      ')

                # <Static value=<ast.Dict object at 0x7f63b15df4c0> name=None at 7f63b15dfd00> -> __attrs_140066151500768
                __attrs_140066151500768 = _static_140066154214592

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="visualClear"><!-- --></div>\n\n                      ')

                # <Static value=<ast.Dict object at 0x7f63b68cea10> name=None at 7f63b68ced40> -> __attrs_140066151501680
                __attrs_140066151501680 = _static_140066241178128

                # <Value 'python:view.home_folder(username)' (119:40)> -> __condition
                __token = 4943
                try:
                    __zt_tmp = __attrs_140066151501680
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140066241369744('python', 'view.home_folder(username)', econtext=econtext)(_static_140066241369456(econtext, __zt_tmp))
                if __condition:

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append('<p>\n                        ')

                    # <Static value=<ast.Dict object at 0x7f63b1349450> name=None at 7f63b1349480> -> __attrs_140066151503504
                    __attrs_140066151503504 = _static_140066151502928

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 7f63b6853d30> -> __default_140066151502544
                    __default_140066151502544 = _DEFAULT_MARKER

                    # <Substitution 'python:view.home_folder(username).absolute_url()' (121:48)> -> __attr_href
                    __token = 5063
                    try:
                        __zt_tmp = __attrs_140066151503504
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140066241369744('python', 'view.home_folder(username).absolute_url()', econtext=econtext)(_static_140066241369456(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '#', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))
                    __append('>')
                    __stream_140066151502448 = []
                    __append_140066151502448 = __stream_140066151502448.append
                    __append_140066151502448("\n                          Author's home page in this site&hellip;\n                        ")
                    __msgid_140066151502448 = __re_whitespace(''.join(__stream_140066151502448)).strip()
                    if 'label_author_internal_home_page':
                        __append(translate('label_author_internal_home_page', mapping=None, default=__msgid_140066151502448, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</a>\n                      </p>')
                __append('\n\n                      ')

                # <Static value=<ast.Dict object at 0x7f63b68cea10> name=None at 7f63b68ced40> -> __attrs_140066151504272
                __attrs_140066151504272 = _static_140066241178128

                # <Value "python: not view.home_folder(username) and authorinfo['home_page']" (127:40)> -> __condition
                __token = 5353
                try:
                    __zt_tmp = __attrs_140066151504272
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140066241369744('python', " not view.home_folder(username) and authorinfo['home_page']", econtext=econtext)(_static_140066241369456(econtext, __zt_tmp))
                if __condition:

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append('<p>\n                        ')

                    # <Static value=<ast.Dict object at 0x7f63b134a0b0> name=None at 7f63b1349d50> -> __attrs_140066151506336
                    __attrs_140066151506336 = _static_140066151506096

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 7f63b6853d30> -> __default_140066151505808
                    __default_140066151505808 = _DEFAULT_MARKER

                    # <Substitution 'authorinfo/home_page' (130:48)> -> __attr_href
                    __token = 5548
                    try:
                        __zt_tmp = __attrs_140066151506336
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140066241369744('path', 'authorinfo/home_page', econtext=econtext)(_static_140066241369456(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '#', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))
                    __append(' rel="nofollow">')
                    __stream_140066151505040 = []
                    __append_140066151505040 = __stream_140066151505040.append
                    __append_140066151505040("\n                          Author's external home page&hellip;\n                        ")
                    __msgid_140066151505040 = __re_whitespace(''.join(__stream_140066151505040)).strip()
                    if 'label_author_external_home_page':
                        __append(translate('label_author_external_home_page', mapping=None, default=__msgid_140066151505040, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</a>\n                      </p>')
                __append('\n\n                      ')

                # <Static value=<ast.Dict object at 0x7f63b68cea10> name=None at 7f63b68ced40> -> __attrs_140066151507008
                __attrs_140066151507008 = _static_140066241178128

                # <Value 'python:not email_from_address' (136:55)> -> __condition
                __token = 5821
                try:
                    __zt_tmp = __attrs_140066151507008
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140066241369744('python', 'not email_from_address', econtext=econtext)(_static_140066241369456(econtext, __zt_tmp))
                if __condition:
                    __append('\n                          ')

                    # <Static value=<ast.Dict object at 0x7f63b134a920> name=None at 7f63b134a950> -> __attrs_140066151508640
                    __attrs_140066151508640 = _static_140066151508256

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append('<p class="discreet">')
                    __stream_140066151507776 = []
                    __append_140066151507776 = __stream_140066151507776.append
                    __append_140066151507776("\n                              This site doesn't have a valid email setup, so you cannot use\n                              any contact forms.\n                          ")
                    __msgid_140066151507776 = __re_whitespace(''.join(__stream_140066151507776)).strip()
                    if 'text_no_email_setup':
                        __append(translate('text_no_email_setup', mapping=None, default=__msgid_140066151507776, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</p>\n                      ')
                __append('\n\n                      ')

                # <Static value=<ast.Dict object at 0x7f63b68cea10> name=None at 7f63b68ced40> -> __attrs_140066151509024
                __attrs_140066151509024 = _static_140066241178128

                # <Value "python:not isAnon and not member_info.get('email', None)" (144:50)> -> __condition
                __token = 6231
                try:
                    __zt_tmp = __attrs_140066151509024
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140066241369744('python', "not isAnon and not member_info.get('email', None)", econtext=econtext)(_static_140066241369456(econtext, __zt_tmp))
                if __condition:
                    __append('\n                          ')

                    # <Static value=<ast.Dict object at 0x7f63b134b100> name=None at 7f63b134b130> -> __attrs_140066151510656
                    __attrs_140066151510656 = _static_140066151510272

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append('<p class="discreet">')
                    __stream_140066151509792 = []
                    __append_140066151509792 = __stream_140066151509792.append
                    __append_140066151509792('\n                              You do not have an email address, so you\n                              cannot use any contact forms. Please edit\n                              your personal information.\n                          ')
                    __msgid_140066151509792 = __re_whitespace(''.join(__stream_140066151509792)).strip()
                    if 'text_no_member_email':
                        __append(translate('text_no_member_email', mapping=None, default=__msgid_140066151509792, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</p>\n                      ')
                __append('\n\n                      ')

                # <Static value=<ast.Dict object at 0x7f63b68cea10> name=None at 7f63b68ced40> -> __attrs_140066151511040
                __attrs_140066151511040 = _static_140066241178128

                # <Value "python:email_from_address and authorinfo['has_email']" (153:52)> -> __condition
                __token = 6725
                try:
                    __zt_tmp = __attrs_140066151511040
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140066241369744('python', "email_from_address and authorinfo['has_email']", econtext=econtext)(_static_140066241369456(econtext, __zt_tmp))
                if __condition:
                    __append('\n\n                          ')

                    # <Static value=<ast.Dict object at 0x7f63b134b880> name=None at 7f63b134b8b0> -> __attrs_140066151512576
                    __attrs_140066151512576 = _static_140066151512192

                    # <Value 'isAnon' (155:67)> -> __condition
                    __token = 6849
                    try:
                        __zt_tmp = __attrs_140066151512576
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140066241369744('path', 'isAnon', econtext=econtext)(_static_140066241369456(econtext, __zt_tmp))
                    if __condition:

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append('<div class="formControls">\n                          ')

                        # <Static value=<ast.Dict object at 0x7f63b134beb0> name=None at 7f63b134bd00> -> __attrs_140066151514320
                        __attrs_140066151514320 = _static_140066151513776

                        # <form ... (0:0)
                        # --------------------------------------------------------
                        __append('<form')

                        # <Symbol value=<DEFAULT> at 7f63b6853d30> -> __default_140066151513440
                        __default_140066151513440 = _DEFAULT_MARKER

                        # <Substitution 'string:$portal_url/login' (157:51)> -> __attr_action
                        __token = 6941
                        try:
                            __zt_tmp = __attrs_140066151514320
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_action = _static_140066241369744('string', '$portal_url/login', econtext=econtext)(_static_140066241369456(econtext, __zt_tmp))
                        __attr_action = __quote(__attr_action, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_action is not None):
                            __append((' action="%s"' % __attr_action))
                        __append('>\n                             ')

                        # <Static value=<ast.Dict object at 0x7f63b134c640> name=None at 7f63b134c670> -> __attrs_140066151516336
                        __attrs_140066151516336 = _static_140066151515712

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input class="btn btn-secondary" type="submit"')

                        # <Symbol value=<DEFAULT> at 7f63b6853d30> -> __default_140066151515904
                        __default_140066151515904 = _DEFAULT_MARKER

                        # <Translate msgid='label_login_to_send_feedback' node=<ast.Constant object at 0x7f63b134c3a0> at 7f63b134c310> -> __attr_value
                        __attr_value = 'Log in to send feedback'
                        __attr_value = translate('label_login_to_send_feedback', default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        if (__attr_value is not None):
                            __append((' value="%s"' % __attr_value))
                        __append(' />\n                          </form>\n                          </div>')
                    __append('\n\n                          <!-- feedback form -->\n\n\n                          ')

                    # <Static value=<ast.Dict object at 0x7f63b68cea10> name=None at 7f63b68ced40> -> __attrs_140066151517008
                    __attrs_140066151517008 = _static_140066241178128

                    # <Value "python: not isOwner and not isAnon and member_info.get('email', None)" (169:52)> -> __condition
                    __token = 7436
                    try:
                        __zt_tmp = __attrs_140066151517008
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140066241369744('python', " not isOwner and not isAnon and member_info.get('email', None)", econtext=econtext)(_static_140066241369456(econtext, __zt_tmp))
                    if __condition:
                        __append('\n                              ')

                        # <Static value=<ast.Dict object at 0x7f63b134d030> name=None at 7f63b134d060> -> __attrs_140066151518640
                        __attrs_140066151518640 = _static_140066151518256

                        # <p ... (0:0)
                        # --------------------------------------------------------
                        __append('<p class="discreet">')
                        __stream_140066151517776 = []
                        __append_140066151517776 = __stream_140066151517776.append
                        __append_140066151517776('\n                                  If you want to contact this author, fill in the form\n                                  below.\n                              ')
                        __msgid_140066151517776 = __re_whitespace(''.join(__stream_140066151517776)).strip()
                        if 'description_author_feedback':
                            __append(translate('description_author_feedback', mapping=None, default=__msgid_140066151517776, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</p>\n\n\n                              ')

                        # <Static value=<ast.Dict object at 0x7f63b68cea10> name=None at 7f63b68ced40> -> __attrs_140066151519456
                        __attrs_140066151519456 = _static_140066241178128
                        __backup_form_140066154205952 = get('form', __marker)

                        # <Value 'nocall:view/feedback_form' (177:66)> -> __value
                        __token = 7868
                        try:
                            __zt_tmp = __attrs_140066151519456
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140066241369744('nocall', 'view/feedback_form', econtext=econtext)(_static_140066241369456(econtext, __zt_tmp))
                        econtext['form'] = __value
                        __backup_view_140066154215360 = get('view', __marker)

                        # <Value 'nocall:form' (178:65)> -> __value
                        __token = 7960
                        try:
                            __zt_tmp = __attrs_140066151519456
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140066241369744('nocall', 'form', econtext=econtext)(_static_140066241369456(econtext, __zt_tmp))
                        econtext['view'] = __value
                        __append('\n                                ')

                        # <Static value=<ast.Dict object at 0x7f63b68cea10> name=None at 7f63b68ced40> -> __attrs_140066151521040
                        __attrs_140066151521040 = _static_140066241178128
                        __backup_macroname_140066224004288 = get('macroname', __marker)

                        # <Static value=<ast.Constant object at 0x7f63b134d9c0> name=None at 7f63b134d9f0> -> __value
                        __value = _static_140066151520704
                        econtext['macroname'] = __value

                        # <Value 'form/@@ploneform-macros/titlelessform' (179:56)> -> __macro
                        __token = 8031
                        try:
                            __zt_tmp = __attrs_140066151521040
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __macro = _static_140066241369744('path', 'form/@@ploneform-macros/titlelessform', econtext=econtext)(_static_140066241369456(econtext, __zt_tmp))
                        __token = 8031
                        __m = __macro.include
                        __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                        econtext.update(rcontext)
                        if (__backup_macroname_140066224004288 is __marker):
                            del econtext['macroname']
                        else:
                            econtext['macroname'] = __backup_macroname_140066224004288
                        __append('\n                              ')
                        if (__backup_view_140066154215360 is __marker):
                            del econtext['view']
                        else:
                            econtext['view'] = __backup_view_140066154215360
                        if (__backup_form_140066154205952 is __marker):
                            del econtext['form']
                        else:
                            econtext['form'] = __backup_form_140066154205952
                        __append('\n\n                          ')
                    __append('\n                      ')
                __append('\n\n                      <!-- listing of content created by this user -->\n                      ')

                # <Static value=<ast.Dict object at 0x7f63b68cea10> name=None at 7f63b68ced40> -> __attrs_140066151519264
                __attrs_140066151519264 = _static_140066241178128
                __backup_author_content_140066153613440 = get('author_content', __marker)

                # <Value 'view/author_content' (187:49)> -> __value
                __token = 8369
                try:
                    __zt_tmp = __attrs_140066151519264
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140066241369744('path', 'view/author_content', econtext=econtext)(_static_140066241369456(econtext, __zt_tmp))
                econtext['author_content'] = __value

                # <Value 'author_content' (188:37)> -> __condition
                __token = 8428
                try:
                    __zt_tmp = __attrs_140066151519264
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140066241369744('path', 'author_content', econtext=econtext)(_static_140066241369456(econtext, __zt_tmp))
                if __condition:
                    __append('\n\n                          ')

                    # <Static value=<ast.Dict object at 0x7f63b68cea10> name=None at 7f63b68ced40> -> __attrs_140066151522240
                    __attrs_140066151522240 = _static_140066241178128

                    # <h2 ... (0:0)
                    # --------------------------------------------------------
                    __append('<h2>')
                    __stream_140066151521760 = []
                    __append_140066151521760 = __stream_140066151521760.append
                    __append_140066151521760('\n                              Latest content created by this user\n                          ')
                    __msgid_140066151521760 = __re_whitespace(''.join(__stream_140066151521760)).strip()
                    if 'heading_author_content':
                        __append(translate('heading_author_content', mapping=None, default=__msgid_140066151521760, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</h2>\n\n                          ')
                    __token = None
                    render_user_content_listing(__stream, econtext.copy(), rcontext, __i18n_domain)
                    econtext.update(rcontext)
                    __append('\n\n                          ')

                    # <Static value=<ast.Dict object at 0x7f63b68cea10> name=None at 7f63b68ced40> -> __attrs_140066151547664
                    __attrs_140066151547664 = _static_140066241178128

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append('<p>\n                          ')

                    # <Static value=<ast.Dict object at 0x7f63b1355c60> name=None at 7f63b1355c90> -> __attrs_140066151554720
                    __attrs_140066151554720 = _static_140066151554144

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 7f63b6853d30> -> __default_140066151553760
                    __default_140066151553760 = _DEFAULT_MARKER

                    # <Substitution 'string:$here_url/search?Creator=${username}&sort_on=created&sort_order=reverse' (222:50)> -> __attr_href
                    __token = 10118
                    try:
                        __zt_tmp = __attrs_140066151554720
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140066241369744('string', '$here_url/search?Creator=${username}&sort_on=created&sort_order=reverse', econtext=econtext)(_static_140066241369456(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))
                    __append('>')
                    __stream_140066154091840_user = ''
                    __stream_140066151553664 = []
                    __append_140066151553664 = __stream_140066151553664.append
                    __append_140066151553664('\n                              All content created by\n                              ')
                    __stream_140066154091840_user = []
                    __append_140066154091840_user = __stream_140066154091840_user.append

                    # <Static value=<ast.Dict object at 0x7f63b68cea10> name=None at 7f63b68ced40> -> __attrs_140066151556352
                    __attrs_140066151556352 = _static_140066241178128

                    # <Symbol value=<DEFAULT> at 7f63b6853d30> -> __default_140066151555872
                    __default_140066151555872 = _DEFAULT_MARKER

                    # <Value "python:authorinfo['fullname'] or username" (225:82)> -> __cache_140066151555344
                    __token = 10416
                    try:
                        __zt_tmp = __attrs_140066151556352
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140066151555344 = _static_140066241369744('python', "authorinfo['fullname'] or username", econtext=econtext)(_static_140066241369456(econtext, __zt_tmp))

                    # <BinOp left=<Value "python:authorinfo['fullname'] or username" (225:82)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f63b6853d30> at 7f63b1356200> -> __condition
                    __expression = __cache_140066151555344

                    # <Symbol value=<DEFAULT> at 7f63b6853d30> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140066151555344
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append_140066154091840_user(__content)
                    __append_140066151553664('${user}')
                    __stream_140066154091840_user = ''.join(__stream_140066154091840_user)
                    __append_140066151553664('&hellip;\n                          ')
                    __msgid_140066151553664 = __re_whitespace(''.join(__stream_140066151553664)).strip()
                    if 'go_to_search_author_content':
                        __append(translate('go_to_search_author_content', mapping={'user': __stream_140066154091840_user, }, default=__msgid_140066151553664, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</a>\n                          </p>\n\n                      ')
                if (__backup_author_content_140066153613440 is __marker):
                    del econtext['author_content']
                else:
                    econtext['author_content'] = __backup_author_content_140066153613440
                __append('\n                  </div>\n                ')
                __condition = __cache_140066153446752
                if __condition:
                    __append('</div>')
                __append('\n\n            </article>\n\n        ')
            if (__backup_member_info_140066153763680 is __marker):
                del econtext['member_info']
            else:
                econtext['member_info'] = __backup_member_info_140066153763680
            if (__backup_portrait_140066153765648 is __marker):
                del econtext['portrait']
            else:
                econtext['portrait'] = __backup_portrait_140066153765648
            if (__backup_authorinfo_140066153763152 is __marker):
                del econtext['authorinfo']
            else:
                econtext['authorinfo'] = __backup_authorinfo_140066153763152
            if (__backup_isAnon_140066153899264 is __marker):
                del econtext['isAnon']
            else:
                econtext['isAnon'] = __backup_isAnon_140066153899264
            if (__backup_isOwner_140066153899360 is __marker):
                del econtext['isOwner']
            else:
                econtext['isOwner'] = __backup_isOwner_140066153899360
            __append('\n\n    ')
            if (__backup_username_140066153901808 is __marker):
                del econtext['username']
            else:
                econtext['username'] = __backup_username_140066153901808
            if (__backup_author_140066153899408 is __marker):
                del econtext['author']
            else:
                econtext['author'] = __backup_author_140066153899408
            if (__backup_email_from_address_140066153898496 is __marker):
                del econtext['email_from_address']
            else:
                econtext['email_from_address'] = __backup_email_from_address_140066153898496
            if (__backup_portal_140066154061376 is __marker):
                del econtext['portal']
            else:
                econtext['portal'] = __backup_portal_140066154061376
            if (__backup_here_url_140066154066272 is __marker):
                del econtext['here_url']
            else:
                econtext['here_url'] = __backup_here_url_140066154066272
            if (__backup_portal_url_140066154059600 is __marker):
                del econtext['portal_url']
            else:
                econtext['portal_url'] = __backup_portal_url_140066154059600
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_user_content_listing(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<ast.Dict object at 0x7f63b68cea10> name=None at 7f63b68ced40> -> __attrs_140066151523104
            __attrs_140066151523104 = _static_140066241178128

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div>\n                          ')

            # <Static value=<ast.Dict object at 0x7f63b134e8f0> name=None at 7f63b134e920> -> __attrs_140066151525072
            __attrs_140066151525072 = _static_140066151524592

            # <table ... (0:0)
            # --------------------------------------------------------
            __append('<table class="table"')

            # <Symbol value=<DEFAULT> at 7f63b6853d30> -> __default_140066151523920
            __default_140066151523920 = _DEFAULT_MARKER

            # <Translate msgid='summary_author_content_list' node=<ast.Constant object at 0x7f63b134e740> at 7f63b134e710> -> __attr_summary
            __attr_summary = 'Lists content written by an author grouped by content type'
            __attr_summary = translate('summary_author_content_list', default=__attr_summary, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
            if (__attr_summary is not None):
                __append((' summary="%s"' % __attr_summary))
            __append('>\n                              ')

            # <Static value=<ast.Dict object at 0x7f63b68cea10> name=None at 7f63b68ced40> -> __attrs_140066151526032
            __attrs_140066151526032 = _static_140066241178128

            # <thead ... (0:0)
            # --------------------------------------------------------
            __append('<thead>\n                                ')

            # <Static value=<ast.Dict object at 0x7f63b68cea10> name=None at 7f63b68ced40> -> __attrs_140066151527088
            __attrs_140066151527088 = _static_140066241178128

            # <tr ... (0:0)
            # --------------------------------------------------------
            __append('<tr>\n                                    ')

            # <Static value=<ast.Dict object at 0x7f63b68cea10> name=None at 7f63b68ced40> -> __attrs_140066151528240
            __attrs_140066151528240 = _static_140066241178128

            # <th ... (0:0)
            # --------------------------------------------------------
            __append('<th>')
            __stream_140066151527760 = []
            __append_140066151527760 = __stream_140066151527760.append
            __append_140066151527760('Date')
            __msgid_140066151527760 = __re_whitespace(''.join(__stream_140066151527760)).strip()
            if __msgid_140066151527760:
                __append(translate(__msgid_140066151527760, mapping=None, default=__msgid_140066151527760, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</th>\n                                    ')

            # <Static value=<ast.Dict object at 0x7f63b68cea10> name=None at 7f63b68ced40> -> __attrs_140066151529296
            __attrs_140066151529296 = _static_140066241178128

            # <th ... (0:0)
            # --------------------------------------------------------
            __append('<th>')
            __stream_140066151528816 = []
            __append_140066151528816 = __stream_140066151528816.append
            __append_140066151528816('Content')
            __msgid_140066151528816 = __re_whitespace(''.join(__stream_140066151528816)).strip()
            if __msgid_140066151528816:
                __append(translate(__msgid_140066151528816, mapping=None, default=__msgid_140066151528816, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</th>\n                                </tr>\n                              </thead>\n                              ')

            # <Static value=<ast.Dict object at 0x7f63b68cea10> name=None at 7f63b68ced40> -> __attrs_140066151529920
            __attrs_140066151529920 = _static_140066241178128
            __backup_item_140066151519600 = get('item', __marker)

            # <Value 'author_content' (204:55)> -> __iterator
            __token = 9274
            try:
                __zt_tmp = __attrs_140066151529920
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140066241369744('path', 'author_content', econtext=econtext)(_static_140066241369456(econtext, __zt_tmp))
            (__iterator, ____index_140066151530160, ) = getname('repeat')('item', __iterator)
            econtext['item'] = None
            for __item in __iterator:
                econtext['item'] = __item
                __append('\n                                  ')

                # <Static value=<ast.Dict object at 0x7f63b68cea10> name=None at 7f63b68ced40> -> __attrs_140066151547568
                __attrs_140066151547568 = _static_140066241178128

                # <tr ... (0:0)
                # --------------------------------------------------------
                __append('<tr>\n                                      ')

                # <Static value=<ast.Dict object at 0x7f63b1354970> name=None at 7f63b13547f0> -> __attrs_140066151549632
                __attrs_140066151549632 = _static_140066151549296

                # <th ... (0:0)
                # --------------------------------------------------------
                __append('<th style="white-space: nowrap">')

                # <Symbol value=<DEFAULT> at 7f63b6853d30> -> __default_140066151548672
                __default_140066151548672 = _DEFAULT_MARKER

                # <Value 'item/date' (206:55)> -> __cache_140066151548192
                __token = 9385
                try:
                    __zt_tmp = __attrs_140066151549632
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140066151548192 = _static_140066241369744('path', 'item/date', econtext=econtext)(_static_140066241369456(econtext, __zt_tmp))

                # <BinOp left=<Value 'item/date' (206:55)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f63b6853d30> at 7f63b13545e0> -> __condition
                __expression = __cache_140066151548192

                # <Symbol value=<DEFAULT> at 7f63b6853d30> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('\n                                          Date\n                                      ')
                else:
                    __content = __cache_140066151548192
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</th>\n                                      ')

                # <Static value=<ast.Dict object at 0x7f63b68cea10> name=None at 7f63b68ced40> -> __attrs_140066151550592
                __attrs_140066151550592 = _static_140066241178128

                # <td ... (0:0)
                # --------------------------------------------------------
                __append('<td>\n                                        ')

                # <Static value=<ast.Dict object at 0x7f63b1355510> name=None at 7f63b1355540> -> __attrs_140066151552848
                __attrs_140066151552848 = _static_140066151552272

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a')

                # <Symbol value=<DEFAULT> at 7f63b6853d30> -> __default_140066151551888
                __default_140066151551888 = _DEFAULT_MARKER

                # <Substitution 'item/url' (212:64)> -> __attr_href
                __token = 9716
                try:
                    __zt_tmp = __attrs_140066151552848
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_140066241369744('path', 'item/url', econtext=econtext)(_static_140066241369456(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((' href="%s"' % __attr_href))
                __append('>')

                # <Symbol value=<DEFAULT> at 7f63b6853d30> -> __default_140066151551696
                __default_140066151551696 = _DEFAULT_MARKER

                # <Value 'item/title' (213:56)> -> __cache_140066151551216
                __token = 9782
                try:
                    __zt_tmp = __attrs_140066151552848
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140066151551216 = _static_140066241369744('path', 'item/title', econtext=econtext)(_static_140066241369456(econtext, __zt_tmp))

                # <BinOp left=<Value 'item/title' (213:56)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f63b6853d30> at 7f63b13551b0> -> __condition
                __expression = __cache_140066151551216

                # <Symbol value=<DEFAULT> at 7f63b6853d30> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('title')
                else:
                    __content = __cache_140066151551216
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</a>\n                                      </td>\n                                  </tr>\n                              ')
                ____index_140066151530160 -= 1
                if (____index_140066151530160 > 0):
                    __append('')
            if (__backup_item_140066151519600 is __marker):
                del econtext['item']
            else:
                econtext['item'] = __backup_item_140066151519600
            __append('\n                          </table>\n                          </div>')
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

            # <Static value=<ast.Dict object at 0x7f63b68cea10> name=None at 7f63b68ced40> -> __attrs_140066154066752
            __attrs_140066154066752 = _static_140066241178128
            __previous_i18n_domain_140066154067904 = __i18n_domain
            __i18n_domain = 'plone'
            __backup_macroname_140066225303104 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f63b15bb9a0> name=None at 7f63b15b9570> -> __value
            __value = _static_140066154068384
            econtext['macroname'] = __value

            def __fill_top_slot(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7f63b68cea10> name=None at 7f63b68ced40> -> __attrs_140066154067712
                __attrs_140066154067712 = _static_140066241178128
                __backup_dummy_140066154059312 = get('dummy', __marker)

                # <Value "python:request.set('disable_border',1)" (11:35)> -> __value
                __token = 408
                try:
                    __zt_tmp = __attrs_140066154067712
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140066241369744('python', "request.set('disable_border',1)", econtext=econtext)(_static_140066241369456(econtext, __zt_tmp))
                econtext['dummy'] = __value
                __backup_disable_column_one_140066154059552 = get('disable_column_one', __marker)

                # <Value "python:request.set('disable_plone.leftcolumn',1)" (12:47)> -> __value
                __token = 495
                try:
                    __zt_tmp = __attrs_140066154067712
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140066241369744('python', "request.set('disable_plone.leftcolumn',1)", econtext=econtext)(_static_140066241369456(econtext, __zt_tmp))
                econtext['disable_column_one'] = __value
                __backup_disable_column_two_140066154059792 = get('disable_column_two', __marker)

                # <Value "python:request.set('disable_plone.rightcolumn',1)" (13:46)> -> __value
                __token = 592
                try:
                    __zt_tmp = __attrs_140066154067712
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140066241369744('python', "request.set('disable_plone.rightcolumn',1)", econtext=econtext)(_static_140066241369456(econtext, __zt_tmp))
                econtext['disable_column_two'] = __value
                if (__backup_disable_column_two_140066154059792 is __marker):
                    del econtext['disable_column_two']
                else:
                    econtext['disable_column_two'] = __backup_disable_column_two_140066154059792
                if (__backup_disable_column_one_140066154059552 is __marker):
                    del econtext['disable_column_one']
                else:
                    econtext['disable_column_one'] = __backup_disable_column_one_140066154059552
                if (__backup_dummy_140066154059312 is __marker):
                    del econtext['dummy']
                else:
                    econtext['dummy'] = __backup_dummy_140066154059312
            _slots = econtext['__slot_top_slot'] = _deque((__fill_top_slot, ))

            def __fill_content(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7f63b68cea10> name=None at 7f63b68ced40> -> __attrs_140066154057200
                __attrs_140066154057200 = _static_140066241178128
                __append('\n    ')
                __token = None
                render_main(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append('\n\n')
            _slots = econtext['__slot_content'] = _deque((__fill_content, ))

            # <Value 'context/@@main_template/macros/master' (6:23)> -> __macro
            __token = 261
            try:
                __zt_tmp = __attrs_140066154066752
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140066241369744('path', 'context/@@main_template/macros/master', econtext=econtext)(_static_140066241369456(econtext, __zt_tmp))
            __token = 261
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140066225303104 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140066225303104
            __i18n_domain = __previous_i18n_domain_140066154067904
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_main': render_main, 'render_user_content_listing': render_user_content_listing, 'render': render, }