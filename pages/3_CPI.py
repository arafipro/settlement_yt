import streamlit as st
import pathlib, os
from packages.defs import check_plus_minus
from dateutil.relativedelta import relativedelta

st.header("消費者物価指数(CPI)")

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
	st.text("")
	st.text("")
	st.text("")
	st.subheader("結果")
	st.subheader("予想")
	st.subheader("前回")

with col2:
	st.subheader("前月比")
	result_month = check_plus_minus(round(st.number_input("結果", key="result_month", step=0.1, label_visibility="collapsed", format="%.1f"), 2))
	predict_month = check_plus_minus(round(st.number_input("予想", key="predict_month", step=0.1, label_visibility="collapsed", format="%.1f"), 2))
	last_month = check_plus_minus(round(st.number_input("前回", key="last_month", step=0.1, label_visibility="collapsed", format="%.1f"), 2))

	st.subheader("コア・前月比")
	result_month_core = check_plus_minus(round(st.number_input("結果", key="result_month_core", step=0.1, label_visibility="collapsed", format="%.1f"), 2))
	predict_month_core = check_plus_minus(round(st.number_input("予想", key="predict_month_core", step=0.1, label_visibility="collapsed", format="%.1f"), 2))
	last_month_core = check_plus_minus(round(st.number_input("前回", key="last_month_core", step=0.1, label_visibility="collapsed", format="%.1f"), 2))

with col3:
	st.subheader("前年比")
	result_year = check_plus_minus(round(st.number_input("結果", key="result_year", step=0.1, label_visibility="collapsed", format="%.1f"), 2))
	predict_year = check_plus_minus(round(st.number_input("予想", key="predict_year", step=0.1, label_visibility="collapsed", format="%.1f"), 2))
	last_year = check_plus_minus(round(st.number_input("前回", key="last_year", step=0.1, label_visibility="collapsed", format="%.1f"), 2))

	st.subheader("コア・前年比")
	result_year_core = check_plus_minus(round(st.number_input("結果", key="result_year_core", step=0.1, label_visibility="collapsed", format="%.1f"), 2))
	predict_year_core = check_plus_minus(round(st.number_input("予想", key="predict_year_core", step=0.1, label_visibility="collapsed", format="%.1f"), 2))
	last_year_core = check_plus_minus(round(st.number_input("前回", key="last_year_core", step=0.1, label_visibility="collapsed", format="%.1f"), 2))

str_title = ""
str_title += f"{selected_last_month.year}年{selected_last_month.month}月消費者物価指数（CPI）\n"
str_title += f"{selected_date_jp}発表\n\n"

str = ""
str += f"CPI・前月比は結果{result_month}%、予想{predict_month}%、前回{last_month}%でした。\n"
str += f"CPI・前年比は結果{result_year}%、予想{predict_year}%、前回{last_year}%でした。\n"
str += f"コアCPI・前月比は結果{result_month_core}%、予想{predict_month_core}%、前回{last_month_core}%でした。\n"
str += f"コアCPI・前年比は結果{result_year_core}%、予想{predict_year_core}%、前回{last_year_core}%でした。"

st.text(str_title + str)

# if(selected_last_month.month < 10):
# 	st.markdown(f"#### cpi_{selected_last_month.year}0{selected_last_month.month}.txtを保存しますか？")
# else:
# 	st.markdown(f"#### cpi_{selected_last_month.year}{selected_last_month.month}.txtを保存しますか？")
# save = st.button("保存")

# # 現在のパスを受け取る
# current_path = os.getcwd()

# if(save and selected_last_month.month < 10):
# 	# 空のファイルのパスを指定
# 	empty_txt_file = pathlib.Path(f"{current_path}/cpi_{selected_last_month.year}0{selected_last_month.month}.txt")
# 	# 空のファイルを作成
# 	empty_txt_file.touch()
# 	# 空のファイルに読み込んだtxtを書き込む
# 	empty_txt_file.write_text(str_title + str)
# 	st.markdown(f"#### cpi_{selected_last_month.year}0{selected_last_month.month}.txtを保存しました")
# elif(save and selected_last_month.month >= 10):
# 	# 空のファイルのパスを指定
# 	empty_txt_file = pathlib.Path(f"{current_path}/cpi_{selected_last_month.year}{selected_last_month.month}.txt")
# 	# 空のファイルを作成
# 	empty_txt_file.touch()
# 	# 空のファイルに読み込んだtxtを書き込む
# 	empty_txt_file.write_text(str_title + str)
# 	st.markdown(f"#### cpi_{selected_last_month.year}{selected_last_month.month}.txtを保存しました")
# else:
# 	""
