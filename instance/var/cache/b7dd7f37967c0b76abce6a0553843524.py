# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/plone/app/layout/nextprevious/nextprevious.pt'

__tokens = {73: ('view/enabled|nothing', 3, 19), 120: (' view/isViewTemplate|nothin', 4, 25), 185: ('python:enabled and isViewTemplate', 6, 24), 300: ('view/site_url', 11, 26), 422: ('view/next', 16, 16), 452: (' view/previou', 17, 19), 503: ('python:previous is not None or next is not None', 19, 24), 696: ('previous', 24, 24), 748: ('previous/url', 26, 16), 1012: ('previous/title', 35, 29), 1240: ('next', 43, 24), 1288: ('next/url', 45, 16), 1500: ('next/title', 53, 29)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139867200371776 = {'class': 'arrow', }
_static_139867200367360 = {'class': 'label', }
_static_139867200371488 = {'class': 'btn btn-sm btn-outline-secondary align-self-end next', 'title': 'Go to next item', 'href': 'next/url', }
_static_139867202362320 = {'class': 'label', }
_static_139867202362704 = {'class': 'arrow', }
_static_139867202358144 = {'class': 'btn btn-sm btn-outline-secondary align-self-start previous', 'title': 'Go to previous item', 'href': 'previous/url', }
_static_139867202361744 = {'class': 'pagination justify-content-between', }
_static_139867362323344 = {}
_static_139867356405408 = __C2ZContextWrapper
_static_139867356405696 = __compile_zt_expr
_static_139867202369376 = {'id': 'section-next-prev', }

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

            # <Static value=<ast.Dict object at 0x7f355ee9b760> name=None at 7f355ee98220> -> __attrs_139867202356560
            __attrs_139867202356560 = _static_139867202369376
            __backup_enabled_139867200647952 = get('enabled', __marker)

            # <Value 'view/enabled|nothing' (3:19)> -> __value
            __token = 73
            try:
                __zt_tmp = __attrs_139867202356560
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139867356405696('path', 'view/enabled|nothing', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            econtext['enabled'] = __value
            __backup_isViewTemplate_139867200010464 = get('isViewTemplate', __marker)

            # <Value 'view/isViewTemplate|nothing' (4:25)> -> __value
            __token = 120
            try:
                __zt_tmp = __attrs_139867202356560
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139867356405696('path', 'view/isViewTemplate|nothing', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            econtext['isViewTemplate'] = __value

            # <Value 'python:enabled and isViewTemplate' (6:24)> -> __condition
            __token = 185
            try:
                __zt_tmp = __attrs_139867202356560
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_139867356405696('python', 'enabled and isViewTemplate', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_139867202367504 = __i18n_domain
                __i18n_domain = 'plone'

                # <section ... (0:0)
                # --------------------------------------------------------
                __append('<section id="section-next-prev" >\n\n  ')

                # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867202357664
                __attrs_139867202357664 = _static_139867362323344
                __backup_portal_url_139867200097776 = get('portal_url', __marker)

                # <Value 'view/site_url' (11:26)> -> __value
                __token = 300
                try:
                    __zt_tmp = __attrs_139867202357664
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139867356405696('path', 'view/site_url', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                econtext['portal_url'] = __value
                __append('\n\n    ')

                # <Static value=<ast.Dict object at 0x7f355ee99990> name=None at 7f355ee99360> -> __attrs_139867202358528
                __attrs_139867202358528 = _static_139867202361744
                __backup_next_139867199000240 = get('next', __marker)

                # <Value 'view/next' (16:16)> -> __value
                __token = 422
                try:
                    __zt_tmp = __attrs_139867202358528
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139867356405696('path', 'view/next', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                econtext['next'] = __value
                __backup_previous_139867199010320 = get('previous', __marker)

                # <Value 'view/previous' (17:19)> -> __value
                __token = 452
                try:
                    __zt_tmp = __attrs_139867202358528
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139867356405696('path', 'view/previous', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                econtext['previous'] = __value

                # <Value 'python:previous is not None or next is not None' (19:24)> -> __condition
                __token = 503
                try:
                    __zt_tmp = __attrs_139867202358528
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139867356405696('python', 'previous is not None or next is not None', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                if __condition:

                    # <nav ... (0:0)
                    # --------------------------------------------------------
                    __append('<nav class="pagination justify-content-between" >\n\n      ')

                    # <Static value=<ast.Dict object at 0x7f355ee98b80> name=None at 7f355ee98af0> -> __attrs_139867202356080
                    __attrs_139867202356080 = _static_139867202358144

                    # <Value 'previous' (24:24)> -> __condition
                    __token = 696
                    try:
                        __zt_tmp = __attrs_139867202356080
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_139867356405696('path', 'previous', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                    if __condition:

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append('<a class="btn btn-sm btn-outline-secondary align-self-start previous"')

                        # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867202361648
                        __default_139867202361648 = _DEFAULT_MARKER

                        # <Translate msgid='title_previous_item' node=<ast.Constant object at 0x7f355ee991b0> at 7f355ee98340> -> __attr_title
                        __attr_title = 'Go to previous item'
                        __attr_title = translate('title_previous_item', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        if (__attr_title is not None):
                            __append((' title="%s"' % __attr_title))

                        # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867202369904
                        __default_139867202369904 = _DEFAULT_MARKER

                        # <Substitution 'previous/url' (26:16)> -> __attr_href
                        __token = 748
                        try:
                            __zt_tmp = __attrs_139867202356080
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_139867356405696('path', 'previous/url', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((' href="%s"' % __attr_href))
                        __append(' >\n        ')

                        # <Static value=<ast.Dict object at 0x7f355ee99d50> name=None at 7f355ee9b430> -> __attrs_139867202367840
                        __attrs_139867202367840 = _static_139867202362704

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="arrow"></span>\n        ')

                        # <Static value=<ast.Dict object at 0x7f355ee99bd0> name=None at 7f355ee98d30> -> __attrs_139867200359584
                        __attrs_139867200359584 = _static_139867202362320

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="label" >')
                        __stream_139867199653696_itemtitle = ''
                        __stream_139867202368176 = []
                        __append_139867202368176 = __stream_139867202368176.append
                        __append_139867202368176('\n              Previous:\n          ')
                        __stream_139867199653696_itemtitle = []
                        __append_139867199653696_itemtitle = __stream_139867199653696_itemtitle.append

                        # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867200358912
                        __attrs_139867200358912 = _static_139867362323344

                        # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867200359824
                        __default_139867200359824 = _DEFAULT_MARKER

                        # <Value 'previous/title' (35:29)> -> __cache_139867200367552
                        __token = 1012
                        try:
                            __zt_tmp = __attrs_139867200358912
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_139867200367552 = _static_139867356405696('path', 'previous/title', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))

                        # <BinOp left=<Value 'previous/title' (35:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f3568756860> at 7f355ecb1c30> -> __condition
                        __expression = __cache_139867200367552

                        # <Symbol value=<DEFAULT> at 7f3568756860> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append_139867199653696_itemtitle('<span ></span>')
                        else:
                            __content = __cache_139867200367552
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append_139867199653696_itemtitle(__content)
                        __append_139867202368176('${itemtitle}')
                        __stream_139867199653696_itemtitle = ''.join(__stream_139867199653696_itemtitle)
                        __append_139867202368176('\n        ')
                        __msgid_139867202368176 = __re_whitespace(''.join(__stream_139867202368176)).strip()
                        if 'label_previous_item':
                            __append(translate('label_previous_item', mapping={'itemtitle': __stream_139867199653696_itemtitle, }, default=__msgid_139867202368176, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</span>\n      </a>')
                    __append('\n\n      ')

                    # <Static value=<ast.Dict object at 0x7f355ecb3b20> name=None at 7f355ecb09a0> -> __attrs_139867200369472
                    __attrs_139867200369472 = _static_139867200371488

                    # <Value 'next' (43:24)> -> __condition
                    __token = 1240
                    try:
                        __zt_tmp = __attrs_139867200369472
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_139867356405696('path', 'next', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                    if __condition:

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append('<a class="btn btn-sm btn-outline-secondary align-self-end next"')

                        # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867200359872
                        __default_139867200359872 = _DEFAULT_MARKER

                        # <Translate msgid='title_next_item' node=<ast.Constant object at 0x7f355ecb2050> at 7f355ecb3e50> -> __attr_title
                        __attr_title = 'Go to next item'
                        __attr_title = translate('title_next_item', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        if (__attr_title is not None):
                            __append((' title="%s"' % __attr_title))

                        # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867200366496
                        __default_139867200366496 = _DEFAULT_MARKER

                        # <Substitution 'next/url' (45:16)> -> __attr_href
                        __token = 1288
                        try:
                            __zt_tmp = __attrs_139867200369472
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_139867356405696('path', 'next/url', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((' href="%s"' % __attr_href))
                        __append(' >\n        ')

                        # <Static value=<ast.Dict object at 0x7f355ecb2b00> name=None at 7f355ecb1a50> -> __attrs_139867200358144
                        __attrs_139867200358144 = _static_139867200367360

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="label" >')
                        __stream_139867199654144_itemtitle = ''
                        __stream_139867200358240 = []
                        __append_139867200358240 = __stream_139867200358240.append
                        __append_139867200358240('\n              Next:\n          ')
                        __stream_139867199654144_itemtitle = []
                        __append_139867199654144_itemtitle = __stream_139867199654144_itemtitle.append

                        # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867200372064
                        __attrs_139867200372064 = _static_139867362323344

                        # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867200371104
                        __default_139867200371104 = _DEFAULT_MARKER

                        # <Value 'next/title' (53:29)> -> __cache_139867200365872
                        __token = 1500
                        try:
                            __zt_tmp = __attrs_139867200372064
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_139867200365872 = _static_139867356405696('path', 'next/title', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))

                        # <BinOp left=<Value 'next/title' (53:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f3568756860> at 7f355ecb22f0> -> __condition
                        __expression = __cache_139867200365872

                        # <Symbol value=<DEFAULT> at 7f3568756860> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append_139867199654144_itemtitle('<span ></span>')
                        else:
                            __content = __cache_139867200365872
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append_139867199654144_itemtitle(__content)
                        __append_139867200358240('${itemtitle}')
                        __stream_139867199654144_itemtitle = ''.join(__stream_139867199654144_itemtitle)
                        __append_139867200358240('\n        ')
                        __msgid_139867200358240 = __re_whitespace(''.join(__stream_139867200358240)).strip()
                        if 'label_next_item':
                            __append(translate('label_next_item', mapping={'itemtitle': __stream_139867199654144_itemtitle, }, default=__msgid_139867200358240, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</span>\n        ')

                        # <Static value=<ast.Dict object at 0x7f355ecb3c40> name=None at 7f355ecb2710> -> __attrs_139867200364000
                        __attrs_139867200364000 = _static_139867200371776

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="arrow"></span>\n      </a>')
                    __append('\n\n\n    </nav>')
                if (__backup_previous_139867199010320 is __marker):
                    del econtext['previous']
                else:
                    econtext['previous'] = __backup_previous_139867199010320
                if (__backup_next_139867199000240 is __marker):
                    del econtext['next']
                else:
                    econtext['next'] = __backup_next_139867199000240
                __append('\n\n  ')
                if (__backup_portal_url_139867200097776 is __marker):
                    del econtext['portal_url']
                else:
                    econtext['portal_url'] = __backup_portal_url_139867200097776
                __append('\n\n</section>')
                __i18n_domain = __previous_i18n_domain_139867202367504
            if (__backup_isViewTemplate_139867200010464 is __marker):
                del econtext['isViewTemplate']
            else:
                econtext['isViewTemplate'] = __backup_isViewTemplate_139867200010464
            if (__backup_enabled_139867200647952 is __marker):
                del econtext['enabled']
            else:
                econtext['enabled'] = __backup_enabled_139867200647952
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }