import streamlit as st
import pathlib, os
from packages.defs import check_plus_minus
from dateutil.relativedelta import relativedelta

st.header("小売売上高（Retail Sales）")

selected_date = st.date_input("発表日")
selected_date_jp = selected_date.strftime("%Y年%m月%d日")
selected_last_month = selected_date - relativedelta(months=1)

col1, col2, col3 = st.columns([1,4,4])
# 結果 result
# 予想 predict
# 前回 last
with col1:
	st.text("")
	st.text("")
	st.text("")
	st.subheader("結果")
	st.subheader("予想")
	st.subheader("前回")

with col2:
	st.subheader("前月比")
	# st.text("前月比")
	result = check_plus_minus(round(st.number_input("結果", key="result", step=0.1, label_visibility="collapsed", format="%.1f"), 2))
	predict = check_plus_minus(round(st.number_input("予想", key="predict", step=0.1, label_visibility="collapsed", format="%.1f"), 2))
	last = check_plus_minus(round(st.number_input("前回", key="last", step=0.1, label_visibility="collapsed", format="%.1f"), 2))

with col3:
	st.subheader("コア・前月比")
	# st.text("コア・前月比")
	result_core = check_plus_minus(round(st.number_input("結果", key="result_core", step=0.1, label_visibility="collapsed", format="%.1f"), 2))
	predict_core = check_plus_minus(round(st.number_input("予想", key="predict_core", step=0.1, label_visibility="collapsed", format="%.1f"), 2))
	last_core = check_plus_minus(round(st.number_input("前回", key="last_core", step=0.1, label_visibility="collapsed", format="%.1f"), 2))

str_title = ""
str_title += f"{selected_last_month.year}年{selected_last_month.month}月小売売上高（Retail Sales）\n"
str_title += f"{selected_date_jp}発表\n\n"

str = ""
str += f"前月比は結果{result}%、予想{predict}%、前回{last}%でした。\n"
str += f"コア・前年比は結果{result_core}%、予想{predict_core}%、前回{last_core}%でした。"

st.text(str_title + str)

if(selected_last_month.month < 10):
	st.markdown(f"#### retailsales_{selected_last_month.year}0{selected_last_month.month}.txtを保存しますか？")
else:
	st.markdown(f"#### retailsales_{selected_last_month.year}{selected_last_month.month}.txtを保存しますか？")
save = st.button("保存")

# 現在のパスを受け取る
current_path = os.getcwd()

if(save and selected_last_month.month < 10):
	# 空のファイルのパスを指定
	empty_txt_file = pathlib.Path(f"{current_path}/retailsales_{selected_last_month.year}0{selected_last_month.month}.txt")
	# 空のファイルを作成
	empty_txt_file.touch()
	# 空のファイルに読み込んだtxtを書き込む
	empty_txt_file.write_text(str_title + str)
	st.markdown(f"#### retailsales_{selected_last_month.year}0{selected_last_month.month}.txtを保存しました")
elif(save and selected_last_month.month >= 10):
	# 空のファイルのパスを指定
	empty_txt_file = pathlib.Path(f"{current_path}/retailsales_{selected_last_month.year}{selected_last_month.month}.txt")
	# 空のファイルを作成
	empty_txt_file.touch()
	# 空のファイルに読み込んだtxtを書き込む
	empty_txt_file.write_text(str_title + str)
	st.markdown(f"#### retailsales_{selected_last_month.year}{selected_last_month.month}.txtを保存しました")
else:
	""
