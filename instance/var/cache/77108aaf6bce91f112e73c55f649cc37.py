# -*- coding: utf-8 -*-
__filename = 'manage_main'

__tokens = {31: ('here/manage_page_header', 1, 31), 89: ('here/manage_tabs', 3, 29), 238: ("python:getattr(here.aq_explicit, 'has_order_support', 0)", 7, 38), 318: (' modules/AccessControl/getSecurityManage', 8, 22), 392: ("t python: 'position' if has_order_support else 'i", 9, 31), 467: ("ey python:request.get('skey',default_so", 10, 22), 532: ("key python:request.get('rkey','a", 11, 21), 594: ("_alt python:'desc' if rkey=='asc' else ", 12, 24), 666: ('lt_up rkey_alt', 13, 26), 705: ('   obs python: here.manage_get_sortedObjects(sortkey = skey, revkey ', 14, 17), 801: (' my_url string:${context/absolute_url}/man', 15, 19), 905: ('string:${request/URL1}/', 17, 31), 962: ('obs', 19, 30), 1057: ('obs', 20, 89), 1120: ("python:'thead-light sorted_%s'%(request.get('rkey',''))", 21, 57), 1550: ('string:Sort ${rkey_alt_up} by meta-type', 29, 39), 1628: (' string:${my_url}?skey=meta_type&rkey=${rkey_alt', 30, 37), 1716: ("s python:skey=='meta_type' and 'zmi-sort_key' or No", 31, 37), 2066: ('string:Sort ${rkey_alt_up} by name', 39, 39), 2139: (' string:${my_url}?skey=id&rkey=${rkey_alt', 40, 37), 2220: ("s python:skey=='id' and 'zmi-sort_key' or No", 41, 37), 2879: ('string:Sort ${rkey_alt_up} by size', 52, 39), 2952: (' string:${my_url}?skey=get_size&rkey=${rkey_alt', 53, 37), 3039: ("s python:skey=='get_size' and 'zmi-sort_key' or No", 54, 37), 3451: ('string:Sort ${rkey_alt_up} by modification date', 63, 39), 3537: (' string:${my_url}?skey=_p_mtime&rkey=${rkey_alt', 64, 37), 3624: ("s python:skey=='_p_mtime' and 'zmi-sort_key' or No", 65, 37), 3906: ('obs', 74, 34), 3944: ('nocall:ob_dict/obj', 75, 32), 4178: ('ob_dict/id', 77, 104), 4519: (' ob/meta_type | defaul', 81, 122), 4491: ('ob/zmi_icon | default', 81, 94), 4598: ('ob/meta_type | default', 82, 53), 4765: ("python:'%s/manage_workspace'%(ob_dict['quoted_id'])", 86, 40), 4856: ('ob_dict/id', 87, 37), 4989: ('ob/wl_isLocked | nothing', 88, 111), 5163: ('ob/title|nothing', 91, 74), 5228: ('ob/title', 92, 46), 5390: ('python:here.compute_size(ob)', 96, 76), 5522: ('python:here.last_modified(ob)', 98, 81), 5737: ("python:sm.checkPermission('Delete objects', context)", 106, 23), 5806: ('obs', 106, 92), 5883: ('not:context/dontAllowCopyAndPaste|nothing', 108, 37), 6160: ('delete_allowed', 110, 121), 6415: ('here/cb_dataValid', 112, 125), 6587: ('delete_allowed', 114, 122), 6741: ("python:sm.checkPermission('Import/Export objects', context)", 115, 135), 6856: ("python: has_order_support and sm.checkPermission('Manage properties', context)", 117, 50), 7050: ('python:range(1,min(5,len(obs)))', 119, 38), 7096: ('val', 119, 84), 7142: ('python:range(5,len(obs),5)', 120, 38), 7183: ('val', 120, 79), 8444: ('not:obs', 146, 26), 8558: ('here/title_or_id', 148, 57), 8662: ('not:context/dontAllowCopyAndPaste|nothing', 151, 35), 8824: ('here/cb_dataValid', 152, 118), 9000: ("python:sm.checkPermission('Import/Export objects', context)", 154, 128), 12921: ('here/manage_page_footer', 281, 31)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140097364736848 = {'class': 'zmi-typename_show', }
_static_140097364735408 = {'class': 'btn btn-primary', 'type': 'submit', 'name': 'manage_importExportForm:method', 'value': 'Import/Export', }
_static_140097364733824 = {'class': 'btn btn-primary', 'type': 'submit', 'name': 'manage_pasteObjects:method', 'value': 'Paste', }
_static_140097364730032 = {'class': 'form-group', }
_static_140097364727344 = {'class': 'alert alert-info mt-4 mb-4', }
_static_140097364726000 = {'class': 'fas fa-arrow-down', 'style': 'border-bottom: 0.2rem solid silver;', }
_static_140097364724512 = {'type': 'submit', 'name': 'manage_move_objects_to_bottom:method', 'value': 'Move to bottom', 'title': 'Move selected items to bottom', 'class': 'btn btn-primary', }
_static_140097364721520 = {'class': 'fas fa-arrow-up', 'style': 'border-top: 0.2rem solid silver;', }
_static_140097364720800 = {'type': 'submit', 'name': 'manage_move_objects_to_top:method', 'value': 'Move to top', 'title': 'Move selected items to top', 'class': 'btn btn-primary ml-2 mr-2', }
_static_140097364718448 = {'class': 'fas fa-arrow-down', }
_static_140097364717440 = {'type': 'submit', 'name': 'manage_move_objects_down:method', 'value': 'Move down', 'title': 'Move selected items down', 'class': 'btn btn-primary rounded-right', }
_static_140097364714992 = {'class': 'fas fa-arrow-up', }
_static_140097364713984 = {'type': 'submit', 'name': 'manage_move_objects_up:method', 'value': 'Move up', 'title': 'Move selected items up', 'class': 'btn btn-primary', }
_static_140097364711248 = {'class': 'input-group-append', }
_static_140097364706880 = {'class': 'form-control btn btn-primary', 'name': 'delta:int', }
_static_140097364704848 = {'class': 'input-group', }
_static_140097364704224 = {'class': 'btn btn-primary mr-2', 'type': 'submit', 'name': 'manage_importExportForm:method', 'value': 'Import/Export', }
_static_140097493029536 = {'class': 'btn btn-primary mr-2', 'type': 'submit', 'name': 'manage_delObjects:method', 'value': 'Delete', }
_static_140097364700672 = {'class': 'btn btn-primary mr-2', 'type': 'submit', 'name': 'manage_pasteObjects:method', 'value': 'Paste', }
_static_140097364698896 = {'class': 'btn btn-primary mr-2', 'type': 'submit', 'name': 'manage_copyObjects:method', 'value': 'Copy', }
_static_140097364696928 = {'class': 'btn btn-primary mr-2', 'type': 'submit', 'name': 'manage_cutObjects:method', 'value': 'Cut', }
_static_140097364695152 = {'class': 'btn btn-primary mr-2', 'type': 'submit', 'name': 'manage_renameForm:method', 'value': 'Rename', }
_static_140097493036592 = {'class': 'input-group', }
_static_140097375209504 = {'class': 'form-group form-inline zmi-controls', }
_static_140097375218624 = {'class': 'text-right zmi-object-date hidden-xs pl-3', }
_static_140097373967584 = {'class': 'text-right zmi-object-size hidden-xs', }
_static_140097371554912 = {'class': 'zmi-object-title hidden-xs', }
_static_140097371567632 = {'class': 'fa fa-lock', }
_static_140097372275856 = {'class': 'badge badge-warning', 'title': 'This item has been locked by WebDAV', }
_static_140097368278832 = {'href': "python:'%s/manage_workspace'%(ob_dict['quoted_id'])", }
_static_140097369976800 = {'class': 'zmi-object-id', }
_static_140097368197968 = {'class': 'sr-only', }
_static_140097367352624 = {'title': 'Broken object', 'class': 'fas fa-ban text-danger', }
_static_140097365068000 = {'class': 'zmi-object-type', 'onclick': "$(this).prev().children('input').trigger('click')", }
_static_140097364276032 = {'type': 'checkbox', 'class': 'checkbox-list-item', 'name': 'ids:list', 'onclick': 'event.stopPropagation();select_objectitem($(this));', 'value': 'ob_dict/id', }
_static_140097364693040 = {'class': 'zmi-object-check text-right', 'onclick': "$(this).children('input').trigger('click');", }
_static_140097364672368 = {'class': 'fa fa-sort', }
_static_140097364670256 = {'title': 'Sort Ascending by Modification Date', 'href': '?skey=_p_mtime&rkey=asc', 'class': "python:skey=='_p_mtime' and 'zmi-sort_key' or None", }
_static_140097364668624 = {'scope': 'col', 'class': 'zmi-object-date text-right hidden-xs', }
_static_140097364667328 = {'class': 'fa fa-sort', }
_static_140097364665216 = {'title': 'Sort Ascending by File-Size', 'href': '?skey=get_size&rkey=asc', 'class': "python:skey=='get_size' and 'zmi-sort_key' or None", }
_static_140097364663584 = {'scope': 'col', 'class': 'zmi-object-size text-right hidden-xs', }
_static_140097364662816 = {'id': 'tablefilter', 'name': 'obj_ids:tokens', 'type': 'text', 'title': 'Filter object list by entering a name. Pressing the Enter key starts recursive search.', }
_static_140097364660464 = {'class': 'fa fa-search tablefilter', 'onclick': "$('#tablefilter').focus()", }
_static_140097364659168 = {'class': 'fa fa-sort', }
_static_140097365669680 = {'title': 'Sort Ascending by Name', 'href': '?skey=id&rkey=asc', 'class': "python:skey=='id' and 'zmi-sort_key' or None", }
_static_140097364623312 = {'scope': 'col', 'class': 'zmi-object-id', }
_static_140097364622064 = {'class': 'fa fa-sort', }
_static_140097364620048 = {'title': 'Sort Ascending by Meta-Type', 'href': '?skey=meta_type&rkey=asc', 'class': "python:skey=='meta_type' and 'zmi-sort_key' or None", }
_static_140097364618560 = {'scope': 'col', 'class': 'zmi-object-type', }
_static_140097364617072 = {'type': 'checkbox', 'id': 'checkAll', 'onclick': 'checkbox_all();', }
_static_140097364615440 = {'scope': 'col', 'class': 'zmi-object-check text-right', }
_static_140097364612512 = {'class': 'thead-light', }
_static_140097364610928 = {'class': 'table table-striped table-hover table-sm objectItems', }
_static_140097402077088 = {'id': 'objectItems', 'name': 'objectItems', 'method': 'post', 'action': 'string:${request/URL1}/', }
_static_140097402074496 = {'class': 'container-fluid', }
_static_140097413192176 = __C2ZContextWrapper
_static_140097413192464 = __compile_zt_expr
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

            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097402065856
            __attrs_140097402065856 = _static_140097412968080

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097402066048
            __default_140097402066048 = _DEFAULT_MARKER

            # <Value 'here/manage_page_header' (1:31)> -> __cache_140097402066384
            __token = 31
            try:
                __zt_tmp = __attrs_140097402065856
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140097402066384 = _static_140097413192464('path', 'here/manage_page_header', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

            # <BinOp left=<Value 'here/manage_page_header' (1:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6af7e255a0> -> __condition
            __expression = __cache_140097402066384

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140097402066384
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097402073968
            __attrs_140097402073968 = _static_140097412968080

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097402073776
            __default_140097402073776 = _DEFAULT_MARKER

            # <Value 'here/manage_tabs' (3:29)> -> __cache_140097402065472
            __token = 89
            try:
                __zt_tmp = __attrs_140097402073968
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140097402065472 = _static_140097413192464('path', 'here/manage_tabs', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

            # <BinOp left=<Value 'here/manage_tabs' (3:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6af7e27190> -> __condition
            __expression = __cache_140097402065472

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140097402065472
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x7f6af7e27580> name=None at 7f6af7e275b0> -> __attrs_140097402074928
            __attrs_140097402074928 = _static_140097402074496

            # <main ... (0:0)
            # --------------------------------------------------------
            __append('<main class="container-fluid">\n  ')

            # <Static value=<ast.Dict object at 0x7f6af7e27fa0> name=None at 7f6af7e27fd0> -> __attrs_140097402075504
            __attrs_140097402075504 = _static_140097402077088
            __backup_has_order_support_140097393610656 = get('has_order_support', __marker)

            # <Value "python:getattr(here.aq_explicit, 'has_order_support', 0)" (7:38)> -> __value
            __token = 238
            try:
                __zt_tmp = __attrs_140097402075504
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('python', "getattr(here.aq_explicit, 'has_order_support', 0)", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['has_order_support'] = __value
            __backup_sm_140097393615024 = get('sm', __marker)

            # <Value 'modules/AccessControl/getSecurityManager' (8:22)> -> __value
            __token = 318
            try:
                __zt_tmp = __attrs_140097402075504
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('path', 'modules/AccessControl/getSecurityManager', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['sm'] = __value
            __backup_default_sort_140097393615408 = get('default_sort', __marker)

            # <Value "python: 'position' if has_order_support else 'id'" (9:31)> -> __value
            __token = 392
            try:
                __zt_tmp = __attrs_140097402075504
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('python', " 'position' if has_order_support else 'id'", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['default_sort'] = __value
            __backup_skey_140097393615792 = get('skey', __marker)

            # <Value "python:request.get('skey',default_sort)" (10:22)> -> __value
            __token = 467
            try:
                __zt_tmp = __attrs_140097402075504
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('python', "request.get('skey',default_sort)", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['skey'] = __value
            __backup_rkey_140097393365904 = get('rkey', __marker)

            # <Value "python:request.get('rkey','asc')" (11:21)> -> __value
            __token = 532
            try:
                __zt_tmp = __attrs_140097402075504
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('python', "request.get('rkey','asc')", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['rkey'] = __value
            __backup_rkey_alt_140097393617568 = get('rkey_alt', __marker)

            # <Value "python:'desc' if rkey=='asc' else 'asc'" (12:24)> -> __value
            __token = 594
            try:
                __zt_tmp = __attrs_140097402075504
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('python', "'desc' if rkey=='asc' else 'asc'", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['rkey_alt'] = __value
            __backup_rkey_alt_up_140097393618000 = get('rkey_alt_up', __marker)

            # <Value 'rkey_alt/upper' (13:26)> -> __value
            __token = 666
            try:
                __zt_tmp = __attrs_140097402075504
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('path', 'rkey_alt/upper', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['rkey_alt_up'] = __value
            __backup_obs_140097393618480 = get('obs', __marker)

            # <Value 'python: here.manage_get_sortedObjects(sortkey = skey, revkey = rkey)' (14:17)> -> __value
            __token = 705
            try:
                __zt_tmp = __attrs_140097402075504
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('python', ' here.manage_get_sortedObjects(sortkey = skey, revkey = rkey)', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['obs'] = __value
            __backup_my_url_140097393618432 = get('my_url', __marker)

            # <Value 'string:${context/absolute_url}/manage_main' (15:19)> -> __value
            __token = 801
            try:
                __zt_tmp = __attrs_140097402075504
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('string', '${context/absolute_url}/manage_main', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['my_url'] = __value

            # <form ... (0:0)
            # --------------------------------------------------------
            __append('<form id="objectItems" name="objectItems" method="post"')

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097402076224
            __default_140097402076224 = _DEFAULT_MARKER

            # <Substitution 'string:${request/URL1}/' (17:31)> -> __attr_action
            __token = 905
            try:
                __zt_tmp = __attrs_140097402075504
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_action = _static_140097413192464('string', '${request/URL1}/', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_action = __quote(__attr_action, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_action is not None):
                __append((' action="%s"' % __attr_action))
            __append('>\n\n    ')

            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097364609824
            __attrs_140097364609824 = _static_140097412968080

            # <Value 'obs' (19:30)> -> __condition
            __token = 962
            try:
                __zt_tmp = __attrs_140097364609824
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140097413192464('path', 'obs', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            if __condition:
                __append('\n      ')

                # <Static value=<ast.Dict object at 0x7f6af5a6cf70> name=None at 7f6af5a6cfa0> -> __attrs_140097364611360
                __attrs_140097364611360 = _static_140097364610928

                # <Value 'obs' (20:89)> -> __condition
                __token = 1057
                try:
                    __zt_tmp = __attrs_140097364611360
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140097413192464('path', 'obs', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                if __condition:

                    # <table ... (0:0)
                    # --------------------------------------------------------
                    __append('<table class="table table-striped table-hover table-sm objectItems">\n        ')

                    # <Static value=<ast.Dict object at 0x7f6af5a6d5a0> name=None at 7f6af5a6d5d0> -> __attrs_140097364613088
                    __attrs_140097364613088 = _static_140097364612512

                    # <thead ... (0:0)
                    # --------------------------------------------------------
                    __append('<thead')

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097364612128
                    __default_140097364612128 = _DEFAULT_MARKER

                    # <Substitution "python:'thead-light sorted_%s'%(request.get('rkey',''))" (21:57)> -> __attr_class
                    __token = 1120
                    try:
                        __zt_tmp = __attrs_140097364613088
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_140097413192464('python', "'thead-light sorted_%s'%(request.get('rkey',''))", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', 'thead-light', _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((' class="%s"' % __attr_class))
                    __append('>\n          ')

                    # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097364614048
                    __attrs_140097364614048 = _static_140097412968080

                    # <tr ... (0:0)
                    # --------------------------------------------------------
                    __append('<tr>\n            ')

                    # <Static value=<ast.Dict object at 0x7f6af5a6e110> name=None at 7f6af5a6e140> -> __attrs_140097364615632
                    __attrs_140097364615632 = _static_140097364615440

                    # <th ... (0:0)
                    # --------------------------------------------------------
                    __append('<th scope="col" class="zmi-object-check text-right">\n              ')

                    # <Static value=<ast.Dict object at 0x7f6af5a6e770> name=None at 7f6af5a6e7a0> -> __attrs_140097364617360
                    __attrs_140097364617360 = _static_140097364617072

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input type="checkbox" id="checkAll" onclick="checkbox_all();" />\n            </th>\n            ')

                    # <Static value=<ast.Dict object at 0x7f6af5a6ed40> name=None at 7f6af5a6e9b0> -> __attrs_140097364618656
                    __attrs_140097364618656 = _static_140097364618560

                    # <th ... (0:0)
                    # --------------------------------------------------------
                    __append('<th scope="col" class="zmi-object-type">\n              ')

                    # <Static value=<ast.Dict object at 0x7f6af5a6f310> name=None at 7f6af5a6f340> -> __attrs_140097364621104
                    __attrs_140097364621104 = _static_140097364620048

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097364619520
                    __default_140097364619520 = _DEFAULT_MARKER

                    # <Substitution 'string:Sort ${rkey_alt_up} by meta-type' (29:39)> -> __attr_title
                    __token = 1550
                    try:
                        __zt_tmp = __attrs_140097364621104
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_title = _static_140097413192464('string', 'Sort ${rkey_alt_up} by meta-type', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    __attr_title = __quote(__attr_title, '"', '&quot;', 'Sort Ascending by Meta-Type', _DEFAULT_MARKER)
                    if (__attr_title is not None):
                        __append((' title="%s"' % __attr_title))

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097364620288
                    __default_140097364620288 = _DEFAULT_MARKER

                    # <Substitution 'string:${my_url}?skey=meta_type&rkey=${rkey_alt}' (30:37)> -> __attr_href
                    __token = 1628
                    try:
                        __zt_tmp = __attrs_140097364621104
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140097413192464('string', '${my_url}?skey=meta_type&rkey=${rkey_alt}', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '?skey=meta_type&rkey=asc', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097364620576
                    __default_140097364620576 = _DEFAULT_MARKER

                    # <Substitution "python:skey=='meta_type' and 'zmi-sort_key' or None" (31:37)> -> __attr_class
                    __token = 1716
                    try:
                        __zt_tmp = __attrs_140097364621104
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_140097413192464('python', "skey=='meta_type' and 'zmi-sort_key' or None", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((' class="%s"' % __attr_class))
                    __append('>\n                ')

                    # <Static value=<ast.Dict object at 0x7f6af5a6faf0> name=None at 7f6af5a6fb20> -> __attrs_140097364622448
                    __attrs_140097364622448 = _static_140097364622064

                    # <i ... (0:0)
                    # --------------------------------------------------------
                    __append('<i class="fa fa-sort"></i>\n              </a>\n            </th>\n            ')

                    # <Static value=<ast.Dict object at 0x7f6af5a6ffd0> name=None at 7f6af5a6f880> -> __attrs_140097420823952
                    __attrs_140097420823952 = _static_140097364623312

                    # <th ... (0:0)
                    # --------------------------------------------------------
                    __append('<th scope="col" class="zmi-object-id">\n              ')

                    # <Static value=<ast.Dict object at 0x7f6af5b6f730> name=None at 7f6af5edd3c0> -> __attrs_140097364658160
                    __attrs_140097364658160 = _static_140097365669680

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097364656624
                    __default_140097364656624 = _DEFAULT_MARKER

                    # <Substitution 'string:Sort ${rkey_alt_up} by name' (39:39)> -> __attr_title
                    __token = 2066
                    try:
                        __zt_tmp = __attrs_140097364658160
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_title = _static_140097413192464('string', 'Sort ${rkey_alt_up} by name', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    __attr_title = __quote(__attr_title, '"', '&quot;', 'Sort Ascending by Name', _DEFAULT_MARKER)
                    if (__attr_title is not None):
                        __append((' title="%s"' % __attr_title))

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097364657296
                    __default_140097364657296 = _DEFAULT_MARKER

                    # <Substitution 'string:${my_url}?skey=id&rkey=${rkey_alt}' (40:37)> -> __attr_href
                    __token = 2139
                    try:
                        __zt_tmp = __attrs_140097364658160
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140097413192464('string', '${my_url}?skey=id&rkey=${rkey_alt}', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '?skey=id&rkey=asc', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097364657632
                    __default_140097364657632 = _DEFAULT_MARKER

                    # <Substitution "python:skey=='id' and 'zmi-sort_key' or None" (41:37)> -> __attr_class
                    __token = 2220
                    try:
                        __zt_tmp = __attrs_140097364658160
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_140097413192464('python', "skey=='id' and 'zmi-sort_key' or None", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((' class="%s"' % __attr_class))
                    __append('>\n                Name\n                ')

                    # <Static value=<ast.Dict object at 0x7f6af5a78be0> name=None at 7f6af5a78c10> -> __attrs_140097364659552
                    __attrs_140097364659552 = _static_140097364659168

                    # <i ... (0:0)
                    # --------------------------------------------------------
                    __append('<i class="fa fa-sort"></i>\n              </a>\n              ')

                    # <Static value=<ast.Dict object at 0x7f6af5a790f0> name=None at 7f6af5a79120> -> __attrs_140097364660704
                    __attrs_140097364660704 = _static_140097364660464

                    # <i ... (0:0)
                    # --------------------------------------------------------
                    __append('<i class="fa fa-search tablefilter" onclick="$(\'#tablefilter\').focus()"></i>\n              ')

                    # <Static value=<ast.Dict object at 0x7f6af5a79a20> name=None at 7f6af5a79a50> -> __attrs_140097364661616
                    __attrs_140097364661616 = _static_140097364662816

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input id="tablefilter" name="obj_ids:tokens" type="text" title="Filter object list by entering a name. Pressing the Enter key starts recursive search." />\n            </th>\n            ')

                    # <Static value=<ast.Dict object at 0x7f6af5a79d20> name=None at 7f6af5a79d50> -> __attrs_140097364663776
                    __attrs_140097364663776 = _static_140097364663584

                    # <th ... (0:0)
                    # --------------------------------------------------------
                    __append('<th scope="col" class="zmi-object-size text-right hidden-xs">\n              ')

                    # <Static value=<ast.Dict object at 0x7f6af5a7a380> name=None at 7f6af5a7a3b0> -> __attrs_140097364666320
                    __attrs_140097364666320 = _static_140097364665216

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097364664688
                    __default_140097364664688 = _DEFAULT_MARKER

                    # <Substitution 'string:Sort ${rkey_alt_up} by size' (52:39)> -> __attr_title
                    __token = 2879
                    try:
                        __zt_tmp = __attrs_140097364666320
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_title = _static_140097413192464('string', 'Sort ${rkey_alt_up} by size', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    __attr_title = __quote(__attr_title, '"', '&quot;', 'Sort Ascending by File-Size', _DEFAULT_MARKER)
                    if (__attr_title is not None):
                        __append((' title="%s"' % __attr_title))

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097364665504
                    __default_140097364665504 = _DEFAULT_MARKER

                    # <Substitution 'string:${my_url}?skey=get_size&rkey=${rkey_alt}' (53:37)> -> __attr_href
                    __token = 2952
                    try:
                        __zt_tmp = __attrs_140097364666320
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140097413192464('string', '${my_url}?skey=get_size&rkey=${rkey_alt}', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '?skey=get_size&rkey=asc', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097364665792
                    __default_140097364665792 = _DEFAULT_MARKER

                    # <Substitution "python:skey=='get_size' and 'zmi-sort_key' or None" (54:37)> -> __attr_class
                    __token = 3039
                    try:
                        __zt_tmp = __attrs_140097364666320
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_140097413192464('python', "skey=='get_size' and 'zmi-sort_key' or None", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((' class="%s"' % __attr_class))
                    __append('>\n                Size\n                ')

                    # <Static value=<ast.Dict object at 0x7f6af5a7abc0> name=None at 7f6af5a7abf0> -> __attrs_140097364667712
                    __attrs_140097364667712 = _static_140097364667328

                    # <i ... (0:0)
                    # --------------------------------------------------------
                    __append('<i class="fa fa-sort"></i>\n              </a>\n            </th>\n            ')

                    # <Static value=<ast.Dict object at 0x7f6af5a7b0d0> name=None at 7f6af5a7b100> -> __attrs_140097364668816
                    __attrs_140097364668816 = _static_140097364668624

                    # <th ... (0:0)
                    # --------------------------------------------------------
                    __append('<th scope="col" class="zmi-object-date text-right hidden-xs">\n              ')

                    # <Static value=<ast.Dict object at 0x7f6af5a7b730> name=None at 7f6af5a7b760> -> __attrs_140097364671360
                    __attrs_140097364671360 = _static_140097364670256

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097364669728
                    __default_140097364669728 = _DEFAULT_MARKER

                    # <Substitution 'string:Sort ${rkey_alt_up} by modification date' (63:39)> -> __attr_title
                    __token = 3451
                    try:
                        __zt_tmp = __attrs_140097364671360
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_title = _static_140097413192464('string', 'Sort ${rkey_alt_up} by modification date', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    __attr_title = __quote(__attr_title, '"', '&quot;', 'Sort Ascending by Modification Date', _DEFAULT_MARKER)
                    if (__attr_title is not None):
                        __append((' title="%s"' % __attr_title))

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097364670544
                    __default_140097364670544 = _DEFAULT_MARKER

                    # <Substitution 'string:${my_url}?skey=_p_mtime&rkey=${rkey_alt}' (64:37)> -> __attr_href
                    __token = 3537
                    try:
                        __zt_tmp = __attrs_140097364671360
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140097413192464('string', '${my_url}?skey=_p_mtime&rkey=${rkey_alt}', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '?skey=_p_mtime&rkey=asc', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097364670832
                    __default_140097364670832 = _DEFAULT_MARKER

                    # <Substitution "python:skey=='_p_mtime' and 'zmi-sort_key' or None" (65:37)> -> __attr_class
                    __token = 3624
                    try:
                        __zt_tmp = __attrs_140097364671360
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_140097413192464('python', "skey=='_p_mtime' and 'zmi-sort_key' or None", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((' class="%s"' % __attr_class))
                    __append('>\n                Last Modified\n                ')

                    # <Static value=<ast.Dict object at 0x7f6af5a7bf70> name=None at 7f6af5a7bfa0> -> __attrs_140097364689200
                    __attrs_140097364689200 = _static_140097364672368

                    # <i ... (0:0)
                    # --------------------------------------------------------
                    __append('<i class="fa fa-sort"></i>\n              </a>\n            </th>\n          </tr>\n        </thead>\n        ')

                    # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097364689488
                    __attrs_140097364689488 = _static_140097412968080

                    # <tbody ... (0:0)
                    # --------------------------------------------------------
                    __append('<tbody>\n          ')

                    # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097364690448
                    __attrs_140097364690448 = _static_140097412968080
                    __backup_ob_dict_140097399366912 = get('ob_dict', __marker)

                    # <Value 'obs' (74:34)> -> __iterator
                    __token = 3906
                    try:
                        __zt_tmp = __attrs_140097364690448
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_140097413192464('path', 'obs', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    (__iterator, ____index_140097364690688, ) = getname('repeat')('ob_dict', __iterator)
                    econtext['ob_dict'] = None
                    for __item in __iterator:
                        econtext['ob_dict'] = __item

                        # <tr ... (0:0)
                        # --------------------------------------------------------
                        __append('<tr>\n            ')

                        # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097364691504
                        __attrs_140097364691504 = _static_140097412968080
                        __backup_ob_140097401212784 = get('ob', __marker)

                        # <Value 'nocall:ob_dict/obj' (75:32)> -> __value
                        __token = 3944
                        try:
                            __zt_tmp = __attrs_140097364691504
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140097413192464('nocall', 'ob_dict/obj', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        econtext['ob'] = __value
                        __append('\n              ')

                        # <Static value=<ast.Dict object at 0x7f6af5a81030> name=None at 7f6af5a81060> -> __attrs_140097364693280
                        __attrs_140097364693280 = _static_140097364693040

                        # <td ... (0:0)
                        # --------------------------------------------------------
                        __append('<td class="zmi-object-check text-right" onclick="$(this).children(\'input\').trigger(\'click\');">\n                ')

                        # <Static value=<ast.Dict object at 0x7f6af5a1b340> name=None at 7f6af5a1acb0> -> __attrs_140097365472496
                        __attrs_140097365472496 = _static_140097364276032

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input type="checkbox" class="checkbox-list-item" name="ids:list"                   onclick="event.stopPropagation();select_objectitem($(this));"')

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097365460256
                        __default_140097365460256 = _DEFAULT_MARKER

                        # <Substitution 'ob_dict/id' (77:104)> -> __attr_value
                        __token = 4178
                        try:
                            __zt_tmp = __attrs_140097365472496
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_value = _static_140097413192464('path', 'ob_dict/id', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_value is not None):
                            __append((' value="%s"' % __attr_value))
                        __append(' />\n              </td>\n              ')

                        # <Static value=<ast.Dict object at 0x7f6af5adc8e0> name=None at 7f6af5adc730> -> __attrs_140097366839632
                        __attrs_140097366839632 = _static_140097365068000

                        # <td ... (0:0)
                        # --------------------------------------------------------
                        __append('<td class="zmi-object-type" onclick="$(this).prev().children(\'input\').trigger(\'click\')">\n                ')

                        # <Static value=<ast.Dict object at 0x7f6af5d0a530> name=None at 7f6af5d0a890> -> __attrs_140097367147280
                        __attrs_140097367147280 = _static_140097367352624

                        # <i ... (0:0)
                        # --------------------------------------------------------
                        __append('<i')

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097367446992
                        __default_140097367446992 = _DEFAULT_MARKER

                        # <Substitution 'ob/meta_type | default' (81:122)> -> __attr_title
                        __token = 4519
                        try:
                            __zt_tmp = __attrs_140097367147280
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_title = _static_140097413192464('path', 'ob/meta_type | default', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_title = __quote(__attr_title, '"', '&quot;', 'Broken object', _DEFAULT_MARKER)
                        if (__attr_title is not None):
                            __append((' title="%s"' % __attr_title))

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097367455536
                        __default_140097367455536 = _DEFAULT_MARKER

                        # <Substitution 'ob/zmi_icon | default' (81:94)> -> __attr_class
                        __token = 4491
                        try:
                            __zt_tmp = __attrs_140097367147280
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_class = _static_140097413192464('path', 'ob/zmi_icon | default', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_class = __quote(__attr_class, '"', '&quot;', 'fas fa-ban text-danger', _DEFAULT_MARKER)
                        if (__attr_class is not None):
                            __append((' class="%s"' % __attr_class))
                        __append('>\n                  ')

                        # <Static value=<ast.Dict object at 0x7f6af5dd8b50> name=None at 7f6af5dd8d00> -> __attrs_140097368207856
                        __attrs_140097368207856 = _static_140097368197968

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="sr-only">')

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097368195808
                        __default_140097368195808 = _DEFAULT_MARKER

                        # <Value 'ob/meta_type | default' (82:53)> -> __cache_140097368368336
                        __token = 4598
                        try:
                            __zt_tmp = __attrs_140097368207856
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140097368368336 = _static_140097413192464('path', 'ob/meta_type | default', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                        # <BinOp left=<Value 'ob/meta_type | default' (82:53)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6af5e012a0> -> __condition
                        __expression = __cache_140097368368336

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('Broken object')
                        else:
                            __content = __cache_140097368368336
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</span>\n                </i>\n              </td>\n              ')

                        # <Static value=<ast.Dict object at 0x7f6af5f8afe0> name=None at 7f6af5ddb0a0> -> __attrs_140097369979872
                        __attrs_140097369979872 = _static_140097369976800

                        # <td ... (0:0)
                        # --------------------------------------------------------
                        __append('<td class="zmi-object-id">\n                ')

                        # <Static value=<ast.Dict object at 0x7f6af5dec730> name=None at 7f6af5deec50> -> __attrs_140097369752624
                        __attrs_140097369752624 = _static_140097368278832

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append('<a')

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097369760784
                        __default_140097369760784 = _DEFAULT_MARKER

                        # <Substitution "python:'%s/manage_workspace'%(ob_dict['quoted_id'])" (86:40)> -> __attr_href
                        __token = 4765
                        try:
                            __zt_tmp = __attrs_140097369752624
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_140097413192464('python', "'%s/manage_workspace'%(ob_dict['quoted_id'])", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((' href="%s"' % __attr_href))
                        __append('>\n                  ')

                        # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097370493504
                        __attrs_140097370493504 = _static_140097412968080

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097370494128
                        __default_140097370494128 = _DEFAULT_MARKER

                        # <Value 'ob_dict/id' (87:37)> -> __cache_140097369263696
                        __token = 4856
                        try:
                            __zt_tmp = __attrs_140097370493504
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140097369263696 = _static_140097413192464('path', 'ob_dict/id', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                        # <BinOp left=<Value 'ob_dict/id' (87:37)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6af604f5e0> -> __condition
                        __expression = __cache_140097369263696

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span>Id</span>')
                        else:
                            __content = __cache_140097369263696
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('\n                  ')

                        # <Static value=<ast.Dict object at 0x7f6af61bc490> name=None at 7f6af61bc0a0> -> __attrs_140097371890080
                        __attrs_140097371890080 = _static_140097372275856

                        # <Value 'ob/wl_isLocked | nothing' (88:111)> -> __condition
                        __token = 4989
                        try:
                            __zt_tmp = __attrs_140097371890080
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140097413192464('path', 'ob/wl_isLocked | nothing', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span class="badge badge-warning" title="This item has been locked by WebDAV">\n                    ')

                            # <Static value=<ast.Dict object at 0x7f6af610f610> name=None at 7f6af610f5e0> -> __attrs_140097371565232
                            __attrs_140097371565232 = _static_140097371567632

                            # <i ... (0:0)
                            # --------------------------------------------------------
                            __append('<i class="fa fa-lock"></i>\n                  </span>')
                        __append('\n                  ')

                        # <Static value=<ast.Dict object at 0x7f6af610c460> name=None at 7f6af610e740> -> __attrs_140097371296752
                        __attrs_140097371296752 = _static_140097371554912

                        # <Value 'ob/title|nothing' (91:74)> -> __condition
                        __token = 5163
                        try:
                            __zt_tmp = __attrs_140097371296752
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140097413192464('path', 'ob/title|nothing', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span class="zmi-object-title hidden-xs">\n                    &nbsp;(')

                            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097374228096
                            __attrs_140097374228096 = _static_140097412968080

                            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097374228672
                            __default_140097374228672 = _DEFAULT_MARKER

                            # <Value 'ob/title' (92:46)> -> __cache_140097372459296
                            __token = 5228
                            try:
                                __zt_tmp = __attrs_140097374228096
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140097372459296 = _static_140097413192464('path', 'ob/title', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                            # <BinOp left=<Value 'ob/title' (92:46)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6af6398fd0> -> __condition
                            __expression = __cache_140097372459296

                            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:

                                # <span ... (0:0)
                                # --------------------------------------------------------
                                __append('<span></span>')
                            else:
                                __content = __cache_140097372459296
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append(__content)
                            __append(')\n                  </span>')
                        __append('\n                </a>\n              </td>\n              ')

                        # <Static value=<ast.Dict object at 0x7f6af63594e0> name=None at 7f6af6358fd0> -> __attrs_140097373571536
                        __attrs_140097373571536 = _static_140097373967584

                        # <td ... (0:0)
                        # --------------------------------------------------------
                        __append('<td class="text-right zmi-object-size hidden-xs">')

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097373974688
                        __default_140097373974688 = _DEFAULT_MARKER

                        # <Value 'python:here.compute_size(ob)' (96:76)> -> __cache_140097373148192
                        __token = 5390
                        try:
                            __zt_tmp = __attrs_140097373571536
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140097373148192 = _static_140097413192464('python', 'here.compute_size(ob)', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                        # <BinOp left=<Value 'python:here.compute_size(ob)' (96:76)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6af6398ac0> -> __condition
                        __expression = __cache_140097373148192

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('\n              ')
                        else:
                            __content = __cache_140097373148192
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</td>\n              ')

                        # <Static value=<ast.Dict object at 0x7f6af648abc0> name=None at 7f6af648aa40> -> __attrs_140097375212144
                        __attrs_140097375212144 = _static_140097375218624

                        # <td ... (0:0)
                        # --------------------------------------------------------
                        __append('<td class="text-right zmi-object-date hidden-xs pl-3">')

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097375425328
                        __default_140097375425328 = _DEFAULT_MARKER

                        # <Value 'python:here.last_modified(ob)' (98:81)> -> __cache_140097373572304
                        __token = 5522
                        try:
                            __zt_tmp = __attrs_140097375212144
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140097373572304 = _static_140097413192464('python', 'here.last_modified(ob)', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                        # <BinOp left=<Value 'python:here.last_modified(ob)' (98:81)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6af62f8be0> -> __condition
                        __expression = __cache_140097373572304

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('\n              ')
                        else:
                            __content = __cache_140097373572304
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</td>\n            ')
                        if (__backup_ob_140097401212784 is __marker):
                            del econtext['ob']
                        else:
                            econtext['ob'] = __backup_ob_140097401212784
                        __append('\n          </tr>')
                        ____index_140097364690688 -= 1
                        if (____index_140097364690688 > 0):
                            __append('\n          ')
                    if (__backup_ob_dict_140097399366912 is __marker):
                        del econtext['ob_dict']
                    else:
                        econtext['ob_dict'] = __backup_ob_dict_140097399366912
                    __append('\n        </tbody>\n      </table>')
                __append('\n\n      ')

                # <Static value=<ast.Dict object at 0x7f6af6488820> name=None at 7f6af6488fa0> -> __attrs_140097393622560
                __attrs_140097393622560 = _static_140097375209504
                __backup_delete_allowed_140097393619584 = get('delete_allowed', __marker)

                # <Value "python:sm.checkPermission('Delete objects', context)" (106:23)> -> __value
                __token = 5737
                try:
                    __zt_tmp = __attrs_140097393622560
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140097413192464('python', "sm.checkPermission('Delete objects', context)", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                econtext['delete_allowed'] = __value

                # <Value 'obs' (106:92)> -> __condition
                __token = 5806
                try:
                    __zt_tmp = __attrs_140097393622560
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140097413192464('path', 'obs', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="form-group form-inline zmi-controls">\n        ')

                    # <Static value=<ast.Dict object at 0x7f6afd4e6e30> name=None at 7f6afd4e6d70> -> __attrs_140097493036016
                    __attrs_140097493036016 = _static_140097493036592

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="input-group">\n          ')

                    # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097494954000
                    __attrs_140097494954000 = _static_140097412968080

                    # <Value 'not:context/dontAllowCopyAndPaste|nothing' (108:37)> -> __condition
                    __token = 5883
                    try:
                        __zt_tmp = __attrs_140097494954000
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140097413192464('not', 'context/dontAllowCopyAndPaste|nothing', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    if __condition:
                        __append('\n            ')

                        # <Static value=<ast.Dict object at 0x7f6af5a81870> name=None at 7f6af5a818a0> -> __attrs_140097364693952
                        __attrs_140097364693952 = _static_140097364695152

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input class="btn btn-primary mr-2" type="submit" name="manage_renameForm:method" value="Rename" />\n            ')

                        # <Static value=<ast.Dict object at 0x7f6af5a81f60> name=None at 7f6af5a81f90> -> __attrs_140097364695728
                        __attrs_140097364695728 = _static_140097364696928

                        # <Value 'delete_allowed' (110:121)> -> __condition
                        __token = 6160
                        try:
                            __zt_tmp = __attrs_140097364695728
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140097413192464('path', 'delete_allowed', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        if __condition:

                            # <input ... (0:0)
                            # --------------------------------------------------------
                            __append('<input class="btn btn-primary mr-2" type="submit" name="manage_cutObjects:method" value="Cut" />')
                        __append('\n            ')

                        # <Static value=<ast.Dict object at 0x7f6af5a82710> name=None at 7f6af5a82740> -> __attrs_140097364697696
                        __attrs_140097364697696 = _static_140097364698896

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input class="btn btn-primary mr-2" type="submit" name="manage_copyObjects:method" value="Copy" />\n            ')

                        # <Static value=<ast.Dict object at 0x7f6af5a82e00> name=None at 7f6af5a82e30> -> __attrs_140097364699472
                        __attrs_140097364699472 = _static_140097364700672

                        # <Value 'here/cb_dataValid' (112:125)> -> __condition
                        __token = 6415
                        try:
                            __zt_tmp = __attrs_140097364699472
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140097413192464('path', 'here/cb_dataValid', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        if __condition:

                            # <input ... (0:0)
                            # --------------------------------------------------------
                            __append('<input class="btn btn-primary mr-2" type="submit" name="manage_pasteObjects:method" value="Paste" />')
                        __append('\n          ')
                    __append('\n          ')

                    # <Static value=<ast.Dict object at 0x7f6afd4e52a0> name=None at 7f6afd4e4f10> -> __attrs_140097364701152
                    __attrs_140097364701152 = _static_140097493029536

                    # <Value 'delete_allowed' (114:122)> -> __condition
                    __token = 6587
                    try:
                        __zt_tmp = __attrs_140097364701152
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140097413192464('path', 'delete_allowed', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    if __condition:

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input class="btn btn-primary mr-2" type="submit" name="manage_delObjects:method" value="Delete" />')
                    __append('\n          ')

                    # <Static value=<ast.Dict object at 0x7f6af5a83be0> name=None at 7f6af5a83c10> -> __attrs_140097364703024
                    __attrs_140097364703024 = _static_140097364704224

                    # <Value "python:sm.checkPermission('Import/Export objects', context)" (115:135)> -> __condition
                    __token = 6741
                    try:
                        __zt_tmp = __attrs_140097364703024
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140097413192464('python', "sm.checkPermission('Import/Export objects', context)", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    if __condition:

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input class="btn btn-primary mr-2" type="submit" name="manage_importExportForm:method" value="Import/Export" />')
                    __append('\n\n          ')

                    # <Static value=<ast.Dict object at 0x7f6af5a83e50> name=None at 7f6af5a83e80> -> __attrs_140097364705232
                    __attrs_140097364705232 = _static_140097364704848

                    # <Value "python: has_order_support and sm.checkPermission('Manage properties', context)" (117:50)> -> __condition
                    __token = 6856
                    try:
                        __zt_tmp = __attrs_140097364705232
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140097413192464('python', " has_order_support and sm.checkPermission('Manage properties', context)", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    if __condition:

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append('<div class="input-group">\n            ')

                        # <Static value=<ast.Dict object at 0x7f6af5a84640> name=None at 7f6af5a84670> -> __attrs_140097364707072
                        __attrs_140097364707072 = _static_140097364706880

                        # <select ... (0:0)
                        # --------------------------------------------------------
                        __append('<select class="form-control btn btn-primary" name="delta:int">\n              ')

                        # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097364708752
                        __attrs_140097364708752 = _static_140097412968080
                        __backup_val_140097365473504 = get('val', __marker)

                        # <Value 'python:range(1,min(5,len(obs)))' (119:38)> -> __iterator
                        __token = 7050
                        try:
                            __zt_tmp = __attrs_140097364708752
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __iterator = _static_140097413192464('python', 'range(1,min(5,len(obs)))', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        (__iterator, ____index_140097364708896, ) = getname('repeat')('val', __iterator)
                        econtext['val'] = None
                        for __item in __iterator:
                            econtext['val'] = __item

                            # <option ... (0:0)
                            # --------------------------------------------------------
                            __append('<option>')

                            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097364708176
                            __default_140097364708176 = _DEFAULT_MARKER

                            # <Value 'val' (119:84)> -> __cache_140097364707696
                            __token = 7096
                            try:
                                __zt_tmp = __attrs_140097364708752
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140097364707696 = _static_140097413192464('path', 'val', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                            # <BinOp left=<Value 'val' (119:84)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6af5a84a30> -> __condition
                            __expression = __cache_140097364707696

                            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                pass
                            else:
                                __content = __cache_140097364707696
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append(__content)
                            __append('</option>')
                            ____index_140097364708896 -= 1
                            if (____index_140097364708896 > 0):
                                __append('\n              ')
                        if (__backup_val_140097365473504 is __marker):
                            del econtext['val']
                        else:
                            econtext['val'] = __backup_val_140097365473504
                        __append('\n              ')

                        # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097364710384
                        __attrs_140097364710384 = _static_140097412968080
                        __backup_val_140097368371264 = get('val', __marker)

                        # <Value 'python:range(5,len(obs),5)' (120:38)> -> __iterator
                        __token = 7142
                        try:
                            __zt_tmp = __attrs_140097364710384
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __iterator = _static_140097413192464('python', 'range(5,len(obs),5)', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        (__iterator, ____index_140097364710672, ) = getname('repeat')('val', __iterator)
                        econtext['val'] = None
                        for __item in __iterator:
                            econtext['val'] = __item

                            # <option ... (0:0)
                            # --------------------------------------------------------
                            __append('<option>')

                            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097364709808
                            __default_140097364709808 = _DEFAULT_MARKER

                            # <Value 'val' (120:79)> -> __cache_140097364709328
                            __token = 7183
                            try:
                                __zt_tmp = __attrs_140097364710384
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140097364709328 = _static_140097413192464('path', 'val', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                            # <BinOp left=<Value 'val' (120:79)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6af5a85090> -> __condition
                            __expression = __cache_140097364709328

                            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                pass
                            else:
                                __content = __cache_140097364709328
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append(__content)
                            __append('</option>')
                            ____index_140097364710672 -= 1
                            if (____index_140097364710672 > 0):
                                __append('\n              ')
                        if (__backup_val_140097368371264 is __marker):
                            del econtext['val']
                        else:
                            econtext['val'] = __backup_val_140097368371264
                        __append('\n            </select>\n            ')

                        # <Static value=<ast.Dict object at 0x7f6af5a85750> name=None at 7f6af5a85780> -> __attrs_140097364711680
                        __attrs_140097364711680 = _static_140097364711248

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append('<div class="input-group-append">\n              ')

                        # <Static value=<ast.Dict object at 0x7f6af5a86200> name=None at 7f6af5a86230> -> __attrs_140097364712256
                        __attrs_140097364712256 = _static_140097364713984

                        # <button ... (0:0)
                        # --------------------------------------------------------
                        __append('<button type="submit" name="manage_move_objects_up:method" value="Move up"                 title="Move selected items up" class="btn btn-primary">\n                ')

                        # <Static value=<ast.Dict object at 0x7f6af5a865f0> name=None at 7f6af5a86620> -> __attrs_140097364715424
                        __attrs_140097364715424 = _static_140097364714992

                        # <i ... (0:0)
                        # --------------------------------------------------------
                        __append('<i class="fas fa-arrow-up"></i>\n              </button>\n              ')

                        # <Static value=<ast.Dict object at 0x7f6af5a86f80> name=None at 7f6af5a86fb0> -> __attrs_140097364715712
                        __attrs_140097364715712 = _static_140097364717440

                        # <button ... (0:0)
                        # --------------------------------------------------------
                        __append('<button type="submit" name="manage_move_objects_down:method" value="Move down"                 title="Move selected items down" class="btn btn-primary rounded-right">\n                ')

                        # <Static value=<ast.Dict object at 0x7f6af5a87370> name=None at 7f6af5a873a0> -> __attrs_140097364718880
                        __attrs_140097364718880 = _static_140097364718448

                        # <i ... (0:0)
                        # --------------------------------------------------------
                        __append('<i class="fas fa-arrow-down"></i>\n              </button>\n            </div>\n            ')

                        # <Static value=<ast.Dict object at 0x7f6af5a87ca0> name=None at 7f6af5a87cd0> -> __attrs_140097364718976
                        __attrs_140097364718976 = _static_140097364720800

                        # <button ... (0:0)
                        # --------------------------------------------------------
                        __append('<button type="submit" name="manage_move_objects_to_top:method" value="Move to top"               title="Move selected items to top" class="btn btn-primary ml-2 mr-2">\n              ')

                        # <Static value=<ast.Dict object at 0x7f6af5a87f70> name=None at 7f6af5a87fd0> -> __attrs_140097364722544
                        __attrs_140097364722544 = _static_140097364721520

                        # <i ... (0:0)
                        # --------------------------------------------------------
                        __append('<i class="fas fa-arrow-up" style="border-top: 0.2rem solid silver;"></i>\n            </button>\n            ')

                        # <Static value=<ast.Dict object at 0x7f6af5a88b20> name=None at 7f6af5a88b50> -> __attrs_140097364724656
                        __attrs_140097364724656 = _static_140097364724512

                        # <button ... (0:0)
                        # --------------------------------------------------------
                        __append('<button type="submit" name="manage_move_objects_to_bottom:method" value="Move to bottom"                title="Move selected items to bottom" class="btn btn-primary">\n              ')

                        # <Static value=<ast.Dict object at 0x7f6af5a890f0> name=None at 7f6af5a89120> -> __attrs_140097364726240
                        __attrs_140097364726240 = _static_140097364726000

                        # <i ... (0:0)
                        # --------------------------------------------------------
                        __append('<i class="fas fa-arrow-down" style="border-bottom: 0.2rem solid silver;"></i>\n            </button>\n          </div>')
                    __append('\n        </div>\n\n      </div>')
                if (__backup_delete_allowed_140097393619584 is __marker):
                    del econtext['delete_allowed']
                else:
                    econtext['delete_allowed'] = __backup_delete_allowed_140097393619584
                __append('\n    ')
            __append('\n\n    ')

            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097493035872
            __attrs_140097493035872 = _static_140097412968080

            # <Value 'not:obs' (146:26)> -> __condition
            __token = 8444
            try:
                __zt_tmp = __attrs_140097493035872
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140097413192464('not', 'obs', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            if __condition:
                __append('\n      ')

                # <Static value=<ast.Dict object at 0x7f6af5a89630> name=None at 7f6af5a89480> -> __attrs_140097364727680
                __attrs_140097364727680 = _static_140097364727344

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="alert alert-info mt-4 mb-4">\n        There are currently no items in ')

                # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097364729360
                __attrs_140097364729360 = _static_140097412968080

                # <em ... (0:0)
                # --------------------------------------------------------
                __append('<em>')

                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097364728784
                __default_140097364728784 = _DEFAULT_MARKER

                # <Value 'here/title_or_id' (148:57)> -> __cache_140097364728304
                __token = 8558
                try:
                    __zt_tmp = __attrs_140097364729360
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140097364728304 = _static_140097413192464('path', 'here/title_or_id', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                # <BinOp left=<Value 'here/title_or_id' (148:57)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6af5a89ab0> -> __condition
                __expression = __cache_140097364728304

                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140097364728304
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</em>.\n      </div>\n      ')

                # <Static value=<ast.Dict object at 0x7f6af5a8a0b0> name=None at 7f6af5a8a0e0> -> __attrs_140097364730416
                __attrs_140097364730416 = _static_140097364730032

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="form-group">\n        ')

                # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097364731328
                __attrs_140097364731328 = _static_140097412968080

                # <Value 'not:context/dontAllowCopyAndPaste|nothing' (151:35)> -> __condition
                __token = 8662
                try:
                    __zt_tmp = __attrs_140097364731328
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140097413192464('not', 'context/dontAllowCopyAndPaste|nothing', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                if __condition:
                    __append('\n          ')

                    # <Static value=<ast.Dict object at 0x7f6af5a8af80> name=None at 7f6af5a8afb0> -> __attrs_140097364732624
                    __attrs_140097364732624 = _static_140097364733824

                    # <Value 'here/cb_dataValid' (152:118)> -> __condition
                    __token = 8824
                    try:
                        __zt_tmp = __attrs_140097364732624
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140097413192464('path', 'here/cb_dataValid', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    if __condition:

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input class="btn btn-primary" type="submit" name="manage_pasteObjects:method" value="Paste" />')
                    __append('\n        ')
                __append('\n        ')

                # <Static value=<ast.Dict object at 0x7f6af5a8b5b0> name=None at 7f6af5a8b5e0> -> __attrs_140097364734208
                __attrs_140097364734208 = _static_140097364735408

                # <Value "python:sm.checkPermission('Import/Export objects', context)" (154:128)> -> __condition
                __token = 9000
                try:
                    __zt_tmp = __attrs_140097364734208
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140097413192464('python', "sm.checkPermission('Import/Export objects', context)", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                if __condition:

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input class="btn btn-primary" type="submit" name="manage_importExportForm:method" value="Import/Export" />')
                __append('\n      </div>\n    ')
            __append('\n  </form>')
            if (__backup_my_url_140097393618432 is __marker):
                del econtext['my_url']
            else:
                econtext['my_url'] = __backup_my_url_140097393618432
            if (__backup_obs_140097393618480 is __marker):
                del econtext['obs']
            else:
                econtext['obs'] = __backup_obs_140097393618480
            if (__backup_rkey_alt_up_140097393618000 is __marker):
                del econtext['rkey_alt_up']
            else:
                econtext['rkey_alt_up'] = __backup_rkey_alt_up_140097393618000
            if (__backup_rkey_alt_140097393617568 is __marker):
                del econtext['rkey_alt']
            else:
                econtext['rkey_alt'] = __backup_rkey_alt_140097393617568
            if (__backup_rkey_140097393365904 is __marker):
                del econtext['rkey']
            else:
                econtext['rkey'] = __backup_rkey_140097393365904
            if (__backup_skey_140097393615792 is __marker):
                del econtext['skey']
            else:
                econtext['skey'] = __backup_skey_140097393615792
            if (__backup_default_sort_140097393615408 is __marker):
                del econtext['default_sort']
            else:
                econtext['default_sort'] = __backup_default_sort_140097393615408
            if (__backup_sm_140097393615024 is __marker):
                del econtext['sm']
            else:
                econtext['sm'] = __backup_sm_140097393615024
            if (__backup_has_order_support_140097393610656 is __marker):
                del econtext['has_order_support']
            else:
                econtext['has_order_support'] = __backup_has_order_support_140097393610656
            __append('\n\n</main>\n\n\n')

            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097364730512
            __attrs_140097364730512 = _static_140097412968080

            # <script ... (0:0)
            # --------------------------------------------------------
            __append('<script>\n  // +++++++++++++++++++++++++++\n  // Item  Selection\n  // +++++++++++++++++++++++++++\n  function checkbox_all() {\n    var checkboxes = document.getElementsByClassName(\'checkbox-list-item\');\n    // Toggle Highlighting CSS-Class\n    if (document.getElementById(\'checkAll\').checked) {\n      $(\'table.objectItems tbody tr\').addClass(\'checked\');\n    } else {\n      $(\'table.objectItems tbody tr\').removeClass(\'checked\');\n    };\n    // Set Checkbox like checkAll-Box\n    for (i = 0; i < checkboxes.length; i++) {\n      checkboxes[i].checked = document.getElementById(\'checkAll\').checked;\n    }\n  };\n\n  function zmicontrols_visible() {\n    var zmicontrols = $(\'form#objectItems .zmi-controls\');\n    var zmicontrols_top = zmicontrols.offset().top;\n    var zmicontrols_bottom = zmicontrols_top + zmicontrols.outerHeight();\n    var viewport_top = $(window).scrollTop();\n    var viewport_bottom = viewport_top + $(window).height();\n    return zmicontrols_bottom > viewport_top && zmicontrols_top < viewport_bottom;\n  };\n\n  function select_objectitem(ob) {\n    ob.parent().parent().toggleClass(\'checked\');\n    if ( !zmicontrols_visible() ) {\n      $(\'form#objectItems\').addClass(\'selected\');\n    }\n    // Anything selected?\n    var checkboxes = document.getElementsByClassName(\'checkbox-list-item\');\n    var selected = false;\n    for (i = 0; i < checkboxes.length; i++) {\n      if ( checkboxes[i].checked ) {\n        selected = true;\n        break;\n      }\n    }\n    if ( !selected ) {\n      $(\'form#objectItems\').removeClass(\'selected\');\n      console.log(\'form#objectItems removed .selected\');\n    }\n  };\n\n\n  $(function () {\n\n    // +++++++++++++++++++++++++++\n    // Icon Tooltips\n    // +++++++++++++++++++++++++++\n    $(\'td.zmi-object-type i\').tooltip({\n      \'placement\': \'top\'\n    });\n\n    // +++++++++++++++++++++++++++\n    // Tablefilter/Search Element\n    // +++++++++++++++++++++++++++\n\n    function isModifierKeyPressed(event) {\n      return event.altKey ||\n        event.ctrlKey ||\n        event.metaKey;\n    }\n\n    $(document).keypress(function (event) {\n\n      if (isModifierKeyPressed(event)) {\n        return; // ignore\n      }\n\n      // Set Focus to Tablefilter only when Modal Dialog is not Shown\n      if (!$(\'#zmi-modal\').hasClass(\'show\')) {\n        $(\'#tablefilter\').focus();\n        // Prevent Submitting a form by hitting Enter\n        // https://stackoverflow.com/questions/895171/prevent-users-from-submitting-a-form-by-hitting-enter\n        if (event.which == 13) {\n          event.preventDefault();\n          return false;\n        };\n      };\n    })\n\n    $(\'#tablefilter\').keyup(function (event) {\n\n      if (isModifierKeyPressed(event)) {\n        return; // ignore\n      }\n\n      var tablefilter = $(this).val();\n      if (event.which == 13) {\n        if (1 === $(\'tbody tr:visible\').length) {\n          window.location.href = $(\'tbody tr:visible a\').attr(\'href\');\n        } else {\n          window.location.href = \'manage_findForm?btn_submit=Find&search_sub:int=1&obj_ids%3Atokens=\' + tablefilter;\n        }\n        event.preventDefault();\n      };\n      $(\'table.objectItems\').find("tbody tr").hide();\n      $(\'table.objectItems\').find("tbody tr td.zmi-object-id a:contains(" + tablefilter + ")").closest(\'tbody tr\').show();\n    });\n\n    // +++++++++++++++++++++++++++\n    // OBJECTIST SORTING: Show skey=meta_type\n    // +++++++++++++++++++++++++++\n    let searchParams = new URLSearchParams(window.location.search);\n    if (searchParams.get(\'skey\') == \'meta_type\') {\n      $(\'td.zmi-object-type i\').each(function () {\n        $(this).parent().parent().find(\'td.zmi-object-id\').prepend(\'')

            # <Static value=<ast.Dict object at 0x7f6af5a8bb50> name=None at 7f6af5a8bb80> -> __attrs_140097364737280
            __attrs_140097364737280 = _static_140097364736848

            # <span ... (0:0)
            # --------------------------------------------------------
            __append('<span class="zmi-typename_show">\' + $(this).text() + \'</span>\')\n      });\n      $(\'th.zmi-object-id\').addClass(\'zmi-typename_show\');\n    }\n\n  });\n\n</script>\n\n')

            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097364755024
            __attrs_140097364755024 = _static_140097412968080

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097364754832
            __default_140097364754832 = _DEFAULT_MARKER

            # <Value 'here/manage_page_footer' (281:31)> -> __cache_140097364737904
            __token = 12921
            try:
                __zt_tmp = __attrs_140097364755024
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140097364737904 = _static_140097413192464('path', 'here/manage_page_footer', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

            # <BinOp left=<Value 'here/manage_page_footer' (281:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6af5a90070> -> __condition
            __expression = __cache_140097364737904

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140097364737904
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }