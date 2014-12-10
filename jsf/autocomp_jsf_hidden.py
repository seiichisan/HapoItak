import sublime, sublime_plugin, re

from ..util import sublime_view_util

############################################################################
# jsf hidden に対するオートコンプリートメソッドです。
############################################################################
def autocomp_get_jsf_hidden(view):
	temp_str2 = "<h:inputHidden id=\"$1\" value=\"#{$2}\" />"

	return ("jsf_hidden\tHapoItak", temp_str2)
