import sublime, sublime_plugin, re



############################################################################
# ダブルクォーテーションに対して、エスケープシーケンスを付与します。
############################################################################
def add_escape_sequence_to_double_quotation(text):
	save = ""
	text_length = len(text)
	i = 0
	while i < text_length:
		if text[i] == "\"":
			save = save + "\\"
		save = save + text[i]
		i = i + 1

	return save

############################################################################
# HTML の特殊文字セットを変換します。
############################################################################
def replace_html_special_character(text):
	save = ""

	text_length = len(text)
	i = 0
	while i < text_length:
		if text[i] == "<":
			save = save + "&lt;"
		elif text[i] == ">":
			save = save + "&gt;"
		elif text[i] == "\"":
			save = save + "&quot;"
		elif text[i] == "&":
			save = save + "&amp;"
		else:
			save = save + text[i]
		i = i + 1

	return save


############################################################################
# 文字列をパスカル形式へ変換します。
############################################################################
def to_pascal_style(text):
	save = ""

	text_length = len(text)
	i = 0
	kirikawari = False
	while i < text_length:
		if i == 0 or kirikawari:
			save = save + (text[i]).upper()
			kirikawari = False
		elif text[i] == "_":
			kirikawari = True
		else:
			save = save + (text[i]).lower()
		i = i + 1
	return save

############################################################################
# 文字列をキャメル形式へ変換します。
############################################################################
def to_camel_style(text):
	save = ""

	text_length = len(text)
	i = 0
	kirikawari = False
	while i < text_length:
		if i == 0:
			save = save + (text[i]).lower()
			kirikawari = False
		elif kirikawari:
			save = save + (text[i]).upper()
			kirikawari = False
		elif text[i] == "_":
			kirikawari = True
		else:
			save = save + (text[i]).lower()
		i = i + 1
	return save



############################################################################
# text における一行毎の最後に word を追加します。
############################################################################
def add_word_to_end_every_line(text, word):
	text_array = text.split("\n")
	text_array_length = len(text_array)

	i = 0
	save = ""
	for text_line in text_array:
		if (i == text_array_length-1) and (len(text_line) == 0):
			# 最後の改行の場合は、word の追加を行いません。
			pass
		else:
			save = save + add_word_to_end(text_line, word)
		if not(i == text_array_length-1):
			save = save + "\n"

		i = i + 1

	return save

############################################################################
# text の最後に word を追加します。
############################################################################
def add_word_to_end(text, word):
	save = text + word
	return save

############################################################################
# text の最初と最後に tag を追加します。
############################################################################
def add_tag_to_outline(text, tag):
	save = "<" + tag + ">" + text + "</" + tag + ">"
	return save

############################################################################
# text の最初と最後に tag を追加します。
# 先頭の空白は無視します。
############################################################################
def add_tag_to_outline_skip_space(text, tag):
	text_length = len(text)
	i = 0
	while i < text_length:
		if text[i] == " " or text[i] == "\t":
			pass
		else:
			break

		i = i + 1

	if i > 0:
		save = text[0:i] + "<" + tag + ">" + text[i:text_length] + "</" + tag + ">"
	else:
		save = "<" + tag + ">" + text + "</" + tag + ">"

	return save

############################################################################
# text における一行毎の最初と最後に tag を追加します。
############################################################################
def add_tag_to_outline_every_line(text, tag):
	text_array = text.split("\n")
	text_array_length = len(text_array)

	i = 0
	save = ""
	for text_line in text_array:
		if (i == text_array_length-1) and (len(text_line) == 0):
			# 最後の改行の場合は、tag の追加を行いません。
			pass
		else:
			save = save + \
				add_tag_to_outline_skip_space(text_line, tag)
		if not(i == text_array_length-1):
			save = save + "\n"

		i = i + 1

	return save























