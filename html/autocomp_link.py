import sublime, sublime_plugin, re

from ..util import sublime_view_util

############################################################################
# link style タグを取得します。
# css_base_path   CSS のベースパス
# stylesheet_name スタイルシート名
############################################################################
def get_link_style(css_base_path, stylesheet_name, is_indent):
	if css_base_path is None:
		tmp = stylesheet_name
	else:
		tmp = css_base_path + "/" + stylesheet_name

	indent = ""
	if is_indent:
		indent = sublime_view_util.get_indent()

	save = indent + "<link rel=\"stylesheet\" type=\"text/css\" href=\"" + \
		tmp + ".css?v=0.1\" />"
	return save

############################################################################
# no cache に対するオートコンプリートメソッドです。
############################################################################
def autocomp_get_link_style(view):
	# 設定を取得します。
	css_base_path = sublime_view_util.get_css_base_path()

	return ("link_style_href=" + css_base_path + "/...\tHapoItak", \
		get_link_style(css_base_path, "$1", False))



############################################################################
# link javascript タグを取得します。
# javascript_base_path   JavaScript のベースパス
# javascript_name        JavaScript 名
############################################################################
def get_link_javascript(javascript_base_path, javascript_name):
	if javascript_base_path is None:
		tmp = javascript_name
	else:
		tmp = javascript_base_path + "/" + javascript_name

	save = "<script type=\"text/javascript\" src=\"" + \
		tmp + ".js?v=0.1\"></script>"
	return save

############################################################################
# link javascript に対するオートコンプリートメソッドです。
############################################################################
def autocomp_get_link_javascript(view):
	# 設定を取得します。
	javascript_base_path = sublime_view_util.get_javascript_base_path()

	return ("link_js_src=" + javascript_base_path + "/...\tHapoItak", \
		get_link_javascript(javascript_base_path, "$1"))






