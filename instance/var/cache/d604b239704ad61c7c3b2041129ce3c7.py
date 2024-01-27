# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/plone/app/dexterity/browser/types_listing.pt'

__tokens = {106: ('view/status', 5, 22), 146: ('view/status', 7, 23), 265: ('view/description', 13, 20), 311: ('view/description', 14, 28), 408: ('${context/absolute_url}/@@add-type', 19, 13), 410: ('context/absolute_url', 19, 15), 619: ('${context/absolute_url}/@@import-types', 27, 13), 621: ('context/absolute_url', 27, 15), 851: ('view/subforms', 36, 24), 896: ('form/render', 37, 30), 971: ('view/actions/values', 42, 26), 1055: ('action/render', 45, 34)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140097252668320 = {'type': 'submit', }
_static_140097252662128 = {'class': 'action', }
_static_140097252659440 = {'class': 'crud-form', }
_static_140097252051456 = {'class': 'btn btn-primary', }
_static_140097252055584 = {'class': 'pat-plone-modal', 'href': '${context/absolute_url}/@@import-types', }
_static_140097252059760 = {'class': 'btn btn-primary', }
_static_140097252057840 = {'class': 'pat-plone-modal', 'href': '${context/absolute_url}/@@add-type', }
_static_140097252057792 = {'class': 'mb-4', }
_static_140097252062880 = {'class': 'crud-description documentDescription', }
_static_140097413192176 = __C2ZContextWrapper
_static_140097413192464 = __compile_zt_expr
_static_140097252050064 = {'class': 'alert alert-info', 'role': 'alert', }
_static_140097412968080 = {}

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

            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097252050880
            __attrs_140097252050880 = _static_140097412968080
            __previous_i18n_domain_140097252053376 = __i18n_domain
            __i18n_domain = 'plone'
            __append('\n\n  ')

            # <Static value=<ast.Dict object at 0x7f6aeef14490> name=None at 7f6aeef14250> -> __attrs_140097252060624
            __attrs_140097252060624 = _static_140097252050064

            # <Value 'view/status' (5:22)> -> __condition
            __token = 106
            try:
                __zt_tmp = __attrs_140097252060624
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140097413192464('path', 'view/status', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="alert alert-info" role="alert" >\n    ')

                # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097252054048
                __attrs_140097252054048 = _static_140097412968080

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span>')

                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252054000
                __default_140097252054000 = _DEFAULT_MARKER

                # <Value 'view/status' (7:23)> -> __cache_140097252057744
                __token = 146
                try:
                    __zt_tmp = __attrs_140097252054048
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140097252057744 = _static_140097413192464('path', 'view/status', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                # <BinOp left=<Value 'view/status' (7:23)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeef17f10> -> __condition
                __expression = __cache_140097252057744

                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('\n      Status\n    ')
                else:
                    __content = __cache_140097252057744
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</span>\n  </div>')
            __append('\n\n  ')

            # <Static value=<ast.Dict object at 0x7f6aeef176a0> name=None at 7f6aeef17790> -> __attrs_140097252063792
            __attrs_140097252063792 = _static_140097252062880

            # <Value 'view/description' (13:20)> -> __condition
            __token = 265
            try:
                __zt_tmp = __attrs_140097252063792
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140097413192464('path', 'view/description', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            if __condition:

                # <p ... (0:0)
                # --------------------------------------------------------
                __append('<p class="crud-description documentDescription" >')

                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252061248
                __default_140097252061248 = _DEFAULT_MARKER

                # <Value 'view/description' (14:28)> -> __cache_140097252061296
                __token = 311
                try:
                    __zt_tmp = __attrs_140097252063792
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140097252061296 = _static_140097413192464('path', 'view/description', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                # <BinOp left=<Value 'view/description' (14:28)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeef17700> -> __condition
                __expression = __cache_140097252061296

                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('\n  ')
                else:
                    __content = __cache_140097252061296
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('</p>')
            __append('\n  ')

            # <Static value=<ast.Dict object at 0x7f6aeef162c0> name=None at 7f6aeef17910> -> __attrs_140097252063312
            __attrs_140097252063312 = _static_140097252057792

            # <header ... (0:0)
            # --------------------------------------------------------
            __append('<header class="mb-4">\n    ')

            # <Static value=<ast.Dict object at 0x7f6aeef162f0> name=None at 7f6aeef16440> -> __attrs_140097252056880
            __attrs_140097252056880 = _static_140097252057840

            # <a ... (0:0)
            # --------------------------------------------------------
            __append('<a class="pat-plone-modal"')

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252057120
            __default_140097252057120 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution '${context/absolute_url}/@@add-type' (19:13)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f6aeef14820> -> __attr_href
            __token = 408
            __token = 410
            try:
                __zt_tmp = __attrs_140097252056880
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_140097413192464('path', 'context/absolute_url', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_href = ('%s%s' % ((__attr_href if (__attr_href is not None) else ''), '/@@add-type', ))
            if (__attr_href is None):
                pass
            else:
                if (__attr_href is _DEFAULT_MARKER):
                    __attr_href = None
                else:
                    __tt = type(__attr_href)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __attr_href = str(__attr_href)
                    else:
                        if (__tt is bytes):
                            __attr_href = decode(__attr_href)
                        else:
                            if (__tt is not str):
                                try:
                                    __attr_href = __attr_href.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__attr_href)
                                    __attr_href = (str(__attr_href) if (__attr_href is __converted) else __converted)
                                else:
                                    __attr_href = __attr_href()
            if (__attr_href is not None):
                __append((' href="%s"' % __attr_href))
            __append(' >\n      ')

            # <Static value=<ast.Dict object at 0x7f6aeef16a70> name=None at 7f6aeef15e40> -> __attrs_140097252055248
            __attrs_140097252055248 = _static_140097252059760

            # <button ... (0:0)
            # --------------------------------------------------------
            __append('<button class="btn btn-primary" >')
            __stream_140097252059376 = []
            __append_140097252059376 = __stream_140097252059376.append
            __append_140097252059376('Add New Content Type&hellip;')
            __msgid_140097252059376 = __re_whitespace(''.join(__stream_140097252059376)).strip()
            if __msgid_140097252059376:
                __append(translate(__msgid_140097252059376, mapping=None, default=__msgid_140097252059376, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</button>\n    </a>\n\n    ')

            # <Static value=<ast.Dict object at 0x7f6aeef15a20> name=None at 7f6aeef15570> -> __attrs_140097252054816
            __attrs_140097252054816 = _static_140097252055584

            # <a ... (0:0)
            # --------------------------------------------------------
            __append('<a class="pat-plone-modal"')

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252054480
            __default_140097252054480 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution '${context/absolute_url}/@@import-types' (27:13)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f6aeef15a80> -> __attr_href
            __token = 619
            __token = 621
            try:
                __zt_tmp = __attrs_140097252054816
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_140097413192464('path', 'context/absolute_url', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_href = ('%s%s' % ((__attr_href if (__attr_href is not None) else ''), '/@@import-types', ))
            if (__attr_href is None):
                pass
            else:
                if (__attr_href is _DEFAULT_MARKER):
                    __attr_href = None
                else:
                    __tt = type(__attr_href)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __attr_href = str(__attr_href)
                    else:
                        if (__tt is bytes):
                            __attr_href = decode(__attr_href)
                        else:
                            if (__tt is not str):
                                try:
                                    __attr_href = __attr_href.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__attr_href)
                                    __attr_href = (str(__attr_href) if (__attr_href is __converted) else __converted)
                                else:
                                    __attr_href = __attr_href()
            if (__attr_href is not None):
                __append((' href="%s"' % __attr_href))
            __append(' >\n      ')

            # <Static value=<ast.Dict object at 0x7f6aeef14a00> name=None at 7f6aeef15330> -> __attrs_140097252050688
            __attrs_140097252050688 = _static_140097252051456

            # <button ... (0:0)
            # --------------------------------------------------------
            __append('<button class="btn btn-primary" >')
            __stream_140097252056112 = []
            __append_140097252056112 = __stream_140097252056112.append
            __append_140097252056112('Import Type Profiles&hellip;')
            __msgid_140097252056112 = __re_whitespace(''.join(__stream_140097252056112)).strip()
            if __msgid_140097252056112:
                __append(translate(__msgid_140097252056112, mapping=None, default=__msgid_140097252056112, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</button>\n    </a>\n  </header>\n\n  ')

            # <Static value=<ast.Dict object at 0x7f6aeefa90f0> name=None at 7f6aeefab700> -> __attrs_140097252662464
            __attrs_140097252662464 = _static_140097252659440
            __backup_form_140097338105504 = get('form', __marker)

            # <Value 'view/subforms' (36:24)> -> __iterator
            __token = 851
            try:
                __zt_tmp = __attrs_140097252662464
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140097413192464('path', 'view/subforms', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            (__iterator, ____index_140097252667408, ) = getname('repeat')('form', __iterator)
            econtext['form'] = None
            for __item in __iterator:
                econtext['form'] = __item

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="crud-form" >')

                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252050592
                __default_140097252050592 = _DEFAULT_MARKER

                # <Value 'form/render' (37:30)> -> __cache_140097252050544
                __token = 896
                try:
                    __zt_tmp = __attrs_140097252662464
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140097252050544 = _static_140097413192464('path', 'form/render', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                # <BinOp left=<Value 'form/render' (37:30)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeef14fd0> -> __condition
                __expression = __cache_140097252050544

                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('\n  ')
                else:
                    __content = __cache_140097252050544
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('</div>')
                ____index_140097252667408 -= 1
                if (____index_140097252667408 > 0):
                    __append('\n  ')
            if (__backup_form_140097338105504 is __marker):
                del econtext['form']
            else:
                econtext['form'] = __backup_form_140097338105504
            __append('\n\n  ')

            # <Static value=<ast.Dict object at 0x7f6aeefa9b70> name=None at 7f6aeefa8b20> -> __attrs_140097252657808
            __attrs_140097252657808 = _static_140097252662128
            __backup_action_140097338105888 = get('action', __marker)

            # <Value 'view/actions/values' (42:26)> -> __iterator
            __token = 971
            try:
                __zt_tmp = __attrs_140097252657808
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140097413192464('path', 'view/actions/values', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            (__iterator, ____index_140097252658000, ) = getname('repeat')('action', __iterator)
            econtext['action'] = None
            for __item in __iterator:
                econtext['action'] = __item

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="action" >\n    ')

                # <Static value=<ast.Dict object at 0x7f6aeefab3a0> name=None at 7f6aeefab3d0> -> __attrs_140097252660160
                __attrs_140097252660160 = _static_140097252668320

                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252657568
                __default_140097252657568 = _DEFAULT_MARKER

                # <Value 'action/render' (45:34)> -> __cache_140097252657520
                __token = 1055
                try:
                    __zt_tmp = __attrs_140097252660160
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140097252657520 = _static_140097413192464('path', 'action/render', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                # <BinOp left=<Value 'action/render' (45:34)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeefa92a0> -> __condition
                __expression = __cache_140097252657520

                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input type="submit" />')
                else:
                    __content = __cache_140097252657520
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n  </div>')
                ____index_140097252658000 -= 1
                if (____index_140097252658000 > 0):
                    __append('\n  ')
            if (__backup_action_140097338105888 is __marker):
                del econtext['action']
            else:
                econtext['action'] = __backup_action_140097338105888
            __append('\n')
            __i18n_domain = __previous_i18n_domain_140097252053376
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }