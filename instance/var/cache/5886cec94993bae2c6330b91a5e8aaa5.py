# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/plone/app/registry/browser/templates/records.pt'

__tokens = {400: ("python:request.set('disable_border', 1)", 10, 31), 484: (" python:request.set('disable_plone.leftcolumn', 1", 11, 43), 578: ("o python:request.set('disable_plone.rightcolumn', ", 12, 42), 741: ('view/records', 17, 22), 1430: ('request/qp|nothing', 36, 37), 1485: (' request/q|nothin', 37, 35), 1853: ('python: qp or q', 45, 46), 2690: ('python: sorted(view.prefixes.keys())', 64, 47), 2885: ('prefixes', 66, 59), 2980: ("python: 'prefix:' + (view.prefixes[prefix] or '')", 68, 48), 3083: ('value', 69, 52), 3134: ('prefix', 70, 43), 4346: ('records', 103, 43), 4401: ('repeat/record/odd', 104, 45), 4463: (' record/field/originalField | record/fiel', 105, 43), 4555: ("python:oddrow and 'odd' or 'even'", 106, 48), 4839: ('string:${context/absolute_url}/edit/${record/__name__}', 110, 54), 4743: ("python:record.__name__.replace('.', ' ')", 109, 46), 5006: ('field/title', 113, 43), 5094: ('field/description', 114, 53), 5184: ('field/__class__/__name__', 115, 43), 5328: ('record/value|nothing', 117, 47), 5398: ('string:?', 118, 48), 5516: ('not: record/interfaceName|nothing', 120, 58), 5628: ('${context/absolute_url}/@@delete-record?name=${record/__name__}', 122, 39), 5630: ('context/absolute_url', 122, 41), 5675: ('record/__name__', 122, 86), 6048: ('python: records.numpages > 1', 131, 36), 6158: ('records', 133, 56), 6216: ('here/batch_macros/macros/navigation', 134, 48), 6216: ('here/batch_macros/macros/navigation', 134, 48), 6934: ("python:context.restrictedTraverse('@@configuration_registry_export_xml')()", 152, 38), 7889: ('context/@@ploneform-macros/titlelessform', 170, 34), 7889: ('context/@@ploneform-macros/titlelessform', 170, 34), 261: ('context/@@prefs_main_template/macros/master', 6, 23), 261: ('context/@@prefs_main_template/macros/master', 6, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tal import ErrorInfo as _ErrorInfo
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from collections import deque as _deque

_static_140453435875840 = 'titlelessform'
_static_140453435872912 = {'class': 'tab', }
_static_140453435872240 = {'class': 'btn btn-primary', 'type': 'submit', }
_static_140453435870224 = {'class': 'formControls mt-3', }
_static_140453435869168 = {'type': 'hidden', 'name': 'button.importregistry', 'value': 'true', }
_static_140453435834224 = {'type': 'file', 'name': 'file', 'id': 'exportFile', 'class': 'form-control', }
_static_140453435833312 = {'for': 'exportFile', 'class': 'form-label', }
_static_140453435831296 = {'class': 'mb-3 field', }
_static_140453435830144 = {'method': 'POST', 'enctype': 'multipart/form-data', }
_static_140453435827408 = {'class': 'tab', }
_static_140453435824720 = {'class': 'btn btn-primary', 'type': 'submit', }
_static_140453435822752 = {'class': 'formControls', }
_static_140453435821648 = {'type': 'hidden', 'name': 'button.exportregistry', 'value': 'true', }
_static_140453435819872 = {'method': 'POST', }
_static_140453435702624 = {'class': 'tab', }
_static_140453435783344 = 'navigation'
_static_140453435782048 = {'colspan': '5', }
_static_140453435779648 = {'href': '${context/absolute_url}/@@delete-record?name=${record/__name__}', 'class': 'recordsDeleteLink', }
_static_140453435775568 = {'class': 'value', }
_static_140453435773552 = {'data-label': 'Value', }
_static_140453435772400 = {'data-label': 'Type', }
_static_140453435770576 = {'data-label': 'Description', }
_static_140453435752304 = {'data-label': 'Title', }
_static_140453435750624 = {'class': 'recordsEditLink', 'href': 'string:${context/absolute_url}/edit/${record/__name__}', }
_static_140453435748080 = {'data-label': 'Name', }
_static_140453435746112 = {'class': "python:oddrow and 'odd' or 'even'", }
_static_140453435703248 = {'class': 'table table-bordered table-striped', }
_static_140453435701856 = {'class': 'table-responsive', }
_static_140453435701424 = {'class': 'btn btn-secondary', 'type': 'reset', }
_static_140453435699456 = {'id': 'clear-filter', }
_static_140453435695616 = {'class': 'mb-3 col-auto', }
_static_140453435697248 = {'value': 'value', }
_static_140453435694176 = {'value': '', }
_static_140453435692784 = {'class': 'form-select', 'name': 'qp', }
_static_140453435690960 = {'class': 'col-form-label me-2', }
_static_140453435689472 = {'class': 'input-group', }
_static_140453435688128 = {'class': 'mb-3 col-auto', }
_static_140453435654000 = {'class': 'row justify-content-between', }
_static_140453435652608 = {'class': 'btn btn-primary', 'type': 'submit', 'value': 'Filter', }
_static_140453435650640 = {'class': 'input-group-append', }
_static_140453435649584 = {'class': 'form-control', 'name': 'q', 'id': 'q', 'placeholder': 'filter by...', 'value': 'python: qp or q', }
_static_140453435646752 = {'class': 'input-group', }
_static_140453435645360 = {'class': 'mb-3', }
_static_140453435643440 = {'id': 'registry-filter', }
_static_140453435642144 = {'id': 'searchrow', }
_static_140453435641136 = {'id': 'recordsTable', 'class': 'pat-registry', }
_static_140453437407136 = {'id': 'recordsContainer', 'class': 'tab', }
_static_140453437406176 = {'class': 'pat-autotoc autotabs', 'data-pat-autotoc': 'section:.tab;levels:h2;', }
_static_140453437404496 = {'id': 'content-core', }
_static_140453437403344 = {'class': 'lead', }
_static_140453437402048 = {'class': 'documentFirstHeading', }
_static_140453437399408 = {'id': 'content', }
_static_140453526790416 = __C2ZContextWrapper
_static_140453526790704 = __compile_zt_expr
_static_140453437395088 = 'master'
_static_140453526549936 = {}

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

            # <Static value=<ast.Dict object at 0x7fbde28eb5b0> name=None at 7fbde28eb8e0> -> __attrs_140453437395424
            __attrs_140453437395424 = _static_140453526549936
            __previous_i18n_domain_140453437395856 = __i18n_domain
            __i18n_domain = 'plone'
            __backup_macroname_140453481312640 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7fbddd3e5090> name=None at 7fbddd3e50c0> -> __value
            __value = _static_140453437395088
            econtext['macroname'] = __value

            def __fill_top_slot(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7fbde28eb5b0> name=None at 7fbde28eb8e0> -> __attrs_140453437396480
                __attrs_140453437396480 = _static_140453526549936
                __append('\n')

                # <Static value=<ast.Dict object at 0x7fbde28eb5b0> name=None at 7fbde28eb8e0> -> __attrs_140453437397296
                __attrs_140453437397296 = _static_140453526549936
                __backup_dummy_140453439326912 = get('dummy', __marker)

                # <Value "python:request.set('disable_border', 1)" (10:31)> -> __value
                __token = 400
                try:
                    __zt_tmp = __attrs_140453437397296
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140453526790704('python', "request.set('disable_border', 1)", econtext=econtext)(_static_140453526790416(econtext, __zt_tmp))
                econtext['dummy'] = __value
                __backup_disable_column_one_140453439326432 = get('disable_column_one', __marker)

                # <Value "python:request.set('disable_plone.leftcolumn', 1)" (11:43)> -> __value
                __token = 484
                try:
                    __zt_tmp = __attrs_140453437397296
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140453526790704('python', "request.set('disable_plone.leftcolumn', 1)", econtext=econtext)(_static_140453526790416(econtext, __zt_tmp))
                econtext['disable_column_one'] = __value
                __backup_disable_column_two_140453439324944 = get('disable_column_two', __marker)

                # <Value "python:request.set('disable_plone.rightcolumn', 0)" (12:42)> -> __value
                __token = 578
                try:
                    __zt_tmp = __attrs_140453437397296
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140453526790704('python', "request.set('disable_plone.rightcolumn', 0)", econtext=econtext)(_static_140453526790416(econtext, __zt_tmp))
                econtext['disable_column_two'] = __value
                if (__backup_disable_column_two_140453439324944 is __marker):
                    del econtext['disable_column_two']
                else:
                    econtext['disable_column_two'] = __backup_disable_column_two_140453439324944
                if (__backup_disable_column_one_140453439326432 is __marker):
                    del econtext['disable_column_one']
                else:
                    econtext['disable_column_one'] = __backup_disable_column_one_140453439326432
                if (__backup_dummy_140453439326912 is __marker):
                    del econtext['dummy']
                else:
                    econtext['dummy'] = __backup_dummy_140453439326912
                __append('\n')
            _slots = econtext['__slot_top_slot'] = _deque((__fill_top_slot, ))

            def __fill_prefs_configlet_main(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7fbddd3e6170> name=None at 7fbddd3e6110> -> __attrs_140453437399696
                __attrs_140453437399696 = _static_140453437399408
                __backup_records_140453439325184 = get('records', __marker)

                # <Value 'view/records' (17:22)> -> __value
                __token = 741
                try:
                    __zt_tmp = __attrs_140453437399696
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140453526790704('path', 'view/records', econtext=econtext)(_static_140453526790416(econtext, __zt_tmp))
                econtext['records'] = __value

                # <article ... (0:0)
                # --------------------------------------------------------
                __append('<article id="content">\n\n  ')

                # <Static value=<ast.Dict object at 0x7fbde28eb5b0> name=None at 7fbde28eb8e0> -> __attrs_140453437400944
                __attrs_140453437400944 = _static_140453526549936

                # <header ... (0:0)
                # --------------------------------------------------------
                __append('<header>\n    ')

                # <Static value=<ast.Dict object at 0x7fbddd3e6bc0> name=None at 7fbddd3e6a40> -> __attrs_140453437402384
                __attrs_140453437402384 = _static_140453437402048

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append('<h1 class="documentFirstHeading">')
                __stream_140453437401520 = []
                __append_140453437401520 = __stream_140453437401520.append
                __append_140453437401520('Configuration Registry')
                __msgid_140453437401520 = __re_whitespace(''.join(__stream_140453437401520)).strip()
                if 'heading_registry':
                    __append(translate('heading_registry', mapping=None, default=__msgid_140453437401520, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</h1>\n\n    ')

                # <Static value=<ast.Dict object at 0x7fbddd3e70d0> name=None at 7fbddd3e7100> -> __attrs_140453437403728
                __attrs_140453437403728 = _static_140453437403344

                # <p ... (0:0)
                # --------------------------------------------------------
                __append('<p class="lead">')
                __stream_140453437402864 = []
                __append_140453437402864 = __stream_140453437402864.append
                __append_140453437402864('\n        The table below shows record currently managed by the configuration\n        registry. Click on a record to edit it.\n    ')
                __msgid_140453437402864 = __re_whitespace(''.join(__stream_140453437402864)).strip()
                if 'description_registry':
                    __append(translate('description_registry', mapping=None, default=__msgid_140453437402864, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</p>\n  </header>\n    ')

                # <Static value=<ast.Dict object at 0x7fbddd3e7550> name=None at 7fbddd3e7580> -> __attrs_140453437404880
                __attrs_140453437404880 = _static_140453437404496

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div id="content-core">\n      ')

                # <Static value=<ast.Dict object at 0x7fbddd3e7be0> name=None at 7fbddd3e7c10> -> __attrs_140453437406464
                __attrs_140453437406464 = _static_140453437406176

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="pat-autotoc autotabs" data-pat-autotoc="section:.tab;levels:h2;">\n        ')

                # <Static value=<ast.Dict object at 0x7fbddd3e7fa0> name=None at 7fbddd3e7f40> -> __attrs_140453435638640
                __attrs_140453435638640 = _static_140453437407136

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div id="recordsContainer" class="tab">\n          ')

                # <Static value=<ast.Dict object at 0x7fbde28eb5b0> name=None at 7fbde28eb8e0> -> __attrs_140453435639696
                __attrs_140453435639696 = _static_140453526549936

                # <h2 ... (0:0)
                # --------------------------------------------------------
                __append('<h2>')
                __stream_140453435639216 = []
                __append_140453435639216 = __stream_140453435639216.append
                __append_140453435639216('Records')
                __msgid_140453435639216 = __re_whitespace(''.join(__stream_140453435639216)).strip()
                if 'heading_records':
                    __append(translate('heading_records', mapping=None, default=__msgid_140453435639216, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</h2>\n          ')

                # <Static value=<ast.Dict object at 0x7fbddd238d30> name=None at 7fbddd238970> -> __attrs_140453435641184
                __attrs_140453435641184 = _static_140453435641136

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div id="recordsTable" class="pat-registry">\n\n            ')

                # <Static value=<ast.Dict object at 0x7fbddd239120> name=None at 7fbddd239150> -> __attrs_140453435642528
                __attrs_140453435642528 = _static_140453435642144

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div id="searchrow">\n\n                ')

                # <Static value=<ast.Dict object at 0x7fbddd239630> name=None at 7fbddd239660> -> __attrs_140453435643872
                __attrs_140453435643872 = _static_140453435643440
                __backup_qp_140453439303408 = get('qp', __marker)

                # <Value 'request/qp|nothing' (36:37)> -> __value
                __token = 1430
                try:
                    __zt_tmp = __attrs_140453435643872
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140453526790704('path', 'request/qp|nothing', econtext=econtext)(_static_140453526790416(econtext, __zt_tmp))
                econtext['qp'] = __value
                __backup_q_140453439361696 = get('q', __marker)

                # <Value 'request/q|nothing' (37:35)> -> __value
                __token = 1485
                try:
                    __zt_tmp = __attrs_140453435643872
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140453526790704('path', 'request/q|nothing', econtext=econtext)(_static_140453526790416(econtext, __zt_tmp))
                econtext['q'] = __value

                # <form ... (0:0)
                # --------------------------------------------------------
                __append('<form id="registry-filter">\n\n                  ')

                # <Static value=<ast.Dict object at 0x7fbddd239db0> name=None at 7fbddd239de0> -> __attrs_140453435645744
                __attrs_140453435645744 = _static_140453435645360

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="mb-3">\n                    ')

                # <Static value=<ast.Dict object at 0x7fbddd23a320> name=None at 7fbddd23a350> -> __attrs_140453435647136
                __attrs_140453435647136 = _static_140453435646752

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="input-group">\n                      ')

                # <Static value=<ast.Dict object at 0x7fbddd23ae30> name=None at 7fbddd23ae60> -> __attrs_140453435649920
                __attrs_140453435649920 = _static_140453435649584

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input class="form-control" name="q" id="q"')

                # <Symbol value=<DEFAULT> at 7fbde28a8340> -> __default_140453435648432
                __default_140453435648432 = _DEFAULT_MARKER

                # <Translate msgid=None node=<ast.Constant object at 0x7fbddd23aa70> at 7fbddd23aa40> -> __attr_placeholder
                __attr_placeholder = 'filter by...'
                __attr_placeholder = translate(__attr_placeholder, default=__attr_placeholder, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                if (__attr_placeholder is not None):
                    __append((' placeholder="%s"' % __attr_placeholder))

                # <Symbol value=<DEFAULT> at 7fbde28a8340> -> __default_140453435648048
                __default_140453435648048 = _DEFAULT_MARKER

                # <Substitution 'python: qp or q' (45:46)> -> __attr_value
                __token = 1853
                try:
                    __zt_tmp = __attrs_140453435649920
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_140453526790704('python', ' qp or q', econtext=econtext)(_static_140453526790416(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append(' />\n                      ')

                # <Static value=<ast.Dict object at 0x7fbddd23b250> name=None at 7fbddd23b280> -> __attrs_140453435651072
                __attrs_140453435651072 = _static_140453435650640

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="input-group-append">\n                        ')

                # <Static value=<ast.Dict object at 0x7fbddd23ba00> name=None at 7fbddd23ba30> -> __attrs_140453435653328
                __attrs_140453435653328 = _static_140453435652608

                # <button ... (0:0)
                # --------------------------------------------------------
                __append('<button class="btn btn-primary" type="submit"')

                # <Symbol value=<DEFAULT> at 7fbde28a8340> -> __default_140453435652800
                __default_140453435652800 = _DEFAULT_MARKER

                # <Translate msgid=None node=<ast.Constant object at 0x7fbddd23b790> at 7fbddd23b760> -> __attr_value
                __attr_value = 'Filter'
                __attr_value = translate(__attr_value, default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append('>')
                __stream_140453435651696 = []
                __append_140453435651696 = __stream_140453435651696.append
                __append_140453435651696('\n                          Filter\n                        ')
                __msgid_140453435651696 = __re_whitespace(''.join(__stream_140453435651696)).strip()
                if __msgid_140453435651696:
                    __append(translate(__msgid_140453435651696, mapping=None, default=__msgid_140453435651696, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</button>\n                      </div>\n                    </div>\n                  </div>\n\n                  ')

                # <Static value=<ast.Dict object at 0x7fbddd23bf70> name=None at 7fbddd23b460> -> __attrs_140453435687168
                __attrs_140453435687168 = _static_140453435654000

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="row justify-content-between">\n                    ')

                # <Static value=<ast.Dict object at 0x7fbddd2444c0> name=None at 7fbddd2444f0> -> __attrs_140453435688512
                __attrs_140453435688512 = _static_140453435688128

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="mb-3 col-auto">\n                      ')

                # <Static value=<ast.Dict object at 0x7fbddd244a00> name=None at 7fbddd244a30> -> __attrs_140453435689856
                __attrs_140453435689856 = _static_140453435689472

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="input-group">\n                        ')

                # <Static value=<ast.Dict object at 0x7fbddd244fd0> name=None at 7fbddd244e50> -> __attrs_140453435691296
                __attrs_140453435691296 = _static_140453435690960

                # <label ... (0:0)
                # --------------------------------------------------------
                __append('<label class="col-form-label me-2">')
                __stream_140453435690432 = []
                __append_140453435690432 = __stream_140453435690432.append
                __append_140453435690432('or')
                __msgid_140453435690432 = __re_whitespace(''.join(__stream_140453435690432)).strip()
                if 'or':
                    __append(translate('or', mapping=None, default=__msgid_140453435690432, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</label>\n                        ')

                # <Static value=<ast.Dict object at 0x7fbddd2456f0> name=None at 7fbddd245330> -> __attrs_140453435692976
                __attrs_140453435692976 = _static_140453435692784
                __backup_prefixes_140453435646080 = get('prefixes', __marker)

                # <Value 'python: sorted(view.prefixes.keys())' (64:47)> -> __value
                __token = 2690
                try:
                    __zt_tmp = __attrs_140453435692976
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140453526790704('python', ' sorted(view.prefixes.keys())', econtext=econtext)(_static_140453526790416(econtext, __zt_tmp))
                econtext['prefixes'] = __value

                # <select ... (0:0)
                # --------------------------------------------------------
                __append('<select class="form-select" name="qp">\n                          ')

                # <Static value=<ast.Dict object at 0x7fbddd245c60> name=None at 7fbddd245c90> -> __attrs_140453435694560
                __attrs_140453435694560 = _static_140453435694176

                # <option ... (0:0)
                # --------------------------------------------------------
                __append('<option value="">')
                __stream_140453435693696 = []
                __append_140453435693696 = __stream_140453435693696.append
                __append_140453435693696('Select Prefix')
                __msgid_140453435693696 = __re_whitespace(''.join(__stream_140453435693696)).strip()
                if 'select_prefix':
                    __append(translate('select_prefix', mapping=None, default=__msgid_140453435693696, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</option>\n                          ')

                # <Static value=<ast.Dict object at 0x7fbde28eb5b0> name=None at 7fbde28eb8e0> -> __attrs_140453435695376
                __attrs_140453435695376 = _static_140453526549936
                __backup_prefix_140453435653664 = get('prefix', __marker)

                # <Value 'prefixes' (66:59)> -> __iterator
                __token = 2885
                try:
                    __zt_tmp = __attrs_140453435695376
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140453526790704('path', 'prefixes', econtext=econtext)(_static_140453526790416(econtext, __zt_tmp))
                (__iterator, ____index_140453435695664, ) = getname('repeat')('prefix', __iterator)
                econtext['prefix'] = None
                for __item in __iterator:
                    econtext['prefix'] = __item
                    __append('\n                            ')

                    # <Static value=<ast.Dict object at 0x7fbddd246860> name=None at 7fbddd246890> -> __attrs_140453435697776
                    __attrs_140453435697776 = _static_140453435697248
                    __backup_value_140453435693408 = get('value', __marker)

                    # <Value "python: 'prefix:' + (view.prefixes[prefix] or '')" (68:48)> -> __value
                    __token = 2980
                    try:
                        __zt_tmp = __attrs_140453435697776
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140453526790704('python', " 'prefix:' + (view.prefixes[prefix] or '')", econtext=econtext)(_static_140453526790416(econtext, __zt_tmp))
                    econtext['value'] = __value

                    # <option ... (0:0)
                    # --------------------------------------------------------
                    __append('<option')

                    # <Symbol value=<DEFAULT> at 7fbde28a8340> -> __default_140453435696912
                    __default_140453435696912 = _DEFAULT_MARKER

                    # <Substitution 'value' (69:52)> -> __attr_value
                    __token = 3083
                    try:
                        __zt_tmp = __attrs_140453435697776
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_140453526790704('path', 'value', econtext=econtext)(_static_140453526790416(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append('>')

                    # <Symbol value=<DEFAULT> at 7fbde28a8340> -> __default_140453435696672
                    __default_140453435696672 = _DEFAULT_MARKER

                    # <Value 'prefix' (70:43)> -> __cache_140453435696192
                    __token = 3134
                    try:
                        __zt_tmp = __attrs_140453435697776
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140453435696192 = _static_140453526790704('path', 'prefix', econtext=econtext)(_static_140453526790416(econtext, __zt_tmp))

                    # <BinOp left=<Value 'prefix' (70:43)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fbde28a8340> at 7fbddd246500> -> __condition
                    __expression = __cache_140453435696192

                    # <Symbol value=<DEFAULT> at 7fbde28a8340> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140453435696192
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</option>')
                    if (__backup_value_140453435693408 is __marker):
                        del econtext['value']
                    else:
                        econtext['value'] = __backup_value_140453435693408
                    __append('\n                          ')
                    ____index_140453435695664 -= 1
                    if (____index_140453435695664 > 0):
                        __append('')
                if (__backup_prefix_140453435653664 is __marker):
                    del econtext['prefix']
                else:
                    econtext['prefix'] = __backup_prefix_140453435653664
                __append('\n                        </select>')
                if (__backup_prefixes_140453435646080 is __marker):
                    del econtext['prefixes']
                else:
                    econtext['prefixes'] = __backup_prefixes_140453435646080
                __append('\n                      </div>\n                    </div>\n                    ')

                # <Static value=<ast.Dict object at 0x7fbddd246200> name=None at 7fbddd246350> -> __attrs_140453435698496
                __attrs_140453435698496 = _static_140453435695616

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="mb-3 col-auto">\n                      ')

                # <Static value=<ast.Dict object at 0x7fbddd247100> name=None at 7fbddd247130> -> __attrs_140453435699840
                __attrs_140453435699840 = _static_140453435699456

                # <form ... (0:0)
                # --------------------------------------------------------
                __append('<form id="clear-filter">\n                          ')

                # <Static value=<ast.Dict object at 0x7fbddd2478b0> name=None at 7fbddd247520> -> __attrs_140453435701520
                __attrs_140453435701520 = _static_140453435701424

                # <button ... (0:0)
                # --------------------------------------------------------
                __append('<button class="btn btn-secondary" type="reset">')
                __stream_140453435700416 = []
                __append_140453435700416 = __stream_140453435700416.append
                __append_140453435700416('\n                              Clear filter\n                          ')
                __msgid_140453435700416 = __re_whitespace(''.join(__stream_140453435700416)).strip()
                if 'clear_filter':
                    __append(translate('clear_filter', mapping=None, default=__msgid_140453435700416, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</button>\n                      </form>\n                    </div>\n                  </div>\n\n                </form>')
                if (__backup_q_140453439361696 is __marker):
                    del econtext['q']
                else:
                    econtext['q'] = __backup_q_140453439361696
                if (__backup_qp_140453439303408 is __marker):
                    del econtext['qp']
                else:
                    econtext['qp'] = __backup_qp_140453439303408
                __append('\n\n\n            </div>\n\n          ')

                # <Static value=<ast.Dict object at 0x7fbddd247a60> name=None at 7fbddd247a90> -> __attrs_140453435702288
                __attrs_140453435702288 = _static_140453435701856

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="table-responsive">\n          ')

                # <Static value=<ast.Dict object at 0x7fbddd247fd0> name=None at 7fbddd247e50> -> __attrs_140453435736464
                __attrs_140453435736464 = _static_140453435703248

                # <table ... (0:0)
                # --------------------------------------------------------
                __append('<table class="table table-bordered table-striped">\n              ')

                # <Static value=<ast.Dict object at 0x7fbde28eb5b0> name=None at 7fbde28eb8e0> -> __attrs_140453435737424
                __attrs_140453435737424 = _static_140453526549936

                # <thead ... (0:0)
                # --------------------------------------------------------
                __append('<thead>\n                  ')

                # <Static value=<ast.Dict object at 0x7fbde28eb5b0> name=None at 7fbde28eb8e0> -> __attrs_140453435738384
                __attrs_140453435738384 = _static_140453526549936

                # <tr ... (0:0)
                # --------------------------------------------------------
                __append('<tr>\n                      ')

                # <Static value=<ast.Dict object at 0x7fbde28eb5b0> name=None at 7fbde28eb8e0> -> __attrs_140453435739440
                __attrs_140453435739440 = _static_140453526549936

                # <th ... (0:0)
                # --------------------------------------------------------
                __append('<th>')
                __stream_140453435738960 = []
                __append_140453435738960 = __stream_140453435738960.append
                __append_140453435738960('Name')
                __msgid_140453435738960 = __re_whitespace(''.join(__stream_140453435738960)).strip()
                if 'heading_name':
                    __append(translate('heading_name', mapping=None, default=__msgid_140453435738960, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</th>\n                      ')

                # <Static value=<ast.Dict object at 0x7fbde28eb5b0> name=None at 7fbde28eb8e0> -> __attrs_140453435740400
                __attrs_140453435740400 = _static_140453526549936

                # <th ... (0:0)
                # --------------------------------------------------------
                __append('<th>')
                __stream_140453435739920 = []
                __append_140453435739920 = __stream_140453435739920.append
                __append_140453435739920('Title')
                __msgid_140453435739920 = __re_whitespace(''.join(__stream_140453435739920)).strip()
                if 'heading_title':
                    __append(translate('heading_title', mapping=None, default=__msgid_140453435739920, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</th>\n                      ')

                # <Static value=<ast.Dict object at 0x7fbde28eb5b0> name=None at 7fbde28eb8e0> -> __attrs_140453435741360
                __attrs_140453435741360 = _static_140453526549936

                # <th ... (0:0)
                # --------------------------------------------------------
                __append('<th>')
                __stream_140453435740880 = []
                __append_140453435740880 = __stream_140453435740880.append
                __append_140453435740880('Description')
                __msgid_140453435740880 = __re_whitespace(''.join(__stream_140453435740880)).strip()
                if 'heading_description':
                    __append(translate('heading_description', mapping=None, default=__msgid_140453435740880, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</th>\n                      ')

                # <Static value=<ast.Dict object at 0x7fbde28eb5b0> name=None at 7fbde28eb8e0> -> __attrs_140453435742320
                __attrs_140453435742320 = _static_140453526549936

                # <th ... (0:0)
                # --------------------------------------------------------
                __append('<th>')
                __stream_140453435741840 = []
                __append_140453435741840 = __stream_140453435741840.append
                __append_140453435741840('Type')
                __msgid_140453435741840 = __re_whitespace(''.join(__stream_140453435741840)).strip()
                if 'heading_type':
                    __append(translate('heading_type', mapping=None, default=__msgid_140453435741840, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</th>\n                      ')

                # <Static value=<ast.Dict object at 0x7fbde28eb5b0> name=None at 7fbde28eb8e0> -> __attrs_140453435743280
                __attrs_140453435743280 = _static_140453526549936

                # <th ... (0:0)
                # --------------------------------------------------------
                __append('<th>')
                __stream_140453435742800 = []
                __append_140453435742800 = __stream_140453435742800.append
                __append_140453435742800('Value')
                __msgid_140453435742800 = __re_whitespace(''.join(__stream_140453435742800)).strip()
                if 'heading_value':
                    __append(translate('heading_value', mapping=None, default=__msgid_140453435742800, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</th>\n                  </tr>\n              </thead>\n              ')

                # <Static value=<ast.Dict object at 0x7fbde28eb5b0> name=None at 7fbde28eb8e0> -> __attrs_140453435743952
                __attrs_140453435743952 = _static_140453526549936

                # <tbody ... (0:0)
                # --------------------------------------------------------
                __append('<tbody>\n                  ')

                # <Static value=<ast.Dict object at 0x7fbde28eb5b0> name=None at 7fbde28eb8e0> -> __attrs_140453435744816
                __attrs_140453435744816 = _static_140453526549936
                __backup_record_140453435644688 = get('record', __marker)

                # <Value 'records' (103:43)> -> __iterator
                __token = 4346
                try:
                    __zt_tmp = __attrs_140453435744816
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140453526790704('path', 'records', econtext=econtext)(_static_140453526790416(econtext, __zt_tmp))
                (__iterator, ____index_140453435745056, ) = getname('repeat')('record', __iterator)
                econtext['record'] = None
                for __item in __iterator:
                    econtext['record'] = __item
                    __append('\n                      ')

                    # <Static value=<ast.Dict object at 0x7fbddd252740> name=None at 7fbddd2525f0> -> __attrs_140453435746688
                    __attrs_140453435746688 = _static_140453435746112
                    __backup_oddrow_140453435647472 = get('oddrow', __marker)

                    # <Value 'repeat/record/odd' (104:45)> -> __value
                    __token = 4401
                    try:
                        __zt_tmp = __attrs_140453435746688
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140453526790704('path', 'repeat/record/odd', econtext=econtext)(_static_140453526790416(econtext, __zt_tmp))
                    econtext['oddrow'] = __value
                    __backup_field_140453435651408 = get('field', __marker)

                    # <Value 'record/field/originalField | record/field' (105:43)> -> __value
                    __token = 4463
                    try:
                        __zt_tmp = __attrs_140453435746688
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140453526790704('path', 'record/field/originalField | record/field', econtext=econtext)(_static_140453526790416(econtext, __zt_tmp))
                    econtext['field'] = __value

                    # <tr ... (0:0)
                    # --------------------------------------------------------
                    __append('<tr')

                    # <Symbol value=<DEFAULT> at 7fbde28a8340> -> __default_140453435745632
                    __default_140453435745632 = _DEFAULT_MARKER

                    # <Substitution "python:oddrow and 'odd' or 'even'" (106:48)> -> __attr_class
                    __token = 4555
                    try:
                        __zt_tmp = __attrs_140453435746688
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_140453526790704('python', "oddrow and 'odd' or 'even'", econtext=econtext)(_static_140453526790416(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((' class="%s"' % __attr_class))
                    __append('>\n                          ')

                    # <Static value=<ast.Dict object at 0x7fbddd252ef0> name=None at 7fbddd252f20> -> __attrs_140453435748464
                    __attrs_140453435748464 = _static_140453435748080

                    # <td ... (0:0)
                    # --------------------------------------------------------
                    __append('<td data-label="Name">\n                              ')

                    # <Static value=<ast.Dict object at 0x7fbddd2538e0> name=None at 7fbddd3e4d30> -> __attrs_140453435750960
                    __attrs_140453435750960 = _static_140453435750624

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a class="recordsEditLink"')

                    # <Symbol value=<DEFAULT> at 7fbde28a8340> -> __default_140453435750096
                    __default_140453435750096 = _DEFAULT_MARKER

                    # <Substitution 'string:${context/absolute_url}/edit/${record/__name__}' (110:54)> -> __attr_href
                    __token = 4839
                    try:
                        __zt_tmp = __attrs_140453435750960
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140453526790704('string', '${context/absolute_url}/edit/${record/__name__}', econtext=econtext)(_static_140453526790416(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))
                    __append('>')

                    # <Symbol value=<DEFAULT> at 7fbde28a8340> -> __default_140453435749664
                    __default_140453435749664 = _DEFAULT_MARKER

                    # <Value "python:record.__name__.replace('.', ' ')" (109:46)> -> __cache_140453435749136
                    __token = 4743
                    try:
                        __zt_tmp = __attrs_140453435750960
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140453435749136 = _static_140453526790704('python', "record.__name__.replace('.', ' ')", econtext=econtext)(_static_140453526790416(econtext, __zt_tmp))

                    # <BinOp left=<Value "python:record.__name__.replace('.', ' ')" (109:46)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fbde28a8340> at 7fbddd253400> -> __condition
                    __expression = __cache_140453435749136

                    # <Symbol value=<DEFAULT> at 7fbde28a8340> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140453435749136
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</a>\n                          </td>\n                          ')

                    # <Static value=<ast.Dict object at 0x7fbddd253f70> name=None at 7fbddd253fa0> -> __attrs_140453435769136
                    __attrs_140453435769136 = _static_140453435752304

                    # <td ... (0:0)
                    # --------------------------------------------------------
                    __append('<td data-label="Title">')

                    # <Symbol value=<DEFAULT> at 7fbde28a8340> -> __default_140453435751728
                    __default_140453435751728 = _DEFAULT_MARKER

                    # <Value 'field/title' (113:43)> -> __cache_140453435751248
                    __token = 5006
                    try:
                        __zt_tmp = __attrs_140453435769136
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140453435751248 = _static_140453526790704('path', 'field/title', econtext=econtext)(_static_140453526790416(econtext, __zt_tmp))

                    # <BinOp left=<Value 'field/title' (113:43)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fbde28a8340> at 7fbddd253c10> -> __condition
                    __expression = __cache_140453435751248

                    # <Symbol value=<DEFAULT> at 7fbde28a8340> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140453435751248
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</td>\n                          ')

                    # <Static value=<ast.Dict object at 0x7fbddd2586d0> name=None at 7fbddd258700> -> __attrs_140453435770960
                    __attrs_140453435770960 = _static_140453435770576

                    # <td ... (0:0)
                    # --------------------------------------------------------
                    __append('<td data-label="Description">')

                    # <Symbol value=<DEFAULT> at 7fbde28a8340> -> __default_140453435770000
                    __default_140453435770000 = _DEFAULT_MARKER

                    # <Value 'field/description' (114:53)> -> __cache_140453435769520
                    __token = 5094
                    try:
                        __zt_tmp = __attrs_140453435770960
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140453435769520 = _static_140453526790704('path', 'field/description', econtext=econtext)(_static_140453526790416(econtext, __zt_tmp))

                    # <BinOp left=<Value 'field/description' (114:53)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fbde28a8340> at 7fbddd258370> -> __condition
                    __expression = __cache_140453435769520

                    # <Symbol value=<DEFAULT> at 7fbde28a8340> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140453435769520
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('</td>\n                          ')

                    # <Static value=<ast.Dict object at 0x7fbddd258df0> name=None at 7fbddd258e20> -> __attrs_140453435772784
                    __attrs_140453435772784 = _static_140453435772400

                    # <td ... (0:0)
                    # --------------------------------------------------------
                    __append('<td data-label="Type">')

                    # <Symbol value=<DEFAULT> at 7fbde28a8340> -> __default_140453435771824
                    __default_140453435771824 = _DEFAULT_MARKER

                    # <Value 'field/__class__/__name__' (115:43)> -> __cache_140453435771344
                    __token = 5184
                    try:
                        __zt_tmp = __attrs_140453435772784
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140453435771344 = _static_140453526790704('path', 'field/__class__/__name__', econtext=econtext)(_static_140453526790416(econtext, __zt_tmp))

                    # <BinOp left=<Value 'field/__class__/__name__' (115:43)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fbde28a8340> at 7fbddd258a90> -> __condition
                    __expression = __cache_140453435771344

                    # <Symbol value=<DEFAULT> at 7fbde28a8340> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140453435771344
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</td>\n                          ')

                    # <Static value=<ast.Dict object at 0x7fbddd259270> name=None at 7fbddd2592a0> -> __attrs_140453435773936
                    __attrs_140453435773936 = _static_140453435773552

                    # <td ... (0:0)
                    # --------------------------------------------------------
                    __append('<td data-label="Value">\n                            ')
                    ____fallback_140453526372272 = len(__stream)
                    try:

                        # <Static value=<ast.Dict object at 0x7fbddd259a50> name=None at 7fbddd259a80> -> __attrs_140453435775952
                        __attrs_140453435775952 = _static_140453435775568

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="value">')

                        # <Symbol value=<DEFAULT> at 7fbde28a8340> -> __default_140453435774992
                        __default_140453435774992 = _DEFAULT_MARKER

                        # <Value 'record/value|nothing' (117:47)> -> __cache_140453435774512
                        __token = 5328
                        try:
                            __zt_tmp = __attrs_140453435775952
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140453435774512 = _static_140453526790704('path', 'record/value|nothing', econtext=econtext)(_static_140453526790416(econtext, __zt_tmp))

                        # <BinOp left=<Value 'record/value|nothing' (117:47)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fbde28a8340> at 7fbddd2596f0> -> __condition
                        __expression = __cache_140453435774512

                        # <Symbol value=<DEFAULT> at 7fbde28a8340> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140453435774512
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</span>')
                    except (Exception, ) as __exc:
                        econtext['error'] = _ErrorInfo(__exc, __tokens[__token][1:3])
                        if (on_error_handler is not None):
                            on_error_handler(__exc)
                        del __stream[____fallback_140453526372272:]

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="value">')

                        # <Value 'string:?' (118:48)> -> __content
                        __token = 5398
                        try:
                            __zt_tmp = __attrs_140453435773936
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __content = _static_140453526790704('string', '?', econtext=econtext)(_static_140453526790416(econtext, __zt_tmp))
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                        __append('</span>')

                    __append('\n                            ')

                    # <Static value=<ast.Dict object at 0x7fbde28eb5b0> name=None at 7fbde28eb8e0> -> __attrs_140453435777296
                    __attrs_140453435777296 = _static_140453526549936

                    # <Value 'not: record/interfaceName|nothing' (120:58)> -> __condition
                    __token = 5516
                    try:
                        __zt_tmp = __attrs_140453435777296
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140453526790704('not', ' record/interfaceName|nothing', econtext=econtext)(_static_140453526790416(econtext, __zt_tmp))
                    if __condition:
                        __append('\n                              ')

                        # <Static value=<ast.Dict object at 0x7fbde28eb5b0> name=None at 7fbde28eb8e0> -> __attrs_140453435778400
                        __attrs_140453435778400 = _static_140453526549936

                        # <br ... (0:0)
                        # --------------------------------------------------------
                        __append('<br />\n                             (')

                        # <Static value=<ast.Dict object at 0x7fbddd25aa40> name=None at 7fbddd25aa70> -> __attrs_140453435780128
                        __attrs_140453435780128 = _static_140453435779648

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append('<a')

                        # <Symbol value=<DEFAULT> at 7fbde28a8340> -> __default_140453435779168
                        __default_140453435779168 = _DEFAULT_MARKER

                        # <Interpolation value=<Substitution '${context/absolute_url}/@@delete-record?name=${record/__name__}' (122:39)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fbddd25a920> -> __attr_href
                        __token = 5628
                        __token = 5630
                        try:
                            __zt_tmp = __attrs_140453435780128
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_140453526790704('path', 'context/absolute_url', econtext=econtext)(_static_140453526790416(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                        __token = 5675
                        try:
                            __zt_tmp = __attrs_140453435780128
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href_5673 = _static_140453526790704('path', 'record/__name__', econtext=econtext)(_static_140453526790416(econtext, __zt_tmp))
                        __attr_href_5673 = __quote(__attr_href_5673, '"', '&quot;', None, _DEFAULT_MARKER)
                        __attr_href = ('%s%s%s' % ((__attr_href if (__attr_href is not None) else ''), '/@@delete-record?name=', (__attr_href_5673 if (__attr_href_5673 is not None) else ''), ))
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
                        __append(' class="recordsDeleteLink">')
                        __stream_140453435778784 = []
                        __append_140453435778784 = __stream_140453435778784.append
                        __append_140453435778784('\n                                 Delete record\n                              ')
                        __msgid_140453435778784 = __re_whitespace(''.join(__stream_140453435778784)).strip()
                        if __msgid_140453435778784:
                            __append(translate(__msgid_140453435778784, mapping=None, default=__msgid_140453435778784, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</a>)\n                            ')
                    __append('\n                          </td>\n                      </tr>')
                    if (__backup_field_140453435651408 is __marker):
                        del econtext['field']
                    else:
                        econtext['field'] = __backup_field_140453435651408
                    if (__backup_oddrow_140453435647472 is __marker):
                        del econtext['oddrow']
                    else:
                        econtext['oddrow'] = __backup_oddrow_140453435647472
                    __append('\n                  ')
                    ____index_140453435745056 -= 1
                    if (____index_140453435745056 > 0):
                        __append('')
                if (__backup_record_140453435644688 is __marker):
                    del econtext['record']
                else:
                    econtext['record'] = __backup_record_140453435644688
                __append('\n              </tbody>\n              ')

                # <Static value=<ast.Dict object at 0x7fbde28eb5b0> name=None at 7fbde28eb8e0> -> __attrs_140453435769232
                __attrs_140453435769232 = _static_140453526549936

                # <Value 'python: records.numpages > 1' (131:36)> -> __condition
                __token = 6048
                try:
                    __zt_tmp = __attrs_140453435769232
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140453526790704('python', ' records.numpages > 1', econtext=econtext)(_static_140453526790416(econtext, __zt_tmp))
                if __condition:

                    # <tfoot ... (0:0)
                    # --------------------------------------------------------
                    __append('<tfoot>\n                  ')

                    # <Static value=<ast.Dict object at 0x7fbde28eb5b0> name=None at 7fbde28eb8e0> -> __attrs_140453435781088
                    __attrs_140453435781088 = _static_140453526549936

                    # <tr ... (0:0)
                    # --------------------------------------------------------
                    __append('<tr>\n                      ')

                    # <Static value=<ast.Dict object at 0x7fbddd25b3a0> name=None at 7fbddd25b3d0> -> __attrs_140453435782432
                    __attrs_140453435782432 = _static_140453435782048
                    __backup_batch_140453435695568 = get('batch', __marker)

                    # <Value 'records' (133:56)> -> __value
                    __token = 6158
                    try:
                        __zt_tmp = __attrs_140453435782432
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140453526790704('path', 'records', econtext=econtext)(_static_140453526790416(econtext, __zt_tmp))
                    econtext['batch'] = __value

                    # <th ... (0:0)
                    # --------------------------------------------------------
                    __append('<th colspan="5">\n                          ')

                    # <Static value=<ast.Dict object at 0x7fbde28eb5b0> name=None at 7fbde28eb8e0> -> __attrs_140453435783680
                    __attrs_140453435783680 = _static_140453526549936
                    __backup_macroname_140453435801408 = get('macroname', __marker)

                    # <Static value=<ast.Constant object at 0x7fbddd25b8b0> name=None at 7fbddd25b8e0> -> __value
                    __value = _static_140453435783344
                    econtext['macroname'] = __value

                    # <Value 'here/batch_macros/macros/navigation' (134:48)> -> __macro
                    __token = 6216
                    try:
                        __zt_tmp = __attrs_140453435783680
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __macro = _static_140453526790704('path', 'here/batch_macros/macros/navigation', econtext=econtext)(_static_140453526790416(econtext, __zt_tmp))
                    __token = 6216
                    __m = __macro.include
                    __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                    econtext.update(rcontext)
                    if (__backup_macroname_140453435801408 is __marker):
                        del econtext['macroname']
                    else:
                        econtext['macroname'] = __backup_macroname_140453435801408
                    __append('\n                      </th>')
                    if (__backup_batch_140453435695568 is __marker):
                        del econtext['batch']
                    else:
                        econtext['batch'] = __backup_batch_140453435695568
                    __append('\n                  </tr>\n              </tfoot>')
                __append('\n          </table>\n          </div>\n        </div>\n        </div>\n        ')

                # <Static value=<ast.Dict object at 0x7fbddd247d60> name=None at 7fbddd2502e0> -> __attrs_140453435784160
                __attrs_140453435784160 = _static_140453435702624

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="tab">\n          ')

                # <Static value=<ast.Dict object at 0x7fbde28eb5b0> name=None at 7fbde28eb8e0> -> __attrs_140453435818048
                __attrs_140453435818048 = _static_140453526549936

                # <h2 ... (0:0)
                # --------------------------------------------------------
                __append('<h2>')
                __stream_140453435784736 = []
                __append_140453435784736 = __stream_140453435784736.append
                __append_140453435784736('Export')
                __msgid_140453435784736 = __re_whitespace(''.join(__stream_140453435784736)).strip()
                if 'export':
                    __append(translate('export', mapping=None, default=__msgid_140453435784736, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</h2>\n          ')

                # <Static value=<ast.Dict object at 0x7fbde28eb5b0> name=None at 7fbde28eb8e0> -> __attrs_140453435819008
                __attrs_140453435819008 = _static_140453526549936

                # <p ... (0:0)
                # --------------------------------------------------------
                __append('<p>')
                __stream_140453435818528 = []
                __append_140453435818528 = __stream_140453435818528.append
                __append_140453435818528('Will export the entire registry into a single XML file.')
                __msgid_140453435818528 = __re_whitespace(''.join(__stream_140453435818528)).strip()
                if 'registry_export_text':
                    __append(translate('registry_export_text', mapping=None, default=__msgid_140453435818528, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</p>\n          ')

                # <Static value=<ast.Dict object at 0x7fbddd264760> name=None at 7fbddd264790> -> __attrs_140453435820256
                __attrs_140453435820256 = _static_140453435819872

                # <form ... (0:0)
                # --------------------------------------------------------
                __append('<form method="POST">\n            ')

                # <Static value=<ast.Dict object at 0x7fbddd264e50> name=None at 7fbddd264e80> -> __attrs_140453435821984
                __attrs_140453435821984 = _static_140453435821648

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="hidden" name="button.exportregistry" value="true"/>\n            ')

                # <Static value=<ast.Dict object at 0x7fbddd2652a0> name=None at 7fbddd2652d0> -> __attrs_140453435823136
                __attrs_140453435823136 = _static_140453435822752

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="formControls">\n              ')

                # <Static value=<ast.Dict object at 0x7fbddd265a50> name=None at 7fbddd2656c0> -> __attrs_140453435824816
                __attrs_140453435824816 = _static_140453435824720

                # <button ... (0:0)
                # --------------------------------------------------------
                __append('<button class="btn btn-primary" type="submit">')
                __stream_140453435823712 = []
                __append_140453435823712 = __stream_140453435823712.append
                __append_140453435823712('Export Now')
                __msgid_140453435823712 = __re_whitespace(''.join(__stream_140453435823712)).strip()
                if 'export_button':
                    __append(translate('export_button', mapping=None, default=__msgid_140453435823712, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</button>\n            </div>\n          </form>\n          ')

                # <Static value=<ast.Dict object at 0x7fbde28eb5b0> name=None at 7fbde28eb8e0> -> __attrs_140453435825392
                __attrs_140453435825392 = _static_140453526549936

                # <hr ... (0:0)
                # --------------------------------------------------------
                __append('<hr />\n          ')

                # <Static value=<ast.Dict object at 0x7fbde28eb5b0> name=None at 7fbde28eb8e0> -> __attrs_140453435826736
                __attrs_140453435826736 = _static_140453526549936

                # <Symbol value=<DEFAULT> at 7fbde28a8340> -> __default_140453435826544
                __default_140453435826544 = _DEFAULT_MARKER

                # <Value "python:context.restrictedTraverse('@@configuration_registry_export_xml')()" (152:38)> -> __cache_140453435826064
                __token = 6934
                try:
                    __zt_tmp = __attrs_140453435826736
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140453435826064 = _static_140453526790704('python', "context.restrictedTraverse('@@configuration_registry_export_xml')()", econtext=econtext)(_static_140453526790416(econtext, __zt_tmp))

                # <BinOp left=<Value "python:context.restrictedTraverse('@@configuration_registry_export_xml')()" (152:38)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fbde28a8340> at 7fbddd266050> -> __condition
                __expression = __cache_140453435826064

                # <Symbol value=<DEFAULT> at 7fbde28a8340> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div />')
                else:
                    __content = __cache_140453435826064
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n        </div>\n        ')

                # <Static value=<ast.Dict object at 0x7fbddd2664d0> name=None at 7fbddd266500> -> __attrs_140453435827792
                __attrs_140453435827792 = _static_140453435827408

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="tab">\n          ')

                # <Static value=<ast.Dict object at 0x7fbde28eb5b0> name=None at 7fbde28eb8e0> -> __attrs_140453435828848
                __attrs_140453435828848 = _static_140453526549936

                # <h2 ... (0:0)
                # --------------------------------------------------------
                __append('<h2>')
                __stream_140453435828368 = []
                __append_140453435828368 = __stream_140453435828368.append
                __append_140453435828368('Import')
                __msgid_140453435828368 = __re_whitespace(''.join(__stream_140453435828368)).strip()
                if 'import':
                    __append(translate('import', mapping=None, default=__msgid_140453435828368, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</h2>\n          ')

                # <Static value=<ast.Dict object at 0x7fbddd266f80> name=None at 7fbddd266fb0> -> __attrs_140453435830336
                __attrs_140453435830336 = _static_140453435830144

                # <form ... (0:0)
                # --------------------------------------------------------
                __append('<form method="POST" enctype=\'multipart/form-data\'>\n            ')

                # <Static value=<ast.Dict object at 0x7fbddd267400> name=None at 7fbddd267430> -> __attrs_140453435831680
                __attrs_140453435831680 = _static_140453435831296

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="mb-3 field">\n              ')

                # <Static value=<ast.Dict object at 0x7fbddd267be0> name=None at 7fbddd267820> -> __attrs_140453435833360
                __attrs_140453435833360 = _static_140453435833312

                # <label ... (0:0)
                # --------------------------------------------------------
                __append('<label for="exportFile" class="form-label">')
                __stream_140453435832256 = []
                __append_140453435832256 = __stream_140453435832256.append
                __append_140453435832256('Registry XML File')
                __msgid_140453435832256 = __re_whitespace(''.join(__stream_140453435832256)).strip()
                if __msgid_140453435832256:
                    __append(translate(__msgid_140453435832256, mapping=None, default=__msgid_140453435832256, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</label>\n              ')

                # <Static value=<ast.Dict object at 0x7fbddd267f70> name=None at 7fbddd267fa0> -> __attrs_140453435867920
                __attrs_140453435867920 = _static_140453435834224

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="file" name="file" id="exportFile" class="form-control" />\n            </div>\n            ')

                # <Static value=<ast.Dict object at 0x7fbddd2707f0> name=None at 7fbddd270820> -> __attrs_140453435869504
                __attrs_140453435869504 = _static_140453435869168

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="hidden" name="button.importregistry" value="true"/>\n            ')

                # <Static value=<ast.Dict object at 0x7fbddd270c10> name=None at 7fbddd270c40> -> __attrs_140453435870656
                __attrs_140453435870656 = _static_140453435870224

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="formControls mt-3">\n              ')

                # <Static value=<ast.Dict object at 0x7fbddd2713f0> name=None at 7fbddd271060> -> __attrs_140453435872336
                __attrs_140453435872336 = _static_140453435872240

                # <button ... (0:0)
                # --------------------------------------------------------
                __append('<button class="btn btn-primary" type="submit">')
                __stream_140453435871232 = []
                __append_140453435871232 = __stream_140453435871232.append
                __append_140453435871232('Import File')
                __msgid_140453435871232 = __re_whitespace(''.join(__stream_140453435871232)).strip()
                if 'import_button':
                    __append(translate('import_button', mapping=None, default=__msgid_140453435871232, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</button>\n            </div>\n          </form>\n        </div>\n        ')

                # <Static value=<ast.Dict object at 0x7fbddd271690> name=None at 7fbddd2716c0> -> __attrs_140453435873296
                __attrs_140453435873296 = _static_140453435872912

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="tab">\n          ')

                # <Static value=<ast.Dict object at 0x7fbde28eb5b0> name=None at 7fbde28eb8e0> -> __attrs_140453435874352
                __attrs_140453435874352 = _static_140453526549936

                # <h2 ... (0:0)
                # --------------------------------------------------------
                __append('<h2>')
                __stream_140453435873872 = []
                __append_140453435873872 = __stream_140453435873872.append
                __append_140453435873872('Add new record')
                __msgid_140453435873872 = __re_whitespace(''.join(__stream_140453435873872)).strip()
                if 'registry_add_record_label':
                    __append(translate('registry_add_record_label', mapping=None, default=__msgid_140453435873872, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</h2>\n          ')

                # <Static value=<ast.Dict object at 0x7fbde28eb5b0> name=None at 7fbde28eb8e0> -> __attrs_140453435875312
                __attrs_140453435875312 = _static_140453526549936

                # <p ... (0:0)
                # --------------------------------------------------------
                __append('<p>')
                __stream_140453435874832 = []
                __append_140453435874832 = __stream_140453435874832.append
                __msgid_140453435874832 = __re_whitespace(''.join(__stream_140453435874832)).strip()
                if 'registry_add_record_text':
                    __append(translate('registry_add_record_text', mapping=None, default=__msgid_140453435874832, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</p>\n          ')

                # <Static value=<ast.Dict object at 0x7fbde28eb5b0> name=None at 7fbde28eb8e0> -> __attrs_140453435876176
                __attrs_140453435876176 = _static_140453526549936
                __backup_macroname_140453435887488 = get('macroname', __marker)

                # <Static value=<ast.Constant object at 0x7fbddd272200> name=None at 7fbddd272230> -> __value
                __value = _static_140453435875840
                econtext['macroname'] = __value

                # <Value 'context/@@ploneform-macros/titlelessform' (170:34)> -> __macro
                __token = 7889
                try:
                    __zt_tmp = __attrs_140453435876176
                except get('NameError', NameError):
                    __zt_tmp = None

                __macro = _static_140453526790704('path', 'context/@@ploneform-macros/titlelessform', econtext=econtext)(_static_140453526790416(econtext, __zt_tmp))
                __token = 7889
                __m = __macro.include
                __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                if (__backup_macroname_140453435887488 is __marker):
                    del econtext['macroname']
                else:
                    econtext['macroname'] = __backup_macroname_140453435887488
                __append('\n        </div>\n      </div>\n    </div>\n</article>')
                if (__backup_records_140453439325184 is __marker):
                    del econtext['records']
                else:
                    econtext['records'] = __backup_records_140453439325184
            _slots = econtext['__slot_prefs_configlet_main'] = _deque((__fill_prefs_configlet_main, ))

            # <Value 'context/@@prefs_main_template/macros/master' (6:23)> -> __macro
            __token = 261
            try:
                __zt_tmp = __attrs_140453437395424
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140453526790704('path', 'context/@@prefs_main_template/macros/master', econtext=econtext)(_static_140453526790416(econtext, __zt_tmp))
            __token = 261
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140453481312640 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140453481312640
            __i18n_domain = __previous_i18n_domain_140453437395856
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }