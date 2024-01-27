# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/Products/CMFPlone/browser/templates/plone-addsite.pt'

__tokens = {481: ('${string:${context/absolute_url}/++theme++barceloneta/css/barceloneta.min.css}', 12, 14), 483: ('string:${context/absolute_url}/++theme++barceloneta/css/barceloneta.min.css', 12, 16), 627: ('${string:${context/absolute_url}/++resource++plone-admin-ui.css}', 15, 14), 629: ('string:${context/absolute_url}/++resource++plone-admin-ui.css', 15, 16), 726: ('string:${context/absolute_url}/++resource++jstz-1.0.4.min.js', 16, 30), 831: ('string:${context/absolute_url}/++resource++plone-admin-ui.js', 18, 30), 1117: ('string:${context/absolute_url}/++resource++plone-logo.svg', 28, 35), 1405: ('view/profiles', 35, 25), 1449: (' profiles/bas', 36, 29), 1495: ('e profiles/defau', 37, 30), 1547: ('es profiles/extensi', 38, 32), 1592: ('ced request/advanced|not', 39, 21), 1332: ('string:${context/absolute_url}/@@plone-addsite', 34, 27), 2255: ('request/site_id|nothing', 55, 40), 3261: ('view/browser_language', 78, 49), 3333: (' python:view.grouped_languages(browser_language', 79, 49), 3426: ('grouped_languages', 80, 42), 3491: ('group/label', 81, 46), 3582: ('group/languages', 84, 41), 3645: ("python:lang['langcode']", 85, 46), 3718: (" python:lang['langcode'] == browser_languag", 86, 48), 3801: ("python: lang['label']", 87, 37), 4403: ('view/timezones', 108, 40), 4462: ('tz_list', 109, 42), 4517: ('group', 110, 46), 4576: ('python:tz_list[group]', 111, 51), 4621: ('tz/value', 111, 96), 4662: ('tz/label', 112, 31), 5112: ('advanced', 124, 30), 5742: ('not:advanced', 140, 32), 5897: ('python: len(base_profiles) > 1', 144, 30), 6069: ('base_profiles', 148, 36), 6388: (' info/i', 155, 43), 6336: ('info/id', 154, 41), 6442: ("d python: default_profile==info['id'] and 'checked' or nothi", 156, 44), 6577: ('info/id', 157, 68), 6586: ('${info/title}', 157, 77), 6588: ('info/title', 157, 79), 6660: ('info/description', 158, 52), 6678: ('${info/description}', 158, 70), 6680: ('info/description', 158, 72), 7046: ("python:[p for p in extension_profiles if p.get('selected', None)]", 170, 40), 7143: ('python: extension_profiles or advanced', 171, 30), 7212: ('python: has_selected and not advanced', 172, 29), 7286: ('python: advanced', 173, 34), 7692: ('extension_profiles', 183, 39), 7757: ('info/selected|nothing', 184, 44), 7824: ('python: not selected or advanced', 185, 43), 7943: ('python: advanced', 187, 37), 8090: ('${info/id}', 190, 33), 8092: ('info/id', 190, 35), 8132: ('${info/id}', 191, 30), 8134: ('info/id', 191, 32), 8245: ('info/selected|nothing', 193, 50), 8329: ('${info/id}', 194, 57), 8331: ('info/id', 194, 59), 8342: ('${info/title}', 194, 70), 8344: ('info/title', 194, 72), 8446: ("python: advanced and info['description']", 196, 39), 8511: ('${info/description}', 197, 22), 8513: ('info/description', 197, 24), 8656: ('python: selected and not advanced', 201, 43), 8812: ('${info/id}', 204, 31), 8814: ('info/id', 204, 33)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139867308734736 = {'class': 'btn btn-success mt-3', 'type': 'submit', 'name': 'submit', }
_static_139867308721680 = {'type': 'hidden', 'name': 'form.submitted:boolean', 'value': 'True', }
_static_139867308878256 = {'class': 'col-md-12 mt-3', }
_static_139867308735840 = {'type': 'hidden', 'name': 'extension_ids:list', 'value': '${info/id}', }
_static_139867308727536 = {'class': 'form-text', }
_static_139867308729888 = {'class': 'form-check-label', 'for': '${info/id}', }
_static_139867308883728 = {'type': 'checkbox', 'name': 'extension_ids:list', 'value': '${info/id}', 'id': '${info/id}', 'class': 'form-check-input', 'checked': 'info/selected|nothing', }
_static_139867308879312 = {'class': 'form-check mb-3', }
_static_139867308873360 = {'class': 'lead', }
_static_139867308871344 = {'class': 'col-md-12 mt-3', }
_static_139867308877296 = {'class': 'form-text', }
_static_139867308869520 = {'class': 'form-text', }
_static_139867308694384 = {'class': 'form-check-label', 'for': 'info/id', }
_static_139867308689824 = {'type': 'radio', 'name': 'profile_id:string', 'value': 'profile', 'class': 'form-check-input', 'id': 'info/id', 'checked': "python: default_profile==info['id'] and 'checked' or nothing", }
_static_139867308692080 = {'class': 'form-check mb-3', }
_static_139867308700768 = {'class': 'lead', }
_static_139867308688144 = {'class': 'mb-3', }
_static_139867308692560 = {'class': 'col-md-12', }
_static_139867308688240 = {'type': 'hidden', 'name': 'setup_content:boolean', 'value': 'true', }
_static_139867308691648 = {'class': 'form-text', }
_static_139867308693040 = {'class': 'form-check-label', 'for': 'example-content', }
_static_139867308814352 = {'class': 'form-check-input', 'id': 'example-content', 'type': 'checkbox', 'name': 'setup_content:boolean', 'checked': 'checked', }
_static_139867308804896 = {'class': 'form-check', }
_static_139867308806240 = {'class': 'col-md-12 mb-3', }
_static_139867308811376 = {'class': 'form-text', }
_static_139867308810464 = {'value': 'UTC', }
_static_139867308802208 = {'label': 'group', }
_static_139867308812768 = {'id': 'portal_timezone', 'name': 'portal_timezone', 'class': 'form-select', }
_static_139867308803792 = {'for': 'portal_timezone', 'class': 'form-label', }
_static_139867308809264 = {'class': 'col-md-12 mb-3 tzx', }
_static_139867308813584 = {'class': 'form-text', }
_static_139867308646528 = {'value': 'en', 'selected': "python:lang['langcode'] == browser_language", }
_static_139867308642064 = {'label': 'group/label', }
_static_139867308650272 = {'name': 'default_language', 'class': 'form-select', }
_static_139867308654016 = {'for': 'default_language', 'class': 'form-label', }
_static_139867308641824 = {'class': 'col-md-12 mb-3', }
_static_139867308641200 = {'class': 'form-text', }
_static_139867308649072 = {'type': 'text', 'name': 'title', 'size': '30', 'value': 'Site', 'class': 'form-control', }
_static_139867308640768 = {'for': 'title', 'class': 'form-label', }
_static_139867308416624 = {'class': 'col-md-12 mb-3', }
_static_139867308413552 = {'class': 'form-text', }
_static_139867308418064 = {'type': 'text', 'name': 'site_id', 'size': '20', 'id': 'site_id', 'class': 'form-control', 'value': 'request/site_id|nothing', }
_static_139867308416960 = {'for': 'site_id', 'class': 'form-label', }
_static_139867308412976 = {'class': 'col-md-12 mb-3 mb-3', }
_static_139867308422240 = {'class': 'lead', }
_static_139867308555856 = {'class': 'col-md-12', }
_static_139867308553216 = {'class': 'row', }
_static_139867308548080 = {'action': '#', 'method': 'post', }
_static_139867308552160 = {'src': '/++resource++plone-logo.svg', 'width': '215', 'height': '56', 'alt': 'Plone logo', }
_static_139867308544960 = {'class': 'row', }
_static_139867308545248 = {'class': 'container admin mt-5 mb-5 p-4 ', }
_static_139867308544720 = {'src': 'string:${context/absolute_url}/++resource++plone-admin-ui.js', }
_static_139867308543184 = {'src': 'string:${context/absolute_url}/++resource++jstz-1.0.4.min.js', }
_static_139867308443152 = {'rel': 'stylesheet', 'type': 'text/css', 'href': '${string:${context/absolute_url}/++resource++plone-admin-ui.css}', }
_static_139867356405408 = __C2ZContextWrapper
_static_139867356405696 = __compile_zt_expr
_static_139867308454816 = {'rel': 'stylesheet', 'type': 'text/css', 'href': '${string:${context/absolute_url}/++theme++barceloneta/css/barceloneta.min.css}', }
_static_139867308457120 = {'name': 'viewport', 'content': 'width=device-width, initial-scale=1', }
_static_139867308449104 = {'charset': 'utf-8', }
_static_139867362323344 = {}
_static_139867308453760 = {'xmlns': 'http://www.w3.org/1999/xhtml', 'xml:lang': 'en', 'lang': 'en', }

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
            __append('<!DOCTYPE html>\n')

            # <Static value=<ast.Dict object at 0x7f35653c6f80> name=None at 7f35653c61a0> -> __attrs_139867308451936
            __attrs_139867308451936 = _static_139867308453760
            __previous_i18n_domain_139867308441808 = __i18n_domain
            __i18n_domain = 'plone'

            # <html ... (0:0)
            # --------------------------------------------------------
            __append('<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">\n\n')

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867308455200
            __attrs_139867308455200 = _static_139867362323344

            # <head ... (0:0)
            # --------------------------------------------------------
            __append('<head>\n  ')

            # <Static value=<ast.Dict object at 0x7f35653c5d50> name=None at 7f35653c7a60> -> __attrs_139867308445168
            __attrs_139867308445168 = _static_139867308449104

            # <meta ... (0:0)
            # --------------------------------------------------------
            __append('<meta charset="utf-8" />\n  ')

            # <Static value=<ast.Dict object at 0x7f35653c7ca0> name=None at 7f35653c54e0> -> __attrs_139867308442720
            __attrs_139867308442720 = _static_139867308457120

            # <meta ... (0:0)
            # --------------------------------------------------------
            __append('<meta name="viewport" content="width=device-width, initial-scale=1" />\n  ')

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867308455440
            __attrs_139867308455440 = _static_139867362323344

            # <title ... (0:0)
            # --------------------------------------------------------
            __append('<title>')
            __stream_139867308450736 = []
            __append_139867308450736 = __stream_139867308450736.append
            __append_139867308450736('Create a Plone site')
            __msgid_139867308450736 = __re_whitespace(''.join(__stream_139867308450736)).strip()
            if __msgid_139867308450736:
                __append(translate(__msgid_139867308450736, mapping=None, default=__msgid_139867308450736, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</title>\n  ')

            # <Static value=<ast.Dict object at 0x7f35653c73a0> name=None at 7f35653c7bb0> -> __attrs_139867308457312
            __attrs_139867308457312 = _static_139867308454816

            # <link ... (0:0)
            # --------------------------------------------------------
            __append('<link rel="stylesheet" type="text/css"')

            # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867308448864
            __default_139867308448864 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution '${string:${context/absolute_url}/++theme++barceloneta/css/barceloneta.min.css}' (12:14)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f35653c7460> -> __attr_href
            __token = 481
            __token = 483
            try:
                __zt_tmp = __attrs_139867308457312
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_139867356405696('string', '${context/absolute_url}/++theme++barceloneta/css/barceloneta.min.css', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
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
            __append(' />\n  ')

            # <Static value=<ast.Dict object at 0x7f35653c4610> name=None at 7f35653c7160> -> __attrs_139867308540544
            __attrs_139867308540544 = _static_139867308443152

            # <link ... (0:0)
            # --------------------------------------------------------
            __append('<link rel="stylesheet" type="text/css"')

            # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867308544288
            __default_139867308544288 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution '${string:${context/absolute_url}/++resource++plone-admin-ui.css}' (15:14)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f35653de740> -> __attr_href
            __token = 627
            __token = 629
            try:
                __zt_tmp = __attrs_139867308540544
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_139867356405696('string', '${context/absolute_url}/++resource++plone-admin-ui.css', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
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
            __append(' />\n  ')

            # <Static value=<ast.Dict object at 0x7f35653dccd0> name=None at 7f35653dcaf0> -> __attrs_139867308542272
            __attrs_139867308542272 = _static_139867308543184

            # <script ... (0:0)
            # --------------------------------------------------------
            __append('<script')

            # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867308547456
            __default_139867308547456 = _DEFAULT_MARKER

            # <Substitution 'string:${context/absolute_url}/++resource++jstz-1.0.4.min.js' (16:30)> -> __attr_src
            __token = 726
            try:
                __zt_tmp = __attrs_139867308542272
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_src = _static_139867356405696('string', '${context/absolute_url}/++resource++jstz-1.0.4.min.js', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            __attr_src = __quote(__attr_src, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_src is not None):
                __append((' src="%s"' % __attr_src))
            __append('>\n  </script>\n  ')

            # <Static value=<ast.Dict object at 0x7f35653dd2d0> name=None at 7f35653dd750> -> __attrs_139867308551920
            __attrs_139867308551920 = _static_139867308544720

            # <script ... (0:0)
            # --------------------------------------------------------
            __append('<script')

            # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867308554992
            __default_139867308554992 = _DEFAULT_MARKER

            # <Substitution 'string:${context/absolute_url}/++resource++plone-admin-ui.js' (18:30)> -> __attr_src
            __token = 831
            try:
                __zt_tmp = __attrs_139867308551920
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_src = _static_139867356405696('string', '${context/absolute_url}/++resource++plone-admin-ui.js', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            __attr_src = __quote(__attr_src, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_src is not None):
                __append((' src="%s"' % __attr_src))
            __append('>\n  </script>\n</head>\n\n')

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867308542848
            __attrs_139867308542848 = _static_139867362323344

            # <body ... (0:0)
            # --------------------------------------------------------
            __append('<body>\n\n  ')

            # <Static value=<ast.Dict object at 0x7f35653dd4e0> name=None at 7f35653df820> -> __attrs_139867308544144
            __attrs_139867308544144 = _static_139867308545248

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="container admin mt-5 mb-5 p-4 ">\n    ')

            # <Static value=<ast.Dict object at 0x7f35653dd3c0> name=None at 7f35653dd450> -> __attrs_139867308554368
            __attrs_139867308554368 = _static_139867308544960

            # <header ... (0:0)
            # --------------------------------------------------------
            __append('<header class="row">\n      ')

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867308546976
            __attrs_139867308546976 = _static_139867362323344

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p>')

            # <Static value=<ast.Dict object at 0x7f35653defe0> name=None at 7f35653de860> -> __attrs_139867308554560
            __attrs_139867308554560 = _static_139867308552160

            # <img ... (0:0)
            # --------------------------------------------------------
            __append('<img')

            # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867308550912
            __default_139867308550912 = _DEFAULT_MARKER

            # <Substitution 'string:${context/absolute_url}/++resource++plone-logo.svg' (28:35)> -> __attr_src
            __token = 1117
            try:
                __zt_tmp = __attrs_139867308554560
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_src = _static_139867356405696('string', '${context/absolute_url}/++resource++plone-logo.svg', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            __attr_src = __quote(__attr_src, '"', '&quot;', '/++resource++plone-logo.svg', _DEFAULT_MARKER)
            if (__attr_src is not None):
                __append((' src="%s"' % __attr_src))
            __append(' width="215" height="56"')

            # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867308551968
            __default_139867308551968 = _DEFAULT_MARKER

            # <Translate msgid=None node=<ast.Constant object at 0x7f35653dfe80> at 7f35653dfc70> -> __attr_alt
            __attr_alt = 'Plone logo'
            __attr_alt = translate(__attr_alt, default=__attr_alt, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
            if (__attr_alt is not None):
                __append((' alt="%s"' % __attr_alt))
            __append(' /></p>\n    </header>\n    ')

            # <Static value=<ast.Dict object at 0x7f35653ddff0> name=None at 7f35653dfd60> -> __attrs_139867308550480
            __attrs_139867308550480 = _static_139867308548080
            __backup_profiles_139867338185968 = get('profiles', __marker)

            # <Value 'view/profiles' (35:25)> -> __value
            __token = 1405
            try:
                __zt_tmp = __attrs_139867308550480
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139867356405696('path', 'view/profiles', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            econtext['profiles'] = __value
            __backup_base_profiles_139867339446720 = get('base_profiles', __marker)

            # <Value 'profiles/base' (36:29)> -> __value
            __token = 1449
            try:
                __zt_tmp = __attrs_139867308550480
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139867356405696('path', 'profiles/base', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            econtext['base_profiles'] = __value
            __backup_default_profile_139867338206432 = get('default_profile', __marker)

            # <Value 'profiles/default' (37:30)> -> __value
            __token = 1495
            try:
                __zt_tmp = __attrs_139867308550480
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139867356405696('path', 'profiles/default', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            econtext['default_profile'] = __value
            __backup_extension_profiles_139867338188176 = get('extension_profiles', __marker)

            # <Value 'profiles/extensions' (38:32)> -> __value
            __token = 1547
            try:
                __zt_tmp = __attrs_139867308550480
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139867356405696('path', 'profiles/extensions', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            econtext['extension_profiles'] = __value
            __backup_advanced_139867338206384 = get('advanced', __marker)

            # <Value 'request/advanced|nothing' (39:21)> -> __value
            __token = 1592
            try:
                __zt_tmp = __attrs_139867308550480
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139867356405696('path', 'request/advanced|nothing', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            econtext['advanced'] = __value

            # <form ... (0:0)
            # --------------------------------------------------------
            __append('<form')

            # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867308555808
            __default_139867308555808 = _DEFAULT_MARKER

            # <Substitution 'string:${context/absolute_url}/@@plone-addsite' (34:27)> -> __attr_action
            __token = 1332
            try:
                __zt_tmp = __attrs_139867308550480
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_action = _static_139867356405696('string', '${context/absolute_url}/@@plone-addsite', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            __attr_action = __quote(__attr_action, '"', '&quot;', '#', _DEFAULT_MARKER)
            if (__attr_action is not None):
                __append((' action="%s"' % __attr_action))
            __append(' method="post">\n      ')

            # <Static value=<ast.Dict object at 0x7f35653df400> name=None at 7f35653df1f0> -> __attrs_139867308549232
            __attrs_139867308549232 = _static_139867308553216

            # <article ... (0:0)
            # --------------------------------------------------------
            __append('<article class="row">\n        ')

            # <Static value=<ast.Dict object at 0x7f35653dfe50> name=None at 7f35653deda0> -> __attrs_139867308417200
            __attrs_139867308417200 = _static_139867308555856

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="col-md-12">\n          ')

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867308416768
            __attrs_139867308416768 = _static_139867362323344

            # <h1 ... (0:0)
            # --------------------------------------------------------
            __append('<h1>')

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867308414944
            __attrs_139867308414944 = _static_139867362323344

            # <span ... (0:0)
            # --------------------------------------------------------
            __append('<span>')
            __stream_139867308414848 = []
            __append_139867308414848 = __stream_139867308414848.append
            __append_139867308414848('Create a Plone site')
            __msgid_139867308414848 = __re_whitespace(''.join(__stream_139867308414848)).strip()
            if __msgid_139867308414848:
                __append(translate(__msgid_139867308414848, mapping=None, default=__msgid_139867308414848, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</span></h1>\n          ')

            # <Static value=<ast.Dict object at 0x7f35653bf460> name=None at 7f35653bc1f0> -> __attrs_139867308409088
            __attrs_139867308409088 = _static_139867308422240

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p class="lead">')
            __stream_139867308423008 = []
            __append_139867308423008 = __stream_139867308423008.append
            __append_139867308423008('Adds a new Plone content management system site to the underlying application server.')
            __msgid_139867308423008 = __re_whitespace(''.join(__stream_139867308423008)).strip()
            if __msgid_139867308423008:
                __append(translate(__msgid_139867308423008, mapping=None, default=__msgid_139867308423008, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</p>\n        </div>\n\n          ')

            # <Static value=<ast.Dict object at 0x7f35653bd030> name=None at 7f35653bc460> -> __attrs_139867308419024
            __attrs_139867308419024 = _static_139867308412976

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="col-md-12 mb-3 mb-3">\n            ')

            # <Static value=<ast.Dict object at 0x7f35653bdfc0> name=None at 7f35653bead0> -> __attrs_139867308421808
            __attrs_139867308421808 = _static_139867308416960

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label for="site_id" class="form-label">')
            __stream_139867308424832 = []
            __append_139867308424832 = __stream_139867308424832.append
            __append_139867308424832('\n              Path identifier\n            ')
            __msgid_139867308424832 = __re_whitespace(''.join(__stream_139867308424832)).strip()
            if __msgid_139867308424832:
                __append(translate(__msgid_139867308424832, mapping=None, default=__msgid_139867308424832, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n\n            ')

            # <Static value=<ast.Dict object at 0x7f35653be410> name=None at 7f35653be650> -> __attrs_139867308421712
            __attrs_139867308421712 = _static_139867308418064

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input type="text" name="site_id" size="20" id="site_id" class="form-control"')

            # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867308424112
            __default_139867308424112 = _DEFAULT_MARKER

            # <Substitution 'request/site_id|nothing' (55:40)> -> __attr_value
            __token = 2255
            try:
                __zt_tmp = __attrs_139867308421712
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_value = _static_139867356405696('path', 'request/site_id|nothing', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_value is not None):
                __append((' value="%s"' % __attr_value))
            __append(' />\n\n            ')

            # <Static value=<ast.Dict object at 0x7f35653bd270> name=None at 7f35653bdd50> -> __attrs_139867308416288
            __attrs_139867308416288 = _static_139867308413552

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="form-text">')
            __stream_139867308412880 = []
            __append_139867308412880 = __stream_139867308412880.append
            __append_139867308412880('\n              The ID of the site. No special characters or spaces are allowed. This ends up as part of the URL unless hidden by an upstream web server.\n            ')
            __msgid_139867308412880 = __re_whitespace(''.join(__stream_139867308412880)).strip()
            if __msgid_139867308412880:
                __append(translate(__msgid_139867308412880, mapping=None, default=__msgid_139867308412880, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</div>\n\n          </div>\n\n          ')

            # <Static value=<ast.Dict object at 0x7f35653bde70> name=None at 7f35653bff40> -> __attrs_139867308413312
            __attrs_139867308413312 = _static_139867308416624

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="col-md-12 mb-3">\n            ')

            # <Static value=<ast.Dict object at 0x7f35653f4a00> name=None at 7f35653f6020> -> __attrs_139867308653248
            __attrs_139867308653248 = _static_139867308640768

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label for="title" class="form-label">')
            __stream_139867308649648 = []
            __append_139867308649648 = __stream_139867308649648.append
            __append_139867308649648('Title')
            __msgid_139867308649648 = __re_whitespace(''.join(__stream_139867308649648)).strip()
            if 'label_title':
                __append(translate('label_title', mapping=None, default=__msgid_139867308649648, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n\n            ')

            # <Static value=<ast.Dict object at 0x7f35653f6a70> name=None at 7f35653f6d70> -> __attrs_139867308651136
            __attrs_139867308651136 = _static_139867308649072

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input type="text" name="title" size="30"')

            # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867308638656
            __default_139867308638656 = _DEFAULT_MARKER

            # <Translate msgid='text_default_site_title' node=<ast.Constant object at 0x7f35653f4940> at 7f35653f7250> -> __attr_value
            __attr_value = 'Site'
            __attr_value = translate('text_default_site_title', default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
            if (__attr_value is not None):
                __append((' value="%s"' % __attr_value))
            __append(' class="form-control" />\n\n            ')

            # <Static value=<ast.Dict object at 0x7f35653f4bb0> name=None at 7f35653f7550> -> __attrs_139867308652624
            __attrs_139867308652624 = _static_139867308641200

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="form-text">')
            __stream_139867308651520 = []
            __append_139867308651520 = __stream_139867308651520.append
            __append_139867308651520('\n              A short title for the site. This will be shown as part of the title of the browser window on each page.\n            ')
            __msgid_139867308651520 = __re_whitespace(''.join(__stream_139867308651520)).strip()
            if __msgid_139867308651520:
                __append(translate(__msgid_139867308651520, mapping=None, default=__msgid_139867308651520, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</div>\n\n          </div>\n\n          ')

            # <Static value=<ast.Dict object at 0x7f35653f4e20> name=None at 7f35653f7b80> -> __attrs_139867308649312
            __attrs_139867308649312 = _static_139867308641824

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="col-md-12 mb-3">\n            ')

            # <Static value=<ast.Dict object at 0x7f35653f7dc0> name=None at 7f35653f47c0> -> __attrs_139867308649360
            __attrs_139867308649360 = _static_139867308654016

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label for="default_language" class="form-label">')
            __stream_139867308640048 = []
            __append_139867308640048 = __stream_139867308640048.append
            __append_139867308640048('Language')
            __msgid_139867308640048 = __re_whitespace(''.join(__stream_139867308640048)).strip()
            if __msgid_139867308640048:
                __append(translate(__msgid_139867308640048, mapping=None, default=__msgid_139867308640048, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n\n            ')

            # <Static value=<ast.Dict object at 0x7f35653f6f20> name=None at 7f35653f6860> -> __attrs_139867308650704
            __attrs_139867308650704 = _static_139867308650272
            __backup_browser_language_139867338315072 = get('browser_language', __marker)

            # <Value 'view/browser_language' (78:49)> -> __value
            __token = 3261
            try:
                __zt_tmp = __attrs_139867308650704
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139867356405696('path', 'view/browser_language', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            econtext['browser_language'] = __value
            __backup_grouped_languages_139867338316656 = get('grouped_languages', __marker)

            # <Value 'python:view.grouped_languages(browser_language)' (79:49)> -> __value
            __token = 3333
            try:
                __zt_tmp = __attrs_139867308650704
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139867356405696('python', 'view.grouped_languages(browser_language)', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            econtext['grouped_languages'] = __value

            # <select ... (0:0)
            # --------------------------------------------------------
            __append('<select name="default_language" class="form-select">\n              ')

            # <Static value=<ast.Dict object at 0x7f35653f4f10> name=None at 7f35653f4d60> -> __attrs_139867308643072
            __attrs_139867308643072 = _static_139867308642064
            __backup_group_139867338325824 = get('group', __marker)

            # <Value 'grouped_languages' (80:42)> -> __iterator
            __token = 3426
            try:
                __zt_tmp = __attrs_139867308643072
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_139867356405696('path', 'grouped_languages', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            (__iterator, ____index_139867308639280, ) = getname('repeat')('group', __iterator)
            econtext['group'] = None
            for __item in __iterator:
                econtext['group'] = __item

                # <optgroup ... (0:0)
                # --------------------------------------------------------
                __append('<optgroup')

                # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867308639952
                __default_139867308639952 = _DEFAULT_MARKER

                # <Substitution 'group/label' (81:46)> -> __attr_label
                __token = 3491
                try:
                    __zt_tmp = __attrs_139867308643072
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_label = _static_139867356405696('path', 'group/label', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                __attr_label = __quote(__attr_label, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_label is not None):
                    __append((' label="%s"' % __attr_label))
                __append('>\n\n                ')

                # <Static value=<ast.Dict object at 0x7f35653f6080> name=None at 7f35653f5270> -> __attrs_139867308654400
                __attrs_139867308654400 = _static_139867308646528
                __backup_lang_139867338323760 = get('lang', __marker)

                # <Value 'group/languages' (84:41)> -> __iterator
                __token = 3582
                try:
                    __zt_tmp = __attrs_139867308654400
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_139867356405696('path', 'group/languages', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                (__iterator, ____index_139867308641296, ) = getname('repeat')('lang', __iterator)
                econtext['lang'] = None
                for __item in __iterator:
                    econtext['lang'] = __item

                    # <option ... (0:0)
                    # --------------------------------------------------------
                    __append('<option')

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867308649120
                    __default_139867308649120 = _DEFAULT_MARKER

                    # <Substitution "python:lang['langcode']" (85:46)> -> __attr_value
                    __token = 3645
                    try:
                        __zt_tmp = __attrs_139867308654400
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_139867356405696('python', "lang['langcode']", econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', 'en', _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867308648496
                    __default_139867308648496 = _DEFAULT_MARKER

                    # <Boolean "python:lang['langcode'] == browser_language" (86:48)> -> __attr_selected
                    __token = 3718
                    try:
                        __zt_tmp = __attrs_139867308654400
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_selected = _static_139867356405696('python', "lang['langcode'] == browser_language", econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                    if (__attr_selected is _DEFAULT_MARKER):
                        __attr_selected = None
                    else:
                        if __attr_selected:
                            __attr_selected = 'selected'
                        else:
                            __attr_selected = None
                    if (__attr_selected is not None):
                        __append((' selected="%s"' % __attr_selected))
                    __append('>')

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867308646960
                    __default_139867308646960 = _DEFAULT_MARKER

                    # <Value "python: lang['label']" (87:37)> -> __cache_139867308640144
                    __token = 3801
                    try:
                        __zt_tmp = __attrs_139867308654400
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139867308640144 = _static_139867356405696('python', " lang['label']", econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))

                    # <BinOp left=<Value "python: lang['label']" (87:37)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f3568756860> at 7f35653f5690> -> __condition
                    __expression = __cache_139867308640144

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n                  English\n                ')
                    else:
                        __content = __cache_139867308640144
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</option>')
                    ____index_139867308641296 -= 1
                    if (____index_139867308641296 > 0):
                        __append('\n                ')
                if (__backup_lang_139867338323760 is __marker):
                    del econtext['lang']
                else:
                    econtext['lang'] = __backup_lang_139867338323760
                __append('\n\n              </optgroup>')
                ____index_139867308639280 -= 1
                if (____index_139867308639280 > 0):
                    __append('\n              ')
            if (__backup_group_139867338325824 is __marker):
                del econtext['group']
            else:
                econtext['group'] = __backup_group_139867338325824
            __append('\n            </select>')
            if (__backup_grouped_languages_139867338316656 is __marker):
                del econtext['grouped_languages']
            else:
                econtext['grouped_languages'] = __backup_grouped_languages_139867338316656
            if (__backup_browser_language_139867338315072 is __marker):
                del econtext['browser_language']
            else:
                econtext['browser_language'] = __backup_browser_language_139867338315072
            __append('\n\n            ')

            # <Static value=<ast.Dict object at 0x7f356541ed10> name=None at 7f35653f6c50> -> __attrs_139867308812672
            __attrs_139867308812672 = _static_139867308813584

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="form-text">')
            __stream_139867308642400 = []
            __append_139867308642400 = __stream_139867308642400.append
            __append_139867308642400('\n              The main language of the site.\n            ')
            __msgid_139867308642400 = __re_whitespace(''.join(__stream_139867308642400)).strip()
            if __msgid_139867308642400:
                __append(translate(__msgid_139867308642400, mapping=None, default=__msgid_139867308642400, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</div>\n\n          </div>\n\n          ')

            # <Static value=<ast.Dict object at 0x7f356541dc30> name=None at 7f356541d570> -> __attrs_139867308802976
            __attrs_139867308802976 = _static_139867308809264

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="col-md-12 mb-3 tzx">\n            ')

            # <Static value=<ast.Dict object at 0x7f356541c6d0> name=None at 7f356541e260> -> __attrs_139867308807632
            __attrs_139867308807632 = _static_139867308803792

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label for="portal_timezone" class="form-label">')
            __stream_139867308804752 = []
            __append_139867308804752 = __stream_139867308804752.append
            __append_139867308804752('\n              Default timezone\n            ')
            __msgid_139867308804752 = __re_whitespace(''.join(__stream_139867308804752)).strip()
            if __msgid_139867308804752:
                __append(translate(__msgid_139867308804752, mapping=None, default=__msgid_139867308804752, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n\n            ')

            # <Static value=<ast.Dict object at 0x7f356541e9e0> name=None at 7f356541ed70> -> __attrs_139867308808208
            __attrs_139867308808208 = _static_139867308812768
            __backup_tz_list_139867338317760 = get('tz_list', __marker)

            # <Value 'view/timezones' (108:40)> -> __value
            __token = 4403
            try:
                __zt_tmp = __attrs_139867308808208
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139867356405696('path', 'view/timezones', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            econtext['tz_list'] = __value

            # <select ... (0:0)
            # --------------------------------------------------------
            __append('<select id="portal_timezone" name="portal_timezone" class="form-select">\n              ')

            # <Static value=<ast.Dict object at 0x7f356541c0a0> name=None at 7f356541f760> -> __attrs_139867308813008
            __attrs_139867308813008 = _static_139867308802208
            __backup_group_139867338310656 = get('group', __marker)

            # <Value 'tz_list' (109:42)> -> __iterator
            __token = 4462
            try:
                __zt_tmp = __attrs_139867308813008
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_139867356405696('path', 'tz_list', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            (__iterator, ____index_139867308807776, ) = getname('repeat')('group', __iterator)
            econtext['group'] = None
            for __item in __iterator:
                econtext['group'] = __item

                # <optgroup ... (0:0)
                # --------------------------------------------------------
                __append('<optgroup')

                # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867308816512
                __default_139867308816512 = _DEFAULT_MARKER

                # <Substitution 'group' (110:46)> -> __attr_label
                __token = 4517
                try:
                    __zt_tmp = __attrs_139867308813008
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_label = _static_139867356405696('path', 'group', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                __attr_label = __quote(__attr_label, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_label is not None):
                    __append((' label="%s"' % __attr_label))
                __append('>\n                ')

                # <Static value=<ast.Dict object at 0x7f356541e0e0> name=None at 7f356541e650> -> __attrs_139867308817424
                __attrs_139867308817424 = _static_139867308810464
                __backup_tz_139867338316512 = get('tz', __marker)

                # <Value 'python:tz_list[group]' (111:51)> -> __iterator
                __token = 4576
                try:
                    __zt_tmp = __attrs_139867308817424
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_139867356405696('python', 'tz_list[group]', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                (__iterator, ____index_139867308810704, ) = getname('repeat')('tz', __iterator)
                econtext['tz'] = None
                for __item in __iterator:
                    econtext['tz'] = __item

                    # <option ... (0:0)
                    # --------------------------------------------------------
                    __append('<option')

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867308808592
                    __default_139867308808592 = _DEFAULT_MARKER

                    # <Substitution 'tz/value' (111:96)> -> __attr_value
                    __token = 4621
                    try:
                        __zt_tmp = __attrs_139867308817424
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_139867356405696('path', 'tz/value', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', 'UTC', _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append('>')

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867308812720
                    __default_139867308812720 = _DEFAULT_MARKER

                    # <Value 'tz/label' (112:31)> -> __cache_139867308805712
                    __token = 4662
                    try:
                        __zt_tmp = __attrs_139867308817424
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139867308805712 = _static_139867356405696('path', 'tz/label', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))

                    # <BinOp left=<Value 'tz/label' (112:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f3568756860> at 7f356541eb60> -> __condition
                    __expression = __cache_139867308805712

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n                  UTC\n                ')
                    else:
                        __content = __cache_139867308805712
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</option>')
                    ____index_139867308810704 -= 1
                    if (____index_139867308810704 > 0):
                        __append('\n                ')
                if (__backup_tz_139867338316512 is __marker):
                    del econtext['tz']
                else:
                    econtext['tz'] = __backup_tz_139867338316512
                __append('\n              </optgroup>')
                ____index_139867308807776 -= 1
                if (____index_139867308807776 > 0):
                    __append('\n              ')
            if (__backup_group_139867338310656 is __marker):
                del econtext['group']
            else:
                econtext['group'] = __backup_group_139867338310656
            __append('\n            </select>')
            if (__backup_tz_list_139867338317760 is __marker):
                del econtext['tz_list']
            else:
                econtext['tz_list'] = __backup_tz_list_139867338317760
            __append('\n            ')

            # <Static value=<ast.Dict object at 0x7f356541e470> name=None at 7f356541f2e0> -> __attrs_139867308817856
            __attrs_139867308817856 = _static_139867308811376

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="form-text">')
            __stream_139867308816368 = []
            __append_139867308816368 = __stream_139867308816368.append
            __append_139867308816368('\n              The default timezone setting of the portal.\n              Users will be able to set their own timezone, if available timezones are defined in the date and time settings.\n            ')
            __msgid_139867308816368 = __re_whitespace(''.join(__stream_139867308816368)).strip()
            if __msgid_139867308816368:
                __append(translate(__msgid_139867308816368, mapping=None, default=__msgid_139867308816368, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</div>\n          </div>\n\n          ')

            # <Static value=<ast.Dict object at 0x7f356541d060> name=None at 7f356541f040> -> __attrs_139867308815168
            __attrs_139867308815168 = _static_139867308806240

            # <Value 'advanced' (124:30)> -> __condition
            __token = 5112
            try:
                __zt_tmp = __attrs_139867308815168
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_139867356405696('path', 'advanced', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="col-md-12 mb-3">\n            ')

                # <Static value=<ast.Dict object at 0x7f356541cb20> name=None at 7f356541ec80> -> __attrs_139867308811280
                __attrs_139867308811280 = _static_139867308804896

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="form-check">\n              ')

                # <Static value=<ast.Dict object at 0x7f356541f010> name=None at 7f356541f850> -> __attrs_139867308700960
                __attrs_139867308700960 = _static_139867308814352

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input class="form-check-input" id="example-content" type="checkbox" name="setup_content:boolean" checked="checked" />\n              ')

                # <Static value=<ast.Dict object at 0x7f3565401630> name=None at 7f35654009d0> -> __attrs_139867308700480
                __attrs_139867308700480 = _static_139867308693040

                # <label ... (0:0)
                # --------------------------------------------------------
                __append('<label class="form-check-label" for="example-content">')
                __stream_139867308695920 = []
                __append_139867308695920 = __stream_139867308695920.append
                __append_139867308695920('Example content')
                __msgid_139867308695920 = __re_whitespace(''.join(__stream_139867308695920)).strip()
                if __msgid_139867308695920:
                    __append(translate(__msgid_139867308695920, mapping=None, default=__msgid_139867308695920, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</label>\n              ')

                # <Static value=<ast.Dict object at 0x7f35654010c0> name=None at 7f3565400ee0> -> __attrs_139867308702304
                __attrs_139867308702304 = _static_139867308691648

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="form-text">')
                __stream_139867308703024 = []
                __append_139867308703024 = __stream_139867308703024.append
                __append_139867308703024('\n                Should the default example content be added to the site?\n              ')
                __msgid_139867308703024 = __re_whitespace(''.join(__stream_139867308703024)).strip()
                if __msgid_139867308703024:
                    __append(translate(__msgid_139867308703024, mapping=None, default=__msgid_139867308703024, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</div>\n            </div>\n          </div>')
            __append('\n\n          ')

            # <Static value=<ast.Dict object at 0x7f3565400370> name=None at 7f35654011b0> -> __attrs_139867308696640
            __attrs_139867308696640 = _static_139867308688240

            # <Value 'not:advanced' (140:32)> -> __condition
            __token = 5742
            try:
                __zt_tmp = __attrs_139867308696640
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_139867356405696('not', 'advanced', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            if __condition:

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="hidden" name="setup_content:boolean" value="true" />')
            __append('\n\n          ')

            # <Static value=<ast.Dict object at 0x7f3565401450> name=None at 7f3565402650> -> __attrs_139867308699088
            __attrs_139867308699088 = _static_139867308692560

            # <Value 'python: len(base_profiles) > 1' (144:30)> -> __condition
            __token = 5897
            try:
                __zt_tmp = __attrs_139867308699088
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_139867356405696('python', ' len(base_profiles) > 1', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="col-md-12">\n            ')

                # <Static value=<ast.Dict object at 0x7f3565400310> name=None at 7f3565402ef0> -> __attrs_139867308698416
                __attrs_139867308698416 = _static_139867308688144

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="mb-3">\n              ')

                # <Static value=<ast.Dict object at 0x7f3565403460> name=None at 7f35654033d0> -> __attrs_139867308698704
                __attrs_139867308698704 = _static_139867308700768

                # <p ... (0:0)
                # --------------------------------------------------------
                __append('<p class="lead">')
                __stream_139867308701008 = []
                __append_139867308701008 = __stream_139867308701008.append
                __append_139867308701008('Base configuration')
                __msgid_139867308701008 = __re_whitespace(''.join(__stream_139867308701008)).strip()
                if __msgid_139867308701008:
                    __append(translate(__msgid_139867308701008, mapping=None, default=__msgid_139867308701008, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</p>\n\n              ')

                # <Static value=<ast.Dict object at 0x7f3565401270> name=None at 7f3565400130> -> __attrs_139867308702592
                __attrs_139867308702592 = _static_139867308692080
                __backup_info_139867337290224 = get('info', __marker)

                # <Value 'base_profiles' (148:36)> -> __iterator
                __token = 6069
                try:
                    __zt_tmp = __attrs_139867308702592
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_139867356405696('path', 'base_profiles', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                (__iterator, ____index_139867308695152, ) = getname('repeat')('info', __iterator)
                econtext['info'] = None
                for __item in __iterator:
                    econtext['info'] = __item

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="form-check mb-3">\n                ')

                    # <Static value=<ast.Dict object at 0x7f35654009a0> name=None at 7f3565403160> -> __attrs_139867308698656
                    __attrs_139867308698656 = _static_139867308689824

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input type="radio" name="profile_id:string"')

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867308695104
                    __default_139867308695104 = _DEFAULT_MARKER

                    # <Substitution 'info/id' (155:43)> -> __attr_value
                    __token = 6388
                    try:
                        __zt_tmp = __attrs_139867308698656
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_139867356405696('path', 'info/id', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', 'profile', _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append(' class="form-check-input"')

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867308690064
                    __default_139867308690064 = _DEFAULT_MARKER

                    # <Substitution 'info/id' (154:41)> -> __attr_id
                    __token = 6336
                    try:
                        __zt_tmp = __attrs_139867308698656
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_id = _static_139867356405696('path', 'info/id', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_id is not None):
                        __append((' id="%s"' % __attr_id))

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867308697408
                    __default_139867308697408 = _DEFAULT_MARKER

                    # <Boolean "python: default_profile==info['id'] and 'checked' or nothing" (156:44)> -> __attr_checked
                    __token = 6442
                    try:
                        __zt_tmp = __attrs_139867308698656
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_checked = _static_139867356405696('python', " default_profile==info['id'] and 'checked' or nothing", econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                    if (__attr_checked is _DEFAULT_MARKER):
                        __attr_checked = None
                    else:
                        if __attr_checked:
                            __attr_checked = 'checked'
                        else:
                            __attr_checked = None
                    if (__attr_checked is not None):
                        __append((' checked="%s"' % __attr_checked))
                    __append(' />\n                ')

                    # <Static value=<ast.Dict object at 0x7f3565401b70> name=None at 7f35654029e0> -> __attrs_139867308878304
                    __attrs_139867308878304 = _static_139867308694384

                    # <label ... (0:0)
                    # --------------------------------------------------------
                    __append('<label class="form-check-label"')

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867308881904
                    __default_139867308881904 = _DEFAULT_MARKER

                    # <Substitution 'info/id' (157:68)> -> __attr_for
                    __token = 6577
                    try:
                        __zt_tmp = __attrs_139867308878304
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_for = _static_139867356405696('path', 'info/id', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                    __attr_for = __quote(__attr_for, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_for is not None):
                        __append((' for="%s"' % __attr_for))
                    __append('>')

                    # <Interpolation value=<Substitution '${info/title}' (157:77)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f356542fbb0> -> __content_139867442113136
                    __token = 6586
                    __token = 6588
                    try:
                        __zt_tmp = __attrs_139867308878304
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __content_139867442113136 = _static_139867356405696('path', 'info/title', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
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
                    __append('</label>\n                ')

                    # <Static value=<ast.Dict object at 0x7f356542c790> name=None at 7f356542d3f0> -> __attrs_139867308876576
                    __attrs_139867308876576 = _static_139867308869520

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="form-text">')

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867308878928
                    __default_139867308878928 = _DEFAULT_MARKER

                    # <Value 'info/description' (158:52)> -> __cache_139867308876000
                    __token = 6660
                    try:
                        __zt_tmp = __attrs_139867308876576
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_139867308876000 = _static_139867356405696('path', 'info/description', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))

                    # <BinOp left=<Value 'info/description' (158:52)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f3568756860> at 7f356542efb0> -> __condition
                    __expression = __cache_139867308876000

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <Interpolation value=<Substitution '${info/description}' (158:70)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f356542cbb0> -> __content_139867442113136
                        __token = 6678
                        __token = 6680
                        try:
                            __zt_tmp = __attrs_139867308876576
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __content_139867442113136 = _static_139867356405696('path', 'info/description', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
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
                    else:
                        __content = __cache_139867308876000
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</div>\n              </div>')
                    ____index_139867308695152 -= 1
                    if (____index_139867308695152 > 0):
                        __append('\n              ')
                if (__backup_info_139867337290224 is __marker):
                    del econtext['info']
                else:
                    econtext['info'] = __backup_info_139867337290224
                __append('\n\n              ')

                # <Static value=<ast.Dict object at 0x7f356542e5f0> name=None at 7f356542f220> -> __attrs_139867308875664
                __attrs_139867308875664 = _static_139867308877296

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="form-text">')
                __stream_139867308875376 = []
                __append_139867308875376 = __stream_139867308875376.append
                __append_139867308875376("\n                You normally don't need to change anything here unless you have specific reasons and know what you are doing.\n              ")
                __msgid_139867308875376 = __re_whitespace(''.join(__stream_139867308875376)).strip()
                if __msgid_139867308875376:
                    __append(translate(__msgid_139867308875376, mapping=None, default=__msgid_139867308875376, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</div>\n\n            </div>\n          </div>')
            __append('\n\n\n          ')

            # <Static value=<ast.Dict object at 0x7f356542ceb0> name=None at 7f356542fac0> -> __attrs_139867308867984
            __attrs_139867308867984 = _static_139867308871344
            __backup_has_selected_139867338324864 = get('has_selected', __marker)

            # <Value "python:[p for p in extension_profiles if p.get('selected', None)]" (170:40)> -> __value
            __token = 7046
            try:
                __zt_tmp = __attrs_139867308867984
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139867356405696('python', "[p for p in extension_profiles if p.get('selected', None)]", econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            econtext['has_selected'] = __value

            # <Value 'python: extension_profiles or advanced' (171:30)> -> __condition
            __token = 7143
            try:
                __zt_tmp = __attrs_139867308867984
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_139867356405696('python', ' extension_profiles or advanced', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            if __condition:

                # <Negate value=<Value 'python: has_selected and not advanced' (172:29)> at 7f356542c760> -> __cache_139867308869472

                # <Value 'python: has_selected and not advanced' (172:29)> -> __cache_139867308869472
                __token = 7212
                try:
                    __zt_tmp = __attrs_139867308867984
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_139867308869472 = _static_139867356405696('python', ' has_selected and not advanced', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                __cache_139867308869472 = not __cache_139867308869472
                __condition = __cache_139867308869472
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="col-md-12 mt-3">')
                __append('\n            ')

                # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867308872928
                __attrs_139867308872928 = _static_139867362323344

                # <Value 'python: advanced' (173:34)> -> __condition
                __token = 7286
                try:
                    __zt_tmp = __attrs_139867308872928
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_139867356405696('python', ' advanced', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                if __condition:
                    __append('\n              ')

                    # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867308880944
                    __attrs_139867308880944 = _static_139867362323344

                    # <h2 ... (0:0)
                    # --------------------------------------------------------
                    __append('<h2>')
                    __stream_139867308871776 = []
                    __append_139867308871776 = __stream_139867308871776.append
                    __append_139867308871776('Add-ons')
                    __msgid_139867308871776 = __re_whitespace(''.join(__stream_139867308871776)).strip()
                    if __msgid_139867308871776:
                        __append(translate(__msgid_139867308871776, mapping=None, default=__msgid_139867308871776, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</h2>\n\n              ')

                    # <Static value=<ast.Dict object at 0x7f356542d690> name=None at 7f356542d960> -> __attrs_139867308877008
                    __attrs_139867308877008 = _static_139867308873360

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="lead" >')
                    __stream_139867308871632 = []
                    __append_139867308871632 = __stream_139867308871632.append
                    __append_139867308871632('\n                Select any add-ons you want to activate immediately.\n                You can also activate add-ons after the site has been created using the Add-ons control panel.\n              ')
                    __msgid_139867308871632 = __re_whitespace(''.join(__stream_139867308871632)).strip()
                    if __msgid_139867308871632:
                        __append(translate(__msgid_139867308871632, mapping=None, default=__msgid_139867308871632, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</div>\n            ')
                __append('\n\n            ')

                # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867308868464
                __attrs_139867308868464 = _static_139867362323344
                __backup_info_139867338316800 = get('info', __marker)

                # <Value 'extension_profiles' (183:39)> -> __iterator
                __token = 7692
                try:
                    __zt_tmp = __attrs_139867308868464
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_139867356405696('path', 'extension_profiles', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                (__iterator, ____index_139867308871584, ) = getname('repeat')('info', __iterator)
                econtext['info'] = None
                for __item in __iterator:
                    econtext['info'] = __item
                    __append('\n              ')

                    # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867308876336
                    __attrs_139867308876336 = _static_139867362323344
                    __backup_selected_139867340155792 = get('selected', __marker)

                    # <Value 'info/selected|nothing' (184:44)> -> __value
                    __token = 7757
                    try:
                        __zt_tmp = __attrs_139867308876336
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_139867356405696('path', 'info/selected|nothing', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                    econtext['selected'] = __value
                    __append('\n                ')

                    # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867308873696
                    __attrs_139867308873696 = _static_139867362323344

                    # <Value 'python: not selected or advanced' (185:43)> -> __condition
                    __token = 7824
                    try:
                        __zt_tmp = __attrs_139867308873696
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_139867356405696('python', ' not selected or advanced', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                    if __condition:
                        __append('\n                  ')

                        # <Static value=<ast.Dict object at 0x7f356542edd0> name=None at 7f356542cf70> -> __attrs_139867308873120
                        __attrs_139867308873120 = _static_139867308879312

                        # <Value 'python: advanced' (187:37)> -> __condition
                        __token = 7943
                        try:
                            __zt_tmp = __attrs_139867308873120
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_139867356405696('python', ' advanced', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                        if __condition:

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append('<div class="form-check mb-3">\n                    ')

                            # <Static value=<ast.Dict object at 0x7f356542ff10> name=None at 7f356542fe50> -> __attrs_139867308733968
                            __attrs_139867308733968 = _static_139867308883728

                            # <input ... (0:0)
                            # --------------------------------------------------------
                            __append('<input type="checkbox" name="extension_ids:list"')

                            # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867308728352
                            __default_139867308728352 = _DEFAULT_MARKER

                            # <Interpolation value=<Substitution '${info/id}' (190:33)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f356540b550> -> __attr_value
                            __token = 8090
                            __token = 8092
                            try:
                                __zt_tmp = __attrs_139867308733968
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_value = _static_139867356405696('path', 'info/id', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                            __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                            __attr_value = __attr_value
                            if (__attr_value is None):
                                pass
                            else:
                                if (__attr_value is _DEFAULT_MARKER):
                                    __attr_value = None
                                else:
                                    __tt = type(__attr_value)
                                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                                        __attr_value = str(__attr_value)
                                    else:
                                        if (__tt is bytes):
                                            __attr_value = decode(__attr_value)
                                        else:
                                            if (__tt is not str):
                                                try:
                                                    __attr_value = __attr_value.__html__
                                                except get('AttributeError', AttributeError):
                                                    __converted = convert(__attr_value)
                                                    __attr_value = (str(__attr_value) if (__attr_value is __converted) else __converted)
                                                else:
                                                    __attr_value = __attr_value()
                            if (__attr_value is not None):
                                __append((' value="%s"' % __attr_value))

                            # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867308720624
                            __default_139867308720624 = _DEFAULT_MARKER

                            # <Interpolation value=<Substitution '${info/id}' (191:30)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f3565408820> -> __attr_id
                            __token = 8132
                            __token = 8134
                            try:
                                __zt_tmp = __attrs_139867308733968
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_id = _static_139867356405696('path', 'info/id', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                            __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                            __attr_id = __attr_id
                            if (__attr_id is None):
                                pass
                            else:
                                if (__attr_id is _DEFAULT_MARKER):
                                    __attr_id = None
                                else:
                                    __tt = type(__attr_id)
                                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                                        __attr_id = str(__attr_id)
                                    else:
                                        if (__tt is bytes):
                                            __attr_id = decode(__attr_id)
                                        else:
                                            if (__tt is not str):
                                                try:
                                                    __attr_id = __attr_id.__html__
                                                except get('AttributeError', AttributeError):
                                                    __converted = convert(__attr_id)
                                                    __attr_id = (str(__attr_id) if (__attr_id is __converted) else __converted)
                                                else:
                                                    __attr_id = __attr_id()
                            if (__attr_id is not None):
                                __append((' id="%s"' % __attr_id))
                            __append(' class="form-check-input"')

                            # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867308731328
                            __default_139867308731328 = _DEFAULT_MARKER

                            # <Boolean 'info/selected|nothing' (193:50)> -> __attr_checked
                            __token = 8245
                            try:
                                __zt_tmp = __attrs_139867308733968
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_checked = _static_139867356405696('path', 'info/selected|nothing', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                            if (__attr_checked is _DEFAULT_MARKER):
                                __attr_checked = None
                            else:
                                if __attr_checked:
                                    __attr_checked = 'checked'
                                else:
                                    __attr_checked = None
                            if (__attr_checked is not None):
                                __append((' checked="%s"' % __attr_checked))
                            __append(' />\n                    ')

                            # <Static value=<ast.Dict object at 0x7f356540a620> name=None at 7f356540b040> -> __attrs_139867308731520
                            __attrs_139867308731520 = _static_139867308729888

                            # <label ... (0:0)
                            # --------------------------------------------------------
                            __append('<label class="form-check-label"')

                            # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867308732672
                            __default_139867308732672 = _DEFAULT_MARKER

                            # <Interpolation value=<Substitution '${info/id}' (194:57)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f356540a290> -> __attr_for
                            __token = 8329
                            __token = 8331
                            try:
                                __zt_tmp = __attrs_139867308731520
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_for = _static_139867356405696('path', 'info/id', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                            __attr_for = __quote(__attr_for, '"', '&quot;', None, _DEFAULT_MARKER)
                            __attr_for = __attr_for
                            if (__attr_for is None):
                                pass
                            else:
                                if (__attr_for is _DEFAULT_MARKER):
                                    __attr_for = None
                                else:
                                    __tt = type(__attr_for)
                                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                                        __attr_for = str(__attr_for)
                                    else:
                                        if (__tt is bytes):
                                            __attr_for = decode(__attr_for)
                                        else:
                                            if (__tt is not str):
                                                try:
                                                    __attr_for = __attr_for.__html__
                                                except get('AttributeError', AttributeError):
                                                    __converted = convert(__attr_for)
                                                    __attr_for = (str(__attr_for) if (__attr_for is __converted) else __converted)
                                                else:
                                                    __attr_for = __attr_for()
                            if (__attr_for is not None):
                                __append((' for="%s"' % __attr_for))
                            __append(' >')

                            # <Interpolation value=<Substitution '${info/title}' (194:70)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f356540a650> -> __content_139867442113136
                            __token = 8342
                            __token = 8344
                            try:
                                __zt_tmp = __attrs_139867308731520
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __content_139867442113136 = _static_139867356405696('path', 'info/title', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
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
                            __append('</label>\n                    ')

                            # <Static value=<ast.Dict object at 0x7f3565409cf0> name=None at 7f356540b130> -> __attrs_139867308728640
                            __attrs_139867308728640 = _static_139867308727536

                            # <Value "python: advanced and info['description']" (196:39)> -> __condition
                            __token = 8446
                            try:
                                __zt_tmp = __attrs_139867308728640
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_139867356405696('python', " advanced and info['description']", econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                            if __condition:

                                # <div ... (0:0)
                                # --------------------------------------------------------
                                __append('<div class="form-text">')

                                # <Interpolation value=<Substitution '\n                      ${info/description}\n                    ' (196:81)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f3565408dc0> -> __content_139867442113136
                                __token = 8511
                                __token = 8513
                                try:
                                    __zt_tmp = __attrs_139867308728640
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __content_139867442113136 = _static_139867356405696('path', 'info/description', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                                __content_139867442113136 = __quote(__content_139867442113136, '\x00', '&#0;', None, None)
                                __content_139867442113136 = ('%s%s%s' % ('\n                      ', (__content_139867442113136 if (__content_139867442113136 is not None) else ''), '\n                    ', ))
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
                                __append('</div>')
                            __append('\n                  </div>')
                        __append('\n                ')
                    __append('\n                ')

                    # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867308721344
                    __attrs_139867308721344 = _static_139867362323344

                    # <Value 'python: selected and not advanced' (201:43)> -> __condition
                    __token = 8656
                    try:
                        __zt_tmp = __attrs_139867308721344
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_139867356405696('python', ' selected and not advanced', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                    if __condition:
                        __append('\n                  ')

                        # <Static value=<ast.Dict object at 0x7f356540bd60> name=None at 7f356540ad10> -> __attrs_139867308722736
                        __attrs_139867308722736 = _static_139867308735840

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input type="hidden" name="extension_ids:list"')

                        # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867308728448
                        __default_139867308728448 = _DEFAULT_MARKER

                        # <Interpolation value=<Substitution '${info/id}' (204:31)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f3565408910> -> __attr_value
                        __token = 8812
                        __token = 8814
                        try:
                            __zt_tmp = __attrs_139867308722736
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_value = _static_139867356405696('path', 'info/id', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                        __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                        __attr_value = __attr_value
                        if (__attr_value is None):
                            pass
                        else:
                            if (__attr_value is _DEFAULT_MARKER):
                                __attr_value = None
                            else:
                                __tt = type(__attr_value)
                                if ((__tt is int) or (__tt is float) or (__tt is int)):
                                    __attr_value = str(__attr_value)
                                else:
                                    if (__tt is bytes):
                                        __attr_value = decode(__attr_value)
                                    else:
                                        if (__tt is not str):
                                            try:
                                                __attr_value = __attr_value.__html__
                                            except get('AttributeError', AttributeError):
                                                __converted = convert(__attr_value)
                                                __attr_value = (str(__attr_value) if (__attr_value is __converted) else __converted)
                                            else:
                                                __attr_value = __attr_value()
                        if (__attr_value is not None):
                            __append((' value="%s"' % __attr_value))
                        __append(' />\n                ')
                    __append('\n              ')
                    if (__backup_selected_139867340155792 is __marker):
                        del econtext['selected']
                    else:
                        econtext['selected'] = __backup_selected_139867340155792
                    __append('\n            ')
                    ____index_139867308871584 -= 1
                    if (____index_139867308871584 > 0):
                        __append('')
                if (__backup_info_139867338316800 is __marker):
                    del econtext['info']
                else:
                    econtext['info'] = __backup_info_139867338316800
                __append('\n          ')
                __condition = __cache_139867308869472
                if __condition:
                    __append('</div>')
            if (__backup_has_selected_139867338324864 is __marker):
                del econtext['has_selected']
            else:
                econtext['has_selected'] = __backup_has_selected_139867338324864
            __append('\n          ')

            # <Static value=<ast.Dict object at 0x7f356542e9b0> name=None at 7f356542f5e0> -> __attrs_139867308881088
            __attrs_139867308881088 = _static_139867308878256

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="col-md-12 mt-3">\n            ')

            # <Static value=<ast.Dict object at 0x7f3565408610> name=None at 7f3565409720> -> __attrs_139867308727824
            __attrs_139867308727824 = _static_139867308721680

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input type="hidden" name="form.submitted:boolean" value="True" />\n            ')

            # <Static value=<ast.Dict object at 0x7f356540b910> name=None at 7f356540a110> -> __attrs_139867308727728
            __attrs_139867308727728 = _static_139867308734736

            # <button ... (0:0)
            # --------------------------------------------------------
            __append('<button class="btn btn-success mt-3" type="submit" name="submit">')
            __stream_139867308723360 = []
            __append_139867308723360 = __stream_139867308723360.append
            __append_139867308723360('Create Plone Site')
            __msgid_139867308723360 = __re_whitespace(''.join(__stream_139867308723360)).strip()
            if __msgid_139867308723360:
                __append(translate(__msgid_139867308723360, mapping=None, default=__msgid_139867308723360, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</button>\n          </div>\n      </article>\n    </form>')
            if (__backup_advanced_139867338206384 is __marker):
                del econtext['advanced']
            else:
                econtext['advanced'] = __backup_advanced_139867338206384
            if (__backup_extension_profiles_139867338188176 is __marker):
                del econtext['extension_profiles']
            else:
                econtext['extension_profiles'] = __backup_extension_profiles_139867338188176
            if (__backup_default_profile_139867338206432 is __marker):
                del econtext['default_profile']
            else:
                econtext['default_profile'] = __backup_default_profile_139867338206432
            if (__backup_base_profiles_139867339446720 is __marker):
                del econtext['base_profiles']
            else:
                econtext['base_profiles'] = __backup_base_profiles_139867339446720
            if (__backup_profiles_139867338185968 is __marker):
                del econtext['profiles']
            else:
                econtext['profiles'] = __backup_profiles_139867338185968
            __append('\n  </div>\n</body>\n\n</html>')
            __i18n_domain = __previous_i18n_domain_139867308441808
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }