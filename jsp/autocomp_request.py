import sublime, sublime_plugin, re

from ..util import sublime_view_util

############################################################################
# request に対するオートコンプリートメソッドです。
############################################################################
def autocomp_get_request(view):
	completions = []

	tmp = "<%= request.getContextPath() %>"
	completions.append((tmp, tmp))

	tmp = "request.getContextPath()"
	completions.append((tmp, tmp))

	tmp = "request.getServletPath()"
	completions.append((tmp, tmp))

	tmp = "request.getPathInfo()"
	completions.append((tmp, tmp))

	tmp = "request.getPathTranslated()"
	completions.append((tmp, tmp))

	tmp = "request.getRequestURL()"
	completions.append((tmp, tmp))

	tmp = "request.getRequestURI()"
	completions.append((tmp, tmp))

	return completions


