import sublime, sublime_plugin, re

from ..util import sublime_view_util

############################################################################
# jsf output text に対するオートコンプリートメソッドです。
############################################################################
def autocomp_get_jsf_output_text(view):
	temp_str2 = "<h:outputText value=\"#{$1}\" />"

	return ("jsf_outputText\tHapoItak", temp_str2)
