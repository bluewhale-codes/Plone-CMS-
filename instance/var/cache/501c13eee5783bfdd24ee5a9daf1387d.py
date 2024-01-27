# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/Products/CMFPlone/browser/templates/main_template.pt'

__tokens = {71: ('string:&lt;!DOCTYPE ht', 2, 36), 344: ("python:context.restrictedTraverse('@@plone_portal_state')", 8, 31), 426: (" python:context.restrictedTraverse('@@plone_context_state'", 9, 23), 506: ("w python:context.restrictedTraverse('@@plone", 10, 19), 567: ("ns python:context.restrictedTraverse('@@iconresolve", 11, 13), 642: ("out python:context.restrictedTraverse('@@plone_layo", 12, 19), 709: ('lang python:portal_state.langu', 13, 10), 755: (' view nocall:view | nocall: plon', 14, 9), 804: (' dummy python: plone_layout.mark_vie', 15, 9), 862: ('tal_url python:portal_state.port', 16, 13), 921: ("rmission python:context.restrictedTraverse('portal_membership').checkP", 17, 17), 1018: ("roperties python:context.restrictedTraverse('portal_properties').site_", 18, 16), 1117: ("clude_head python:request.get('ajax_include_he", 19, 17), 1184: ('  ajax_load ', 20, 8), 1264: ('lang', 22, 27), 1313: ('provider:plone.httpheaders', 24, 40), 1416: ('provider:plone.htmlhead', 29, 32), 1471: ('nothing', 31, 26), 1757: ('provider:plone.scripts', 38, 32), 1882: ('provider:plone.htmlhead.links', 41, 33), 2021: ('portal_state/is_rtl', 46, 26), 2064: (" python:plone_layout.have_portlets('plone.leftcolumn', view", 47, 22), 2147: ("r python:plone_layout.have_portlets('plone.rightcolumn', vie", 48, 21), 2239: ('ss python:plone_layout.bodyClass(template, vi', 49, 28), 2415: ("  python:context.restrictedTraverse('@@plone_patterns_settings')", 52, 22), 2320: ('body_class', 50, 30), 2359: (" python:isRTL and 'rtl' or 'ltr", 51, 27), 2553: ('provider:plone.toolbar', 55, 32), 2664: ('provider:plone.portaltop', 58, 34), 2760: ('provider:plone.portalheader', 60, 36), 2880: ('provider:plone.mainnavigation', 65, 59), 3032: ('provider:plone.globalstatusmessage', 70, 42), 3211: ('provider:plone.abovecontent', 75, 59), 5052: ('sl', 130, 26), 5150: ('provider:plone.leftcolumn', 132, 38), 5325: ('sr', 138, 26), 5423: ('provider:plone.rightcolumn', 140, 38), 5586: ('provider:plone.portalfooter', 145, 34), 3606: ('provider:plone.abovecontenttitle', 91, 77), 3747: ('context/@@title', 94, 45), 3876: ('provider:plone.belowcontenttitle', 97, 77), 4028: ('context/@@description', 100, 44), 4175: ('provider:plone.belowcontentdescription', 103, 83), 4318: ('provider:plone.abovecontentbody', 107, 74), 4461: ('nothing', 110, 68), 4630: ('provider:plone.belowcontentbody', 115, 74), 4787: ('provider:plone.belowcontent', 119, 69)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139867316472224 = {'id': 'viewlet-below-content', }
_static_139867316481152 = {'id': 'viewlet-below-content-body', }
_static_139867316478032 = {'id': 'content-core', }
_static_139867338811296 = {'id': 'viewlet-above-content-body', }
_static_139867338807168 = {'id': 'viewlet-below-content-description', }
_static_139867338807936 = {'id': 'viewlet-below-content-title', }
_static_139867338808128 = {'id': 'viewlet-above-content-title', }
_static_139867338803520 = {'id': 'content', }
_static_139867316479136 = {'id': 'portal-footer-wrapper', }
_static_139867316472752 = {'id': 'portal-column-two', }
_static_139867309133584 = {'id': 'portal-column-one', }
_static_139867309144432 = {'id': 'portal-column-content', }
_static_139867309130992 = {'id': 'viewlet-above-content', }
_static_139867309142944 = {'id': 'global_statusmessage', }
_static_139867309137232 = {'id': 'portal-mainnavigation', }
_static_139867309144336 = {'id': 'portal-header', }
_static_139867309137088 = {'id': 'portal-top', }
_static_139867308701248 = set([])
_static_139867308690880 = set(['readonly', 'noresize', 'checked', 'declare', 'selected', 'defer', 'multiple', 'nowrap', 'ismap', 'noshade', 'compact', 'disabled', ])
_static_139867344826528 = {'id': 'visual-portal-wrapper', 'class': 'body_class', 'dir': "python:isRTL and 'rtl' or 'ltr'", }
_static_139867344826192 = {'name': 'generator', 'content': 'Plone - https://plone.org/', }
_static_139867308757136 = {'charset': 'utf-8', }
_static_139867308758336 = {'xmlns': 'http://www.w3.org/1999/xhtml', 'lang': 'lang', }
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

    def render_master(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __slot_javascript_head_slot = econtext['__slot_javascript_head_slot'].pop()
        except:
            __slot_javascript_head_slot = None

        try:
            __slot_column_two_slot = econtext['__slot_column_two_slot'].pop()
        except:
            __slot_column_two_slot = None

        try:
            __slot_portlets_two_slot = econtext['__slot_portlets_two_slot'].pop()
        except:
            __slot_portlets_two_slot = None

        try:
            __slot_content = econtext['__slot_content'].pop()
        except:
            __slot_content = None

        try:
            __slot_portlets_one_slot = econtext['__slot_portlets_one_slot'].pop()
        except:
            __slot_portlets_one_slot = None

        try:
            __slot_style_slot = econtext['__slot_style_slot'].pop()
        except:
            __slot_style_slot = None

        try:
            __slot_global_statusmessage = econtext['__slot_global_statusmessage'].pop()
        except:
            __slot_global_statusmessage = None

        try:
            __slot_column_one_slot = econtext['__slot_column_one_slot'].pop()
        except:
            __slot_column_one_slot = None

        try:
            __slot_head_slot = econtext['__slot_head_slot'].pop()
        except:
            __slot_head_slot = None

        try:
            __slot_top_slot = econtext['__slot_top_slot'].pop()
        except:
            __slot_top_slot = None

        try:
            getname = econtext.get_name
            get = econtext.get

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867308762752
            __attrs_139867308762752 = _static_139867362323344
            __append('\n')

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867308764336
            __attrs_139867308764336 = _static_139867362323344

            # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867308765776
            __default_139867308765776 = _DEFAULT_MARKER

            # <Value 'string:<!DOCTYPE html>' (2:36)> -> __cache_139867308764000
            __token = 71
            try:
                __zt_tmp = __attrs_139867308764336
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139867308764000 = _static_139867356405696('string', '<!DOCTYPE html>', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))

            # <BinOp left=<Value 'string:<!DOCTYPE html>' (2:36)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f3568756860> at 7f3565410670> -> __condition
            __expression = __cache_139867308764000

            # <Symbol value=<DEFAULT> at 7f3568756860> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_139867308764000
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x7f3565411540> name=None at 7f35654106a0> -> __attrs_139867308756368
            __attrs_139867308756368 = _static_139867308758336
            __backup_portal_state_139867342976480 = get('portal_state', __marker)

            # <Value "python:context.restrictedTraverse('@@plone_portal_state')" (8:31)> -> __value
            __token = 344
            try:
                __zt_tmp = __attrs_139867308756368
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139867356405696('python', "context.restrictedTraverse('@@plone_portal_state')", econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            econtext['portal_state'] = __value
            __backup_context_state_139867341535888 = get('context_state', __marker)

            # <Value "python:context.restrictedTraverse('@@plone_context_state')" (9:23)> -> __value
            __token = 426
            try:
                __zt_tmp = __attrs_139867308756368
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139867356405696('python', "context.restrictedTraverse('@@plone_context_state')", econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            econtext['context_state'] = __value
            __backup_plone_view_139867346842048 = get('plone_view', __marker)

            # <Value "python:context.restrictedTraverse('@@plone')" (10:19)> -> __value
            __token = 506
            try:
                __zt_tmp = __attrs_139867308756368
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139867356405696('python', "context.restrictedTraverse('@@plone')", econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            econtext['plone_view'] = __value
            __backup_icons_139867341525808 = get('icons', __marker)

            # <Value "python:context.restrictedTraverse('@@iconresolver')" (11:13)> -> __value
            __token = 567
            try:
                __zt_tmp = __attrs_139867308756368
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139867356405696('python', "context.restrictedTraverse('@@iconresolver')", econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            econtext['icons'] = __value
            __backup_plone_layout_139867341530224 = get('plone_layout', __marker)

            # <Value "python:context.restrictedTraverse('@@plone_layout')" (12:19)> -> __value
            __token = 642
            try:
                __zt_tmp = __attrs_139867308756368
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139867356405696('python', "context.restrictedTraverse('@@plone_layout')", econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            econtext['plone_layout'] = __value
            __backup_lang_139867342730624 = get('lang', __marker)

            # <Value 'python:portal_state.language()' (13:10)> -> __value
            __token = 709
            try:
                __zt_tmp = __attrs_139867308756368
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139867356405696('python', 'portal_state.language()', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            econtext['lang'] = __value
            __backup_view_139867343991424 = get('view', __marker)

            # <Value 'nocall:view | nocall: plone_view' (14:9)> -> __value
            __token = 755
            try:
                __zt_tmp = __attrs_139867308756368
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139867356405696('nocall', 'view | nocall: plone_view', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            econtext['view'] = __value
            __backup_dummy_139867341209760 = get('dummy', __marker)

            # <Value 'python: plone_layout.mark_view(view)' (15:9)> -> __value
            __token = 804
            try:
                __zt_tmp = __attrs_139867308756368
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139867356405696('python', ' plone_layout.mark_view(view)', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            econtext['dummy'] = __value
            __backup_portal_url_139867342614592 = get('portal_url', __marker)

            # <Value 'python:portal_state.portal_url()' (16:13)> -> __value
            __token = 862
            try:
                __zt_tmp = __attrs_139867308756368
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139867356405696('python', 'portal_state.portal_url()', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            econtext['portal_url'] = __value
            __backup_checkPermission_139867342975184 = get('checkPermission', __marker)

            # <Value "python:context.restrictedTraverse('portal_membership').checkPermission" (17:17)> -> __value
            __token = 921
            try:
                __zt_tmp = __attrs_139867308756368
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139867356405696('python', "context.restrictedTraverse('portal_membership').checkPermission", econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            econtext['checkPermission'] = __value
            __backup_site_properties_139867341529216 = get('site_properties', __marker)

            # <Value "python:context.restrictedTraverse('portal_properties').site_properties" (18:16)> -> __value
            __token = 1018
            try:
                __zt_tmp = __attrs_139867308756368
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139867356405696('python', "context.restrictedTraverse('portal_properties').site_properties", econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            econtext['site_properties'] = __value
            __backup_ajax_include_head_139867308511088 = get('ajax_include_head', __marker)

            # <Value "python:request.get('ajax_include_head', False)" (19:17)> -> __value
            __token = 1117
            try:
                __zt_tmp = __attrs_139867308756368
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139867356405696('python', "request.get('ajax_include_head', False)", econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            econtext['ajax_include_head'] = __value
            __backup_ajax_load_139867340851472 = get('ajax_load', __marker)

            # <Value 'python:False' (20:8)> -> __value
            __token = 1184
            try:
                __zt_tmp = __attrs_139867308756368
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139867356405696('python', 'False', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            econtext['ajax_load'] = __value
            __previous_i18n_domain_139867308754016 = __i18n_domain
            __i18n_domain = 'plone'

            # <html ... (0:0)
            # --------------------------------------------------------
            __append('<html xmlns="http://www.w3.org/1999/xhtml"')

            # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867308760784
            __default_139867308760784 = _DEFAULT_MARKER

            # <Substitution 'lang' (22:27)> -> __attr_lang
            __token = 1264
            try:
                __zt_tmp = __attrs_139867308756368
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_lang = _static_139867356405696('path', 'lang', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            __attr_lang = __quote(__attr_lang, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_lang is not None):
                __append((' lang="%s"' % __attr_lang))
            __append('>\n\n    ')

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867308755984
            __attrs_139867308755984 = _static_139867362323344

            # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867308761504
            __default_139867308761504 = _DEFAULT_MARKER

            # <Value 'provider:plone.httpheaders' (24:40)> -> __cache_139867308760496
            __token = 1313
            try:
                __zt_tmp = __attrs_139867308755984
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139867308760496 = _static_139867356405696('provider', 'plone.httpheaders', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.httpheaders' (24:40)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f3568756860> at 7f3565411000> -> __condition
            __expression = __cache_139867308760496

            # <Symbol value=<DEFAULT> at 7f3568756860> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_139867308760496
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n\n  ')

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867308765632
            __attrs_139867308765632 = _static_139867362323344

            # <head ... (0:0)
            # --------------------------------------------------------
            __append('<head>\n    ')

            # <Static value=<ast.Dict object at 0x7f3565411090> name=None at 7f3565410f10> -> __attrs_139867308759008
            __attrs_139867308759008 = _static_139867308757136

            # <meta ... (0:0)
            # --------------------------------------------------------
            __append('<meta charset="utf-8" />\n\n    ')

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867308753104
            __attrs_139867308753104 = _static_139867362323344

            # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867308756176
            __default_139867308756176 = _DEFAULT_MARKER

            # <Value 'provider:plone.htmlhead' (29:32)> -> __cache_139867308764576
            __token = 1416
            try:
                __zt_tmp = __attrs_139867308753104
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139867308764576 = _static_139867356405696('provider', 'plone.htmlhead', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.htmlhead' (29:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f3568756860> at 7f3565412260> -> __condition
            __expression = __cache_139867308764576

            # <Symbol value=<DEFAULT> at 7f3568756860> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div />')
            else:
                __content = __cache_139867308764576
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n\n    ')

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867344823312
            __attrs_139867344823312 = _static_139867362323344

            # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867344823504
            __default_139867344823504 = _DEFAULT_MARKER

            # <Value 'nothing' (31:26)> -> __cache_139867344830224
            __token = 1471
            try:
                __zt_tmp = __attrs_139867344823312
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139867344830224 = _static_139867356405696('path', 'nothing', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))

            # <BinOp left=<Value 'nothing' (31:26)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f3568756860> at 7f35676750c0> -> __condition
            __expression = __cache_139867344830224

            # <Symbol value=<DEFAULT> at 7f3568756860> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                __append('\n        Various slots where you can insert elements in the header from a template.\n    ')
            else:
                __content = __cache_139867344830224
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append('\n    ')
            if (__slot_top_slot is None):

                # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867344827920
                __attrs_139867344827920 = _static_139867362323344
            else:
                __slot_top_slot(__stream, econtext.copy(), rcontext)
            __append('\n    ')
            if (__slot_head_slot is None):

                # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867344829984
                __attrs_139867344829984 = _static_139867362323344
            else:
                __slot_head_slot(__stream, econtext.copy(), rcontext)
            __append('\n    ')
            if (__slot_style_slot is None):

                # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867344817408
                __attrs_139867344817408 = _static_139867362323344
            else:
                __slot_style_slot(__stream, econtext.copy(), rcontext)
            __append('\n\n    ')

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867344822496
            __attrs_139867344822496 = _static_139867362323344

            # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867344818128
            __default_139867344818128 = _DEFAULT_MARKER

            # <Value 'provider:plone.scripts' (38:32)> -> __cache_139867344825904
            __token = 1757
            try:
                __zt_tmp = __attrs_139867344822496
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139867344825904 = _static_139867356405696('provider', 'plone.scripts', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.scripts' (38:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f3568756860> at 7f3567674f40> -> __condition
            __expression = __cache_139867344825904

            # <Symbol value=<DEFAULT> at 7f3568756860> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div />')
            else:
                __content = __cache_139867344825904
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n    ')
            if (__slot_javascript_head_slot is None):

                # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867344820048
                __attrs_139867344820048 = _static_139867362323344
            else:
                __slot_javascript_head_slot(__stream, econtext.copy(), rcontext)
            __append('\n\n    ')

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867344829792
            __attrs_139867344829792 = _static_139867362323344

            # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867344829168
            __default_139867344829168 = _DEFAULT_MARKER

            # <Value 'provider:plone.htmlhead.links' (41:33)> -> __cache_139867344819328
            __token = 1882
            try:
                __zt_tmp = __attrs_139867344829792
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139867344819328 = _static_139867356405696('provider', 'plone.htmlhead.links', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.htmlhead.links' (41:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f3568756860> at 7f3567677970> -> __condition
            __expression = __cache_139867344819328

            # <Symbol value=<DEFAULT> at 7f3568756860> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <link ... (0:0)
                # --------------------------------------------------------
                __append('<link />')
            else:
                __content = __cache_139867344819328
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n    ')

            # <Static value=<ast.Dict object at 0x7f3567676f50> name=None at 7f3567677640> -> __attrs_139867344828880
            __attrs_139867344828880 = _static_139867344826192

            # <meta ... (0:0)
            # --------------------------------------------------------
            __append('<meta name="generator" content="Plone - https://plone.org/" />\n\n  </head>\n\n  ')

            # <Static value=<ast.Dict object at 0x7f35676770a0> name=None at 7f3567677e80> -> __attrs_139867344814528
            __attrs_139867344814528 = _static_139867344826528
            __backup_isRTL_139867339908400 = get('isRTL', __marker)

            # <Value 'portal_state/is_rtl' (46:26)> -> __value
            __token = 2021
            try:
                __zt_tmp = __attrs_139867344814528
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139867356405696('path', 'portal_state/is_rtl', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            econtext['isRTL'] = __value
            __backup_sl_139867339907296 = get('sl', __marker)

            # <Value "python:plone_layout.have_portlets('plone.leftcolumn', view)" (47:22)> -> __value
            __token = 2064
            try:
                __zt_tmp = __attrs_139867344814528
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139867356405696('python', "plone_layout.have_portlets('plone.leftcolumn', view)", econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            econtext['sl'] = __value
            __backup_sr_139867339907392 = get('sr', __marker)

            # <Value "python:plone_layout.have_portlets('plone.rightcolumn', view)" (48:21)> -> __value
            __token = 2147
            try:
                __zt_tmp = __attrs_139867344814528
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139867356405696('python', "plone_layout.have_portlets('plone.rightcolumn', view)", econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            econtext['sr'] = __value
            __backup_body_class_139867339908688 = get('body_class', __marker)

            # <Value 'python:plone_layout.bodyClass(template, view)' (49:28)> -> __value
            __token = 2239
            try:
                __zt_tmp = __attrs_139867344814528
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139867356405696('python', 'plone_layout.bodyClass(template, view)', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            econtext['body_class'] = __value

            # <body ... (0:0)
            # --------------------------------------------------------
            __append('<body')

            # <Value "python:context.restrictedTraverse('@@plone_patterns_settings')()" (52:22)> -> __cache_139867344827440
            __token = 2415
            try:
                __zt_tmp = __attrs_139867344814528
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139867344827440 = _static_139867356405696('python', "context.restrictedTraverse('@@plone_patterns_settings')()", econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            if ('id' not in __chain(__cache_139867344827440)):
                __append(' id="visual-portal-wrapper"')

            # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867344826816
            __default_139867344826816 = _DEFAULT_MARKER

            # <Substitution 'body_class' (50:30)> -> __attr_class
            __token = 2320
            try:
                __zt_tmp = __attrs_139867344814528
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_139867356405696('path', 'body_class', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
            if ((__attr_class is not None) and ('class' not in __chain(__cache_139867344827440))):
                __append((' class="%s"' % __attr_class))

            # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867344824416
            __default_139867344824416 = _DEFAULT_MARKER

            # <Substitution "python:isRTL and 'rtl' or 'ltr'" (51:27)> -> __attr_dir
            __token = 2359
            try:
                __zt_tmp = __attrs_139867344814528
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_dir = _static_139867356405696('python', "isRTL and 'rtl' or 'ltr'", econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            __attr_dir = __quote(__attr_dir, '"', '&quot;', None, _DEFAULT_MARKER)
            if ((__attr_dir is not None) and ('dir' not in __chain(__cache_139867344827440))):
                __append((' dir="%s"' % __attr_dir))
            __attr_139867344825376 = __cache_139867344827440
            for (name, value, ) in __attr_139867344825376.items():
                if (name in _static_139867308690880):
                    if not bool(value):
                        continue
                    value = name
                if ((name not in _static_139867308701248) and (value is not None)):
                    if (name in _static_139867308690880):
                        if not bool(value):
                            continue
                        value = name
                    __append((((((' ' + name) + '=') + '"') + __quote(value, '"', '&quot;', None, None)) + '"'))
            __append('>\n\n    ')

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867309145632
            __attrs_139867309145632 = _static_139867362323344

            # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867309134880
            __default_139867309134880 = _DEFAULT_MARKER

            # <Value 'provider:plone.toolbar' (55:32)> -> __cache_139867344824992
            __token = 2553
            try:
                __zt_tmp = __attrs_139867309145632
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139867344824992 = _static_139867356405696('provider', 'plone.toolbar', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.toolbar' (55:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f3568756860> at 7f356546c790> -> __condition
            __expression = __cache_139867344824992

            # <Symbol value=<DEFAULT> at 7f3568756860> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div />')
            else:
                __content = __cache_139867344824992
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n\n    ')

            # <Static value=<ast.Dict object at 0x7f356546dcc0> name=None at 7f356546dc90> -> __attrs_139867309133536
            __attrs_139867309133536 = _static_139867309137088
            __previous_i18n_domain_139867309136272 = __i18n_domain
            __i18n_domain = 'plone'

            # <header ... (0:0)
            # --------------------------------------------------------
            __append('<header id="portal-top">\n      ')

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867309144384
            __attrs_139867309144384 = _static_139867362323344

            # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867309134640
            __default_139867309134640 = _DEFAULT_MARKER

            # <Value 'provider:plone.portaltop' (58:34)> -> __cache_139867309131520
            __token = 2664
            try:
                __zt_tmp = __attrs_139867309144384
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139867309131520 = _static_139867356405696('provider', 'plone.portaltop', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.portaltop' (58:34)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f3568756860> at 7f356546ec50> -> __condition
            __expression = __cache_139867309131520

            # <Symbol value=<DEFAULT> at 7f3568756860> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div />')
            else:
                __content = __cache_139867309131520
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n      ')

            # <Static value=<ast.Dict object at 0x7f356546f910> name=None at 7f356546f760> -> __attrs_139867309135552
            __attrs_139867309135552 = _static_139867309144336

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div id="portal-header">\n        ')

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867309136896
            __attrs_139867309136896 = _static_139867362323344

            # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867309142800
            __default_139867309142800 = _DEFAULT_MARKER

            # <Value 'provider:plone.portalheader' (60:36)> -> __cache_139867309135360
            __token = 2760
            try:
                __zt_tmp = __attrs_139867309136896
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139867309135360 = _static_139867356405696('provider', 'plone.portalheader', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.portalheader' (60:36)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f3568756860> at 7f356546fd90> -> __condition
            __expression = __cache_139867309135360

            # <Symbol value=<DEFAULT> at 7f3568756860> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div />')
            else:
                __content = __cache_139867309135360
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n      </div>\n\n    </header>')
            __i18n_domain = __previous_i18n_domain_139867309136272
            __append('\n\n    ')

            # <Static value=<ast.Dict object at 0x7f356546dd50> name=None at 7f356546c520> -> __attrs_139867309139536
            __attrs_139867309139536 = _static_139867309137232

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div id="portal-mainnavigation">')

            # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867309135216
            __default_139867309135216 = _DEFAULT_MARKER

            # <Value 'provider:plone.mainnavigation' (65:59)> -> __cache_139867309136512
            __token = 2880
            try:
                __zt_tmp = __attrs_139867309139536
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139867309136512 = _static_139867356405696('provider', 'plone.mainnavigation', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.mainnavigation' (65:59)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f3568756860> at 7f356546e9b0> -> __condition
            __expression = __cache_139867309136512

            # <Symbol value=<DEFAULT> at 7f3568756860> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                __append('\n      The main navigation\n    ')
            else:
                __content = __cache_139867309136512
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('</div>\n\n    ')

            # <Static value=<ast.Dict object at 0x7f356546f3a0> name=None at 7f356546c070> -> __attrs_139867309139296
            __attrs_139867309139296 = _static_139867309142944

            # <section ... (0:0)
            # --------------------------------------------------------
            __append('<section id="global_statusmessage">\n      ')

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867309141552
            __attrs_139867309141552 = _static_139867362323344

            # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867309134832
            __default_139867309134832 = _DEFAULT_MARKER

            # <Value 'provider:plone.globalstatusmessage' (70:42)> -> __cache_139867309136224
            __token = 3032
            try:
                __zt_tmp = __attrs_139867309141552
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139867309136224 = _static_139867356405696('provider', 'plone.globalstatusmessage', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.globalstatusmessage' (70:42)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f3568756860> at 7f356546e0e0> -> __condition
            __expression = __cache_139867309136224

            # <Symbol value=<DEFAULT> at 7f3568756860> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_139867309136224
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n      ')
            if (__slot_global_statusmessage is None):

                # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867309136368
                __attrs_139867309136368 = _static_139867362323344

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div>\n      </div>')
            else:
                __slot_global_statusmessage(__stream, econtext.copy(), rcontext)
            __append('\n    </section>\n\n    ')

            # <Static value=<ast.Dict object at 0x7f356546c4f0> name=None at 7f356546ca00> -> __attrs_139867309130128
            __attrs_139867309130128 = _static_139867309130992

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div id="viewlet-above-content">')

            # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867309130224
            __default_139867309130224 = _DEFAULT_MARKER

            # <Value 'provider:plone.abovecontent' (75:59)> -> __cache_139867309139104
            __token = 3211
            try:
                __zt_tmp = __attrs_139867309130128
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139867309139104 = _static_139867356405696('provider', 'plone.abovecontent', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.abovecontent' (75:59)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f3568756860> at 7f356546d5a0> -> __condition
            __expression = __cache_139867309139104

            # <Symbol value=<DEFAULT> at 7f3568756860> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_139867309139104
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('</div>\n\n    ')

            # <Static value=<ast.Dict object at 0x7f356546f970> name=None at 7f356546ecb0> -> __attrs_139867309132624
            __attrs_139867309132624 = _static_139867309144432

            # <article ... (0:0)
            # --------------------------------------------------------
            __append('<article id="portal-column-content">\n\n      ')
            if (__slot_content is None):

                # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867309140832
                __attrs_139867309140832 = _static_139867362323344
                __append('\n\n      ')
                __token = None
                render_content(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append('\n\n      ')
            else:
                __slot_content(__stream, econtext.copy(), rcontext)
            __append('\n    </article>\n\n    ')
            if (__slot_column_one_slot is None):

                # <Static value=<ast.Dict object at 0x7f356546cf10> name=None at 7f356546c550> -> __attrs_139867338811536
                __attrs_139867338811536 = _static_139867309133584

                # <Value 'sl' (130:26)> -> __condition
                __token = 5052
                try:
                    __zt_tmp = __attrs_139867338811536
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139867356405696('path', 'sl', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                if __condition:

                    # <aside ... (0:0)
                    # --------------------------------------------------------
                    __append('<aside id="portal-column-one">\n      ')
                    if (__slot_portlets_one_slot is None):

                        # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867316479232
                        __attrs_139867316479232 = _static_139867362323344
                        __append('\n        ')

                        # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867316476448
                        __attrs_139867316476448 = _static_139867362323344

                        # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867316476928
                        __default_139867316476928 = _DEFAULT_MARKER

                        # <Value 'provider:plone.leftcolumn' (132:38)> -> __cache_139867316476976
                        __token = 5150
                        try:
                            __zt_tmp = __attrs_139867316476448
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_139867316476976 = _static_139867356405696('provider', 'plone.leftcolumn', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))

                        # <BinOp left=<Value 'provider:plone.leftcolumn' (132:38)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f3568756860> at 7f3565b6d900> -> __condition
                        __expression = __cache_139867316476976

                        # <Symbol value=<DEFAULT> at 7f3568756860> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_139867316476976
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        __append('\n      ')
                    else:
                        __slot_portlets_one_slot(__stream, econtext.copy(), rcontext)
                    __append('\n    </aside>')
            else:
                __slot_column_one_slot(__stream, econtext.copy(), rcontext)
            __append('\n\n    ')
            if (__slot_column_two_slot is None):

                # <Static value=<ast.Dict object at 0x7f3565b6cbb0> name=None at 7f3565b6ce50> -> __attrs_139867316481728
                __attrs_139867316481728 = _static_139867316472752

                # <Value 'sr' (138:26)> -> __condition
                __token = 5325
                try:
                    __zt_tmp = __attrs_139867316481728
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139867356405696('path', 'sr', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                if __condition:

                    # <aside ... (0:0)
                    # --------------------------------------------------------
                    __append('<aside id="portal-column-two">\n      ')
                    if (__slot_portlets_two_slot is None):

                        # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867316483648
                        __attrs_139867316483648 = _static_139867362323344
                        __append('\n        ')

                        # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867316479184
                        __attrs_139867316479184 = _static_139867362323344

                        # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867316484848
                        __default_139867316484848 = _DEFAULT_MARKER

                        # <Value 'provider:plone.rightcolumn' (140:38)> -> __cache_139867316483216
                        __token = 5423
                        try:
                            __zt_tmp = __attrs_139867316479184
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_139867316483216 = _static_139867356405696('provider', 'plone.rightcolumn', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))

                        # <BinOp left=<Value 'provider:plone.rightcolumn' (140:38)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f3568756860> at 7f3565b6f910> -> __condition
                        __expression = __cache_139867316483216

                        # <Symbol value=<DEFAULT> at 7f3568756860> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_139867316483216
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        __append('\n      ')
                    else:
                        __slot_portlets_two_slot(__stream, econtext.copy(), rcontext)
                    __append('\n    </aside>')
            else:
                __slot_column_two_slot(__stream, econtext.copy(), rcontext)
            __append('\n\n    ')

            # <Static value=<ast.Dict object at 0x7f3565b6e4a0> name=None at 7f3565b6f7c0> -> __attrs_139867316480672
            __attrs_139867316480672 = _static_139867316479136
            __previous_i18n_domain_139867316480048 = __i18n_domain
            __i18n_domain = 'plone'

            # <footer ... (0:0)
            # --------------------------------------------------------
            __append('<footer id="portal-footer-wrapper">\n      ')

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867316481536
            __attrs_139867316481536 = _static_139867362323344

            # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867316470496
            __default_139867316470496 = _DEFAULT_MARKER

            # <Value 'provider:plone.portalfooter' (145:34)> -> __cache_139867316482352
            __token = 5586
            try:
                __zt_tmp = __attrs_139867316481536
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139867316482352 = _static_139867356405696('provider', 'plone.portalfooter', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.portalfooter' (145:34)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f3568756860> at 7f3565b6e470> -> __condition
            __expression = __cache_139867316482352

            # <Symbol value=<DEFAULT> at 7f3568756860> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div />')
            else:
                __content = __cache_139867316482352
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n    </footer>')
            __i18n_domain = __previous_i18n_domain_139867316480048
            __append('\n\n  </body>')
            if (__backup_body_class_139867339908688 is __marker):
                del econtext['body_class']
            else:
                econtext['body_class'] = __backup_body_class_139867339908688
            if (__backup_sr_139867339907392 is __marker):
                del econtext['sr']
            else:
                econtext['sr'] = __backup_sr_139867339907392
            if (__backup_sl_139867339907296 is __marker):
                del econtext['sl']
            else:
                econtext['sl'] = __backup_sl_139867339907296
            if (__backup_isRTL_139867339908400 is __marker):
                del econtext['isRTL']
            else:
                econtext['isRTL'] = __backup_isRTL_139867339908400
            __append('\n</html>')
            __i18n_domain = __previous_i18n_domain_139867308754016
            if (__backup_ajax_load_139867340851472 is __marker):
                del econtext['ajax_load']
            else:
                econtext['ajax_load'] = __backup_ajax_load_139867340851472
            if (__backup_ajax_include_head_139867308511088 is __marker):
                del econtext['ajax_include_head']
            else:
                econtext['ajax_include_head'] = __backup_ajax_include_head_139867308511088
            if (__backup_site_properties_139867341529216 is __marker):
                del econtext['site_properties']
            else:
                econtext['site_properties'] = __backup_site_properties_139867341529216
            if (__backup_checkPermission_139867342975184 is __marker):
                del econtext['checkPermission']
            else:
                econtext['checkPermission'] = __backup_checkPermission_139867342975184
            if (__backup_portal_url_139867342614592 is __marker):
                del econtext['portal_url']
            else:
                econtext['portal_url'] = __backup_portal_url_139867342614592
            if (__backup_dummy_139867341209760 is __marker):
                del econtext['dummy']
            else:
                econtext['dummy'] = __backup_dummy_139867341209760
            if (__backup_view_139867343991424 is __marker):
                del econtext['view']
            else:
                econtext['view'] = __backup_view_139867343991424
            if (__backup_lang_139867342730624 is __marker):
                del econtext['lang']
            else:
                econtext['lang'] = __backup_lang_139867342730624
            if (__backup_plone_layout_139867341530224 is __marker):
                del econtext['plone_layout']
            else:
                econtext['plone_layout'] = __backup_plone_layout_139867341530224
            if (__backup_icons_139867341525808 is __marker):
                del econtext['icons']
            else:
                econtext['icons'] = __backup_icons_139867341525808
            if (__backup_plone_view_139867346842048 is __marker):
                del econtext['plone_view']
            else:
                econtext['plone_view'] = __backup_plone_view_139867346842048
            if (__backup_context_state_139867341535888 is __marker):
                del econtext['context_state']
            else:
                econtext['context_state'] = __backup_context_state_139867341535888
            if (__backup_portal_state_139867342976480 is __marker):
                del econtext['portal_state']
            else:
                econtext['portal_state'] = __backup_portal_state_139867342976480
            __append('\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_content(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __slot_main = econtext['__slot_main'].pop()
        except:
            __slot_main = None

        try:
            __slot_content_title = econtext['__slot_content_title'].pop()
        except:
            __slot_content_title = None

        try:
            __slot_body = econtext['__slot_body'].pop()
        except:
            __slot_body = None

        try:
            __slot_content_core = econtext['__slot_content_core'].pop()
        except:
            __slot_content_core = None

        try:
            __slot_content_description = econtext['__slot_content_description'].pop()
        except:
            __slot_content_description = None

        try:
            getname = econtext.get_name
            get = econtext.get

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867338810432
            __attrs_139867338810432 = _static_139867362323344
            __append('\n\n        ')
            if (__slot_body is None):

                # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867338802992
                __attrs_139867338802992 = _static_139867362323344
                __append('\n\n          ')

                # <Static value=<ast.Dict object at 0x7f35670b8940> name=None at 7f35670b8220> -> __attrs_139867338802272
                __attrs_139867338802272 = _static_139867338803520

                # <article ... (0:0)
                # --------------------------------------------------------
                __append('<article id="content">\n\n            ')
                if (__slot_main is None):

                    # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867338805584
                    __attrs_139867338805584 = _static_139867362323344
                    __append('\n\n              ')

                    # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867338803328
                    __attrs_139867338803328 = _static_139867362323344

                    # <header ... (0:0)
                    # --------------------------------------------------------
                    __append('<header>\n\n                ')

                    # <Static value=<ast.Dict object at 0x7f35670b9b40> name=None at 7f35670b8fa0> -> __attrs_139867338817200
                    __attrs_139867338817200 = _static_139867338808128

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div id="viewlet-above-content-title">')

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867338806112
                    __default_139867338806112 = _DEFAULT_MARKER

                    # <Value 'provider:plone.abovecontenttitle' (91:77)> -> __cache_139867338815472
                    __token = 3606
                    try:
                        __zt_tmp = __attrs_139867338817200
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139867338815472 = _static_139867356405696('provider', 'plone.abovecontenttitle', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))

                    # <BinOp left=<Value 'provider:plone.abovecontenttitle' (91:77)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f3568756860> at 7f35670b8490> -> __condition
                    __expression = __cache_139867338815472

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_139867338815472
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('</div>\n\n                ')
                    if (__slot_content_title is None):

                        # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867338808608
                        __attrs_139867338808608 = _static_139867362323344
                        __append('\n                  ')

                        # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867338816240
                        __attrs_139867338816240 = _static_139867362323344

                        # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867338817392
                        __default_139867338817392 = _DEFAULT_MARKER

                        # <Value 'context/@@title' (94:45)> -> __cache_139867338808032
                        __token = 3747
                        try:
                            __zt_tmp = __attrs_139867338816240
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_139867338808032 = _static_139867356405696('path', 'context/@@title', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))

                        # <BinOp left=<Value 'context/@@title' (94:45)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f3568756860> at 7f35670b93c0> -> __condition
                        __expression = __cache_139867338808032

                        # <Symbol value=<DEFAULT> at 7f3568756860> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <h1 ... (0:0)
                            # --------------------------------------------------------
                            __append('<h1 />')
                        else:
                            __content = __cache_139867338808032
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        __append('\n                ')
                    else:
                        __slot_content_title(__stream, econtext.copy(), rcontext)
                    __append('\n\n                ')

                    # <Static value=<ast.Dict object at 0x7f35670b9a80> name=None at 7f35670bb340> -> __attrs_139867338808800
                    __attrs_139867338808800 = _static_139867338807936

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div id="viewlet-below-content-title">')

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867338814128
                    __default_139867338814128 = _DEFAULT_MARKER

                    # <Value 'provider:plone.belowcontenttitle' (97:77)> -> __cache_139867338808944
                    __token = 3876
                    try:
                        __zt_tmp = __attrs_139867338808800
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139867338808944 = _static_139867356405696('provider', 'plone.belowcontenttitle', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))

                    # <BinOp left=<Value 'provider:plone.belowcontenttitle' (97:77)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f3568756860> at 7f35670bb8b0> -> __condition
                    __expression = __cache_139867338808944

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_139867338808944
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('</div>\n\n                ')
                    if (__slot_content_description is None):

                        # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867338809904
                        __attrs_139867338809904 = _static_139867362323344
                        __append('\n                  ')

                        # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867338814032
                        __attrs_139867338814032 = _static_139867362323344

                        # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867338814176
                        __default_139867338814176 = _DEFAULT_MARKER

                        # <Value 'context/@@description' (100:44)> -> __cache_139867338812640
                        __token = 4028
                        try:
                            __zt_tmp = __attrs_139867338814032
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_139867338812640 = _static_139867356405696('path', 'context/@@description', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))

                        # <BinOp left=<Value 'context/@@description' (100:44)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f3568756860> at 7f35670ba710> -> __condition
                        __expression = __cache_139867338812640

                        # <Symbol value=<DEFAULT> at 7f3568756860> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <p ... (0:0)
                            # --------------------------------------------------------
                            __append('<p />')
                        else:
                            __content = __cache_139867338812640
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        __append('\n                ')
                    else:
                        __slot_content_description(__stream, econtext.copy(), rcontext)
                    __append('\n\n                ')

                    # <Static value=<ast.Dict object at 0x7f35670b9780> name=None at 7f35670bb460> -> __attrs_139867338813936
                    __attrs_139867338813936 = _static_139867338807168

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div id="viewlet-below-content-description">')

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867338817440
                    __default_139867338817440 = _DEFAULT_MARKER

                    # <Value 'provider:plone.belowcontentdescription' (103:83)> -> __cache_139867338810192
                    __token = 4175
                    try:
                        __zt_tmp = __attrs_139867338813936
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139867338810192 = _static_139867356405696('provider', 'plone.belowcontentdescription', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))

                    # <BinOp left=<Value 'provider:plone.belowcontentdescription' (103:83)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f3568756860> at 7f35670bbdc0> -> __condition
                    __expression = __cache_139867338810192

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_139867338810192
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('</div>\n\n              </header>\n\n              ')

                    # <Static value=<ast.Dict object at 0x7f35670ba7a0> name=None at 7f35670bad70> -> __attrs_139867316470928
                    __attrs_139867316470928 = _static_139867338811296

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div id="viewlet-above-content-body">')

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867338811440
                    __default_139867338811440 = _DEFAULT_MARKER

                    # <Value 'provider:plone.abovecontentbody' (107:74)> -> __cache_139867338811632
                    __token = 4318
                    try:
                        __zt_tmp = __attrs_139867316470928
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139867338811632 = _static_139867356405696('provider', 'plone.abovecontentbody', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))

                    # <BinOp left=<Value 'provider:plone.abovecontentbody' (107:74)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f3568756860> at 7f35670babc0> -> __condition
                    __expression = __cache_139867338811632

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_139867338811632
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('</div>\n\n              ')

                    # <Static value=<ast.Dict object at 0x7f3565b6e050> name=None at 7f3565b6dea0> -> __attrs_139867316478416
                    __attrs_139867316478416 = _static_139867316478032

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div id="content-core">\n                ')
                    if (__slot_content_core is None):

                        # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867316485712
                        __attrs_139867316485712 = _static_139867362323344

                        # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867316472704
                        __default_139867316472704 = _DEFAULT_MARKER

                        # <Value 'nothing' (110:68)> -> __cache_139867316485328
                        __token = 4461
                        try:
                            __zt_tmp = __attrs_139867316485712
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_139867316485328 = _static_139867356405696('path', 'nothing', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))

                        # <BinOp left=<Value 'nothing' (110:68)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f3568756860> at 7f3565b6ebf0> -> __condition
                        __expression = __cache_139867316485328

                        # <Symbol value=<DEFAULT> at 7f3568756860> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('\n                  Page body text\n                ')
                        else:
                            __content = __cache_139867316485328
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                    else:
                        __slot_content_core(__stream, econtext.copy(), rcontext)
                    __append('\n              </div>\n\n              ')

                    # <Static value=<ast.Dict object at 0x7f3565b6ec80> name=None at 7f3565b6e140> -> __attrs_139867316474288
                    __attrs_139867316474288 = _static_139867316481152

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div id="viewlet-below-content-body">')

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867316478512
                    __default_139867316478512 = _DEFAULT_MARKER

                    # <Value 'provider:plone.belowcontentbody' (115:74)> -> __cache_139867316485808
                    __token = 4630
                    try:
                        __zt_tmp = __attrs_139867316474288
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139867316485808 = _static_139867356405696('provider', 'plone.belowcontentbody', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))

                    # <BinOp left=<Value 'provider:plone.belowcontentbody' (115:74)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f3568756860> at 7f3565b6f370> -> __condition
                    __expression = __cache_139867316485808

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_139867316485808
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('</div>\n\n            ')
                else:
                    __slot_main(__stream, econtext.copy(), rcontext)
                __append('\n            ')

                # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867316477984
                __attrs_139867316477984 = _static_139867362323344

                # <footer ... (0:0)
                # --------------------------------------------------------
                __append('<footer>\n              ')

                # <Static value=<ast.Dict object at 0x7f3565b6c9a0> name=None at 7f3565b6c580> -> __attrs_139867316476736
                __attrs_139867316476736 = _static_139867316472224

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div id="viewlet-below-content">')

                # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867316471408
                __default_139867316471408 = _DEFAULT_MARKER

                # <Value 'provider:plone.belowcontent' (119:69)> -> __cache_139867316470880
                __token = 4787
                try:
                    __zt_tmp = __attrs_139867316476736
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_139867316470880 = _static_139867356405696('provider', 'plone.belowcontent', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))

                # <BinOp left=<Value 'provider:plone.belowcontent' (119:69)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f3568756860> at 7f3565b6c9d0> -> __condition
                __expression = __cache_139867316470880

                # <Symbol value=<DEFAULT> at 7f3568756860> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_139867316470880
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('</div>\n            </footer>\n          </article>\n        ')
            else:
                __slot_body(__stream, econtext.copy(), rcontext)
            __append('\n      ')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


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
            __token = None
            render_master(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_master': render_master, 'render_content': render_content, 'render': render, }