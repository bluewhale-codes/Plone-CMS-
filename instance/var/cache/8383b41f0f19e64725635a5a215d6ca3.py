# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/plone/app/contenttypes/behaviors/leadimage.pt'

__tokens = {56: ('view/available', 2, 24), 153: ('context/@@images', 6, 19), 219: ("python: images.tag('image', scale='large', css_class='figure-img img-fluid')", 9, 32), 370: ("python: getattr(context, 'image_caption', None)", 11, 31), 448: ('python: context.image_caption', 12, 29)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140097338226288 = {'class': 'figure-caption', }
_static_140097412968080 = {}
_static_140097338224512 = {'class': 'newsImageContainer', }
_static_140097413192176 = __C2ZContextWrapper
_static_140097413192464 = __compile_zt_expr
_static_140097339651312 = {'id': 'section-leadimage', }

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

            # <Static value=<ast.Dict object at 0x7f6af429f4f0> name=None at 7f6af429fd00> -> __attrs_140097338223024
            __attrs_140097338223024 = _static_140097339651312

            # <Value 'view/available' (2:24)> -> __condition
            __token = 56
            try:
                __zt_tmp = __attrs_140097338223024
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140097413192464('path', 'view/available', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            if __condition:

                # <section ... (0:0)
                # --------------------------------------------------------
                __append('<section id="section-leadimage" >\n  ')

                # <Static value=<ast.Dict object at 0x7f6af4142f80> name=None at 7f6af4143400> -> __attrs_140097338213088
                __attrs_140097338213088 = _static_140097338224512
                __backup_images_140097247581744 = get('images', __marker)

                # <Value 'context/@@images' (6:19)> -> __value
                __token = 153
                try:
                    __zt_tmp = __attrs_140097338213088
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140097413192464('path', 'context/@@images', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                econtext['images'] = __value

                # <figure ... (0:0)
                # --------------------------------------------------------
                __append('<figure class="newsImageContainer" >\n    ')

                # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097338224752
                __attrs_140097338224752 = _static_140097412968080

                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338223264
                __default_140097338223264 = _DEFAULT_MARKER

                # <Value "python: images.tag('image', scale='large', css_class='figure-img img-fluid')" (9:32)> -> __cache_140097338223696
                __token = 219
                try:
                    __zt_tmp = __attrs_140097338224752
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140097338223696 = _static_140097413192464('python', " images.tag('image', scale='large', css_class='figure-img img-fluid')", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                # <BinOp left=<Value "python: images.tag('image', scale='large', css_class='figure-img img-fluid')" (9:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6af4142950> -> __condition
                __expression = __cache_140097338223696

                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <img ... (0:0)
                    # --------------------------------------------------------
                    __append('<img />')
                else:
                    __content = __cache_140097338223696
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n    ')

                # <Static value=<ast.Dict object at 0x7f6af4143670> name=None at 7f6af41421d0> -> __attrs_140097338212944
                __attrs_140097338212944 = _static_140097338226288

                # <Value "python: getattr(context, 'image_caption', None)" (11:31)> -> __condition
                __token = 370
                try:
                    __zt_tmp = __attrs_140097338212944
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140097413192464('python', " getattr(context, 'image_caption', None)", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                if __condition:

                    # <figcaption ... (0:0)
                    # --------------------------------------------------------
                    __append('<figcaption class="figure-caption" >')

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338226096
                    __default_140097338226096 = _DEFAULT_MARKER

                    # <Value 'python: context.image_caption' (12:29)> -> __cache_140097338223792
                    __token = 448
                    try:
                        __zt_tmp = __attrs_140097338212944
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140097338223792 = _static_140097413192464('python', ' context.image_caption', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                    # <BinOp left=<Value 'python: context.image_caption' (12:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6af41438e0> -> __condition
                    __expression = __cache_140097338223792

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n        Image caption\n    ')
                    else:
                        __content = __cache_140097338223792
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</figcaption>')
                __append('\n  </figure>')
                if (__backup_images_140097247581744 is __marker):
                    del econtext['images']
                else:
                    econtext['images'] = __backup_images_140097247581744
                __append('\n</section>')
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }