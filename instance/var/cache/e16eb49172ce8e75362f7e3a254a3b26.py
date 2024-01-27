# -*- coding: utf-8 -*-
__filename = '/mnt/d/mylinuxprojects/training/backend/venv/lib/python3.10/site-packages/Products/CMFPlone/controlpanel/browser/quickinstaller.pt'

__tokens = {1150: ('view/get_upgrades', 35, 36), 1208: (' python:len(products', 36, 39), 1386: ('not:products', 39, 30), 1667: ('products', 43, 27), 1781: ('products', 45, 44), 1822: ('product/id', 46, 30), 2084: ('pid', 50, 44), 2355: ('string:Upgrade ${pid}', 56, 44), 2451: ('product/title', 59, 33), 2648: ('product/description', 64, 39), 2682: ('product/description', 64, 73), 2809: ('pid', 65, 58), 2856: ('product/version', 65, 105), 3022: ('product/upgrade_info', 68, 43), 3237: ('not:upgrade_info/hasProfile', 72, 39), 3419: ('upgrade_info/installedVersion', 74, 77), 3533: ('upgrade_info/hasProfile', 76, 39), 3736: ('upgrade_info/installedVersion', 78, 87), 3993: ('upgrade_info/newVersion', 81, 86), 4133: ('not:upgrade_info/available', 85, 38), 4617: ('python:num_products > 1', 96, 29), 4787: ('products', 98, 51), 4953: ('product/id', 101, 44), 5522: ('view/get_available', 116, 36), 5578: (' python:len(products', 117, 36), 5829: ('products', 121, 34), 5909: ('product/id', 122, 35), 6129: ('pid', 126, 46), 6485: ('product/title', 137, 33), 6682: ('product/description', 142, 39), 6766: ('product/description', 144, 29), 6875: ('pid', 145, 58), 6922: ('product/version', 145, 105), 7091: ('not:product/uninstall_profile', 149, 31), 7389: ('view/get_installed', 158, 36), 7448: (' python:len(products', 159, 39), 7701: ('products', 163, 34), 7781: ('product/id', 164, 35), 7995: ('pid', 168, 42), 8213: ('product/uninstall_profile', 173, 37), 8405: ('product/title', 179, 35), 8612: ('product/description', 184, 41), 8700: ('product/description', 186, 31), 8811: ('pid', 187, 60), 8858: ('product/version', 187, 107), 9032: ('not:product/uninstall_profile', 191, 33), 9331: ('view/get_broken', 200, 36), 9388: (' python:len(products', 201, 40), 9443: ('num_products', 202, 31), 9685: ('products', 206, 34), 9780: ('product/product_id', 208, 33), 9976: ('product/type', 213, 33), 10087: ('product/value', 214, 61), 261: ('context/prefs_main_template/macros/master', 6, 23), 261: ('context/prefs_main_template/macros/master', 6, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from collections import deque as _deque
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140097251534752 = {'class': 'discreet', }
_static_140097338268192 = {'class': 'configletDescription discreet', }
_static_140097338272944 = {'class': 'list-group-item mt-2 pb-3', }
_static_140097338270400 = {'class': 'configlets list-group list-group-flush', }
_static_140097338269248 = {'class': 'card-header', }
_static_140097252541632 = {'id': 'broken-products', 'class': 'card mb-4', }
_static_140097338347616 = {'class': 'alert alert-info mt-2 mb-0', 'role': 'status', }
_static_140097338355440 = {'class': 'discreet', }
_static_140097338196464 = {'class': 'configletDescription discreet', }
_static_140097338202080 = {'class': 'btn btn-sm btn-danger', 'type': 'submit', 'value': 'Uninstall', 'name': 'form.submitted', }
_static_140097252540576 = {'type': 'hidden', 'name': 'uninstall_product', 'value': 'pid', }
_static_140097252554160 = {'action': 'uninstall_products', 'method': 'post', 'class': 'float-end', }
_static_140097252551184 = {'class': 'list-group-item mt-2 pb-3', }
_static_140097252540624 = {'class': 'configlets list-group list-group-flush', }
_static_140097252554592 = {'class': 'card-header', }
_static_140097251789216 = {'id': 'activated-products', 'class': 'card mb-4', }
_static_140097251789360 = {'class': 'alert alert-warning mt-2 mb-0', 'role': 'status', }
_static_140097251795888 = {'class': 'discreet', }
_static_140097251790320 = {'class': 'configletDescription discreet', }
_static_140097251800880 = {'class': 'btn btn-sm btn-primary', 'type': 'submit', 'value': 'Install', 'name': 'form.submitted', }
_static_140097251839904 = {'type': 'hidden', 'name': 'install_product', 'value': 'pid', }
_static_140097251836976 = {'action': 'install_products', 'method': 'post', 'class': 'float-end', }
_static_140097251847824 = {'class': 'list-group-item mt-2 pb-3', }
_static_140097251848256 = {'class': 'configlets list-group list-group-flush', }
_static_140097251836400 = {'class': 'card-header', }
_static_140097338280352 = {'id': 'install-products', 'class': 'card mb-4', }
_static_140097251847248 = {'class': 'btn btn-primary', 'type': 'submit', 'value': 'Upgrade them ALL!', 'name': 'form.submitted', }
_static_140097338286208 = {'type': 'hidden', 'value': 'product', 'name': 'prefs_reinstallProducts:list', }
_static_140097338291488 = {'action': 'upgrade_products', 'method': 'post', }
_static_140097251655792 = {'class': 'list-group-item mt-2 pb-3', }
_static_140097251666592 = {'class': 'list-group-item mt-2 pb-3', }
_static_140097251658576 = {'class': 'configletDetails list-group list-group-flush', }
_static_140097251656464 = {'class': 'discreet', }
_static_140097251662752 = {'class': 'configletDescription discreet', }
_static_140097251664912 = {'class': 'btn btn-secondary', 'type': 'submit', 'value': 'Upgrade ${pid}', 'name': 'form.submitted', }
_static_140097251571840 = {'type': 'hidden', 'name': 'prefs_reinstallProducts:list', 'value': 'pid', }
_static_140097251559360 = {'action': 'upgrade_products', 'method': 'post', 'class': 'float-end', }
_static_140097251568336 = {'class': 'list-group-item mt-2 pb-3', }
_static_140097251558688 = {'class': 'configlets list-group list-group-flush', }
_static_140097251567376 = {'id': 'up-to-date-message', 'class': 'alert alert-info m-3 mb-0', 'role': 'status', }
_static_140097251573184 = {'class': 'card-header', }
_static_140097413192176 = __C2ZContextWrapper
_static_140097413192464 = __compile_zt_expr
_static_140097251573328 = {'id': 'upgrade-products', 'class': 'card mb-4', }
_static_140097252807184 = {'id': 'content-core', }
_static_140097252806224 = {'href': 'http://docs.plone.org/manage/installing/installing_addons.html', }
_static_140097252812272 = {'class': 'discreet', }
_static_140097252809440 = {'class': 'lead', }
_static_140097252812944 = {'class': 'documentFirstHeading', }
_static_140097252387584 = 'master'
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

            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097252382736
            __attrs_140097252382736 = _static_140097412968080
            __backup_macroname_140097248643584 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f6aeef66b00> name=None at 7f6aeef65000> -> __value
            __value = _static_140097252387584
            econtext['macroname'] = __value

            def __fill_prefs_configlet_main(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097252809392
                __attrs_140097252809392 = _static_140097412968080
                __previous_i18n_domain_140097252803968 = __i18n_domain
                __i18n_domain = 'plone'
                __append('\n  ')

                # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097252813520
                __attrs_140097252813520 = _static_140097412968080

                # <header ... (0:0)
                # --------------------------------------------------------
                __append('<header>\n\n    ')

                # <Static value=<ast.Dict object at 0x7f6aeefce890> name=None at 7f6aeefce9e0> -> __attrs_140097252803296
                __attrs_140097252803296 = _static_140097252812944

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append('<h1 class="documentFirstHeading">')
                __stream_140097252808816 = []
                __append_140097252808816 = __stream_140097252808816.append
                __append_140097252808816('Add-ons')
                __msgid_140097252808816 = __re_whitespace(''.join(__stream_140097252808816)).strip()
                if __msgid_140097252808816:
                    __append(translate(__msgid_140097252808816, mapping=None, default=__msgid_140097252808816, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</h1>\n\n    ')

                # <Static value=<ast.Dict object at 0x7f6aeefcdae0> name=None at 7f6aeefcc640> -> __attrs_140097252803536
                __attrs_140097252803536 = _static_140097252809440

                # <p ... (0:0)
                # --------------------------------------------------------
                __append('<p class="lead">')
                __stream_140097252808336 = []
                __append_140097252808336 = __stream_140097252808336.append
                __append_140097252808336('\n      This is the Add-on configuration section, you can activate and deactivate\n      add-ons in the lists below.\n    ')
                __msgid_140097252808336 = __re_whitespace(''.join(__stream_140097252808336)).strip()
                if __msgid_140097252808336:
                    __append(translate(__msgid_140097252808336, mapping=None, default=__msgid_140097252808336, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</p>\n    ')

                # <Static value=<ast.Dict object at 0x7f6aeefce5f0> name=None at 7f6aeefcc520> -> __attrs_140097252816064
                __attrs_140097252816064 = _static_140097252812272

                # <p ... (0:0)
                # --------------------------------------------------------
                __append('<p class="discreet">')
                __stream_140097251289664_third_party_product = ''
                __stream_140097252812368 = []
                __append_140097252812368 = __stream_140097252812368.append
                __append_140097252812368('\n      To make new add-ons show up here, add them to your buildout\n      configuration, run buildout, and restart the server process.\n      For detailed instructions see\n      ')
                __stream_140097251289664_third_party_product = []
                __append_140097251289664_third_party_product = __stream_140097251289664_third_party_product.append

                # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097252807616
                __attrs_140097252807616 = _static_140097412968080

                # <span ... (0:0)
                # --------------------------------------------------------
                __append_140097251289664_third_party_product('<span>\n      ')

                # <Static value=<ast.Dict object at 0x7f6aeefcce50> name=None at 7f6aeefcd780> -> __attrs_140097252802672
                __attrs_140097252802672 = _static_140097252806224

                # <a ... (0:0)
                # --------------------------------------------------------
                __append_140097251289664_third_party_product('<a href="http://docs.plone.org/manage/installing/installing_addons.html">')
                __stream_140097252809584 = []
                __append_140097252809584 = __stream_140097252809584.append
                __append_140097252809584('\n        Installing a third party add-on\n      ')
                __msgid_140097252809584 = __re_whitespace(''.join(__stream_140097252809584)).strip()
                if __msgid_140097252809584:
                    __append_140097251289664_third_party_product(translate(__msgid_140097252809584, mapping=None, default=__msgid_140097252809584, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append_140097251289664_third_party_product('</a>\n      </span>')
                __append_140097252812368('${third_party_product}')
                __stream_140097251289664_third_party_product = ''.join(__stream_140097251289664_third_party_product)
                __append_140097252812368('.\n    ')
                __msgid_140097252812368 = __re_whitespace(''.join(__stream_140097252812368)).strip()
                if __msgid_140097252812368:
                    __append(translate(__msgid_140097252812368, mapping={'third_party_product': __stream_140097251289664_third_party_product, }, default=__msgid_140097252812368, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</p>\n  </header>\n  ')

                # <Static value=<ast.Dict object at 0x7f6aeefcd210> name=None at 7f6aeefcebf0> -> __attrs_140097252817600
                __attrs_140097252817600 = _static_140097252807184

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div id="content-core">\n\n\n      ')

                # <Static value=<ast.Dict object at 0x7f6aeee9fe50> name=None at 7f6aeee9ec20> -> __attrs_140097251570256
                __attrs_140097251570256 = _static_140097251573328
                __backup_products_140097252818656 = get('products', __marker)

                # <Value 'view/get_upgrades' (35:36)> -> __value
                __token = 1150
                try:
                    __zt_tmp = __attrs_140097251570256
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140097413192464('path', 'view/get_upgrades', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                econtext['products'] = __value
                __backup_num_products_140097252811408 = get('num_products', __marker)

                # <Value 'python:len(products)' (36:39)> -> __value
                __token = 1208
                try:
                    __zt_tmp = __attrs_140097251570256
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140097413192464('python', 'len(products)', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                econtext['num_products'] = __value

                # <section ... (0:0)
                # --------------------------------------------------------
                __append('<section id="upgrade-products" class="card mb-4">\n        ')

                # <Static value=<ast.Dict object at 0x7f6aeee9fdc0> name=None at 7f6aeee9e110> -> __attrs_140097251567568
                __attrs_140097251567568 = _static_140097251573184

                # <header ... (0:0)
                # --------------------------------------------------------
                __append('<header class="card-header">')
                __stream_140097251567616 = []
                __append_140097251567616 = __stream_140097251567616.append
                __append_140097251567616('Upgrades')
                __msgid_140097251567616 = __re_whitespace(''.join(__stream_140097251567616)).strip()
                if __msgid_140097251567616:
                    __append(translate(__msgid_140097251567616, mapping=None, default=__msgid_140097251567616, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</header>\n          ')

                # <Static value=<ast.Dict object at 0x7f6aeee9e710> name=None at 7f6aeee9ed10> -> __attrs_140097251567040
                __attrs_140097251567040 = _static_140097251567376

                # <Value 'not:products' (39:30)> -> __condition
                __token = 1386
                try:
                    __zt_tmp = __attrs_140097251567040
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140097413192464('not', 'products', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div id="up-to-date-message" class="alert alert-info m-3 mb-0" role="status">\n            ')

                    # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097251569440
                    __attrs_140097251569440 = _static_140097412968080

                    # <strong ... (0:0)
                    # --------------------------------------------------------
                    __append('<strong>')
                    __stream_140097251567904 = []
                    __append_140097251567904 = __stream_140097251567904.append
                    __append_140097251567904('No upgrades in this corner.')
                    __msgid_140097251567904 = __re_whitespace(''.join(__stream_140097251567904)).strip()
                    if __msgid_140097251567904:
                        __append(translate(__msgid_140097251567904, mapping=None, default=__msgid_140097251567904, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</strong>\n            ')

                    # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097251573232
                    __attrs_140097251573232 = _static_140097412968080

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>')
                    __stream_140097251560128 = []
                    __append_140097251560128 = __stream_140097251560128.append
                    __append_140097251560128('You are up to date. High fives.')
                    __msgid_140097251560128 = __re_whitespace(''.join(__stream_140097251560128)).strip()
                    if __msgid_140097251560128:
                        __append(translate(__msgid_140097251560128, mapping=None, default=__msgid_140097251560128, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</span>\n          </div>')
                __append('\n        ')

                # <Static value=<ast.Dict object at 0x7f6aeee9c520> name=None at 7f6aeee9d720> -> __attrs_140097251572032
                __attrs_140097251572032 = _static_140097251558688

                # <Value 'products' (43:27)> -> __condition
                __token = 1667
                try:
                    __zt_tmp = __attrs_140097251572032
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140097413192464('path', 'products', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                if __condition:

                    # <ul ... (0:0)
                    # --------------------------------------------------------
                    __append('<ul class="configlets list-group list-group-flush">\n          ')

                    # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097251558784
                    __attrs_140097251558784 = _static_140097412968080
                    __backup_product_140097252813184 = get('product', __marker)

                    # <Value 'products' (45:44)> -> __iterator
                    __token = 1781
                    try:
                        __zt_tmp = __attrs_140097251558784
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_140097413192464('path', 'products', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    (__iterator, ____index_140097251565072, ) = getname('repeat')('product', __iterator)
                    econtext['product'] = None
                    for __item in __iterator:
                        econtext['product'] = __item
                        __append('\n          ')

                        # <Static value=<ast.Dict object at 0x7f6aeee9ead0> name=None at 7f6aeee9d900> -> __attrs_140097251572944
                        __attrs_140097251572944 = _static_140097251568336
                        __backup_pid_140097251559792 = get('pid', __marker)

                        # <Value 'product/id' (46:30)> -> __value
                        __token = 1822
                        try:
                            __zt_tmp = __attrs_140097251572944
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140097413192464('path', 'product/id', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        econtext['pid'] = __value

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li class="list-group-item mt-2 pb-3">\n            ')

                        # <Static value=<ast.Dict object at 0x7f6aeee9c7c0> name=None at 7f6aeee9fb50> -> __attrs_140097251572800
                        __attrs_140097251572800 = _static_140097251559360

                        # <form ... (0:0)
                        # --------------------------------------------------------
                        __append('<form action="upgrade_products" method="post" class="float-end">\n              ')

                        # <Static value=<ast.Dict object at 0x7f6aeee9f880> name=None at 7f6aeee9c640> -> __attrs_140097251572656
                        __attrs_140097251572656 = _static_140097251571840

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input type="hidden" name="prefs_reinstallProducts:list"')

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097251561184
                        __default_140097251561184 = _DEFAULT_MARKER

                        # <Substitution 'pid' (50:44)> -> __attr_value
                        __token = 2084
                        try:
                            __zt_tmp = __attrs_140097251572656
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_value = _static_140097413192464('path', 'pid', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_value is not None):
                            __append((' value="%s"' % __attr_value))
                        __append(' />\n              ')

                        # <Static value=<ast.Dict object at 0x7f6aeeeb6410> name=None at 7f6aeeeb4130> -> __attrs_140097251660880
                        __attrs_140097251660880 = _static_140097251664912

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input class="btn btn-secondary" type="submit"')

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097251668320
                        __default_140097251668320 = _DEFAULT_MARKER

                        # <Translate msgid=None node=<Substitution 'string:Upgrade ${pid}' (56:44)> at 7f6aeeeb5510> -> __attr_value

                        # <Substitution 'string:Upgrade ${pid}' (56:44)> -> __attr_value
                        __token = 2355
                        try:
                            __zt_tmp = __attrs_140097251660880
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_value = _static_140097413192464('string', 'Upgrade ${pid}', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        __attr_value = __quote(__attr_value, '"', '&quot;', 'Upgrade ${pid}', _DEFAULT_MARKER)
                        __attr_value = translate(__attr_value, default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        if (__attr_value is not None):
                            __append((' value="%s"' % __attr_value))
                        __append(' name="form.submitted"/>\n            </form>\n            ')

                        # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097251662896
                        __attrs_140097251662896 = _static_140097412968080

                        # <h3 ... (0:0)
                        # --------------------------------------------------------
                        __append('<h3>\n              ')

                        # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097251661408
                        __attrs_140097251661408 = _static_140097412968080

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097251666448
                        __default_140097251666448 = _DEFAULT_MARKER

                        # <Value 'product/title' (59:33)> -> __cache_140097251672016
                        __token = 2451
                        try:
                            __zt_tmp = __attrs_140097251661408
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140097251672016 = _static_140097413192464('path', 'product/title', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                        # <BinOp left=<Value 'product/title' (59:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeeeb56c0> -> __condition
                        __expression = __cache_140097251672016

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span>\n                Add-on Name\n              </span>')
                        else:
                            __content = __cache_140097251672016
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('\n            </h3>\n            ')

                        # <Static value=<ast.Dict object at 0x7f6aeeeb5ba0> name=None at 7f6aeeeb7c10> -> __attrs_140097251656032
                        __attrs_140097251656032 = _static_140097251662752

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append('<div class="configletDescription discreet">\n              ')

                        # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097251658960
                        __attrs_140097251658960 = _static_140097412968080

                        # <Value 'product/description' (64:39)> -> __condition
                        __token = 2648
                        try:
                            __zt_tmp = __attrs_140097251658960
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140097413192464('path', 'product/description', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        if __condition:

                            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097251668176
                            __default_140097251668176 = _DEFAULT_MARKER

                            # <Value 'product/description' (64:73)> -> __cache_140097251665104
                            __token = 2682
                            try:
                                __zt_tmp = __attrs_140097251658960
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140097251665104 = _static_140097413192464('path', 'product/description', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                            # <BinOp left=<Value 'product/description' (64:73)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeeeb54e0> -> __condition
                            __expression = __cache_140097251665104

                            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                __append('add-on description')
                            else:
                                __content = __cache_140097251665104
                                __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append(__content)
                        __append('\n              ')

                        # <Static value=<ast.Dict object at 0x7f6aeeeb4310> name=None at 7f6aeeeb4910> -> __attrs_140097251668128
                        __attrs_140097251668128 = _static_140097251656464

                        # <em ... (0:0)
                        # --------------------------------------------------------
                        __append('<em class="discreet"> – (')

                        # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097251667408
                        __attrs_140097251667408 = _static_140097412968080

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097251667984
                        __default_140097251667984 = _DEFAULT_MARKER

                        # <Value 'pid' (65:58)> -> __cache_140097251667024
                        __token = 2809
                        try:
                            __zt_tmp = __attrs_140097251667408
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140097251667024 = _static_140097413192464('path', 'pid', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                        # <BinOp left=<Value 'pid' (65:58)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeeeb5570> -> __condition
                        __expression = __cache_140097251667024

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span>plugin.app.name</span>')
                        else:
                            __content = __cache_140097251667024
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(' ')

                        # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097251659632
                        __attrs_140097251659632 = _static_140097412968080

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097251666880
                        __default_140097251666880 = _DEFAULT_MARKER

                        # <Value 'product/version' (65:105)> -> __cache_140097251666688
                        __token = 2856
                        try:
                            __zt_tmp = __attrs_140097251659632
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140097251666688 = _static_140097413192464('path', 'product/version', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                        # <BinOp left=<Value 'product/version' (65:105)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeeeb5810> -> __condition
                        __expression = __cache_140097251666688

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span>1.0</span>')
                        else:
                            __content = __cache_140097251666688
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(')</em>\n            </div>\n            ')

                        # <Static value=<ast.Dict object at 0x7f6aeeeb4b50> name=None at 7f6aeeeb4040> -> __attrs_140097251659680
                        __attrs_140097251659680 = _static_140097251658576

                        # <ul ... (0:0)
                        # --------------------------------------------------------
                        __append('<ul class="configletDetails list-group list-group-flush">\n              ')

                        # <Static value=<ast.Dict object at 0x7f6aeeeb6aa0> name=None at 7f6aeeeb77c0> -> __attrs_140097251666016
                        __attrs_140097251666016 = _static_140097251666592
                        __backup_upgrade_info_140097251571984 = get('upgrade_info', __marker)

                        # <Value 'product/upgrade_info' (68:43)> -> __value
                        __token = 3022
                        try:
                            __zt_tmp = __attrs_140097251666016
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140097413192464('path', 'product/upgrade_info', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        econtext['upgrade_info'] = __value

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li class="list-group-item mt-2 pb-3">\n                  ')

                        # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097248159504
                        __attrs_140097248159504 = _static_140097412968080

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>')
                        __stream_140097248150096 = []
                        __append_140097248150096 = __stream_140097248150096.append
                        __append_140097248150096('\n                    This addon has been upgraded.\n                  ')
                        __msgid_140097248150096 = __re_whitespace(''.join(__stream_140097248150096)).strip()
                        if __msgid_140097248150096:
                            __append(translate(__msgid_140097248150096, mapping=None, default=__msgid_140097248150096, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</span>\n                  ')

                        # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097248156672
                        __attrs_140097248156672 = _static_140097412968080

                        # <Value 'not:upgrade_info/hasProfile' (72:39)> -> __condition
                        __token = 3237
                        try:
                            __zt_tmp = __attrs_140097248156672
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140097413192464('not', 'upgrade_info/hasProfile', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span>')
                            __stream_140097251290784_version = ''
                            __stream_140097248165600 = []
                            __append_140097248165600 = __stream_140097248165600.append
                            __append_140097248165600('\n                    Old version was ')
                            __stream_140097251290784_version = []
                            __append_140097251290784_version = __stream_140097251290784_version.append

                            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097248152928
                            __attrs_140097248152928 = _static_140097412968080

                            # <strong ... (0:0)
                            # --------------------------------------------------------
                            __append_140097251290784_version('<strong>')

                            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097248160176
                            __default_140097248160176 = _DEFAULT_MARKER

                            # <Value 'upgrade_info/installedVersion' (74:77)> -> __cache_140097248157200
                            __token = 3419
                            try:
                                __zt_tmp = __attrs_140097248152928
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140097248157200 = _static_140097413192464('path', 'upgrade_info/installedVersion', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                            # <BinOp left=<Value 'upgrade_info/installedVersion' (74:77)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeeb5d720> -> __condition
                            __expression = __cache_140097248157200

                            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                __append_140097251290784_version('version')
                            else:
                                __content = __cache_140097248157200
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append_140097251290784_version(__content)
                            __append_140097251290784_version('</strong>')
                            __append_140097248165600('${version}')
                            __stream_140097251290784_version = ''.join(__stream_140097251290784_version)
                            __append_140097248165600('.\n                  ')
                            __msgid_140097248165600 = __re_whitespace(''.join(__stream_140097248165600)).strip()
                            if 'label_product_upgrade_old_version':
                                __append(translate('label_product_upgrade_old_version', mapping={'version': __stream_140097251290784_version, }, default=__msgid_140097248165600, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                            __append('</span>')
                        __append('\n                  ')

                        # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097248161280
                        __attrs_140097248161280 = _static_140097412968080

                        # <Value 'upgrade_info/hasProfile' (76:39)> -> __condition
                        __token = 3533
                        try:
                            __zt_tmp = __attrs_140097248161280
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140097413192464('path', 'upgrade_info/hasProfile', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span>\n                    ')

                            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097248163488
                            __attrs_140097248163488 = _static_140097412968080
                            __stream_140097251291232_version = ''
                            __stream_140097248150384 = []
                            __append_140097248150384 = __stream_140097248150384.append
                            __append_140097248150384('\n                      Old profile version was ')
                            __stream_140097251291232_version = []
                            __append_140097251291232_version = __stream_140097251291232_version.append

                            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097248164400
                            __attrs_140097248164400 = _static_140097412968080

                            # <strong ... (0:0)
                            # --------------------------------------------------------
                            __append_140097251291232_version('<strong>')

                            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097248156624
                            __default_140097248156624 = _DEFAULT_MARKER

                            # <Value 'upgrade_info/installedVersion' (78:87)> -> __cache_140097248158400
                            __token = 3736
                            try:
                                __zt_tmp = __attrs_140097248164400
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140097248158400 = _static_140097413192464('path', 'upgrade_info/installedVersion', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                            # <BinOp left=<Value 'upgrade_info/installedVersion' (78:87)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeeb5d510> -> __condition
                            __expression = __cache_140097248158400

                            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                __append_140097251291232_version('version')
                            else:
                                __content = __cache_140097248158400
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append_140097251291232_version(__content)
                            __append_140097251291232_version('</strong>')
                            __append_140097248150384('${version}')
                            __stream_140097251291232_version = ''.join(__stream_140097251291232_version)
                            __append_140097248150384('.\n                    ')
                            __msgid_140097248150384 = __re_whitespace(''.join(__stream_140097248150384)).strip()
                            if 'label_product_upgrade_old_profile_version':
                                __append(translate('label_product_upgrade_old_profile_version', mapping={'version': __stream_140097251291232_version, }, default=__msgid_140097248150384, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                            __append('\n                    ')

                            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097248149568
                            __attrs_140097248149568 = _static_140097412968080
                            __stream_140097251291232_version = ''
                            __stream_140097248157824 = []
                            __append_140097248157824 = __stream_140097248157824.append
                            __append_140097248157824('\n                      New profile version is ')
                            __stream_140097251291232_version = []
                            __append_140097251291232_version = __stream_140097251291232_version.append

                            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097248151392
                            __attrs_140097248151392 = _static_140097412968080

                            # <strong ... (0:0)
                            # --------------------------------------------------------
                            __append_140097251291232_version('<strong>')

                            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097248157248
                            __default_140097248157248 = _DEFAULT_MARKER

                            # <Value 'upgrade_info/newVersion' (81:86)> -> __cache_140097248152688
                            __token = 3993
                            try:
                                __zt_tmp = __attrs_140097248151392
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140097248152688 = _static_140097413192464('path', 'upgrade_info/newVersion', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                            # <BinOp left=<Value 'upgrade_info/newVersion' (81:86)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeeb5d840> -> __condition
                            __expression = __cache_140097248152688

                            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                __append_140097251291232_version('version')
                            else:
                                __content = __cache_140097248152688
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append_140097251291232_version(__content)
                            __append_140097251291232_version('</strong>')
                            __append_140097248157824('${version}')
                            __stream_140097251291232_version = ''.join(__stream_140097251291232_version)
                            __append_140097248157824('.\n                    ')
                            __msgid_140097248157824 = __re_whitespace(''.join(__stream_140097248157824)).strip()
                            if 'label_product_upgrade_new_profile_version':
                                __append(translate('label_product_upgrade_new_profile_version', mapping={'version': __stream_140097251291232_version, }, default=__msgid_140097248157824, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                            __append('\n                  </span>')
                        __append('\n\n                  ')

                        # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097248162240
                        __attrs_140097248162240 = _static_140097412968080

                        # <Value 'not:upgrade_info/available' (85:38)> -> __condition
                        __token = 4133
                        try:
                            __zt_tmp = __attrs_140097248162240
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140097413192464('not', 'upgrade_info/available', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        if __condition:

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append('<div>\n                    ')

                            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097248155088
                            __attrs_140097248155088 = _static_140097412968080

                            # <strong ... (0:0)
                            # --------------------------------------------------------
                            __append('<strong>')
                            __stream_140097248159312 = []
                            __append_140097248159312 = __stream_140097248159312.append
                            __append_140097248159312('Warning')
                            __msgid_140097248159312 = __re_whitespace(''.join(__stream_140097248159312)).strip()
                            if __msgid_140097248159312:
                                __append(translate(__msgid_140097248159312, mapping=None, default=__msgid_140097248159312, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                            __append('</strong>\n                    ')

                            # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097248150528
                            __attrs_140097248150528 = _static_140097412968080

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span>')
                            __stream_140097248161904 = []
                            __append_140097248161904 = __stream_140097248161904.append
                            __append_140097248161904('There is no upgrade procedure defined for this\n                    addon. Please consult the addon documentation\n                    for upgrade information, or contact the addon\n                    author.')
                            __msgid_140097248161904 = __re_whitespace(''.join(__stream_140097248161904)).strip()
                            if __msgid_140097248161904:
                                __append(translate(__msgid_140097248161904, mapping=None, default=__msgid_140097248161904, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                            __append('</span>\n                  </div>')
                        __append('\n              </li>')
                        if (__backup_upgrade_info_140097251571984 is __marker):
                            del econtext['upgrade_info']
                        else:
                            econtext['upgrade_info'] = __backup_upgrade_info_140097251571984
                        __append('\n            </ul>\n          </li>')
                        if (__backup_pid_140097251559792 is __marker):
                            del econtext['pid']
                        else:
                            econtext['pid'] = __backup_pid_140097251559792
                        __append('\n          ')
                        ____index_140097251565072 -= 1
                        if (____index_140097251565072 > 0):
                            __append('')
                    if (__backup_product_140097252813184 is __marker):
                        del econtext['product']
                    else:
                        econtext['product'] = __backup_product_140097252813184
                    __append('\n          ')

                    # <Static value=<ast.Dict object at 0x7f6aeeeb4070> name=None at 7f6aeeeb4c10> -> __attrs_140097248153360
                    __attrs_140097248153360 = _static_140097251655792

                    # <Value 'python:num_products > 1' (96:29)> -> __condition
                    __token = 4617
                    try:
                        __zt_tmp = __attrs_140097248153360
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140097413192464('python', 'num_products > 1', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    if __condition:

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li class="list-group-item mt-2 pb-3">\n            ')

                        # <Static value=<ast.Dict object at 0x7f6af4153520> name=None at 7f6af4150700> -> __attrs_140097338282704
                        __attrs_140097338282704 = _static_140097338291488

                        # <form ... (0:0)
                        # --------------------------------------------------------
                        __append('<form action="upgrade_products" method="post">\n                ')

                        # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097338294128
                        __attrs_140097338294128 = _static_140097412968080
                        __backup_product_140097251658432 = get('product', __marker)

                        # <Value 'products' (98:51)> -> __iterator
                        __token = 4787
                        try:
                            __zt_tmp = __attrs_140097338294128
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __iterator = _static_140097413192464('path', 'products', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                        (__iterator, ____index_140097338289808, ) = getname('repeat')('product', __iterator)
                        econtext['product'] = None
                        for __item in __iterator:
                            econtext['product'] = __item
                            __append('\n                ')

                            # <Static value=<ast.Dict object at 0x7f6af4152080> name=None at 7f6af4153c70> -> __attrs_140097251841488
                            __attrs_140097251841488 = _static_140097338286208

                            # <input ... (0:0)
                            # --------------------------------------------------------
                            __append('<input type="hidden"')

                            # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097251843024
                            __default_140097251843024 = _DEFAULT_MARKER

                            # <Substitution 'product/id' (101:44)> -> __attr_value
                            __token = 4953
                            try:
                                __zt_tmp = __attrs_140097251841488
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_value = _static_140097413192464('path', 'product/id', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                            __attr_value = __quote(__attr_value, '"', '&quot;', 'product', _DEFAULT_MARKER)
                            if (__attr_value is not None):
                                __append((' value="%s"' % __attr_value))
                            __append(' name="prefs_reinstallProducts:list" />\n                ')
                            ____index_140097338289808 -= 1
                            if (____index_140097338289808 > 0):
                                __append('')
                        if (__backup_product_140097251658432 is __marker):
                            del econtext['product']
                        else:
                            econtext['product'] = __backup_product_140097251658432
                        __append('\n                ')

                        # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097251838944
                        __attrs_140097251838944 = _static_140097412968080

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>\n                  ')

                        # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097251843168
                        __attrs_140097251843168 = _static_140097412968080

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append('<div>')
                        __stream_140097251836448 = []
                        __append_140097251836448 = __stream_140097251836448.append
                        __append_140097251836448('This can be risky, are you sure you want to do this?')
                        __msgid_140097251836448 = __re_whitespace(''.join(__stream_140097251836448)).strip()
                        if 'label_product_upgrade_all_action':
                            __append(translate('label_product_upgrade_all_action', mapping=None, default=__msgid_140097251836448, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</div>\n                  ')

                        # <Static value=<ast.Dict object at 0x7f6aeeee2c50> name=None at 7f6aeeee2a70> -> __attrs_140097251842208
                        __attrs_140097251842208 = _static_140097251847248

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input class="btn btn-primary" type="submit"')

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097251846672
                        __default_140097251846672 = _DEFAULT_MARKER

                        # <Translate msgid=None node=<ast.Constant object at 0x7f6aeeee3e50> at 7f6aeeee1e40> -> __attr_value
                        __attr_value = 'Upgrade them ALL!'
                        __attr_value = translate(__attr_value, default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        if (__attr_value is not None):
                            __append((' value="%s"' % __attr_value))
                        __append(' name="form.submitted" />\n                </span>\n            </form>\n            </li>')
                    __append('\n          </ul>')
                __append('\n      </section>')
                if (__backup_num_products_140097252811408 is __marker):
                    del econtext['num_products']
                else:
                    econtext['num_products'] = __backup_num_products_140097252811408
                if (__backup_products_140097252818656 is __marker):
                    del econtext['products']
                else:
                    econtext['products'] = __backup_products_140097252818656
                __append('\n\n      ')

                # <Static value=<ast.Dict object at 0x7f6af41509a0> name=None at 7f6af4150940> -> __attrs_140097251851568
                __attrs_140097251851568 = _static_140097338280352
                __backup_products_140097252803440 = get('products', __marker)

                # <Value 'view/get_available' (116:36)> -> __value
                __token = 5522
                try:
                    __zt_tmp = __attrs_140097251851568
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140097413192464('path', 'view/get_available', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                econtext['products'] = __value
                __backup_num_products_140097252817456 = get('num_products', __marker)

                # <Value 'python:len(products)' (117:36)> -> __value
                __token = 5578
                try:
                    __zt_tmp = __attrs_140097251851568
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140097413192464('python', 'len(products)', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                econtext['num_products'] = __value

                # <section ... (0:0)
                # --------------------------------------------------------
                __append('<section id="install-products" class="card mb-4">\n        ')

                # <Static value=<ast.Dict object at 0x7f6aeeee01f0> name=None at 7f6aeeee2b30> -> __attrs_140097251841776
                __attrs_140097251841776 = _static_140097251836400

                # <header ... (0:0)
                # --------------------------------------------------------
                __append('<header class="card-header">')
                __stream_140097251838800 = []
                __append_140097251838800 = __stream_140097251838800.append
                __append_140097251838800('Available add-ons')
                __msgid_140097251838800 = __re_whitespace(''.join(__stream_140097251838800)).strip()
                if __msgid_140097251838800:
                    __append(translate(__msgid_140097251838800, mapping=None, default=__msgid_140097251838800, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</header>\n        ')

                # <Static value=<ast.Dict object at 0x7f6aeeee3040> name=None at 7f6aeeee0580> -> __attrs_140097251841824
                __attrs_140097251841824 = _static_140097251848256

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append('<ul class="configlets list-group list-group-flush">\n          ')

                # <Static value=<ast.Dict object at 0x7f6aeeee2e90> name=None at 7f6aeeee00d0> -> __attrs_140097251848832
                __attrs_140097251848832 = _static_140097251847824
                __backup_product_140097251572512 = get('product', __marker)

                # <Value 'products' (121:34)> -> __iterator
                __token = 5829
                try:
                    __zt_tmp = __attrs_140097251848832
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140097413192464('path', 'products', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                (__iterator, ____index_140097251842832, ) = getname('repeat')('product', __iterator)
                econtext['product'] = None
                for __item in __iterator:
                    econtext['product'] = __item

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append('<li class="list-group-item mt-2 pb-3">\n          ')

                    # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097251850704
                    __attrs_140097251850704 = _static_140097412968080
                    __backup_pid_140097251560896 = get('pid', __marker)

                    # <Value 'product/id' (122:35)> -> __value
                    __token = 5909
                    try:
                        __zt_tmp = __attrs_140097251850704
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140097413192464('path', 'product/id', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    econtext['pid'] = __value
                    __append('\n            ')

                    # <Static value=<ast.Dict object at 0x7f6aeeee0430> name=None at 7f6aeeee3790> -> __attrs_140097251836640
                    __attrs_140097251836640 = _static_140097251836976

                    # <form ... (0:0)
                    # --------------------------------------------------------
                    __append('<form action="install_products" method="post" class="float-end">\n                ')

                    # <Static value=<ast.Dict object at 0x7f6aeeee0fa0> name=None at 7f6aeeee0610> -> __attrs_140097251795024
                    __attrs_140097251795024 = _static_140097251839904

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input type="hidden" name="install_product"')

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097251836160
                    __default_140097251836160 = _DEFAULT_MARKER

                    # <Substitution 'pid' (126:46)> -> __attr_value
                    __token = 6129
                    try:
                        __zt_tmp = __attrs_140097251795024
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_140097413192464('path', 'pid', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append(' />\n                ')

                    # <Static value=<ast.Dict object at 0x7f6aeeed7730> name=None at 7f6aeeed5630> -> __attrs_140097251793536
                    __attrs_140097251793536 = _static_140097251800880

                    # <button ... (0:0)
                    # --------------------------------------------------------
                    __append('<button class="btn btn-sm btn-primary" type="submit" value="Install" name="form.submitted">')
                    __stream_140097251787728 = []
                    __append_140097251787728 = __stream_140097251787728.append
                    __append_140097251787728('\n                    Install\n                ')
                    __msgid_140097251787728 = __re_whitespace(''.join(__stream_140097251787728)).strip()
                    if __msgid_140097251787728:
                        __append(translate(__msgid_140097251787728, mapping=None, default=__msgid_140097251787728, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</button>\n            </form>\n\n            ')

                    # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097251800976
                    __attrs_140097251800976 = _static_140097412968080

                    # <h3 ... (0:0)
                    # --------------------------------------------------------
                    __append('<h3>\n              ')

                    # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097251793056
                    __attrs_140097251793056 = _static_140097412968080

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097251799296
                    __default_140097251799296 = _DEFAULT_MARKER

                    # <Value 'product/title' (137:33)> -> __cache_140097251797616
                    __token = 6485
                    try:
                        __zt_tmp = __attrs_140097251793056
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140097251797616 = _static_140097413192464('path', 'product/title', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                    # <BinOp left=<Value 'product/title' (137:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeeed75e0> -> __condition
                    __expression = __cache_140097251797616

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>\n                Add-on Name\n              </span>')
                    else:
                        __content = __cache_140097251797616
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('\n            </h3>\n            ')

                    # <Static value=<ast.Dict object at 0x7f6aeeed4df0> name=None at 7f6aeeed6e60> -> __attrs_140097251795696
                    __attrs_140097251795696 = _static_140097251790320

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="configletDescription discreet">\n              ')

                    # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097251790176
                    __attrs_140097251790176 = _static_140097412968080

                    # <Value 'product/description' (142:39)> -> __condition
                    __token = 6682
                    try:
                        __zt_tmp = __attrs_140097251790176
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140097413192464('path', 'product/description', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    if __condition:

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097251786864
                        __default_140097251786864 = _DEFAULT_MARKER

                        # <Value 'product/description' (144:29)> -> __cache_140097251794544
                        __token = 6766
                        try:
                            __zt_tmp = __attrs_140097251790176
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140097251794544 = _static_140097413192464('path', 'product/description', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                        # <BinOp left=<Value 'product/description' (144:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeeed41c0> -> __condition
                        __expression = __cache_140097251794544

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('add-on description')
                        else:
                            __content = __cache_140097251794544
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                    __append('\n              ')

                    # <Static value=<ast.Dict object at 0x7f6aeeed63b0> name=None at 7f6aeeed6410> -> __attrs_140097251800016
                    __attrs_140097251800016 = _static_140097251795888

                    # <em ... (0:0)
                    # --------------------------------------------------------
                    __append('<em class="discreet"> – (')

                    # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097251796128
                    __attrs_140097251796128 = _static_140097412968080

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097251791568
                    __default_140097251791568 = _DEFAULT_MARKER

                    # <Value 'pid' (145:58)> -> __cache_140097251792528
                    __token = 6875
                    try:
                        __zt_tmp = __attrs_140097251796128
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140097251792528 = _static_140097413192464('path', 'pid', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                    # <BinOp left=<Value 'pid' (145:58)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeeed7d00> -> __condition
                    __expression = __cache_140097251792528

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>plugin.app.name</span>')
                    else:
                        __content = __cache_140097251792528
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(' ')

                    # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097251787824
                    __attrs_140097251787824 = _static_140097412968080

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097251802800
                    __default_140097251802800 = _DEFAULT_MARKER

                    # <Value 'product/version' (145:105)> -> __cache_140097251793008
                    __token = 6922
                    try:
                        __zt_tmp = __attrs_140097251787824
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140097251793008 = _static_140097413192464('path', 'product/version', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                    # <BinOp left=<Value 'product/version' (145:105)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeeed57e0> -> __condition
                    __expression = __cache_140097251793008

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>1.0</span>')
                    else:
                        __content = __cache_140097251793008
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(')</em>\n            </div>\n            ')

                    # <Static value=<ast.Dict object at 0x7f6aeeed4a30> name=None at 7f6aeeed4250> -> __attrs_140097251793584
                    __attrs_140097251793584 = _static_140097251789360

                    # <Value 'not:product/uninstall_profile' (149:31)> -> __condition
                    __token = 7091
                    try:
                        __zt_tmp = __attrs_140097251793584
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140097413192464('not', 'product/uninstall_profile', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    if __condition:

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append('<div class="alert alert-warning mt-2 mb-0" role="status">\n              ')

                        # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097251799248
                        __attrs_140097251799248 = _static_140097412968080

                        # <strong ... (0:0)
                        # --------------------------------------------------------
                        __append('<strong>')
                        __stream_140097251791472 = []
                        __append_140097251791472 = __stream_140097251791472.append
                        __append_140097251791472('Warning')
                        __msgid_140097251791472 = __re_whitespace(''.join(__stream_140097251791472)).strip()
                        if __msgid_140097251791472:
                            __append(translate(__msgid_140097251791472, mapping=None, default=__msgid_140097251791472, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</strong>\n              ')

                        # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097251788832
                        __attrs_140097251788832 = _static_140097412968080

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>')
                        __stream_140097251788928 = []
                        __append_140097251788928 = __stream_140097251788928.append
                        __append_140097251788928('This product cannot be uninstalled!')
                        __msgid_140097251788928 = __re_whitespace(''.join(__stream_140097251788928)).strip()
                        if __msgid_140097251788928:
                            __append(translate(__msgid_140097251788928, mapping=None, default=__msgid_140097251788928, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</span>\n            </div>')
                    __append('\n          ')
                    if (__backup_pid_140097251560896 is __marker):
                        del econtext['pid']
                    else:
                        econtext['pid'] = __backup_pid_140097251560896
                    __append('\n          </li>')
                    ____index_140097251842832 -= 1
                    if (____index_140097251842832 > 0):
                        __append('\n          ')
                if (__backup_product_140097251572512 is __marker):
                    del econtext['product']
                else:
                    econtext['product'] = __backup_product_140097251572512
                __append('\n        </ul>\n      </section>')
                if (__backup_num_products_140097252817456 is __marker):
                    del econtext['num_products']
                else:
                    econtext['num_products'] = __backup_num_products_140097252817456
                if (__backup_products_140097252803440 is __marker):
                    del econtext['products']
                else:
                    econtext['products'] = __backup_products_140097252803440
                __append('\n\n      ')

                # <Static value=<ast.Dict object at 0x7f6aeeed49a0> name=None at 7f6aeeed7f70> -> __attrs_140097252556464
                __attrs_140097252556464 = _static_140097251789216
                __backup_products_140097252804784 = get('products', __marker)

                # <Value 'view/get_installed' (158:36)> -> __value
                __token = 7389
                try:
                    __zt_tmp = __attrs_140097252556464
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140097413192464('path', 'view/get_installed', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                econtext['products'] = __value
                __backup_num_products_140097251561664 = get('num_products', __marker)

                # <Value 'python:len(products)' (159:39)> -> __value
                __token = 7448
                try:
                    __zt_tmp = __attrs_140097252556464
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140097413192464('python', 'len(products)', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                econtext['num_products'] = __value

                # <section ... (0:0)
                # --------------------------------------------------------
                __append('<section id="activated-products" class="card mb-4">\n        ')

                # <Static value=<ast.Dict object at 0x7f6aeef8f760> name=None at 7f6aeef8d000> -> __attrs_140097252542976
                __attrs_140097252542976 = _static_140097252554592

                # <header ... (0:0)
                # --------------------------------------------------------
                __append('<header class="card-header">')
                __stream_140097252544560 = []
                __append_140097252544560 = __stream_140097252544560.append
                __append_140097252544560('Activated add-ons')
                __msgid_140097252544560 = __re_whitespace(''.join(__stream_140097252544560)).strip()
                if __msgid_140097252544560:
                    __append(translate(__msgid_140097252544560, mapping=None, default=__msgid_140097252544560, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</header>\n        ')

                # <Static value=<ast.Dict object at 0x7f6aeef8c0d0> name=None at 7f6aeef8ce50> -> __attrs_140097252551760
                __attrs_140097252551760 = _static_140097252540624

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append('<ul class="configlets list-group list-group-flush">\n          ')

                # <Static value=<ast.Dict object at 0x7f6aeef8ea10> name=None at 7f6aeef8fe20> -> __attrs_140097252542112
                __attrs_140097252542112 = _static_140097252551184
                __backup_product_140097248153696 = get('product', __marker)

                # <Value 'products' (163:34)> -> __iterator
                __token = 7701
                try:
                    __zt_tmp = __attrs_140097252542112
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140097413192464('path', 'products', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                (__iterator, ____index_140097252540528, ) = getname('repeat')('product', __iterator)
                econtext['product'] = None
                for __item in __iterator:
                    econtext['product'] = __item

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append('<li class="list-group-item mt-2 pb-3">\n          ')

                    # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097252544848
                    __attrs_140097252544848 = _static_140097412968080
                    __backup_pid_140097251660736 = get('pid', __marker)

                    # <Value 'product/id' (164:35)> -> __value
                    __token = 7781
                    try:
                        __zt_tmp = __attrs_140097252544848
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140097413192464('path', 'product/id', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    econtext['pid'] = __value
                    __append('\n            ')

                    # <Static value=<ast.Dict object at 0x7f6aeef8f5b0> name=None at 7f6aeef8e1a0> -> __attrs_140097252545520
                    __attrs_140097252545520 = _static_140097252554160

                    # <form ... (0:0)
                    # --------------------------------------------------------
                    __append('<form action="uninstall_products" method="post" class="float-end">\n              ')

                    # <Static value=<ast.Dict object at 0x7f6aeef8c0a0> name=None at 7f6aeef8ecb0> -> __attrs_140097252547056
                    __attrs_140097252547056 = _static_140097252540576

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input type="hidden" name="uninstall_product"')

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097252552240
                    __default_140097252552240 = _DEFAULT_MARKER

                    # <Substitution 'pid' (168:42)> -> __attr_value
                    __token = 7995
                    try:
                        __zt_tmp = __attrs_140097252547056
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_140097413192464('path', 'pid', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append(' />\n              ')

                    # <Static value=<ast.Dict object at 0x7f6af413d7e0> name=None at 7f6af413c4c0> -> __attrs_140097338204144
                    __attrs_140097338204144 = _static_140097338202080

                    # <Value 'product/uninstall_profile' (173:37)> -> __condition
                    __token = 8213
                    try:
                        __zt_tmp = __attrs_140097338204144
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140097413192464('path', 'product/uninstall_profile', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    if __condition:

                        # <button ... (0:0)
                        # --------------------------------------------------------
                        __append('<button class="btn btn-sm btn-danger" type="submit" value="Uninstall" name="form.submitted">')
                        __stream_140097338198480 = []
                        __append_140097338198480 = __stream_140097338198480.append
                        __append_140097338198480('\n                Uninstall\n              ')
                        __msgid_140097338198480 = __re_whitespace(''.join(__stream_140097338198480)).strip()
                        if __msgid_140097338198480:
                            __append(translate(__msgid_140097338198480, mapping=None, default=__msgid_140097338198480, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</button>')
                    __append('\n            </form>\n              ')

                    # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097338207168
                    __attrs_140097338207168 = _static_140097412968080

                    # <h3 ... (0:0)
                    # --------------------------------------------------------
                    __append('<h3>\n                ')

                    # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097338207312
                    __attrs_140097338207312 = _static_140097412968080

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338205440
                    __default_140097338205440 = _DEFAULT_MARKER

                    # <Value 'product/title' (179:35)> -> __cache_140097338201168
                    __token = 8405
                    try:
                        __zt_tmp = __attrs_140097338207312
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140097338201168 = _static_140097413192464('path', 'product/title', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                    # <BinOp left=<Value 'product/title' (179:35)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6af413e8f0> -> __condition
                    __expression = __cache_140097338201168

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>\n                  Add-on Name\n                </span>')
                    else:
                        __content = __cache_140097338201168
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('\n              </h3>\n              ')

                    # <Static value=<ast.Dict object at 0x7f6af413c1f0> name=None at 7f6af413ffa0> -> __attrs_140097338205056
                    __attrs_140097338205056 = _static_140097338196464

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="configletDescription discreet">\n                ')

                    # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097338346704
                    __attrs_140097338346704 = _static_140097412968080

                    # <Value 'product/description' (184:41)> -> __condition
                    __token = 8612
                    try:
                        __zt_tmp = __attrs_140097338346704
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140097413192464('path', 'product/description', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    if __condition:

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338353328
                        __default_140097338353328 = _DEFAULT_MARKER

                        # <Value 'product/description' (186:31)> -> __cache_140097338201936
                        __token = 8700
                        try:
                            __zt_tmp = __attrs_140097338346704
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140097338201936 = _static_140097413192464('path', 'product/description', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                        # <BinOp left=<Value 'product/description' (186:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6af4162650> -> __condition
                        __expression = __cache_140097338201936

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('add-on description')
                        else:
                            __content = __cache_140097338201936
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                    __append('\n                ')

                    # <Static value=<ast.Dict object at 0x7f6af4162ef0> name=None at 7f6af4160d90> -> __attrs_140097338348672
                    __attrs_140097338348672 = _static_140097338355440

                    # <em ... (0:0)
                    # --------------------------------------------------------
                    __append('<em class="discreet"> – (')

                    # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097338354768
                    __attrs_140097338354768 = _static_140097412968080

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338343968
                    __default_140097338343968 = _DEFAULT_MARKER

                    # <Value 'pid' (187:60)> -> __cache_140097338358272
                    __token = 8811
                    try:
                        __zt_tmp = __attrs_140097338354768
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140097338358272 = _static_140097413192464('path', 'pid', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                    # <BinOp left=<Value 'pid' (187:60)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6af4161090> -> __condition
                    __expression = __cache_140097338358272

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>plugin.app.name</span>')
                    else:
                        __content = __cache_140097338358272
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(' ')

                    # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097338350688
                    __attrs_140097338350688 = _static_140097412968080

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338350544
                    __default_140097338350544 = _DEFAULT_MARKER

                    # <Value 'product/version' (187:107)> -> __cache_140097338356304
                    __token = 8858
                    try:
                        __zt_tmp = __attrs_140097338350688
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140097338356304 = _static_140097413192464('path', 'product/version', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                    # <BinOp left=<Value 'product/version' (187:107)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6af41638b0> -> __condition
                    __expression = __cache_140097338356304

                    # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>1.0</span>')
                    else:
                        __content = __cache_140097338356304
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(')</em>\n              </div>\n              ')

                    # <Static value=<ast.Dict object at 0x7f6af4161060> name=None at 7f6af4160a00> -> __attrs_140097338357744
                    __attrs_140097338357744 = _static_140097338347616

                    # <Value 'not:product/uninstall_profile' (191:33)> -> __condition
                    __token = 9032
                    try:
                        __zt_tmp = __attrs_140097338357744
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140097413192464('not', 'product/uninstall_profile', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    if __condition:

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append('<div class="alert alert-info mt-2 mb-0" role="status">\n                ')

                        # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097338355680
                        __attrs_140097338355680 = _static_140097412968080

                        # <strong ... (0:0)
                        # --------------------------------------------------------
                        __append('<strong>')
                        __stream_140097338356592 = []
                        __append_140097338356592 = __stream_140097338356592.append
                        __append_140097338356592('Info')
                        __msgid_140097338356592 = __re_whitespace(''.join(__stream_140097338356592)).strip()
                        if __msgid_140097338356592:
                            __append(translate(__msgid_140097338356592, mapping=None, default=__msgid_140097338356592, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</strong>\n                ')

                        # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097338276784
                        __attrs_140097338276784 = _static_140097412968080

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>')
                        __stream_140097338354528 = []
                        __append_140097338354528 = __stream_140097338354528.append
                        __append_140097338354528('This product cannot be uninstalled!')
                        __msgid_140097338354528 = __re_whitespace(''.join(__stream_140097338354528)).strip()
                        if __msgid_140097338354528:
                            __append(translate(__msgid_140097338354528, mapping=None, default=__msgid_140097338354528, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</span>\n            </div>')
                    __append('\n          ')
                    if (__backup_pid_140097251660736 is __marker):
                        del econtext['pid']
                    else:
                        econtext['pid'] = __backup_pid_140097251660736
                    __append('\n          </li>')
                    ____index_140097252540528 -= 1
                    if (____index_140097252540528 > 0):
                        __append('\n          ')
                if (__backup_product_140097248153696 is __marker):
                    del econtext['product']
                else:
                    econtext['product'] = __backup_product_140097248153696
                __append('\n        </ul>\n      </section>')
                if (__backup_num_products_140097251561664 is __marker):
                    del econtext['num_products']
                else:
                    econtext['num_products'] = __backup_num_products_140097251561664
                if (__backup_products_140097252804784 is __marker):
                    del econtext['products']
                else:
                    econtext['products'] = __backup_products_140097252804784
                __append('\n\n      ')

                # <Static value=<ast.Dict object at 0x7f6aeef8c4c0> name=None at 7f6af4161db0> -> __attrs_140097338275056
                __attrs_140097338275056 = _static_140097252541632
                __backup_products_140097252809680 = get('products', __marker)

                # <Value 'view/get_broken' (200:36)> -> __value
                __token = 9331
                try:
                    __zt_tmp = __attrs_140097338275056
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140097413192464('path', 'view/get_broken', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                econtext['products'] = __value
                __backup_num_products_140097251563200 = get('num_products', __marker)

                # <Value 'python:len(products)' (201:40)> -> __value
                __token = 9388
                try:
                    __zt_tmp = __attrs_140097338275056
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140097413192464('python', 'len(products)', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                econtext['num_products'] = __value

                # <Value 'num_products' (202:31)> -> __condition
                __token = 9443
                try:
                    __zt_tmp = __attrs_140097338275056
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140097413192464('path', 'num_products', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                if __condition:

                    # <section ... (0:0)
                    # --------------------------------------------------------
                    __append('<section id="broken-products" class="card mb-4">\n        ')

                    # <Static value=<ast.Dict object at 0x7f6af414de40> name=None at 7f6af414c430> -> __attrs_140097338267616
                    __attrs_140097338267616 = _static_140097338269248

                    # <header ... (0:0)
                    # --------------------------------------------------------
                    __append('<header class="card-header">')
                    __stream_140097338267472 = []
                    __append_140097338267472 = __stream_140097338267472.append
                    __append_140097338267472('Broken add-ons')
                    __msgid_140097338267472 = __re_whitespace(''.join(__stream_140097338267472)).strip()
                    if __msgid_140097338267472:
                        __append(translate(__msgid_140097338267472, mapping=None, default=__msgid_140097338267472, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</header>\n        ')

                    # <Static value=<ast.Dict object at 0x7f6af414e2c0> name=None at 7f6af414cc10> -> __attrs_140097338269392
                    __attrs_140097338269392 = _static_140097338270400

                    # <ul ... (0:0)
                    # --------------------------------------------------------
                    __append('<ul class="configlets list-group list-group-flush">\n          ')

                    # <Static value=<ast.Dict object at 0x7f6af414ecb0> name=None at 7f6af414cb20> -> __attrs_140097338277024
                    __attrs_140097338277024 = _static_140097338272944
                    __backup_product_140097252556512 = get('product', __marker)

                    # <Value 'products' (206:34)> -> __iterator
                    __token = 9685
                    try:
                        __zt_tmp = __attrs_140097338277024
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_140097413192464('path', 'products', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
                    (__iterator, ____index_140097338266224, ) = getname('repeat')('product', __iterator)
                    econtext['product'] = None
                    for __item in __iterator:
                        econtext['product'] = __item

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li class="list-group-item mt-2 pb-3">\n            ')

                        # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097338277840
                        __attrs_140097338277840 = _static_140097412968080

                        # <h3 ... (0:0)
                        # --------------------------------------------------------
                        __append('<h3>\n              ')

                        # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097338267568
                        __attrs_140097338267568 = _static_140097412968080

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338277600
                        __default_140097338277600 = _DEFAULT_MARKER

                        # <Value 'product/product_id' (208:33)> -> __cache_140097338272272
                        __token = 9780
                        try:
                            __zt_tmp = __attrs_140097338267568
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140097338272272 = _static_140097413192464('path', 'product/product_id', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                        # <BinOp left=<Value 'product/product_id' (208:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6af414e830> -> __condition
                        __expression = __cache_140097338272272

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span>\n                Add-on Name\n              </span>')
                        else:
                            __content = __cache_140097338272272
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('\n            </h3>\n            ')

                        # <Static value=<ast.Dict object at 0x7f6af414da20> name=None at 7f6af414cfa0> -> __attrs_140097338266752
                        __attrs_140097338266752 = _static_140097338268192

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append('<div class="configletDescription discreet">\n              ')

                        # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097251531680
                        __attrs_140097251531680 = _static_140097412968080

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>')

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097338267184
                        __default_140097338267184 = _DEFAULT_MARKER

                        # <Value 'product/type' (213:33)> -> __cache_140097338276352
                        __token = 9976
                        try:
                            __zt_tmp = __attrs_140097251531680
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140097338276352 = _static_140097413192464('path', 'product/type', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                        # <BinOp left=<Value 'product/type' (213:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6af414ec80> -> __condition
                        __expression = __cache_140097338276352

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('Error Type')
                        else:
                            __content = __cache_140097338276352
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</span>\n              ')

                        # <Static value=<ast.Dict object at 0x7f6aeee967a0> name=None at 7f6aeee94910> -> __attrs_140097251524816
                        __attrs_140097251524816 = _static_140097251534752

                        # <em ... (0:0)
                        # --------------------------------------------------------
                        __append('<em class="discreet"> - ')

                        # <Static value=<ast.Dict object at 0x7f6af888ae90> name=None at 7f6af888b1c0> -> __attrs_140097251537824
                        __attrs_140097251537824 = _static_140097412968080

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __default_140097251539696
                        __default_140097251539696 = _DEFAULT_MARKER

                        # <Value 'product/value' (214:61)> -> __cache_140097251526784
                        __token = 10087
                        try:
                            __zt_tmp = __attrs_140097251537824
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140097251526784 = _static_140097413192464('path', 'product/value', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))

                        # <BinOp left=<Value 'product/value' (214:61)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f6af880bb50> at 7f6aeee94340> -> __condition
                        __expression = __cache_140097251526784

                        # <Symbol value=<DEFAULT> at 7f6af880bb50> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('Error Reason')
                        else:
                            __content = __cache_140097251526784
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</em>\n            </div>\n          </li>')
                        ____index_140097338266224 -= 1
                        if (____index_140097338266224 > 0):
                            __append('\n          ')
                    if (__backup_product_140097252556512 is __marker):
                        del econtext['product']
                    else:
                        econtext['product'] = __backup_product_140097252556512
                    __append('\n        </ul>\n      </section>')
                if (__backup_num_products_140097251563200 is __marker):
                    del econtext['num_products']
                else:
                    econtext['num_products'] = __backup_num_products_140097251563200
                if (__backup_products_140097252809680 is __marker):
                    del econtext['products']
                else:
                    econtext['products'] = __backup_products_140097252809680
                __append('\n\n  </div>\n')
                __i18n_domain = __previous_i18n_domain_140097252803968
            _slots = econtext['__slot_prefs_configlet_main'] = _deque((__fill_prefs_configlet_main, ))

            # <Value 'context/prefs_main_template/macros/master' (6:23)> -> __macro
            __token = 261
            try:
                __zt_tmp = __attrs_140097252382736
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140097413192464('path', 'context/prefs_main_template/macros/master', econtext=econtext)(_static_140097413192176(econtext, __zt_tmp))
            __token = 261
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140097248643584 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140097248643584
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }