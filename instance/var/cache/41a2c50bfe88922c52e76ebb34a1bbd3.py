# -*- coding: utf-8 -*-
__filename = 'manage_main'

__tokens = {27: ('context/manage_page_header', 1, 27), 94: ('context/manage_tabs', 2, 27), 465: ('container/getProperties', 13, 20), 792: ('props/keep_entries', 23, 27), 1152: ('props/copy_to_zlog', 35, 29), 1185: (' not:container/checkEventLogPermission|nothin', 36, 13), 1566: ("python: '\\n'.join(props['ignored_exceptions'])", 48, 18), 1858: ('container/getLogEntries', 62, 26), 1933: ('not:entries', 64, 47), 2071: ('entries', 66, 94), 2337: ('entries', 76, 26), 2426: ("python: modules['DateTime'].DateTime(entry['time']).ISO()", 78, 25), 2579: ('string: ${entry/username} (${entry/userid})', 81, 25), 2731: ('string:showEntry?id=${entry/id}', 84, 47), 2791: ('entry/type', 85, 26), 2857: ('entry/value', 86, 31), 2891: ("python: len(value) &lt; 70 and value or value[:70] + '.", 87, 21), 3075: ('string:${context/absolute_url}/forgetEntry?id=${entry/id}', 91, 42), 3408: ('context/manage_page_footer', 104, 27)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140120092461712 = {'class': 'btn btn-primary', 'type': 'submit', 'name': 'submit', 'value': 'Refresh', }
_static_140120092458912 = {'class': 'zmi-controls', }
_static_140120092409664 = {'action': 'manage_main', 'method': 'GET', }
_static_140120092456464 = {'href': '#', }
_static_140120092450848 = {'href': 'showEntry', }
_static_140120092449456 = {'class': 'zmi-exception', }
_static_140120092446576 = {'class': 'zmi-username', }
_static_140120092443888 = {'class': 'zmi-time', 'style': 'white-space:nowrap', }
_static_140120092407456 = {'class': 'blank', }
_static_140120092406208 = {'class': 'zmi-exception', }
_static_140120092405296 = {'class': 'zmi-username', 'title': 'User Id', }
_static_140120092403424 = {'class': 'zmi-time', }
_static_140120092400016 = {'class': 'table table-sm zmi-errorlog-entries', 'style': 'font-size:smaller', }
_static_140120092398096 = {'class': 'alert alert-info', }
_static_140120092395888 = {'class': 'btn btn-primary', 'type': 'submit', 'name': 'submit', 'value': 'Save Changes', }
_static_140120092376704 = {'class': 'zmi-controls', }
_static_140120092376368 = {'id': 'ignored_exceptions', 'class': 'form-control', 'name': 'ignored_exceptions:ulines', 'rows': '3', }
_static_140120092372864 = {'class': ' col-sm-7 col-md-8', }
_static_140120092371808 = {'for': 'ignored_exceptions', 'class': 'form-label col-sm-5 col-md-4', }
_static_140120092370032 = {'class': 'form-group row', }
_static_140120092368928 = {'type': 'checkbox', 'id': 'copy_to_zlog', 'class': 'checkbox-list-item', 'name': 'copy_to_zlog', 'checked': 'props/copy_to_zlog', 'disabled': 'not:container/checkEventLogPermission|nothing', }
_static_140120092366096 = {'class': ' col-sm-7 col-md-8', }
_static_140120092365040 = {'for': 'copy_to_zlog', 'class': 'form-label col-sm-5 col-md-4', }
_static_140120092363216 = {'class': 'form-group row', }
_static_140120092362640 = {'type': 'text', 'id': 'keep_entries', 'class': 'form-control', 'name': 'keep_entries', 'value': 'props/keep_entries', }
_static_140120092212288 = {'class': ' col-sm-7 col-md-8', }
_static_140120092211232 = {'for': 'keep_entries', 'class': 'form-label col-sm-5 col-md-4', }
_static_140120092209360 = {'class': 'form-group row', }
_static_140120092208160 = {'action': 'setProperties', 'method': 'post', }
_static_140120092206288 = {'class': 'form-help mb-4', }
_static_140120092205232 = {'class': 'container-fluid', }
_static_140120153207616 = __C2ZContextWrapper
_static_140120153207904 = __compile_zt_expr
_static_140120153196576 = {}

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

            # <Static value=<ast.Dict object at 0x7f7043f50820> name=None at 7f7043f50b50> -> __attrs_140120092202832
            __attrs_140120092202832 = _static_140120153196576

            # <Symbol value=<DEFAULT> at 7f7043ee9570> -> __default_140120092202640
            __default_140120092202640 = _DEFAULT_MARKER

            # <Value 'context/manage_page_header' (1:27)> -> __cache_140120092202160
            __token = 27
            try:
                __zt_tmp = __attrs_140120092202832
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140120092202160 = _static_140120153207904('path', 'context/manage_page_header', econtext=econtext)(_static_140120153207616(econtext, __zt_tmp))

            # <BinOp left=<Value 'context/manage_page_header' (1:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7043ee9570> at 7f7040525570> -> __condition
            __expression = __cache_140120092202160

            # <Symbol value=<DEFAULT> at 7f7043ee9570> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append('<h1>Header</h1>')
            else:
                __content = __cache_140120092202160
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n')

            # <Static value=<ast.Dict object at 0x7f7043f50820> name=None at 7f7043f50b50> -> __attrs_140120092204416
            __attrs_140120092204416 = _static_140120153196576

            # <Symbol value=<DEFAULT> at 7f7043ee9570> -> __default_140120092204224
            __default_140120092204224 = _DEFAULT_MARKER

            # <Value 'context/manage_tabs' (2:27)> -> __cache_140120092203744
            __token = 94
            try:
                __zt_tmp = __attrs_140120092204416
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140120092203744 = _static_140120153207904('path', 'context/manage_tabs', econtext=econtext)(_static_140120153207616(econtext, __zt_tmp))

            # <BinOp left=<Value 'context/manage_tabs' (2:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7043ee9570> at 7f7040525ba0> -> __condition
            __expression = __cache_140120092203744

            # <Symbol value=<DEFAULT> at 7f7043ee9570> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append('<h1>Tabs</h1>')
            else:
                __content = __cache_140120092203744
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x7f70405260b0> name=None at 7f70405260e0> -> __attrs_140120092205568
            __attrs_140120092205568 = _static_140120092205232

            # <main ... (0:0)
            # --------------------------------------------------------
            __append('<main class="container-fluid">\n\t')

            # <Static value=<ast.Dict object at 0x7f70405264d0> name=None at 7f7040526500> -> __attrs_140120092206720
            __attrs_140120092206720 = _static_140120092206288

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p class="form-help mb-4">\n\t\tThis page lists the exceptions that have occurred in this site\n\t\trecently.  You can configure how many exceptions should be kept\n\t\tand whether the exceptions should be copied to Zope\'s event log\n\t\tfile(s).\n\t</p>\n\n\t')

            # <Static value=<ast.Dict object at 0x7f7040526c20> name=None at 7f7040526860> -> __attrs_140120092208208
            __attrs_140120092208208 = _static_140120092208160
            __backup_props_140120092201296 = get('props', __marker)

            # <Value 'container/getProperties' (13:20)> -> __value
            __token = 465
            try:
                __zt_tmp = __attrs_140120092208208
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140120153207904('path', 'container/getProperties', econtext=econtext)(_static_140120153207616(econtext, __zt_tmp))
            econtext['props'] = __value

            # <form ... (0:0)
            # --------------------------------------------------------
            __append('<form action="setProperties" method="post">\n\n\t\t')

            # <Static value=<ast.Dict object at 0x7f70405270d0> name=None at 7f7040527100> -> __attrs_140120092209792
            __attrs_140120092209792 = _static_140120092209360

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="form-group row">\n\t\t\t')

            # <Static value=<ast.Dict object at 0x7f7040527820> name=None at 7f7040527850> -> __attrs_140120092211424
            __attrs_140120092211424 = _static_140120092211232

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label for="keep_entries" class="form-label col-sm-5 col-md-4">Number of exceptions to keep</label>\n\t\t\t')

            # <Static value=<ast.Dict object at 0x7f7040527c40> name=None at 7f7040527c70> -> __attrs_140120092212720
            __attrs_140120092212720 = _static_140120092212288

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class=" col-sm-7 col-md-8">\n\t\t\t\t')

            # <Static value=<ast.Dict object at 0x7f704054c790> name=None at 7f704054c7c0> -> __attrs_140120092360864
            __attrs_140120092360864 = _static_140120092362640

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input type="text" id="keep_entries" class="form-control" name="keep_entries"')

            # <Symbol value=<DEFAULT> at 7f7043ee9570> -> __default_140120092361488
            __default_140120092361488 = _DEFAULT_MARKER

            # <Substitution 'props/keep_entries' (23:27)> -> __attr_value
            __token = 792
            try:
                __zt_tmp = __attrs_140120092360864
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_value = _static_140120153207904('path', 'props/keep_entries', econtext=econtext)(_static_140120153207616(econtext, __zt_tmp))
            __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_value is not None):
                __append((' value="%s"' % __attr_value))
            __append(' />\n\t\t\t</div>\n\t\t</div>\n\n\t\t')

            # <Static value=<ast.Dict object at 0x7f704054c9d0> name=None at 7f704054ca00> -> __attrs_140120092363648
            __attrs_140120092363648 = _static_140120092363216

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="form-group row">\n\t\t\t')

            # <Static value=<ast.Dict object at 0x7f704054d0f0> name=None at 7f704054d120> -> __attrs_140120092365232
            __attrs_140120092365232 = _static_140120092365040

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label for="copy_to_zlog" class="form-label col-sm-5 col-md-4">Copy exceptions to the event log</label>\n\t\t\t')

            # <Static value=<ast.Dict object at 0x7f704054d510> name=None at 7f704054d540> -> __attrs_140120092366528
            __attrs_140120092366528 = _static_140120092366096

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class=" col-sm-7 col-md-8">\n\t\t\t\t')

            # <Static value=<ast.Dict object at 0x7f704054e020> name=None at 7f704054e050> -> __attrs_140120092369504
            __attrs_140120092369504 = _static_140120092368928

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input \t\t\t\t\ttype="checkbox" id="copy_to_zlog" class="checkbox-list-item" \t\t\t\t\tname="copy_to_zlog"')

            # <Symbol value=<DEFAULT> at 7f7043ee9570> -> __default_140120092367584
            __default_140120092367584 = _DEFAULT_MARKER

            # <Boolean 'props/copy_to_zlog' (35:29)> -> __attr_checked
            __token = 1152
            try:
                __zt_tmp = __attrs_140120092369504
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_checked = _static_140120153207904('path', 'props/copy_to_zlog', econtext=econtext)(_static_140120153207616(econtext, __zt_tmp))
            if (__attr_checked is _DEFAULT_MARKER):
                __attr_checked = None
            else:
                if __attr_checked:
                    __attr_checked = 'checked'
                else:
                    __attr_checked = None
            if (__attr_checked is not None):
                __append((' checked="%s"' % __attr_checked))

            # <Symbol value=<DEFAULT> at 7f7043ee9570> -> __default_140120092367104
            __default_140120092367104 = _DEFAULT_MARKER

            # <Boolean 'not:container/checkEventLogPermission|nothing' (36:13)> -> __attr_disabled
            __token = 1185
            try:
                __zt_tmp = __attrs_140120092369504
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_disabled = _static_140120153207904('not', 'container/checkEventLogPermission|nothing', econtext=econtext)(_static_140120153207616(econtext, __zt_tmp))
            if (__attr_disabled is _DEFAULT_MARKER):
                __attr_disabled = None
            else:
                if __attr_disabled:
                    __attr_disabled = 'disabled'
                else:
                    __attr_disabled = None
            if (__attr_disabled is not None):
                __append((' disabled="%s"' % __attr_disabled))
            __append(' />\n\t\t\t</div>\n\t\t</div>\n\n\t\t')

            # <Static value=<ast.Dict object at 0x7f704054e470> name=None at 7f704054e4a0> -> __attrs_140120092370464
            __attrs_140120092370464 = _static_140120092370032

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="form-group row">\n\t\t\t')

            # <Static value=<ast.Dict object at 0x7f704054eb60> name=None at 7f704054eb90> -> __attrs_140120092372048
            __attrs_140120092372048 = _static_140120092371808

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label for="ignored_exceptions" class="form-label col-sm-5 col-md-4">Ignored exception types</label>\n\t\t\t')

            # <Static value=<ast.Dict object at 0x7f704054ef80> name=None at 7f704054efb0> -> __attrs_140120092373296
            __attrs_140120092373296 = _static_140120092372864

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class=" col-sm-7 col-md-8">\n\t\t\t\t')

            # <Static value=<ast.Dict object at 0x7f704054fd30> name=None at 7f704054fd60> -> __attrs_140120092374976
            __attrs_140120092374976 = _static_140120092376368

            # <textarea ... (0:0)
            # --------------------------------------------------------
            __append('<textarea id="ignored_exceptions" class="form-control" name="ignored_exceptions:ulines" rows="3" >')

            # <Symbol value=<DEFAULT> at 7f7043ee9570> -> __default_140120092374448
            __default_140120092374448 = _DEFAULT_MARKER

            # <Value "python: '\\n'.join(props['ignored_exceptions'])" (48:18)> -> __cache_140120092373920
            __token = 1566
            try:
                __zt_tmp = __attrs_140120092374976
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140120092373920 = _static_140120153207904('python', " '\\n'.join(props['ignored_exceptions'])", econtext=econtext)(_static_140120153207616(econtext, __zt_tmp))

            # <BinOp left=<Value "python: '\\n'.join(props['ignored_exceptions'])" (48:18)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7043ee9570> at 7f704054f490> -> __condition
            __expression = __cache_140120092373920

            # <Symbol value=<DEFAULT> at 7f7043ee9570> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140120092373920
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append('</textarea>\n\t\t\t</div>\n\t\t</div>\n\n\n\t\t')

            # <Static value=<ast.Dict object at 0x7f704054fe80> name=None at 7f704054feb0> -> __attrs_140120092393536
            __attrs_140120092393536 = _static_140120092376704

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="zmi-controls">\n\t\t\t')

            # <Static value=<ast.Dict object at 0x7f7040554970> name=None at 7f70405549a0> -> __attrs_140120092394688
            __attrs_140120092394688 = _static_140120092395888

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input class="btn btn-primary" type="submit" name="submit" value="Save Changes" />\n\t\t</div>\n\n\t</form>')
            if (__backup_props_140120092201296 is __marker):
                del econtext['props']
            else:
                econtext['props'] = __backup_props_140120092201296
            __append('\n\n\n\t')

            # <Static value=<ast.Dict object at 0x7f7043f50820> name=None at 7f7043f50b50> -> __attrs_140120092396080
            __attrs_140120092396080 = _static_140120153196576

            # <h3 ... (0:0)
            # --------------------------------------------------------
            __append('<h3>Exception Log (most recent first)</h3>\n\t')

            # <Static value=<ast.Dict object at 0x7f7043f50820> name=None at 7f7043f50b50> -> __attrs_140120092396992
            __attrs_140120092396992 = _static_140120153196576
            __backup_entries_140120092201584 = get('entries', __marker)

            # <Value 'container/getLogEntries' (62:26)> -> __value
            __token = 1858
            try:
                __zt_tmp = __attrs_140120092396992
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140120153207904('path', 'container/getLogEntries', econtext=econtext)(_static_140120153207616(econtext, __zt_tmp))
            econtext['entries'] = __value

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div>\n\t\n\t\t')

            # <Static value=<ast.Dict object at 0x7f7040555210> name=None at 7f7040555240> -> __attrs_140120092398528
            __attrs_140120092398528 = _static_140120092398096

            # <Value 'not:entries' (64:47)> -> __condition
            __token = 1933
            try:
                __zt_tmp = __attrs_140120092398528
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140120153207904('not', 'entries', econtext=econtext)(_static_140120153207616(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="alert alert-info">No exceptions logged.</div>')
            __append('\n\t\t\n\t\t')

            # <Static value=<ast.Dict object at 0x7f7040555990> name=None at 7f70405559c0> -> __attrs_140120092400256
            __attrs_140120092400256 = _static_140120092400016

            # <Value 'entries' (66:94)> -> __condition
            __token = 2071
            try:
                __zt_tmp = __attrs_140120092400256
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140120153207904('path', 'entries', econtext=econtext)(_static_140120153207616(econtext, __zt_tmp))
            if __condition:

                # <table ... (0:0)
                # --------------------------------------------------------
                __append('<table class="table table-sm zmi-errorlog-entries" style="font-size:smaller">\n\t\t\t')

                # <Static value=<ast.Dict object at 0x7f7043f50820> name=None at 7f7043f50b50> -> __attrs_140120092401408
                __attrs_140120092401408 = _static_140120153196576

                # <thead ... (0:0)
                # --------------------------------------------------------
                __append('<thead>\n\t\t\t\t')

                # <Static value=<ast.Dict object at 0x7f7043f50820> name=None at 7f7043f50b50> -> __attrs_140120092402416
                __attrs_140120092402416 = _static_140120153196576

                # <tr ... (0:0)
                # --------------------------------------------------------
                __append('<tr>\n\t\t\t\t\t')

                # <Static value=<ast.Dict object at 0x7f70405566e0> name=None at 7f7040556710> -> __attrs_140120092403808
                __attrs_140120092403808 = _static_140120092403424

                # <th ... (0:0)
                # --------------------------------------------------------
                __append('<th class="zmi-time">Time</th>\n\t\t\t\t\t')

                # <Static value=<ast.Dict object at 0x7f7040556e30> name=None at 7f7040556a70> -> __attrs_140120092405344
                __attrs_140120092405344 = _static_140120092405296

                # <th ... (0:0)
                # --------------------------------------------------------
                __append('<th class="zmi-username" title="User Id">Username</th>\n\t\t\t\t\t')

                # <Static value=<ast.Dict object at 0x7f70405571c0> name=None at 7f70405571f0> -> __attrs_140120092406592
                __attrs_140120092406592 = _static_140120092406208

                # <th ... (0:0)
                # --------------------------------------------------------
                __append('<th class="zmi-exception">Exception</th>\n\t\t\t\t\t')

                # <Static value=<ast.Dict object at 0x7f70405576a0> name=None at 7f70405576d0> -> __attrs_140120092407840
                __attrs_140120092407840 = _static_140120092407456

                # <th ... (0:0)
                # --------------------------------------------------------
                __append('<th class="blank">&nbsp;</th>\n\t\t\t\t</tr>\n\t\t\t</thead>\n\t\t\t')

                # <Static value=<ast.Dict object at 0x7f7043f50820> name=None at 7f7043f50b50> -> __attrs_140120092408512
                __attrs_140120092408512 = _static_140120153196576

                # <tbody ... (0:0)
                # --------------------------------------------------------
                __append('<tbody>\n\t\t\t\t')

                # <Static value=<ast.Dict object at 0x7f7043f50820> name=None at 7f7043f50b50> -> __attrs_140120092409472
                __attrs_140120092409472 = _static_140120153196576
                __backup_entry_140120092399056 = get('entry', __marker)

                # <Value 'entries' (76:26)> -> __iterator
                __token = 2337
                try:
                    __zt_tmp = __attrs_140120092409472
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140120153207904('path', 'entries', econtext=econtext)(_static_140120153207616(econtext, __zt_tmp))
                (__iterator, ____index_140120092409712, ) = getname('repeat')('entry', __iterator)
                econtext['entry'] = None
                for __item in __iterator:
                    econtext['entry'] = __item

                    # <tr ... (0:0)
                    # --------------------------------------------------------
                    __append('<tr>\n\t\t\t\t\t')

                    # <Static value=<ast.Dict object at 0x7f70405604f0> name=None at 7f7040560520> -> __attrs_140120092444080
                    __attrs_140120092444080 = _static_140120092443888

                    # <td ... (0:0)
                    # --------------------------------------------------------
                    __append('<td class="zmi-time" style="white-space:nowrap">\n\t\t\t\t\t\t')

                    # <Static value=<ast.Dict object at 0x7f7043f50820> name=None at 7f7043f50b50> -> __attrs_140120092445760
                    __attrs_140120092445760 = _static_140120153196576

                    # <Symbol value=<DEFAULT> at 7f7043ee9570> -> __default_140120092445568
                    __default_140120092445568 = _DEFAULT_MARKER

                    # <Value "python: modules['DateTime'].DateTime(entry['time']).ISO()" (78:25)> -> __cache_140120092445088
                    __token = 2426
                    try:
                        __zt_tmp = __attrs_140120092445760
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140120092445088 = _static_140120153207904('python', " modules['DateTime'].DateTime(entry['time']).ISO()", econtext=econtext)(_static_140120153207616(econtext, __zt_tmp))

                    # <BinOp left=<Value "python: modules['DateTime'].DateTime(entry['time']).ISO()" (78:25)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7043ee9570> at 7f7040560a60> -> __condition
                    __expression = __cache_140120092445088

                    # <Symbol value=<DEFAULT> at 7f7043ee9570> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>2022-07-01 11:59:15</span>')
                    else:
                        __content = __cache_140120092445088
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('\n\t\t\t\t\t</td>\n\t\t\t\t\t')

                    # <Static value=<ast.Dict object at 0x7f7040560f70> name=None at 7f7040560fa0> -> __attrs_140120092446960
                    __attrs_140120092446960 = _static_140120092446576

                    # <td ... (0:0)
                    # --------------------------------------------------------
                    __append('<td class="zmi-username">\n\t\t\t\t\t\t')

                    # <Static value=<ast.Dict object at 0x7f7043f50820> name=None at 7f7043f50b50> -> __attrs_140120092448688
                    __attrs_140120092448688 = _static_140120153196576

                    # <Symbol value=<DEFAULT> at 7f7043ee9570> -> __default_140120092448496
                    __default_140120092448496 = _DEFAULT_MARKER

                    # <Value 'string: ${entry/username} (${entry/userid})' (81:25)> -> __cache_140120092447968
                    __token = 2579
                    try:
                        __zt_tmp = __attrs_140120092448688
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140120092447968 = _static_140120153207904('string', ' ${entry/username} (${entry/userid})', econtext=econtext)(_static_140120153207616(econtext, __zt_tmp))

                    # <BinOp left=<Value 'string: ${entry/username} (${entry/userid})' (81:25)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7043ee9570> at 7f70405615d0> -> __condition
                    __expression = __cache_140120092447968

                    # <Symbol value=<DEFAULT> at 7f7043ee9570> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>joe (joe)</span>')
                    else:
                        __content = __cache_140120092447968
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('\n\t\t\t\t\t</td>\n\t\t\t\t\t')

                    # <Static value=<ast.Dict object at 0x7f7040561ab0> name=None at 7f7040561ae0> -> __attrs_140120092449840
                    __attrs_140120092449840 = _static_140120092449456

                    # <td ... (0:0)
                    # --------------------------------------------------------
                    __append('<td class="zmi-exception">\n\t\t\t\t\t\t')

                    # <Static value=<ast.Dict object at 0x7f7040562020> name=None at 7f7040562050> -> __attrs_140120092451424
                    __attrs_140120092451424 = _static_140120092450848

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 7f7043ee9570> -> __default_140120092450608
                    __default_140120092450608 = _DEFAULT_MARKER

                    # <Substitution 'string:showEntry?id=${entry/id}' (84:47)> -> __attr_href
                    __token = 2731
                    try:
                        __zt_tmp = __attrs_140120092451424
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140120153207904('string', 'showEntry?id=${entry/id}', econtext=econtext)(_static_140120153207616(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', 'showEntry', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))
                    __append('>\n\t\t\t\t\t\t\t')

                    # <Static value=<ast.Dict object at 0x7f7043f50820> name=None at 7f7043f50b50> -> __attrs_140120092453056
                    __attrs_140120092453056 = _static_140120153196576

                    # <Symbol value=<DEFAULT> at 7f7043ee9570> -> __default_140120092452864
                    __default_140120092452864 = _DEFAULT_MARKER

                    # <Value 'entry/type' (85:26)> -> __cache_140120092452384
                    __token = 2791
                    try:
                        __zt_tmp = __attrs_140120092453056
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140120092452384 = _static_140120153207904('path', 'entry/type', econtext=econtext)(_static_140120153207616(econtext, __zt_tmp))

                    # <BinOp left=<Value 'entry/type' (85:26)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7043ee9570> at 7f70405626e0> -> __condition
                    __expression = __cache_140120092452384

                    # <Symbol value=<DEFAULT> at 7f7043ee9570> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>AttributeError</span>')
                    else:
                        __content = __cache_140120092452384
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(':\n\t\t\t\t\t\t\t')

                    # <Static value=<ast.Dict object at 0x7f7043f50820> name=None at 7f7043f50b50> -> __attrs_140120092454640
                    __attrs_140120092454640 = _static_140120153196576
                    __backup_value_140120092404144 = get('value', __marker)

                    # <Value 'entry/value' (86:31)> -> __value
                    __token = 2857
                    try:
                        __zt_tmp = __attrs_140120092454640
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140120153207904('path', 'entry/value', econtext=econtext)(_static_140120153207616(econtext, __zt_tmp))
                    econtext['value'] = __value

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span >')

                    # <Symbol value=<DEFAULT> at 7f7043ee9570> -> __default_140120092454064
                    __default_140120092454064 = _DEFAULT_MARKER

                    # <Value "python: len(value) < 70 and value or value[:70] + '...'" (87:21)> -> __cache_140120092453584
                    __token = 2891
                    try:
                        __zt_tmp = __attrs_140120092454640
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140120092453584 = _static_140120153207904('python', " len(value) < 70 and value or value[:70] + '...'", econtext=econtext)(_static_140120153207616(econtext, __zt_tmp))

                    # <BinOp left=<Value "python: len(value) < 70 and value or value[:70] + '...'" (87:21)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7043ee9570> at 7f7040562b90> -> __condition
                    __expression = __cache_140120092453584

                    # <Symbol value=<DEFAULT> at 7f7043ee9570> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('Application object has no attribute "zzope"')
                    else:
                        __content = __cache_140120092453584
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</span>')
                    if (__backup_value_140120092404144 is __marker):
                        del econtext['value']
                    else:
                        econtext['value'] = __backup_value_140120092404144
                    __append('\n\t\t\t\t\t\t</a>\n\t\t\t\t\t</td>\n\t\t\t\t\t')

                    # <Static value=<ast.Dict object at 0x7f7043f50820> name=None at 7f7043f50b50> -> __attrs_140120092455600
                    __attrs_140120092455600 = _static_140120153196576

                    # <td ... (0:0)
                    # --------------------------------------------------------
                    __append('<td>')

                    # <Static value=<ast.Dict object at 0x7f7040563610> name=None at 7f7040563640> -> __attrs_140120092457040
                    __attrs_140120092457040 = _static_140120092456464

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 7f7043ee9570> -> __default_140120092456080
                    __default_140120092456080 = _DEFAULT_MARKER

                    # <Substitution 'string:${context/absolute_url}/forgetEntry?id=${entry/id}' (91:42)> -> __attr_href
                    __token = 3075
                    try:
                        __zt_tmp = __attrs_140120092457040
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140120153207904('string', '${context/absolute_url}/forgetEntry?id=${entry/id}', econtext=econtext)(_static_140120153207616(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '#', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))
                    __append(' >Forget this entry</a></td>\n\t\t\t\t</tr>')
                    ____index_140120092409712 -= 1
                    if (____index_140120092409712 > 0):
                        __append('\n    ')
                if (__backup_entry_140120092399056 is __marker):
                    del econtext['entry']
                else:
                    econtext['entry'] = __backup_entry_140120092399056
                __append('\n\t\t\t</tbody>\n\t\t</table>')
            __append('\n\t</div>')
            if (__backup_entries_140120092201584 is __marker):
                del econtext['entries']
            else:
                econtext['entries'] = __backup_entries_140120092201584
            __append('\n\n\t')

            # <Static value=<ast.Dict object at 0x7f7040557f40> name=None at 7f7040557b20> -> __attrs_140120092457952
            __attrs_140120092457952 = _static_140120092409664

            # <form ... (0:0)
            # --------------------------------------------------------
            __append('<form action="manage_main" method="GET">\n\t\t')

            # <Static value=<ast.Dict object at 0x7f7040563fa0> name=None at 7f7040563fd0> -> __attrs_140120092459360
            __attrs_140120092459360 = _static_140120092458912

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="zmi-controls">\n\t\t\t')

            # <Static value=<ast.Dict object at 0x7f7040564a90> name=None at 7f7040564ac0> -> __attrs_140120092460512
            __attrs_140120092460512 = _static_140120092461712

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input class="btn btn-primary" type="submit" name="submit" value="Refresh" />\n\t\t</div>\n\t</form>\n\n')

            # <Static value=<ast.Dict object at 0x7f7043f50820> name=None at 7f7043f50b50> -> __attrs_140120092462624
            __attrs_140120092462624 = _static_140120153196576

            # <Symbol value=<DEFAULT> at 7f7043ee9570> -> __default_140120092462432
            __default_140120092462432 = _DEFAULT_MARKER

            # <Value 'context/manage_page_footer' (104:27)> -> __cache_140120092461952
            __token = 3408
            try:
                __zt_tmp = __attrs_140120092462624
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140120092461952 = _static_140120153207904('path', 'context/manage_page_footer', econtext=econtext)(_static_140120153207616(econtext, __zt_tmp))

            # <BinOp left=<Value 'context/manage_page_footer' (104:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f7043ee9570> at 7f7040564c40> -> __condition
            __expression = __cache_140120092461952

            # <Symbol value=<DEFAULT> at 7f7043ee9570> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append('<h1>Footer</h1>')
            else:
                __content = __cache_140120092461952
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }