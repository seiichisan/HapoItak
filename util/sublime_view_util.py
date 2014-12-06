import sublime, sublime_plugin, re

############################################################################
# ファイル名の拡張子を取得します。
# self sublime self
############################################################################
def get_extension_from_view(self):
	file_name = self.view.file_name()

	# self.view.set_status("key1", "ファイル名：" + file_name)

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
# self sublime self
############################################################################
def get_indent(self):
	# 設定を取得します。
	hapo_settings = sublime.load_settings("HapoItak.sublime-settings")
	indent = hapo_settings.get("indent")
	# self.view.set_status("key10", "インデント")
	return indent

############################################################################
# lang を取得します。
# self sublime self
############################################################################
def get_lang(self):
	# 設定を取得します。
	hapo_settings = sublime.load_settings("HapoItak.sublime-settings")
	lang = hapo_settings.get("lang")
	# self.view.set_status("key11", "ラング")
	return lang

############################################################################
# charset を取得します。
# self sublime self
############################################################################
def get_charset(self):
	# 設定を取得します。
	hapo_settings = sublime.load_settings("HapoItak.sublime-settings")
	charset = hapo_settings.get("charset")
	# self.view.set_status("key12", "キャーセット")
	return charset


############################################################################
# ul_default_class を取得します。
# self sublime self
############################################################################
def get_ul_default_class(self):
	# 設定を取得します。
	hapo_settings = sublime.load_settings("HapoItak.sublime-settings")
	ul_default_class = hapo_settings.get("ul_default_class")
	# self.view.set_status("key12", "キャーセット")
	return ul_default_class

############################################################################
# h_default_class を取得します。
# self sublime self
############################################################################
def get_h_default_class(self, h_level):
	# 設定を取得します。
	hapo_settings = sublime.load_settings("HapoItak.sublime-settings")
	h_default_class = hapo_settings.get("h" + str(h_level) + "_default_class")
	return h_default_class


















