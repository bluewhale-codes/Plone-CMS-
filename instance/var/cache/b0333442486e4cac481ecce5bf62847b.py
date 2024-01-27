# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/Products/CMFPlone/browser/templates/error_message.pt'

__tokens = {390: ('options/error_type|nothing', 11, 26), 441: (' options/error_tb|nothin', 12, 23), 494: ('d options/error_log_id|nothi', 13, 26), 567: ("python:err_type == 'NotFound'", 15, 39), 651: ('nocall:view/@@plone_redirector_view', 17, 51), 1699: ('string:${context/portal_url}/contact-info', 35, 48), 2055: ('redirection_view/find_first_parent', 43, 58), 2149: (' redirection_view/search_for_simila', 44, 58), 2241: ('w context/@@plo', 45, 54), 2311: ('ry context/portal_regis', 46, 51), 2396: ("ion python:registry['plone.types_use_view_action_in_listin", 47, 57), 2512: ("ngth python:registry['plone.search_results_description_len", 48, 52), 2632: ('tring nocall:plone_view/normalize', 49, 55), 2722: ('python:first_parent is not None or similar_items', 50, 48), 3031: ('first_parent/absolute_url | nothing', 56, 52), 3124: ('first_parent/absolute_url', 57, 55), 3206: (" python:hasattr(first_parent, 'getTypeInfo') and first_parent.getTypeInfo().getId(", 58, 55), 3337: ("l python:result_url + '/view' if result_type in use_view_action else result_u", 59, 46), 3466: ('result_type', 60, 47), 3596: ("python:' state-' + context.portal_workflow.getInfoFor(first_parent, 'review_state', '')", 62, 67), 3521: ('${url}', 61, 41), 3523: ('url', 61, 43), 3743: ("python:'contenttype-' + normalizeString(result_type) + item_wf_state_class", 63, 57), 3819: ('${first_parent/Title}', 63, 133), 3821: ('first_parent/Title', 63, 135), 3896: ('python:plone_view.cropText(first_parent.Description(), desc_length)', 64, 51), 4134: ('similar_items', 68, 53), 4205: ('similar/getURL', 69, 55), 4276: (' similar/portal_typ', 70, 55), 4344: ("l python:result_url + '/view' if result_type in use_view_action else result_u", 71, 46), 4543: ('string: state-${similar/review_state}', 73, 67), 4468: ('${url}', 72, 41), 4470: ('url', 72, 43), 4640: ("python:'contenttype-' + normalizeString(result_type) + item_wf_state_class", 74, 57), 4716: ('${similar/pretty_title_or_id}', 74, 133), 4718: ('similar/pretty_title_or_id', 74, 135), 4801: ("python:plone_view.cropText(similar.Description or '', desc_length)", 75, 51), 5269: ('view/is_manager', 89, 35), 5202: ("python: err_type != 'NotFound'", 88, 41), 5557: ('isManager', 97, 36), 5756: ('err_tb', 102, 37), 5830: ('not:isManager', 105, 40), 6231: ('string:${context/portal_url}/contact-info', 111, 44), 261: ('context/@@main_template/macros/master', 6, 23), 261: ('context/@@main_template/macros/master', 6, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from collections import deque as _deque
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139867308484320 = {'href': '#', }
_static_139867308959792 = {'id': 'content-core', }
_static_139867308951344 = {'class': 'documentFirstHeading', }
_static_139867308950336 = {'class': 'discreet', }
_static_139867308959456 = {'href': '${url}', 'class': "python:'contenttype-' + normalizeString(result_type) + item_wf_state_class", }
_static_139867308961040 = {'class': 'discreet', }
_static_139867308963968 = {'href': '${url}', 'class': "python:'contenttype-' + normalizeString(result_type) + item_wf_state_class", }
_static_139867308969504 = {'id': 'page-not-found-list', }
_static_139867308969888 = {'href': '#', }
_static_139867308976320 = {'class': 'discreet', }
_static_139867308977664 = {'class': 'description', }
_static_139867308979104 = {'id': 'content-core', }
_static_139867308980304 = {'class': 'documentFirstHeading', }
_static_139867356405408 = __C2ZContextWrapper
_static_139867356405696 = __compile_zt_expr
_static_139867308520448 = 'master'
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

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867308510320
            __attrs_139867308510320 = _static_139867362323344
            __previous_i18n_domain_139867308508832 = __i18n_domain
            __i18n_domain = 'plone'
            __backup_macroname_139867360560448 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f35653d7400> name=None at 7f35653d4670> -> __value
            __value = _static_139867308520448
            econtext['macroname'] = __value

            def __fill_main(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867308519536
                __attrs_139867308519536 = _static_139867362323344
                __backup_err_type_139867343985520 = get('err_type', __marker)

                # <Value 'options/error_type|nothing' (11:26)> -> __value
                __token = 390
                try:
                    __zt_tmp = __attrs_139867308519536
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139867356405696('path', 'options/error_type|nothing', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                econtext['err_type'] = __value
                __backup_err_tb_139867340853680 = get('err_tb', __marker)

                # <Value 'options/error_tb|nothing' (12:23)> -> __value
                __token = 441
                try:
                    __zt_tmp = __attrs_139867308519536
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139867356405696('path', 'options/error_tb|nothing', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                econtext['err_tb'] = __value
                __backup_err_log_id_139867340860304 = get('err_log_id', __marker)

                # <Value 'options/error_log_id|nothing' (13:26)> -> __value
                __token = 494
                try:
                    __zt_tmp = __attrs_139867308519536
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139867356405696('path', 'options/error_log_id|nothing', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                econtext['err_log_id'] = __value
                __append('\n\n        ')

                # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867308981936
                __attrs_139867308981936 = _static_139867362323344

                # <Value "python:err_type == 'NotFound'" (15:39)> -> __condition
                __token = 567
                try:
                    __zt_tmp = __attrs_139867308981936
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139867356405696('python', "err_type == 'NotFound'", econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                if __condition:
                    __append('\n\n            ')

                    # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867308981648
                    __attrs_139867308981648 = _static_139867362323344
                    __backup_redirection_view_139867342604896 = get('redirection_view', __marker)

                    # <Value 'nocall:view/@@plone_redirector_view' (17:51)> -> __value
                    __token = 651
                    try:
                        __zt_tmp = __attrs_139867308981648
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_139867356405696('nocall', 'view/@@plone_redirector_view', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                    econtext['redirection_view'] = __value
                    __append('\n\n                ')

                    # <Static value=<ast.Dict object at 0x7f3565447850> name=None at 7f35654479d0> -> __attrs_139867308979968
                    __attrs_139867308979968 = _static_139867308980304

                    # <h1 ... (0:0)
                    # --------------------------------------------------------
                    __append('<h1 class="documentFirstHeading">')
                    __stream_139867308980832 = []
                    __append_139867308980832 = __stream_139867308980832.append
                    __append_139867308980832('\n                    This page does not seem to exist&hellip;\n                ')
                    __msgid_139867308980832 = __re_whitespace(''.join(__stream_139867308980832)).strip()
                    if 'heading_site_there_seems_to_be_an_error':
                        __append(translate('heading_site_there_seems_to_be_an_error', mapping=None, default=__msgid_139867308980832, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</h1>\n\n                ')

                    # <Static value=<ast.Dict object at 0x7f35654473a0> name=None at 7f3565447370> -> __attrs_139867308978720
                    __attrs_139867308978720 = _static_139867308979104

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div id="content-core">\n                    ')

                    # <Static value=<ast.Dict object at 0x7f3565446e00> name=None at 7f3565446dd0> -> __attrs_139867308977280
                    __attrs_139867308977280 = _static_139867308977664

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append('<p class="description">')
                    __stream_139867308978144 = []
                    __append_139867308978144 = __stream_139867308978144.append
                    __append_139867308978144('\n \t                    We apologize for the inconvenience, but the page you were trying to access is not at this address.\n                        You can use the links below to help you find what you are looking for.\n                     ')
                    __msgid_139867308978144 = __re_whitespace(''.join(__stream_139867308978144)).strip()
                    if 'description_site_error':
                        __append(translate('description_site_error', mapping=None, default=__msgid_139867308978144, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</p>\n\n                    ')

                    # <Static value=<ast.Dict object at 0x7f35654468c0> name=None at 7f3565446890> -> __attrs_139867308975936
                    __attrs_139867308975936 = _static_139867308976320

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append('<p class="discreet">')
                    __stream_139867347280480_site_admin = ''
                    __stream_139867308976800 = []
                    __append_139867308976800 = __stream_139867308976800.append
                    __append_139867308976800('\n                        If you are certain you have the correct web address but are encountering an error, please\n                        contact the ')
                    __stream_139867347280480_site_admin = []
                    __append_139867347280480_site_admin = __stream_139867347280480_site_admin.append

                    # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867308973056
                    __attrs_139867308973056 = _static_139867362323344

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append_139867347280480_site_admin('<span>\n                        ')

                    # <Static value=<ast.Dict object at 0x7f3565444fa0> name=None at 7f3565445300> -> __attrs_139867308969840
                    __attrs_139867308969840 = _static_139867308969888

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append_139867347280480_site_admin('<a')

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867308972960
                    __default_139867308972960 = _DEFAULT_MARKER

                    # <Substitution 'string:${context/portal_url}/contact-info' (35:48)> -> __attr_href
                    __token = 1699
                    try:
                        __zt_tmp = __attrs_139867308969840
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_139867356405696('string', '${context/portal_url}/contact-info', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '#', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append_139867347280480_site_admin((' href="%s"' % __attr_href))
                    __append_139867347280480_site_admin('>')
                    __stream_139867308973920 = []
                    __append_139867308973920 = __stream_139867308973920.append
                    __append_139867308973920('site administration')
                    __msgid_139867308973920 = __re_whitespace(''.join(__stream_139867308973920)).strip()
                    if 'label_site_administration':
                        __append_139867347280480_site_admin(translate('label_site_administration', mapping=None, default=__msgid_139867308973920, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append_139867347280480_site_admin('</a></span>')
                    __append_139867308976800('${site_admin}')
                    __stream_139867347280480_site_admin = ''.join(__stream_139867347280480_site_admin)
                    __append_139867308976800('.\n                    ')
                    __msgid_139867308976800 = __re_whitespace(''.join(__stream_139867308976800)).strip()
                    if 'description_site_error_mail_site_admin':
                        __append(translate('description_site_error_mail_site_admin', mapping={'site_admin': __stream_139867347280480_site_admin, }, default=__msgid_139867308976800, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</p>\n\n                    ')

                    # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867308973584
                    __attrs_139867308973584 = _static_139867362323344

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append('<p>')
                    __stream_139867308972288 = []
                    __append_139867308972288 = __stream_139867308972288.append
                    __append_139867308972288('\n                    Thank you.\n                    ')
                    __msgid_139867308972288 = __re_whitespace(''.join(__stream_139867308972288)).strip()
                    if 'description_site_error_thank_you':
                        __append(translate('description_site_error_thank_you', mapping=None, default=__msgid_139867308972288, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</p>\n\n                    <!-- Offer search results for suggestions -->\n                    ')

                    # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867308972240
                    __attrs_139867308972240 = _static_139867362323344
                    __backup_first_parent_139867344185152 = get('first_parent', __marker)

                    # <Value 'redirection_view/find_first_parent' (43:58)> -> __value
                    __token = 2055
                    try:
                        __zt_tmp = __attrs_139867308972240
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_139867356405696('path', 'redirection_view/find_first_parent', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                    econtext['first_parent'] = __value
                    __backup_similar_items_139867344182608 = get('similar_items', __marker)

                    # <Value 'redirection_view/search_for_similar' (44:58)> -> __value
                    __token = 2149
                    try:
                        __zt_tmp = __attrs_139867308972240
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_139867356405696('path', 'redirection_view/search_for_similar', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                    econtext['similar_items'] = __value
                    __backup_plone_view_139867346834032 = get('plone_view', __marker)

                    # <Value 'context/@@plone' (45:54)> -> __value
                    __token = 2241
                    try:
                        __zt_tmp = __attrs_139867308972240
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_139867356405696('path', 'context/@@plone', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                    econtext['plone_view'] = __value
                    __backup_registry_139867344189712 = get('registry', __marker)

                    # <Value 'context/portal_registry' (46:51)> -> __value
                    __token = 2311
                    try:
                        __zt_tmp = __attrs_139867308972240
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_139867356405696('path', 'context/portal_registry', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                    econtext['registry'] = __value
                    __backup_use_view_action_139867344180736 = get('use_view_action', __marker)

                    # <Value "python:registry['plone.types_use_view_action_in_listings']" (47:57)> -> __value
                    __token = 2396
                    try:
                        __zt_tmp = __attrs_139867308972240
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_139867356405696('python', "registry['plone.types_use_view_action_in_listings']", econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                    econtext['use_view_action'] = __value
                    __backup_desc_length_139867345777424 = get('desc_length', __marker)

                    # <Value "python:registry['plone.search_results_description_length']" (48:52)> -> __value
                    __token = 2512
                    try:
                        __zt_tmp = __attrs_139867308972240
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_139867356405696('python', "registry['plone.search_results_description_length']", econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                    econtext['desc_length'] = __value
                    __backup_normalizeString_139867345576160 = get('normalizeString', __marker)

                    # <Value 'nocall:plone_view/normalizeString' (49:55)> -> __value
                    __token = 2632
                    try:
                        __zt_tmp = __attrs_139867308972240
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_139867356405696('nocall', 'plone_view/normalizeString', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                    econtext['normalizeString'] = __value

                    # <Value 'python:first_parent is not None or similar_items' (50:48)> -> __condition
                    __token = 2722
                    try:
                        __zt_tmp = __attrs_139867308972240
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_139867356405696('python', 'first_parent is not None or similar_items', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                    if __condition:
                        __append('\n\n                        ')

                        # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867308968352
                        __attrs_139867308968352 = _static_139867362323344

                        # <h2 ... (0:0)
                        # --------------------------------------------------------
                        __append('<h2>')
                        __stream_139867308969216 = []
                        __append_139867308969216 = __stream_139867308969216.append
                        __append_139867308969216('You might have been looking for&hellip;')
                        __msgid_139867308969216 = __re_whitespace(''.join(__stream_139867308969216)).strip()
                        if 'heading_not_found_suggestions':
                            __append(translate('heading_not_found_suggestions', mapping=None, default=__msgid_139867308969216, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</h2>\n                        ')

                        # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867308966288
                        __attrs_139867308966288 = _static_139867362323344

                        # <nav ... (0:0)
                        # --------------------------------------------------------
                        __append('<nav>\n                        ')

                        # <Static value=<ast.Dict object at 0x7f3565444e20> name=None at 7f3565445840> -> __attrs_139867308957872
                        __attrs_139867308957872 = _static_139867308969504

                        # <ul ... (0:0)
                        # --------------------------------------------------------
                        __append('<ul id="page-not-found-list">\n\n                        ')

                        # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867308962480
                        __attrs_139867308962480 = _static_139867362323344

                        # <Value 'first_parent/absolute_url | nothing' (56:52)> -> __condition
                        __token = 3031
                        try:
                            __zt_tmp = __attrs_139867308962480
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_139867356405696('path', 'first_parent/absolute_url | nothing', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                        if __condition:
                            __append('\n                            ')

                            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867308963344
                            __attrs_139867308963344 = _static_139867362323344
                            __backup_result_url_139867346830720 = get('result_url', __marker)

                            # <Value 'first_parent/absolute_url' (57:55)> -> __value
                            __token = 3124
                            try:
                                __zt_tmp = __attrs_139867308963344
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_139867356405696('path', 'first_parent/absolute_url', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                            econtext['result_url'] = __value
                            __backup_result_type_139867340863376 = get('result_type', __marker)

                            # <Value "python:hasattr(first_parent, 'getTypeInfo') and first_parent.getTypeInfo().getId()" (58:55)> -> __value
                            __token = 3206
                            try:
                                __zt_tmp = __attrs_139867308963344
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_139867356405696('python', "hasattr(first_parent, 'getTypeInfo') and first_parent.getTypeInfo().getId()", econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                            econtext['result_type'] = __value
                            __backup_url_139867341215712 = get('url', __marker)

                            # <Value "python:result_url + '/view' if result_type in use_view_action else result_url" (59:46)> -> __value
                            __token = 3337
                            try:
                                __zt_tmp = __attrs_139867308963344
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_139867356405696('python', "result_url + '/view' if result_type in use_view_action else result_url", econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                            econtext['url'] = __value

                            # <Value 'result_type' (60:47)> -> __condition
                            __token = 3466
                            try:
                                __zt_tmp = __attrs_139867308963344
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_139867356405696('path', 'result_type', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                            if __condition:

                                # <li ... (0:0)
                                # --------------------------------------------------------
                                __append('<li>\n                                ')

                                # <Static value=<ast.Dict object at 0x7f3565443880> name=None at 7f3565440dc0> -> __attrs_139867308961376
                                __attrs_139867308961376 = _static_139867308963968
                                __backup_item_wf_state_class_139867341216912 = get('item_wf_state_class', __marker)

                                # <Value "python:' state-' + context.portal_workflow.getInfoFor(first_parent, 'review_state', '')" (62:67)> -> __value
                                __token = 3596
                                try:
                                    __zt_tmp = __attrs_139867308961376
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __value = _static_139867356405696('python', "' state-' + context.portal_workflow.getInfoFor(first_parent, 'review_state', '')", econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                                econtext['item_wf_state_class'] = __value

                                # <a ... (0:0)
                                # --------------------------------------------------------
                                __append('<a')

                                # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867308963584
                                __default_139867308963584 = _DEFAULT_MARKER

                                # <Interpolation value=<Substitution '${url}' (61:41)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f35654434f0> -> __attr_href
                                __token = 3521
                                __token = 3523
                                try:
                                    __zt_tmp = __attrs_139867308961376
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_href = _static_139867356405696('path', 'url', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
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

                                # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867308965024
                                __default_139867308965024 = _DEFAULT_MARKER

                                # <Substitution "python:'contenttype-' + normalizeString(result_type) + item_wf_state_class" (63:57)> -> __attr_class
                                __token = 3743
                                try:
                                    __zt_tmp = __attrs_139867308961376
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_class = _static_139867356405696('python', "'contenttype-' + normalizeString(result_type) + item_wf_state_class", econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                                __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                                if (__attr_class is not None):
                                    __append((' class="%s"' % __attr_class))
                                __append('>')

                                # <Interpolation value=<Substitution '${first_parent/Title}' (63:133)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f3565442fe0> -> __content_139867442113136
                                __token = 3819
                                __token = 3821
                                try:
                                    __zt_tmp = __attrs_139867308961376
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __content_139867442113136 = _static_139867356405696('path', 'first_parent/Title', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                                __content_139867442113136 = __quote(__content_139867442113136, '\x00', '&#0;', None, None)
                                __content_139867442113136 = __content_139867442113136
                                if (__content_139867442113136 is None):
                                    pass
                                else:
                                    if (__content_139867442113136 is None):
                                        __content_139867442113136 = None
                                    else:
                                        __tt = type(__content_139867442113136)
                                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                                            __content_139867442113136 = str(__content_139867442113136)
                                        else:
                                            if (__tt is bytes):
                                                __content_139867442113136 = decode(__content_139867442113136)
                                            else:
                                                if (__tt is not str):
                                                    try:
                                                        __content_139867442113136 = __content_139867442113136.__html__
                                                    except get('AttributeError', AttributeError):
                                                        __converted = convert(__content_139867442113136)
                                                        __content_139867442113136 = (str(__content_139867442113136) if (__content_139867442113136 is __converted) else __converted)
                                                    else:
                                                        __content_139867442113136 = __content_139867442113136()
                                if (__content_139867442113136 is not None):
                                    __append(__content_139867442113136)
                                __append('</a>')
                                if (__backup_item_wf_state_class_139867341216912 is __marker):
                                    del econtext['item_wf_state_class']
                                else:
                                    econtext['item_wf_state_class'] = __backup_item_wf_state_class_139867341216912
                                __append('\n                                ')

                                # <Static value=<ast.Dict object at 0x7f3565442d10> name=None at 7f3565442d70> -> __attrs_139867308957344
                                __attrs_139867308957344 = _static_139867308961040

                                # <span ... (0:0)
                                # --------------------------------------------------------
                                __append('<span class="discreet">')

                                # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867308959888
                                __default_139867308959888 = _DEFAULT_MARKER

                                # <Value 'python:plone_view.cropText(first_parent.Description(), desc_length)' (64:51)> -> __cache_139867308961712
                                __token = 3896
                                try:
                                    __zt_tmp = __attrs_139867308957344
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __cache_139867308961712 = _static_139867356405696('python', 'plone_view.cropText(first_parent.Description(), desc_length)', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))

                                # <BinOp left=<Value 'python:plone_view.cropText(first_parent.Description(), desc_length)' (64:51)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f3568756860> at 7f35654430a0> -> __condition
                                __expression = __cache_139867308961712

                                # <Symbol value=<DEFAULT> at 7f3568756860> -> __value
                                __value = _DEFAULT_MARKER
                                __condition = (__expression is __value)
                                if __condition:
                                    __append(' Description ')
                                else:
                                    __content = __cache_139867308961712
                                    __content = __quote(__content, None, '\xad', None, None)
                                    if (__content is not None):
                                        __append(__content)
                                __append('</span>\n                            </li>')
                            if (__backup_url_139867341215712 is __marker):
                                del econtext['url']
                            else:
                                econtext['url'] = __backup_url_139867341215712
                            if (__backup_result_type_139867340863376 is __marker):
                                del econtext['result_type']
                            else:
                                econtext['result_type'] = __backup_result_type_139867340863376
                            if (__backup_result_url_139867346830720 is __marker):
                                del econtext['result_url']
                            else:
                                econtext['result_url'] = __backup_result_url_139867346830720
                            __append('\n                        ')
                        __append('\n\n                        ')

                        # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867308957104
                        __attrs_139867308957104 = _static_139867362323344
                        __backup_similar_139867340861936 = get('similar', __marker)

                        # <Value 'similar_items' (68:53)> -> __iterator
                        __token = 4134
                        try:
                            __zt_tmp = __attrs_139867308957104
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __iterator = _static_139867356405696('path', 'similar_items', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                        (__iterator, ____index_139867308956384, ) = getname('repeat')('similar', __iterator)
                        econtext['similar'] = None
                        for __item in __iterator:
                            econtext['similar'] = __item
                            __append('\n                            ')

                            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867308957920
                            __attrs_139867308957920 = _static_139867362323344
                            __backup_result_url_139867341216000 = get('result_url', __marker)

                            # <Value 'similar/getURL' (69:55)> -> __value
                            __token = 4205
                            try:
                                __zt_tmp = __attrs_139867308957920
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_139867356405696('path', 'similar/getURL', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                            econtext['result_url'] = __value
                            __backup_result_type_139867340859680 = get('result_type', __marker)

                            # <Value 'similar/portal_type' (70:55)> -> __value
                            __token = 4276
                            try:
                                __zt_tmp = __attrs_139867308957920
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_139867356405696('path', 'similar/portal_type', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                            econtext['result_type'] = __value
                            __backup_url_139867341218352 = get('url', __marker)

                            # <Value "python:result_url + '/view' if result_type in use_view_action else result_url" (71:46)> -> __value
                            __token = 4344
                            try:
                                __zt_tmp = __attrs_139867308957920
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_139867356405696('python', "result_url + '/view' if result_type in use_view_action else result_url", econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                            econtext['url'] = __value

                            # <li ... (0:0)
                            # --------------------------------------------------------
                            __append('<li>\n                                ')

                            # <Static value=<ast.Dict object at 0x7f35654426e0> name=None at 7f3565441c30> -> __attrs_139867308955664
                            __attrs_139867308955664 = _static_139867308959456
                            __backup_item_wf_state_class_139867341218256 = get('item_wf_state_class', __marker)

                            # <Value 'string: state-${similar/review_state}' (73:67)> -> __value
                            __token = 4543
                            try:
                                __zt_tmp = __attrs_139867308955664
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_139867356405696('string', ' state-${similar/review_state}', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                            econtext['item_wf_state_class'] = __value

                            # <a ... (0:0)
                            # --------------------------------------------------------
                            __append('<a')

                            # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867308958064
                            __default_139867308958064 = _DEFAULT_MARKER

                            # <Interpolation value=<Substitution '${url}' (72:41)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f3565441c90> -> __attr_href
                            __token = 4468
                            __token = 4470
                            try:
                                __zt_tmp = __attrs_139867308955664
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_href = _static_139867356405696('path', 'url', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
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

                            # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867308952448
                            __default_139867308952448 = _DEFAULT_MARKER

                            # <Substitution "python:'contenttype-' + normalizeString(result_type) + item_wf_state_class" (74:57)> -> __attr_class
                            __token = 4640
                            try:
                                __zt_tmp = __attrs_139867308955664
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_class = _static_139867356405696('python', "'contenttype-' + normalizeString(result_type) + item_wf_state_class", econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                            if (__attr_class is not None):
                                __append((' class="%s"' % __attr_class))
                            __append('>')

                            # <Interpolation value=<Substitution '${similar/pretty_title_or_id}' (74:133)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f3565440f40> -> __content_139867442113136
                            __token = 4716
                            __token = 4718
                            try:
                                __zt_tmp = __attrs_139867308955664
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __content_139867442113136 = _static_139867356405696('path', 'similar/pretty_title_or_id', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                            __content_139867442113136 = __quote(__content_139867442113136, '\x00', '&#0;', None, None)
                            __content_139867442113136 = __content_139867442113136
                            if (__content_139867442113136 is None):
                                pass
                            else:
                                if (__content_139867442113136 is None):
                                    __content_139867442113136 = None
                                else:
                                    __tt = type(__content_139867442113136)
                                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                                        __content_139867442113136 = str(__content_139867442113136)
                                    else:
                                        if (__tt is bytes):
                                            __content_139867442113136 = decode(__content_139867442113136)
                                        else:
                                            if (__tt is not str):
                                                try:
                                                    __content_139867442113136 = __content_139867442113136.__html__
                                                except get('AttributeError', AttributeError):
                                                    __converted = convert(__content_139867442113136)
                                                    __content_139867442113136 = (str(__content_139867442113136) if (__content_139867442113136 is __converted) else __converted)
                                                else:
                                                    __content_139867442113136 = __content_139867442113136()
                            if (__content_139867442113136 is not None):
                                __append(__content_139867442113136)
                            __append('</a>')
                            if (__backup_item_wf_state_class_139867341218256 is __marker):
                                del econtext['item_wf_state_class']
                            else:
                                econtext['item_wf_state_class'] = __backup_item_wf_state_class_139867341218256
                            __append('\n                                ')

                            # <Static value=<ast.Dict object at 0x7f3565440340> name=None at 7f3565440370> -> __attrs_139867308949952
                            __attrs_139867308949952 = _static_139867308950336

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span class="discreet">')

                            # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867308951872
                            __default_139867308951872 = _DEFAULT_MARKER

                            # <Value "python:plone_view.cropText(similar.Description or '', desc_length)" (75:51)> -> __cache_139867308953600
                            __token = 4801
                            try:
                                __zt_tmp = __attrs_139867308949952
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_139867308953600 = _static_139867356405696('python', "plone_view.cropText(similar.Description or '', desc_length)", econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))

                            # <BinOp left=<Value "python:plone_view.cropText(similar.Description or '', desc_length)" (75:51)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f3568756860> at 7f3565440250> -> __condition
                            __expression = __cache_139867308953600

                            # <Symbol value=<DEFAULT> at 7f3568756860> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                __append(' Description ')
                            else:
                                __content = __cache_139867308953600
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append(__content)
                            __append('</span>\n                            </li>')
                            if (__backup_url_139867341218352 is __marker):
                                del econtext['url']
                            else:
                                econtext['url'] = __backup_url_139867341218352
                            if (__backup_result_type_139867340859680 is __marker):
                                del econtext['result_type']
                            else:
                                econtext['result_type'] = __backup_result_type_139867340859680
                            if (__backup_result_url_139867341216000 is __marker):
                                del econtext['result_url']
                            else:
                                econtext['result_url'] = __backup_result_url_139867341216000
                            __append('\n                        ')
                            ____index_139867308956384 -= 1
                            if (____index_139867308956384 > 0):
                                __append('')
                        if (__backup_similar_139867340861936 is __marker):
                            del econtext['similar']
                        else:
                            econtext['similar'] = __backup_similar_139867340861936
                        __append('\n\n                        </ul>\n                        </nav>\n\n                    ')
                    if (__backup_normalizeString_139867345576160 is __marker):
                        del econtext['normalizeString']
                    else:
                        econtext['normalizeString'] = __backup_normalizeString_139867345576160
                    if (__backup_desc_length_139867345777424 is __marker):
                        del econtext['desc_length']
                    else:
                        econtext['desc_length'] = __backup_desc_length_139867345777424
                    if (__backup_use_view_action_139867344180736 is __marker):
                        del econtext['use_view_action']
                    else:
                        econtext['use_view_action'] = __backup_use_view_action_139867344180736
                    if (__backup_registry_139867344189712 is __marker):
                        del econtext['registry']
                    else:
                        econtext['registry'] = __backup_registry_139867344189712
                    if (__backup_plone_view_139867346834032 is __marker):
                        del econtext['plone_view']
                    else:
                        econtext['plone_view'] = __backup_plone_view_139867346834032
                    if (__backup_similar_items_139867344182608 is __marker):
                        del econtext['similar_items']
                    else:
                        econtext['similar_items'] = __backup_similar_items_139867344182608
                    if (__backup_first_parent_139867344185152 is __marker):
                        del econtext['first_parent']
                    else:
                        econtext['first_parent'] = __backup_first_parent_139867344185152
                    __append('\n                </div>\n            ')
                    if (__backup_redirection_view_139867342604896 is __marker):
                        del econtext['redirection_view']
                    else:
                        econtext['redirection_view'] = __backup_redirection_view_139867342604896
                    __append('\n\n        ')
                __append('\n\n        ')

                # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867308974112
                __attrs_139867308974112 = _static_139867362323344
                __backup_isManager_139867342603984 = get('isManager', __marker)

                # <Value 'view/is_manager' (89:35)> -> __value
                __token = 5269
                try:
                    __zt_tmp = __attrs_139867308974112
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_139867356405696('path', 'view/is_manager', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                econtext['isManager'] = __value

                # <Value "python: err_type != 'NotFound'" (88:41)> -> __condition
                __token = 5202
                try:
                    __zt_tmp = __attrs_139867308974112
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139867356405696('python', " err_type != 'NotFound'", econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                if __condition:
                    __append('\n\n            ')

                    # <Static value=<ast.Dict object at 0x7f3565440730> name=None at 7f3565440c70> -> __attrs_139867308949904
                    __attrs_139867308949904 = _static_139867308951344

                    # <h1 ... (0:0)
                    # --------------------------------------------------------
                    __append('<h1 class="documentFirstHeading">')
                    __stream_139867308964256 = []
                    __append_139867308964256 = __stream_139867308964256.append
                    __append_139867308964256('\n                We&#8217;re sorry, but there seems to be an error&hellip;\n            ')
                    __msgid_139867308964256 = __re_whitespace(''.join(__stream_139867308964256)).strip()
                    if 'heading_site_error_sorry':
                        __append(translate('heading_site_error_sorry', mapping=None, default=__msgid_139867308964256, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</h1>\n\n            ')

                    # <Static value=<ast.Dict object at 0x7f3565442830> name=None at 7f35654438b0> -> __attrs_139867308954896
                    __attrs_139867308954896 = _static_139867308959792

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div id="content-core">\n                ')

                    # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867308478224
                    __attrs_139867308478224 = _static_139867362323344

                    # <Value 'isManager' (97:36)> -> __condition
                    __token = 5557
                    try:
                        __zt_tmp = __attrs_139867308478224
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_139867356405696('path', 'isManager', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                    if __condition:

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append('<div>\n                   ')

                        # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867308475632
                        __attrs_139867308475632 = _static_139867362323344

                        # <p ... (0:0)
                        # --------------------------------------------------------
                        __append('<p>')
                        __stream_139867308486336 = []
                        __append_139867308486336 = __stream_139867308486336.append
                        __append_139867308486336('\n                   Here is the full error message:\n                   ')
                        __msgid_139867308486336 = __re_whitespace(''.join(__stream_139867308486336)).strip()
                        if 'description_site_admin_full_error':
                            __append(translate('description_site_admin_full_error', mapping=None, default=__msgid_139867308486336, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</p>\n\n                   ')

                        # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867308487488
                        __attrs_139867308487488 = _static_139867362323344

                        # <pre ... (0:0)
                        # --------------------------------------------------------
                        __append('<pre>')

                        # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867308487824
                        __default_139867308487824 = _DEFAULT_MARKER

                        # <Value 'err_tb' (102:37)> -> __cache_139867308486720
                        __token = 5756
                        try:
                            __zt_tmp = __attrs_139867308487488
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_139867308486720 = _static_139867356405696('path', 'err_tb', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))

                        # <BinOp left=<Value 'err_tb' (102:37)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f3568756860> at 7f35653cf8b0> -> __condition
                        __expression = __cache_139867308486720

                        # <Symbol value=<DEFAULT> at 7f3568756860> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_139867308486720
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</pre>\n                </div>')
                    __append('\n\n                ')

                    # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867308486192
                    __attrs_139867308486192 = _static_139867362323344

                    # <Value 'not:isManager' (105:40)> -> __condition
                    __token = 5830
                    try:
                        __zt_tmp = __attrs_139867308486192
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_139867356405696('not', 'isManager', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                    if __condition:
                        __append('\n                    ')

                        # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867308475488
                        __attrs_139867308475488 = _static_139867362323344

                        # <p ... (0:0)
                        # --------------------------------------------------------
                        __append('<p>')
                        __stream_139867347280480_site_admin = ''
                        __stream_139867308490368 = []
                        __append_139867308490368 = __stream_139867308490368.append
                        __append_139867308490368('\n                    If you are certain you have the correct web address but are encountering an error, please\n                    contact the ')
                        __stream_139867347280480_site_admin = []
                        __append_139867347280480_site_admin = __stream_139867347280480_site_admin.append

                        # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867308480240
                        __attrs_139867308480240 = _static_139867362323344

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append_139867347280480_site_admin('<span>\n                    ')

                        # <Static value=<ast.Dict object at 0x7f35653ce6e0> name=None at 7f35653cdf90> -> __attrs_139867308483600
                        __attrs_139867308483600 = _static_139867308484320

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append_139867347280480_site_admin('<a')

                        # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867308483120
                        __default_139867308483120 = _DEFAULT_MARKER

                        # <Substitution 'string:${context/portal_url}/contact-info' (111:44)> -> __attr_href
                        __token = 6231
                        try:
                            __zt_tmp = __attrs_139867308483600
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_139867356405696('string', '${context/portal_url}/contact-info', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', '#', _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append_139867347280480_site_admin((' href="%s"' % __attr_href))
                        __append_139867347280480_site_admin('>')
                        __stream_139867308479808 = []
                        __append_139867308479808 = __stream_139867308479808.append
                        __append_139867308479808('site administration')
                        __msgid_139867308479808 = __re_whitespace(''.join(__stream_139867308479808)).strip()
                        if 'label_site_admin':
                            __append_139867347280480_site_admin(translate('label_site_admin', mapping=None, default=__msgid_139867308479808, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append_139867347280480_site_admin('</a></span>')
                        __append_139867308490368('${site_admin}')
                        __stream_139867347280480_site_admin = ''.join(__stream_139867347280480_site_admin)
                        __append_139867308490368('.\n                    ')
                        __msgid_139867308490368 = __re_whitespace(''.join(__stream_139867308490368)).strip()
                        if 'description_site_error_mail_site_admin':
                            __append(translate('description_site_error_mail_site_admin', mapping={'site_admin': __stream_139867347280480_site_admin, }, default=__msgid_139867308490368, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</p>\n                ')
                    __append('\n            </div>\n\n        ')
                if (__backup_isManager_139867342603984 is __marker):
                    del econtext['isManager']
                else:
                    econtext['isManager'] = __backup_isManager_139867342603984
                __append('\n\n')
                if (__backup_err_log_id_139867340860304 is __marker):
                    del econtext['err_log_id']
                else:
                    econtext['err_log_id'] = __backup_err_log_id_139867340860304
                if (__backup_err_tb_139867340853680 is __marker):
                    del econtext['err_tb']
                else:
                    econtext['err_tb'] = __backup_err_tb_139867340853680
                if (__backup_err_type_139867343985520 is __marker):
                    del econtext['err_type']
                else:
                    econtext['err_type'] = __backup_err_type_139867343985520
            _slots = econtext['__slot_main'] = _deque((__fill_main, ))

            # <Value 'context/@@main_template/macros/master' (6:23)> -> __macro
            __token = 261
            try:
                __zt_tmp = __attrs_139867308510320
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_139867356405696('path', 'context/@@main_template/macros/master', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            __token = 261
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139867360560448 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139867360560448
            __i18n_domain = __previous_i18n_domain_139867308508832
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }