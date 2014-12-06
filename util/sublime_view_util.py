import sublime, sublime_plugin, re

############################################################################
# ファイル名の拡張子を取得します。
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
