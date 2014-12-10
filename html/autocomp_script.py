import sublime, sublime_plugin, re

from ..util import sublime_view_util

############################################################################
# script に対するオートコンプリートメソッドです。
############################################################################
def autocomp_get_script(view):
	ans = "<script>\n" +\
		"$1\n" +\
		"</script>\n"

	return ("script\tHapoItak", ans)
