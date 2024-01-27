# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/plone/app/dexterity/browser/behaviors.pt'

__tokens = {62: ('view/status', 3, 22), 95: ('view/status', 4, 20), 563: ('request/getURL', 25, 17), 596: (' view/enctyp', 26, 17), 657: ('view/widgets/values|nothing', 29, 32), 752: ('python: widget.field.__name__', 31, 34), 815: (' python: view.behaviors[behavior_name', 32, 32), 950: ('widget/error', 36, 21), 985: (" python:widget.mode == 'hidden", 37, 21), 1084: ("python:'mb-3 field' + (error and 'alert alert-warning' or '')", 40, 21), 1275: ('python:widget.required and not hidden', 46, 31), 1498: ('error', 53, 30), 1543: ('error/render', 54, 38), 1860: ('widget/render', 65, 50), 1992: ('behavior_name', 69, 35), 2083: ('python:behavior_reg.interface.__identifier__', 71, 35), 2245: ('widget/field/description', 74, 34), 2328: ('python:description and not hidden', 76, 35), 2499: ('description', 80, 39), 2823: ('context/@@ploneform-macros/actions', 95, 36), 2823: ('context/@@ploneform-macros/actions', 95, 36)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140097251390800 = 'actions'
_static_140097245720448 = {'class': 'form-text', }
_static_140097245721456 = {'colspan': '3', }
_static_140097245711808 = {'class': 'w-25', }
_static_140097339175504 = {'type': 'text', }
_static_140097247583040 = {'class': 'w-25', }
_static_140097247580016 = {'class': 'table table-borderless table-sm', }
_static_140097247591920 = {'class': 'widget', }
_static_140097247587072 = {'class': 'fieldRequired', 'title': 'Required', }
_static_140097251386528 = {'class': 'field', }
_static_140097251384224 = {'action': '.', 'method': 'post', 'enctype': 'view/enctype', }
_static_140097251381488 = {'class': 'w-25', }
_static_140097251378032 = {'class': 'w-25', }
_static_140097338360544 = {'class': 'table', }
_static_140097413192176 = __C2ZContextWrapper
_static_140097413192464 = __compile_zt_expr
_static_140097402060864 = {'class': 'portalMessage', }
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

            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097251866896
            __attrs_140097251866896 = _static_140097412968080
            __append('\n  ')

            # <Static value=<ast.Dict object at 0x7f6af7e24040> name=None at 7f6af7e25e10> -> __attrs_140097338371536
            __attrs_140097338371536 = _static_140097402060864

            # <Value 'view/status' (3:22)> -> __condition
            __token = 62
            try:
                __zt_tmp = __attrs_140097338371536
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140097413192464('path', 'view/status', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="portalMessage" >')

                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097402067008
                __default_140097402067008 = _DEFAULT_MARKER

                # <Value 'view/status' (4:20)> -> __cache_140097251862192
                __token = 95
                try:
                    __zt_tmp = __attrs_140097338371536
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140097251862192 = _static_140097413192464('path', 'view/status', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                # <BinOp left=<Value 'view/status' (4:20)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeeee7010> -> __condition
                __expression = __cache_140097251862192

                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140097251862192
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</div>')
            __append('\n\n  ')

            # <Static value=<ast.Dict object at 0x7f6af41642e0> name=None at 7f6af41656c0> -> __attrs_140097252061584
            __attrs_140097252061584 = _static_140097338360544

            # <table ... (0:0)
            # --------------------------------------------------------
            __append('<table class="table">\n    ')

            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097252063888
            __attrs_140097252063888 = _static_140097412968080

            # <thead ... (0:0)
            # --------------------------------------------------------
            __append('<thead>\n      ')

            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097338136736
            __attrs_140097338136736 = _static_140097412968080

            # <tr ... (0:0)
            # --------------------------------------------------------
            __append('<tr>\n        ')

            # <Static value=<ast.Dict object at 0x7f6aeee70370> name=None at 7f6aeee72a70> -> __attrs_140097251388784
            __attrs_140097251388784 = _static_140097251378032

            # <th ... (0:0)
            # --------------------------------------------------------
            __append('<th class="w-25">\n        </th>\n        ')

            # <Static value=<ast.Dict object at 0x7f6aeee710f0> name=None at 7f6aeee72950> -> __attrs_140097251393440
            __attrs_140097251393440 = _static_140097251381488

            # <th ... (0:0)
            # --------------------------------------------------------
            __append('<th class="w-25">\n          ')

            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097251388736
            __attrs_140097251388736 = _static_140097412968080

            # <span ... (0:0)
            # --------------------------------------------------------
            __append('<span>')
            __stream_140097251392960 = []
            __append_140097251392960 = __stream_140097251392960.append
            __append_140097251392960('Name of behavior')
            __msgid_140097251392960 = __re_whitespace(''.join(__stream_140097251392960)).strip()
            if 'label_name_of_behavior':
                __append(translate('label_name_of_behavior', mapping=None, default=__msgid_140097251392960, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</span>\n        </th>\n        ')

            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097251383648
            __attrs_140097251383648 = _static_140097412968080

            # <th ... (0:0)
            # --------------------------------------------------------
            __append('<th>\n          ')

            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097251378896
            __attrs_140097251378896 = _static_140097412968080

            # <span ... (0:0)
            # --------------------------------------------------------
            __append('<span>')
            __stream_140097251385568 = []
            __append_140097251385568 = __stream_140097251385568.append
            __append_140097251385568('Interface of behavior')
            __msgid_140097251385568 = __re_whitespace(''.join(__stream_140097251385568)).strip()
            if 'label_interface_of_behavior':
                __append(translate('label_interface_of_behavior', mapping=None, default=__msgid_140097251385568, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</span>\n        </th>\n      </tr>\n    </thead>\n  </table>\n\n  ')

            # <Static value=<ast.Dict object at 0x7f6aeee71ba0> name=None at 7f6af412c850> -> __attrs_140097251383408
            __attrs_140097251383408 = _static_140097251384224

            # <form ... (0:0)
            # --------------------------------------------------------
            __append('<form')

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097251385376
            __default_140097251385376 = _DEFAULT_MARKER

            # <Substitution 'request/getURL' (25:17)> -> __attr_action
            __token = 563
            try:
                __zt_tmp = __attrs_140097251383408
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_action = _static_140097413192464('path', 'request/getURL', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_action = __quote(__attr_action, '"', '&quot;', '.', _DEFAULT_MARKER)
            if (__attr_action is not None):
                __append((' action="%s"' % __attr_action))
            __append(' method="post"')

            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097251384656
            __default_140097251384656 = _DEFAULT_MARKER

            # <Substitution 'view/enctype' (26:17)> -> __attr_enctype
            __token = 596
            try:
                __zt_tmp = __attrs_140097251383408
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_enctype = _static_140097413192464('path', 'view/enctype', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __attr_enctype = __quote(__attr_enctype, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_enctype is not None):
                __append((' enctype="%s"' % __attr_enctype))
            __append(' >\n    ')

            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097251383312
            __attrs_140097251383312 = _static_140097412968080
            __backup_widget_140097252810496 = get('widget', __marker)

            # <Value 'view/widgets/values|nothing' (29:32)> -> __iterator
            __token = 657
            try:
                __zt_tmp = __attrs_140097251383312
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140097413192464('path', 'view/widgets/values|nothing', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            (__iterator, ____index_140097251382544, ) = getname('repeat')('widget', __iterator)
            econtext['widget'] = None
            for __item in __iterator:
                econtext['widget'] = __item
                __append('\n      ')

                # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097251385760
                __attrs_140097251385760 = _static_140097412968080
                __backup_behavior_name_140097252806368 = get('behavior_name', __marker)

                # <Value 'python: widget.field.__name__' (31:34)> -> __value
                __token = 752
                try:
                    __zt_tmp = __attrs_140097251385760
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140097413192464('python', ' widget.field.__name__', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                econtext['behavior_name'] = __value
                __backup_behavior_reg_140097251876032 = get('behavior_reg', __marker)

                # <Value 'python: view.behaviors[behavior_name]' (32:32)> -> __value
                __token = 815
                try:
                    __zt_tmp = __attrs_140097251385760
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140097413192464('python', ' view.behaviors[behavior_name]', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                econtext['behavior_reg'] = __value
                __append('\n        ')

                # <Static value=<ast.Dict object at 0x7f6aeee724a0> name=None at 7f6aeee713c0> -> __attrs_140097251382688
                __attrs_140097251382688 = _static_140097251386528
                __backup_error_140097338227824 = get('error', __marker)

                # <Value 'widget/error' (36:21)> -> __value
                __token = 950
                try:
                    __zt_tmp = __attrs_140097251382688
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140097413192464('path', 'widget/error', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                econtext['error'] = __value
                __backup_hidden_140097251384080 = get('hidden', __marker)

                # <Value "python:widget.mode == 'hidden'" (37:21)> -> __value
                __token = 985
                try:
                    __zt_tmp = __attrs_140097251382688
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140097413192464('python', "widget.mode == 'hidden'", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                econtext['hidden'] = __value

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div')

                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097251383264
                __default_140097251383264 = _DEFAULT_MARKER

                # <Substitution "python:'mb-3 field' + (error and 'alert alert-warning' or '')" (40:21)> -> __attr_class
                __token = 1084
                try:
                    __zt_tmp = __attrs_140097251382688
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_class = _static_140097413192464('python', "'mb-3 field' + (error and 'alert alert-warning' or '')", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                __attr_class = __quote(__attr_class, '"', '&quot;', 'field', _DEFAULT_MARKER)
                if (__attr_class is not None):
                    __append((' class="%s"' % __attr_class))
                __append(' >\n\n          ')

                # <Static value=<ast.Dict object at 0x7f6aeead2b00> name=None at 7f6aeead38b0> -> __attrs_140097247576176
                __attrs_140097247576176 = _static_140097247587072

                # <Value 'python:widget.required and not hidden' (46:31)> -> __condition
                __token = 1275
                try:
                    __zt_tmp = __attrs_140097247576176
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140097413192464('python', 'widget.required and not hidden', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span class="fieldRequired"')

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097247584144
                    __default_140097247584144 = _DEFAULT_MARKER

                    # <Translate msgid='title_required' node=<ast.Constant object at 0x7f6aeead2e00> at 7f6aeead3fa0> -> __attr_title
                    __attr_title = 'Required'
                    __attr_title = translate('title_required', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    if (__attr_title is not None):
                        __append((' title="%s"' % __attr_title))
                    __append(' >')
                    __stream_140097247589664 = []
                    __append_140097247589664 = __stream_140097247589664.append
                    __append_140097247589664('\n        (Required)\n          ')
                    __msgid_140097247589664 = __re_whitespace(''.join(__stream_140097247589664)).strip()
                    if 'label_required':
                        __append(translate('label_required', mapping=None, default=__msgid_140097247589664, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</span>')
                __append('\n\n          ')

                # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097247584864
                __attrs_140097247584864 = _static_140097412968080

                # <Value 'error' (53:30)> -> __condition
                __token = 1498
                try:
                    __zt_tmp = __attrs_140097247584864
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140097413192464('path', 'error', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div >')

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097247584336
                    __default_140097247584336 = _DEFAULT_MARKER

                    # <Value 'error/render' (54:38)> -> __cache_140097247576800
                    __token = 1543
                    try:
                        __zt_tmp = __attrs_140097247584864
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140097247576800 = _static_140097413192464('path', 'error/render', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                    # <BinOp left=<Value 'error/render' (54:38)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeead1480> -> __condition
                    __expression = __cache_140097247576800

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n        Error\n          ')
                    else:
                        __content = __cache_140097247576800
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('</div>')
                __append('\n\n          ')

                # <Static value=<ast.Dict object at 0x7f6aeead3df0> name=None at 7f6aeead0850> -> __attrs_140097247591344
                __attrs_140097247591344 = _static_140097247591920

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="widget">\n            ')

                # <Static value=<ast.Dict object at 0x7f6aeead0f70> name=None at 7f6aeead3ac0> -> __attrs_140097247577136
                __attrs_140097247577136 = _static_140097247580016

                # <table ... (0:0)
                # --------------------------------------------------------
                __append('<table class="table table-borderless table-sm">\n              ')

                # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097247585872
                __attrs_140097247585872 = _static_140097412968080

                # <tbody ... (0:0)
                # --------------------------------------------------------
                __append('<tbody>\n                ')

                # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097247587936
                __attrs_140097247587936 = _static_140097412968080

                # <tr ... (0:0)
                # --------------------------------------------------------
                __append('<tr>\n                  ')

                # <Static value=<ast.Dict object at 0x7f6aeead1b40> name=None at 7f6aeead37c0> -> __attrs_140097339171664
                __attrs_140097339171664 = _static_140097247583040

                # <td ... (0:0)
                # --------------------------------------------------------
                __append('<td class="w-25">\n                    ')

                # <Static value=<ast.Dict object at 0x7f6af422b250> name=None at 7f6af4228370> -> __attrs_140097339170704
                __attrs_140097339170704 = _static_140097339175504

                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097339176272
                __default_140097339176272 = _DEFAULT_MARKER

                # <Value 'widget/render' (65:50)> -> __cache_140097339175072
                __token = 1860
                try:
                    __zt_tmp = __attrs_140097339170704
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140097339175072 = _static_140097413192464('path', 'widget/render', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                # <BinOp left=<Value 'widget/render' (65:50)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6af422a380> -> __condition
                __expression = __cache_140097339175072

                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input type="text" />')
                else:
                    __content = __cache_140097339175072
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n                  </td>\n                  ')

                # <Static value=<ast.Dict object at 0x7f6aee908dc0> name=None at 7f6aee909420> -> __attrs_140097245711280
                __attrs_140097245711280 = _static_140097245711808

                # <td ... (0:0)
                # --------------------------------------------------------
                __append('<td class="w-25" >')

                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097339174304
                __default_140097339174304 = _DEFAULT_MARKER

                # <Value 'behavior_name' (69:35)> -> __cache_140097339173536
                __token = 1992
                try:
                    __zt_tmp = __attrs_140097245711280
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140097339173536 = _static_140097413192464('path', 'behavior_name', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                # <BinOp left=<Value 'behavior_name' (69:35)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6af422b5b0> -> __condition
                __expression = __cache_140097339173536

                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('name of behavior')
                else:
                    __content = __cache_140097339173536
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</td>\n                  ')

                # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097245718336
                __attrs_140097245718336 = _static_140097412968080

                # <td ... (0:0)
                # --------------------------------------------------------
                __append('<td>')

                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097245722752
                __default_140097245722752 = _DEFAULT_MARKER

                # <Value 'python:behavior_reg.interface.__identifier__' (71:35)> -> __cache_140097245710320
                __token = 2083
                try:
                    __zt_tmp = __attrs_140097245718336
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140097245710320 = _static_140097413192464('python', 'behavior_reg.interface.__identifier__', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                # <BinOp left=<Value 'python:behavior_reg.interface.__identifier__' (71:35)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aee9089d0> -> __condition
                __expression = __cache_140097245710320

                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('interface of behavior')
                else:
                    __content = __cache_140097245710320
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</td>\n                </tr>\n                ')

                # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097245714880
                __attrs_140097245714880 = _static_140097412968080
                __backup_description_140097247582512 = get('description', __marker)

                # <Value 'widget/field/description' (74:34)> -> __value
                __token = 2245
                try:
                    __zt_tmp = __attrs_140097245714880
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140097413192464('path', 'widget/field/description', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                econtext['description'] = __value

                # <Value 'python:description and not hidden' (76:35)> -> __condition
                __token = 2328
                try:
                    __zt_tmp = __attrs_140097245714880
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140097413192464('python', 'description and not hidden', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                if __condition:

                    # <tr ... (0:0)
                    # --------------------------------------------------------
                    __append('<tr >\n                  ')

                    # <Static value=<ast.Dict object at 0x7f6aee90b370> name=None at 7f6aee90b730> -> __attrs_140097245718816
                    __attrs_140097245718816 = _static_140097245721456

                    # <td ... (0:0)
                    # --------------------------------------------------------
                    __append('<td colspan="3">\n                    ')

                    # <Static value=<ast.Dict object at 0x7f6aee90af80> name=None at 7f6aee908340> -> __attrs_140097245717856
                    __attrs_140097245717856 = _static_140097245720448

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span class="form-text" >')

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097245715552
                    __default_140097245715552 = _DEFAULT_MARKER

                    # <Value 'description' (80:39)> -> __cache_140097245712096
                    __token = 2499
                    try:
                        __zt_tmp = __attrs_140097245717856
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140097245712096 = _static_140097413192464('path', 'description', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                    # <BinOp left=<Value 'description' (80:39)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aee90bd30> -> __condition
                    __expression = __cache_140097245712096

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('field description\n                    ')
                    else:
                        __content = __cache_140097245712096
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</span>\n                  </td>\n                </tr>')
                if (__backup_description_140097247582512 is __marker):
                    del econtext['description']
                else:
                    econtext['description'] = __backup_description_140097247582512
                __append('\n              </tbody>\n            </table>\n          </div>\n        </div>')
                if (__backup_hidden_140097251384080 is __marker):
                    del econtext['hidden']
                else:
                    econtext['hidden'] = __backup_hidden_140097251384080
                if (__backup_error_140097338227824 is __marker):
                    del econtext['error']
                else:
                    econtext['error'] = __backup_error_140097338227824
                __append('\n\n      ')
                if (__backup_behavior_reg_140097251876032 is __marker):
                    del econtext['behavior_reg']
                else:
                    econtext['behavior_reg'] = __backup_behavior_reg_140097251876032
                if (__backup_behavior_name_140097252806368 is __marker):
                    del econtext['behavior_name']
                else:
                    econtext['behavior_name'] = __backup_behavior_name_140097252806368
                __append('\n\n\n    ')
                ____index_140097251382544 -= 1
                if (____index_140097251382544 > 0):
                    __append('')
            if (__backup_widget_140097252810496 is __marker):
                del econtext['widget']
            else:
                econtext['widget'] = __backup_widget_140097252810496
            __append('\n    ')

            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097251385184
            __attrs_140097251385184 = _static_140097412968080
            __backup_macroname_140097248706688 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f6aeee73550> name=None at 7f6aeee70d60> -> __value
            __value = _static_140097251390800
            econtext['macroname'] = __value

            # <Value 'context/@@ploneform-macros/actions' (95:36)> -> __macro
            __token = 2823
            try:
                __zt_tmp = __attrs_140097251385184
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140097413192464('path', 'context/@@ploneform-macros/actions', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __token = 2823
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140097248706688 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140097248706688
            __append('\n  </form>\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }