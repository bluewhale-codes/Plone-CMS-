# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/plone/app/layout/viewlets/sections.pt'

__tokens = {218: ('python:view.navtree', 4, 29), 369: ('python:view.render_globalnav()', 11, 36)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139867200645408 = {'class': 'navbar-toggler-icon', }
_static_139867200643632 = {'class': 'navbar-toggler', 'aria-label': 'Toggle navigation', 'type': 'button', }
_static_139867200649440 = {'class': 'navbar-nav', 'id': 'portal-globalnav', }
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

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867200643536
            __attrs_139867200643536 = _static_139867362323344

            # <Value 'python:view.navtree' (4:29)> -> __condition
            __token = 218
            try:
                __zt_tmp = __attrs_139867200643536
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_139867356405696('python', 'view.navtree', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_139867200648000 = __i18n_domain
                __i18n_domain = 'plone'
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x7f355ecf78e0> name=None at 7f355ecf4d30> -> __attrs_139867200647328
                __attrs_139867200647328 = _static_139867200649440

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append('<ul class="navbar-nav" id="portal-globalnav" >\n    ')

                # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867200640944
                __attrs_139867200640944 = _static_139867362323344

                # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867200643824
                __default_139867200643824 = _DEFAULT_MARKER

                # <Value 'python:view.render_globalnav()' (11:36)> -> __cache_139867200641088
                __token = 369
                try:
                    __zt_tmp = __attrs_139867200640944
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_139867200641088 = _static_139867356405696('python', 'view.render_globalnav()', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))

                # <BinOp left=<Value 'python:view.render_globalnav()' (11:36)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f3568756860> at 7f355ecf5570> -> __condition
                __expression = __cache_139867200641088

                # <Symbol value=<DEFAULT> at 7f3568756860> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <navtree ... (0:0)
                    # --------------------------------------------------------
                    __append('<navtree></navtree>')
                else:
                    __content = __cache_139867200641088
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n  </ul>\n\n  ')

                # <Static value=<ast.Dict object at 0x7f355ecf6230> name=None at 7f355ecf4460> -> __attrs_139867200640752
                __attrs_139867200640752 = _static_139867200643632

                # <button ... (0:0)
                # --------------------------------------------------------
                __append('<button class="navbar-toggler"')

                # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867200644640
                __default_139867200644640 = _DEFAULT_MARKER

                # <Translate msgid='label_toggle_navigation' node=<ast.Constant object at 0x7f355ecf6c50> at 7f355ecf59f0> -> __attr_aria_label
                __attr_aria_label = 'Toggle navigation'
                __attr_aria_label = translate('label_toggle_navigation', default=__attr_aria_label, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                if (__attr_aria_label is not None):
                    __append((' aria-label="%s"' % __attr_aria_label))
                __append(' type="button" >\n    ')

                # <Static value=<ast.Dict object at 0x7f355ecf6920> name=None at 7f355ecf4760> -> __attrs_139867200635952
                __attrs_139867200635952 = _static_139867200645408

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span class="navbar-toggler-icon"></span>\n  </button>\n\n')
                __i18n_domain = __previous_i18n_domain_139867200648000
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }