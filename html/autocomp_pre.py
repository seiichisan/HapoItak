import sublime, sublime_plugin, re

from ..util import sublime_view_util

############################################################################
# pre タグを取得します。
############################################################################
def get_pre(pre_default_class):
	if pre_default_class is None or pre_default_class == "":
		pre_default_class = ""
	else:
		pre_default_class = " class=\"" + pre_default_class + "\""

	save = "<pre" + pre_default_class + ">$1</pre>"

	return save


############################################################################
# pre に対するオートコンプリートメソッドです。
############################################################################
def autocomp_get_pre(view):
	# 設定を取得します。
	pre_default_class_list = sublime_view_util.get_pre_default_class()

	completions = []
	for pre_default_class in pre_default_class_list:
		completions.append(("pre_class=" + pre_default_class + \
			"\tHapoItak", get_pre(pre_default_class)))

	return completions
