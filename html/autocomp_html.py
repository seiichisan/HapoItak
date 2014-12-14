import sublime, sublime_plugin, re

from ..util import sublime_view_util
from .      import autocomp_meta
from .      import autocomp_link

############################################################################
# html4 に対するオートコンプリートメソッドです。
############################################################################
def autocomp_get_html4(view):
	completions = []
	completions.append(autocomp_get_html4_main(view, True, True))
	completions.append(autocomp_get_html4_main(view, True, False))
	completions.append(autocomp_get_html4_main(view, False, True))
	completions.append(autocomp_get_html4_main(view, False, False))
	return completions

############################################################################
# html4 に対するオートコンプリートメソッドです。
############################################################################
def autocomp_get_html4_main(view, is_no_cache, is_style):
	# 設定を取得します。
	css_base_path = sublime_view_util.get_css_base_path()

	ans = "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01 Transitional//EN\" \"http://www.w3.org/TR/html4/loose.dtd\">\n" +\
		"<html lang=\"" + sublime_view_util.get_lang() + "\">\n" +\
		"<head>\n" +\
		autocomp_meta.get_meta_charset(True) + "\n"
	if is_no_cache:
		ans += autocomp_meta.get_no_cache(True)
	if is_style:
		ans += autocomp_link.get_link_style(css_base_path, "${1:xxx}", True) + "\n"
	ans += sublime_view_util.get_indent() + "<title>${2:yyy}</title>\n" +\
		"</head>\n" +\
		"<body>\n" +\
		"$3\n" +\
		"</body>\n" +\
		"</html>\n"

	if is_no_cache and is_style:
		return ("html4_no_cache_and_link_style\tHapoItak", ans)
	if is_no_cache:
		return ("html4_no_cache\tHapoItak", ans)
	if is_style:
		return ("html4_link_style\tHapoItak", ans)
	return ("html4\tHapoItak", ans)



############################################################################
# html5 に対するオートコンプリートメソッドです。
############################################################################
def autocomp_get_html5(view):
	ans = "<!doctype html>\n" +\
		"<html lang=\"" + sublime_view_util.get_lang() + "\">\n" +\
		"<head>\n" +\
		sublime_view_util.get_indent() + "<meta charset=\"" + sublime_view_util.get_charset() + "\">\n" +\
		sublime_view_util.get_indent() + "<title>${1:xxx}</title>\n" +\
		"</head>\n" +\
		"<body>\n" +\
		"$2\n" +\
		"</body>\n" +\
		"</html>\n"

	return ("html5\tHapoItak", ans)












