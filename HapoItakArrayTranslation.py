import sublime, sublime_plugin, re

from .util import string_util
from .util import sublime_view_util



############################################################################
# 定数
############################################################################
CONST_WRAP_DOUBLE_QUOTATION_EVERY_LINE = "wrap_double_quotation_and_comma_every_line"
CONST_WRAP_DOUBLE_QUOTATION_EVERY_WORD = "wrap_double_quotation_and_comma_every_word"
CONST_COMMA_EVERY_LINE                 = "adding_comma_at_the_end_every_line"
CONST_COMMA_EVERY_WORD                 = "adding_comma_at_the_end_every_word"


############################################################################
# 囲むコマンド
############################################################################
class HapoItakArrayTranslationCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.list = [CONST_WRAP_DOUBLE_QUOTATION_EVERY_LINE,
						CONST_WRAP_DOUBLE_QUOTATION_EVERY_WORD,
						CONST_COMMA_EVERY_LINE, CONST_COMMA_EVERY_WORD]
		self.view.window().show_quick_panel(self.list, lambda idx: self._on_select(idx, edit))

	########################################################################
	# クイックパネルの選択肢が選択されたときに動作します。
	########################################################################
	def _on_select(self, idx, edit):
		if idx != -1:
			self.view.run_command("insert_quotation_to_begin_end", {"args":{'text':self.list[idx]}})

############################################################################
# クイックパネルの選択文字列を挿入するコマンドです。
############################################################################
class InsertQuotationToBeginEndCommand(sublime_plugin.TextCommand):
	def run(self, edit, args):
		tag_name = args['text']

		selection_list = self.view.sel()
		for region in selection_list:
			if not region.empty():
				selection = self.view.substr(region)
				if tag_name == CONST_WRAP_DOUBLE_QUOTATION_EVERY_LINE:
					selection = string_util.wrap_double_quotation_every_line(selection)

				elif tag_name == CONST_WRAP_DOUBLE_QUOTATION_EVERY_WORD:
					selection = string_util.wrap_double_quotation_every_word(selection)
				
				elif tag_name == CONST_COMMA_EVERY_LINE:
					selection = string_util.add_comma_at_the_end_every_line(selection)
				
				elif tag_name == CONST_COMMA_EVERY_WORD:
					selection = string_util.add_comma_at_the_end_every_word(selection)

				self.view.replace(edit, region, selection)






# ############################################################################
# # クイックパネルに関連付けられたメソッドです。
# # 選択時、InsertMyText メソッドを呼び出すことで、選択された文字列を挿入します。
# ############################################################################
# def on_done(self, index):
# 	#self.view.set_status("key1", "クイックパネルインデックス=" + index)
# 	# if index != -1:
# 	# 	self.view.run_command("insert_my_text", {"args":{'text':self.list[index]}})

