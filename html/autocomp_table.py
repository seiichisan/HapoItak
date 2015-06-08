import sublime, sublime_plugin, re

from ..util import sublime_view_util

############################################################################
# table を取得します。
############################################################################
def get_table(view, tr_count, td_count):
	save = ""

	save += "<table>\n"
	save += get_tr_td(view, tr_count, td_count)
	# k = 1
	# i = 0
	# while i < tr_count:
	# 	save += sublime_view_util.get_indent() + "<tr>\n"
	# 	j = 0
	# 	while j < td_count:
	# 		save += sublime_view_util.get_indent() + \
	# 					sublime_view_util.get_indent() + "<td>$" + str(k) + "</td>\n"
	# 		j += 1
	# 		k += 1
	# 	save += sublime_view_util.get_indent() + "</tr>\n"
	# 	i += 1
	save += "</table>\n"

	return save;












############################################################################
# tr ～ td を取得します。
############################################################################
def get_tr_td(view, tr_count, td_count):
	save = ""

	k = 1
	i = 0
	while i < tr_count:
		save += sublime_view_util.get_indent() + "<tr>\n"
		j = 0
		while j < td_count:
			save += sublime_view_util.get_indent() + \
						sublime_view_util.get_indent() + "<td>$" + str(k) + "</td>\n"
			j += 1
			k += 1
		save += sublime_view_util.get_indent() + "</tr>\n"
		i += 1

	return save;





############################################################################
# table に対するオートコンプリートを取得します。
############################################################################
def autocomp_get_table(view):
	completions = []

	tr_count_list = sublime_view_util.get_table_tr_count()
	td_count_list = sublime_view_util.get_table_td_count()

	for tr_count in tr_count_list:
		for td_count in td_count_list:
			key = "table_tr*" + str(tr_count) + "_td*" + str(td_count) + "\tHapoItak"
			completions.append((key, get_table(view, tr_count, td_count)))

	for tr_count in tr_count_list:
		for td_count in td_count_list:
			key = "tr*" + str(tr_count) + "_td*" + str(td_count) + "\tHapoItak"
			completions.append((key, get_tr_td(view, tr_count, td_count)))

	return completions






