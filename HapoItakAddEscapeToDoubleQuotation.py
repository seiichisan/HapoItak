import sublime, sublime_plugin, re
from .util import string_util
from .util import sublime_view_util

############################################################################
# ダブルクォーテーションに対してエスケープシーケンスを付与します。
############################################################################
class HapoItakAddEscapeToDoubleQuotationCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		selection_list = self.view.sel()
		for region in selection_list:
			if not region.empty():
				selection = self.view.substr(region)
				selection = string_util.add_escape_sequence_to_double_quotation(selection)
				self.view.replace(edit, region, selection)
