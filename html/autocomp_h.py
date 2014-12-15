import sublime, sublime_plugin, re

from ..util import sublime_view_util

############################################################################
# h タグを取得します。
############################################################################
def get_h(level, h_default_class):
	h_default_class = " class=\"" + h_default_class + "\""

	save = "<h" + str(level) + h_default_class + \
		">$1</h" + str(level) + ">"

	return save


############################################################################
# h タグに対するオートコンプリートメソッドです。
############################################################################
def autocomp_get_h(view, h_level):
	# 設定を取得します。
	h_default_class_list = sublime_view_util.get_h_default_class(h_level)

	completions = []
	for h_default_class in h_default_class_list:
		completions.append(("h" + str(h_level) + "_class=" + \
			h_default_class + "\tHapoItak", \
			get_h(h_level, h_default_class)))

	return completions

############################################################################
# h タグに対するオートコンプリートメソッドです。
############################################################################
def autocomp_get_h_all(view):
	completions = []

	i = 1
	while i <= 6:
		comp_list = autocomp_get_h(view, i)
		completions.extend(comp_list)
		i = i + 1

	return completions


























