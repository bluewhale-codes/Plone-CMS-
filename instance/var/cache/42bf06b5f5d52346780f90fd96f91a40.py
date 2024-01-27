# -*- coding: utf-8 -*-
__filename = 'manage_catalogIndexes'

__tokens = {31: ('here/manage_page_header', 1, 31), 89: ('here/manage_tabs', 3, 29), 578: ('context/Indexes', 14, 33), 641: ('context/availableIndexes', 15, 45), 709: ('context/absolute_url', 16, 41), 1117: ('python:len(filtered_meta_types) > 1', 22, 54), 1354: ("string:location.href='${request/URL1}/'+this.options[this.selectedIndex].value", 25, 61), 1609: ('filtered_meta_types', 27, 65), 1701: ('indextype/action', 28, 70), 1776: ('indextype/name', 29, 57), 2262: ('string:${request/URL1}/', 40, 37), 2378: ("python:request.get('skey','id')", 42, 25), 2435: (" python:request.get('rkey','asc'", 43, 24), 2497: ("t python:'desc' if rkey=='asc' else 'as", 44, 27), 2561: ('bs python: indexes.manage_get_sortedObjects(sortkey=skey, revkey=rk', 45, 21), 2677: ('obs', 46, 42), 2845: ("python:'thead-light sorted_%s'%(request.get('rkey',''))", 48, 73), 3486: ("python:'Sort %s by Name'%( rkey_alt.upper() )", 57, 50), 3581: (" python:'?skey=id&rkey=%s'%( rkey_alt ", 58, 48), 3670: ("s python:request.get('skey',None)=='id' and 'zmi-sort_key' or No", 59, 48), 4276: ("python:'Sort %s by index type'%( rkey_alt.upper() )", 68, 50), 4377: (" python:'?skey=meta_type&rkey=%s'%( rkey_alt ", 69, 48), 4473: ("s python:request.get('skey',None)=='meta_type' and 'zmi-sort_key' or No", 70, 48), 5101: ("python:'Sort %s by indexed values'%( rkey_alt.upper() )", 79, 50), 5206: (" python:'?skey=indexSize&rkey=%s'%( rkey_alt ", 80, 48), 5302: ("s python:request.get('skey',None)=='indexSize' and 'zmi-sort_key' or No", 81, 48), 5734: ('obs', 89, 52), 5792: ('nocall:ob_dict/obj', 90, 52), 6072: ('ob_dict/id', 92, 128), 6337: ('string:Indexes/${ob_dict/quoted_id}/manage_workspace', 96, 64), 6404: ('ob_dict/id', 96, 131), 6492: ('ob/getIndexSourceNames', 97, 71), 6571: ("python: len(sourcenames) != 1 or sourcenames[0] != ob_dict['id']", 98, 55), 6811: ("python: ', '.join(sourcenames)", 100, 84), 6691: ('string:(${ob_dict/title|nothing})', 99, 54), 7015: ('ob/meta_type', 103, 71), 7176: ('ob/indexSize|string:n/a', 105, 57), 7902: ('not: obs', 120, 40), 8775: ('here/manage_page_footer', 150, 31)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tal import ErrorInfo as _ErrorInfo
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140007911663040 = {'class': 'alert alert-info', }
_static_140007911662080 = {'class': 'btn btn-primary', 'type': 'submit', 'name': 'manage_clearIndex:method', 'value': 'Clear index', }
_static_140007911660304 = {'class': 'btn btn-primary', 'type': 'submit', 'name': 'manage_reindexIndex:method', 'value': 'Reindex', }
_static_140007911658528 = {'class': 'btn btn-primary', 'type': 'submit', 'name': 'manage_delIndex:method', 'value': 'Remove index', }
_static_140007911624512 = {'class': 'zmi-controls', }
_static_140007911655120 = {'class': 'text-left zmi-object-size hidden-xs', }
_static_140007911636848 = {'class': 'text-left', }
_static_140007911631472 = {'href': 'string:Indexes/${ob_dict/quoted_id}/manage_workspace', }
_static_140007911628928 = {'type': 'checkbox', 'class': 'checkbox-list-item', 'name': 'ids:list', 'onclick': 'event.stopPropagation();select_objectitem($(this));', 'value': 'ob_dict/id', }
_static_140007911626336 = {'class': 'zmi-object-check text-right', 'onclick': "$(this).children('input').trigger('click');", }
_static_140007911621872 = {'class': 'fa fa-sort', }
_static_140007911555424 = {'title': 'Sort Ascending by indexed values', 'href': '?skey=indexSize&rkey=asc', 'class': "python:request.get('skey',None)=='indexSize' and 'zmi-sort_key' or None", }
_static_140007911556624 = {'scope': 'col', 'class': 'zmi-object-size hidden-xs text-nowrap', }
_static_140007911558448 = {'class': 'fa fa-sort', }
_static_140007911560608 = {'title': 'Sort Ascending by index type', 'href': '?skey=meta_type&rkey=asc', 'class': "python:request.get('skey',None)=='meta_type' and 'zmi-sort_key' or None", }
_static_140007911562480 = {'scope': 'col', 'class': 'zmi-object-indextype text-nowrap', }
_static_140007911564160 = {'class': 'fa fa-sort', }
_static_140007911565936 = {'title': 'Sort Ascending by Name', 'href': '?skey=id&rkey=asc', 'class': "python:request.get('skey',None)=='id' and 'zmi-sort_key' or None", }
_static_140007911568336 = {'scope': 'col', 'class': 'zmi-object-id', }
_static_140007911550608 = {'type': 'checkbox', 'id': 'checkAll', 'onclick': 'checkbox_all();', }
_static_140007911539424 = {'scope': 'col', 'class': 'zmi-object-check text-right text-nowrap', }
_static_140007911542448 = {'class': 'thead-light', }
_static_140007911543936 = {'class': 'table table-striped table-hover table-sm objectItems', }
_static_140007912076240 = {'name': 'objectItems', 'method': 'post', 'action': 'string:${request/URL1}/', }
_static_140007911550032 = {'class': 'btn btn-primary', 'type': 'submit', 'name': 'submit', 'value': 'Add', }
_static_140007912064672 = {'class': 'input-group-append', }
_static_140007911551856 = {'value': 'indextype/action', }
_static_140007912071440 = {'value': 'manage_workspace', 'disabled': '', }
_static_140007912066736 = {'id': 'addindex', 'class': 'form-control', 'name': ':action', 'onChange': '', }
_static_140007912065776 = {'class': 'd-sm-block d-none', }
_static_140007912068512 = {'class': 'input-group-text', }
_static_140007912074944 = {'class': 'input-group-prepend', }
_static_140007912069472 = {'class': 'input-group', }
_static_140007911282800 = {'class': 'form-group mt-4 mb-4', }
_static_140007911289904 = {'method': 'get', 'action': 'context/absolute_url', }
_static_140007911278576 = {'class': 'form-help', }
_static_140007911289040 = {'class': 'container-fluid', }
_static_140007999377936 = __C2ZContextWrapper
_static_140007999378224 = __compile_zt_expr
_static_140008001267376 = {}

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

            # <Static value=<ast.Dict object at 0x7f56272e66b0> name=None at 7f56272e69e0> -> __attrs_140007911277904
            __attrs_140007911277904 = _static_140008001267376

            # <Symbol value=<DEFAULT> at 7f562726ee00> -> __default_140007911283808
            __default_140007911283808 = _DEFAULT_MARKER

            # <Value 'here/manage_page_header' (1:31)> -> __cache_140007911284240
            __token = 31
            try:
                __zt_tmp = __attrs_140007911277904
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140007911284240 = _static_140007999378224('path', 'here/manage_page_header', econtext=econtext)(_static_140007999377936(econtext, __zt_tmp))

            # <BinOp left=<Value 'here/manage_page_header' (1:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f562726ee00> at 7f5621d16530> -> __condition
            __expression = __cache_140007911284240

            # <Symbol value=<DEFAULT> at 7f562726ee00> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140007911284240
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x7f56272e66b0> name=None at 7f56272e69e0> -> __attrs_140007911282416
            __attrs_140007911282416 = _static_140008001267376

            # <Symbol value=<DEFAULT> at 7f562726ee00> -> __default_140007911288944
            __default_140007911288944 = _DEFAULT_MARKER

            # <Value 'here/manage_tabs' (3:29)> -> __cache_140007911286208
            __token = 89
            try:
                __zt_tmp = __attrs_140007911282416
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140007911286208 = _static_140007999378224('path', 'here/manage_tabs', econtext=econtext)(_static_140007999377936(econtext, __zt_tmp))

            # <BinOp left=<Value 'here/manage_tabs' (3:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f562726ee00> at 7f5621d168f0> -> __condition
            __expression = __cache_140007911286208

            # <Symbol value=<DEFAULT> at 7f562726ee00> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140007911286208
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x7f5621d170d0> name=None at 7f5621d14f70> -> __attrs_140007911276896
            __attrs_140007911276896 = _static_140007911289040

            # <main ... (0:0)
            # --------------------------------------------------------
            __append('<main class="container-fluid">\n\n    ')

            # <Static value=<ast.Dict object at 0x7f5621d147f0> name=None at 7f5621d14be0> -> __attrs_140007911277616
            __attrs_140007911277616 = _static_140007911278576

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p class="form-help">\n        This list defines what indexes the Catalog will contain. When objects\n        get cataloged, the values of any attributes which match\n        an index in this list will get indexed. If you add indexes to a Catalog\n        which contains indexed objects, you MUST at the least re-index your newly\n        added index. You may want to update the whole Catalog.\n    </p>\n    ')

            # <Static value=<ast.Dict object at 0x7f56272e66b0> name=None at 7f56272e69e0> -> __attrs_140007911279920
            __attrs_140007911279920 = _static_140008001267376
            __backup_indexes_140007911839952 = get('indexes', __marker)

            # <Value 'context/Indexes' (14:33)> -> __value
            __token = 578
            try:
                __zt_tmp = __attrs_140007911279920
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140007999378224('path', 'context/Indexes', econtext=econtext)(_static_140007999377936(econtext, __zt_tmp))
            econtext['indexes'] = __value
            __append('\n        ')

            # <Static value=<ast.Dict object at 0x7f56272e66b0> name=None at 7f56272e69e0> -> __attrs_140007911282752
            __attrs_140007911282752 = _static_140008001267376
            __backup_filtered_meta_types_140007911840528 = get('filtered_meta_types', __marker)

            # <Value 'context/availableIndexes' (15:45)> -> __value
            __token = 641
            try:
                __zt_tmp = __attrs_140007911282752
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140007999378224('path', 'context/availableIndexes', econtext=econtext)(_static_140007999377936(econtext, __zt_tmp))
            econtext['filtered_meta_types'] = __value
            __append('\n            ')

            # <Static value=<ast.Dict object at 0x7f5621d17430> name=None at 7f5621d17730> -> __attrs_140007911290912
            __attrs_140007911290912 = _static_140007911289904

            # <form ... (0:0)
            # --------------------------------------------------------
            __append('<form method="get"')

            # <Symbol value=<DEFAULT> at 7f562726ee00> -> __default_140007911290384
            __default_140007911290384 = _DEFAULT_MARKER

            # <Substitution 'context/absolute_url' (16:41)> -> __attr_action
            __token = 709
            try:
                __zt_tmp = __attrs_140007911290912
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_action = _static_140007999378224('path', 'context/absolute_url', econtext=econtext)(_static_140007999377936(econtext, __zt_tmp))
            __attr_action = __quote(__attr_action, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_action is not None):
                __append((' action="%s"' % __attr_action))
            __append('>\n                ')

            # <Static value=<ast.Dict object at 0x7f5621d15870> name=None at 7f5621d143a0> -> __attrs_140007912072256
            __attrs_140007912072256 = _static_140007911282800

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="form-group mt-4 mb-4">\n                    ')

            # <Static value=<ast.Dict object at 0x7f5621dd5960> name=None at 7f5621dd6200> -> __attrs_140007912069088
            __attrs_140007912069088 = _static_140007912069472

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="input-group">\n                        ')

            # <Static value=<ast.Dict object at 0x7f5621dd6ec0> name=None at 7f5621dd7100> -> __attrs_140007912074416
            __attrs_140007912074416 = _static_140007912074944

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="input-group-prepend">\n                            ')

            # <Static value=<ast.Dict object at 0x7f5621dd55a0> name=None at 7f5621dd60b0> -> __attrs_140007912075856
            __attrs_140007912075856 = _static_140007912068512

            # <span ... (0:0)
            # --------------------------------------------------------
            __append('<span class="input-group-text">Add ')

            # <Static value=<ast.Dict object at 0x7f5621dd4af0> name=None at 7f5621dd5b70> -> __attrs_140007912078544
            __attrs_140007912078544 = _static_140007912065776

            # <span ... (0:0)
            # --------------------------------------------------------
            __append('<span class="d-sm-block d-none">&nbsp;new&nbsp;</span> Index:</span>\n                        </div>\n                            ')

            # <Static value=<ast.Dict object at 0x7f56272e66b0> name=None at 7f56272e69e0> -> __attrs_140007912063040
            __attrs_140007912063040 = _static_140008001267376

            # <Value 'python:len(filtered_meta_types) > 1' (22:54)> -> __condition
            __token = 1117
            try:
                __zt_tmp = __attrs_140007912063040
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140007999378224('python', 'len(filtered_meta_types) > 1', econtext=econtext)(_static_140007999377936(econtext, __zt_tmp))
            if __condition:
                __append('\n                                ')

                # <Static value=<ast.Dict object at 0x7f5621dd4eb0> name=None at 7f5621dd5240> -> __attrs_140007912065728
                __attrs_140007912065728 = _static_140007912066736

                # <select ... (0:0)
                # --------------------------------------------------------
                __append('<select id="addindex" class="form-control" name=":action"')

                # <Symbol value=<DEFAULT> at 7f562726ee00> -> __default_140007912066304
                __default_140007912066304 = _DEFAULT_MARKER

                # <Substitution "string:location.href='${request/URL1}/'+this.options[this.selectedIndex].value" (25:61)> -> __attr_onChange
                __token = 1354
                try:
                    __zt_tmp = __attrs_140007912065728
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_onChange = _static_140007999378224('string', "location.href='${request/URL1}/'+this.options[this.selectedIndex].value", econtext=econtext)(_static_140007999377936(econtext, __zt_tmp))
                __attr_onChange = __quote(__attr_onChange, '"', '&quot;', '', _DEFAULT_MARKER)
                if (__attr_onChange is not None):
                    __append((' onChange="%s"' % __attr_onChange))
                __append('>\n                                    ')

                # <Static value=<ast.Dict object at 0x7f5621dd6110> name=None at 7f5621dd52a0> -> __attrs_140007911553056
                __attrs_140007911553056 = _static_140007912071440

                # <option ... (0:0)
                # --------------------------------------------------------
                __append('<option value="manage_workspace" disabled>Select type to add...</option>\n                                    ')

                # <Static value=<ast.Dict object at 0x7f56272e66b0> name=None at 7f56272e69e0> -> __attrs_140007911549792
                __attrs_140007911549792 = _static_140008001267376
                __backup_indextype_140007911846240 = get('indextype', __marker)

                # <Value 'filtered_meta_types' (27:65)> -> __iterator
                __token = 1609
                try:
                    __zt_tmp = __attrs_140007911549792
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140007999378224('path', 'filtered_meta_types', econtext=econtext)(_static_140007999377936(econtext, __zt_tmp))
                (__iterator, ____index_140007911553440, ) = getname('repeat')('indextype', __iterator)
                econtext['indextype'] = None
                for __item in __iterator:
                    econtext['indextype'] = __item
                    __append('\n                                        ')

                    # <Static value=<ast.Dict object at 0x7f5621d57370> name=None at 7f5621d56ec0> -> __attrs_140007911555024
                    __attrs_140007911555024 = _static_140007911551856

                    # <option ... (0:0)
                    # --------------------------------------------------------
                    __append('<option')

                    # <Symbol value=<DEFAULT> at 7f562726ee00> -> __default_140007911549264
                    __default_140007911549264 = _DEFAULT_MARKER

                    # <Substitution 'indextype/action' (28:70)> -> __attr_value
                    __token = 1701
                    try:
                        __zt_tmp = __attrs_140007911555024
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_140007999378224('path', 'indextype/action', econtext=econtext)(_static_140007999377936(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append('>')

                    # <Symbol value=<DEFAULT> at 7f562726ee00> -> __default_140007911548160
                    __default_140007911548160 = _DEFAULT_MARKER

                    # <Value 'indextype/name' (29:57)> -> __cache_140007911554304
                    __token = 1776
                    try:
                        __zt_tmp = __attrs_140007911555024
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140007911554304 = _static_140007999378224('path', 'indextype/name', econtext=econtext)(_static_140007999377936(econtext, __zt_tmp))

                    # <BinOp left=<Value 'indextype/name' (29:57)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f562726ee00> at 7f5621d57430> -> __condition
                    __expression = __cache_140007911554304

                    # <Symbol value=<DEFAULT> at 7f562726ee00> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140007911554304
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</option>\n                                    ')
                    ____index_140007911553440 -= 1
                    if (____index_140007911553440 > 0):
                        __append('')
                if (__backup_indextype_140007911846240 is __marker):
                    del econtext['indextype']
                else:
                    econtext['indextype'] = __backup_indextype_140007911846240
                __append('\n                                </select>\n                            ')
            __append('\n                            ')

            # <Static value=<ast.Dict object at 0x7f5621dd46a0> name=None at 7f5621dd46d0> -> __attrs_140007911551568
            __attrs_140007911551568 = _static_140007912064672

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="input-group-append">\n                                ')

            # <Static value=<ast.Dict object at 0x7f5621d56c50> name=None at 7f5621d564a0> -> __attrs_140007911548880
            __attrs_140007911548880 = _static_140007911550032

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input class="btn btn-primary" type="submit" name="submit" value="Add" />\n                        </div>\n                    </div>\n                </div>\n            </form>\n        ')
            if (__backup_filtered_meta_types_140007911840528 is __marker):
                del econtext['filtered_meta_types']
            else:
                econtext['filtered_meta_types'] = __backup_filtered_meta_types_140007911840528
            __append('\n        ')

            # <Static value=<ast.Dict object at 0x7f5621dd73d0> name=None at 7f5621dd7490> -> __attrs_140007911547632
            __attrs_140007911547632 = _static_140007912076240

            # <form ... (0:0)
            # --------------------------------------------------------
            __append('<form name="objectItems" method="post"')

            # <Symbol value=<DEFAULT> at 7f562726ee00> -> __default_140007911549504
            __default_140007911549504 = _DEFAULT_MARKER

            # <Substitution 'string:${request/URL1}/' (40:37)> -> __attr_action
            __token = 2262
            try:
                __zt_tmp = __attrs_140007911547632
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_action = _static_140007999378224('string', '${request/URL1}/', econtext=econtext)(_static_140007999377936(econtext, __zt_tmp))
            __attr_action = __quote(__attr_action, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_action is not None):
                __append((' action="%s"' % __attr_action))
            __append('>\n            ')

            # <Static value=<ast.Dict object at 0x7f56272e66b0> name=None at 7f56272e69e0> -> __attrs_140007911546528
            __attrs_140007911546528 = _static_140008001267376
            __backup_skey_140007911842064 = get('skey', __marker)

            # <Value "python:request.get('skey','id')" (42:25)> -> __value
            __token = 2378
            try:
                __zt_tmp = __attrs_140007911546528
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140007999378224('python', "request.get('skey','id')", econtext=econtext)(_static_140007999377936(econtext, __zt_tmp))
            econtext['skey'] = __value
            __backup_rkey_140007911842592 = get('rkey', __marker)

            # <Value "python:request.get('rkey','asc')" (43:24)> -> __value
            __token = 2435
            try:
                __zt_tmp = __attrs_140007911546528
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140007999378224('python', "request.get('rkey','asc')", econtext=econtext)(_static_140007999377936(econtext, __zt_tmp))
            econtext['rkey'] = __value
            __backup_rkey_alt_140007911842880 = get('rkey_alt', __marker)

            # <Value "python:'desc' if rkey=='asc' else 'asc'" (44:27)> -> __value
            __token = 2497
            try:
                __zt_tmp = __attrs_140007911546528
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140007999378224('python', "'desc' if rkey=='asc' else 'asc'", econtext=econtext)(_static_140007999377936(econtext, __zt_tmp))
            econtext['rkey_alt'] = __value
            __backup_obs_140007911843456 = get('obs', __marker)

            # <Value 'python: indexes.manage_get_sortedObjects(sortkey=skey, revkey=rkey)' (45:21)> -> __value
            __token = 2561
            try:
                __zt_tmp = __attrs_140007911546528
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140007999378224('python', ' indexes.manage_get_sortedObjects(sortkey=skey, revkey=rkey)', econtext=econtext)(_static_140007999377936(econtext, __zt_tmp))
            econtext['obs'] = __value
            __append('\n                ')

            # <Static value=<ast.Dict object at 0x7f56272e66b0> name=None at 7f56272e69e0> -> __attrs_140007911544560
            __attrs_140007911544560 = _static_140008001267376

            # <Value 'obs' (46:42)> -> __condition
            __token = 2677
            try:
                __zt_tmp = __attrs_140007911544560
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140007999378224('path', 'obs', econtext=econtext)(_static_140007999377936(econtext, __zt_tmp))
            if __condition:
                __append('\n                    ')

                # <Static value=<ast.Dict object at 0x7f5621d55480> name=None at 7f5621d553c0> -> __attrs_140007911543408
                __attrs_140007911543408 = _static_140007911543936

                # <table ... (0:0)
                # --------------------------------------------------------
                __append('<table class="table table-striped table-hover table-sm objectItems">\n                        ')

                # <Static value=<ast.Dict object at 0x7f5621d54eb0> name=None at 7f5621d54ee0> -> __attrs_140007911541824
                __attrs_140007911541824 = _static_140007911542448

                # <thead ... (0:0)
                # --------------------------------------------------------
                __append('<thead')

                # <Symbol value=<DEFAULT> at 7f562726ee00> -> __default_140007911542784
                __default_140007911542784 = _DEFAULT_MARKER

                # <Substitution "python:'thead-light sorted_%s'%(request.get('rkey',''))" (48:73)> -> __attr_class
                __token = 2845
                try:
                    __zt_tmp = __attrs_140007911541824
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_class = _static_140007999378224('python', "'thead-light sorted_%s'%(request.get('rkey',''))", econtext=econtext)(_static_140007999377936(econtext, __zt_tmp))
                __attr_class = __quote(__attr_class, '"', '&quot;', 'thead-light', _DEFAULT_MARKER)
                if (__attr_class is not None):
                    __append((' class="%s"' % __attr_class))
                __append('>\n                            ')

                # <Static value=<ast.Dict object at 0x7f56272e66b0> name=None at 7f56272e69e0> -> __attrs_140007911540864
                __attrs_140007911540864 = _static_140008001267376

                # <tr ... (0:0)
                # --------------------------------------------------------
                __append('<tr>\n                                ')

                # <Static value=<ast.Dict object at 0x7f5621d542e0> name=None at 7f5621d54160> -> __attrs_140007911539376
                __attrs_140007911539376 = _static_140007911539424

                # <th ... (0:0)
                # --------------------------------------------------------
                __append('<th scope="col" class="zmi-object-check text-right text-nowrap">\n                                    ')

                # <Static value=<ast.Dict object at 0x7f5621d56e90> name=None at 7f5621d57a00> -> __attrs_140007911569248
                __attrs_140007911569248 = _static_140007911550608

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="checkbox" id="checkAll" onclick="checkbox_all();" />\n                                </th>\n                                ')

                # <Static value=<ast.Dict object at 0x7f5621d5b3d0> name=None at 7f5621d5b7c0> -> __attrs_140007911568096
                __attrs_140007911568096 = _static_140007911568336

                # <th ... (0:0)
                # --------------------------------------------------------
                __append('<th scope="col" class="zmi-object-id">\n                                    ')

                # <Static value=<ast.Dict object at 0x7f5621d5aa70> name=None at 7f5621d5ac80> -> __attrs_140007911565216
                __attrs_140007911565216 = _static_140007911565936

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a')

                # <Symbol value=<DEFAULT> at 7f562726ee00> -> __default_140007911566944
                __default_140007911566944 = _DEFAULT_MARKER

                # <Substitution "python:'Sort %s by Name'%( rkey_alt.upper() )" (57:50)> -> __attr_title
                __token = 3486
                try:
                    __zt_tmp = __attrs_140007911565216
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_title = _static_140007999378224('python', "'Sort %s by Name'%( rkey_alt.upper() )", econtext=econtext)(_static_140007999377936(econtext, __zt_tmp))
                __attr_title = __quote(__attr_title, '"', '&quot;', 'Sort Ascending by Name', _DEFAULT_MARKER)
                if (__attr_title is not None):
                    __append((' title="%s"' % __attr_title))

                # <Symbol value=<DEFAULT> at 7f562726ee00> -> __default_140007911566176
                __default_140007911566176 = _DEFAULT_MARKER

                # <Substitution "python:'?skey=id&rkey=%s'%( rkey_alt )" (58:48)> -> __attr_href
                __token = 3581
                try:
                    __zt_tmp = __attrs_140007911565216
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_140007999378224('python', "'?skey=id&rkey=%s'%( rkey_alt )", econtext=econtext)(_static_140007999377936(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', '?skey=id&rkey=asc', _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((' href="%s"' % __attr_href))

                # <Symbol value=<DEFAULT> at 7f562726ee00> -> __default_140007911565696
                __default_140007911565696 = _DEFAULT_MARKER

                # <Substitution "python:request.get('skey',None)=='id' and 'zmi-sort_key' or None" (59:48)> -> __attr_class
                __token = 3670
                try:
                    __zt_tmp = __attrs_140007911565216
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_class = _static_140007999378224('python', "request.get('skey',None)=='id' and 'zmi-sort_key' or None", econtext=econtext)(_static_140007999377936(econtext, __zt_tmp))
                __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_class is not None):
                    __append((' class="%s"' % __attr_class))
                __append('>\n                                        Name\n                                        ')

                # <Static value=<ast.Dict object at 0x7f5621d5a380> name=None at 7f5621d5a2c0> -> __attrs_140007911563776
                __attrs_140007911563776 = _static_140007911564160

                # <i ... (0:0)
                # --------------------------------------------------------
                __append('<i class="fa fa-sort"></i>\n                                    </a>\n                                </th>\n                                ')

                # <Static value=<ast.Dict object at 0x7f5621d59cf0> name=None at 7f5621d59c30> -> __attrs_140007911562192
                __attrs_140007911562192 = _static_140007911562480

                # <th ... (0:0)
                # --------------------------------------------------------
                __append('<th scope="col" class="zmi-object-indextype text-nowrap">\n                                    ')

                # <Static value=<ast.Dict object at 0x7f5621d595a0> name=None at 7f5621d595d0> -> __attrs_140007911559408
                __attrs_140007911559408 = _static_140007911560608

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a')

                # <Symbol value=<DEFAULT> at 7f562726ee00> -> __default_140007911561136
                __default_140007911561136 = _DEFAULT_MARKER

                # <Substitution "python:'Sort %s by index type'%( rkey_alt.upper() )" (68:50)> -> __attr_title
                __token = 4276
                try:
                    __zt_tmp = __attrs_140007911559408
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_title = _static_140007999378224('python', "'Sort %s by index type'%( rkey_alt.upper() )", econtext=econtext)(_static_140007999377936(econtext, __zt_tmp))
                __attr_title = __quote(__attr_title, '"', '&quot;', 'Sort Ascending by index type', _DEFAULT_MARKER)
                if (__attr_title is not None):
                    __append((' title="%s"' % __attr_title))

                # <Symbol value=<DEFAULT> at 7f562726ee00> -> __default_140007911560320
                __default_140007911560320 = _DEFAULT_MARKER

                # <Substitution "python:'?skey=meta_type&rkey=%s'%( rkey_alt )" (69:48)> -> __attr_href
                __token = 4377
                try:
                    __zt_tmp = __attrs_140007911559408
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_140007999378224('python', "'?skey=meta_type&rkey=%s'%( rkey_alt )", econtext=econtext)(_static_140007999377936(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', '?skey=meta_type&rkey=asc', _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((' href="%s"' % __attr_href))

                # <Symbol value=<DEFAULT> at 7f562726ee00> -> __default_140007911560128
                __default_140007911560128 = _DEFAULT_MARKER

                # <Substitution "python:request.get('skey',None)=='meta_type' and 'zmi-sort_key' or None" (70:48)> -> __attr_class
                __token = 4473
                try:
                    __zt_tmp = __attrs_140007911559408
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_class = _static_140007999378224('python', "request.get('skey',None)=='meta_type' and 'zmi-sort_key' or None", econtext=econtext)(_static_140007999377936(econtext, __zt_tmp))
                __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_class is not None):
                    __append((' class="%s"' % __attr_class))
                __append('>\n                                        Index type\n                                        ')

                # <Static value=<ast.Dict object at 0x7f5621d58d30> name=None at 7f5621d58ca0> -> __attrs_140007911558112
                __attrs_140007911558112 = _static_140007911558448

                # <i ... (0:0)
                # --------------------------------------------------------
                __append('<i class="fa fa-sort"></i>\n                                    </a>\n                                </th>\n                                ')

                # <Static value=<ast.Dict object at 0x7f5621d58610> name=None at 7f5621d587c0> -> __attrs_140007911556768
                __attrs_140007911556768 = _static_140007911556624

                # <th ... (0:0)
                # --------------------------------------------------------
                __append('<th scope="col" class="zmi-object-size hidden-xs text-nowrap">\n                                    ')

                # <Static value=<ast.Dict object at 0x7f5621d58160> name=None at 7f5621d5bcd0> -> __attrs_140007911620912
                __attrs_140007911620912 = _static_140007911555424

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a')

                # <Symbol value=<DEFAULT> at 7f562726ee00> -> __default_140007911555808
                __default_140007911555808 = _DEFAULT_MARKER

                # <Substitution "python:'Sort %s by indexed values'%( rkey_alt.upper() )" (79:50)> -> __attr_title
                __token = 5101
                try:
                    __zt_tmp = __attrs_140007911620912
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_title = _static_140007999378224('python', "'Sort %s by indexed values'%( rkey_alt.upper() )", econtext=econtext)(_static_140007999377936(econtext, __zt_tmp))
                __attr_title = __quote(__attr_title, '"', '&quot;', 'Sort Ascending by indexed values', _DEFAULT_MARKER)
                if (__attr_title is not None):
                    __append((' title="%s"' % __attr_title))

                # <Symbol value=<DEFAULT> at 7f562726ee00> -> __default_140007911570880
                __default_140007911570880 = _DEFAULT_MARKER

                # <Substitution "python:'?skey=indexSize&rkey=%s'%( rkey_alt )" (80:48)> -> __attr_href
                __token = 5206
                try:
                    __zt_tmp = __attrs_140007911620912
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_140007999378224('python', "'?skey=indexSize&rkey=%s'%( rkey_alt )", econtext=econtext)(_static_140007999377936(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', '?skey=indexSize&rkey=asc', _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((' href="%s"' % __attr_href))

                # <Symbol value=<DEFAULT> at 7f562726ee00> -> __default_140007911571168
                __default_140007911571168 = _DEFAULT_MARKER

                # <Substitution "python:request.get('skey',None)=='indexSize' and 'zmi-sort_key' or None" (81:48)> -> __attr_class
                __token = 5302
                try:
                    __zt_tmp = __attrs_140007911620912
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_class = _static_140007999378224('python', "request.get('skey',None)=='indexSize' and 'zmi-sort_key' or None", econtext=econtext)(_static_140007999377936(econtext, __zt_tmp))
                __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_class is not None):
                    __append((' class="%s"' % __attr_class))
                __append('>\n                                        # distinct values\n                                        ')

                # <Static value=<ast.Dict object at 0x7f5621d684f0> name=None at 7f5621d68520> -> __attrs_140007911622256
                __attrs_140007911622256 = _static_140007911621872

                # <i ... (0:0)
                # --------------------------------------------------------
                __append('<i class="fa fa-sort"></i>\n                                    </a>\n                                </th>\n                            </tr>\n                        </thead>\n                        ')

                # <Static value=<ast.Dict object at 0x7f56272e66b0> name=None at 7f56272e69e0> -> __attrs_140007911622688
                __attrs_140007911622688 = _static_140008001267376

                # <tbody ... (0:0)
                # --------------------------------------------------------
                __append('<tbody>\n                            ')

                # <Static value=<ast.Dict object at 0x7f56272e66b0> name=None at 7f56272e69e0> -> __attrs_140007911623648
                __attrs_140007911623648 = _static_140008001267376
                __backup_ob_dict_140007911920432 = get('ob_dict', __marker)

                # <Value 'obs' (89:52)> -> __iterator
                __token = 5734
                try:
                    __zt_tmp = __attrs_140007911623648
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140007999378224('path', 'obs', econtext=econtext)(_static_140007999377936(econtext, __zt_tmp))
                (__iterator, ____index_140007911623888, ) = getname('repeat')('ob_dict', __iterator)
                econtext['ob_dict'] = None
                for __item in __iterator:
                    econtext['ob_dict'] = __item

                    # <tr ... (0:0)
                    # --------------------------------------------------------
                    __append('<tr>\n                                ')

                    # <Static value=<ast.Dict object at 0x7f56272e66b0> name=None at 7f56272e69e0> -> __attrs_140007911624752
                    __attrs_140007911624752 = _static_140008001267376
                    __backup_ob_140007911921200 = get('ob', __marker)

                    # <Value 'nocall:ob_dict/obj' (90:52)> -> __value
                    __token = 5792
                    try:
                        __zt_tmp = __attrs_140007911624752
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140007999378224('nocall', 'ob_dict/obj', econtext=econtext)(_static_140007999377936(econtext, __zt_tmp))
                    econtext['ob'] = __value
                    __append('\n                                    ')

                    # <Static value=<ast.Dict object at 0x7f5621d69660> name=None at 7f5621d69690> -> __attrs_140007911626576
                    __attrs_140007911626576 = _static_140007911626336

                    # <td ... (0:0)
                    # --------------------------------------------------------
                    __append('<td class="zmi-object-check text-right" onclick="$(this).children(\'input\').trigger(\'click\');">\n                                        ')

                    # <Static value=<ast.Dict object at 0x7f5621d6a080> name=None at 7f5621d6a0b0> -> __attrs_140007911627200
                    __attrs_140007911627200 = _static_140007911628928

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input type="checkbox" class="checkbox-list-item" name="ids:list"                                         onclick="event.stopPropagation();select_objectitem($(this));"')

                    # <Symbol value=<DEFAULT> at 7f562726ee00> -> __default_140007911627776
                    __default_140007911627776 = _DEFAULT_MARKER

                    # <Substitution 'ob_dict/id' (92:128)> -> __attr_value
                    __token = 6072
                    try:
                        __zt_tmp = __attrs_140007911627200
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_140007999378224('path', 'ob_dict/id', econtext=econtext)(_static_140007999377936(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append(' />\n                                    </td>\n                                    ')

                    # <Static value=<ast.Dict object at 0x7f56272e66b0> name=None at 7f56272e69e0> -> __attrs_140007911629840
                    __attrs_140007911629840 = _static_140008001267376

                    # <td ... (0:0)
                    # --------------------------------------------------------
                    __append('<td>\n                                        ')

                    # <Static value=<ast.Dict object at 0x7f5621d6aa70> name=None at 7f5621d6aaa0> -> __attrs_140007911632048
                    __attrs_140007911632048 = _static_140007911631472

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 7f562726ee00> -> __default_140007911631136
                    __default_140007911631136 = _DEFAULT_MARKER

                    # <Substitution 'string:Indexes/${ob_dict/quoted_id}/manage_workspace' (96:64)> -> __attr_href
                    __token = 6337
                    try:
                        __zt_tmp = __attrs_140007911632048
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140007999378224('string', 'Indexes/${ob_dict/quoted_id}/manage_workspace', econtext=econtext)(_static_140007999377936(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))
                    __append('>')

                    # <Symbol value=<DEFAULT> at 7f562726ee00> -> __default_140007911630944
                    __default_140007911630944 = _DEFAULT_MARKER

                    # <Value 'ob_dict/id' (96:131)> -> __cache_140007911630464
                    __token = 6404
                    try:
                        __zt_tmp = __attrs_140007911632048
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140007911630464 = _static_140007999378224('path', 'ob_dict/id', econtext=econtext)(_static_140007999377936(econtext, __zt_tmp))

                    # <BinOp left=<Value 'ob_dict/id' (96:131)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f562726ee00> at 7f5621d6a740> -> __condition
                    __expression = __cache_140007911630464

                    # <Symbol value=<DEFAULT> at 7f562726ee00> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140007911630464
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</a>\n                                        ')
                    ____fallback_140008001043824 = len(__stream)
                    try:

                        # <Static value=<ast.Dict object at 0x7f56272e66b0> name=None at 7f56272e69e0> -> __attrs_140007911633104
                        __attrs_140007911633104 = _static_140008001267376
                        __backup_sourcenames_140007911927344 = get('sourcenames', __marker)

                        # <Value 'ob/getIndexSourceNames' (97:71)> -> __value
                        __token = 6492
                        try:
                            __zt_tmp = __attrs_140007911633104
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140007999378224('path', 'ob/getIndexSourceNames', econtext=econtext)(_static_140007999377936(econtext, __zt_tmp))
                        econtext['sourcenames'] = __value

                        # <Value "python: len(sourcenames) != 1 or sourcenames[0] != ob_dict['id']" (98:55)> -> __condition
                        __token = 6571
                        try:
                            __zt_tmp = __attrs_140007911633104
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140007999378224('python', " len(sourcenames) != 1 or sourcenames[0] != ob_dict['id']", econtext=econtext)(_static_140007999377936(econtext, __zt_tmp))
                        if __condition:

                            # <small ... (0:0)
                            # --------------------------------------------------------
                            __append('<small>\n                                            (indexed attributes: ')

                            # <Static value=<ast.Dict object at 0x7f56272e66b0> name=None at 7f56272e69e0> -> __attrs_140007911635408
                            __attrs_140007911635408 = _static_140008001267376

                            # <Symbol value=<DEFAULT> at 7f562726ee00> -> __default_140007911635216
                            __default_140007911635216 = _DEFAULT_MARKER

                            # <Value "python: ', '.join(sourcenames)" (100:84)> -> __cache_140007911634736
                            __token = 6811
                            try:
                                __zt_tmp = __attrs_140007911635408
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140007911634736 = _static_140007999378224('python', " ', '.join(sourcenames)", econtext=econtext)(_static_140007999377936(econtext, __zt_tmp))

                            # <BinOp left=<Value "python: ', '.join(sourcenames)" (100:84)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f562726ee00> at 7f5621d6b7f0> -> __condition
                            __expression = __cache_140007911634736

                            # <Symbol value=<DEFAULT> at 7f562726ee00> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:

                                # <span ... (0:0)
                                # --------------------------------------------------------
                                __append('<span/>')
                            else:
                                __content = __cache_140007911634736
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append(__content)
                            __append(')       \n                                        </small>')
                        if (__backup_sourcenames_140007911927344 is __marker):
                            del econtext['sourcenames']
                        else:
                            econtext['sourcenames'] = __backup_sourcenames_140007911927344
                    except (Exception, ) as __exc:
                        econtext['error'] = _ErrorInfo(__exc, __tokens[__token][1:3])
                        if (on_error_handler is not None):
                            on_error_handler(__exc)
                        del __stream[____fallback_140008001043824:]

                        # <small ... (0:0)
                        # --------------------------------------------------------
                        __append('<small>')

                        # <Value 'string:(${ob_dict/title|nothing})' (99:54)> -> __content
                        __token = 6691
                        try:
                            __zt_tmp = __attrs_140007911629840
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __content = _static_140007999378224('string', '(${ob_dict/title|nothing})', econtext=econtext)(_static_140007999377936(econtext, __zt_tmp))
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                        __append('</small>')

                    __append('\n                                    </td>\n                                    ')

                    # <Static value=<ast.Dict object at 0x7f5621d6bf70> name=None at 7f5621d6bfa0> -> __attrs_140007911653680
                    __attrs_140007911653680 = _static_140007911636848

                    # <td ... (0:0)
                    # --------------------------------------------------------
                    __append('<td class="text-left">')

                    # <Symbol value=<DEFAULT> at 7f562726ee00> -> __default_140007911636272
                    __default_140007911636272 = _DEFAULT_MARKER

                    # <Value 'ob/meta_type' (103:71)> -> __cache_140007911635792
                    __token = 7015
                    try:
                        __zt_tmp = __attrs_140007911653680
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140007911635792 = _static_140007999378224('path', 'ob/meta_type', econtext=econtext)(_static_140007999377936(econtext, __zt_tmp))

                    # <BinOp left=<Value 'ob/meta_type' (103:71)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f562726ee00> at 7f5621d6bc10> -> __condition
                    __expression = __cache_140007911635792

                    # <Symbol value=<DEFAULT> at 7f562726ee00> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140007911635792
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</td>\n                                    ')

                    # <Static value=<ast.Dict object at 0x7f5621d706d0> name=None at 7f5621d70700> -> __attrs_140007911655552
                    __attrs_140007911655552 = _static_140007911655120

                    # <td ... (0:0)
                    # --------------------------------------------------------
                    __append('<td class="text-left zmi-object-size hidden-xs">')

                    # <Symbol value=<DEFAULT> at 7f562726ee00> -> __default_140007911654592
                    __default_140007911654592 = _DEFAULT_MARKER

                    # <Value 'ob/indexSize|string:n/a' (105:57)> -> __cache_140007911654112
                    __token = 7176
                    try:
                        __zt_tmp = __attrs_140007911655552
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140007911654112 = _static_140007999378224('path', 'ob/indexSize|string:n/a', econtext=econtext)(_static_140007999377936(econtext, __zt_tmp))

                    # <BinOp left=<Value 'ob/indexSize|string:n/a' (105:57)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f562726ee00> at 7f5621d703a0> -> __condition
                    __expression = __cache_140007911654112

                    # <Symbol value=<DEFAULT> at 7f562726ee00> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n                                    ')
                    else:
                        __content = __cache_140007911654112
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</td>\n                                ')
                    if (__backup_ob_140007911921200 is __marker):
                        del econtext['ob']
                    else:
                        econtext['ob'] = __backup_ob_140007911921200
                    __append('\n                            </tr>')
                    ____index_140007911623888 -= 1
                    if (____index_140007911623888 > 0):
                        __append('\n                            ')
                if (__backup_ob_dict_140007911920432 is __marker):
                    del econtext['ob_dict']
                else:
                    econtext['ob_dict'] = __backup_ob_dict_140007911920432
                __append('\n                        </tbody>\n                    </table>\n\n                    ')

                # <Static value=<ast.Dict object at 0x7f5621d68f40> name=None at 7f5621d69150> -> __attrs_140007911656224
                __attrs_140007911656224 = _static_140007911624512

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="zmi-controls">\n                        ')

                # <Static value=<ast.Dict object at 0x7f5621d71420> name=None at 7f5621d71450> -> __attrs_140007911657328
                __attrs_140007911657328 = _static_140007911658528

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input class="btn btn-primary" type="submit" name="manage_delIndex:method" value="Remove index" />\n                        ')

                # <Static value=<ast.Dict object at 0x7f5621d71b10> name=None at 7f5621d71b40> -> __attrs_140007911659104
                __attrs_140007911659104 = _static_140007911660304

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input class="btn btn-primary" type="submit" name="manage_reindexIndex:method" value="Reindex" />\n                        ')

                # <Static value=<ast.Dict object at 0x7f5621d72200> name=None at 7f5621d72230> -> __attrs_140007911660880
                __attrs_140007911660880 = _static_140007911662080

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input class="btn btn-primary" type="submit" name="manage_clearIndex:method" value="Clear index" />\n                    </div>\n\n                ')
            __append('\n\n                ')

            # <Static value=<ast.Dict object at 0x7f56272e66b0> name=None at 7f56272e69e0> -> __attrs_140007911660688
            __attrs_140007911660688 = _static_140008001267376

            # <Value 'not: obs' (120:40)> -> __condition
            __token = 7902
            try:
                __zt_tmp = __attrs_140007911660688
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140007999378224('not', ' obs', econtext=econtext)(_static_140007999377936(econtext, __zt_tmp))
            if __condition:
                __append('\n                    ')

                # <Static value=<ast.Dict object at 0x7f5621d725c0> name=None at 7f5621d725f0> -> __attrs_140007911663472
                __attrs_140007911663472 = _static_140007911663040

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="alert alert-info">There are currently no indexes</div>\n                ')
            __append('\n\n            ')
            if (__backup_obs_140007911843456 is __marker):
                del econtext['obs']
            else:
                econtext['obs'] = __backup_obs_140007911843456
            if (__backup_rkey_alt_140007911842880 is __marker):
                del econtext['rkey_alt']
            else:
                econtext['rkey_alt'] = __backup_rkey_alt_140007911842880
            if (__backup_rkey_140007911842592 is __marker):
                del econtext['rkey']
            else:
                econtext['rkey'] = __backup_rkey_140007911842592
            if (__backup_skey_140007911842064 is __marker):
                del econtext['skey']
            else:
                econtext['skey'] = __backup_skey_140007911842064
            __append('\n        </form>\n    ')
            if (__backup_indexes_140007911839952 is __marker):
                del econtext['indexes']
            else:
                econtext['indexes'] = __backup_indexes_140007911839952
            __append('\n</main>\n\n')

            # <Static value=<ast.Dict object at 0x7f56272e66b0> name=None at 7f56272e69e0> -> __attrs_140007911546576
            __attrs_140007911546576 = _static_140008001267376

            # <script ... (0:0)
            # --------------------------------------------------------
            __append("<script>\n//<!--\n    // +++++++++++++++++++++++++++\n    // Item  Selection\n    // +++++++++++++++++++++++++++\n    function checkbox_all() {\n    var checkboxes = document.getElementsByClassName('checkbox-list-item');\n    // Toggle Highlighting CSS-Class\n    if (document.getElementById('checkAll').checked) {\n        $('table.objectItems tbody tr').addClass('checked');\n    } else {\n        $('table.objectItems tbody tr').removeClass('checked');\n    };\n    // Set Checkbox like checkAll-Box\n    for (i = 0; i < checkboxes.length; i++) {\n        checkboxes[i].checked = document.getElementById('checkAll').checked;\n    }\n    };\n//-->\n</script>\n\n")

            # <Static value=<ast.Dict object at 0x7f56272e66b0> name=None at 7f56272e69e0> -> __attrs_140007911664576
            __attrs_140007911664576 = _static_140008001267376

            # <Symbol value=<DEFAULT> at 7f562726ee00> -> __default_140007911664384
            __default_140007911664384 = _DEFAULT_MARKER

            # <Value 'here/manage_page_footer' (150:31)> -> __cache_140007911663904
            __token = 8775
            try:
                __zt_tmp = __attrs_140007911664576
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140007911663904 = _static_140007999378224('path', 'here/manage_page_footer', econtext=econtext)(_static_140007999377936(econtext, __zt_tmp))

            # <BinOp left=<Value 'here/manage_page_footer' (150:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f562726ee00> at 7f5621d729e0> -> __condition
            __expression = __cache_140007911663904

            # <Symbol value=<DEFAULT> at 7f562726ee00> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140007911663904
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }