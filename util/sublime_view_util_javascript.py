import sublime, sublime_plugin, re


############################################################################
# 現在のカーソル位置が javascript ブロック内であることを判定します。
# javascript ブロック内であれば、True。
############################################################################
def is_javascript_block(view):
	# view.set_status("key1", "ジャバスクリプトブロックの判定")

	# 現在のカーソル位置を取得します。
	curr_pos = view.sel()[0].begin()

	curr_row = view.rowcol(curr_pos)[0]
	curr_col = view.rowcol(curr_pos)[1]

	FIND_PATTERN_1_B = "<style type=\"text/javascript\">"
	FIND_PATTERN_1_E = "</style>"
	FIND_PATTERN_2_B = "<script>"
	FIND_PATTERN_2_E = "</script>"

	is_javascript_block_end   = False
	is_javascript_block_begin = False
	while curr_row >= 0:
		curr_line_str = get_line(view, 0, curr_row)
		if curr_line_str.find(FIND_PATTERN_1_E) > -1 or \
			curr_line_str.find(FIND_PATTERN_2_E) > -1:
			is_javascript_block_end = True
			break

		elif curr_line_str.find(FIND_PATTERN_1_B) > -1 or \
			curr_line_str.find(FIND_PATTERN_2_B) > -1:
			is_javascript_block_begin = True
			break
		curr_row = curr_row - 1

	if is_javascript_block_begin:
		return True
	return False

############################################################################
# 指定された行のテキスト文字列を取得します。
############################################################################
def get_line(view, position_x, positon_y):
	# 指定位置のポイントを求めます。
	point = view.text_point(positon_y, position_x)
	# 指定ポイントのリージョンを求めます。
	curr_region = view.line(point)
	# 指定行の内容（文字列）を取得します。
	curr_line_str = view.substr(curr_region)

	return curr_line_str
