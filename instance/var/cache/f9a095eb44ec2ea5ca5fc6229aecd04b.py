# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/plone/app/layout/viewlets/dublin_core.pt'

__tokens = {25: ('view/metatags', 1, 25), 76: ('python:keyval[0]', 3, 13), 109: (' python:keyval[1', 4, 15)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139867356405408 = __C2ZContextWrapper
_static_139867356405696 = __compile_zt_expr
_static_139867202739056 = {'name': 'python:keyval[0]', 'content': 'python:keyval[1]', }

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

            # <Static value=<ast.Dict object at 0x7f355eef5b70> name=None at 7f355eef6410> -> __attrs_139867202221344
            __attrs_139867202221344 = _static_139867202739056
            __backup_keyval_139867202216016 = get('keyval', __marker)

            # <Value 'view/metatags' (1:25)> -> __iterator
            __token = 25
            try:
                __zt_tmp = __attrs_139867202221344
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_139867356405696('path', 'view/metatags', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            (__iterator, ____index_139867202211024, ) = getname('repeat')('keyval', __iterator)
            econtext['keyval'] = None
            for __item in __iterator:
                econtext['keyval'] = __item

                # <meta ... (0:0)
                # --------------------------------------------------------
                __append('<meta')

                # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867202741552
                __default_139867202741552 = _DEFAULT_MARKER

                # <Substitution 'python:keyval[0]' (3:13)> -> __attr_name
                __token = 76
                try:
                    __zt_tmp = __attrs_139867202221344
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_name = _static_139867356405696('python', 'keyval[0]', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_name is not None):
                    __append((' name="%s"' % __attr_name))

                # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867308452944
                __default_139867308452944 = _DEFAULT_MARKER

                # <Substitution 'python:keyval[1]' (4:15)> -> __attr_content
                __token = 109
                try:
                    __zt_tmp = __attrs_139867202221344
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_content = _static_139867356405696('python', 'keyval[1]', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                __attr_content = __quote(__attr_content, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_content is not None):
                    __append((' content="%s"' % __attr_content))
                __append(' />')
                ____index_139867202211024 -= 1
                if (____index_139867202211024 > 0):
                    __append('\n')
            if (__backup_keyval_139867202216016 is __marker):
                del econtext['keyval']
            else:
                econtext['keyval'] = __backup_keyval_139867202216016
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }