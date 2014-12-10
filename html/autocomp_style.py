import sublime, sublime_plugin, re

from ..util import sublime_view_util

############################################################################
# style に対するオートコンプリートメソッドです。
############################################################################
def autocomp_get_style(view):
	completions = []

	ans = "<style type=\"text/javascript\">\n" +\
		"<!--\n" +\
		"$1\n" +\
		"// -->\n" +\
		"</style>\n"
	completions.append(("style_type=text/javascript\tHapoItak", ans))

	ans = "<style type=\"text/css\">\n" +\
		"$1\n" +\
		"</style>\n"
	completions.append(("style_type=text/css\tHapoItak", ans))
	return completions
