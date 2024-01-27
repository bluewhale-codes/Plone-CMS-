# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/plone/app/portlets/portlets/navigation.pt'

__tokens = {260: ('view/navigation_root', 9, 14), 395: ("python:view.hasName() and 'card-header' or 'card-header hiddenStructure'", 16, 17), 602: ('string:${view/heading_link_target}', 23, 16), 548: ('view/title', 21, 22), 832: ('view/root_item_class', 32, 28), 876: (" python:selectedClass and ' navTreeCurrentNode' or '", 33, 22), 959: ('g nocall:context/plone_utils/normalizeStri', 34, 28), 1030: ('le root/Ti', 35, 25), 1063: ('ion python:normalizeString(section_ti', 36, 18), 1147: ('view/include_top', 38, 27), 1214: ('string:navTreeItem navTreeTopNode${li_class} nav-section-${section}', 40, 20), 1365: ('view/root_is_portal', 44, 30), 1412: (' root/portal_typ', 45, 26), 1462: ("s python:'contenttype-' + normalizeString(root_typ", 46, 31), 1541: ("ss python:rootIsPortal and 'contenttype-plone-site' or root_type_cl", 47, 25), 1685: ('root/absolute_url', 50, 22), 1726: (' root/Descriptio', 51, 22), 1766: ("s python:' '.join([root_class, selectedClass]).strip", 52, 21), 1875: ('rootIsPortal', 54, 35), 2034: ('not:rootIsPortal', 58, 35), 2085: ('root/Title', 59, 33), 2218: ('view/createNavTree', 64, 35)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140097338215248 = {'href': 'root/absolute_url', 'title': 'root/Description', 'class': "python:' '.join([root_class, selectedClass]).strip()", }
_static_140097412968080 = {}
_static_140097338222592 = {'class': 'string:navTreeItem navTreeTopNode${li_class} nav-section-${section}', }
_static_140097338214480 = {'class': 'navTree navTreeLevel0', }
_static_140097338214288 = {'class': 'card-body', }
_static_140097338213040 = {'class': 'tile', 'href': '#', }
_static_140097338215968 = {'class': 'card-header', }
_static_140097413192176 = __C2ZContextWrapper
_static_140097413192464 = __compile_zt_expr
_static_140097338219136 = {'class': 'card portlet portletNavigationTree', }
_static_140097339394464 = {'xmlns': 'http://www.w3.org/1999/xhtml', }

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

            # <Static value=<ast.Dict object at 0x7f6af42609a0> name=None at 7f6af4260850> -> __attrs_140097339401952
            __attrs_140097339401952 = _static_140097339394464
            __append('\n\n  ')

            # <Static value=<ast.Dict object at 0x7f6af4141a80> name=None at 7f6af4141d80> -> __attrs_140097338215776
            __attrs_140097338215776 = _static_140097338219136
            __backup_root_140097252852640 = get('root', __marker)

            # <Value 'view/navigation_root' (9:14)> -> __value
            __token = 260
            try:
                __zt_tmp = __attrs_140097338215776
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('path', 'view/navigation_root', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['root'] = __value
            __previous_i18n_domain_140097338217072 = __i18n_domain
            __i18n_domain = 'plone'

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="card portlet portletNavigationTree" >\n\n    ')

            # <Static value=<ast.Dict object at 0x7f6af4140e20> name=None at 7f6af4140ee0> -> __attrs_140097338220528
            __attrs_140097338220528 = _static_140097338215968

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div')

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338218992
            __default_140097338218992 = _DEFAULT_MARKER

            # <Substitution "python:view.hasName() and 'card-header' or 'card-header hiddenStructure'" (16:17)> -> __attr_class
            __token = 395
            try:
                __zt_tmp = __attrs_140097338220528
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_140097413192464('python', "view.hasName() and 'card-header' or 'card-header hiddenStructure'", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', 'card-header', _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((' class="%s"' % __attr_class))
            __append(' >\n      ')

            # <Static value=<ast.Dict object at 0x7f6af41402b0> name=None at 7f6af41402e0> -> __attrs_140097338212800
            __attrs_140097338212800 = _static_140097338213040

            # <a ... (0:0)
            # --------------------------------------------------------
            __append('<a class="tile"')

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338216688
            __default_140097338216688 = _DEFAULT_MARKER

            # <Substitution 'string:${view/heading_link_target}' (23:16)> -> __attr_href
            __token = 602
            try:
                __zt_tmp = __attrs_140097338212800
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_140097413192464('string', '${view/heading_link_target}', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', '#', _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((' href="%s"' % __attr_href))
            __append(' >')

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338221728
            __default_140097338221728 = _DEFAULT_MARKER

            # <Value 'view/title' (21:22)> -> __cache_140097338217648
            __token = 548
            try:
                __zt_tmp = __attrs_140097338212800
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140097338217648 = _static_140097413192464('path', 'view/title', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

            # <BinOp left=<Value 'view/title' (21:22)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6af4141030> -> __condition
            __expression = __cache_140097338217648

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                __append('Navigation')
            else:
                __content = __cache_140097338217648
                __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append('</a>\n    </div>\n\n    ')

            # <Static value=<ast.Dict object at 0x7f6af4140790> name=None at 7f6af4140730> -> __attrs_140097338225040
            __attrs_140097338225040 = _static_140097338214288

            # <nav ... (0:0)
            # --------------------------------------------------------
            __append('<nav class="card-body">\n      ')

            # <Static value=<ast.Dict object at 0x7f6af4140850> name=None at 7f6af4142e30> -> __attrs_140097338223792
            __attrs_140097338223792 = _static_140097338214480

            # <ul ... (0:0)
            # --------------------------------------------------------
            __append('<ul class="navTree navTreeLevel0">\n        ')

            # <Static value=<ast.Dict object at 0x7f6af4142800> name=None at 7f6af4142860> -> __attrs_140097338225136
            __attrs_140097338225136 = _static_140097338222592
            __backup_selectedClass_140097342771200 = get('selectedClass', __marker)

            # <Value 'view/root_item_class' (32:28)> -> __value
            __token = 832
            try:
                __zt_tmp = __attrs_140097338225136
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('path', 'view/root_item_class', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['selectedClass'] = __value
            __backup_li_class_140097337737760 = get('li_class', __marker)

            # <Value "python:selectedClass and ' navTreeCurrentNode' or ''" (33:22)> -> __value
            __token = 876
            try:
                __zt_tmp = __attrs_140097338225136
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('python', "selectedClass and ' navTreeCurrentNode' or ''", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['li_class'] = __value
            __backup_normalizeString_140097342771296 = get('normalizeString', __marker)

            # <Value 'nocall:context/plone_utils/normalizeString' (34:28)> -> __value
            __token = 959
            try:
                __zt_tmp = __attrs_140097338225136
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('nocall', 'context/plone_utils/normalizeString', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['normalizeString'] = __value
            __backup_section_title_140097340072064 = get('section_title', __marker)

            # <Value 'root/Title' (35:25)> -> __value
            __token = 1030
            try:
                __zt_tmp = __attrs_140097338225136
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('path', 'root/Title', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['section_title'] = __value
            __backup_section_140097337632720 = get('section', __marker)

            # <Value 'python:normalizeString(section_title)' (36:18)> -> __value
            __token = 1063
            try:
                __zt_tmp = __attrs_140097338225136
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('python', 'normalizeString(section_title)', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['section'] = __value

            # <Value 'view/include_top' (38:27)> -> __condition
            __token = 1147
            try:
                __zt_tmp = __attrs_140097338225136
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140097413192464('path', 'view/include_top', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            if __condition:

                # <li ... (0:0)
                # --------------------------------------------------------
                __append('<li')

                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338222400
                __default_140097338222400 = _DEFAULT_MARKER

                # <Substitution 'string:navTreeItem navTreeTopNode${li_class} nav-section-${section}' (40:20)> -> __attr_class
                __token = 1214
                try:
                    __zt_tmp = __attrs_140097338225136
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_class = _static_140097413192464('string', 'navTreeItem navTreeTopNode${li_class} nav-section-${section}', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_class is not None):
                    __append((' class="%s"' % __attr_class))
                __append(' >\n          ')

                # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097338227728
                __attrs_140097338227728 = _static_140097412968080
                __backup_rootIsPortal_140097337741936 = get('rootIsPortal', __marker)

                # <Value 'view/root_is_portal' (44:30)> -> __value
                __token = 1365
                try:
                    __zt_tmp = __attrs_140097338227728
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140097413192464('path', 'view/root_is_portal', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                econtext['rootIsPortal'] = __value
                __backup_root_type_140097338343584 = get('root_type', __marker)

                # <Value 'root/portal_type' (45:26)> -> __value
                __token = 1412
                try:
                    __zt_tmp = __attrs_140097338227728
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140097413192464('path', 'root/portal_type', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                econtext['root_type'] = __value
                __backup_root_type_class_140097340074848 = get('root_type_class', __marker)

                # <Value "python:'contenttype-' + normalizeString(root_type)" (46:31)> -> __value
                __token = 1462
                try:
                    __zt_tmp = __attrs_140097338227728
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140097413192464('python', "'contenttype-' + normalizeString(root_type)", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                econtext['root_type_class'] = __value
                __backup_root_class_140097252813904 = get('root_class', __marker)

                # <Value "python:rootIsPortal and 'contenttype-plone-site' or root_type_class" (47:25)> -> __value
                __token = 1541
                try:
                    __zt_tmp = __attrs_140097338227728
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140097413192464('python', "rootIsPortal and 'contenttype-plone-site' or root_type_class", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                econtext['root_class'] = __value

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div>\n            ')

                # <Static value=<ast.Dict object at 0x7f6af4140b50> name=None at 7f6af4142d70> -> __attrs_140097338213328
                __attrs_140097338213328 = _static_140097338215248

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a')

                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338221104
                __default_140097338221104 = _DEFAULT_MARKER

                # <Substitution 'root/absolute_url' (50:22)> -> __attr_href
                __token = 1685
                try:
                    __zt_tmp = __attrs_140097338213328
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_140097413192464('path', 'root/absolute_url', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((' href="%s"' % __attr_href))

                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338225376
                __default_140097338225376 = _DEFAULT_MARKER

                # <Substitution 'root/Description' (51:22)> -> __attr_title
                __token = 1726
                try:
                    __zt_tmp = __attrs_140097338213328
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_title = _static_140097413192464('path', 'root/Description', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_title is not None):
                    __append((' title="%s"' % __attr_title))

                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338225520
                __default_140097338225520 = _DEFAULT_MARKER

                # <Substitution "python:' '.join([root_class, selectedClass]).strip()" (52:21)> -> __attr_class
                __token = 1766
                try:
                    __zt_tmp = __attrs_140097338213328
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_class = _static_140097413192464('python', "' '.join([root_class, selectedClass]).strip()", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_class is not None):
                    __append((' class="%s"' % __attr_class))
                __append('>\n              ')

                # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097252866944
                __attrs_140097252866944 = _static_140097412968080

                # <Value 'rootIsPortal' (54:35)> -> __condition
                __token = 1875
                try:
                    __zt_tmp = __attrs_140097252866944
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140097413192464('path', 'rootIsPortal', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                if __condition:
                    __stream_140097252866032 = []
                    __append_140097252866032 = __stream_140097252866032.append
                    __append_140097252866032('Home')
                    __msgid_140097252866032 = __re_whitespace(''.join(__stream_140097252866032)).strip()
                    if 'tabs_home':
                        __append(translate('tabs_home', mapping=None, default=__msgid_140097252866032, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('\n              ')

                # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097252865360
                __attrs_140097252865360 = _static_140097412968080

                # <Value 'not:rootIsPortal' (58:35)> -> __condition
                __token = 2034
                try:
                    __zt_tmp = __attrs_140097252865360
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140097413192464('not', 'rootIsPortal', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                if __condition:

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252867904
                    __default_140097252867904 = _DEFAULT_MARKER

                    # <Value 'root/Title' (59:33)> -> __cache_140097252865504
                    __token = 2085
                    try:
                        __zt_tmp = __attrs_140097252865360
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140097252865504 = _static_140097413192464('path', 'root/Title', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                    # <BinOp left=<Value 'root/Title' (59:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeefdbd90> -> __condition
                    __expression = __cache_140097252865504

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span >Root item title</span>')
                    else:
                        __content = __cache_140097252865504
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                __append('\n            </a>\n          </div>')
                if (__backup_root_class_140097252813904 is __marker):
                    del econtext['root_class']
                else:
                    econtext['root_class'] = __backup_root_class_140097252813904
                if (__backup_root_type_class_140097340074848 is __marker):
                    del econtext['root_type_class']
                else:
                    econtext['root_type_class'] = __backup_root_type_class_140097340074848
                if (__backup_root_type_140097338343584 is __marker):
                    del econtext['root_type']
                else:
                    econtext['root_type'] = __backup_root_type_140097338343584
                if (__backup_rootIsPortal_140097337741936 is __marker):
                    del econtext['rootIsPortal']
                else:
                    econtext['rootIsPortal'] = __backup_rootIsPortal_140097337741936
                __append('\n        </li>')
            if (__backup_section_140097337632720 is __marker):
                del econtext['section']
            else:
                econtext['section'] = __backup_section_140097337632720
            if (__backup_section_title_140097340072064 is __marker):
                del econtext['section_title']
            else:
                econtext['section_title'] = __backup_section_title_140097340072064
            if (__backup_normalizeString_140097342771296 is __marker):
                del econtext['normalizeString']
            else:
                econtext['normalizeString'] = __backup_normalizeString_140097342771296
            if (__backup_li_class_140097337737760 is __marker):
                del econtext['li_class']
            else:
                econtext['li_class'] = __backup_li_class_140097337737760
            if (__backup_selectedClass_140097342771200 is __marker):
                del econtext['selectedClass']
            else:
                econtext['selectedClass'] = __backup_selectedClass_140097342771200
            __append('\n        ')

            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097252862624
            __attrs_140097252862624 = _static_140097412968080

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252867760
            __default_140097252867760 = _DEFAULT_MARKER

            # <Value 'view/createNavTree' (64:35)> -> __cache_140097252867856
            __token = 2218
            try:
                __zt_tmp = __attrs_140097252862624
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140097252867856 = _static_140097413192464('path', 'view/createNavTree', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

            # <BinOp left=<Value 'view/createNavTree' (64:35)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeefdbd30> -> __condition
            __expression = __cache_140097252867856

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <li ... (0:0)
                # --------------------------------------------------------
                __append('<li>\n            SUBTREE\n        </li>')
            else:
                __content = __cache_140097252867856
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n      </ul>\n    </nav>\n\n  </div>')
            __i18n_domain = __previous_i18n_domain_140097338217072
            if (__backup_root_140097252852640 is __marker):
                del econtext['root']
            else:
                econtext['root'] = __backup_root_140097252852640
            __append('\n\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }