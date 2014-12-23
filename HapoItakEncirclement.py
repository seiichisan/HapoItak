import sublime, sublime_plugin, re

from .util import string_util
# from .util import sublime_view_util



############################################################################
# 定数
############################################################################
CONST_BR_SLASH = "br/"
CONST_BR       = "br"
CONST_TD       = "td"
CONST_LI       = "li"
CONST_P        = "p"
CONST_H1       = "h1"
CONST_H2       = "h2"
CONST_H3       = "h3"
CONST_H4       = "h4"
CONST_H5       = "h5"
CONST_H6       = "h6"

CONST_BR_SLASH_EVERY_LINE = "br/_in_every_line"
CONST_BR_EVERY_LINE       = "br_in_every_line"

CONST_TD_EVERY_LINE       = "td_in_every_line"
CONST_LI_EVERY_LINE       = "li_in_every_line"

CONST_P_EVERY_LINE        = "p_in_every_line"

CONST_H1_EVERY_LINE       = "h1_in_every_line"
CONST_H2_EVERY_LINE       = "h2_in_every_line"
CONST_H3_EVERY_LINE       = "h3_in_every_line"
CONST_H4_EVERY_LINE       = "h4_in_every_line"
CONST_H5_EVERY_LINE       = "h5_in_every_line"
CONST_H6_EVERY_LINE       = "h6_in_every_line"



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
						CONST_TD, CONST_LI, CONST_P_EVERY_LINE,
						CONST_H1_EVERY_LINE, CONST_H2_EVERY_LINE,
						CONST_H3_EVERY_LINE, CONST_H4_EVERY_LINE,
						CONST_H5_EVERY_LINE, CONST_H6_EVERY_LINE]
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

				elif tag_name == CONST_P_EVERY_LINE:
					selection = string_util.add_tag_to_outline_every_line(selection, CONST_P)

				elif tag_name == CONST_H1_EVERY_LINE:
					selection = string_util.add_tag_to_outline_every_line(selection, CONST_H1)

				elif tag_name == CONST_H2_EVERY_LINE:
					selection = string_util.add_tag_to_outline_every_line(selection, CONST_H2)

				elif tag_name == CONST_H3_EVERY_LINE:
					selection = string_util.add_tag_to_outline_every_line(selection, CONST_H3)

				elif tag_name == CONST_H4_EVERY_LINE:
					selection = string_util.add_tag_to_outline_every_line(selection, CONST_H4)

				elif tag_name == CONST_H5_EVERY_LINE:
					selection = string_util.add_tag_to_outline_every_line(selection, CONST_H5)

				elif tag_name == CONST_H6_EVERY_LINE:
					selection = string_util.add_tag_to_outline_every_line(selection, CONST_H6)
				
				else:
					selection = string_util.add_tag_to_outline(selection, tag_name)
				self.view.replace(edit, region, selection)







