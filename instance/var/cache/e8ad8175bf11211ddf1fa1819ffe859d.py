# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/Products/CMFPlone/browser/templates/plone-overview.pt'

__tokens = {581: ('${string:${context/absolute_url}/++theme++barceloneta/css/barceloneta.min.css}', 16, 14), 583: ('string:${context/absolute_url}/++theme++barceloneta/css/barceloneta.min.css', 16, 16), 727: ('${string:${context/absolute_url}/++resource++plone-admin-ui.css}', 19, 14), 729: ('string:${context/absolute_url}/++resource++plone-admin-ui.css', 19, 16), 830: ('view/sites', 23, 24), 864: (' python:len(sites) > ', 24, 22), 1087: ('string:${context/absolute_url}/++resource++plone-logo.svg', 29, 36), 1755: ('sites', 44, 28), 1802: ('sites', 45, 39), 1852: ('python: view.outdated(site)', 46, 42), 1910: ("mb-3 ${python: 'p-3 alert alert-warning' if outdated else ''}", 47, 28), 1917: ("python: 'p-3 alert alert-warning' if outdated else ''", 47, 35), 2012: ('outdated', 48, 38), 2285: ('site/absolute_url', 50, 45), 2166: ("btn btn-primary ${python:'btn-lg' if not many and not outdated  else ''}", 49, 60), 2184: ("python:'btn-lg' if not many and not outdated  else ''", 49, 78), 2450: ('not: many', 53, 44), 2555: ('many', 54, 45), 2561: ('${python:site.title}', 54, 51), 2563: ('python:site.title', 54, 53), 2589: ('(${python:"/".join(site.getPhysicalPath())})', 54, 79), 2592: ('python:"/".join(site.getPhysicalPath())', 54, 82), 2851: ('outdated', 59, 43), 2912: ('python:view.upgrade_url(site)', 60, 51), 2990: ('not:view/can_manage', 61, 46), 3128: ('python:view.upgrade_url(site, can_manage=True)', 63, 54), 3620: ('sites', 74, 30), 3770: ('not:sites', 78, 30), 4017: ("python: '' if not sites else len(sites) + 1", 84, 44), 4100: (' string:${context/absolute_url}/@@plone-addsit', 85, 38), 4177: ('${action}', 86, 28), 4179: ('action', 86, 30), 4248: ('Plone${site_number}', 87, 59), 4255: ('site_number', 87, 66), 4341: ("btn btn-${python:'success' if sites else 'primary'}", 89, 31), 4351: ("python:'success' if sites else 'primary'", 89, 41), 4582: ('view/has_volto', 93, 35), 4624: ('${action}?site_id=Plone${site_number}&amp;classic=1', 94, 26), 4626: ('action', 94, 28), 4649: ('site_number', 94, 51), 4837: ('${action}?site_id=Plone${site_number}&amp;advanced=1', 98, 26), 4839: ('action', 98, 28), 4862: ('site_number', 98, 51), 6194: ('string:${context/absolute_url}/manage_main', 126, 29)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139867308423056 = {'href': '#', 'title': 'Go to the ZMI', }
_static_139867308422000 = {'class': 'row', }
_static_139867308417440 = {'href': 'https://6.docs.plone.org/', 'title': 'Plone 6 developer documentation', }
_static_139867309145920 = {'class': 'btn btn-secondary', 'href': '${action}?site_id=Plone${site_number}&amp;advanced=1', }
_static_139867309144192 = {'class': 'btn btn-info', 'href': '${action}?site_id=Plone${site_number}&amp;classic=1', }
_static_139867309145584 = {'type': 'submit', 'class': "btn btn-${python:'success' if sites else 'primary'}", }
_static_139867309141984 = {'type': 'hidden', 'name': 'site_id', 'value': 'Plone${site_number}', }
_static_139867309135744 = {'id': 'add-plone-site', 'method': 'get', 'action': '${action}', }
_static_139867309130272 = {'class': 'alert alert-warning p-1', }
_static_139867338808992 = {'class': 'col-md-12', }
_static_139867338813696 = {'type': 'submit', 'class': 'btn btn-warning me-3', }
_static_139867338808080 = {'type': 'hidden', 'name': 'came_from', 'value': 'python:view.upgrade_url(site, can_manage=True)', }
_static_139867338809376 = {'action': '', 'style': 'display: inline;', 'method': 'get', }
_static_139867338805728 = {'href': '#', 'id': 'go-to-site-link', 'class': "btn btn-primary ${python:'btn-lg' if not many and not outdated  else ''}", 'title': 'Go to your instance', }
_static_139867338812304 = {'class': "mb-3 ${python: 'p-3 alert alert-warning' if outdated else ''}", }
_static_139867316484032 = {'class': 'col-md-12 mb-4', }
_static_139867316480960 = {'class': 'row mb-5', }
_static_139867316472512 = {'href': 'http://plone.org', 'title': 'Plone Community Home', }
_static_139867316472128 = {'class': 'lead', }
_static_139867316475056 = {'src': '/++resource++plone-logo.svg', 'width': '215', 'height': '56', 'alt': 'Plone logo', }
_static_139867316478608 = {'class': 'row', }
_static_139867316480336 = {'class': 'container admin mt-5 mb-5 p-4', }
_static_139867316485424 = {'rel': 'stylesheet', 'type': 'text/css', 'href': '${string:${context/absolute_url}/++resource++plone-admin-ui.css}', }
_static_139867356405408 = __C2ZContextWrapper
_static_139867356405696 = __compile_zt_expr
_static_139867344823264 = {'rel': 'stylesheet', 'type': 'text/css', 'href': '${string:${context/absolute_url}/++theme++barceloneta/css/barceloneta.min.css}', }
_static_139867344825472 = {'name': 'viewport', 'content': 'width=device-width, initial-scale=1', }
_static_139867344826960 = {'charset': 'utf-8', }
_static_139867362323344 = {}
_static_139867344829216 = {'xmlns': 'http://www.w3.org/1999/xhtml', 'xml:lang': 'en', 'lang': 'en', }

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
            __append('<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"\n  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n')

            # <Static value=<ast.Dict object at 0x7f3567677b20> name=None at 7f3567677af0> -> __attrs_139867344828784
            __attrs_139867344828784 = _static_139867344829216
            __previous_i18n_domain_139867344815968 = __i18n_domain
            __i18n_domain = 'plone'

            # <html ... (0:0)
            # --------------------------------------------------------
            __append('<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">\n\n')

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867344827920
            __attrs_139867344827920 = _static_139867362323344

            # <head ... (0:0)
            # --------------------------------------------------------
            __append('<head>\n  ')

            # <Static value=<ast.Dict object at 0x7f3567677250> name=None at 7f3567677220> -> __attrs_139867344826672
            __attrs_139867344826672 = _static_139867344826960

            # <meta ... (0:0)
            # --------------------------------------------------------
            __append('<meta charset="utf-8"/>\n  ')

            # <Static value=<ast.Dict object at 0x7f3567676c80> name=None at 7f3567676c50> -> __attrs_139867344825376
            __attrs_139867344825376 = _static_139867344825472

            # <meta ... (0:0)
            # --------------------------------------------------------
            __append('<meta name="viewport" content="width=device-width, initial-scale=1"/>\n  ')

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867344824608
            __attrs_139867344824608 = _static_139867362323344

            # <title ... (0:0)
            # --------------------------------------------------------
            __append('<title>Plone</title>\n  ')

            # <Static value=<ast.Dict object at 0x7f35676763e0> name=None at 7f35676763b0> -> __attrs_139867344822736
            __attrs_139867344822736 = _static_139867344823264

            # <link ... (0:0)
            # --------------------------------------------------------
            __append('<link rel="stylesheet" type="text/css"')

            # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867344824128
            __default_139867344824128 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution '${string:${context/absolute_url}/++theme++barceloneta/css/barceloneta.min.css}' (16:14)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f3567676680> -> __attr_href
            __token = 581
            __token = 583
            try:
                __zt_tmp = __attrs_139867344822736
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

            # <Static value=<ast.Dict object at 0x7f3565b6fd30> name=None at 7f3565b6feb0> -> __attrs_139867316480816
            __attrs_139867316480816 = _static_139867316485424

            # <link ... (0:0)
            # --------------------------------------------------------
            __append('<link rel="stylesheet" type="text/css"')

            # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867316485376
            __default_139867316485376 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution '${string:${context/absolute_url}/++resource++plone-admin-ui.css}' (19:14)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f3565b6cb80> -> __attr_href
            __token = 727
            __token = 729
            try:
                __zt_tmp = __attrs_139867316480816
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
            __append(' />\n</head>\n\n\n')

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867316482256
            __attrs_139867316482256 = _static_139867362323344
            __backup_sites_139867346841664 = get('sites', __marker)

            # <Value 'view/sites' (23:24)> -> __value
            __token = 830
            try:
                __zt_tmp = __attrs_139867316482256
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139867356405696('path', 'view/sites', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            econtext['sites'] = __value
            __backup_many_139867347392576 = get('many', __marker)

            # <Value 'python:len(sites) > 1' (24:22)> -> __value
            __token = 864
            try:
                __zt_tmp = __attrs_139867316482256
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139867356405696('python', 'len(sites) > 1', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            econtext['many'] = __value

            # <body ... (0:0)
            # --------------------------------------------------------
            __append('<body>\n  ')

            # <Static value=<ast.Dict object at 0x7f3565b6e950> name=None at 7f3565b6e7d0> -> __attrs_139867316480864
            __attrs_139867316480864 = _static_139867316480336

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="container admin mt-5 mb-5 p-4">\n    ')

            # <Static value=<ast.Dict object at 0x7f3565b6e290> name=None at 7f3565b6efe0> -> __attrs_139867316480480
            __attrs_139867316480480 = _static_139867316478608

            # <header ... (0:0)
            # --------------------------------------------------------
            __append('<header class="row">\n        ')

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867316470880
            __attrs_139867316470880 = _static_139867362323344

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p>')

            # <Static value=<ast.Dict object at 0x7f3565b6d4b0> name=None at 7f3565b6d3f0> -> __attrs_139867316474768
            __attrs_139867316474768 = _static_139867316475056

            # <img ... (0:0)
            # --------------------------------------------------------
            __append('<img')

            # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867316471264
            __default_139867316471264 = _DEFAULT_MARKER

            # <Substitution 'string:${context/absolute_url}/++resource++plone-logo.svg' (29:36)> -> __attr_src
            __token = 1087
            try:
                __zt_tmp = __attrs_139867316474768
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_src = _static_139867356405696('string', '${context/absolute_url}/++resource++plone-logo.svg', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            __attr_src = __quote(__attr_src, '"', '&quot;', '/++resource++plone-logo.svg', _DEFAULT_MARKER)
            if (__attr_src is not None):
                __append((' src="%s"' % __attr_src))
            __append(' width="215" height="56"')

            # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867316477840
            __default_139867316477840 = _DEFAULT_MARKER

            # <Translate msgid=None node=<ast.Constant object at 0x7f3565b6ddb0> at 7f3565b6e080> -> __attr_alt
            __attr_alt = 'Plone logo'
            __attr_alt = translate(__attr_alt, default=__attr_alt, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
            if (__attr_alt is not None):
                __append((' alt="%s"' % __attr_alt))
            __append(' /></p>\n        ')

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867316476400
            __attrs_139867316476400 = _static_139867362323344

            # <h1 ... (0:0)
            # --------------------------------------------------------
            __append('<h1>')
            __stream_139867316471072 = []
            __append_139867316471072 = __stream_139867316471072.append
            __append_139867316471072('Plone is up and running.')
            __msgid_139867316471072 = __re_whitespace(''.join(__stream_139867316471072)).strip()
            if __msgid_139867316471072:
                __append(translate(__msgid_139867316471072, mapping=None, default=__msgid_139867316471072, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</h1>\n        ')

            # <Static value=<ast.Dict object at 0x7f3565b6c940> name=None at 7f3565b6dbd0> -> __attrs_139867316475344
            __attrs_139867316475344 = _static_139867316472128

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p class="lead">\n            ')

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867316473712
            __attrs_139867316473712 = _static_139867362323344

            # <span ... (0:0)
            # --------------------------------------------------------
            __append('<span>')
            __stream_139867316475248 = []
            __append_139867316475248 = __stream_139867316475248.append
            __append_139867316475248(' For an introduction to Plone, documentation, demos, add-ons, support, and community, visit')
            __msgid_139867316475248 = __re_whitespace(''.join(__stream_139867316475248)).strip()
            if 'label_plone_org_description':
                __append(translate('label_plone_org_description', mapping=None, default=__msgid_139867316475248, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</span>\n            ')

            # <Static value=<ast.Dict object at 0x7f3565b6cac0> name=None at 7f3565b6cb20> -> __attrs_139867316471552
            __attrs_139867316471552 = _static_139867316472512

            # <a ... (0:0)
            # --------------------------------------------------------
            __append('<a href="http://plone.org"')

            # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867316473232
            __default_139867316473232 = _DEFAULT_MARKER

            # <Translate msgid='label_plone_org_title' node=<ast.Constant object at 0x7f3565b6c0a0> at 7f3565b6d0f0> -> __attr_title
            __attr_title = 'Plone Community Home'
            __attr_title = translate('label_plone_org_title', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
            if (__attr_title is not None):
                __append((' title="%s"' % __attr_title))
            __append('>plone.org</a>.\n          </p>\n\n    </header>\n\n    ')

            # <Static value=<ast.Dict object at 0x7f3565b6ebc0> name=None at 7f3565b6e4d0> -> __attrs_139867316483552
            __attrs_139867316483552 = _static_139867316480960

            # <article ... (0:0)
            # --------------------------------------------------------
            __append('<article class="row mb-5">\n        ')

            # <Static value=<ast.Dict object at 0x7f3565b6f7c0> name=None at 7f3565b6f7f0> -> __attrs_139867316483456
            __attrs_139867316483456 = _static_139867316484032

            # <Value 'sites' (44:28)> -> __condition
            __token = 1755
            try:
                __zt_tmp = __attrs_139867316483456
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_139867356405696('path', 'sites', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="col-md-12 mb-4">\n            ')

                # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867338814896
                __attrs_139867338814896 = _static_139867362323344
                __backup_site_139867346239936 = get('site', __marker)

                # <Value 'sites' (45:39)> -> __iterator
                __token = 1802
                try:
                    __zt_tmp = __attrs_139867338814896
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_139867356405696('path', 'sites', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                (__iterator, ____index_139867338815184, ) = getname('repeat')('site', __iterator)
                econtext['site'] = None
                for __item in __iterator:
                    econtext['site'] = __item
                    __append('\n                ')

                    # <Static value=<ast.Dict object at 0x7f35670bab90> name=None at 7f35670bac20> -> __attrs_139867338811440
                    __attrs_139867338811440 = _static_139867338812304
                    __backup_outdated_139867346255680 = get('outdated', __marker)

                    # <Value 'python: view.outdated(site)' (46:42)> -> __value
                    __token = 1852
                    try:
                        __zt_tmp = __attrs_139867338811440
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_139867356405696('python', ' view.outdated(site)', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                    econtext['outdated'] = __value

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div')

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867338812544
                    __default_139867338812544 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution "mb-3 ${python: 'p-3 alert alert-warning' if outdated else ''}" (47:28)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f35670bad10> -> __attr_class
                    __token = 1910
                    __token = 1917
                    try:
                        __zt_tmp = __attrs_139867338811440
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_139867356405696('python', " 'p-3 alert alert-warning' if outdated else ''", econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    __attr_class = ('%s%s' % ('mb-3 ', (__attr_class if (__attr_class is not None) else ''), ))
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
                    __append('>\n                    ')

                    # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867338810768
                    __attrs_139867338810768 = _static_139867362323344

                    # <Value 'outdated' (48:38)> -> __condition
                    __token = 2012
                    try:
                        __zt_tmp = __attrs_139867338810768
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_139867356405696('path', 'outdated', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                    if __condition:

                        # <p ... (0:0)
                        # --------------------------------------------------------
                        __append('<p>')
                        __stream_139867338810480 = []
                        __append_139867338810480 = __stream_139867338810480.append
                        __append_139867338810480('This site configuration is outdated and needs to be upgraded:')
                        __msgid_139867338810480 = __re_whitespace(''.join(__stream_139867338810480)).strip()
                        if __msgid_139867338810480:
                            __append(translate(__msgid_139867338810480, mapping=None, default=__msgid_139867338810480, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</p>')
                    __append('\n                    ')

                    # <Static value=<ast.Dict object at 0x7f35670b91e0> name=None at 7f35670b87c0> -> __attrs_139867338802320
                    __attrs_139867338802320 = _static_139867338805728

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867338803424
                    __default_139867338803424 = _DEFAULT_MARKER

                    # <Substitution 'site/absolute_url' (50:45)> -> __attr_href
                    __token = 2285
                    try:
                        __zt_tmp = __attrs_139867338802320
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_139867356405696('path', 'site/absolute_url', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '#', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))
                    __append(' id="go-to-site-link"')

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867338816000
                    __default_139867338816000 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution "btn btn-primary ${python:'btn-lg' if not many and not outdated  else ''}" (49:60)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f35670bb970> -> __attr_class
                    __token = 2166
                    __token = 2184
                    try:
                        __zt_tmp = __attrs_139867338802320
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_139867356405696('python', "'btn-lg' if not many and not outdated  else ''", econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    __attr_class = ('%s%s' % ('btn btn-primary ', (__attr_class if (__attr_class is not None) else ''), ))
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

                    # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867338813456
                    __default_139867338813456 = _DEFAULT_MARKER

                    # <Translate msgid=None node=<ast.Constant object at 0x7f35670b95d0> at 7f35670bb7f0> -> __attr_title
                    __attr_title = 'Go to your instance'
                    __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    if (__attr_title is not None):
                        __append((' title="%s"' % __attr_title))
                    __append('>\n                        ')

                    # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867338801936
                    __attrs_139867338801936 = _static_139867362323344

                    # <Value 'not: many' (53:44)> -> __condition
                    __token = 2450
                    try:
                        __zt_tmp = __attrs_139867338801936
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_139867356405696('not', ' many', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                    if __condition:
                        __stream_139867338802512 = []
                        __append_139867338802512 = __stream_139867338802512.append
                        __append_139867338802512('View your Plone site')
                        __msgid_139867338802512 = __re_whitespace(''.join(__stream_139867338802512)).strip()
                        if __msgid_139867338802512:
                            __append(translate(__msgid_139867338802512, mapping=None, default=__msgid_139867338802512, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('\n                        ')

                    # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867338801216
                    __attrs_139867338801216 = _static_139867362323344

                    # <Value 'many' (54:45)> -> __condition
                    __token = 2555
                    try:
                        __zt_tmp = __attrs_139867338801216
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_139867356405696('path', 'many', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                    if __condition:

                        # <Interpolation value=<Substitution '${python:site.title} ' (54:51)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f35670b8100> -> __content_139867442113136
                        __token = 2561
                        __token = 2563
                        try:
                            __zt_tmp = __attrs_139867338801216
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __content_139867442113136 = _static_139867356405696('python', 'site.title', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                        __content_139867442113136 = __quote(__content_139867442113136, '\x00', '&#0;', None, None)
                        __content_139867442113136 = ('%s%s' % ((__content_139867442113136 if (__content_139867442113136 is not None) else ''), ' ', ))
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

                        # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867338805632
                        __attrs_139867338805632 = _static_139867362323344

                        # <small ... (0:0)
                        # --------------------------------------------------------
                        __append('<small>')

                        # <Interpolation value=<Substitution '(${python:"/".join(site.getPhysicalPath())})' (54:79)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f35670b8f10> -> __content_139867442113136
                        __token = 2589
                        __token = 2592
                        try:
                            __zt_tmp = __attrs_139867338805632
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __content_139867442113136 = _static_139867356405696('python', '"/".join(site.getPhysicalPath())', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                        __content_139867442113136 = __quote(__content_139867442113136, '\x00', '&#0;', None, None)
                        __content_139867442113136 = ('%s%s%s' % ('(', (__content_139867442113136 if (__content_139867442113136 is not None) else ''), ')', ))
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
                        __append('</small>')
                    __append('\n                    </a>\n                    ')

                    # <Static value=<ast.Dict object at 0x7f35670ba020> name=None at 7f35670ba050> -> __attrs_139867338807696
                    __attrs_139867338807696 = _static_139867338809376

                    # <Value 'outdated' (59:43)> -> __condition
                    __token = 2851
                    try:
                        __zt_tmp = __attrs_139867338807696
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_139867356405696('path', 'outdated', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                    if __condition:

                        # <form ... (0:0)
                        # --------------------------------------------------------
                        __append('<form')

                        # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867338808368
                        __default_139867338808368 = _DEFAULT_MARKER

                        # <Substitution 'python:view.upgrade_url(site)' (60:51)> -> __attr_action
                        __token = 2912
                        try:
                            __zt_tmp = __attrs_139867338807696
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_action = _static_139867356405696('python', 'view.upgrade_url(site)', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                        __attr_action = __quote(__attr_action, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_action is not None):
                            __append((' action="%s"' % __attr_action))
                        __append(' style="display: inline;" method="get">\n                        ')

                        # <Static value=<ast.Dict object at 0x7f35670b9b10> name=None at 7f35670b99f0> -> __attrs_139867338806928
                        __attrs_139867338806928 = _static_139867338808080

                        # <Value 'not:view/can_manage' (61:46)> -> __condition
                        __token = 2990
                        try:
                            __zt_tmp = __attrs_139867338806928
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_139867356405696('not', 'view/can_manage', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                        if __condition:

                            # <input ... (0:0)
                            # --------------------------------------------------------
                            __append('<input type="hidden" name="came_from"')

                            # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867338808320
                            __default_139867338808320 = _DEFAULT_MARKER

                            # <Substitution 'python:view.upgrade_url(site, can_manage=True)' (63:54)> -> __attr_value
                            __token = 3128
                            try:
                                __zt_tmp = __attrs_139867338806928
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_value = _static_139867356405696('python', 'view.upgrade_url(site, can_manage=True)', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                            __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                            if (__attr_value is not None):
                                __append((' value="%s"' % __attr_value))
                            __append('/>')
                        __append('\n                        ')

                        # <Static value=<ast.Dict object at 0x7f35670bb100> name=None at 7f35670bb0a0> -> __attrs_139867338814944
                        __attrs_139867338814944 = _static_139867338813696

                        # <button ... (0:0)
                        # --------------------------------------------------------
                        __append('<button type="submit" class="btn btn-warning me-3">')
                        __stream_139867338817344 = []
                        __append_139867338817344 = __stream_139867338817344.append
                        __append_139867338817344('Upgrade&hellip;')
                        __msgid_139867338817344 = __re_whitespace(''.join(__stream_139867338817344)).strip()
                        if 'label_upgrade_hellip':
                            __append(translate('label_upgrade_hellip', mapping=None, default=__msgid_139867338817344, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</button>\n                    </form>')
                    __append('\n                </div>')
                    if (__backup_outdated_139867346255680 is __marker):
                        del econtext['outdated']
                    else:
                        econtext['outdated'] = __backup_outdated_139867346255680
                    __append('\n            ')
                    ____index_139867338815184 -= 1
                    if (____index_139867338815184 > 0):
                        __append('')
                if (__backup_site_139867346239936 is __marker):
                    del econtext['site']
                else:
                    econtext['site'] = __backup_site_139867346239936
                __append('\n        </div>')
            __append('\n        ')

            # <Static value=<ast.Dict object at 0x7f35670b9ea0> name=None at 7f35670b9cf0> -> __attrs_139867338816672
            __attrs_139867338816672 = _static_139867338808992

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="col-md-12">\n            ')

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867309129936
            __attrs_139867309129936 = _static_139867362323344

            # <h2 ... (0:0)
            # --------------------------------------------------------
            __append('<h2 >')
            __stream_139867338817440 = []
            __append_139867338817440 = __stream_139867338817440.append
            __append_139867338817440('Add Plone site')
            __msgid_139867338817440 = __re_whitespace(''.join(__stream_139867338817440)).strip()
            if __msgid_139867338817440:
                __append(translate(__msgid_139867338817440, mapping=None, default=__msgid_139867338817440, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</h2>\n            ')

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867309139152
            __attrs_139867309139152 = _static_139867362323344

            # <Value 'sites' (74:30)> -> __condition
            __token = 3620
            try:
                __zt_tmp = __attrs_139867309139152
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_139867356405696('path', 'sites', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            if __condition:

                # <p ... (0:0)
                # --------------------------------------------------------
                __append('<p>')
                __stream_139867309139632 = []
                __append_139867309139632 = __stream_139867309139632.append
                __append_139867309139632('\n                You can add another Plone site to the server.\n            ')
                __msgid_139867309139632 = __re_whitespace(''.join(__stream_139867309139632)).strip()
                if __msgid_139867309139632:
                    __append(translate(__msgid_139867309139632, mapping=None, default=__msgid_139867309139632, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</p>')
            __append('\n            ')

            # <Static value=<ast.Dict object at 0x7f356546c220> name=None at 7f356546dde0> -> __attrs_139867309138048
            __attrs_139867309138048 = _static_139867309130272

            # <Value 'not:sites' (78:30)> -> __condition
            __token = 3770
            try:
                __zt_tmp = __attrs_139867309138048
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_139867356405696('not', 'sites', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            if __condition:

                # <p ... (0:0)
                # --------------------------------------------------------
                __append('<p class="alert alert-warning p-1">')
                __stream_139867309137616 = []
                __append_139867309137616 = __stream_139867309137616.append
                __append_139867309137616('\n                Your Plone site has not been added yet.\n            ')
                __msgid_139867309137616 = __re_whitespace(''.join(__stream_139867309137616)).strip()
                if __msgid_139867309137616:
                    __append(translate(__msgid_139867309137616, mapping=None, default=__msgid_139867309137616, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</p>')
            __append('\n            ')

            # <Static value=<ast.Dict object at 0x7f356546d780> name=None at 7f356546d5d0> -> __attrs_139867309141552
            __attrs_139867309141552 = _static_139867309135744
            __backup_site_number_139867347392528 = get('site_number', __marker)

            # <Value "python: '' if not sites else len(sites) + 1" (84:44)> -> __value
            __token = 4017
            try:
                __zt_tmp = __attrs_139867309141552
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139867356405696('python', " '' if not sites else len(sites) + 1", econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            econtext['site_number'] = __value
            __backup_action_139867347392672 = get('action', __marker)

            # <Value 'string:${context/absolute_url}/@@plone-addsite' (85:38)> -> __value
            __token = 4100
            try:
                __zt_tmp = __attrs_139867309141552
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139867356405696('string', '${context/absolute_url}/@@plone-addsite', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            econtext['action'] = __value

            # <form ... (0:0)
            # --------------------------------------------------------
            __append('<form id="add-plone-site" method="get"')

            # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867309134160
            __default_139867309134160 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution '${action}' (86:28)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f356546cd30> -> __attr_action
            __token = 4177
            __token = 4179
            try:
                __zt_tmp = __attrs_139867309141552
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_action = _static_139867356405696('path', 'action', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            __attr_action = __quote(__attr_action, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_action = __attr_action
            if (__attr_action is None):
                pass
            else:
                if (__attr_action is _DEFAULT_MARKER):
                    __attr_action = None
                else:
                    __tt = type(__attr_action)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __attr_action = str(__attr_action)
                    else:
                        if (__tt is bytes):
                            __attr_action = decode(__attr_action)
                        else:
                            if (__tt is not str):
                                try:
                                    __attr_action = __attr_action.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__attr_action)
                                    __attr_action = (str(__attr_action) if (__attr_action is __converted) else __converted)
                                else:
                                    __attr_action = __attr_action()
            if (__attr_action is not None):
                __append((' action="%s"' % __attr_action))
            __append('>\n                ')

            # <Static value=<ast.Dict object at 0x7f356546efe0> name=None at 7f356546da80> -> __attrs_139867309139968
            __attrs_139867309139968 = _static_139867309141984

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input type="hidden" name="site_id"')

            # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867309140688
            __default_139867309140688 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution 'Plone${site_number}' (87:59)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f356546f1c0> -> __attr_value
            __token = 4248
            __token = 4255
            try:
                __zt_tmp = __attrs_139867309139968
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_value = _static_139867356405696('path', 'site_number', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_value = ('%s%s' % ('Plone', (__attr_value if (__attr_value is not None) else ''), ))
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

            # <Static value=<ast.Dict object at 0x7f356546fdf0> name=None at 7f356546fcd0> -> __attrs_139867309145488
            __attrs_139867309145488 = _static_139867309145584

            # <button ... (0:0)
            # --------------------------------------------------------
            __append('<button type="submit"')

            # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867309141888
            __default_139867309141888 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution "btn btn-${python:'success' if sites else 'primary'}" (89:31)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f356546f0d0> -> __attr_class
            __token = 4341
            __token = 4351
            try:
                __zt_tmp = __attrs_139867309145488
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_139867356405696('python', "'success' if sites else 'primary'", econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_class = ('%s%s' % ('btn btn-', (__attr_class if (__attr_class is not None) else ''), ))
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
            __append('>')
            __stream_139867309135552 = []
            __append_139867309135552 = __stream_139867309135552.append
            __append_139867309135552('Create a new Plone site')
            __msgid_139867309135552 = __re_whitespace(''.join(__stream_139867309135552)).strip()
            if __msgid_139867309135552:
                __append(translate(__msgid_139867309135552, mapping=None, default=__msgid_139867309135552, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</button>\n                ')

            # <Static value=<ast.Dict object at 0x7f356546f880> name=None at 7f356546f850> -> __attrs_139867309144096
            __attrs_139867309144096 = _static_139867309144192

            # <Value 'view/has_volto' (93:35)> -> __condition
            __token = 4582
            try:
                __zt_tmp = __attrs_139867309144096
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_139867356405696('path', 'view/has_volto', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            if __condition:

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a class="btn btn-info"')

                # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867309134688
                __default_139867309134688 = _DEFAULT_MARKER

                # <Interpolation value=<Substitution '${action}?site_id=Plone${site_number}&amp;classic=1' (94:26)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f356546f6d0> -> __attr_href
                __token = 4624
                __token = 4626
                try:
                    __zt_tmp = __attrs_139867309144096
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_139867356405696('path', 'action', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                __token = 4649
                try:
                    __zt_tmp = __attrs_139867309144096
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href_4647 = _static_139867356405696('path', 'site_number', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
                __attr_href_4647 = __quote(__attr_href_4647, '"', '&quot;', None, _DEFAULT_MARKER)
                __attr_href = ('%s%s%s%s' % ((__attr_href if (__attr_href is not None) else ''), '?site_id=Plone', (__attr_href_4647 if (__attr_href_4647 is not None) else ''), '&amp;classic=1', ))
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
                __append(' >')
                __stream_139867309144672 = []
                __append_139867309144672 = __stream_139867309144672.append
                __append_139867309144672('Create Classic Plone site')
                __msgid_139867309144672 = __re_whitespace(''.join(__stream_139867309144672)).strip()
                if __msgid_139867309144672:
                    __append(translate(__msgid_139867309144672, mapping=None, default=__msgid_139867309144672, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</a>')
            __append('\n                ')

            # <Static value=<ast.Dict object at 0x7f356546ff40> name=None at 7f356546fac0> -> __attrs_139867309138720
            __attrs_139867309138720 = _static_139867309145920

            # <a ... (0:0)
            # --------------------------------------------------------
            __append('<a class="btn btn-secondary"')

            # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867309133680
            __default_139867309133680 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution '${action}?site_id=Plone${site_number}&amp;advanced=1' (98:26)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f356546cfa0> -> __attr_href
            __token = 4837
            __token = 4839
            try:
                __zt_tmp = __attrs_139867309138720
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_139867356405696('path', 'action', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
            __token = 4862
            try:
                __zt_tmp = __attrs_139867309138720
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href_4860 = _static_139867356405696('path', 'site_number', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            __attr_href_4860 = __quote(__attr_href_4860, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_href = ('%s%s%s%s' % ((__attr_href if (__attr_href is not None) else ''), '?site_id=Plone', (__attr_href_4860 if (__attr_href_4860 is not None) else ''), '&amp;advanced=1', ))
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
            __append(' >')
            __stream_139867309133776 = []
            __append_139867309133776 = __stream_139867309133776.append
            __append_139867309133776('Advanced')
            __msgid_139867309133776 = __re_whitespace(''.join(__stream_139867309133776)).strip()
            if __msgid_139867309133776:
                __append(translate(__msgid_139867309133776, mapping=None, default=__msgid_139867309133776, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</a>\n            </form>')
            if (__backup_action_139867347392672 is __marker):
                del econtext['action']
            else:
                econtext['action'] = __backup_action_139867347392672
            if (__backup_site_number_139867347392528 is __marker):
                del econtext['site_number']
            else:
                econtext['site_number'] = __backup_site_number_139867347392528
            __append('\n            ')

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867309134208
            __attrs_139867309134208 = _static_139867362323344

            # <br ... (0:0)
            # --------------------------------------------------------
            __append('<br/>\n            ')

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867309132192
            __attrs_139867309132192 = _static_139867362323344

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p>')
            __stream_139867309130224 = []
            __append_139867309130224 = __stream_139867309130224.append
            __append_139867309130224("\n                Starting with Plone 6, 'Create a new Plone site' applies a\n                profile and creates default content for the new React based\n                default frontend Volto. You are however required to set up and run\n                an additional frontend service to use this setup.\n            ")
            __msgid_139867309130224 = __re_whitespace(''.join(__stream_139867309130224)).strip()
            if 'help_create_plone_site_buttons_1':
                __append(translate('help_create_plone_site_buttons_1', mapping=None, default=__msgid_139867309130224, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</p>\n            ')

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867309130464
            __attrs_139867309130464 = _static_139867362323344

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p>')
            __stream_139867348318048_docs_link = ''
            __stream_139867309130944 = []
            __append_139867309130944 = __stream_139867309130944.append
            __append_139867309130944("\n                The 'Create Classic Plone site' button creates a Plone site configured\n                for HTML based output, as was already supported by previous Plone versions.\n                Please consult our\n                ")
            __stream_139867348318048_docs_link = []
            __append_139867348318048_docs_link = __stream_139867348318048_docs_link.append

            # <Static value=<ast.Dict object at 0x7f35653be1a0> name=None at 7f35653bdf30> -> __attrs_139867308421136
            __attrs_139867308421136 = _static_139867308417440

            # <a ... (0:0)
            # --------------------------------------------------------
            __append_139867348318048_docs_link('<a href="https://6.docs.plone.org/"')

            # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867308423728
            __default_139867308423728 = _DEFAULT_MARKER

            # <Translate msgid=None node=<ast.Constant object at 0x7f35653bdab0> at 7f35653bdc30> -> __attr_title
            __attr_title = 'Plone 6 developer documentation'
            __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
            if (__attr_title is not None):
                __append_139867348318048_docs_link((' title="%s"' % __attr_title))
            __append_139867348318048_docs_link('>')
            __stream_139867308412928 = []
            __append_139867308412928 = __stream_139867308412928.append
            __append_139867308412928('developer documentation overview ')
            __msgid_139867308412928 = __re_whitespace(''.join(__stream_139867308412928)).strip()
            if __msgid_139867308412928:
                __append_139867348318048_docs_link(translate(__msgid_139867308412928, mapping=None, default=__msgid_139867308412928, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append_139867348318048_docs_link('</a>')
            __append_139867309130944('${docs_link}')
            __stream_139867348318048_docs_link = ''.join(__stream_139867348318048_docs_link)
            __append_139867309130944('\n                for more information about differences and requirements for\n                these frontends and possible upgrade paths from older Plone versions\n                to Plone 6.\n            ')
            __msgid_139867309130944 = __re_whitespace(''.join(__stream_139867309130944)).strip()
            if 'help_create_plone_site_buttons_2':
                __append(translate('help_create_plone_site_buttons_2', mapping={'docs_link': __stream_139867348318048_docs_link, }, default=__msgid_139867309130944, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</p>\n        </div>\n    </article>\n\n    ')

            # <Static value=<ast.Dict object at 0x7f35653bf370> name=None at 7f356546c3d0> -> __attrs_139867308418400
            __attrs_139867308418400 = _static_139867308422000

            # <footer ... (0:0)
            # --------------------------------------------------------
            __append('<footer class="row">\n    ')

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867308424688
            __attrs_139867308424688 = _static_139867362323344

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p>\n      ')

            # <Static value=<ast.Dict object at 0x7f35653bf790> name=None at 7f35653bc460> -> __attrs_139867308419024
            __attrs_139867308419024 = _static_139867308423056

            # <a ... (0:0)
            # --------------------------------------------------------
            __append('<a')

            # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867308417584
            __default_139867308417584 = _DEFAULT_MARKER

            # <Substitution 'string:${context/absolute_url}/manage_main' (126:29)> -> __attr_href
            __token = 6194
            try:
                __zt_tmp = __attrs_139867308419024
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_139867356405696('string', '${context/absolute_url}/manage_main', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', '#', _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((' href="%s"' % __attr_href))

            # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867308423008
            __default_139867308423008 = _DEFAULT_MARKER

            # <Translate msgid=None node=<ast.Constant object at 0x7f35653bc370> at 7f35653bc100> -> __attr_title
            __attr_title = 'Go to the ZMI'
            __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
            if (__attr_title is not None):
                __append((' title="%s"' % __attr_title))
            __append('>')
            __stream_139867308414272 = []
            __append_139867308414272 = __stream_139867308414272.append
            __append_139867308414272('Management Interface')
            __msgid_139867308414272 = __re_whitespace(''.join(__stream_139867308414272)).strip()
            if 'label_zmi_link':
                __append(translate('label_zmi_link', mapping=None, default=__msgid_139867308414272, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</a>\n      ')

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867308421808
            __attrs_139867308421808 = _static_139867362323344

            # <span ... (0:0)
            # --------------------------------------------------------
            __append('<span>')
            __stream_139867308422912 = []
            __append_139867308422912 = __stream_139867308422912.append
            __append_139867308422912(' &#151; low-level technical configuration.')
            __msgid_139867308422912 = __re_whitespace(''.join(__stream_139867308422912)).strip()
            if 'label_zmi_link_description':
                __append(translate('label_zmi_link_description', mapping=None, default=__msgid_139867308422912, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</span>\n    </p>\n  </footer>\n</div>\n</body>')
            if (__backup_many_139867347392576 is __marker):
                del econtext['many']
            else:
                econtext['many'] = __backup_many_139867347392576
            if (__backup_sites_139867346841664 is __marker):
                del econtext['sites']
            else:
                econtext['sites'] = __backup_sites_139867346841664
            __append('\n</html>')
            __i18n_domain = __previous_i18n_domain_139867344815968
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }