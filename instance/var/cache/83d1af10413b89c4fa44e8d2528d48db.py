# -*- coding: utf-8 -*-
__filename = 'manage_tool'

__tokens = {27: ('context/manage_page_header', 1, 27), 99: ('context/manage_tabs', 2, 27), 313: ('context/listContextInfos', 15, 26), 361: (" python: [x for x in contexts if x['type'] == 'base'", 16, 22), 442: ('d context/getBaselineContext', 17, 26), 507: ("ay python: context_id or '(non", 18, 33), 571: ("yle python: context_id != ''\n                                    and 'display: none' or 'display: bl", 19, 29), 872: ('context_id_display', 29, 41), 948: ('python:context.getProfileImportDate(context_id)', 31, 26), 1066: ('last', 34, 24), 1112: ('last', 35, 39), 1192: ("python: context_id != ''", 39, 22), 1697: ('overwrite_style', 54, 29), 1882: ('bases', 59, 33), 1991: (' context_info/i', 61, 28), 1922: ("python:context_id == context_info['id']", 60, 33), 2030: ('context_info/title', 62, 21), 2282: ('context/getExcludeGlobalSteps', 69, 35), 2651: ('context/manage_page_footer', 82, 27)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139970367510160 = {'class': 'form-element', 'type': 'submit', 'name': 'manage_updateToolProperties:method', 'value': 'Update Base Profile', }
_static_139970367506080 = {'type': 'checkbox', 'name': 'exclude_global_steps', 'checked': 'context/getExcludeGlobalSteps', }
_static_139970367470608 = {'id': 'exclude_global_steps_fs', }
_static_139970367469072 = {'value': 'context-CONTEXT_ID', 'selected': "python:context_id == context_info['id']", }
_static_139970367466624 = {'name': 'context_id', }
_static_139970367464416 = {'id': 'context_id_fs', }
_static_139970367463216 = {'id': 'overwrite', 'style': 'overwrite_style', }
_static_139970367461776 = {'href': '#', 'onclick': 'showOverwrite(this); return false', }
_static_139970367460000 = {'style': 'color: red', }
_static_139970367458944 = {'type': 'text/javascript', 'lang': 'JavaScript', }
_static_139970367438752 = {'class': 'info', }
_static_139970367432752 = {'id': 'baseline_fs', }
_static_139970367431744 = {'method': 'post', 'action': '.', }
_static_139970367426848 = {'type': 'text/css', }
_static_139970428920176 = __C2ZContextWrapper
_static_139970428920464 = __compile_zt_expr
_static_139970428728848 = {}

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

            # <Static value=<ast.Dict object at 0x7f4d67aef610> name=None at 7f4d67aef940> -> __attrs_139970367424400
            __attrs_139970367424400 = _static_139970428728848

            # <Symbol value=<DEFAULT> at 7f4d67aac3a0> -> __default_139970367424208
            __default_139970367424208 = _DEFAULT_MARKER

            # <Value 'context/manage_page_header' (1:27)> -> __cache_139970367423728
            __token = 27
            try:
                __zt_tmp = __attrs_139970367424400
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139970367423728 = _static_139970428920464('path', 'context/manage_page_header', econtext=econtext)(_static_139970428920176(econtext, __zt_tmp))

            # <BinOp left=<Value 'context/manage_page_header' (1:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f4d67aac3a0> at 7f4d640785b0> -> __condition
            __expression = __cache_139970367423728

            # <Symbol value=<DEFAULT> at 7f4d67aac3a0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append('<h1>PAGE HEADER</h1>')
            else:
                __content = __cache_139970367423728
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n')

            # <Static value=<ast.Dict object at 0x7f4d67aef610> name=None at 7f4d67aef940> -> __attrs_139970367425984
            __attrs_139970367425984 = _static_139970428728848

            # <Symbol value=<DEFAULT> at 7f4d67aac3a0> -> __default_139970367425792
            __default_139970367425792 = _DEFAULT_MARKER

            # <Value 'context/manage_tabs' (2:27)> -> __cache_139970367425312
            __token = 99
            try:
                __zt_tmp = __attrs_139970367425984
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139970367425312 = _static_139970428920464('path', 'context/manage_tabs', econtext=econtext)(_static_139970428920176(econtext, __zt_tmp))

            # <BinOp left=<Value 'context/manage_tabs' (2:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f4d67aac3a0> at 7f4d64078be0> -> __condition
            __expression = __cache_139970367425312

            # <Symbol value=<DEFAULT> at 7f4d67aac3a0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <h2 ... (0:0)
                # --------------------------------------------------------
                __append('<h2>TABS</h2>')
            else:
                __content = __cache_139970367425312
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n')

            # <Static value=<ast.Dict object at 0x7f4d64079120> name=None at 7f4d64079150> -> __attrs_139970367427232
            __attrs_139970367427232 = _static_139970367426848

            # <style ... (0:0)
            # --------------------------------------------------------
            __append('<style type="text/css">\n.warning {\n   color: red;\n   font-weight: bold;\n}\n.info {\n   color: #446688;\n   font-style: italic;\n   margin-left: 2em;\n}\n</style>\n\n')

            # <Static value=<ast.Dict object at 0x7f4d67aef610> name=None at 7f4d67aef940> -> __attrs_139970367428192
            __attrs_139970367428192 = _static_139970428728848
            __backup_contexts_139970367422816 = get('contexts', __marker)

            # <Value 'context/listContextInfos' (15:26)> -> __value
            __token = 313
            try:
                __zt_tmp = __attrs_139970367428192
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139970428920464('path', 'context/listContextInfos', econtext=econtext)(_static_139970428920176(econtext, __zt_tmp))
            econtext['contexts'] = __value
            __backup_bases_139970367423152 = get('bases', __marker)

            # <Value "python: [x for x in contexts if x['type'] == 'base']" (16:22)> -> __value
            __token = 361
            try:
                __zt_tmp = __attrs_139970367428192
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139970428920464('python', " [x for x in contexts if x['type'] == 'base']", econtext=econtext)(_static_139970428920176(econtext, __zt_tmp))
            econtext['bases'] = __value
            __backup_context_id_139970367423296 = get('context_id', __marker)

            # <Value 'context/getBaselineContextID' (17:26)> -> __value
            __token = 442
            try:
                __zt_tmp = __attrs_139970367428192
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139970428920464('path', 'context/getBaselineContextID', econtext=econtext)(_static_139970428920176(econtext, __zt_tmp))
            econtext['context_id'] = __value
            __backup_context_id_display_139970367424736 = get('context_id_display', __marker)

            # <Value "python: context_id or '(none)'" (18:33)> -> __value
            __token = 507
            try:
                __zt_tmp = __attrs_139970367428192
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139970428920464('python', " context_id or '(none)'", econtext=econtext)(_static_139970428920176(econtext, __zt_tmp))
            econtext['context_id_display'] = __value
            __backup_overwrite_style_139970367428096 = get('overwrite_style', __marker)

            # <Value "python: context_id != ''\n                                    and 'display: none' or 'display: block'" (19:29)> -> __value
            __token = 571
            try:
                __zt_tmp = __attrs_139970367428192
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139970428920464('python', " context_id != ''\n                                    and 'display: none' or 'display: block'", econtext=econtext)(_static_139970428920176(econtext, __zt_tmp))
            econtext['overwrite_style'] = __value

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div>\n')

            # <Static value=<ast.Dict object at 0x7f4d67aef610> name=None at 7f4d67aef940> -> __attrs_139970367430256
            __attrs_139970367430256 = _static_139970428728848

            # <h3 ... (0:0)
            # --------------------------------------------------------
            __append('<h3> Setup Tool Profiles </h3>\n\n')

            # <Static value=<ast.Dict object at 0x7f4d6407a440> name=None at 7f4d6407a0b0> -> __attrs_139970367431792
            __attrs_139970367431792 = _static_139970367431744

            # <form ... (0:0)
            # --------------------------------------------------------
            __append('<form method="post" action=".">\n\n ')

            # <Static value=<ast.Dict object at 0x7f4d6407a830> name=None at 7f4d6407a860> -> __attrs_139970367433136
            __attrs_139970367433136 = _static_139970367432752

            # <fieldset ... (0:0)
            # --------------------------------------------------------
            __append('<fieldset id="baseline_fs">\n   ')

            # <Static value=<ast.Dict object at 0x7f4d67aef610> name=None at 7f4d67aef940> -> __attrs_139970367434144
            __attrs_139970367434144 = _static_139970428728848

            # <legend ... (0:0)
            # --------------------------------------------------------
            __append('<legend>Baseline Profile</legend>\n   \n  ')

            # <Static value=<ast.Dict object at 0x7f4d67aef610> name=None at 7f4d67aef940> -> __attrs_139970367435056
            __attrs_139970367435056 = _static_139970428728848

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p>Active baseline: ')

            # <Static value=<ast.Dict object at 0x7f4d67aef610> name=None at 7f4d67aef940> -> __attrs_139970367436688
            __attrs_139970367436688 = _static_139970428728848

            # <span ... (0:0)
            # --------------------------------------------------------
            __append('<span>')

            # <Symbol value=<DEFAULT> at 7f4d67aac3a0> -> __default_139970367436112
            __default_139970367436112 = _DEFAULT_MARKER

            # <Value 'context_id_display' (29:41)> -> __cache_139970367435632
            __token = 872
            try:
                __zt_tmp = __attrs_139970367436688
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139970367435632 = _static_139970428920464('path', 'context_id_display', econtext=econtext)(_static_139970428920176(econtext, __zt_tmp))

            # <BinOp left=<Value 'context_id_display' (29:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f4d67aac3a0> at 7f4d6407b430> -> __condition
            __expression = __cache_139970367435632

            # <Symbol value=<DEFAULT> at 7f4d67aac3a0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                __append('(none)')
            else:
                __content = __cache_139970367435632
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append('</span>\n  ')

            # <Static value=<ast.Dict object at 0x7f4d67aef610> name=None at 7f4d67aef940> -> __attrs_139970367437504
            __attrs_139970367437504 = _static_139970428728848
            __backup_last_139970367430592 = get('last', __marker)

            # <Value 'python:context.getProfileImportDate(context_id)' (31:26)> -> __value
            __token = 948
            try:
                __zt_tmp = __attrs_139970367437504
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_139970428920464('python', 'context.getProfileImportDate(context_id)', econtext=econtext)(_static_139970428920176(econtext, __zt_tmp))
            econtext['last'] = __value
            __append('\n   ')

            # <Static value=<ast.Dict object at 0x7f4d6407bfa0> name=None at 7f4d6407bfd0> -> __attrs_139970367455584
            __attrs_139970367455584 = _static_139970367438752

            # <Value 'last' (34:24)> -> __condition
            __token = 1066
            try:
                __zt_tmp = __attrs_139970367455584
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_139970428920464('path', 'last', econtext=econtext)(_static_139970428920176(econtext, __zt_tmp))
            if __condition:

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span class="info">\n     Last imported ')

                # <Static value=<ast.Dict object at 0x7f4d67aef610> name=None at 7f4d67aef940> -> __attrs_139970367457408
                __attrs_139970367457408 = _static_139970428728848

                # <Symbol value=<DEFAULT> at 7f4d67aac3a0> -> __default_139970367456928
                __default_139970367456928 = _DEFAULT_MARKER

                # <Value 'last' (35:39)> -> __cache_139970367456448
                __token = 1112
                try:
                    __zt_tmp = __attrs_139970367457408
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_139970367456448 = _static_139970428920464('path', 'last', econtext=econtext)(_static_139970428920176(econtext, __zt_tmp))

                # <BinOp left=<Value 'last' (35:39)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f4d67aac3a0> at 7f4d64080580> -> __condition
                __expression = __cache_139970367456448

                # <Symbol value=<DEFAULT> at 7f4d67aac3a0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('TIMESTAMP')
                else:
                    __content = __cache_139970367456448
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</span>')
            __append('\n   ')
            if (__backup_last_139970367430592 is __marker):
                del econtext['last']
            else:
                econtext['last'] = __backup_last_139970367430592
            __append('\n  </p>\n\n  ')

            # <Static value=<ast.Dict object at 0x7f4d67aef610> name=None at 7f4d67aef940> -> __attrs_139970367456256
            __attrs_139970367456256 = _static_139970428728848

            # <Value "python: context_id != ''" (39:22)> -> __condition
            __token = 1192
            try:
                __zt_tmp = __attrs_139970367456256
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_139970428920464('python', " context_id != ''", econtext=econtext)(_static_139970428920176(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div>\n  ')

                # <Static value=<ast.Dict object at 0x7f4d64080e80> name=None at 7f4d64080eb0> -> __attrs_139970367459136
                __attrs_139970367459136 = _static_139970367458944

                # <script ... (0:0)
                # --------------------------------------------------------
                __append('<script type="text/javascript" lang="JavaScript">\n  function showOverwrite(e) {\n      var overwrite = document.getElementById(\'overwrite\');\n      overwrite.style.display = \'block\';\n  }\n  </script>\n  ')

                # <Static value=<ast.Dict object at 0x7f4d640812a0> name=None at 7f4d640812d0> -> __attrs_139970367460384
                __attrs_139970367460384 = _static_139970367460000

                # <p ... (0:0)
                # --------------------------------------------------------
                __append('<p style="color: red"> Changing the baseline profile is potentially a\n     dangerous operation.\n     ')

                # <Static value=<ast.Dict object at 0x7f4d64081990> name=None at 7f4d640819c0> -> __attrs_139970367461968
                __attrs_139970367461968 = _static_139970367461776

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a href="#" onclick="showOverwrite(this); return false">Click here</a>\n     if you really need to do this.\n   </p>\n  </div>')
            __append('\n\n  ')

            # <Static value=<ast.Dict object at 0x7f4d64081f30> name=None at 7f4d64081ba0> -> __attrs_139970367463456
            __attrs_139970367463456 = _static_139970367463216

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div id="overwrite"')

            # <Symbol value=<DEFAULT> at 7f4d67aac3a0> -> __default_139970367462736
            __default_139970367462736 = _DEFAULT_MARKER

            # <Substitution 'overwrite_style' (54:29)> -> __attr_style
            __token = 1697
            try:
                __zt_tmp = __attrs_139970367463456
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_style = _static_139970428920464('path', 'overwrite_style', econtext=econtext)(_static_139970428920176(econtext, __zt_tmp))
            __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_style is not None):
                __append((' style="%s"' % __attr_style))
            __append('>\n   ')

            # <Static value=<ast.Dict object at 0x7f4d640823e0> name=None at 7f4d64082410> -> __attrs_139970367464800
            __attrs_139970367464800 = _static_139970367464416

            # <fieldset ... (0:0)
            # --------------------------------------------------------
            __append('<fieldset id="context_id_fs">\n    ')

            # <Static value=<ast.Dict object at 0x7f4d67aef610> name=None at 7f4d67aef940> -> __attrs_139970367465760
            __attrs_139970367465760 = _static_139970428728848

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label>Context ID</label>\n    ')

            # <Static value=<ast.Dict object at 0x7f4d64082c80> name=None at 7f4d64082cb0> -> __attrs_139970367467008
            __attrs_139970367467008 = _static_139970367466624

            # <select ... (0:0)
            # --------------------------------------------------------
            __append('<select name="context_id">\n     ')

            # <Static value=<ast.Dict object at 0x7f4d64083610> name=None at 7f4d64083640> -> __attrs_139970367469696
            __attrs_139970367469696 = _static_139970367469072
            __backup_context_info_139970367438080 = get('context_info', __marker)

            # <Value 'bases' (59:33)> -> __iterator
            __token = 1882
            try:
                __zt_tmp = __attrs_139970367469696
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_139970428920464('path', 'bases', econtext=econtext)(_static_139970428920176(econtext, __zt_tmp))
            (__iterator, ____index_139970367469936, ) = getname('repeat')('context_info', __iterator)
            econtext['context_info'] = None
            for __item in __iterator:
                econtext['context_info'] = __item

                # <option ... (0:0)
                # --------------------------------------------------------
                __append('<option')

                # <Symbol value=<DEFAULT> at 7f4d67aac3a0> -> __default_139970367468640
                __default_139970367468640 = _DEFAULT_MARKER

                # <Substitution 'context_info/id' (61:28)> -> __attr_value
                __token = 1991
                try:
                    __zt_tmp = __attrs_139970367469696
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_139970428920464('path', 'context_info/id', econtext=econtext)(_static_139970428920176(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', 'context-CONTEXT_ID', _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))

                # <Symbol value=<DEFAULT> at 7f4d67aac3a0> -> __default_139970367469168
                __default_139970367469168 = _DEFAULT_MARKER

                # <Boolean "python:context_id == context_info['id']" (60:33)> -> __attr_selected
                __token = 1922
                try:
                    __zt_tmp = __attrs_139970367469696
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_selected = _static_139970428920464('python', "context_id == context_info['id']", econtext=econtext)(_static_139970428920176(econtext, __zt_tmp))
                if (__attr_selected is _DEFAULT_MARKER):
                    __attr_selected = None
                else:
                    if __attr_selected:
                        __attr_selected = 'selected'
                    else:
                        __attr_selected = None
                if (__attr_selected is not None):
                    __append((' selected="%s"' % __attr_selected))
                __append(' >')

                # <Symbol value=<DEFAULT> at 7f4d67aac3a0> -> __default_139970367468064
                __default_139970367468064 = _DEFAULT_MARKER

                # <Value 'context_info/title' (62:21)> -> __cache_139970367467584
                __token = 2030
                try:
                    __zt_tmp = __attrs_139970367469696
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_139970367467584 = _static_139970428920464('path', 'context_info/title', econtext=econtext)(_static_139970428920176(econtext, __zt_tmp))

                # <BinOp left=<Value 'context_info/title' (62:21)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f4d67aac3a0> at 7f4d64083100> -> __condition
                __expression = __cache_139970367467584

                # <Symbol value=<DEFAULT> at 7f4d67aac3a0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('CONTEXT_TITLE')
                else:
                    __content = __cache_139970367467584
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</option>')
                ____index_139970367469936 -= 1
                if (____index_139970367469936 > 0):
                    __append('\n     ')
            if (__backup_context_info_139970367438080 is __marker):
                del econtext['context_info']
            else:
                econtext['context_info'] = __backup_context_info_139970367438080
            __append('\n    </select>\n   </fieldset>\n   ')

            # <Static value=<ast.Dict object at 0x7f4d64083c10> name=None at 7f4d64083a90> -> __attrs_139970367470944
            __attrs_139970367470944 = _static_139970367470608

            # <fieldset ... (0:0)
            # --------------------------------------------------------
            __append('<fieldset id="exclude_global_steps_fs">\n    ')

            # <Static value=<ast.Dict object at 0x7f4d67aef610> name=None at 7f4d67aef940> -> __attrs_139970367504736
            __attrs_139970367504736 = _static_139970428728848

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label>Exclude global steps?</label>\n    ')

            # <Static value=<ast.Dict object at 0x7f4d6408c6a0> name=None at 7f4d6408c6d0> -> __attrs_139970367506608
            __attrs_139970367506608 = _static_139970367506080

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input type="checkbox" name="exclude_global_steps"')

            # <Symbol value=<DEFAULT> at 7f4d67aac3a0> -> __default_139970367505408
            __default_139970367505408 = _DEFAULT_MARKER

            # <Boolean 'context/getExcludeGlobalSteps' (69:35)> -> __attr_checked
            __token = 2282
            try:
                __zt_tmp = __attrs_139970367506608
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_checked = _static_139970428920464('path', 'context/getExcludeGlobalSteps', econtext=econtext)(_static_139970428920176(econtext, __zt_tmp))
            if (__attr_checked is _DEFAULT_MARKER):
                __attr_checked = None
            else:
                if __attr_checked:
                    __attr_checked = 'checked'
                else:
                    __attr_checked = None
            if (__attr_checked is not None):
                __append((' checked="%s"' % __attr_checked))
            __append(' />\n    ')

            # <Static value=<ast.Dict object at 0x7f4d67aef610> name=None at 7f4d67aef940> -> __attrs_139970367507376
            __attrs_139970367507376 = _static_139970428728848

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p>')

            # <Static value=<ast.Dict object at 0x7f4d67aef610> name=None at 7f4d67aef940> -> __attrs_139970367508240
            __attrs_139970367508240 = _static_139970428728848

            # <em ... (0:0)
            # --------------------------------------------------------
            __append('<em>If checked, only steps explicitly registered by the profile will\n       be available.</em></p>\n   </fieldset>\n   ')

            # <Static value=<ast.Dict object at 0x7f4d6408d690> name=None at 7f4d6408d6c0> -> __attrs_139970367509008
            __attrs_139970367509008 = _static_139970367510160

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input class="form-element" type="submit" name="manage_updateToolProperties:method" value="Update Base Profile" />\n  </div>\n </fieldset>\n</form>\n</div>')
            if (__backup_overwrite_style_139970367428096 is __marker):
                del econtext['overwrite_style']
            else:
                econtext['overwrite_style'] = __backup_overwrite_style_139970367428096
            if (__backup_context_id_display_139970367424736 is __marker):
                del econtext['context_id_display']
            else:
                econtext['context_id_display'] = __backup_context_id_display_139970367424736
            if (__backup_context_id_139970367423296 is __marker):
                del econtext['context_id']
            else:
                econtext['context_id'] = __backup_context_id_139970367423296
            if (__backup_bases_139970367423152 is __marker):
                del econtext['bases']
            else:
                econtext['bases'] = __backup_bases_139970367423152
            if (__backup_contexts_139970367422816 is __marker):
                del econtext['contexts']
            else:
                econtext['contexts'] = __backup_contexts_139970367422816
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x7f4d67aef610> name=None at 7f4d67aef940> -> __attrs_139970367510928
            __attrs_139970367510928 = _static_139970428728848

            # <Symbol value=<DEFAULT> at 7f4d67aac3a0> -> __default_139970367510736
            __default_139970367510736 = _DEFAULT_MARKER

            # <Value 'context/manage_page_footer' (82:27)> -> __cache_139970367510256
            __token = 2651
            try:
                __zt_tmp = __attrs_139970367510928
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139970367510256 = _static_139970428920464('path', 'context/manage_page_footer', econtext=econtext)(_static_139970428920176(econtext, __zt_tmp))

            # <BinOp left=<Value 'context/manage_page_footer' (82:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f4d67aac3a0> at 7f4d6408d7b0> -> __condition
            __expression = __cache_139970367510256

            # <Symbol value=<DEFAULT> at 7f4d67aac3a0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append('<h1>PAGE FOOTER</h1>')
            else:
                __content = __cache_139970367510256
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }