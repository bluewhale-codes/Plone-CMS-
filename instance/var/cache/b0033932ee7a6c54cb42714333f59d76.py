# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/plone/app/registry/browser/templates/exportxml.pt'

__tokens = {666: ('python:view.interfaces()', 18, 31), 701: ('${python:prefix[1]}', 18, 66), 703: ('python:prefix[1]', 18, 68), 762: ('${python:prefix[0]}', 20, 11), 764: ('python:prefix[0]', 20, 13), 1038: ('python:view.prefixes()', 30, 31), 1071: ('${python:prefix[1]}', 30, 64), 1073: ('python:prefix[1]', 30, 66), 1132: ('${python:prefix[0]}', 32, 11), 1134: ('python:prefix[0]', 32, 13)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140453434868544 = {'href': '${python:prefix[1]}', 'target': '_blank', }
_static_140453434878576 = {'id': 'h3-prefixes', }
_static_140453434876704 = {'class': 'exporttab', 'id': 'export-section-prefixes', }
_static_140453434880880 = {'href': '${python:prefix[1]}', 'target': '_blank', }
_static_140453526790416 = __C2ZContextWrapper
_static_140453526790704 = __compile_zt_expr
_static_140453434882704 = {'class': 'collapse_interfaces', }
_static_140453434869792 = {'id': 'h3-interfaces', }
_static_140453434923120 = {'class': 'exporttab', 'id': 'export-section-interfaces', }
_static_140453434920768 = {'class': 'pat-autotoc autotabs', 'data-pat-autotoc': 'levels: h3; section: div.exporttab; className: autotabs', }
_static_140453526549936 = {}

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

            # <Static value=<ast.Dict object at 0x7fbde28eb5b0> name=None at 7fbde28eb8e0> -> __attrs_140453434925136
            __attrs_140453434925136 = _static_140453526549936

            # <tal ... (0:0)
            # --------------------------------------------------------
            __append('<tal>\n  ')

            # <Static value=<ast.Dict object at 0x7fbde28eb5b0> name=None at 7fbde28eb8e0> -> __attrs_140453434917744
            __attrs_140453434917744 = _static_140453526549936

            # <h3 ... (0:0)
            # --------------------------------------------------------
            __append('<h3>')
            __stream_140453434924080 = []
            __append_140453434924080 = __stream_140453434924080.append
            __append_140453434924080('Export parts')
            __msgid_140453434924080 = __re_whitespace(''.join(__stream_140453434924080)).strip()
            if 'registry_export_parts_heading':
                __append(translate('registry_export_parts_heading', mapping=None, default=__msgid_140453434924080, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</h3>\n  ')

            # <Static value=<ast.Dict object at 0x7fbde28eb5b0> name=None at 7fbde28eb8e0> -> __attrs_140453434917984
            __attrs_140453434917984 = _static_140453526549936

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p>')
            __stream_140453434922208 = []
            __append_140453434922208 = __stream_140453434922208.append
            __append_140453434922208('\n      Download of a XML-file optimized to be used in a GenericSetup profile of an add-on or policy profile.\n      It contains only the selected parts.\n  ')
            __msgid_140453434922208 = __re_whitespace(''.join(__stream_140453434922208)).strip()
            if 'registry_export_parts_text':
                __append(translate('registry_export_parts_text', mapping=None, default=__msgid_140453434922208, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</p>\n\n  ')

            # <Static value=<ast.Dict object at 0x7fbddd188f40> name=None at 7fbddd188bb0> -> __attrs_140453434920000
            __attrs_140453434920000 = _static_140453434920768

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="pat-autotoc autotabs" data-pat-autotoc="levels: h3; section: div.exporttab; className: autotabs" >\n    ')

            # <Static value=<ast.Dict object at 0x7fbddd189870> name=None at 7fbddd1898d0> -> __attrs_140453434878096
            __attrs_140453434878096 = _static_140453434923120

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="exporttab" id="export-section-interfaces" >\n      ')

            # <Static value=<ast.Dict object at 0x7fbddd17c820> name=None at 7fbddd17e6e0> -> __attrs_140453434881504
            __attrs_140453434881504 = _static_140453434869792

            # <h3 ... (0:0)
            # --------------------------------------------------------
            __append('<h3 id="h3-interfaces" >')
            __stream_140453434871424 = []
            __append_140453434871424 = __stream_140453434871424.append
            __append_140453434871424('by Interface')
            __msgid_140453434871424 = __re_whitespace(''.join(__stream_140453434871424)).strip()
            if 'registry_export_parts_label_iface':
                __append(translate('registry_export_parts_label_iface', mapping=None, default=__msgid_140453434871424, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</h3>\n      ')

            # <Static value=<ast.Dict object at 0x7fbddd17fa90> name=None at 7fbddd17fdf0> -> __attrs_140453434875792
            __attrs_140453434875792 = _static_140453434882704

            # <ul ... (0:0)
            # --------------------------------------------------------
            __append('<ul class="collapse_interfaces">\n        ')

            # <Static value=<ast.Dict object at 0x7fbde28eb5b0> name=None at 7fbde28eb8e0> -> __attrs_140453434879296
            __attrs_140453434879296 = _static_140453526549936
            __backup_prefix_140453434875696 = get('prefix', __marker)

            # <Value 'python:view.interfaces()' (18:31)> -> __iterator
            __token = 666
            try:
                __zt_tmp = __attrs_140453434879296
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140453526790704('python', 'view.interfaces()', econtext=econtext)(_static_140453526790416(econtext, __zt_tmp))
            (__iterator, ____index_140453434869648, ) = getname('repeat')('prefix', __iterator)
            econtext['prefix'] = None
            for __item in __iterator:
                econtext['prefix'] = __item

                # <li ... (0:0)
                # --------------------------------------------------------
                __append('<li>')

                # <Static value=<ast.Dict object at 0x7fbddd17f370> name=None at 7fbddd17f220> -> __attrs_140453434869936
                __attrs_140453434869936 = _static_140453434880880

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a')

                # <Symbol value=<DEFAULT> at 7fbde28a8340> -> __default_140453434875312
                __default_140453434875312 = _DEFAULT_MARKER

                # <Interpolation value=<Substitution '${python:prefix[1]}' (18:66)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fbddd17f3d0> -> __attr_href
                __token = 701
                __token = 703
                try:
                    __zt_tmp = __attrs_140453434869936
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_140453526790704('python', 'prefix[1]', econtext=econtext)(_static_140453526790416(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                __attr_href = __attr_href
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
                __append(' target="_blank" >')

                # <Interpolation value=<Substitution '${python:prefix[0]}' (20:11)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fbddd17f010> -> __content_140453610629680
                __token = 762
                __token = 764
                try:
                    __zt_tmp = __attrs_140453434869936
                except get('NameError', NameError):
                    __zt_tmp = None

                __content_140453610629680 = _static_140453526790704('python', 'prefix[0]', econtext=econtext)(_static_140453526790416(econtext, __zt_tmp))
                __content_140453610629680 = __quote(__content_140453610629680, '\x00', '&#0;', None, None)
                __content_140453610629680 = __content_140453610629680
                if (__content_140453610629680 is None):
                    pass
                else:
                    if (__content_140453610629680 is None):
                        __content_140453610629680 = None
                    else:
                        __tt = type(__content_140453610629680)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __content_140453610629680 = str(__content_140453610629680)
                        else:
                            if (__tt is bytes):
                                __content_140453610629680 = decode(__content_140453610629680)
                            else:
                                if (__tt is not str):
                                    try:
                                        __content_140453610629680 = __content_140453610629680.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__content_140453610629680)
                                        __content_140453610629680 = (str(__content_140453610629680) if (__content_140453610629680 is __converted) else __converted)
                                    else:
                                        __content_140453610629680 = __content_140453610629680()
                if (__content_140453610629680 is not None):
                    __append(__content_140453610629680)
                __append('</a></li>')
                ____index_140453434869648 -= 1
                if (____index_140453434869648 > 0):
                    __append('\n        ')
            if (__backup_prefix_140453434875696 is __marker):
                del econtext['prefix']
            else:
                econtext['prefix'] = __backup_prefix_140453434875696
            __append('\n      </ul>\n    </div>\n    ')

            # <Static value=<ast.Dict object at 0x7fbddd17e320> name=None at 7fbddd17e740> -> __attrs_140453434876512
            __attrs_140453434876512 = _static_140453434876704

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="exporttab" id="export-section-prefixes" >\n      ')

            # <Static value=<ast.Dict object at 0x7fbddd17ea70> name=None at 7fbddd17cf40> -> __attrs_140453434878288
            __attrs_140453434878288 = _static_140453434878576

            # <h3 ... (0:0)
            # --------------------------------------------------------
            __append('<h3 id="h3-prefixes" >')
            __stream_140453434876560 = []
            __append_140453434876560 = __stream_140453434876560.append
            __append_140453434876560('by Prefix')
            __msgid_140453434876560 = __re_whitespace(''.join(__stream_140453434876560)).strip()
            if 'registry_export_parts_label_prefix':
                __append(translate('registry_export_parts_label_prefix', mapping=None, default=__msgid_140453434876560, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</h3>\n      ')

            # <Static value=<ast.Dict object at 0x7fbde28eb5b0> name=None at 7fbde28eb8e0> -> __attrs_140453434875936
            __attrs_140453434875936 = _static_140453526549936

            # <ul ... (0:0)
            # --------------------------------------------------------
            __append('<ul>\n        ')

            # <Static value=<ast.Dict object at 0x7fbde28eb5b0> name=None at 7fbde28eb8e0> -> __attrs_140453434873872
            __attrs_140453434873872 = _static_140453526549936
            __backup_prefix_140453434875552 = get('prefix', __marker)

            # <Value 'python:view.prefixes()' (30:31)> -> __iterator
            __token = 1038
            try:
                __zt_tmp = __attrs_140453434873872
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140453526790704('python', 'view.prefixes()', econtext=econtext)(_static_140453526790416(econtext, __zt_tmp))
            (__iterator, ____index_140453434873632, ) = getname('repeat')('prefix', __iterator)
            econtext['prefix'] = None
            for __item in __iterator:
                econtext['prefix'] = __item

                # <li ... (0:0)
                # --------------------------------------------------------
                __append('<li>')

                # <Static value=<ast.Dict object at 0x7fbddd17c340> name=None at 7fbddd17db40> -> __attrs_140453434874592
                __attrs_140453434874592 = _static_140453434868544

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a')

                # <Symbol value=<DEFAULT> at 7fbde28a8340> -> __default_140453434869696
                __default_140453434869696 = _DEFAULT_MARKER

                # <Interpolation value=<Substitution '${python:prefix[1]}' (30:64)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fbddd17c2b0> -> __attr_href
                __token = 1071
                __token = 1073
                try:
                    __zt_tmp = __attrs_140453434874592
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_140453526790704('python', 'prefix[1]', econtext=econtext)(_static_140453526790416(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                __attr_href = __attr_href
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
                __append(' target="_blank" >')

                # <Interpolation value=<Substitution '${python:prefix[0]}' (32:11)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fbddd17dcc0> -> __content_140453610629680
                __token = 1132
                __token = 1134
                try:
                    __zt_tmp = __attrs_140453434874592
                except get('NameError', NameError):
                    __zt_tmp = None

                __content_140453610629680 = _static_140453526790704('python', 'prefix[0]', econtext=econtext)(_static_140453526790416(econtext, __zt_tmp))
                __content_140453610629680 = __quote(__content_140453610629680, '\x00', '&#0;', None, None)
                __content_140453610629680 = __content_140453610629680
                if (__content_140453610629680 is None):
                    pass
                else:
                    if (__content_140453610629680 is None):
                        __content_140453610629680 = None
                    else:
                        __tt = type(__content_140453610629680)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __content_140453610629680 = str(__content_140453610629680)
                        else:
                            if (__tt is bytes):
                                __content_140453610629680 = decode(__content_140453610629680)
                            else:
                                if (__tt is not str):
                                    try:
                                        __content_140453610629680 = __content_140453610629680.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__content_140453610629680)
                                        __content_140453610629680 = (str(__content_140453610629680) if (__content_140453610629680 is __converted) else __converted)
                                    else:
                                        __content_140453610629680 = __content_140453610629680()
                if (__content_140453610629680 is not None):
                    __append(__content_140453610629680)
                __append('</a></li>')
                ____index_140453434873632 -= 1
                if (____index_140453434873632 > 0):
                    __append('\n        ')
            if (__backup_prefix_140453434875552 is __marker):
                del econtext['prefix']
            else:
                econtext['prefix'] = __backup_prefix_140453434875552
            __append('\n      </ul>\n    </div>\n  </div>\n</tal>\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }