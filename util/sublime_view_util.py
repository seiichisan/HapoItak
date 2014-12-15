import sublime, sublime_plugin, re

############################################################################
# ファイル名の拡張子を取得します。
# view sublime view
############################################################################
def get_extension_from_view(view):
	file_name = view.file_name()
	return get_extension(file_name)

############################################################################
# ファイル名の拡張子を取得します。
############################################################################
def get_extension(text):
	# , で分割した最後の単語を拡張子として取り出します。
	word_array = text.split(".")

	extension = ""
	for i, word in enumerate(word_array):
		if i > 0:
			extension = word

	return extension









############################################################################
# インデントを取得します。
############################################################################
def get_indent():
	# 設定を取得します。
	hapo_settings = sublime.load_settings("HapoItak.sublime-settings")
	indent = hapo_settings.get("indent")
	return indent

############################################################################
# css_base_path を取得します。
############################################################################
def get_css_base_path():
	# 設定を取得します。
	hapo_settings = sublime.load_settings("HapoItak.sublime-settings")
	css_base_path = hapo_settings.get("css_base_path")
	return css_base_path

############################################################################
# javascript_base_path を取得します。
############################################################################
def get_javascript_base_path():
	# 設定を取得します。
	hapo_settings = sublime.load_settings("HapoItak.sublime-settings")
	javascript_base_path = hapo_settings.get("javascript_base_path")
	return javascript_base_path





############################################################################
# lang を取得します。
############################################################################
def get_lang():
	# 設定を取得します。
	hapo_settings = sublime.load_settings("HapoItak.sublime-settings")
	lang = hapo_settings.get("lang")
	return lang

############################################################################
# charset を取得します。
############################################################################
def get_charset():
	# 設定を取得します。
	hapo_settings = sublime.load_settings("HapoItak.sublime-settings")
	charset = hapo_settings.get("charset")
	return charset


############################################################################
# ul_default_class を取得します。
############################################################################
def get_ul_default_class():
	# 設定を取得します。
	hapo_settings = sublime.load_settings("HapoItak.sublime-settings")
	ul_default_class = hapo_settings.get("ul_default_class")
	return ul_default_class

############################################################################
# ul_count を取得します。
############################################################################
def get_ul_count():
	hapo_settings = sublime.load_settings("HapoItak.sublime-settings")
	ul_count = hapo_settings.get("ul_count")
	return ul_count






############################################################################
# ol_default_class を取得します。
############################################################################
def get_ol_default_class():
	# 設定を取得します。
	hapo_settings = sublime.load_settings("HapoItak.sublime-settings")
	ol_default_class = hapo_settings.get("ol_default_class")
	return ol_default_class

############################################################################
# ol_count を取得します。
############################################################################
def get_ol_count():
	hapo_settings = sublime.load_settings("HapoItak.sublime-settings")
	ol_count = hapo_settings.get("ol_count")
	return ol_count














############################################################################
# pre_default_class を取得します。
############################################################################
def get_pre_default_class():
	# 設定を取得します。
	hapo_settings = sublime.load_settings("HapoItak.sublime-settings")
	pre_default_class = hapo_settings.get("pre_default_class")
	return pre_default_class


############################################################################
# p_default_class を取得します。
############################################################################
def get_p_default_class():
	# 設定を取得します。
	hapo_settings = sublime.load_settings("HapoItak.sublime-settings")
	p_default_class = hapo_settings.get("p_default_class")
	return p_default_class

############################################################################
# div_default_class を取得します。
############################################################################
def get_div_default_class():
	# 設定を取得します。
	hapo_settings = sublime.load_settings("HapoItak.sublime-settings")
	div_default_class = hapo_settings.get("div_default_class")
	return div_default_class













############################################################################
# h_default_class を取得します。
############################################################################
def get_h_default_class(h_level):
	# 設定を取得します。
	hapo_settings = sublime.load_settings("HapoItak.sublime-settings")
	h_default_class = hapo_settings.get("h" + str(h_level) + "_default_class")
	return h_default_class











############################################################################
# 移動列数と移動行数を指定することにより、現在のカーソル位置を移動します。
# move_col 移動列数
# move_row 移動行数
############################################################################
def move_cursor(self, move_col, move_row):
	# self.view.set_status("key1", "ムーブカーソル")

	curr_col = self.view.rowcol(self.view.sel()[0].begin())[1]
	curr_row = self.view.rowcol(self.view.sel()[0].begin())[0]

	# self.view.set_status("key3", "現在のカーソル位置 = " + str(curr_col) + str(curr_row))

	curr_col = curr_col + move_col
	curr_row = curr_row + move_row

	target = self.view.text_point(curr_row, curr_col)
	self.view.sel().clear()
	self.view.sel().add(sublime.Region(target))












