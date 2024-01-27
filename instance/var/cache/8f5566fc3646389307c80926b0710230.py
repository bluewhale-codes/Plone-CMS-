# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/plone/volto/browser/voltobackendwarning.pt'

__tokens = {33: ('nocall: context/@@iconresolver', 1, 33), 253: ("python:icons.tag('plone-statusmessage-warning', tag_alt='warning', tag_class='statusmessage-icon mb-1 me-2')", 6, 41)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139867198614656 = {'href': 'https://6.docs.plone.org/volto/index.html', }
_static_139867198607744 = {'href': 'https://6.docs.plone.org/install/install-from-packages.html', }
_static_139867200516592 = {'class': 'content', }
_static_139867200513568 = {'class': 'portalMessage statusmessage statusmessage-warning alert alert-warning', 'role': 'alert', }
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

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867200513856
            __attrs_139867200513856 = _static_139867362323344
            __backup_icons_139867200509680 = get('icons', __marker)

            # <Value 'nocall: context/@@iconresolver' (1:33)> -> __value
            __token = 33
            try:
                __zt_tmp = __attrs_139867200513856
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139867356405696('nocall', ' context/@@iconresolver', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            econtext['icons'] = __value
            __previous_i18n_domain_139867200507520 = __i18n_domain
            __i18n_domain = 'plone'
            __append('\n\n    ')

            # <Static value=<ast.Dict object at 0x7f355ecd6620> name=None at 7f355ecd7670> -> __attrs_139867200513088
            __attrs_139867200513088 = _static_139867200513568

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="portalMessage statusmessage statusmessage-warning alert alert-warning" role="alert">\n        ')

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867200512080
            __attrs_139867200512080 = _static_139867362323344

            # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867200513184
            __default_139867200513184 = _DEFAULT_MARKER

            # <Value "python:icons.tag('plone-statusmessage-warning', tag_alt='warning', tag_class='statusmessage-icon mb-1 me-2')" (6:41)> -> __cache_139867200518512
            __token = 253
            try:
                __zt_tmp = __attrs_139867200512080
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139867200518512 = _static_139867356405696('python', "icons.tag('plone-statusmessage-warning', tag_alt='warning', tag_class='statusmessage-icon mb-1 me-2')", econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))

            # <BinOp left=<Value "python:icons.tag('plone-statusmessage-warning', tag_alt='warning', tag_class='statusmessage-icon mb-1 me-2')" (6:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f3568756860> at 7f355ecd7790> -> __condition
            __expression = __cache_139867200518512

            # <Symbol value=<DEFAULT> at 7f3568756860> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_139867200518512
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n        ')

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867200514000
            __attrs_139867200514000 = _static_139867362323344

            # <strong ... (0:0)
            # --------------------------------------------------------
            __append('<strong>')
            __stream_139867200512416 = []
            __append_139867200512416 = __stream_139867200512416.append
            __append_139867200512416('Warning')
            __msgid_139867200512416 = __re_whitespace(''.join(__stream_139867200512416)).strip()
            if __msgid_139867200512416:
                __append(translate(__msgid_139867200512416, mapping=None, default=__msgid_139867200512416, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</strong>:\n        ')

            # <Static value=<ast.Dict object at 0x7f355ecd71f0> name=None at 7f355ecd6ce0> -> __attrs_139867200510256
            __attrs_139867200510256 = _static_139867200516592

            # <span ... (0:0)
            # --------------------------------------------------------
            __append('<span class="content">\n            ')

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867200507280
            __attrs_139867200507280 = _static_139867362323344
            __stream_139867200513952 = []
            __append_139867200513952 = __stream_139867200513952.append
            __append_139867200513952('You have accessed the Plone backend through its Classic UI frontend.')
            __msgid_139867200513952 = __re_whitespace(''.join(__stream_139867200513952)).strip()
            if 'volto_backend_warning':
                __append(translate('volto_backend_warning', mapping=None, default=__msgid_139867200513952, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('\n            ')

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867200510736
            __attrs_139867200510736 = _static_139867362323344

            # <br ... (0:0)
            # --------------------------------------------------------
            __append('<br />\n            ')

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867200507184
            __attrs_139867200507184 = _static_139867362323344

            # <br ... (0:0)
            # --------------------------------------------------------
            __append('<br />\n            ')

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867200519472
            __attrs_139867200519472 = _static_139867362323344
            __stream_139867200518224 = []
            __append_139867200518224 = __stream_139867200518224.append
            __append_139867200518224("If you want to use Plone's new frontend Volto instead:\n              ")

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867198610864
            __attrs_139867198610864 = _static_139867362323344

            # <ul ... (0:0)
            # --------------------------------------------------------
            __append_139867200518224('<ul>\n                ')

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867198614752
            __attrs_139867198614752 = _static_139867362323344

            # <li ... (0:0)
            # --------------------------------------------------------
            __append_139867200518224('<li>Install Volto, if not already installed.</li>\n                ')

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867198611680
            __attrs_139867198611680 = _static_139867362323344

            # <li ... (0:0)
            # --------------------------------------------------------
            __append_139867200518224('<li>Start Volto, if not already started.</li>\n                ')

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867198605824
            __attrs_139867198605824 = _static_139867362323344

            # <li ... (0:0)
            # --------------------------------------------------------
            __append_139867200518224('<li>Visit the Volto frontend.</li>\n              </ul>\n              For more information, please read the documentation for how to\n              ')

            # <Static value=<ast.Dict object at 0x7f355eb05180> name=None at 7f355eb06350> -> __attrs_139867198606976
            __attrs_139867198606976 = _static_139867198607744

            # <a ... (0:0)
            # --------------------------------------------------------
            __append_139867200518224('<a href="https://6.docs.plone.org/install/install-from-packages.html">Install Plone from its packages</a>\n              and refer to the full Volto documentation\n              ')

            # <Static value=<ast.Dict object at 0x7f355eb06c80> name=None at 7f355eb07cd0> -> __attrs_139867198608272
            __attrs_139867198608272 = _static_139867198614656

            # <a ... (0:0)
            # --------------------------------------------------------
            __append_139867200518224('<a href="https://6.docs.plone.org/volto/index.html">Frontend</a>.')
            __msgid_139867200518224 = __re_whitespace(''.join(__stream_139867200518224)).strip()
            if 'volto_backend_warning_link':
                __append(translate('volto_backend_warning_link', mapping=None, default=__msgid_139867200518224, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('\n        </span>\n    </div>\n\n')
            __i18n_domain = __previous_i18n_domain_139867200507520
            if (__backup_icons_139867200509680 is __marker):
                del econtext['icons']
            else:
                econtext['icons'] = __backup_icons_139867200509680
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }