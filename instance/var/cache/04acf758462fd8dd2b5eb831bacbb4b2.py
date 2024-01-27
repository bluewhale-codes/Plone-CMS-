# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/plone/app/layout/viewlets/toc.pt'

__tokens = {135: ('view/enabled', 5, 24)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info

_static_139867200536528 = {'class': 'portletItem', }
_static_139867200525248 = {'class': 'portletContent', }
_static_139867200536336 = {'class': 'portletHeader', }
_static_139867356405408 = __C2ZContextWrapper
_static_139867356405696 = __compile_zt_expr
_static_139867200529232 = {'class': 'portlet toc', 'id': 'document-toc', 'role': 'section', 'style': 'display: none', }

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

            # <Static value=<ast.Dict object at 0x7f355ecda350> name=None at 7f355ecd95a0> -> __attrs_139867200534944
            __attrs_139867200534944 = _static_139867200529232

            # <Value 'view/enabled' (5:24)> -> __condition
            __token = 135
            try:
                __zt_tmp = __attrs_139867200534944
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_139867356405696('path', 'view/enabled', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_139867200525296 = __i18n_domain
                __i18n_domain = 'plone'

                # <section ... (0:0)
                # --------------------------------------------------------
                __append('<section class="portlet toc" id="document-toc" role="section" style="display: none" >\n  ')

                # <Static value=<ast.Dict object at 0x7f355ecdbf10> name=None at 7f355ecd9480> -> __attrs_139867200529760
                __attrs_139867200529760 = _static_139867200536336

                # <header ... (0:0)
                # --------------------------------------------------------
                __append('<header class="portletHeader" >')
                __stream_139867200520688 = []
                __append_139867200520688 = __stream_139867200520688.append
                __append_139867200520688('Contents')
                __msgid_139867200520688 = __re_whitespace(''.join(__stream_139867200520688)).strip()
                if 'label_tableofcontents':
                    __append(translate('label_tableofcontents', mapping=None, default=__msgid_139867200520688, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</header>\n  ')

                # <Static value=<ast.Dict object at 0x7f355ecd93c0> name=None at 7f355ecdacb0> -> __attrs_139867200533600
                __attrs_139867200533600 = _static_139867200525248

                # <section ... (0:0)
                # --------------------------------------------------------
                __append('<section class="portletContent">\n    ')

                # <Static value=<ast.Dict object at 0x7f355ecdbfd0> name=None at 7f355ecdbf70> -> __attrs_139867200531536
                __attrs_139867200531536 = _static_139867200536528

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="portletItem">\n    </div>\n  </section>\n</section>')
                __i18n_domain = __previous_i18n_domain_139867200525296
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }