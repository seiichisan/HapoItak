import sublime, sublime_plugin, re

from ..util import sublime_view_util
from ..util import sublime_view_util_javascript

############################################################################
# document に対するオートコンプリートメソッドです。
############################################################################
def autocomp_get_document(view, is_javascript):
	completions = []

	# javascript の場合だけ、動作します。の判定
	if is_javascript or sublime_view_util_javascript.is_javascript_block(view):
		pass
	else:
		return completions

	HAPO_ITAK_STR = "\tHapoItak"

	auto_keyword = "document_getElementById" + HAPO_ITAK_STR
	auto_value   = "document.getElementById($1)"
	completions.append((auto_keyword, auto_value))

	auto_keyword = "document_getElementsByClassName" + HAPO_ITAK_STR
	auto_value   = "document.getElementsByClassName($1)"
	completions.append((auto_keyword, auto_value))

	auto_keyword = "document_getElementsByName" + HAPO_ITAK_STR
	auto_value   = "document.getElementsByName($1)"
	completions.append((auto_keyword, auto_value))

	auto_keyword = "document_getElementsByTagName" + HAPO_ITAK_STR
	auto_value   = "document.getElementsByTagName($1)"
	completions.append((auto_keyword, auto_value))

	auto_keyword = "document_querySelector" + HAPO_ITAK_STR
	auto_value   = "document.querySelector($1)"
	completions.append((auto_keyword, auto_value))

	auto_keyword = "document_querySelectorAll" + HAPO_ITAK_STR
	auto_value   = "document.querySelectorAll($1)"
	completions.append((auto_keyword, auto_value))

	return completions



