# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/plone/app/event/browser/formatted_start_date.pt'

__tokens = {278: ('view/date_dict', 10, 20), 356: ('date_dict/start_date', 15, 23), 418: ('not:date_dict/whole_day', 16, 32), 521: ('date_dict/start_iso', 19, 20), 621: ('date_dict/start_time', 23, 27)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140533343928720 = {'class': 'explain', }
_static_140533343928576 = {'class': 'dtstart', 'title': 'date_dict/start_iso', }
_static_140533417024992 = __C2ZContextWrapper
_static_140533417025280 = __compile_zt_expr
_static_140533416833664 = {}
_static_140533343940480 = {'xmlns': 'http://www.w3.org/1999/xhtml', 'lang': 'en', 'xml:lang': 'en', }

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

            # <Static value=<ast.Dict object at 0x7fd0780b6f80> name=None at 7fd0780b6f50> -> __attrs_140533343940144
            __attrs_140533343940144 = _static_140533343940480
            __previous_i18n_domain_140533343940000 = __i18n_domain
            __i18n_domain = 'plone'
            __append('\n  ')

            # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533343938992
            __attrs_140533343938992 = _static_140533416833664
            __backup_date_dict_140533346014672 = get('date_dict', __marker)

            # <Value 'view/date_dict' (10:20)> -> __value
            __token = 278
            try:
                __zt_tmp = __attrs_140533343938992
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140533417025280('path', 'view/date_dict', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
            econtext['date_dict'] = __value
            __append('\n\n    ')

            # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533343936496
            __attrs_140533343936496 = _static_140533416833664

            # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533343936400
            __default_140533343936400 = _DEFAULT_MARKER

            # <Value 'date_dict/start_date' (15:23)> -> __cache_140533343937024
            __token = 356
            try:
                __zt_tmp = __attrs_140533343936496
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140533343937024 = _static_140533417025280('path', 'date_dict/start_date', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))

            # <BinOp left=<Value 'date_dict/start_date' (15:23)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fd07c5afbe0> at 7fd0780b65c0> -> __condition
            __expression = __cache_140533343937024

            # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span></span>')
            else:
                __content = __cache_140533343937024
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append('\n    ')

            # <Static value=<ast.Dict object at 0x7fd07c63b280> name=None at 7fd07c63b5b0> -> __attrs_140533343936352
            __attrs_140533343936352 = _static_140533416833664

            # <Value 'not:date_dict/whole_day' (16:32)> -> __condition
            __token = 418
            try:
                __zt_tmp = __attrs_140533343936352
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140533417025280('not', 'date_dict/whole_day', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
            if __condition:
                __append('\n      ')

                # <Static value=<ast.Dict object at 0x7fd0780b4100> name=None at 7fd0780b4af0> -> __attrs_140533343932320
                __attrs_140533343932320 = _static_140533343928576

                # <abbr ... (0:0)
                # --------------------------------------------------------
                __append('<abbr class="dtstart"')

                # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533343933664
                __default_140533343933664 = _DEFAULT_MARKER

                # <Substitution 'date_dict/start_iso' (19:20)> -> __attr_title
                __token = 521
                try:
                    __zt_tmp = __attrs_140533343932320
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_title = _static_140533417025280('path', 'date_dict/start_iso', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))
                __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_title is not None):
                    __append((' title="%s"' % __attr_title))
                __append(' >\n        ')

                # <Static value=<ast.Dict object at 0x7fd0780b4190> name=None at 7fd0780b4520> -> __attrs_140533343928432
                __attrs_140533343928432 = _static_140533343928720

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span class="explain" >')

                # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __default_140533343930880
                __default_140533343930880 = _DEFAULT_MARKER

                # <Value 'date_dict/start_time' (23:27)> -> __cache_140533343932848
                __token = 621
                try:
                    __zt_tmp = __attrs_140533343928432
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140533343932848 = _static_140533417025280('path', 'date_dict/start_time', econtext=econtext)(_static_140533417024992(econtext, __zt_tmp))

                # <BinOp left=<Value 'date_dict/start_time' (23:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fd07c5afbe0> at 7fd0780b4ac0> -> __condition
                __expression = __cache_140533343932848

                # <Symbol value=<DEFAULT> at 7fd07c5afbe0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('Start Time')
                else:
                    __content = __cache_140533343932848
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</span>\n      </abbr>\n    ')
            __append('\n\n  ')
            if (__backup_date_dict_140533346014672 is __marker):
                del econtext['date_dict']
            else:
                econtext['date_dict'] = __backup_date_dict_140533346014672
            __append('\n')
            __i18n_domain = __previous_i18n_domain_140533343940000
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }