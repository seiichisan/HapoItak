import sublime, sublime_plugin, re

from ..util import sublime_view_util

############################################################################
# jsf command button に対するオートコンプリートメソッドです。
############################################################################
def autocomp_get_jsf_command_button(view):
	temp_str2 = "<h:commandButton styleClass=\"$1\" id=\"$2\"\n" +\
		"\tvalue=\"$3\" action=\"#{${4:className}.${5:methodName}}\">\n" +\
		"</h:commandButton>\n"

	return ("jsf_commandButton\tHapoItak", temp_str2)
