# -*- coding: utf-8 -*-
__filename = 'manage_main'

__tokens = {27: ('context/manage_page_header', 1, 27), 90: ('string:Databases', 2, 32), 135: ('context/manage_tabs', 3, 27), 366: ('python:context.getDatabaseNames(quote=True)', 12, 26), 435: ('databases', 13, 22), 555: ('python: info[0]', 16, 20), 577: (' python: info[1', 16, 42), 619: ('string:${context/absolute_url}/${qname}/manage_main', 17, 24), 688: ('name', 18, 16), 760: ('context/manage_page_footer', 26, 27)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139755642645632 = {'class': 'font-weight-bold', 'href': 'string:${context/absolute_url}/${qname}/manage_main', }
_static_139755642643328 = {'class': 'fa fa-database text-secondary ml-3 mr-2', }
_static_139755642638864 = {'class': 'form-help mt-4', }
_static_139755642637520 = {'class': 'container-fluid', }
_static_139755726364320 = __C2ZContextWrapper
_static_139755726364608 = __compile_zt_expr
_static_139755728237376 = {}

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

            # <Static value=<ast.Dict object at 0x7f1b6a897340> name=None at 7f1b6a897670> -> __attrs_139755642635216
            __attrs_139755642635216 = _static_139755728237376

            # <Symbol value=<DEFAULT> at 7f1b6a8480d0> -> __default_139755642635024
            __default_139755642635024 = _DEFAULT_MARKER

            # <Value 'context/manage_page_header' (1:27)> -> __cache_139755642634544
            __token = 27
            try:
                __zt_tmp = __attrs_139755642635216
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139755642634544 = _static_139755726364608('path', 'context/manage_page_header', econtext=econtext)(_static_139755726364320(econtext, __zt_tmp))

            # <BinOp left=<Value 'context/manage_page_header' (1:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f1b6a8480d0> at 7f1b656f41f0> -> __condition
            __expression = __cache_139755642634544

            # <Symbol value=<DEFAULT> at 7f1b6a8480d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append('<h1 />')
            else:
                __content = __cache_139755642634544
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n')

            # <Static value=<ast.Dict object at 0x7f1b6a897340> name=None at 7f1b6a897670> -> __attrs_139755642636752
            __attrs_139755642636752 = _static_139755728237376
            __backup_management_view_139755710026256 = get('management_view', __marker)

            # <Value 'string:Databases' (2:32)> -> __value
            __token = 90
            try:
                __zt_tmp = __attrs_139755642636752
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139755726364608('string', 'Databases', econtext=econtext)(_static_139755726364320(econtext, __zt_tmp))
            econtext['management_view'] = __value

            # <Symbol value=<DEFAULT> at 7f1b6a8480d0> -> __default_139755642636416
            __default_139755642636416 = _DEFAULT_MARKER

            # <Value 'context/manage_tabs' (3:27)> -> __cache_139755642635936
            __token = 135
            try:
                __zt_tmp = __attrs_139755642636752
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139755642635936 = _static_139755726364608('path', 'context/manage_tabs', econtext=econtext)(_static_139755726364320(econtext, __zt_tmp))

            # <BinOp left=<Value 'context/manage_tabs' (3:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f1b6a8480d0> at 7f1b656f4760> -> __condition
            __expression = __cache_139755642635936

            # <Symbol value=<DEFAULT> at 7f1b6a8480d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <h2 ... (0:0)
                # --------------------------------------------------------
                __append('<h2 />')
            else:
                __content = __cache_139755642635936
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            if (__backup_management_view_139755710026256 is __marker):
                del econtext['management_view']
            else:
                econtext['management_view'] = __backup_management_view_139755710026256
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x7f1b656f4cd0> name=None at 7f1b656f4d00> -> __attrs_139755642637952
            __attrs_139755642637952 = _static_139755642637520

            # <main ... (0:0)
            # --------------------------------------------------------
            __append('<main class="container-fluid">\n\n')

            # <Static value=<ast.Dict object at 0x7f1b656f5210> name=None at 7f1b656f5240> -> __attrs_139755642639296
            __attrs_139755642639296 = _static_139755642638864

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p class="form-help mt-4">\n\tMounted Zope Object Databases (ZODB): Please select a database name \n\tto get into it\'s ')

            # <Static value=<ast.Dict object at 0x7f1b6a897340> name=None at 7f1b6a897670> -> __attrs_139755642640256
            __attrs_139755642640256 = _static_139755728237376

            # <em ... (0:0)
            # --------------------------------------------------------
            __append('<em>Database Manager</em>.\n</p>\n\n')

            # <Static value=<ast.Dict object at 0x7f1b6a897340> name=None at 7f1b6a897670> -> __attrs_139755642641024
            __attrs_139755642641024 = _static_139755728237376
            __backup_databases_139755710027168 = get('databases', __marker)

            # <Value 'python:context.getDatabaseNames(quote=True)' (12:26)> -> __value
            __token = 366
            try:
                __zt_tmp = __attrs_139755642641024
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139755726364608('python', 'context.getDatabaseNames(quote=True)', econtext=econtext)(_static_139755726364320(econtext, __zt_tmp))
            econtext['databases'] = __value

            # <ol ... (0:0)
            # --------------------------------------------------------
            __append('<ol>\n\t')

            # <Static value=<ast.Dict object at 0x7f1b6a897340> name=None at 7f1b6a897670> -> __attrs_139755642642224
            __attrs_139755642642224 = _static_139755728237376
            __backup_info_139755710335056 = get('info', __marker)

            # <Value 'databases' (13:22)> -> __iterator
            __token = 435
            try:
                __zt_tmp = __attrs_139755642642224
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_139755726364608('path', 'databases', econtext=econtext)(_static_139755726364320(econtext, __zt_tmp))
            (__iterator, ____index_139755642642464, ) = getname('repeat')('info', __iterator)
            econtext['info'] = None
            for __item in __iterator:
                econtext['info'] = __item

                # <li ... (0:0)
                # --------------------------------------------------------
                __append('<li>\n\t\t')

                # <Static value=<ast.Dict object at 0x7f1b656f6380> name=None at 7f1b656f63b0> -> __attrs_139755642643760
                __attrs_139755642643760 = _static_139755642643328

                # <i ... (0:0)
                # --------------------------------------------------------
                __append('<i class="fa fa-database text-secondary ml-3 mr-2"></i>\n\t\t')

                # <Static value=<ast.Dict object at 0x7f1b656f6c80> name=None at 7f1b656f6cb0> -> __attrs_139755642645824
                __attrs_139755642645824 = _static_139755642645632
                __backup_name_139755710335008 = get('name', __marker)

                # <Value 'python: info[0]' (16:20)> -> __value
                __token = 555
                try:
                    __zt_tmp = __attrs_139755642645824
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139755726364608('python', ' info[0]', econtext=econtext)(_static_139755726364320(econtext, __zt_tmp))
                econtext['name'] = __value
                __backup_qname_139755710334144 = get('qname', __marker)

                # <Value 'python: info[1]' (16:42)> -> __value
                __token = 577
                try:
                    __zt_tmp = __attrs_139755642645824
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139755726364608('python', ' info[1]', econtext=econtext)(_static_139755726364320(econtext, __zt_tmp))
                econtext['qname'] = __value

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a class="font-weight-bold"')

                # <Symbol value=<DEFAULT> at 7f1b6a8480d0> -> __default_139755642645344
                __default_139755642645344 = _DEFAULT_MARKER

                # <Substitution 'string:${context/absolute_url}/${qname}/manage_main' (17:24)> -> __attr_href
                __token = 619
                try:
                    __zt_tmp = __attrs_139755642645824
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_139755726364608('string', '${context/absolute_url}/${qname}/manage_main', econtext=econtext)(_static_139755726364320(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((' href="%s"' % __attr_href))
                __append('>')

                # <Symbol value=<DEFAULT> at 7f1b6a8480d0> -> __default_139755642644672
                __default_139755642644672 = _DEFAULT_MARKER

                # <Value 'name' (18:16)> -> __cache_139755642644192
                __token = 688
                try:
                    __zt_tmp = __attrs_139755642645824
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_139755642644192 = _static_139755726364608('path', 'name', econtext=econtext)(_static_139755726364320(econtext, __zt_tmp))

                # <BinOp left=<Value 'name' (18:16)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f1b6a8480d0> at 7f1b656f67a0> -> __condition
                __expression = __cache_139755642644192

                # <Symbol value=<DEFAULT> at 7f1b6a8480d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('\n\t\t\tMain\n\t\t')
                else:
                    __content = __cache_139755642644192
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</a>')
                if (__backup_qname_139755710334144 is __marker):
                    del econtext['qname']
                else:
                    econtext['qname'] = __backup_qname_139755710334144
                if (__backup_name_139755710335008 is __marker):
                    del econtext['name']
                else:
                    econtext['name'] = __backup_name_139755710335008
                __append('\n\t</li>')
                ____index_139755642642464 -= 1
                if (____index_139755642642464 > 0):
                    __append('\n ')
            if (__backup_info_139755710335056 is __marker):
                del econtext['info']
            else:
                econtext['info'] = __backup_info_139755710335056
            __append('\n</ol>')
            if (__backup_databases_139755710027168 is __marker):
                del econtext['databases']
            else:
                econtext['databases'] = __backup_databases_139755710027168
            __append('\n\n</main>\n\n')

            # <Static value=<ast.Dict object at 0x7f1b6a897340> name=None at 7f1b6a897670> -> __attrs_139755642647408
            __attrs_139755642647408 = _static_139755728237376

            # <Symbol value=<DEFAULT> at 7f1b6a8480d0> -> __default_139755642647216
            __default_139755642647216 = _DEFAULT_MARKER

            # <Value 'context/manage_page_footer' (26:27)> -> __cache_139755642646736
            __token = 760
            try:
                __zt_tmp = __attrs_139755642647408
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139755642646736 = _static_139755726364608('path', 'context/manage_page_footer', econtext=econtext)(_static_139755726364320(econtext, __zt_tmp))

            # <BinOp left=<Value 'context/manage_page_footer' (26:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f1b6a8480d0> at 7f1b656f7190> -> __condition
            __expression = __cache_139755642646736

            # <Symbol value=<DEFAULT> at 7f1b6a8480d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append('<h1 />')
            else:
                __content = __cache_139755642646736
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }