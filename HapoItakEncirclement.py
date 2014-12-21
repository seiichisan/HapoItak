import sublime, sublime_plugin, re

from .util import string_util
from .util import sublime_view_util



############################################################################
# 定数
############################################################################
CONST_BR_SLASH = "br/"
CONST_BR       = "br"
CONST_TD       = "td"
CONST_LI       = "li"

CONST_BR_SLASH_EVERY_LINE = "br/_in_every_line"
CONST_BR_EVERY_LINE       = "br_in_every_line"

CONST_TD_EVERY_LINE       = "td_in_every_line"
CONST_LI_EVERY_LINE       = "li_in_every_line"

TAG_BR_SLASH = "<br/>"
TAG_BR       = "<br>"

TAG_TD = "<td>"
TAG_LI = "<li>"

############################################################################
# 囲むコマンド
############################################################################
class HapoItakEncirclementCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.list = [CONST_BR_EVERY_LINE, CONST_BR_SLASH_EVERY_LINE,
						CONST_TD_EVERY_LINE, CONST_LI_EVERY_LINE,
						CONST_BR, CONST_BR_SLASH,
						CONST_TD, CONST_LI]
		self.view.window().show_quick_panel(self.list, lambda idx: self._on_select(idx, edit))

	########################################################################
	# クイックパネルの選択肢が選択されたときに動作します。
	########################################################################
	def _on_select(self, idx, edit):
		if idx != -1:
			self.view.run_command("insert_tag_to_begin_end", {"args":{'text':self.list[idx]}})

############################################################################
# クイックパネルの選択文字列を挿入するコマンドです。
############################################################################
class InsertTagToBeginEndCommand(sublime_plugin.TextCommand):
	def run(self, edit, args):
		# self.view.set_status("key2", "クイックパネル")
		
		# # 現在のカーソル位置を取得します。
		# curr_pos = self.view.sel()[0].begin()
		# # 現在の単語のリージョンを取得します。
		# curr_region = self.view.word(curr_pos)

		# self.view.replace(edit, curr_region, args['text'])

		tag_name = args['text']

		selection_list = self.view.sel()
		for region in selection_list:
			if not region.empty():
				selection = self.view.substr(region)
				if tag_name == CONST_BR_SLASH_EVERY_LINE:
					selection = string_util.add_word_to_end_every_line(selection, TAG_BR_SLASH)

				elif tag_name == CONST_BR_EVERY_LINE:
					selection = string_util.add_word_to_end_every_line(selection, TAG_BR)
				
				elif tag_name == CONST_BR_SLASH:
					selection = string_util.add_word_to_end(selection, TAG_BR_SLASH)
				
				elif tag_name == CONST_BR:
					selection = string_util.add_word_to_end(selection, TAG_BR)

				elif tag_name == CONST_TD_EVERY_LINE:
					selection = \
						string_util.add_tag_to_outline_every_line(selection, CONST_TD)

				elif tag_name == CONST_LI_EVERY_LINE:
					selection = \
						string_util.add_tag_to_outline_every_line(selection, CONST_LI)
				
				else:
					selection = string_util.add_tag_to_outline(selection, tag_name)
				self.view.replace(edit, region, selection)






# ############################################################################
# # クイックパネルに関連付けられたメソッドです。
# # 選択時、InsertMyText メソッドを呼び出すことで、選択された文字列を挿入します。
# ############################################################################
# def on_done(self, index):
# 	#self.view.set_status("key1", "クイックパネルインデックス=" + index)
# 	# if index != -1:
# 	# 	self.view.run_command("insert_my_text", {"args":{'text':self.list[index]}})

