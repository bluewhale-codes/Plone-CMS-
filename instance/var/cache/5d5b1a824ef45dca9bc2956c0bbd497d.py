# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/Products/CMFPlone/controlpanel/browser/prefsmaintemplate.pt'

__tokens = {256: ("python:request.set('disable_border',1)", 6, 43), 345: (" python:modules['Products.CMFCore.utils'].getToolByName(here, 'portal_controlpanel'", 7, 49), 485: ("e python:request.set('disable_plone.leftcolumn', ", 8, 54), 591: ("wo python:request.set('disable_plone.rightcolumn'", 9, 53), 1074: ("python:modules['Products.CMFCore.utils'].getToolByName(here, 'portal_controlpanel')", 21, 46), 1198: (" python:controlPanel.getGroups('site'", 22, 39), 1278: ('l controlPanel/site_u', 23, 40), 1345: ('rl request/', 24, 42), 1496: ('string:$portal_url/@@overview-controlpanel', 27, 49), 1573: ("nav-link ${python:'active' if overview_url in current_url else ''}", 28, 32), 1584: ("python:'active' if overview_url in current_url else ''", 28, 43), 1667: ('${overview_url}', 28, 126), 1669: ('overview_url', 28, 128), 1792: ('groups', 30, 49), 1850: ("python:controlPanel.enumConfiglets(group=group['id'])", 31, 49), 1949: (" python:'active' if bool([c for c in configlets if current_url.startswith(c['url'])]) else 'inactive", 32, 44), 2093: ('python:configlets and controlPanel.maySeeSomeConfiglets', 33, 41), 2237: ('nav-link dropdown-toggle ${active}', 35, 34), 2264: ('active', 35, 61), 2344: ('${group/title}', 35, 141), 2346: ('group/title', 35, 143), 2474: ('configlets', 37, 58), 2534: ('configlet/visible', 38, 47), 2608: ("python:'http' in configlet['icon']", 39, 54), 2738: ('${configlet/url}', 41, 39), 2740: ('configlet/url', 41, 41), 2809: ('icon_url', 42, 52), 2938: ('configlet/icon', 44, 56), 3009: (' configlet/titl', 45, 55), 3143: ('not: icon_url', 47, 57), 3223: ("python:icons.tag(configlet['icon'] or 'plone-controlpanel', tag_alt=configlet['title'])", 48, 65), 3347: ('${configlet/title}', 49, 32), 3349: ('configlet/title', 49, 34), 3694: ('nothing', 59, 82), 898: ('context/@@main_template/macros/content', 17, 42), 898: ('context/@@main_template/macros/content', 17, 42), 85: ('context/@@main_template/macros/master', 2, 30), 85: ('context/@@main_template/macros/master', 2, 30)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from collections import deque as _deque

_static_140097338271120 = {'src': '', 'alt': '', 'class': 'icon', }
_static_140097338262432 = {'class': 'dropdown-item', 'href': '${configlet/url}', }
_static_140097338275824 = {'class': 'dropdown-menu', }
_static_140097338262480 = {'class': 'nav-link dropdown-toggle ${active}', 'data-bs-toggle': 'dropdown', 'href': '#', 'role': 'button', 'aria-expanded': 'false', }
_static_140097338261760 = {'class': 'nav-item dropdown', }
_static_140097338212016 = {'class': "nav-link ${python:'active' if overview_url in current_url else ''}", 'aria-current': 'page', 'href': '${overview_url}', }
_static_140097338203952 = {'class': 'nav-item', }
_static_140097338203472 = {'class': 'nav nav-tabs', }
_static_140097252216352 = {'class': 'mb-3', }
_static_140097252223168 = 'content'
_static_140097413192176 = __C2ZContextWrapper
_static_140097413192464 = __compile_zt_expr
_static_140097252217552 = 'master'
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
            __slot_prefs_configlet_wrapper = econtext['__slot_prefs_configlet_wrapper'].pop()
        except:
            __slot_prefs_configlet_wrapper = None

        try:
            __slot_prefs_configlet_main = econtext['__slot_prefs_configlet_main'].pop()
        except:
            __slot_prefs_configlet_main = None

        try:
            __slot_prefs_configlet_content = econtext['__slot_prefs_configlet_content'].pop()
        except:
            __slot_prefs_configlet_content = None

        try:
            __slot_top_slot = econtext['__slot_top_slot'].pop()
        except:
            __slot_top_slot = None

        try:
            getname = econtext.get_name
            get = econtext.get

            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097252215536
            __attrs_140097252215536 = _static_140097412968080
            __previous_i18n_domain_140097252219088 = __i18n_domain
            __i18n_domain = 'plone'
            __append('\n  ')

            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097252215008
            __attrs_140097252215008 = _static_140097412968080
            __backup_macroname_140097248673088 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f6aeef3d2d0> name=None at 7f6aeef3d1b0> -> __value
            __value = _static_140097252217552
            econtext['macroname'] = __value

            def __fill_top_slot(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097252227824
                __attrs_140097252227824 = _static_140097412968080
                __append('\n        ')
                if (__slot_top_slot is None):

                    # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097252222448
                    __attrs_140097252222448 = _static_140097412968080
                    __append('\n            ')

                    # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097252217072
                    __attrs_140097252217072 = _static_140097412968080
                    __backup_dummy_140097245760960 = get('dummy', __marker)

                    # <Value "python:request.set('disable_border',1)" (6:43)> -> __value
                    __token = 256
                    try:
                        __zt_tmp = __attrs_140097252217072
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140097413192464('python', "request.set('disable_border',1)", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    econtext['dummy'] = __value
                    __backup_controlPanel_140097338463648 = get('controlPanel', __marker)

                    # <Value "python:modules['Products.CMFCore.utils'].getToolByName(here, 'portal_controlpanel')" (7:49)> -> __value
                    __token = 345
                    try:
                        __zt_tmp = __attrs_140097252217072
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140097413192464('python', "modules['Products.CMFCore.utils'].getToolByName(here, 'portal_controlpanel')", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    econtext['controlPanel'] = __value
                    __backup_disable_column_one_140097248368224 = get('disable_column_one', __marker)

                    # <Value "python:request.set('disable_plone.leftcolumn', 1)" (8:54)> -> __value
                    __token = 485
                    try:
                        __zt_tmp = __attrs_140097252217072
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140097413192464('python', "request.set('disable_plone.leftcolumn', 1)", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    econtext['disable_column_one'] = __value
                    __backup_disable_column_two_140097252584912 = get('disable_column_two', __marker)

                    # <Value "python:request.set('disable_plone.rightcolumn',1)" (9:53)> -> __value
                    __token = 591
                    try:
                        __zt_tmp = __attrs_140097252217072
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140097413192464('python', "request.set('disable_plone.rightcolumn',1)", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    econtext['disable_column_two'] = __value
                    if (__backup_disable_column_two_140097252584912 is __marker):
                        del econtext['disable_column_two']
                    else:
                        econtext['disable_column_two'] = __backup_disable_column_two_140097252584912
                    if (__backup_disable_column_one_140097248368224 is __marker):
                        del econtext['disable_column_one']
                    else:
                        econtext['disable_column_one'] = __backup_disable_column_one_140097248368224
                    if (__backup_controlPanel_140097338463648 is __marker):
                        del econtext['controlPanel']
                    else:
                        econtext['controlPanel'] = __backup_controlPanel_140097338463648
                    if (__backup_dummy_140097245760960 is __marker):
                        del econtext['dummy']
                    else:
                        econtext['dummy'] = __backup_dummy_140097245760960
                    __append('\n        ')
                else:
                    __slot_top_slot(__stream, econtext.copy(), rcontext)
                __append('\n    ')
            _slots = econtext['__slot_top_slot'] = _deque((__fill_top_slot, ))

            def __fill_content(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097252216448
                __attrs_140097252216448 = _static_140097412968080
                __append('\n        ')
                if (__slot_prefs_configlet_wrapper is None):

                    # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097252225568
                    __attrs_140097252225568 = _static_140097412968080
                    __append('\n          ')
                    if (__slot_prefs_configlet_content is None):

                        # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097252214192
                        __attrs_140097252214192 = _static_140097412968080
                        __append('\n\n            ')

                        # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097252215728
                        __attrs_140097252215728 = _static_140097412968080
                        __backup_macroname_140097247593856 = get('macroname', __marker)

                        # <Static value=<ast.Constant object at 0x7f6aeef3e8c0> name=None at 7f6aeef3d270> -> __value
                        __value = _static_140097252223168
                        econtext['macroname'] = __value

                        def __fill_main(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                            getname = econtext.get_name
                            get = econtext.get

                            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097252228496
                            __attrs_140097252228496 = _static_140097412968080
                            __append('\n\n                ')

                            # <Static value=<ast.Dict object at 0x7f6aeef3ce20> name=None at 7f6aeef3dc30> -> __attrs_140097338196560
                            __attrs_140097338196560 = _static_140097252216352
                            __backup_controlPanel_140097337743424 = get('controlPanel', __marker)

                            # <Value "python:modules['Products.CMFCore.utils'].getToolByName(here, 'portal_controlpanel')" (21:46)> -> __value
                            __token = 1074
                            try:
                                __zt_tmp = __attrs_140097338196560
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_140097413192464('python', "modules['Products.CMFCore.utils'].getToolByName(here, 'portal_controlpanel')", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                            econtext['controlPanel'] = __value
                            __backup_groups_140097337746448 = get('groups', __marker)

                            # <Value "python:controlPanel.getGroups('site')" (22:39)> -> __value
                            __token = 1198
                            try:
                                __zt_tmp = __attrs_140097338196560
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_140097413192464('python', "controlPanel.getGroups('site')", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                            econtext['groups'] = __value
                            __backup_site_url_140097338204288 = get('site_url', __marker)

                            # <Value 'controlPanel/site_url' (23:40)> -> __value
                            __token = 1278
                            try:
                                __zt_tmp = __attrs_140097338196560
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_140097413192464('path', 'controlPanel/site_url', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                            econtext['site_url'] = __value
                            __backup_current_url_140097252057648 = get('current_url', __marker)

                            # <Value 'request/URL' (24:42)> -> __value
                            __token = 1345
                            try:
                                __zt_tmp = __attrs_140097338196560
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_140097413192464('path', 'request/URL', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                            econtext['current_url'] = __value

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append('<div class="mb-3">\n                  ')

                            # <Static value=<ast.Dict object at 0x7f6af413dd50> name=None at 7f6af413ec80> -> __attrs_140097338204816
                            __attrs_140097338204816 = _static_140097338203472

                            # <ul ... (0:0)
                            # --------------------------------------------------------
                            __append('<ul class="nav nav-tabs">\n                    ')

                            # <Static value=<ast.Dict object at 0x7f6af413df30> name=None at 7f6af413f7f0> -> __attrs_140097338208656
                            __attrs_140097338208656 = _static_140097338203952
                            __backup_overview_url_140097248374656 = get('overview_url', __marker)

                            # <Value 'string:$portal_url/@@overview-controlpanel' (27:49)> -> __value
                            __token = 1496
                            try:
                                __zt_tmp = __attrs_140097338208656
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_140097413192464('string', '$portal_url/@@overview-controlpanel', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                            econtext['overview_url'] = __value

                            # <li ... (0:0)
                            # --------------------------------------------------------
                            __append('<li class="nav-item">\n                      ')

                            # <Static value=<ast.Dict object at 0x7f6af413feb0> name=None at 7f6af413ee60> -> __attrs_140097338261712
                            __attrs_140097338261712 = _static_140097338212016

                            # <a ... (0:0)
                            # --------------------------------------------------------
                            __append('<a')

                            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338211776
                            __default_140097338211776 = _DEFAULT_MARKER

                            # <Interpolation value=<Substitution "nav-link ${python:'active' if overview_url in current_url else ''}" (28:32)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f6af413d450> -> __attr_class
                            __token = 1573
                            __token = 1584
                            try:
                                __zt_tmp = __attrs_140097338261712
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_class = _static_140097413192464('python', "'active' if overview_url in current_url else ''", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                            __attr_class = ('%s%s' % ('nav-link ', (__attr_class if (__attr_class is not None) else ''), ))
                            if (__attr_class is None):
                                pass
                            else:
                                if (__attr_class is _DEFAULT_MARKER):
                                    __attr_class = None
                                else:
                                    __tt = type(__attr_class)
                                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                                        __attr_class = str(__attr_class)
                                    else:
                                        if (__tt is bytes):
                                            __attr_class = decode(__attr_class)
                                        else:
                                            if (__tt is not str):
                                                try:
                                                    __attr_class = __attr_class.__html__
                                                except get('AttributeError', AttributeError):
                                                    __converted = convert(__attr_class)
                                                    __attr_class = (str(__attr_class) if (__attr_class is __converted) else __converted)
                                                else:
                                                    __attr_class = __attr_class()
                            if (__attr_class is not None):
                                __append((' class="%s"' % __attr_class))
                            __append(' aria-current="page"')

                            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338212208
                            __default_140097338212208 = _DEFAULT_MARKER

                            # <Interpolation value=<Substitution '${overview_url}' (28:126)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f6af413cdf0> -> __attr_href
                            __token = 1667
                            __token = 1669
                            try:
                                __zt_tmp = __attrs_140097338261712
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_href = _static_140097413192464('path', 'overview_url', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
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
                            __append('>')
                            __stream_140097338210624 = []
                            __append_140097338210624 = __stream_140097338210624.append
                            __append_140097338210624('Site Setup')
                            __msgid_140097338210624 = __re_whitespace(''.join(__stream_140097338210624)).strip()
                            if __msgid_140097338210624:
                                __append(translate(__msgid_140097338210624, mapping=None, default=__msgid_140097338210624, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                            __append('</a>\n                    </li>')
                            if (__backup_overview_url_140097248374656 is __marker):
                                del econtext['overview_url']
                            else:
                                econtext['overview_url'] = __backup_overview_url_140097248374656
                            __append('\n                    ')

                            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097338265792
                            __attrs_140097338265792 = _static_140097412968080
                            __backup_group_140097252580448 = get('group', __marker)

                            # <Value 'groups' (30:49)> -> __iterator
                            __token = 1792
                            try:
                                __zt_tmp = __attrs_140097338265792
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __iterator = _static_140097413192464('path', 'groups', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                            (__iterator, ____index_140097338271312, ) = getname('repeat')('group', __iterator)
                            econtext['group'] = None
                            for __item in __iterator:
                                econtext['group'] = __item
                                __append('\n                      ')

                                # <Static value=<ast.Dict object at 0x7f6af414c100> name=None at 7f6af414f370> -> __attrs_140097338268816
                                __attrs_140097338268816 = _static_140097338261760
                                __backup_configlets_140097248365296 = get('configlets', __marker)

                                # <Value "python:controlPanel.enumConfiglets(group=group['id'])" (31:49)> -> __value
                                __token = 1850
                                try:
                                    __zt_tmp = __attrs_140097338268816
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __value = _static_140097413192464('python', "controlPanel.enumConfiglets(group=group['id'])", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                                econtext['configlets'] = __value
                                __backup_active_140097252665344 = get('active', __marker)

                                # <Value "python:'active' if bool([c for c in configlets if current_url.startswith(c['url'])]) else 'inactive'" (32:44)> -> __value
                                __token = 1949
                                try:
                                    __zt_tmp = __attrs_140097338268816
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __value = _static_140097413192464('python', "'active' if bool([c for c in configlets if current_url.startswith(c['url'])]) else 'inactive'", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                                econtext['active'] = __value

                                # <Value 'python:configlets and controlPanel.maySeeSomeConfiglets' (33:41)> -> __condition
                                __token = 2093
                                try:
                                    __zt_tmp = __attrs_140097338268816
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __condition = _static_140097413192464('python', 'configlets and controlPanel.maySeeSomeConfiglets', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                                if __condition:

                                    # <li ... (0:0)
                                    # --------------------------------------------------------
                                    __append('<li class="nav-item dropdown">\n                        ')

                                    # <Static value=<ast.Dict object at 0x7f6af414c3d0> name=None at 7f6af414fa90> -> __attrs_140097338270160
                                    __attrs_140097338270160 = _static_140097338262480

                                    # <a ... (0:0)
                                    # --------------------------------------------------------
                                    __append('<a')

                                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338271360
                                    __default_140097338271360 = _DEFAULT_MARKER

                                    # <Interpolation value=<Substitution 'nav-link dropdown-toggle ${active}' (35:34)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f6af414fa00> -> __attr_class
                                    __token = 2237
                                    __token = 2264
                                    try:
                                        __zt_tmp = __attrs_140097338270160
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_class = _static_140097413192464('path', 'active', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                                    __attr_class = ('%s%s' % ('nav-link dropdown-toggle ', (__attr_class if (__attr_class is not None) else ''), ))
                                    if (__attr_class is None):
                                        pass
                                    else:
                                        if (__attr_class is _DEFAULT_MARKER):
                                            __attr_class = None
                                        else:
                                            __tt = type(__attr_class)
                                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                                __attr_class = str(__attr_class)
                                            else:
                                                if (__tt is bytes):
                                                    __attr_class = decode(__attr_class)
                                                else:
                                                    if (__tt is not str):
                                                        try:
                                                            __attr_class = __attr_class.__html__
                                                        except get('AttributeError', AttributeError):
                                                            __converted = convert(__attr_class)
                                                            __attr_class = (str(__attr_class) if (__attr_class is __converted) else __converted)
                                                        else:
                                                            __attr_class = __attr_class()
                                    if (__attr_class is not None):
                                        __append((' class="%s"' % __attr_class))
                                    __append(' data-bs-toggle="dropdown" href="#" role="button" aria-expanded="false">')

                                    # <Interpolation value=<Substitution '${group/title}' (35:141)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f6af414ed70> -> __content_140097497049648
                                    __token = 2344
                                    __token = 2346
                                    try:
                                        __zt_tmp = __attrs_140097338270160
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __content_140097497049648 = _static_140097413192464('path', 'group/title', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                                    __content_140097497049648 = __quote(__content_140097497049648, '\x00', '&#0;', None, None)
                                    __content_140097497049648 = __content_140097497049648
                                    if (__content_140097497049648 is None):
                                        pass
                                    else:
                                        if (__content_140097497049648 is None):
                                            __content_140097497049648 = None
                                        else:
                                            __tt = type(__content_140097497049648)
                                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                                __content_140097497049648 = str(__content_140097497049648)
                                            else:
                                                if (__tt is bytes):
                                                    __content_140097497049648 = decode(__content_140097497049648)
                                                else:
                                                    if (__tt is not str):
                                                        try:
                                                            __content_140097497049648 = __content_140097497049648.__html__
                                                        except get('AttributeError', AttributeError):
                                                            __converted = convert(__content_140097497049648)
                                                            __content_140097497049648 = (str(__content_140097497049648) if (__content_140097497049648 is __converted) else __converted)
                                                        else:
                                                            __content_140097497049648 = __content_140097497049648()
                                    if (__content_140097497049648 is not None):
                                        __append(__content_140097497049648)
                                    __append('</a>\n                          ')

                                    # <Static value=<ast.Dict object at 0x7f6af414f7f0> name=None at 7f6af414c2e0> -> __attrs_140097338273520
                                    __attrs_140097338273520 = _static_140097338275824

                                    # <ul ... (0:0)
                                    # --------------------------------------------------------
                                    __append('<ul class="dropdown-menu">\n                          ')

                                    # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097338264928
                                    __attrs_140097338264928 = _static_140097412968080
                                    __backup_configlet_140097248364864 = get('configlet', __marker)

                                    # <Value 'configlets' (37:58)> -> __iterator
                                    __token = 2474
                                    try:
                                        __zt_tmp = __attrs_140097338264928
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __iterator = _static_140097413192464('path', 'configlets', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                                    (__iterator, ____index_140097338264592, ) = getname('repeat')('configlet', __iterator)
                                    econtext['configlet'] = None
                                    for __item in __iterator:
                                        econtext['configlet'] = __item
                                        __append('\n                            ')

                                        # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097338267376
                                        __attrs_140097338267376 = _static_140097412968080

                                        # <Value 'configlet/visible' (38:47)> -> __condition
                                        __token = 2534
                                        try:
                                            __zt_tmp = __attrs_140097338267376
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __condition = _static_140097413192464('path', 'configlet/visible', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                                        if __condition:

                                            # <li ... (0:0)
                                            # --------------------------------------------------------
                                            __append('<li>\n                              ')

                                            # <Static value=<ast.Dict object at 0x7f6af414c3a0> name=None at 7f6af414d660> -> __attrs_140097338262576
                                            __attrs_140097338262576 = _static_140097338262432
                                            __backup_icon_url_140097245762544 = get('icon_url', __marker)

                                            # <Value "python:'http' in configlet['icon']" (39:54)> -> __value
                                            __token = 2608
                                            try:
                                                __zt_tmp = __attrs_140097338262576
                                            except get('NameError', NameError):
                                                __zt_tmp = None

                                            __value = _static_140097413192464('python', "'http' in configlet['icon']", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                                            econtext['icon_url'] = __value

                                            # <a ... (0:0)
                                            # --------------------------------------------------------
                                            __append('<a class="dropdown-item"')

                                            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338274240
                                            __default_140097338274240 = _DEFAULT_MARKER

                                            # <Interpolation value=<Substitution '${configlet/url}' (41:39)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f6af414d330> -> __attr_href
                                            __token = 2738
                                            __token = 2740
                                            try:
                                                __zt_tmp = __attrs_140097338262576
                                            except get('NameError', NameError):
                                                __zt_tmp = None

                                            __attr_href = _static_140097413192464('path', 'configlet/url', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
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
                                            __append('>\n                                ')

                                            # <Static value=<ast.Dict object at 0x7f6af414e590> name=None at 7f6af414ea70> -> __attrs_140097338227056
                                            __attrs_140097338227056 = _static_140097338271120

                                            # <Value 'icon_url' (42:52)> -> __condition
                                            __token = 2809
                                            try:
                                                __zt_tmp = __attrs_140097338227056
                                            except get('NameError', NameError):
                                                __zt_tmp = None

                                            __condition = _static_140097413192464('path', 'icon_url', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                                            if __condition:

                                                # <img ... (0:0)
                                                # --------------------------------------------------------
                                                __append('<img')

                                                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338222832
                                                __default_140097338222832 = _DEFAULT_MARKER

                                                # <Substitution 'configlet/icon' (44:56)> -> __attr_src
                                                __token = 2938
                                                try:
                                                    __zt_tmp = __attrs_140097338227056
                                                except get('NameError', NameError):
                                                    __zt_tmp = None

                                                __attr_src = _static_140097413192464('path', 'configlet/icon', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                                                __attr_src = __quote(__attr_src, '"', '&quot;', '', _DEFAULT_MARKER)
                                                if (__attr_src is not None):
                                                    __append((' src="%s"' % __attr_src))

                                                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338218176
                                                __default_140097338218176 = _DEFAULT_MARKER

                                                # <Translate msgid=None node=<Substitution 'configlet/title' (45:55)> at 7f6af41405b0> -> __attr_alt

                                                # <Substitution 'configlet/title' (45:55)> -> __attr_alt
                                                __token = 3009
                                                try:
                                                    __zt_tmp = __attrs_140097338227056
                                                except get('NameError', NameError):
                                                    __zt_tmp = None

                                                __attr_alt = _static_140097413192464('path', 'configlet/title', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                                                __attr_alt = __quote(__attr_alt, '"', '&quot;', '', _DEFAULT_MARKER)
                                                __attr_alt = translate(__attr_alt, default=__attr_alt, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                                                if (__attr_alt is not None):
                                                    __append((' alt="%s"' % __attr_alt))
                                                __append(' class="icon">')
                                            __append('\n                                ')

                                            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097338227104
                                            __attrs_140097338227104 = _static_140097412968080

                                            # <Value 'not: icon_url' (47:57)> -> __condition
                                            __token = 3143
                                            try:
                                                __zt_tmp = __attrs_140097338227104
                                            except get('NameError', NameError):
                                                __zt_tmp = None

                                            __condition = _static_140097413192464('not', ' icon_url', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                                            if __condition:

                                                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338213952
                                                __default_140097338213952 = _DEFAULT_MARKER

                                                # <Value "python:icons.tag(configlet['icon'] or 'plone-controlpanel', tag_alt=configlet['title'])" (48:65)> -> __cache_140097338214480
                                                __token = 3223
                                                try:
                                                    __zt_tmp = __attrs_140097338227104
                                                except get('NameError', NameError):
                                                    __zt_tmp = None

                                                __cache_140097338214480 = _static_140097413192464('python', "icons.tag(configlet['icon'] or 'plone-controlpanel', tag_alt=configlet['title'])", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                                                # <BinOp left=<Value "python:icons.tag(configlet['icon'] or 'plone-controlpanel', tag_alt=configlet['title'])" (48:65)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6af4142f20> -> __condition
                                                __expression = __cache_140097338214480

                                                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                                                __value = _DEFAULT_MARKER
                                                __condition = (__expression is __value)
                                                if __condition:
                                                    pass
                                                else:
                                                    __content = __cache_140097338214480
                                                    __content = __convert(__content)
                                                    if (__content is not None):
                                                        __append(__content)

                                            # <Interpolation value=<Substitution '\n                                ${configlet/title}\n                              ' (48:156)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f6af4140040> -> __content_140097497049648
                                            __token = 3347
                                            __token = 3349
                                            try:
                                                __zt_tmp = __attrs_140097338262576
                                            except get('NameError', NameError):
                                                __zt_tmp = None

                                            __content_140097497049648 = _static_140097413192464('path', 'configlet/title', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                                            __content_140097497049648 = __quote(__content_140097497049648, '\x00', '&#0;', None, None)
                                            __content_140097497049648 = ('%s%s%s' % ('\n                                ', (__content_140097497049648 if (__content_140097497049648 is not None) else ''), '\n                              ', ))
                                            if (__content_140097497049648 is None):
                                                pass
                                            else:
                                                if (__content_140097497049648 is None):
                                                    __content_140097497049648 = None
                                                else:
                                                    __tt = type(__content_140097497049648)
                                                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                                                        __content_140097497049648 = str(__content_140097497049648)
                                                    else:
                                                        if (__tt is bytes):
                                                            __content_140097497049648 = decode(__content_140097497049648)
                                                        else:
                                                            if (__tt is not str):
                                                                try:
                                                                    __content_140097497049648 = __content_140097497049648.__html__
                                                                except get('AttributeError', AttributeError):
                                                                    __converted = convert(__content_140097497049648)
                                                                    __content_140097497049648 = (str(__content_140097497049648) if (__content_140097497049648 is __converted) else __converted)
                                                                else:
                                                                    __content_140097497049648 = __content_140097497049648()
                                            if (__content_140097497049648 is not None):
                                                __append(__content_140097497049648)
                                            __append('</a>')
                                            if (__backup_icon_url_140097245762544 is __marker):
                                                del econtext['icon_url']
                                            else:
                                                econtext['icon_url'] = __backup_icon_url_140097245762544
                                            __append('\n                            </li>')
                                        __append('\n                          ')
                                        ____index_140097338264592 -= 1
                                        if (____index_140097338264592 > 0):
                                            __append('')
                                    if (__backup_configlet_140097248364864 is __marker):
                                        del econtext['configlet']
                                    else:
                                        econtext['configlet'] = __backup_configlet_140097248364864
                                    __append('\n                        </ul>\n                      </li>')
                                if (__backup_active_140097252665344 is __marker):
                                    del econtext['active']
                                else:
                                    econtext['active'] = __backup_active_140097252665344
                                if (__backup_configlets_140097248365296 is __marker):
                                    del econtext['configlets']
                                else:
                                    econtext['configlets'] = __backup_configlets_140097248365296
                                __append('\n                    ')
                                ____index_140097338271312 -= 1
                                if (____index_140097338271312 > 0):
                                    __append('')
                            if (__backup_group_140097252580448 is __marker):
                                del econtext['group']
                            else:
                                econtext['group'] = __backup_group_140097252580448
                            __append('\n                  </ul>\n                </div>')
                            if (__backup_current_url_140097252057648 is __marker):
                                del econtext['current_url']
                            else:
                                econtext['current_url'] = __backup_current_url_140097252057648
                            if (__backup_site_url_140097338204288 is __marker):
                                del econtext['site_url']
                            else:
                                econtext['site_url'] = __backup_site_url_140097338204288
                            if (__backup_groups_140097337746448 is __marker):
                                del econtext['groups']
                            else:
                                econtext['groups'] = __backup_groups_140097337746448
                            if (__backup_controlPanel_140097337743424 is __marker):
                                del econtext['controlPanel']
                            else:
                                econtext['controlPanel'] = __backup_controlPanel_140097337743424
                            __append('\n\n                ')
                            if (__slot_prefs_configlet_main is None):

                                # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097338263824
                                __attrs_140097338263824 = _static_140097412968080

                                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338272224
                                __default_140097338272224 = _DEFAULT_MARKER

                                # <Value 'nothing' (59:82)> -> __cache_140097338271600
                                __token = 3694
                                try:
                                    __zt_tmp = __attrs_140097338263824
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __cache_140097338271600 = _static_140097413192464('path', 'nothing', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                                # <BinOp left=<Value 'nothing' (59:82)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6af414d420> -> __condition
                                __expression = __cache_140097338271600

                                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                                __value = _DEFAULT_MARKER
                                __condition = (__expression is __value)
                                if __condition:
                                    __append('\n                  Page body text\n                ')
                                else:
                                    __content = __cache_140097338271600
                                    __content = __quote(__content, None, '\xad', None, None)
                                    if (__content is not None):
                                        __append(__content)
                            else:
                                __slot_prefs_configlet_main(__stream, econtext.copy(), rcontext)
                            __append('\n\n              ')
                        _slots = econtext['__slot_main'] = _deque((__fill_main, ))

                        # <Value 'context/@@main_template/macros/content' (17:42)> -> __macro
                        __token = 898
                        try:
                            __zt_tmp = __attrs_140097252215728
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __macro = _static_140097413192464('path', 'context/@@main_template/macros/content', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __token = 898
                        __m = __macro.include
                        __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                        econtext.update(rcontext)
                        if (__backup_macroname_140097247593856 is __marker):
                            del econtext['macroname']
                        else:
                            econtext['macroname'] = __backup_macroname_140097247593856
                        __append('\n\n          ')
                    else:
                        __slot_prefs_configlet_content(__stream, econtext.copy(), rcontext)
                    __append('\n        ')
                else:
                    __slot_prefs_configlet_wrapper(__stream, econtext.copy(), rcontext)
                __append('\n    ')
            _slots = econtext['__slot_content'] = _deque((__fill_content, ))

            # <Value 'context/@@main_template/macros/master' (2:30)> -> __macro
            __token = 85
            try:
                __zt_tmp = __attrs_140097252215008
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140097413192464('path', 'context/@@main_template/macros/master', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __token = 85
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140097248673088 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140097248673088
            __append('\n')
            __i18n_domain = __previous_i18n_domain_140097252219088
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

    return {'render_master': render_master, 'render': render, }