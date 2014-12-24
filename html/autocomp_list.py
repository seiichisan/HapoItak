import sublime, sublime_plugin, re

from ..util import sublime_view_util

############################################################################
# list に対するオートコンプリートメソッドです。
############################################################################
def autocomp_get_list(view):
	ul_default_class_list = sublime_view_util.get_ul_default_class()
	ul_count_list         = sublime_view_util.get_ul_count()

	completions = []
	for ul_default_class in ul_default_class_list:
		for ul_count in ul_count_list:
			completions.append(get_list(ul_default_class, ul_count))

	return completions

############################################################################
# ul タグを取得します。
# ul_default_class ul タグのデフォルトクラス
# max_count        li 要素の数
############################################################################
def get_list(ul_default_class, max_count):
	temp_str3 = " class=\"" + ul_default_class + "\""
	temp_str2 = "<ul" + temp_str3 + ">\n"

	i = 0
	while i < max_count:
		temp_str2 = temp_str2 + \
			sublime_view_util.get_indent() + "<li>$" + str(i+1) + "</li>\n"
		i = i + 1

	temp_str2 = temp_str2 + "</ul>\n"

	return ("list_class=" + ul_default_class + "*" + \
		str(max_count) + "\tHapoItak", temp_str2)




############################################################################
# number list に対するオートコンプリートメソッドです。
############################################################################
def autocomp_get_number_list(view):
	ol_default_class_list = sublime_view_util.get_ol_default_class()
	ol_count_list         = sublime_view_util.get_ol_count()

	completions = []
	for ol_default_class in ol_default_class_list:
		for ol_count in ol_count_list:
			completions.append(get_number_list(ol_default_class, ol_count))

	return completions

############################################################################
# ol タグを取得します。
# ol_default_class ol タグのデフォルトクラス
# max_count        li 要素の数
############################################################################
def get_number_list(ol_default_class, max_count):
	temp_str3 = " class=\"" + ol_default_class + "\""
	temp_str2 = "<ol" + temp_str3 + ">\n"

	i = 0
	while i < max_count:
		temp_str2 = temp_str2 + \
			sublime_view_util.get_indent() + "<li>$" + str(i+1) + "</li>\n"
		i = i + 1

	temp_str2 = temp_str2 + "</ol>\n"

	return ("number_list_class=" + ol_default_class + "*" + \
		str(max_count) + "\tHapoItak", temp_str2)














