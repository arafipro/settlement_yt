# 英数字を漢数字に変更
def jp_yen(jp_yen):
	if(len(str(jp_yen)) > 8):
		str(jp_yen*100)
		cho = str(jp_yen*100)[-14:-10]
		oku = str(jp_yen*100)[-10:-6]
		man = str(jp_yen*100)[-6:-2]
		return f"{cho}兆{oku}億{man}万"
	elif(len(str(jp_yen)) > 4):
		str(jp_yen*100)
		oku = str(jp_yen*100)[-10:-6]
		man = str(jp_yen*100)[-6:-2]
		return f"{oku}億{man}万"
	else:
		str(jp_yen*100)
		man = str(jp_yen*100)[-6:-2]
		return f"{man}万"

# 当期 current - 前期 last
# 売上高、純利益
def fluct_last(current, last):
	if(current - last >= 0):
		return f"{round((current - last)/last*100, 1)}%増"
	elif(current - last < 0):
		return f"{round(-(current - last)/last*100, 1)}%減"
	else:
		return "変化なし"

# 当期 current - 前期 last
# EPS
def fluct_last_eps(current, last):
	if(current - last >= 0):
		return (f"{round(current - last, 2)}ドル増")
	elif(current - last < 0):
		return (f"{round(-(current - last), 2)}ドル減")
	else:
		return ("変化なし")

# 当期 current - アナリスト予想 predict
# 売上高、純利益
def fluct_predict(current, predict):
	if((current - predict)/predict >= 0):
		return (f"{round((current - predict)/predict*100, 1)}%上回")
	elif((current - predict)/predict < 0):
		return (f"{round(-(current - predict)/predict*100, 1)}%下回")
	else:
		return "変化なし"

# 当期 current - アナリスト予想 predict
# EPS
def fluct_predict_eps(current, predict):
	if(current - predict >= 0):
		return (f"{round(current - predict, 2)}ドル上回")
	elif(current - predict < 0):
		return (f"{round(-(current - predict), 2)}ドル下回")
	else:
		return "変化なし"

# 増減比較
def high_low(current, other):
	if(current - other > 0):
		return 'style="color: red"'
	elif(current - other < 0):
		return 'style="color: blue"'
	else:
		return ''

# マイナス記号を文字列マイナスに変更
def check_plus_minus(i: float):
	if str(i).startswith("-"):
		i: str = str(i).replace("-", "マイナス")
		return i
	else:
		return i
