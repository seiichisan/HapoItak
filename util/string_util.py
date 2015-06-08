import sublime, sublime_plugin, re

############################################################################
# ダブルクォーテーションとバックスラッシュをエスケープします。
############################################################################
def add_escape_sequence_to_double_quotation(text):
	save = ""
	text_length = len(text)
	i = 0
	while i < text_length:
		if text[i] == "\"" or text[i] == "\\":
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
# word 付与系 Begin
############################################################################

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
# word 付与系 End
############################################################################












############################################################################
# tag 付与系 Begin
############################################################################

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










############################################################################
# text の最初と最後に JSP エクスプレッション <%= %> を追加します。
############################################################################
def add_jsp_expression_to_outline(text):
	save = "<%= " + text + " %>"

	return save


############################################################################
# text の最初と最後に JSP エクスプレッション <%= %> を追加します。
# 先頭の空白は無視します。
############################################################################
def add_jsp_expression_to_outline_skip_space(text):
	text_length = len(text)
	i = 0
	while i < text_length:
		if text[i] == " " or text[i] == "\t":
			pass
		else:
			break

		i = i + 1

	if i > 0:
		save = text[0:i] + "<%= " + text[i:text_length] + " %>"
	else:
		save = "<%= " + text + " %>"

	return save

############################################################################
# text における一行毎の最初と最後に JSP エクスプレッション <%= %> を追加します。
############################################################################
def add_jsp_expression_to_outline_every_line(text):
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
				add_jsp_expression_to_outline_skip_space(text_line)
		if not(i == text_array_length-1):
			save = save + "\n"

		i = i + 1

	return save





############################################################################
# text における一行毎の最初と最後に td タグと JSP エクスプレッション <%= %> を追加します。
############################################################################
def add_td_jsp_expression_to_outline_every_line(text):
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
				add_tag_to_outline_skip_space( \
					add_jsp_expression_to_outline_skip_space(text_line), "td")
		if not(i == text_array_length-1):
			save = save + "\n"

		i = i + 1

	return save











############################################################################
# tag 付与系 End
############################################################################














############################################################################
# カンマ付与処理系 Begin
############################################################################

############################################################################
# text の一行毎の最後にカンマを付与します。
############################################################################
def add_comma_at_the_end_every_line(text):
	text_array = text.split("\n")
	text_array_length = len(text_array)

	i = 0
	save = ""
	for text_line in text_array:
		if (i == text_array_length-1) and (len(text_line) == 0):
			pass
		else:
			if i == text_array_length-2:
				save = save + text_line
			else:
				save = save + \
					add_word_to_end(text_line, ",")

		if not(i == text_array_length-1):
			save = save + "\n"

		i = i + 1

	return save

############################################################################
# text の単語毎の最後にカンマを付与します。
# 行分割を行い、行毎に処理を行います。
############################################################################
def add_comma_at_the_end_every_word(text):
	text_array = text.split("\n")
	text_array_length = len(text_array)

	if len(text_array[text_array_length-1]) == 0:
		is_semi_last = True
	else:
		is_semi_last = False

	i = 0
	save = ""
	for text_line in text_array:
		if i == text_array_length-2 and is_semi_last:
			save = save + add_comma_at_the_end_every_word_main(text_line, True)
		elif i == text_array_length-1:
			save = save + add_comma_at_the_end_every_word_main(text_line, True)
		else:
			save = save + add_comma_at_the_end_every_word_main(text_line, False)
		if not(i == text_array_length-1):
			save = save + "\n"
		i = i + 1

	return save

############################################################################
# text の単語毎の最後にカンマを付与します。
# 一行を単語で分割し、単語毎に処理を行います。
############################################################################
def add_comma_at_the_end_every_word_main(text, is_last_line):
	text_array = text.split(" ")
	text_array_length = len(text_array)

	i = 0
	save = ""
	for text_line in text_array:
		if len(text_line) == 0:
			pass
		elif not(is_last_line):
			save = save + add_word_to_end(text_line, ",")
		elif i == text_array_length-1:
			save = save + text_line
		else:
			save = save + add_word_to_end(text_line, ",")

		if not(i == text_array_length-1):
			save = save + " "

		i = i + 1

	return save

