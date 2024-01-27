# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/plone/batching/batchnavigation.pt'

__tokens = {132: ('view/batch|nothing', 4, 29), 207: ('batch', 6, 32), 284: ('batch/multiple_pages', 10, 22), 395: ('nothing', 16, 28), 519: ('batch/has_previous', 20, 25), 622: ('python:view.make_link(batch.previouspage)', 24, 18), 885: ('batch/pagesize', 32, 31), 1085: ('nothing', 41, 28), 1203: ('batch/show_link_to_first', 45, 25), 1312: ('python:view.make_link(1)', 49, 18), 1407: ('nothing', 54, 28), 1543: ('batch/second_page_not_in_navlist', 58, 25), 1651: ('nothing', 63, 28), 1819: ('batch/previous_pages', 67, 33), 1960: ('python:view.make_link(pagenumber)', 72, 18), 1902: ('pagenumber', 70, 24), 2063: ('nothing', 77, 28), 2213: ('batch/navlist', 82, 25), 2295: ('batch/pagenumber', 85, 27), 2459: ('nothing', 92, 28), 2623: ('batch/next_pages', 96, 33), 2760: ('python:view.make_link(pagenumber)', 101, 18), 2702: ('pagenumber', 99, 24), 2863: ('nothing', 106, 28), 2999: ('batch/before_last_page_not_in_navlist', 110, 25), 3130: ('nothing', 115, 28), 3246: ('batch/show_link_to_last', 119, 25), 3394: ('python:view.make_link(batch.lastpage)', 124, 18), 3332: ('batch/lastpage', 122, 24), 3501: ('nothing', 129, 28), 3617: ('batch/has_next', 133, 25), 3716: ('python:view.make_link(batch.nextpage)', 137, 18), 3920: ('batch/next_item_count', 144, 31)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140097252668032 = {'aria-hidden': 'true', }
_static_140097252662560 = {'class': 'label', }
_static_140097252658816 = {'class': 'page-link', 'href': 'python:view.make_link(batch.nextpage)', }
_static_140097252670768 = {'class': 'page-item next', }
_static_140097252671440 = {'class': 'page-link', 'href': 'python:view.make_link(batch.lastpage)', }
_static_140097338351600 = {'class': 'page-item last', }
_static_140097338358896 = {'class': 'page-link', }
_static_140097338353712 = {'class': 'page-item disabled', }
_static_140097338346032 = {'class': 'page-link', 'href': 'python:view.make_link(pagenumber)', }
_static_140097252064896 = {'class': 'page-item', }
_static_140097252058944 = {'class': 'sr-only', }
_static_140097252053616 = {'class': 'page-link', }
_static_140097252055632 = {'class': 'page-item active', 'aria-current': 'page', }
_static_140097252064128 = {'class': 'page-link', 'href': 'python:view.make_link(pagenumber)', }
_static_140097252062928 = {'class': 'page-item', }
_static_140097252064608 = {'class': 'page-item disabled', }
_static_140097364941536 = {'class': 'page-link', 'href': 'python:view.make_link(1)', }
_static_140097344272032 = {'class': 'first page-item', }
_static_140097342597552 = {'class': 'label', }
_static_140097342600576 = {'aria-hidden': 'true', }
_static_140097364815840 = {'class': 'page-link', 'href': 'python:view.make_link(batch.previouspage)', }
_static_140097339903088 = {'class': 'page-item previous', }
_static_140097339900976 = {'class': 'pagination', }
_static_140097339916240 = {'class': 'd-flex justify-content-center', }
_static_140097413192176 = __C2ZContextWrapper
_static_140097413192464 = __compile_zt_expr
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

    def render_navigation(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097340843024
            __attrs_140097340843024 = _static_140097412968080
            __backup_batch_140097252064320 = get('batch', __marker)

            # <Value 'view/batch|nothing' (4:29)> -> __value
            __token = 132
            try:
                __zt_tmp = __attrs_140097340843024
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140097413192464('path', 'view/batch|nothing', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            econtext['batch'] = __value

            # <Value 'batch' (6:32)> -> __condition
            __token = 207
            try:
                __zt_tmp = __attrs_140097340843024
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140097413192464('path', 'batch', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            if __condition:
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x7f6af42dffd0> name=None at 7f6af42dc040> -> __attrs_140097339903856
                __attrs_140097339903856 = _static_140097339916240

                # <Value 'batch/multiple_pages' (10:22)> -> __condition
                __token = 284
                try:
                    __zt_tmp = __attrs_140097339903856
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140097413192464('path', 'batch/multiple_pages', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                if __condition:
                    __previous_i18n_domain_140097339912016 = __i18n_domain
                    __i18n_domain = 'plone'

                    # <nav ... (0:0)
                    # --------------------------------------------------------
                    __append('<nav class="d-flex justify-content-center" >\n\n    ')

                    # <Static value=<ast.Dict object at 0x7f6af42dc430> name=None at 7f6af42df8e0> -> __attrs_140097339902656
                    __attrs_140097339902656 = _static_140097339900976

                    # <ul ... (0:0)
                    # --------------------------------------------------------
                    __append('<ul class="pagination">\n\n      ')

                    # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097339911776
                    __attrs_140097339911776 = _static_140097412968080

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097339915472
                    __default_140097339915472 = _DEFAULT_MARKER

                    # <Value 'nothing' (16:28)> -> __cache_140097339914608
                    __token = 395
                    try:
                        __zt_tmp = __attrs_140097339911776
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140097339914608 = _static_140097413192464('path', 'nothing', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                    # <BinOp left=<Value 'nothing' (16:28)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6af42dfd30> -> __condition
                    __expression = __cache_140097339914608

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n        <!-- Previous page -->\n      ')
                    else:
                        __content = __cache_140097339914608
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('\n      ')

                    # <Static value=<ast.Dict object at 0x7f6af42dcc70> name=None at 7f6af42defb0> -> __attrs_140097339911728
                    __attrs_140097339911728 = _static_140097339903088

                    # <Value 'batch/has_previous' (20:25)> -> __condition
                    __token = 519
                    try:
                        __zt_tmp = __attrs_140097339911728
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140097413192464('path', 'batch/has_previous', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    if __condition:

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li class="page-item previous" >\n        ')

                        # <Static value=<ast.Dict object at 0x7f6af5a9efe0> name=None at 7f6af5a9f850> -> __attrs_140097342597360
                        __attrs_140097342597360 = _static_140097364815840

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append('<a class="page-link"')

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097364815648
                        __default_140097364815648 = _DEFAULT_MARKER

                        # <Substitution 'python:view.make_link(batch.previouspage)' (24:18)> -> __attr_href
                        __token = 622
                        try:
                            __zt_tmp = __attrs_140097342597360
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_140097413192464('python', 'view.make_link(batch.previouspage)', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((' href="%s"' % __attr_href))
                        __append(' >\n          ')

                        # <Static value=<ast.Dict object at 0x7f6af456f580> name=None at 7f6af456f190> -> __attrs_140097342594864
                        __attrs_140097342594864 = _static_140097342600576

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span aria-hidden="true">&lt;</span>\n          ')

                        # <Static value=<ast.Dict object at 0x7f6af456e9b0> name=None at 7f6af456e9e0> -> __attrs_140097342857872
                        __attrs_140097342857872 = _static_140097342597552

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="label" >')
                        __stream_140097344498016_number = ''
                        __stream_140097342595152 = []
                        __append_140097342595152 = __stream_140097342595152.append
                        __append_140097342595152('\n            Previous\n            ')
                        __stream_140097344498016_number = []
                        __append_140097344498016_number = __stream_140097344498016_number.append

                        # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097344343824
                        __attrs_140097344343824 = _static_140097412968080

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097339401952
                        __default_140097339401952 = _DEFAULT_MARKER

                        # <Value 'batch/pagesize' (32:31)> -> __cache_140097342413056
                        __token = 885
                        try:
                            __zt_tmp = __attrs_140097344343824
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140097342413056 = _static_140097413192464('path', 'batch/pagesize', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                        # <BinOp left=<Value 'batch/pagesize' (32:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6af45404f0> -> __condition
                        __expression = __cache_140097342413056

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append_140097344498016_number('n')
                        else:
                            __content = __cache_140097342413056
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append_140097344498016_number(__content)
                        __append_140097342595152('${number}')
                        __stream_140097344498016_number = ''.join(__stream_140097344498016_number)
                        __append_140097342595152('\n             items\n          ')
                        __msgid_140097342595152 = __re_whitespace(''.join(__stream_140097342595152)).strip()
                        if 'batch_previous_x_items':
                            __append(translate('batch_previous_x_items', mapping={'number': __stream_140097344498016_number, }, default=__msgid_140097342595152, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</span>\n        </a>\n      </li>')
                    __append('\n\n      ')

                    # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097344175792
                    __attrs_140097344175792 = _static_140097412968080

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097344170656
                    __default_140097344170656 = _DEFAULT_MARKER

                    # <Value 'nothing' (41:28)> -> __cache_140097339394464
                    __token = 1085
                    try:
                        __zt_tmp = __attrs_140097344175792
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140097339394464 = _static_140097413192464('path', 'nothing', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                    # <BinOp left=<Value 'nothing' (41:28)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6af5aa3250> -> __condition
                    __expression = __cache_140097339394464

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n        <!-- First page -->\n      ')
                    else:
                        __content = __cache_140097339394464
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('\n      ')

                    # <Static value=<ast.Dict object at 0x7f6af47076a0> name=None at 7f6af46ee440> -> __attrs_140097364941680
                    __attrs_140097364941680 = _static_140097344272032

                    # <Value 'batch/show_link_to_first' (45:25)> -> __condition
                    __token = 1203
                    try:
                        __zt_tmp = __attrs_140097364941680
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140097413192464('path', 'batch/show_link_to_first', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    if __condition:

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li class="first page-item" >\n        ')

                        # <Static value=<ast.Dict object at 0x7f6af5abdae0> name=None at 7f6af5abd840> -> __attrs_140097342125104
                        __attrs_140097342125104 = _static_140097364941536

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append('<a class="page-link"')

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097364940816
                        __default_140097364940816 = _DEFAULT_MARKER

                        # <Substitution 'python:view.make_link(1)' (49:18)> -> __attr_href
                        __token = 1312
                        try:
                            __zt_tmp = __attrs_140097342125104
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_140097413192464('python', 'view.make_link(1)', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((' href="%s"' % __attr_href))
                        __append(' >1</a>\n      </li>')
                    __append('\n\n      ')

                    # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097342120832
                    __attrs_140097342120832 = _static_140097412968080

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097342124912
                    __default_140097342124912 = _DEFAULT_MARKER

                    # <Value 'nothing' (54:28)> -> __cache_140097342123472
                    __token = 1407
                    try:
                        __zt_tmp = __attrs_140097342120832
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140097342123472 = _static_140097413192464('path', 'nothing', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                    # <BinOp left=<Value 'nothing' (54:28)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6af44fb5b0> -> __condition
                    __expression = __cache_140097342123472

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n        <!-- Ellipsis after first item -->\n      ')
                    else:
                        __content = __cache_140097342123472
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('\n      ')

                    # <Static value=<ast.Dict object at 0x7f6aeef17d60> name=None at 7f6af44fb160> -> __attrs_140097252054528
                    __attrs_140097252054528 = _static_140097252064608

                    # <Value 'batch/second_page_not_in_navlist' (58:25)> -> __condition
                    __token = 1543
                    try:
                        __zt_tmp = __attrs_140097252054528
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140097413192464('path', 'batch/second_page_not_in_navlist', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    if __condition:

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li class="page-item disabled" >\n        ')

                        # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097252060768
                        __attrs_140097252060768 = _static_140097412968080

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>...</span>\n      </li>')
                    __append('\n\n      ')

                    # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097252061392
                    __attrs_140097252061392 = _static_140097412968080

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252060288
                    __default_140097252060288 = _DEFAULT_MARKER

                    # <Value 'nothing' (63:28)> -> __cache_140097252061728
                    __token = 1651
                    try:
                        __zt_tmp = __attrs_140097252061392
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140097252061728 = _static_140097413192464('path', 'nothing', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                    # <BinOp left=<Value 'nothing' (63:28)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeef175e0> -> __condition
                    __expression = __cache_140097252061728

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n        <!-- Pagelist with links to previous pages for quick navigation -->\n      ')
                    else:
                        __content = __cache_140097252061728
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('\n      ')

                    # <Static value=<ast.Dict object at 0x7f6aeef176d0> name=None at 7f6aeef176a0> -> __attrs_140097252051216
                    __attrs_140097252051216 = _static_140097252062928
                    __backup_pagenumber_140097252061104 = get('pagenumber', __marker)

                    # <Value 'batch/previous_pages' (67:33)> -> __iterator
                    __token = 1819
                    try:
                        __zt_tmp = __attrs_140097252051216
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_140097413192464('path', 'batch/previous_pages', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    (__iterator, ____index_140097252062544, ) = getname('repeat')('pagenumber', __iterator)
                    econtext['pagenumber'] = None
                    for __item in __iterator:
                        econtext['pagenumber'] = __item

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li class="page-item" >\n        ')

                        # <Static value=<ast.Dict object at 0x7f6aeef17b80> name=None at 7f6aeef14190> -> __attrs_140097252055776
                        __attrs_140097252055776 = _static_140097252064128

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append('<a class="page-link"')

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252061680
                        __default_140097252061680 = _DEFAULT_MARKER

                        # <Substitution 'python:view.make_link(pagenumber)' (72:18)> -> __attr_href
                        __token = 1960
                        try:
                            __zt_tmp = __attrs_140097252055776
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_140097413192464('python', 'view.make_link(pagenumber)', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((' href="%s"' % __attr_href))
                        __append(' >')

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252058080
                        __default_140097252058080 = _DEFAULT_MARKER

                        # <Value 'pagenumber' (70:24)> -> __cache_140097252054288
                        __token = 1902
                        try:
                            __zt_tmp = __attrs_140097252055776
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140097252054288 = _static_140097413192464('path', 'pagenumber', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                        # <BinOp left=<Value 'pagenumber' (70:24)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeef166b0> -> __condition
                        __expression = __cache_140097252054288

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140097252054288
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</a>\n      </li>')
                        ____index_140097252062544 -= 1
                        if (____index_140097252062544 > 0):
                            __append('\n      ')
                    if (__backup_pagenumber_140097252061104 is __marker):
                        del econtext['pagenumber']
                    else:
                        econtext['pagenumber'] = __backup_pagenumber_140097252061104
                    __append('\n\n      ')

                    # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097252056160
                    __attrs_140097252056160 = _static_140097412968080

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252056448
                    __default_140097252056448 = _DEFAULT_MARKER

                    # <Value 'nothing' (77:28)> -> __cache_140097252056064
                    __token = 2063
                    try:
                        __zt_tmp = __attrs_140097252056160
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140097252056064 = _static_140097413192464('path', 'nothing', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                    # <BinOp left=<Value 'nothing' (77:28)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeef145b0> -> __condition
                    __expression = __cache_140097252056064

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n        <!-- Active page -->\n      ')
                    else:
                        __content = __cache_140097252056064
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('\n      ')

                    # <Static value=<ast.Dict object at 0x7f6aeef15a50> name=None at 7f6aeef15a20> -> __attrs_140097252055056
                    __attrs_140097252055056 = _static_140097252055632

                    # <Value 'batch/navlist' (82:25)> -> __condition
                    __token = 2213
                    try:
                        __zt_tmp = __attrs_140097252055056
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140097413192464('path', 'batch/navlist', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    if __condition:

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li class="page-item active" aria-current="page" >\n        ')

                        # <Static value=<ast.Dict object at 0x7f6aeef15270> name=None at 7f6aeef147c0> -> __attrs_140097252058560
                        __attrs_140097252058560 = _static_140097252053616

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="page-link" >')

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252053088
                        __default_140097252053088 = _DEFAULT_MARKER

                        # <Value 'batch/pagenumber' (85:27)> -> __cache_140097252063552
                        __token = 2295
                        try:
                            __zt_tmp = __attrs_140097252058560
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140097252063552 = _static_140097413192464('path', 'batch/pagenumber', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                        # <BinOp left=<Value 'batch/pagenumber' (85:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeef178e0> -> __condition
                        __expression = __cache_140097252063552

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140097252063552
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</span>\n        ')

                        # <Static value=<ast.Dict object at 0x7f6aeef16740> name=None at 7f6aeef16b90> -> __attrs_140097252051120
                        __attrs_140097252051120 = _static_140097252058944

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="sr-only" >')
                        __stream_140097252059760 = []
                        __append_140097252059760 = __stream_140097252059760.append
                        __msgid_140097252059760 = __re_whitespace(''.join(__stream_140097252059760)).strip()
                        if '(current)':
                            __append(translate('(current)', mapping=None, default=__msgid_140097252059760, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</span>\n      </li>')
                    __append('\n\n      ')

                    # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097252053520
                    __attrs_140097252053520 = _static_140097412968080

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252051696
                    __default_140097252051696 = _DEFAULT_MARKER

                    # <Value 'nothing' (92:28)> -> __cache_140097252053136
                    __token = 2459
                    try:
                        __zt_tmp = __attrs_140097252053520
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140097252053136 = _static_140097413192464('path', 'nothing', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                    # <BinOp left=<Value 'nothing' (92:28)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeef14970> -> __condition
                    __expression = __cache_140097252053136

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n        <!-- Pagelist with links to next pages for quick navigation -->\n      ')
                    else:
                        __content = __cache_140097252053136
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('\n      ')

                    # <Static value=<ast.Dict object at 0x7f6aeef17e80> name=None at 7f6aeef15450> -> __attrs_140097338347136
                    __attrs_140097338347136 = _static_140097252064896
                    __backup_pagenumber_140097252058512 = get('pagenumber', __marker)

                    # <Value 'batch/next_pages' (96:33)> -> __iterator
                    __token = 2623
                    try:
                        __zt_tmp = __attrs_140097338347136
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_140097413192464('path', 'batch/next_pages', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    (__iterator, ____index_140097338344736, ) = getname('repeat')('pagenumber', __iterator)
                    econtext['pagenumber'] = None
                    for __item in __iterator:
                        econtext['pagenumber'] = __item

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li class="page-item" >\n        ')

                        # <Static value=<ast.Dict object at 0x7f6af4160a30> name=None at 7f6af41604c0> -> __attrs_140097338349248
                        __attrs_140097338349248 = _static_140097338346032

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append('<a class="page-link"')

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338355872
                        __default_140097338355872 = _DEFAULT_MARKER

                        # <Substitution 'python:view.make_link(pagenumber)' (101:18)> -> __attr_href
                        __token = 2760
                        try:
                            __zt_tmp = __attrs_140097338349248
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_140097413192464('python', 'view.make_link(pagenumber)', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((' href="%s"' % __attr_href))
                        __append(' >')

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338347328
                        __default_140097338347328 = _DEFAULT_MARKER

                        # <Value 'pagenumber' (99:24)> -> __cache_140097338352560
                        __token = 2702
                        try:
                            __zt_tmp = __attrs_140097338349248
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140097338352560 = _static_140097413192464('path', 'pagenumber', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                        # <BinOp left=<Value 'pagenumber' (99:24)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6af4162ce0> -> __condition
                        __expression = __cache_140097338352560

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140097338352560
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</a>\n      </li>')
                        ____index_140097338344736 -= 1
                        if (____index_140097338344736 > 0):
                            __append('\n      ')
                    if (__backup_pagenumber_140097252058512 is __marker):
                        del econtext['pagenumber']
                    else:
                        econtext['pagenumber'] = __backup_pagenumber_140097252058512
                    __append('\n\n      ')

                    # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097338357504
                    __attrs_140097338357504 = _static_140097412968080

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338354048
                    __default_140097338354048 = _DEFAULT_MARKER

                    # <Value 'nothing' (106:28)> -> __cache_140097338351216
                    __token = 2863
                    try:
                        __zt_tmp = __attrs_140097338357504
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140097338351216 = _static_140097413192464('path', 'nothing', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                    # <BinOp left=<Value 'nothing' (106:28)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6af4162fe0> -> __condition
                    __expression = __cache_140097338351216

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n        <!-- Ellipsis before last item -->\n      ')
                    else:
                        __content = __cache_140097338351216
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('\n      ')

                    # <Static value=<ast.Dict object at 0x7f6af4162830> name=None at 7f6af4161b70> -> __attrs_140097338345216
                    __attrs_140097338345216 = _static_140097338353712

                    # <Value 'batch/before_last_page_not_in_navlist' (110:25)> -> __condition
                    __token = 2999
                    try:
                        __zt_tmp = __attrs_140097338345216
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140097413192464('path', 'batch/before_last_page_not_in_navlist', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    if __condition:

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li class="page-item disabled" >\n        ')

                        # <Static value=<ast.Dict object at 0x7f6af4163c70> name=None at 7f6af4162cb0> -> __attrs_140097338349632
                        __attrs_140097338349632 = _static_140097338358896

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="page-link">...</span>\n      </li>')
                    __append('\n\n      ')

                    # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097338351120
                    __attrs_140097338351120 = _static_140097412968080

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338357888
                    __default_140097338357888 = _DEFAULT_MARKER

                    # <Value 'nothing' (115:28)> -> __cache_140097338349872
                    __token = 3130
                    try:
                        __zt_tmp = __attrs_140097338351120
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140097338349872 = _static_140097413192464('path', 'nothing', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                    # <BinOp left=<Value 'nothing' (115:28)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6af4160d00> -> __condition
                    __expression = __cache_140097338349872

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n        <!-- Last page -->\n      ')
                    else:
                        __content = __cache_140097338349872
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('\n      ')

                    # <Static value=<ast.Dict object at 0x7f6af4161ff0> name=None at 7f6af41630d0> -> __attrs_140097252662464
                    __attrs_140097252662464 = _static_140097338351600

                    # <Value 'batch/show_link_to_last' (119:25)> -> __condition
                    __token = 3246
                    try:
                        __zt_tmp = __attrs_140097252662464
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140097413192464('path', 'batch/show_link_to_last', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    if __condition:

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li class="page-item last" >\n        ')

                        # <Static value=<ast.Dict object at 0x7f6aeefabfd0> name=None at 7f6aeefaa3b0> -> __attrs_140097252664720
                        __attrs_140097252664720 = _static_140097252671440

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append('<a class="page-link"')

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252659152
                        __default_140097252659152 = _DEFAULT_MARKER

                        # <Substitution 'python:view.make_link(batch.lastpage)' (124:18)> -> __attr_href
                        __token = 3394
                        try:
                            __zt_tmp = __attrs_140097252664720
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_140097413192464('python', 'view.make_link(batch.lastpage)', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((' href="%s"' % __attr_href))
                        __append(' >')

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252659392
                        __default_140097252659392 = _DEFAULT_MARKER

                        # <Value 'batch/lastpage' (122:24)> -> __cache_140097252658480
                        __token = 3332
                        try:
                            __zt_tmp = __attrs_140097252664720
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140097252658480 = _static_140097413192464('path', 'batch/lastpage', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                        # <BinOp left=<Value 'batch/lastpage' (122:24)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeefa8ca0> -> __condition
                        __expression = __cache_140097252658480

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140097252658480
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</a>\n      </li>')
                    __append('\n\n      ')

                    # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097252663232
                    __attrs_140097252663232 = _static_140097412968080

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252666592
                    __default_140097252666592 = _DEFAULT_MARKER

                    # <Value 'nothing' (129:28)> -> __cache_140097252662176
                    __token = 3501
                    try:
                        __zt_tmp = __attrs_140097252663232
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140097252662176 = _static_140097413192464('path', 'nothing', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                    # <BinOp left=<Value 'nothing' (129:28)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeefa88e0> -> __condition
                    __expression = __cache_140097252662176

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n        <!-- Next page -->\n      ')
                    else:
                        __content = __cache_140097252662176
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('\n      ')

                    # <Static value=<ast.Dict object at 0x7f6aeefabd30> name=None at 7f6aeefa8700> -> __attrs_140097252667744
                    __attrs_140097252667744 = _static_140097252670768

                    # <Value 'batch/has_next' (133:25)> -> __condition
                    __token = 3617
                    try:
                        __zt_tmp = __attrs_140097252667744
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140097413192464('path', 'batch/has_next', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    if __condition:

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li class="page-item next" >\n        ')

                        # <Static value=<ast.Dict object at 0x7f6aeefa8e80> name=None at 7f6aeefa9b10> -> __attrs_140097252659200
                        __attrs_140097252659200 = _static_140097252658816

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append('<a class="page-link"')

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252656944
                        __default_140097252656944 = _DEFAULT_MARKER

                        # <Substitution 'python:view.make_link(batch.nextpage)' (137:18)> -> __attr_href
                        __token = 3716
                        try:
                            __zt_tmp = __attrs_140097252659200
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_140097413192464('python', 'view.make_link(batch.nextpage)', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((' href="%s"' % __attr_href))
                        __append(' >\n          ')

                        # <Static value=<ast.Dict object at 0x7f6aeefa9d20> name=None at 7f6aeefa8b80> -> __attrs_140097252659296
                        __attrs_140097252659296 = _static_140097252662560

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="label" >')
                        __stream_140097339280288_number = ''
                        __stream_140097252667840 = []
                        __append_140097252667840 = __stream_140097252667840.append
                        __append_140097252667840('\n            Next\n            ')
                        __stream_140097339280288_number = []
                        __append_140097339280288_number = __stream_140097339280288_number.append

                        # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097252660064
                        __attrs_140097252660064 = _static_140097412968080

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252665248
                        __default_140097252665248 = _DEFAULT_MARKER

                        # <Value 'batch/next_item_count' (144:31)> -> __cache_140097252666976
                        __token = 3920
                        try:
                            __zt_tmp = __attrs_140097252660064
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140097252666976 = _static_140097413192464('path', 'batch/next_item_count', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                        # <BinOp left=<Value 'batch/next_item_count' (144:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeefa9180> -> __condition
                        __expression = __cache_140097252666976

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append_140097339280288_number('n')
                        else:
                            __content = __cache_140097252666976
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append_140097339280288_number(__content)
                        __append_140097252667840('${number}')
                        __stream_140097339280288_number = ''.join(__stream_140097339280288_number)
                        __append_140097252667840('\n            items\n          ')
                        __msgid_140097252667840 = __re_whitespace(''.join(__stream_140097252667840)).strip()
                        if 'batch_next_x_items':
                            __append(translate('batch_next_x_items', mapping={'number': __stream_140097339280288_number, }, default=__msgid_140097252667840, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</span>\n          ')

                        # <Static value=<ast.Dict object at 0x7f6aeefab280> name=None at 7f6aeefaae00> -> __attrs_140097252663712
                        __attrs_140097252663712 = _static_140097252668032

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span aria-hidden="true">&gt;</span>\n        </a>\n      </li>')
                    __append('\n    </ul>\n\n  </nav>')
                    __i18n_domain = __previous_i18n_domain_140097339912016
                __append('\n\n')
            if (__backup_batch_140097252064320 is __marker):
                del econtext['batch']
            else:
                econtext['batch'] = __backup_batch_140097252064320
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
            __append('<!-- Navigation -->\n')
            __token = None
            render_navigation(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_navigation': render_navigation, 'render': render, }