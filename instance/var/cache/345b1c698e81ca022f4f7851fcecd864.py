# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/plone/z3cform/crud/crud-table.pt'

__tokens = {173: ('view/subforms', 5, 21), 268: ('view/label | nothing', 10, 21), 309: ('view/label', 11, 19), 395: ('view/status', 15, 22), 435: ('view/status', 17, 23), 549: ('view/getURL', 23, 17), 615: ('view/render_batch_navigation', 27, 38), 745: ('view/subforms', 31, 18), 825: ('python:len(rows) and rows[0] or None', 35, 20), 906: ('python:row1 is not None', 37, 28), 1012: ('row1/getTitleWidgets', 41, 33), 1060: (' row1/getNiceTitle', 42, 26), 1130: ('widgetsForTitles', 44, 33), 1216: ('repeat/widget/index', 48, 24), 1374: ('widget/field/description', 52, 26), 1425: (" python: 'header-' + niceTitles[idx", 53, 25), 1288: ('python: niceTitles[idx]', 50, 31), 1613: ("python:widget.required and widget.mode == 'input'", 60, 33), 1806: ('view/subforms', 68, 31), 1859: ('row/render', 69, 37), 2014: ('view/actions/values', 77, 29), 2104: ('action/render', 80, 36)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140097252722240 = {'type': 'submit', }
_static_140097252722288 = {'class': 'action', }
_static_140097252731600 = {'class': 'fieldRequired', }
_static_140097252734240 = {'title': 'widget/field/description', 'class': "python: 'header-' + niceTitles[idx]", }
_static_140097252726560 = {'class': 'table table-striped table-bordered', }
_static_140097252858256 = {'action': '.', 'method': 'post', }
_static_140097252863440 = {'class': 'alert alert-info', }
_static_140097412968080 = {}
_static_140097413192176 = __C2ZContextWrapper
_static_140097413192464 = __compile_zt_expr
_static_140097252862096 = {'xmlns': 'http://www.w3.org/1999/xhtml', }

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
            __append('\n')

            # <Static value=<ast.Dict object at 0x7f6aeefda890> name=None at 7f6aeefdb010> -> __attrs_140097252852928
            __attrs_140097252852928 = _static_140097252862096

            # <Value 'view/subforms' (5:21)> -> __condition
            __token = 173
            try:
                __zt_tmp = __attrs_140097252852928
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140097413192464('path', 'view/subforms', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_140097252855232 = __i18n_domain
                __i18n_domain = 'plone.z3cform'
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097252861760
                __attrs_140097252861760 = _static_140097412968080

                # <Value 'view/label | nothing' (10:21)> -> __condition
                __token = 268
                try:
                    __zt_tmp = __attrs_140097252861760
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140097413192464('path', 'view/label | nothing', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                if __condition:

                    # <h2 ... (0:0)
                    # --------------------------------------------------------
                    __append('<h2 >')

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252866512
                    __default_140097252866512 = _DEFAULT_MARKER

                    # <Value 'view/label' (11:19)> -> __cache_140097252852976
                    __token = 309
                    try:
                        __zt_tmp = __attrs_140097252861760
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140097252852976 = _static_140097413192464('path', 'view/label', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                    # <BinOp left=<Value 'view/label' (11:19)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeefdaaa0> -> __condition
                    __expression = __cache_140097252852976

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('Form title')
                    else:
                        __content = __cache_140097252852976
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</h2>')
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x7f6aeefdadd0> name=None at 7f6aeefd8fa0> -> __attrs_140097252856864
                __attrs_140097252856864 = _static_140097252863440

                # <Value 'view/status' (15:22)> -> __condition
                __token = 395
                try:
                    __zt_tmp = __attrs_140097252856864
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140097413192464('path', 'view/status', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="alert alert-info" >\n    ')

                    # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097252863632
                    __attrs_140097252863632 = _static_140097412968080

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>')

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252865360
                    __default_140097252865360 = _DEFAULT_MARKER

                    # <Value 'view/status' (17:23)> -> __cache_140097252857632
                    __token = 435
                    try:
                        __zt_tmp = __attrs_140097252863632
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140097252857632 = _static_140097413192464('path', 'view/status', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                    # <BinOp left=<Value 'view/status' (17:23)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeefdaa40> -> __condition
                    __expression = __cache_140097252857632

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140097252857632
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</span>\n  </div>')
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x7f6aeefd9990> name=None at 7f6aeefd8e80> -> __attrs_140097252867664
                __attrs_140097252867664 = _static_140097252858256

                # <form ... (0:0)
                # --------------------------------------------------------
                __append('<form')

                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252861424
                __default_140097252861424 = _DEFAULT_MARKER

                # <Substitution 'view/getURL' (23:17)> -> __attr_action
                __token = 549
                try:
                    __zt_tmp = __attrs_140097252867664
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_action = _static_140097413192464('path', 'view/getURL', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                __attr_action = __quote(__attr_action, '"', '&quot;', '.', _DEFAULT_MARKER)
                if (__attr_action is not None):
                    __append((' action="%s"' % __attr_action))
                __append(' method="post" >\n\n    ')

                # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097252867280
                __attrs_140097252867280 = _static_140097412968080

                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252866128
                __default_140097252866128 = _DEFAULT_MARKER

                # <Value 'view/render_batch_navigation' (27:38)> -> __cache_140097252857680
                __token = 615
                try:
                    __zt_tmp = __attrs_140097252867280
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140097252857680 = _static_140097413192464('path', 'view/render_batch_navigation', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                # <BinOp left=<Value 'view/render_batch_navigation' (27:38)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeefdbaf0> -> __condition
                __expression = __cache_140097252857680

                # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140097252857680
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n\n    ')

                # <Static value=<ast.Dict object at 0x7f6aeefb9720> name=None at 7f6aeefdbbb0> -> __attrs_140097252726032
                __attrs_140097252726032 = _static_140097252726560
                __backup_rows_140097252460576 = get('rows', __marker)

                # <Value 'view/subforms' (31:18)> -> __value
                __token = 745
                try:
                    __zt_tmp = __attrs_140097252726032
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140097413192464('path', 'view/subforms', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                econtext['rows'] = __value

                # <table ... (0:0)
                # --------------------------------------------------------
                __append('<table class="table table-striped table-bordered" >\n      ')

                # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097252734624
                __attrs_140097252734624 = _static_140097412968080
                __backup_row1_140097252262192 = get('row1', __marker)

                # <Value 'python:len(rows) and rows[0] or None' (35:20)> -> __value
                __token = 825
                try:
                    __zt_tmp = __attrs_140097252734624
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140097413192464('python', 'len(rows) and rows[0] or None', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                econtext['row1'] = __value

                # <Value 'python:row1 is not None' (37:28)> -> __condition
                __token = 906
                try:
                    __zt_tmp = __attrs_140097252734624
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140097413192464('python', 'row1 is not None', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                if __condition:

                    # <thead ... (0:0)
                    # --------------------------------------------------------
                    __append('<thead >\n        ')

                    # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097252735536
                    __attrs_140097252735536 = _static_140097412968080

                    # <tr ... (0:0)
                    # --------------------------------------------------------
                    __append('<tr>\n          ')

                    # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097252735488
                    __attrs_140097252735488 = _static_140097412968080
                    __backup_widgetsForTitles_140097252385232 = get('widgetsForTitles', __marker)

                    # <Value 'row1/getTitleWidgets' (41:33)> -> __value
                    __token = 1012
                    try:
                        __zt_tmp = __attrs_140097252735488
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140097413192464('path', 'row1/getTitleWidgets', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    econtext['widgetsForTitles'] = __value
                    __backup_niceTitles_140097252265552 = get('niceTitles', __marker)

                    # <Value 'row1/getNiceTitles' (42:26)> -> __value
                    __token = 1060
                    try:
                        __zt_tmp = __attrs_140097252735488
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140097413192464('path', 'row1/getNiceTitles', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    econtext['niceTitles'] = __value
                    __backup_widget_140097338176752 = get('widget', __marker)

                    # <Value 'widgetsForTitles' (44:33)> -> __iterator
                    __token = 1130
                    try:
                        __zt_tmp = __attrs_140097252735488
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_140097413192464('path', 'widgetsForTitles', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    (__iterator, ____index_140097252729056, ) = getname('repeat')('widget', __iterator)
                    econtext['widget'] = None
                    for __item in __iterator:
                        econtext['widget'] = __item

                        # <th ... (0:0)
                        # --------------------------------------------------------
                        __append('<th >\n\n            ')

                        # <Static value=<ast.Dict object at 0x7f6aeefbb520> name=None at 7f6aeefb9390> -> __attrs_140097252729776
                        __attrs_140097252729776 = _static_140097252734240
                        __backup_idx_140097338177520 = get('idx', __marker)

                        # <Value 'repeat/widget/index' (48:24)> -> __value
                        __token = 1216
                        try:
                            __zt_tmp = __attrs_140097252729776
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140097413192464('path', 'repeat/widget/index', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        econtext['idx'] = __value

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span')

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252728768
                        __default_140097252728768 = _DEFAULT_MARKER

                        # <Substitution 'widget/field/description' (52:26)> -> __attr_title
                        __token = 1374
                        try:
                            __zt_tmp = __attrs_140097252729776
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_title = _static_140097413192464('path', 'widget/field/description', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_title is not None):
                            __append((' title="%s"' % __attr_title))

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252732416
                        __default_140097252732416 = _DEFAULT_MARKER

                        # <Substitution "python: 'header-' + niceTitles[idx]" (53:25)> -> __attr_class
                        __token = 1425
                        try:
                            __zt_tmp = __attrs_140097252729776
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_class = _static_140097413192464('python', " 'header-' + niceTitles[idx]", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_class is not None):
                            __append((' class="%s"' % __attr_class))
                        __append(' >')

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252730640
                        __default_140097252730640 = _DEFAULT_MARKER

                        # <Value 'python: niceTitles[idx]' (50:31)> -> __cache_140097252735008
                        __token = 1288
                        try:
                            __zt_tmp = __attrs_140097252729776
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140097252735008 = _static_140097413192464('python', ' niceTitles[idx]', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                        # <BinOp left=<Value 'python: niceTitles[idx]' (50:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeefbadd0> -> __condition
                        __expression = __cache_140097252735008

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('\n                Field\n            ')
                        else:
                            __content = __cache_140097252735008
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</span>')
                        if (__backup_idx_140097338177520 is __marker):
                            del econtext['idx']
                        else:
                            econtext['idx'] = __backup_idx_140097338177520
                        __append('\n\n            ')

                        # <Static value=<ast.Dict object at 0x7f6aeefbaad0> name=None at 7f6aeefbb490> -> __attrs_140097252729344
                        __attrs_140097252729344 = _static_140097252731600

                        # <Value "python:widget.required and widget.mode == 'input'" (60:33)> -> __condition
                        __token = 1613
                        try:
                            __zt_tmp = __attrs_140097252729344
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140097413192464('python', "widget.required and widget.mode == 'input'", econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span class="fieldRequired" >\n                *\n            </span>')
                        __append('\n          </th>')
                        ____index_140097252729056 -= 1
                        if (____index_140097252729056 > 0):
                            __append('\n          ')
                    if (__backup_widget_140097338176752 is __marker):
                        del econtext['widget']
                    else:
                        econtext['widget'] = __backup_widget_140097338176752
                    if (__backup_niceTitles_140097252265552 is __marker):
                        del econtext['niceTitles']
                    else:
                        econtext['niceTitles'] = __backup_niceTitles_140097252265552
                    if (__backup_widgetsForTitles_140097252385232 is __marker):
                        del econtext['widgetsForTitles']
                    else:
                        econtext['widgetsForTitles'] = __backup_widgetsForTitles_140097252385232
                    __append('\n        </tr>\n      </thead>')
                if (__backup_row1_140097252262192 is __marker):
                    del econtext['row1']
                else:
                    econtext['row1'] = __backup_row1_140097252262192
                __append('\n      ')

                # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097252723344
                __attrs_140097252723344 = _static_140097412968080

                # <tbody ... (0:0)
                # --------------------------------------------------------
                __append('<tbody>\n        ')

                # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097252732320
                __attrs_140097252732320 = _static_140097412968080
                __backup_row_140097339175264 = get('row', __marker)

                # <Value 'view/subforms' (68:31)> -> __iterator
                __token = 1806
                try:
                    __zt_tmp = __attrs_140097252732320
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140097413192464('path', 'view/subforms', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                (__iterator, ____index_140097252727280, ) = getname('repeat')('row', __iterator)
                econtext['row'] = None
                for __item in __iterator:
                    econtext['row'] = __item
                    __append('\n          ')

                    # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097252730064
                    __attrs_140097252730064 = _static_140097412968080

                    # <tr ... (0:0)
                    # --------------------------------------------------------
                    __append('<tr>')

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252723872
                    __default_140097252723872 = _DEFAULT_MARKER

                    # <Value 'row/render' (69:37)> -> __cache_140097252727664
                    __token = 1859
                    try:
                        __zt_tmp = __attrs_140097252730064
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140097252727664 = _static_140097413192464('path', 'row/render', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                    # <BinOp left=<Value 'row/render' (69:37)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeefb90c0> -> __condition
                    __expression = __cache_140097252727664

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n            ')

                        # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097252727616
                        __attrs_140097252727616 = _static_140097412968080

                        # <td ... (0:0)
                        # --------------------------------------------------------
                        __append('<td></td>\n          ')
                    else:
                        __content = __cache_140097252727664
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('</tr>\n        ')
                    ____index_140097252727280 -= 1
                    if (____index_140097252727280 > 0):
                        __append('')
                if (__backup_row_140097339175264 is __marker):
                    del econtext['row']
                else:
                    econtext['row'] = __backup_row_140097339175264
                __append('\n      </tbody>\n    </table>')
                if (__backup_rows_140097252460576 is __marker):
                    del econtext['rows']
                else:
                    econtext['rows'] = __backup_rows_140097252460576
                __append('\n\n    ')

                # <Static value=<ast.Dict object at 0x7f6aeefb8670> name=None at 7f6aeefb8700> -> __attrs_140097252721664
                __attrs_140097252721664 = _static_140097252722288
                __backup_action_140097252392000 = get('action', __marker)

                # <Value 'view/actions/values' (77:29)> -> __iterator
                __token = 2014
                try:
                    __zt_tmp = __attrs_140097252721664
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140097413192464('path', 'view/actions/values', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                (__iterator, ____index_140097252721088, ) = getname('repeat')('action', __iterator)
                econtext['action'] = None
                for __item in __iterator:
                    econtext['action'] = __item

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span class="action" >\n      ')

                    # <Static value=<ast.Dict object at 0x7f6aeefb8640> name=None at 7f6aeefb92d0> -> __attrs_140097338458512
                    __attrs_140097338458512 = _static_140097252722240

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338461008
                    __default_140097338461008 = _DEFAULT_MARKER

                    # <Value 'action/render' (80:36)> -> __cache_140097252726608
                    __token = 2104
                    try:
                        __zt_tmp = __attrs_140097338458512
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140097252726608 = _static_140097413192464('path', 'action/render', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                    # <BinOp left=<Value 'action/render' (80:36)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6af417f3a0> -> __condition
                    __expression = __cache_140097252726608

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input type="submit" />')
                    else:
                        __content = __cache_140097252726608
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('\n    </span>')
                    ____index_140097252721088 -= 1
                    if (____index_140097252721088 > 0):
                        __append('\n    ')
                if (__backup_action_140097252392000 is __marker):
                    del econtext['action']
                else:
                    econtext['action'] = __backup_action_140097252392000
                __append('\n\n  </form>\n\n')
                __i18n_domain = __previous_i18n_domain_140097252855232
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }