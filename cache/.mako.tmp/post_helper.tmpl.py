# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1499659212.9930267
_enable_loop = True
_template_filename = '/home/hades/.virtualenvs/data_science_with_python/lib/python3.5/site-packages/nikola/data/themes/base/templates/post_helper.tmpl'
_template_uri = 'post_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_pager', 'html_tags', 'open_graph_metadata', 'mathjax_script', 'twitter_card_information', 'meta_translations']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('math', context._clean_inheritance_tokens(), templateuri='math_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'math')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_pager(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        messages = context.get('messages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if post.prev_post or post.next_post:
            __M_writer('        <ul class="pager hidden-print">\n')
            if post.prev_post:
                __M_writer('            <li class="previous">\n                <a href="')
                __M_writer(str(post.prev_post.permalink()))
                __M_writer('" rel="prev" title="')
                __M_writer(filters.html_escape(str(post.prev_post.title())))
                __M_writer('">')
                __M_writer(str(messages("Previous post")))
                __M_writer('</a>\n            </li>\n')
            if post.next_post:
                __M_writer('            <li class="next">\n                <a href="')
                __M_writer(str(post.next_post.permalink()))
                __M_writer('" rel="next" title="')
                __M_writer(filters.html_escape(str(post.next_post.title())))
                __M_writer('">')
                __M_writer(str(messages("Next post")))
                __M_writer('</a>\n            </li>\n')
            __M_writer('        </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_tags(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        hidden_tags = context.get('hidden_tags', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if post.tags:
            __M_writer('        <ul itemprop="keywords" class="tags">\n')
            for tag in post.tags:
                if tag not in hidden_tags:
                    __M_writer('            <li><a class="tag p-category" href="')
                    __M_writer(str(_link('tag', tag)))
                    __M_writer('" rel="tag">')
                    __M_writer(filters.html_escape(str(tag)))
                    __M_writer('</a></li>\n')
            __M_writer('        </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_open_graph_metadata(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        blog_title = context.get('blog_title', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        url_replacer = context.get('url_replacer', UNDEFINED)
        use_open_graph = context.get('use_open_graph', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if use_open_graph:
            __M_writer('    <meta property="og:site_name" content="')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('">\n    <meta property="og:title" content="')
            __M_writer(filters.html_escape(str(post.title()[:70])))
            __M_writer('">\n    <meta property="og:url" content="')
            __M_writer(str(abs_link(permalink)))
            __M_writer('">\n')
            if post.description():
                __M_writer('    <meta property="og:description" content="')
                __M_writer(filters.html_escape(str(post.description()[:200])))
                __M_writer('">\n')
            else:
                __M_writer('    <meta property="og:description" content="')
                __M_writer(filters.html_escape(str(post.text(strip_html=True)[:200])))
                __M_writer('">\n')
            if post.previewimage:
                __M_writer('    <meta property="og:image" content="')
                __M_writer(str(url_replacer(permalink, post.previewimage, lang, 'absolute')))
                __M_writer('">\n')
            __M_writer('    <meta property="og:type" content="article">\n')
            if post.date.isoformat():
                __M_writer('    <meta property="article:published_time" content="')
                __M_writer(str(post.formatted_date('webiso')))
                __M_writer('">\n')
            if post.tags:
                for tag in post.tags:
                    __M_writer('           <meta property="article:tag" content="')
                    __M_writer(filters.html_escape(str(tag)))
                    __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_mathjax_script(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        math = _mako_get_namespace(context, 'math')
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(math.math_scripts_ifpost(post)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_twitter_card_information(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        twitter_card = context.get('twitter_card', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if twitter_card and twitter_card['use_twitter_cards']:
            __M_writer('    <meta name="twitter:card" content="')
            __M_writer(filters.html_escape(str(twitter_card.get('card', 'summary'))))
            __M_writer('">\n')
            if 'site:id' in twitter_card:
                __M_writer('    <meta name="twitter:site:id" content="')
                __M_writer(str(twitter_card['site:id']))
                __M_writer('">\n')
            elif 'site' in twitter_card:
                __M_writer('    <meta name="twitter:site" content="')
                __M_writer(str(twitter_card['site']))
                __M_writer('">\n')
            if 'creator:id' in twitter_card:
                __M_writer('    <meta name="twitter:creator:id" content="')
                __M_writer(str(twitter_card['creator:id']))
                __M_writer('">\n')
            elif 'creator' in twitter_card:
                __M_writer('    <meta name="twitter:creator" content="')
                __M_writer(str(twitter_card['creator']))
                __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_meta_translations(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        len = context.get('len', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if len(translations) > 1:
            for langname in sorted(translations):
                if langname != lang and ((not post.skip_untranslated) or post.is_translation_available(langname)):
                    __M_writer('                <link rel="alternate" hreflang="')
                    __M_writer(str(langname))
                    __M_writer('" href="')
                    __M_writer(str(post.permalink(langname)))
                    __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/home/hades/.virtualenvs/data_science_with_python/lib/python3.5/site-packages/nikola/data/themes/base/templates/post_helper.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 0, "31": 2, "32": 12, "33": 24, "34": 41, "35": 70, "36": 86, "37": 91, "43": 26, "48": 26, "49": 27, "50": 28, "51": 29, "52": 30, "53": 31, "54": 31, "55": 31, "56": 31, "57": 31, "58": 31, "59": 34, "60": 35, "61": 36, "62": 36, "63": 36, "64": 36, "65": 36, "66": 36, "67": 39, "73": 14, "79": 14, "80": 15, "81": 16, "82": 17, "83": 18, "84": 19, "85": 19, "86": 19, "87": 19, "88": 19, "89": 22, "95": 43, "105": 43, "106": 44, "107": 45, "108": 45, "109": 45, "110": 46, "111": 46, "112": 47, "113": 47, "114": 48, "115": 49, "116": 49, "117": 49, "118": 50, "119": 51, "120": 51, "121": 51, "122": 53, "123": 54, "124": 54, "125": 54, "126": 56, "127": 61, "128": 62, "129": 62, "130": 62, "131": 64, "132": 65, "133": 66, "134": 66, "135": 66, "141": 89, "146": 89, "147": 90, "148": 90, "154": 72, "159": 72, "160": 73, "161": 74, "162": 74, "163": 74, "164": 75, "165": 76, "166": 76, "167": 76, "168": 77, "169": 78, "170": 78, "171": 78, "172": 80, "173": 81, "174": 81, "175": 81, "176": 82, "177": 83, "178": 83, "179": 83, "185": 4, "193": 4, "194": 5, "195": 6, "196": 7, "197": 8, "198": 8, "199": 8, "200": 8, "201": 8, "207": 201}, "uri": "post_helper.tmpl"}
__M_END_METADATA
"""