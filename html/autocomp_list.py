import sublime, sublime_plugin, re

from ..util import sublime_view_util

############################################################################
# list に対するオートコンプリートメソッドです。
############################################################################
def autocomp_get_list(view):
	completions = []
	completions.append(autocomp_get_list_main(view, 3))
	completions.append(autocomp_get_list_main(view, 5))
	completions.append(autocomp_get_list_main(view, 7))
	return completions

############################################################################
# list に対するオートコンプリートメソッドです。
# view      sublime view
# max_count リストの数
############################################################################
def autocomp_get_list_main(view, max_count):
	temp_str3 = ""
	ul_default_class = sublime_view_util.get_ul_default_class()
	if ul_default_class != "":
		temp_str3 = " class=\"" + ul_default_class + "\""

	temp_str2 = "<ul" + temp_str3 + ">\n"

	i = 0
	while i < max_count:
		temp_str2 = temp_str2 + \
			sublime_view_util.get_indent() + "<li>$" + str(i+1) + "</li>\n"
		i = i + 1

	temp_str2 = temp_str2 + "</ul>\n"

	if ul_default_class == "":
		return ("list_" + str(max_count) + "\tHapoItak", temp_str2)
	else:
		return ("list_class=" + ul_default_class + "_" + str(max_count) + "\tHapoItak", temp_str2)





############################################################################
# number list に対するオートコンプリートメソッドです。
############################################################################
def autocomp_get_number_list(view):
	completions = []
	completions.append(autocomp_get_number_list_main(view, 3))
	completions.append(autocomp_get_number_list_main(view, 5))
	completions.append(autocomp_get_number_list_main(view, 7))
	return completions

############################################################################
# number list に対するオートコンプリートメソッドです。
# view      sublime view
# max_count リストの数
############################################################################
def autocomp_get_number_list_main(view, max_count):
	temp_str3 = ""
	ol_default_class = sublime_view_util.get_ol_default_class()
	if ol_default_class != "":
		temp_str3 = " class=\"" + ol_default_class + "\""

	temp_str2 = "<ol" + temp_str3 + ">\n"

	i = 0
	while i < max_count:
		temp_str2 = temp_str2 + \
			sublime_view_util.get_indent() + "<li>$" + str(i+1) + "</li>\n"
		i = i + 1

	temp_str2 = temp_str2 + "</ol>\n"

	if ol_default_class == "":
		return ("number_list_" + str(max_count) + "\tHapoItak", temp_str2)
	else:
		return ("number_list_class=" + ol_default_class + "_" + str(max_count) + "\tHapoItak", temp_str2)














