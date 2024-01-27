# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/plone/locking/browser/info.pt'

__tokens = {60: ('view/info/is_locked_for_current_user', 3, 14), 114: (' view/lock_is_stealabl', 4, 16), 157: ('s view/lock_in', 5, 18), 185: ("ns python:context.restrictedTraverse('@@iconresolve", 6, 10), 299: ('locked', 10, 24), 401: ("python:icons.tag('lock-fill', tag_alt='locked', tag_class='mb-1 me-2')", 12, 39), 574: ('lock_details/author_page', 14, 38), 819: ('lock_details/author_page', 20, 18), 750: ('lock_details/fullname', 18, 24), 929: ('lock_details/time_difference', 24, 27), 1087: ('not:lock_details/author_page', 29, 41), 1273: ('lock_details/fullname', 33, 27), 1373: ('lock_details/time_difference', 36, 27), 1546: ('stealable', 42, 27), 1607: ('string:${context/absolute_url}/@@plone_lock_operations/force_unlock', 44, 21)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139867202241872 = {'type': 'submit', 'value': 'Unlock', }
_static_139867199398592 = {'method': 'POST', 'action': 'string:${context/absolute_url}/@@plone_lock_operations/force_unlock', }
_static_139867199391200 = {'href': 'lock_details/author_page', }
_static_139867199390048 = {'class': 'portalMessage info alert alert-info', }
_static_139867362323344 = {}
_static_139867356405408 = __C2ZContextWrapper
_static_139867356405696 = __compile_zt_expr
_static_139867199160912 = {'id': 'plone-lock-status', }

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

            # <Static value=<ast.Dict object at 0x7f355eb8c250> name=None at 7f355eb8ee30> -> __attrs_139867199163600
            __attrs_139867199163600 = _static_139867199160912
            __backup_locked_139867199390384 = get('locked', __marker)

            # <Value 'view/info/is_locked_for_current_user' (3:14)> -> __value
            __token = 60
            try:
                __zt_tmp = __attrs_139867199163600
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139867356405696('path', 'view/info/is_locked_for_current_user', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            econtext['locked'] = __value
            __backup_stealable_139867199396240 = get('stealable', __marker)

            # <Value 'view/lock_is_stealable' (4:16)> -> __value
            __token = 114
            try:
                __zt_tmp = __attrs_139867199163600
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139867356405696('path', 'view/lock_is_stealable', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            econtext['stealable'] = __value
            __backup_lock_details_139867199455392 = get('lock_details', __marker)

            # <Value 'view/lock_info' (5:18)> -> __value
            __token = 157
            try:
                __zt_tmp = __attrs_139867199163600
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139867356405696('path', 'view/lock_info', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            econtext['lock_details'] = __value
            __backup_icons_139867199949936 = get('icons', __marker)

            # <Value "python:context.restrictedTraverse('@@iconresolver')" (6:10)> -> __value
            __token = 185
            try:
                __zt_tmp = __attrs_139867199163600
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139867356405696('python', "context.restrictedTraverse('@@iconresolver')", econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            econtext['icons'] = __value
            __previous_i18n_domain_139867199173104 = __i18n_domain
            __i18n_domain = 'plone'

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div id="plone-lock-status" >\n  ')

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867199400752
            __attrs_139867199400752 = _static_139867362323344

            # <Value 'locked' (10:24)> -> __condition
            __token = 299
            try:
                __zt_tmp = __attrs_139867199400752
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_139867356405696('path', 'locked', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            if __condition:
                __append('\n    ')

                # <Static value=<ast.Dict object at 0x7f355ebc4160> name=None at 7f355ebc6080> -> __attrs_139867199405744
                __attrs_139867199405744 = _static_139867199390048

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="portalMessage info alert alert-info">\n      ')

                # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867199396720
                __attrs_139867199396720 = _static_139867362323344

                # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867199394416
                __default_139867199394416 = _DEFAULT_MARKER

                # <Value "python:icons.tag('lock-fill', tag_alt='locked', tag_class='mb-1 me-2')" (12:39)> -> __cache_139867199400512
                __token = 401
                try:
                    __zt_tmp = __attrs_139867199396720
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_139867199400512 = _static_139867356405696('python', "icons.tag('lock-fill', tag_alt='locked', tag_class='mb-1 me-2')", econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))

                # <BinOp left=<Value "python:icons.tag('lock-fill', tag_alt='locked', tag_class='mb-1 me-2')" (12:39)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f3568756860> at 7f355ebc7a60> -> __condition
                __expression = __cache_139867199400512

                # <Symbol value=<DEFAULT> at 7f3568756860> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_139867199400512
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n      ')

                # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867199393600
                __attrs_139867199393600 = _static_139867362323344

                # <strong ... (0:0)
                # --------------------------------------------------------
                __append('<strong>')
                __stream_139867199400848 = []
                __append_139867199400848 = __stream_139867199400848.append
                __append_139867199400848('Locked')
                __msgid_139867199400848 = __re_whitespace(''.join(__stream_139867199400848)).strip()
                if 'label_locked':
                    __append(translate('label_locked', mapping=None, default=__msgid_139867199400848, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</strong>\n      ')

                # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867199406032
                __attrs_139867199406032 = _static_139867362323344

                # <Value 'lock_details/author_page' (14:38)> -> __condition
                __token = 574
                try:
                    __zt_tmp = __attrs_139867199406032
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139867356405696('path', 'lock_details/author_page', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                if __condition:
                    __stream_139867198903616_author = ''
                    __stream_139867198903616_time = ''
                    __stream_139867199402960 = []
                    __append_139867199402960 = __stream_139867199402960.append
                    __append_139867199402960('\n          This item was locked by\n        ')
                    __stream_139867198903616_author = []
                    __append_139867198903616_author = __stream_139867198903616_author.append

                    # <Static value=<ast.Dict object at 0x7f355ebc45e0> name=None at 7f355ebc48b0> -> __attrs_139867199394992
                    __attrs_139867199394992 = _static_139867199391200

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append_139867198903616_author('<a')

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867199399264
                    __default_139867199399264 = _DEFAULT_MARKER

                    # <Substitution 'lock_details/author_page' (20:18)> -> __attr_href
                    __token = 819
                    try:
                        __zt_tmp = __attrs_139867199394992
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_139867356405696('path', 'lock_details/author_page', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append_139867198903616_author((' href="%s"' % __attr_href))
                    __append_139867198903616_author(' >')

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867199402096
                    __default_139867199402096 = _DEFAULT_MARKER

                    # <Value 'lock_details/fullname' (18:24)> -> __cache_139867199395232
                    __token = 750
                    try:
                        __zt_tmp = __attrs_139867199394992
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139867199395232 = _static_139867356405696('path', 'lock_details/fullname', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))

                    # <BinOp left=<Value 'lock_details/fullname' (18:24)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f3568756860> at 7f355ebc4d30> -> __condition
                    __expression = __cache_139867199395232

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_139867199395232
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append_139867198903616_author(__content)
                    __append_139867198903616_author('</a>')
                    __append_139867199402960('${author}')
                    __stream_139867198903616_author = ''.join(__stream_139867198903616_author)
                    __append_139867199402960('\n        ')
                    __stream_139867198903616_time = []
                    __append_139867198903616_time = __stream_139867198903616_time.append

                    # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867199396432
                    __attrs_139867199396432 = _static_139867362323344

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append_139867198903616_time('<span >')

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867199404160
                    __default_139867199404160 = _DEFAULT_MARKER

                    # <Value 'lock_details/time_difference' (24:27)> -> __cache_139867199399312
                    __token = 929
                    try:
                        __zt_tmp = __attrs_139867199396432
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139867199399312 = _static_139867356405696('path', 'lock_details/time_difference', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))

                    # <BinOp left=<Value 'lock_details/time_difference' (24:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f3568756860> at 7f355ebc5120> -> __condition
                    __expression = __cache_139867199399312

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_139867199399312
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append_139867198903616_time(__content)
                    __append_139867198903616_time('</span>')
                    __append_139867199402960('${time}')
                    __stream_139867198903616_time = ''.join(__stream_139867198903616_time)
                    __append_139867199402960('\n         ago.\n      ')
                    __msgid_139867199402960 = __re_whitespace(''.join(__stream_139867199402960)).strip()
                    if 'description_webdav_locked_by_author_on_time':
                        __append(translate('description_webdav_locked_by_author_on_time', mapping={'time': __stream_139867198903616_time, 'author': __stream_139867198903616_author, }, default=__msgid_139867199402960, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('\n      ')

                # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867199393744
                __attrs_139867199393744 = _static_139867362323344

                # <Value 'not:lock_details/author_page' (29:41)> -> __condition
                __token = 1087
                try:
                    __zt_tmp = __attrs_139867199393744
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139867356405696('not', 'lock_details/author_page', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                if __condition:
                    __stream_139867198903616_author = ''
                    __stream_139867198903616_time = ''
                    __stream_139867199397296 = []
                    __append_139867199397296 = __stream_139867199397296.append
                    __append_139867199397296('\n          This item was locked by\n        ')
                    __stream_139867198903616_author = []
                    __append_139867198903616_author = __stream_139867198903616_author.append

                    # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867202255120
                    __attrs_139867202255120 = _static_139867362323344

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append_139867198903616_author('<span >')

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867202246768
                    __default_139867202246768 = _DEFAULT_MARKER

                    # <Value 'lock_details/fullname' (33:27)> -> __cache_139867199391536
                    __token = 1273
                    try:
                        __zt_tmp = __attrs_139867202255120
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139867199391536 = _static_139867356405696('path', 'lock_details/fullname', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))

                    # <BinOp left=<Value 'lock_details/fullname' (33:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f3568756860> at 7f355ebc7250> -> __condition
                    __expression = __cache_139867199391536

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_139867199391536
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append_139867198903616_author(__content)
                    __append_139867198903616_author('</span>')
                    __append_139867199397296('${author}')
                    __stream_139867198903616_author = ''.join(__stream_139867198903616_author)
                    __append_139867199397296('\n        ')
                    __stream_139867198903616_time = []
                    __append_139867198903616_time = __stream_139867198903616_time.append

                    # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867202252432
                    __attrs_139867202252432 = _static_139867362323344

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append_139867198903616_time('<span >')

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867202247584
                    __default_139867202247584 = _DEFAULT_MARKER

                    # <Value 'lock_details/time_difference' (36:27)> -> __cache_139867202241392
                    __token = 1373
                    try:
                        __zt_tmp = __attrs_139867202252432
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139867202241392 = _static_139867356405696('path', 'lock_details/time_difference', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))

                    # <BinOp left=<Value 'lock_details/time_difference' (36:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f3568756860> at 7f355ee7dd20> -> __condition
                    __expression = __cache_139867202241392

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_139867202241392
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append_139867198903616_time(__content)
                    __append_139867198903616_time('</span>')
                    __append_139867199397296('${time}')
                    __stream_139867198903616_time = ''.join(__stream_139867198903616_time)
                    __append_139867199397296('\n         ago.\n      ')
                    __msgid_139867199397296 = __re_whitespace(''.join(__stream_139867199397296)).strip()
                    if 'description_webdav_locked_by_author_on_time':
                        __append(translate('description_webdav_locked_by_author_on_time', mapping={'time': __stream_139867198903616_time, 'author': __stream_139867198903616_author, }, default=__msgid_139867199397296, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('\n      ')

                # <Static value=<ast.Dict object at 0x7f355ebc62c0> name=None at 7f355ebc4100> -> __attrs_139867202251520
                __attrs_139867202251520 = _static_139867199398592

                # <Value 'stealable' (42:27)> -> __condition
                __token = 1546
                try:
                    __zt_tmp = __attrs_139867202251520
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139867356405696('path', 'stealable', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                if __condition:

                    # <form ... (0:0)
                    # --------------------------------------------------------
                    __append('<form method="POST"')

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867202244560
                    __default_139867202244560 = _DEFAULT_MARKER

                    # <Substitution 'string:${context/absolute_url}/@@plone_lock_operations/force_unlock' (44:21)> -> __attr_action
                    __token = 1607
                    try:
                        __zt_tmp = __attrs_139867202251520
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_action = _static_139867356405696('string', '${context/absolute_url}/@@plone_lock_operations/force_unlock', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                    __attr_action = __quote(__attr_action, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_action is not None):
                        __append((' action="%s"' % __attr_action))
                    __append(' >\n        ')

                    # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867202242304
                    __attrs_139867202242304 = _static_139867362323344

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>')
                    __stream_139867198903392_unlock_button = ''
                    __stream_139867202244368 = []
                    __append_139867202244368 = __stream_139867202244368.append
                    __append_139867202244368('\n            If you are certain this user has abandoned the object,\n            you may\n          ')
                    __stream_139867198903392_unlock_button = []
                    __append_139867198903392_unlock_button = __stream_139867198903392_unlock_button.append

                    # <Static value=<ast.Dict object at 0x7f355ee7c550> name=None at 7f355ee7dff0> -> __attrs_139867202252864
                    __attrs_139867202252864 = _static_139867202241872

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append_139867198903392_unlock_button('<input type="submit"')

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867202250752
                    __default_139867202250752 = _DEFAULT_MARKER

                    # <Translate msgid=None node=<ast.Constant object at 0x7f355ee7d0c0> at 7f355ee7ce80> -> __attr_value
                    __attr_value = 'Unlock'
                    __attr_value = translate(__attr_value, default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    if (__attr_value is not None):
                        __append_139867198903392_unlock_button((' value="%s"' % __attr_value))
                    __append_139867198903392_unlock_button(' />')
                    __append_139867202244368('${unlock_button}')
                    __stream_139867198903392_unlock_button = ''.join(__stream_139867198903392_unlock_button)
                    __append_139867202244368('\n            the object. You will then be able to edit it.\n        ')
                    __msgid_139867202244368 = __re_whitespace(''.join(__stream_139867202244368)).strip()
                    if 'description_webdav_locked_steal':
                        __append(translate('description_webdav_locked_steal', mapping={'unlock_button': __stream_139867198903392_unlock_button, }, default=__msgid_139867202244368, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</span>\n      </form>')
                __append('\n    </div>\n  ')
            __append('\n</div>')
            __i18n_domain = __previous_i18n_domain_139867199173104
            if (__backup_icons_139867199949936 is __marker):
                del econtext['icons']
            else:
                econtext['icons'] = __backup_icons_139867199949936
            if (__backup_lock_details_139867199455392 is __marker):
                del econtext['lock_details']
            else:
                econtext['lock_details'] = __backup_lock_details_139867199455392
            if (__backup_stealable_139867199396240 is __marker):
                del econtext['stealable']
            else:
                econtext['stealable'] = __backup_stealable_139867199396240
            if (__backup_locked_139867199390384 is __marker):
                del econtext['locked']
            else:
                econtext['locked'] = __backup_locked_139867199390384
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }