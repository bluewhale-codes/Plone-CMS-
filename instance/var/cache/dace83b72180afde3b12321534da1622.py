# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/Products/CMFPlone/browser/login/templates/logged_out.pt'

__tokens = {402: ("python:request.set('disable_border',1)", 10, 35), 489: (" python:request.set('disable_plone.leftcolumn',1", 11, 47), 586: ("o python:request.set('disable_plone.rightcolumn',", 12, 46), 1204: ('string:${portal_url}/@@plone-root-logout', 30, 36), 255: ('context/@@main_template/macros/master', 5, 23), 255: ('context/@@main_template/macros/master', 5, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from collections import deque as _deque

_static_139867200031664 = {'href': 'string:${portal_url}/@@plone-root-logout', }
_static_139867200040496 = {'id': 'content-core', }
_static_139867200178400 = {'class': 'documentDescription', }
_static_139867200191312 = {'class': 'documentFirstHeading', }
_static_139867356405408 = __C2ZContextWrapper
_static_139867356405696 = __compile_zt_expr
_static_139867200177392 = 'master'
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

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867200187664
            __attrs_139867200187664 = _static_139867362323344
            __previous_i18n_domain_139867200184640 = __i18n_domain
            __i18n_domain = 'plone'
            __backup_macroname_139867199083712 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f355ec844f0> name=None at 7f355ec84af0> -> __value
            __value = _static_139867200177392
            econtext['macroname'] = __value

            def __fill_top_slot(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867200191024
                __attrs_139867200191024 = _static_139867362323344
                __backup_dummy_139867199391200 = get('dummy', __marker)

                # <Value "python:request.set('disable_border',1)" (10:35)> -> __value
                __token = 402
                try:
                    __zt_tmp = __attrs_139867200191024
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139867356405696('python', "request.set('disable_border',1)", econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                econtext['dummy'] = __value
                __backup_disable_column_one_139867200361312 = get('disable_column_one', __marker)

                # <Value "python:request.set('disable_plone.leftcolumn',1)" (11:47)> -> __value
                __token = 489
                try:
                    __zt_tmp = __attrs_139867200191024
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139867356405696('python', "request.set('disable_plone.leftcolumn',1)", econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                econtext['disable_column_one'] = __value
                __backup_disable_column_two_139867200275552 = get('disable_column_two', __marker)

                # <Value "python:request.set('disable_plone.rightcolumn',1)" (12:46)> -> __value
                __token = 586
                try:
                    __zt_tmp = __attrs_139867200191024
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139867356405696('python', "request.set('disable_plone.rightcolumn',1)", econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                econtext['disable_column_two'] = __value
                if (__backup_disable_column_two_139867200275552 is __marker):
                    del econtext['disable_column_two']
                else:
                    econtext['disable_column_two'] = __backup_disable_column_two_139867200275552
                if (__backup_disable_column_one_139867200361312 is __marker):
                    del econtext['disable_column_one']
                else:
                    econtext['disable_column_one'] = __backup_disable_column_one_139867200361312
                if (__backup_dummy_139867199391200 is __marker):
                    del econtext['dummy']
                else:
                    econtext['dummy'] = __backup_dummy_139867199391200
            _slots = econtext['__slot_top_slot'] = _deque((__fill_top_slot, ))

            def __fill_main(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867200287600
                __attrs_139867200287600 = _static_139867362323344
                __append('\n\n')

                # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867200283136
                __attrs_139867200283136 = _static_139867362323344
                __append('\n    ')

                # <Static value=<ast.Dict object at 0x7f355ec87b50> name=None at 7f355ec858a0> -> __attrs_139867200189584
                __attrs_139867200189584 = _static_139867200191312

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append('<h1 class="documentFirstHeading">')
                __stream_139867200183392 = []
                __append_139867200183392 = __stream_139867200183392.append
                __append_139867200183392('Still logged in as a Zope user')
                __msgid_139867200183392 = __re_whitespace(''.join(__stream_139867200183392)).strip()
                if 'heading_quit_to_log_out':
                    __append(translate('heading_quit_to_log_out', mapping=None, default=__msgid_139867200183392, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</h1>\n\n    ')

                # <Static value=<ast.Dict object at 0x7f355ec848e0> name=None at 7f355ec851b0> -> __attrs_139867200179888
                __attrs_139867200179888 = _static_139867200178400

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="documentDescription">')
                __stream_139867200192176 = []
                __append_139867200192176 = __stream_139867200192176.append
                __append_139867200192176('\n        You are logged in via HTTP authentication (i.e. the Zope Management\n        Interface). In order to log out, you must:\n    ')
                __msgid_139867200192176 = __re_whitespace(''.join(__stream_139867200192176)).strip()
                if 'description_quit_to_log_out':
                    __append(translate('description_quit_to_log_out', mapping=None, default=__msgid_139867200192176, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</div>\n\n    ')

                # <Static value=<ast.Dict object at 0x7f355ec62e30> name=None at 7f355ee4cf40> -> __attrs_139867200030320
                __attrs_139867200030320 = _static_139867200040496

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div id="content-core">\n        ')

                # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867200038240
                __attrs_139867200038240 = _static_139867362323344

                # <p ... (0:0)
                # --------------------------------------------------------
                __append('<p>')
                __stream_139867197005760_text_logged_out_link = ''
                __stream_139867200041072 = []
                __append_139867200041072 = __stream_139867200041072.append
                __append_139867200041072('\n            ')
                __stream_139867197005760_text_logged_out_link = []
                __append_139867197005760_text_logged_out_link = __stream_139867197005760_text_logged_out_link.append

                # <Static value=<ast.Dict object at 0x7f355ec60bb0> name=None at 7f355ec635b0> -> __attrs_139867200034256
                __attrs_139867200034256 = _static_139867200031664

                # <a ... (0:0)
                # --------------------------------------------------------
                __append_139867197005760_text_logged_out_link('<a')

                # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867200044144
                __default_139867200044144 = _DEFAULT_MARKER

                # <Substitution 'string:${portal_url}/@@plone-root-logout' (30:36)> -> __attr_href
                __token = 1204
                try:
                    __zt_tmp = __attrs_139867200034256
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_139867356405696('string', '${portal_url}/@@plone-root-logout', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append_139867197005760_text_logged_out_link((' href="%s"' % __attr_href))
                __append_139867197005760_text_logged_out_link('>')
                __stream_139867200042800 = []
                __append_139867200042800 = __stream_139867200042800.append
                __append_139867200042800('\n                Visit this link\n            ')
                __msgid_139867200042800 = __re_whitespace(''.join(__stream_139867200042800)).strip()
                if __msgid_139867200042800:
                    __append_139867197005760_text_logged_out_link(translate(__msgid_139867200042800, mapping=None, default=__msgid_139867200042800, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append_139867197005760_text_logged_out_link('</a>')
                __append_139867200041072('${text_logged_out_link}')
                __stream_139867197005760_text_logged_out_link = ''.join(__stream_139867197005760_text_logged_out_link)
                __append_139867200041072("\n            and click 'Cancel' when prompted with an authentication prompt.\n        ")
                __msgid_139867200041072 = __re_whitespace(''.join(__stream_139867200041072)).strip()
                if __msgid_139867200041072:
                    __append(translate(__msgid_139867200041072, mapping={'text_logged_out_link': __stream_139867197005760_text_logged_out_link, }, default=__msgid_139867200041072, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</p>\n    </div>\n\n\n')
            _slots = econtext['__slot_main'] = _deque((__fill_main, ))

            # <Value 'context/@@main_template/macros/master' (5:23)> -> __macro
            __token = 255
            try:
                __zt_tmp = __attrs_139867200187664
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_139867356405696('path', 'context/@@main_template/macros/master', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            __token = 255
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139867199083712 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139867199083712
            __i18n_domain = __previous_i18n_domain_139867200184640
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }