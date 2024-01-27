# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/plone/app/layout/viewlets/globalstatusmessage.pt'

__tokens = {51: ('nocall: context/@@iconresolver', 2, 23), 135: ('python:view.messages', 4, 35), 279: ('message/type | nothing', 10, 15), 324: (' python:view.display_info_for_mtype(mtype', 11, 21), 399: ('mtype', 13, 22), 174: ("portalMessage ${python:display_info['cssclass']}", 7, 14), 190: ("python:display_info['cssclass']", 7, 30), 447: ("python:icons.tag(display_info['icon'], tag_alt=display_info['msg'], tag_class='statusmessage-icon mb-1 me-2')", 15, 37), 573: ("${python:display_info['msg']}", 16, 12), 575: ("python:display_info['msg']", 16, 14), 661: ('message/message | nothing', 18, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139867199405984 = {'class': 'content', }
_static_139867199395040 = {'class': "portalMessage ${python:display_info['cssclass']}", 'role': 'alert', }
_static_139867356405408 = __C2ZContextWrapper
_static_139867356405696 = __compile_zt_expr
_static_139867362323344 = {}

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

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867199405840
            __attrs_139867199405840 = _static_139867362323344
            __backup_icons_139867199392352 = get('icons', __marker)

            # <Value 'nocall: context/@@iconresolver' (2:23)> -> __value
            __token = 51
            try:
                __zt_tmp = __attrs_139867199405840
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139867356405696('nocall', ' context/@@iconresolver', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            econtext['icons'] = __value
            __backup_message_139867199405552 = get('message', __marker)

            # <Value 'python:view.messages' (4:35)> -> __iterator
            __token = 135
            try:
                __zt_tmp = __attrs_139867199405840
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_139867356405696('python', 'view.messages', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            (__iterator, ____index_139867199405408, ) = getname('repeat')('message', __iterator)
            econtext['message'] = None
            for __item in __iterator:
                econtext['message'] = __item
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x7f355ebc54e0> name=None at 7f355ebc55a0> -> __attrs_139867199404304
                __attrs_139867199404304 = _static_139867199395040
                __backup_mtype_139867199402720 = get('mtype', __marker)

                # <Value 'message/type | nothing' (10:15)> -> __value
                __token = 279
                try:
                    __zt_tmp = __attrs_139867199404304
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139867356405696('path', 'message/type | nothing', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                econtext['mtype'] = __value
                __backup_display_info_139867199393312 = get('display_info', __marker)

                # <Value 'python:view.display_info_for_mtype(mtype)' (11:21)> -> __value
                __token = 324
                try:
                    __zt_tmp = __attrs_139867199404304
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139867356405696('python', 'view.display_info_for_mtype(mtype)', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                econtext['display_info'] = __value

                # <Value 'mtype' (13:22)> -> __condition
                __token = 399
                try:
                    __zt_tmp = __attrs_139867199404304
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139867356405696('path', 'mtype', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div')

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867199397728
                    __default_139867199397728 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution "portalMessage ${python:display_info['cssclass']}" (7:14)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f355ebc4df0> -> __attr_class
                    __token = 174
                    __token = 190
                    try:
                        __zt_tmp = __attrs_139867199404304
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_139867356405696('python', "display_info['cssclass']", econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    __attr_class = ('%s%s' % ('portalMessage ', (__attr_class if (__attr_class is not None) else ''), ))
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
                    __append(' role="alert" >\n    ')

                    # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867199400944
                    __attrs_139867199400944 = _static_139867362323344

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867199403872
                    __default_139867199403872 = _DEFAULT_MARKER

                    # <Value "python:icons.tag(display_info['icon'], tag_alt=display_info['msg'], tag_class='statusmessage-icon mb-1 me-2')" (15:37)> -> __cache_139867199390432
                    __token = 447
                    try:
                        __zt_tmp = __attrs_139867199400944
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139867199390432 = _static_139867356405696('python', "icons.tag(display_info['icon'], tag_alt=display_info['msg'], tag_class='statusmessage-icon mb-1 me-2')", econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))

                    # <BinOp left=<Value "python:icons.tag(display_info['icon'], tag_alt=display_info['msg'], tag_class='statusmessage-icon mb-1 me-2')" (15:37)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f3568756860> at 7f355ebc44f0> -> __condition
                    __expression = __cache_139867199390432

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_139867199390432
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('\n    ')

                    # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867199392400
                    __attrs_139867199392400 = _static_139867362323344

                    # <strong ... (0:0)
                    # --------------------------------------------------------
                    __append('<strong>')

                    # <Interpolation value=<Substitution "${python:display_info['msg']}" (16:12)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f355ebc6050> -> __content_139867442113136
                    __token = 573
                    __token = 575
                    try:
                        __zt_tmp = __attrs_139867199392400
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __content_139867442113136 = _static_139867356405696('python', "display_info['msg']", econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                    __content_139867442113136 = __quote(__content_139867442113136, '\x00', '&#0;', None, None)
                    __content_139867442113136 = __content_139867442113136
                    if (__content_139867442113136 is None):
                        pass
                    else:
                        if (__content_139867442113136 is None):
                            __content_139867442113136 = None
                        else:
                            __tt = type(__content_139867442113136)
                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                __content_139867442113136 = str(__content_139867442113136)
                            else:
                                if (__tt is bytes):
                                    __content_139867442113136 = decode(__content_139867442113136)
                                else:
                                    if (__tt is not str):
                                        try:
                                            __content_139867442113136 = __content_139867442113136.__html__
                                        except get('AttributeError', AttributeError):
                                            __converted = convert(__content_139867442113136)
                                            __content_139867442113136 = (str(__content_139867442113136) if (__content_139867442113136 is __converted) else __converted)
                                        else:
                                            __content_139867442113136 = __content_139867442113136()
                    if (__content_139867442113136 is not None):
                        __append(__content_139867442113136)
                    __append('</strong>\n    ')

                    # <Static value=<ast.Dict object at 0x7f355ebc7fa0> name=None at 7f355ebc44c0> -> __attrs_139867199402768
                    __attrs_139867199402768 = _static_139867199405984

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867199400800
                    __default_139867199400800 = _DEFAULT_MARKER

                    # <Value 'message/message | nothing' (18:23)> -> __cache_139867199400752
                    __token = 661
                    try:
                        __zt_tmp = __attrs_139867199402768
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139867199400752 = _static_139867356405696('path', 'message/message | nothing', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))

                    # <BinOp left=<Value 'message/message | nothing' (18:23)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f3568756860> at 7f355ebc7d90> -> __condition
                    __expression = __cache_139867199400752

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="content" >\n            The status message.\n    </span>')
                    else:
                        __content = __cache_139867199400752
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('\n  </div>')
                if (__backup_display_info_139867199393312 is __marker):
                    del econtext['display_info']
                else:
                    econtext['display_info'] = __backup_display_info_139867199393312
                if (__backup_mtype_139867199402720 is __marker):
                    del econtext['mtype']
                else:
                    econtext['mtype'] = __backup_mtype_139867199402720
                __append('\n\n')
                ____index_139867199405408 -= 1
                if (____index_139867199405408 > 0):
                    __append('')
            if (__backup_message_139867199405552 is __marker):
                del econtext['message']
            else:
                econtext['message'] = __backup_message_139867199405552
            if (__backup_icons_139867199392352 is __marker):
                del econtext['icons']
            else:
                econtext['icons'] = __backup_icons_139867199392352
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }