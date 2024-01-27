# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/plone/app/layout/viewlets/document_rights.pt'

__tokens = {97: ('context/Rights', 4, 18), 148: ('rights', 6, 24), 324: ('rights', 16, 22)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139867362323344 = {}
_static_139867202249264 = {'class': 'section-heading', }
_static_139867356405408 = __C2ZContextWrapper
_static_139867356405696 = __compile_zt_expr
_static_139867202255408 = {'class': 'text-muted', 'id': 'section-rights', }

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

            # <Static value=<ast.Dict object at 0x7f355ee7fa30> name=None at 7f355ee7e350> -> __attrs_139867202247632
            __attrs_139867202247632 = _static_139867202255408
            __backup_rights_139867199456448 = get('rights', __marker)

            # <Value 'context/Rights' (4:18)> -> __value
            __token = 97
            try:
                __zt_tmp = __attrs_139867202247632
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139867356405696('path', 'context/Rights', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            econtext['rights'] = __value

            # <Value 'rights' (6:24)> -> __condition
            __token = 148
            try:
                __zt_tmp = __attrs_139867202247632
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_139867356405696('path', 'rights', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_139867202253488 = __i18n_domain
                __i18n_domain = 'plone'

                # <section ... (0:0)
                # --------------------------------------------------------
                __append('<section class="text-muted" id="section-rights" >\n\n  ')

                # <Static value=<ast.Dict object at 0x7f355ee7e230> name=None at 7f355ee7f6d0> -> __attrs_139867202252432
                __attrs_139867202252432 = _static_139867202249264

                # <header ... (0:0)
                # --------------------------------------------------------
                __append('<header class="section-heading" >')
                __stream_139867202249456 = []
                __append_139867202249456 = __stream_139867202249456.append
                __append_139867202249456('\n      Rights\n  ')
                __msgid_139867202249456 = __re_whitespace(''.join(__stream_139867202249456)).strip()
                if 'section_rights_heading':
                    __append(translate('section_rights_heading', mapping=None, default=__msgid_139867202249456, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</header>\n\n  ')

                # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867202255888
                __attrs_139867202255888 = _static_139867362323344

                # <small ... (0:0)
                # --------------------------------------------------------
                __append('<small>')

                # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867202256512
                __default_139867202256512 = _DEFAULT_MARKER

                # <Value 'rights' (16:22)> -> __cache_139867202253968
                __token = 324
                try:
                    __zt_tmp = __attrs_139867202255888
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_139867202253968 = _static_139867356405696('path', 'rights', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))

                # <BinOp left=<Value 'rights' (16:22)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f3568756860> at 7f355ee7f4f0> -> __condition
                __expression = __cache_139867202253968

                # <Symbol value=<DEFAULT> at 7f3568756860> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('Copyleft NiceCorp Inc.')
                else:
                    __content = __cache_139867202253968
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</small>\n\n</section>')
                __i18n_domain = __previous_i18n_domain_139867202253488
            if (__backup_rights_139867199456448 is __marker):
                del econtext['rights']
            else:
                econtext['rights'] = __backup_rights_139867199456448
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }