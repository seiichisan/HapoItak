import sublime, sublime_plugin, re

from ..util import sublime_view_util

############################################################################
# jsp コードブロックに対するオートコンプリートメソッドです。
############################################################################
def autocomp_get_jsp_code(view):
	completions = []

	HAPO_ITAK_STR = "\tHapoItak"

	tmp = "<%= $1 %>"
	completions.append(("jsp_code<%=...%>" + HAPO_ITAK_STR, tmp))

	tmp = "<%\n" + "$1\n" + "%>\n"
	completions.append(("jsp_code<%...%>" + HAPO_ITAK_STR, tmp))

	tmp = "<%-- $1 --%>"
	completions.append(("jsp_comment<%--_--%>" + HAPO_ITAK_STR, tmp))

	return completions



