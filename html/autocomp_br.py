import sublime, sublime_plugin, re

############################################################################
# <br/> に対するオートコンプリートメソッドです。
############################################################################
def autocomp_get_br(view):
	completions = []
	completions.append(("br/\ttag", "<br/>"))
	return completions
