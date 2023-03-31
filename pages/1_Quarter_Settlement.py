import streamlit as st
import pathlib, os
from packages.defs import jp_yen, fluct_last, fluct_last_eps, fluct_predict, fluct_predict_eps

st.header("四半期決算")

q_stock_name = st.text_input("銘柄名", key="q_stock_name")
col1, col2, col3 = st.columns(3)
with col1:
	q_ticker = st.text_input("ティッカ", key="q_ticker", max_chars=5)
with col2:
	quarter = st.number_input("四半期", key="quarter", max_value=4, min_value=1)
with col3:
	q_selected_date = st.date_input("発表日")
	q_selected_date_jp = q_selected_date.strftime("%Y年%m月%d日")

if(quarter == 4):
	quarter_year = q_selected_date.year - 1
else:
	quarter_year = q_selected_date.year

col1, col2, col3, col4 = st.columns([1,3,3,3])

with col1:
	st.text("")
	st.text("")
	st.text("")
	st.subheader("前回")
	st.subheader("結果")
	st.subheader("予想")

with col2:
	st.subheader("売上高")
	q_last_sales = round(st.number_input("前回", key="q_last_sales", step=0.1, label_visibility="collapsed"), 2)
	q_current_sales = round(st.number_input("結果", key="q_current_sales", step=0.1, label_visibility="collapsed"), 2)
	q_predict_sales = round(st.number_input("予想", key="q_predict_sales", step=0.1, label_visibility="collapsed"), 2)

with col3:
	st.subheader("純利益")
	q_last_net_income = round(st.number_input("前回", key="q_last_net_income", step=0.1, label_visibility="collapsed"), 2)
	q_current_net_income = round(st.number_input("結果", key="q_current_net_income", step=0.1, label_visibility="collapsed"), 2)
	q_predict_net_income = round(st.number_input("予想", key="q_predict_net_income", step=0.1, label_visibility="collapsed"), 2)

with col4:
	st.subheader("EPS")
	q_last_eps = round(st.number_input("前回", key="q_last_eps", step=0.1, label_visibility="collapsed"), 2)
	q_current_eps = round(st.number_input("結果", key="q_current_eps", step=0.1, label_visibility="collapsed"), 2)
	q_predict_eps = round(st.number_input("予想", key="q_predict_eps", step=0.1, label_visibility="collapsed"), 2)

if (q_stock_name=="" or q_ticker==""):
	st.markdown(f"#### 銘柄詳細をすべて入力してください")
else:
	str_title = ""
	str_title += f"{q_stock_name}（{q_ticker.upper()}）\n"
	str_title += f"{quarter_year}年第{quarter}四半期決算結果\n"
	str_title += f"{q_selected_date_jp}発表\n\n"
	st.text(str_title)

	if not all(x != 0 for x in [q_last_sales,q_current_sales,q_predict_sales,q_last_net_income,q_current_net_income,q_predict_net_income,q_last_eps,q_current_eps,q_predict_eps]):
		st.markdown(f"#### 数字をすべて入力してください")
	else:
		str = ""
		# 売上高は前年の108億7100万ドルから14.0%増の123億9000万ドルとなりました。
		str += f"売上高は前年の{jp_yen(q_last_sales)}ドルから{fluct_last(q_current_sales,q_last_sales)}の{jp_yen(q_current_sales)}ドルとなりました。\n"
		str += f"純利益は前年の{jp_yen(q_last_net_income)}ドルから{fluct_last(q_current_net_income,q_last_net_income)}の{jp_yen(q_current_net_income)}ドルとなりました。\n"
		str += f"EPSは前年の{q_last_eps}ドルから{fluct_last_eps(q_current_eps,q_last_eps)}の{q_current_eps}ドルとなりました。\n\n"

		str += f"売上高予想は{jp_yen(q_predict_sales)}ドルで結果は{fluct_predict(q_current_sales,q_predict_sales)}る{jp_yen(q_current_sales)}ドルとなりました。\n"
		str += f"純利益予想は{jp_yen(q_predict_net_income)}ドルで結果は{fluct_predict(q_current_net_income,q_predict_net_income)}る{jp_yen(q_current_net_income)}ドルとなりました。\n"
		str += f"EPS予想は{q_predict_eps}ドルで結果は{fluct_predict_eps(q_current_eps,q_predict_eps)}る{q_current_eps}ドルとなりました。"

		st.text(str)

		# st.markdown(f"#### {q_ticker.upper()}_{quarter_year}_{quarter}Q.txtを保存しますか？")
		# save = st.button("保存")
		# if(save):
		# 	# 現在のパスを受け取る
		# 	current_path = os.getcwd()
		# 	# 空のファイルのパスを指定
		# 	empty_txt_file = pathlib.Path(f"{current_path}/{q_ticker.upper()}_{quarter_year}_{quarter}Q.txt")
		# 	# 空のファイルを作成
		# 	empty_txt_file.touch()
		# 	# 空のファイルに読み込んだtxtを書き込む
		# 	empty_txt_file.write_text(str_title + str)
		# 	st.markdown(f"#### {q_ticker.upper()}_{quarter_year}_{quarter}Q.txtを保存しました")
