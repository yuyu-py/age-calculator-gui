import tkinter as tk
from tkinter import ttk
from datetime import datetime

def perform_age_calculation():
    try:
        # 入力された生年月日を日付オブジェクトに変換
        birth_date = datetime.strptime(birth_date_entry.get(), "%Y-%m-%d")
        # 入力された基準日を日付オブジェクトに変換
        target_date = datetime.strptime(target_date_entry.get(), "%Y-%m-%d")
        
        # 日付の差を計算
        age_difference = target_date - birth_date
        
        # 年数と余りの日数を計算
        years_old = age_difference.days // 365
        remaining_days = age_difference.days % 365
        
        # 結果を表示形式に整理
        age_result_text = f"年齢: {years_old}歳 {remaining_days}日"
        result_display_label.config(text=age_result_text)
        
    except ValueError:
        # 日付形式が正しくない場合のエラーメッセージ
        result_display_label.config(text="日付は YYYY-MM-DD 形式で入力してください")

# メインウィンドウを作成（サイズを調整）
main_window = tk.Tk()
main_window.title("年齢計算システム")
main_window.geometry("400x250")
main_window.resizable(False, False)

# 生年月日入力セクションの作成
birth_date_label = ttk.Label(main_window, text="生年月日 (YYYY-MM-DD):")
birth_date_label.grid(column=0, row=0, padx=15, pady=8, sticky="w")

birth_date_entry = ttk.Entry(main_window, width=20)
birth_date_entry.grid(column=1, row=0, padx=15, pady=8)

# 基準日入力セクションの作成
target_date_label = ttk.Label(main_window, text="基準日 (YYYY-MM-DD):")
target_date_label.grid(column=0, row=1, padx=15, pady=8, sticky="w")

target_date_entry = ttk.Entry(main_window, width=20)
target_date_entry.grid(column=1, row=1, padx=15, pady=8)

# 年齢を計算するボタンを作る（クリック時の動作を設定）
calculate_button = ttk.Button(main_window, text="年齢を計算", command=perform_age_calculation)
calculate_button.grid(column=0, row=2, columnspan=2, pady=15)

# 計算結果を表示するラベルを作る
result_display_label = ttk.Label(main_window, text="")
result_display_label.grid(column=0, row=3, columnspan=2, pady=10)

# 現在日付を取得してデフォルト値として設定
current_date_string = datetime.now().strftime("%Y-%m-%d")
target_date_entry.insert(0, current_date_string)

# GUIアプリケーションの開始
main_window.mainloop()