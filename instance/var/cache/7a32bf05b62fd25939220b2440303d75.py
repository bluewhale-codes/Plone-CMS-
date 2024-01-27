# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/Products/CMFPlone/browser/templates/footer.pt'

__tokens = {860: ('nocall:modules/DateTime.DateTime', 20, 30), 921: (' python:DateTime(', 21, 27), 963: ('python:myTime.year()', 22, 22)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139867202249264 = {'xmlns': 'http://www.w3.org/1999/xhtml', 'xml:lang': 'en', 'lang': 'en', }
_static_139867200024304 = {'href': 'http://creativecommons.org/licenses/GPL/2.0/', }
_static_139867200017584 = {'href': 'http://plone.org/foundation', }
_static_139867356405408 = __C2ZContextWrapper
_static_139867356405696 = __compile_zt_expr
_static_139867200027232 = {'title': 'Copyright', }
_static_139867200026704 = {'href': 'http://plone.org', }
_static_139867362323344 = {}
_static_139867200023968 = {'class': 'card-body', }
_static_139867202252000 = {'class': 'card card-classic', 'id': 'portal-footer-signature', }

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

    def render_portlet(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<ast.Dict object at 0x7f355ee7ece0> name=None at 7f35689c9600> -> __attrs_139867200026176
            __attrs_139867200026176 = _static_139867202252000

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="card card-classic" id="portal-footer-signature">\n\n    ')

            # <Static value=<ast.Dict object at 0x7f355ec5eda0> name=None at 7f355ec5dd20> -> __attrs_139867200015088
            __attrs_139867200015088 = _static_139867200023968

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="card-body">\n      ')

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867200016384
            __attrs_139867200016384 = _static_139867362323344
            __stream_139867198909216_current_year = ''
            __stream_139867198909216_plonefoundation = ''
            __stream_139867198909216_plonecms = ''
            __stream_139867198909216_copyright = ''
            __stream_139867200026512 = []
            __append_139867200026512 = __stream_139867200026512.append
            __append_139867200026512('\n      The\n      ')
            __stream_139867198909216_plonecms = []
            __append_139867198909216_plonecms = __stream_139867198909216_plonecms.append

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867200023680
            __attrs_139867200023680 = _static_139867362323344
            __append_139867198909216_plonecms('\n           ')

            # <Static value=<ast.Dict object at 0x7f355ec5f850> name=None at 7f355ec5d1e0> -> __attrs_139867200025360
            __attrs_139867200025360 = _static_139867200026704

            # <a ... (0:0)
            # --------------------------------------------------------
            __append_139867198909216_plonecms('<a href="http://plone.org">')
            __stream_139867200021184 = []
            __append_139867200021184 = __stream_139867200021184.append
            __append_139867200021184('Plone')

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867200025120
            __attrs_139867200025120 = _static_139867362323344

            # <sup ... (0:0)
            # --------------------------------------------------------
            __append_139867200021184('<sup>&reg;</sup> Open Source CMS/WCM')
            __msgid_139867200021184 = __re_whitespace(''.join(__stream_139867200021184)).strip()
            if 'label_plone_cms':
                __append_139867198909216_plonecms(translate('label_plone_cms', mapping=None, default=__msgid_139867200021184, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append_139867198909216_plonecms('</a>\n      ')
            __append_139867200026512('${plonecms}')
            __stream_139867198909216_plonecms = ''.join(__stream_139867198909216_plonecms)
            __append_139867200026512('\n      is\n      ')
            __stream_139867198909216_copyright = []
            __append_139867198909216_copyright = __stream_139867198909216_copyright.append

            # <Static value=<ast.Dict object at 0x7f355ec5fa60> name=None at 7f355ec5ece0> -> __attrs_139867200021904
            __attrs_139867200021904 = _static_139867200027232

            # <abbr ... (0:0)
            # --------------------------------------------------------
            __append_139867198909216_copyright('<abbr')

            # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867200027328
            __default_139867200027328 = _DEFAULT_MARKER

            # <Translate msgid='title_copyright' node=<ast.Constant object at 0x7f355ec5c040> at 7f355ec5e3b0> -> __attr_title
            __attr_title = 'Copyright'
            __attr_title = translate('title_copyright', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
            if (__attr_title is not None):
                __append_139867198909216_copyright((' title="%s"' % __attr_title))
            __append_139867198909216_copyright('>&copy;</abbr>')
            __append_139867200026512('${copyright}')
            __stream_139867198909216_copyright = ''.join(__stream_139867198909216_copyright)
            __append_139867200026512('\n      2000-')
            __stream_139867198909216_current_year = []
            __append_139867198909216_current_year = __stream_139867198909216_current_year.append

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867200023584
            __attrs_139867200023584 = _static_139867362323344
            __backup_DateTime_139867200511408 = get('DateTime', __marker)

            # <Value 'nocall:modules/DateTime.DateTime' (20:30)> -> __value
            __token = 860
            try:
                __zt_tmp = __attrs_139867200023584
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139867356405696('nocall', 'modules/DateTime.DateTime', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            econtext['DateTime'] = __value
            __backup_myTime_139867200018112 = get('myTime', __marker)

            # <Value 'python:DateTime()' (21:27)> -> __value
            __token = 921
            try:
                __zt_tmp = __attrs_139867200023584
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139867356405696('python', 'DateTime()', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))
            econtext['myTime'] = __value

            # <Symbol value=<DEFAULT> at 7f3568756860> -> __default_139867200025072
            __default_139867200025072 = _DEFAULT_MARKER

            # <Value 'python:myTime.year()' (22:22)> -> __cache_139867200027856
            __token = 963
            try:
                __zt_tmp = __attrs_139867200023584
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139867200027856 = _static_139867356405696('python', 'myTime.year()', econtext=econtext)(_static_139867356405408(econtext, __zt_tmp))

            # <BinOp left=<Value 'python:myTime.year()' (22:22)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f3568756860> at 7f355ec5f250> -> __condition
            __expression = __cache_139867200027856

            # <Symbol value=<DEFAULT> at 7f3568756860> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_139867200027856
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append_139867198909216_current_year(__content)
            if (__backup_myTime_139867200018112 is __marker):
                del econtext['myTime']
            else:
                econtext['myTime'] = __backup_myTime_139867200018112
            if (__backup_DateTime_139867200511408 is __marker):
                del econtext['DateTime']
            else:
                econtext['DateTime'] = __backup_DateTime_139867200511408
            __append_139867200026512('${current_year}')
            __stream_139867198909216_current_year = ''.join(__stream_139867198909216_current_year)
            __append_139867200026512('\n      by the\n      ')
            __stream_139867198909216_plonefoundation = []
            __append_139867198909216_plonefoundation = __stream_139867198909216_plonefoundation.append

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867200013072
            __attrs_139867200013072 = _static_139867362323344
            __append_139867198909216_plonefoundation('\n           ')

            # <Static value=<ast.Dict object at 0x7f355ec5d4b0> name=None at 7f355ec5f8e0> -> __attrs_139867200020512
            __attrs_139867200020512 = _static_139867200017584

            # <a ... (0:0)
            # --------------------------------------------------------
            __append_139867198909216_plonefoundation('<a href="http://plone.org/foundation">')
            __stream_139867200014320 = []
            __append_139867200014320 = __stream_139867200014320.append
            __append_139867200014320('Plone Foundation')
            __msgid_139867200014320 = __re_whitespace(''.join(__stream_139867200014320)).strip()
            if 'label_plone_foundation':
                __append_139867198909216_plonefoundation(translate('label_plone_foundation', mapping=None, default=__msgid_139867200014320, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append_139867198909216_plonefoundation('</a>')
            __append_139867200026512('${plonefoundation}')
            __stream_139867198909216_plonefoundation = ''.join(__stream_139867198909216_plonefoundation)
            __append_139867200026512('\n      and friends.\n      ')
            __msgid_139867200026512 = __re_whitespace(''.join(__stream_139867200026512)).strip()
            if 'description_copyright':
                __append(translate('description_copyright', mapping={'copyright': __stream_139867198909216_copyright, 'plonecms': __stream_139867198909216_plonecms, 'plonefoundation': __stream_139867198909216_plonefoundation, 'current_year': __stream_139867198909216_current_year, }, default=__msgid_139867200026512, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('\n\n      ')

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867200016288
            __attrs_139867200016288 = _static_139867362323344
            __stream_139867198909216_license = ''
            __stream_139867200017920 = []
            __append_139867200017920 = __stream_139867200017920.append
            __append_139867200017920('\n      Distributed under the\n           ')
            __stream_139867198909216_license = []
            __append_139867198909216_license = __stream_139867198909216_license.append

            # <Static value=<ast.Dict object at 0x7f3568726b90> name=None at 7f3568727670> -> __attrs_139867200018496
            __attrs_139867200018496 = _static_139867362323344
            __append_139867198909216_license('\n                ')

            # <Static value=<ast.Dict object at 0x7f355ec5eef0> name=None at 7f355ec5f1c0> -> __attrs_139867202493440
            __attrs_139867202493440 = _static_139867200024304

            # <a ... (0:0)
            # --------------------------------------------------------
            __append_139867198909216_license('<a href="http://creativecommons.org/licenses/GPL/2.0/">')
            __stream_139867200015856 = []
            __append_139867200015856 = __stream_139867200015856.append
            __append_139867200015856('GNU GPL license')
            __msgid_139867200015856 = __re_whitespace(''.join(__stream_139867200015856)).strip()
            if 'label_gnu_gpl_licence':
                __append_139867198909216_license(translate('label_gnu_gpl_licence', mapping=None, default=__msgid_139867200015856, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append_139867198909216_license('</a>')
            __append_139867200017920('${license}')
            __stream_139867198909216_license = ''.join(__stream_139867198909216_license)
            __append_139867200017920('.\n      ')
            __msgid_139867200017920 = __re_whitespace(''.join(__stream_139867200017920)).strip()
            if 'description_license':
                __append(translate('description_license', mapping={'license': __stream_139867198909216_license, }, default=__msgid_139867200017920, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('\n    </div>\n\n  </div>')
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

            # <Static value=<ast.Dict object at 0x7f355ee7e230> name=None at 7f355ee7c700> -> __attrs_139867202248496
            __attrs_139867202248496 = _static_139867202249264
            __previous_i18n_domain_139867202256800 = __i18n_domain
            __i18n_domain = 'plone'
            __append('\n\n  ')
            __token = None
            render_portlet(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n\n')
            __i18n_domain = __previous_i18n_domain_139867202256800
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_portlet': render_portlet, 'render': render, }