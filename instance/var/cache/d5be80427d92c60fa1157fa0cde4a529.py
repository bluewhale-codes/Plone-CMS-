# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/plone/app/layout/nextprevious/links.pt'

__tokens = {181: ('view/enabled|nothing', 5, 15), 224: (' view/isViewTemplate|nothin', 6, 21), 281: ('python:enabled and isViewTemplate', 8, 20), 455: ('view/previous', 16, 19), 503: ('previous', 18, 23), 553: ('previous/url', 20, 15), 738: ('view/next', 29, 15), 782: ('next', 31, 23), 828: ('next/url', 33, 15)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139867202361984 = {'href': '', 'rel': 'next', 'title': 'Go to next item', }
_static_139867202496032 = {'href': '', 'rel': 'previous', 'title': 'Go to previous item', }
_static_139867356405408 = __C2ZContextWrapper
_static_139867356405696 = __compile_zt_expr
_static_139867202212416 = {'xmlns': 'http://www.w3.org/1999/xhtml', }

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

            # <Static value=<ast.Dict object at 0x7f355ee75240> name=None at 7f355ee76aa0> -> __attrs_139867202499392
            __attrs_139867202499392 = _static_139867202212416
            __backup_enabled_139867202215152 = get('enabled', __marker)

            # <Value 'view/enabled|nothing' (5:15)> -> __value
            __token = 181
            try:
                __zt_tmp = __attrs_139867202499392
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139867356405696('path', 'view/enabled|nothing', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            econtext['enabled'] = __value
            __backup_isViewTemplate_139867202229856 = get('isViewTemplate', __marker)

            # <Value 'view/isViewTemplate|nothing' (6:21)> -> __value
            __token = 224
            try:
                __zt_tmp = __attrs_139867202499392
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139867356405696('path', 'view/isViewTemplate|nothing', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            econtext['isViewTemplate'] = __value

            # <Value 'python:enabled and isViewTemplate' (8:20)> -> __condition
            __token = 281
            try:
                __zt_tmp = __attrs_139867202499392
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_139867356405696('python', 'enabled and isViewTemplate', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            if __condition:
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x7f355eeba620> name=None at 7f355eebad10> -> __attrs_139867202367456
                __attrs_139867202367456 = _static_139867202496032
                __backup_previous_139867202238016 = get('previous', __marker)

                # <Value 'view/previous' (16:19)> -> __value
                __token = 455
                try:
                    __zt_tmp = __attrs_139867202367456
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139867356405696('path', 'view/previous', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                econtext['previous'] = __value

                # <Value 'previous' (18:23)> -> __condition
                __token = 503
                try:
                    __zt_tmp = __attrs_139867202367456
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139867356405696('path', 'previous', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                if __condition:

                    # <link ... (0:0)
                    # --------------------------------------------------------
                    __append('<link')

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867202363664
                    __default_139867202363664 = _DEFAULT_MARKER

                    # <Substitution 'previous/url' (20:15)> -> __attr_href
                    __token = 553
                    try:
                        __zt_tmp = __attrs_139867202367456
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_139867356405696('path', 'previous/url', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))
                    __append(' rel="previous"')

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867202362368
                    __default_139867202362368 = _DEFAULT_MARKER

                    # <Translate msgid='title_previous_item' node=<ast.Constant object at 0x7f355ee9bf70> at 7f355ee98d00> -> __attr_title
                    __attr_title = 'Go to previous item'
                    __attr_title = translate('title_previous_item', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    if (__attr_title is not None):
                        __append((' title="%s"' % __attr_title))
                    __append(' />')
                if (__backup_previous_139867202238016 is __marker):
                    del econtext['previous']
                else:
                    econtext['previous'] = __backup_previous_139867202238016
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x7f355ee99a80> name=None at 7f355ee9b3d0> -> __attrs_139867202365488
                __attrs_139867202365488 = _static_139867202361984
                __backup_next_139867202224960 = get('next', __marker)

                # <Value 'view/next' (29:15)> -> __value
                __token = 738
                try:
                    __zt_tmp = __attrs_139867202365488
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139867356405696('path', 'view/next', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                econtext['next'] = __value

                # <Value 'next' (31:23)> -> __condition
                __token = 782
                try:
                    __zt_tmp = __attrs_139867202365488
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139867356405696('path', 'next', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                if __condition:

                    # <link ... (0:0)
                    # --------------------------------------------------------
                    __append('<link')

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867202355264
                    __default_139867202355264 = _DEFAULT_MARKER

                    # <Substitution 'next/url' (33:15)> -> __attr_href
                    __token = 828
                    try:
                        __zt_tmp = __attrs_139867202365488
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_139867356405696('path', 'next/url', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))
                    __append(' rel="next"')

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867202362512
                    __default_139867202362512 = _DEFAULT_MARKER

                    # <Translate msgid='title_next_item' node=<ast.Constant object at 0x7f355ee994e0> at 7f355ee9b580> -> __attr_title
                    __attr_title = 'Go to next item'
                    __attr_title = translate('title_next_item', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    if (__attr_title is not None):
                        __append((' title="%s"' % __attr_title))
                    __append(' />')
                if (__backup_next_139867202224960 is __marker):
                    del econtext['next']
                else:
                    econtext['next'] = __backup_next_139867202224960
                __append('\n\n')
            if (__backup_isViewTemplate_139867202229856 is __marker):
                del econtext['isViewTemplate']
            else:
                econtext['isViewTemplate'] = __backup_isViewTemplate_139867202229856
            if (__backup_enabled_139867202215152 is __marker):
                del econtext['enabled']
            else:
                econtext['enabled'] = __backup_enabled_139867202215152
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }