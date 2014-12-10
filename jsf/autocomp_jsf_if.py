import sublime, sublime_plugin, re

from ..util import sublime_view_util

############################################################################
# jsf if タグを取得します。
# if_flag が true  の場合、if   の働きをするタグを取得します。
# if_flag が false の場合、else の働きをするタグを取得します。
############################################################################
def get_jsf_if_tag(if_flag):
	if if_flag:
		save = "<c:if test='\${$1 == \"$2\"}'>\n" +\
			"$3\n" +\
			"</c:if>\n"
	else:
		save = "<c:if test='\${$4 != \"$5\"}'>\n" +\
			"$6\n" +\
			"</c:if>\n"
	return save

############################################################################
# jsf if に対するオートコンプリートメソッドです。
############################################################################
def autocomp_get_jsf_if(view):
	completions = []

	completions.append(("jsf_if_a=b\tHapoItak", get_jsf_if_tag(True)))
	completions.append(("jsf_if_a=b_else\tHapoItak", get_jsf_if_tag(True) + get_jsf_if_tag(False)))

	return completions
