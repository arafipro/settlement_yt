import streamlit as st
import pathlib, os
from packages.defs import jp_yen, fluct_last, fluct_last_eps, fluct_predict, fluct_predict_eps

st.header("通期決算")

stock_name = st.text_input("銘柄名", key="stock_name")
col1, col2 = st.columns(2)
with col1:
	ticker = st.text_input("ティッカ", key="ticker", max_chars=5)
with col2:
	selected_date = st.date_input("発表日")
	selected_date_jp = selected_date.strftime("%Y年%m月%d日")

full_year = selected_date.year - 1

col1, col2, col3, col4 = st.columns([1,3,3,3])

# 結果 result
# 予想 predict
# 前回 last
with col1:
	st.text("")
	st.text("")
	st.text("")
	st.subheader("前回")
	st.subheader("結果")
	st.subheader("予想")

with col2:
	st.subheader("売上高")
	last_sales = round(st.number_input("前回", key="last_sales", step=0.1, label_visibility="collapsed"), 2)
	current_sales = round(st.number_input("結果", key="current_sales", step=0.1, label_visibility="collapsed"), 2)
	predict_sales = round(st.number_input("予想", key="predict_sales", step=0.1, label_visibility="collapsed"), 2)

with col3:
	st.subheader("純利益")
	last_net_income = round(st.number_input("前回", key="last_net_income", step=0.1, label_visibility="collapsed"), 2)
	current_net_income = round(st.number_input("結果", key="current_net_income", step=0.1, label_visibility="collapsed"), 2)
	predict_net_income = round(st.number_input("予想", key="predict_net_income", step=0.1, label_visibility="collapsed"), 2)

with col4:
	st.subheader("EPS")
	last_eps = round(st.number_input("前回", key="last_eps", step=0.1, label_visibility="collapsed"), 2)
	current_eps = round(st.number_input("結果", key="current_eps", step=0.1, label_visibility="collapsed"), 2)
	predict_eps = round(st.number_input("予想", key="predict_eps", step=0.1, label_visibility="collapsed"), 2)

if (stock_name=="" or ticker==""):
	st.markdown(f"#### 銘柄詳細をすべて入力してください")
else:
	str_title = ""
	str_title += f"{stock_name}（{ticker.upper()}）\n"
	str_title += f"{full_year}年通期決算結果\n"
	str_title += f"{selected_date_jp}発表\n\n"
	st.text(str_title)

	if not all(x != 0 for x in [last_sales,current_sales,predict_sales,last_net_income,current_net_income,predict_net_income,last_eps,current_eps,predict_eps]):
		st.markdown(f"#### 数字をすべて入力してください")
	else:
		str = ""
		str += f"売上高は前年の{jp_yen(last_sales)}ドルから{fluct_last(current_sales,last_sales)}の{jp_yen(current_sales)}ドルとなりました。\n"
		str += f"純利益は前年の{jp_yen(last_net_income)}ドルから{fluct_last(current_net_income,last_net_income)}の{jp_yen(current_net_income)}ドルとなりました。\n"
		str += f"EPSは前年の{last_eps}ドルから{fluct_last_eps(current_eps,last_eps)}の{current_eps}ドルとなりました。\n\n"

		str += f"売上高はアナリスト予想{jp_yen(predict_sales)}ドルで結果が{jp_yen(current_sales)}ドル、{fluct_predict(current_sales,predict_sales)}りました。\n"
		str += f"純利益はアナリスト予想{jp_yen(predict_net_income)}ドルで結果が{jp_yen(current_net_income)}ドル、{fluct_predict(current_net_income,predict_net_income)}りました。\n"
		str += f"EPSはアナリスト予想{predict_eps}ドルで結果が{current_eps}ドル、{fluct_predict_eps(current_eps,predict_eps)}りました。"

		st.text(str)

		# st.markdown(f"#### {ticker.upper()}_{full_year}_year.txtを保存しますか？")
		# save = st.button("保存")
		# if(save):
		# 	# 現在のパスを受け取る
		# 	current_path = os.getcwd()
		# 	# 空のファイルのパスを指定
		# 	empty_txt_file = pathlib.Path(f"{current_path}/{ticker.upper()}_{full_year}_year.txt")
		# 	# 空のファイルを作成
		# 	empty_txt_file.touch()
		# 	# 空のファイルに読み込んだtxtを書き込む
		# 	empty_txt_file.write_text(str_title + str)
		# 	st.markdown(f"#### {ticker.upper()}_{full_year}_year.txtを保存しました")
