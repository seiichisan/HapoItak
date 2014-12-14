import sublime, sublime_plugin, re

from ..util import sublime_view_util

############################################################################
# ie7 css hack first child を取得します。
############################################################################
def get_css_hack_ie7_first_child():
	return "*:first-child+html "

############################################################################
# css hack のオートコンプリートメソッドです。
############################################################################
def autocomp_get_css_hack(view):
	completions = []

	completions.append(("css_hack_ie7_first_child\tHapoItak", \
		get_css_hack_ie7_first_child()))

	return completions
