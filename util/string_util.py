import sublime, sublime_plugin, re

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



