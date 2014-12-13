import sublime, sublime_plugin, re

from ..util import sublime_view_util

############################################################################
# h タグを取得します。
############################################################################
def get_h(level, h_default_class):
	if h_default_class is None or h_default_class == "":
		h_default_class = ""
	else:
		h_default_class = " class=\"" + h_default_class + "\""

	save = "<h" + str(level) + h_default_class + \
		">$1</h" + str(level) + ">"

	return save


############################################################################
# h タグに対するオートコンプリートメソッドです。
############################################################################
def autocomp_get_h(view, h_level):
	# 設定を取得します。
	h_default_class = sublime_view_util.get_h_default_class(h_level)

	if h_default_class == "":
		return ("h" + str(h_level) + "\tHapoItak", get_h(h_level, h_default_class))
	else:
		return ("h" + str(h_level) + "_class=" + h_default_class + "\tHapoItak", \
			get_h(h_level, h_default_class))

############################################################################
# h タグに対するオートコンプリートメソッドです。
############################################################################
def autocomp_get_h_all(view):
	completions = []

	i = 1
	while i <= 6:
		completions.append(autocomp_get_h(view, i))
		i = i + 1

	return completions


























