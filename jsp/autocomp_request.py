import sublime, sublime_plugin, re

from ..util import sublime_view_util

############################################################################
# request に対するオートコンプリートメソッドです。
############################################################################
def autocomp_get_request(view):
	completions = []

	HAPO_ITAK_STR = "\tHapoItak"

	auto_keyword = "<%=request_getContextPath%>" + HAPO_ITAK_STR
	auto_value   = "<%= request.getContextPath() %>"
	completions.append((auto_keyword, auto_value))

	auto_keyword = "request_getContextPath" + HAPO_ITAK_STR
	auto_value   = "request.getContextPath()"
	completions.append((auto_keyword, auto_value))

	auto_keyword = "request_getServletPath" + HAPO_ITAK_STR
	auto_value   = "request.getServletPath()"
	completions.append((auto_keyword, auto_value))

	auto_keyword = "request_getPathInfo" + HAPO_ITAK_STR
	auto_value   = "request.getPathInfo()"
	completions.append((auto_keyword, auto_value))

	auto_keyword = "request_getPathTranslated" + HAPO_ITAK_STR
	auto_value   = "request.getPathTranslated()"
	completions.append((auto_keyword, auto_value))

	auto_keyword = "request_getRequestURL" + HAPO_ITAK_STR
	auto_value   = "request.getRequestURL()"
	completions.append((auto_keyword, auto_value))

	auto_keyword = "request_getRequestURI" + HAPO_ITAK_STR
	auto_value   = "request.getRequestURI()"
	completions.append((auto_keyword, auto_value))

	return completions


