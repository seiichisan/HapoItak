import sublime, sublime_plugin, re

from ..util import sublime_view_util

############################################################################
# href タグを取得します。
############################################################################
def get_href():
	save = "<a href=\"$1\">$2</a>"

	return save

############################################################################
# href に対するオートコンプリートメソッドです。
############################################################################
def autocomp_get_href(view):
	completions = []

	completions.append(("href\tHapoItak", get_href()))

	return completions
