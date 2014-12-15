import sublime, sublime_plugin, re

from ..util import sublime_view_util

############################################################################
# p タグを取得します。
############################################################################
def get_p(p_default_class):
	p_default_class = " class=\"" + p_default_class + "\""
	save = "<p" + p_default_class + ">$1</p>"

	return save


############################################################################
# p に対するオートコンプリートメソッドです。
############################################################################
def autocomp_get_p(view):
	# 設定を取得します。
	p_default_class_list = sublime_view_util.get_p_default_class()

	completions = []
	for p_default_class in p_default_class_list:
		completions.append(("p_class=" + p_default_class + \
			"\tHapoItak", get_p(p_default_class)))

	return completions
