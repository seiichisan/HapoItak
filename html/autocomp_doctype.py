import sublime, sublime_plugin, re

from ..util import sublime_view_util

############################################################################
# doctype に対するオートコンプリートメソッドです。
############################################################################
def autocomp_get_doctype(view):
	completions = []

	ans = "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01 Transitional//EN\" \"http://www.w3.org/TR/html4/loose.dtd\">"
	completions.append(("doctype_html4\tHapoItak", ans))

	ans = "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01 Frameset//EN\" \"http://www.w3.org/TR/html4/frameset.dtd\">"
	completions.append(("doctype_html4_frame\tHapoItak", ans))

	ans = "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01//EN\" \"http://www.w3.org/TR/html4/strict.dtd\">"
	completions.append(("doctype_html4_strict\tHapoItak", ans))

	

	return completions