############################################################################
# カンマ付与処理系 End
############################################################################











############################################################################
# ダブルクォーテーションで囲む系 Begin
############################################################################

############################################################################
# ダブルクォーテーションで一行毎の text を囲みます。
# 先頭の空白は無視して、ダブルクォーテーションで text を囲みます。
# 各行の最後には、カンマを付与します。
# 最後行のだけ最後尾のカンマ付与をスキップします。
############################################################################
def wrap_double_quotation_every_line(text, is_double_quotation):
	text_array = text.split("\n")
	text_array_length = len(text_array)

	i = 0
	save = ""
	for text_line in text_array:
		if (i == text_array_length-1) and (len(text_line) == 0):
			pass
		else:
			if i == text_array_length-2:
				save = save + \
					wrap_double_quotation_to_outline(text_line, True, is_double_quotation)
			else:
				save = save + \
					wrap_double_quotation_to_outline(text_line, False, is_double_quotation)

		if not(i == text_array_length-1):
			save = save + "\n"

		i = i + 1

	return save

############################################################################
# ダブルクォーテーションで単語毎の text を囲みます。
# 先頭の空白は無視して、ダブルクォーテーションで text を囲みます。
# 各単語の最後には、カンマを付与します。
# 最後だけ最後尾のカンマ付与をスキップします。
############################################################################
def wrap_double_quotation_every_word(text, is_double_quotation):
	text_array = text.split("\n")
	text_array_length = len(text_array)

	if len(text_array[text_array_length-1]) == 0:
		is_semi_last = True
	else:
		is_semi_last = False

	i = 0
	save = ""
	for text_line in text_array:
		if i == text_array_length-2 and is_semi_last:
			save = save + wrap_double_quotation_every_word_main(text_line, True, is_double_quotation)
		elif i == text_array_length-1:
			save = save + wrap_double_quotation_every_word_main(text_line, True, is_double_quotation)
		else:
			save = save + wrap_double_quotation_every_word_main(text_line, False, is_double_quotation)
		if not(i == text_array_length-1):
			save = save + "\n"
		i = i + 1

	return save

############################################################################
# ダブルクォーテーションで単語毎の text を囲みます。
# 先頭の空白は無視して、ダブルクォーテーションで text を囲みます。
# 各単語の最後には、カンマを付与します。
# 最後だけ最後尾のカンマ付与をスキップします。
############################################################################
def wrap_double_quotation_every_word_main(text, is_last_line, is_double_quotation):
	if len(text) == 0:
		return ""

	text_array = text.split(" ")
	text_array_length = len(text_array)

	i = 0
	save = ""
	for text_line in text_array:
		if len(text_line) == 0:
			pass
		elif not(is_last_line):
			save = save + \
				wrap_double_quotation_to_outline(text_line, False, is_double_quotation)
		elif i == text_array_length-1:
			save = save + \
				wrap_double_quotation_to_outline(text_line, True, is_double_quotation)
		else:
			save = save + \
				wrap_double_quotation_to_outline(text_line, False, is_double_quotation)

		if not(i == text_array_length-1):
			save = save + " "

		i = i + 1

	return save

############################################################################
# ダブルクォーテーションで text を囲みます。
# 先頭の空白は無視して、ダブルクォーテーションで text を囲みます。
# is_last_line が false の場合、最後にカンマを付けます。
# is_double_quotation が true の場合、ダブルクォーテーションで囲みます。
############################################################################
def wrap_double_quotation_to_outline(text, is_last_line, is_double_quotation):
	if is_double_quotation:
		kakomi_moji = "\""
	else:
		kakomi_moji = "'"

	text_length = len(text)
	i = 0
	while i < text_length:
		if text[i] == " " or text[i] == "\t":
			pass
		else:
			break

		i = i + 1

	if i > 0:
		save = text[0:i] + kakomi_moji + text[i:text_length] + kakomi_moji
	else:
		save = kakomi_moji + text + kakomi_moji

	if is_last_line:
		pass
	else:
		save = save + ","

	return save

############################################################################
# ダブルクォーテーションで囲む系 End
############################################################################

















