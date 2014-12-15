import sublime, sublime_plugin, re

from ..util import sublime_view_util

############################################################################
# div タグを取得します。
############################################################################
def get_div(div_default_class):
	div_default_class = " class=\"" + div_default_class + "\""
	save = "<div" + div_default_class + ">$1</div>"

	return save


############################################################################
# div に対するオートコンプリートメソッドです。
############################################################################
def autocomp_get_div(view):
	# 設定を取得します。
	div_default_class_list = sublime_view_util.get_div_default_class()

	completions = []
	for div_default_class in div_default_class_list:
		completions.append(("div_class=" + div_default_class + \
			"\tHapoItak", get_div(div_default_class)))

	return completions
