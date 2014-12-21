import sublime, sublime_plugin, re

from .util import string_util
from .util import sublime_view_util

from .java import java_property

############################################################################
# 関数 Begin
############################################################################

# ステータスバー表示
# self.view.set_status("key1", "In sample_read_excel3")

############################################################################
# 関数 End
############################################################################


# tameshi = 10

############################################################################
# Translate Command
# メイン処理
############################################################################
class HapoItakTranslateCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		# global tameshi
		# tameshi = tameshi + 1
		# self.view.set_status("key1", "試し = " + str(tameshi))

		# 現在のカーソル位置を取得します。
		curr_pos = self.view.sel()[0].begin()
		# 現在の行のリージョンを取得します。
		curr_region = self.view.line(curr_pos)
		# 現在の行の内容（文字列）を取得します。
		curr_line_str = self.view.substr(curr_region)

		extension = sublime_view_util.get_extension_from_view(self.view)

		# java ファイルのための処理
		if extension == "java":
			if java_property.match_property(self, edit, curr_pos, curr_region, curr_line_str):
				# sublime_view_util.move_cursor(self, edit, 0, -5)
				return True

		self.view.run_command('auto_complete', {
			'disable_auto_insert'      : False,
			'api_completions_only'     : True,
			'next_competion_if_showing': False
		})

# ############################################################################
# # クイックパネルに関連付けられたメソッドです。
# # 選択時、InsertMyText メソッドを呼び出すことで、選択された文字列を挿入します。
# ############################################################################
# def on_done(self, index):
# 	if index != -1:
# 		self.view.run_command("insert_my_text", {"args":{'text':self.list[index]}})

# ############################################################################
# # クイックパネルの選択文字列を挿入するコマンドです。
# ############################################################################
# class InsertMyText(sublime_plugin.TextCommand):
# 	def run(self, edit, args):
# 		self.view.set_status("key1", "クイックパネル")
		
# 		# 現在のカーソル位置を取得します。
# 		curr_pos = self.view.sel()[0].begin()
# 		# 現在の単語のリージョンを取得します。
# 		curr_region = self.view.word(curr_pos)

# 		self.view.replace(edit, curr_region, args['text'])








