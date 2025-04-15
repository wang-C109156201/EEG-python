import pandas as pd
import numpy as np

# 讀取 Excel
df = pd.read_excel("腦波數據.xlsx") # 記得換成你自己的檔名

# 可以自己換成你要的欄位
split_columns = [
    'Attention/注意力', 'Relaxation/放松度', 'Delta/δ波', 'Theta/θ波',
    'Low-Alpha/低α波', 'High-Alpha/高α波', 'Low-Beta/低β波', 'High-Beta/高β波',
    'Low-Gamma/低γ波', 'Mid-Gamma/高γ波', 'Appreciation/喜好度',
    'Pitch/俯仰角', 'Yaw/偏航角', 'Roll/滚转角', 'SyncRate/同步率'
]

all_rows = []

for _, row in df.iterrows():
    split_data = {}
    max_len = 0  # 用來找最長的欄位長度，避免有些欄位資料不齊

    for col in split_columns:
        cell = row[col]

        if pd.isna(cell):  # 如果欄位是 NaN
            values = []
        else:
            # 避開非整數的錯誤項
            try:
                values = [int(x.strip()) for x in str(cell).split(',') if x.strip().isdigit()]
            except ValueError:
                values = []

        split_data[col] = values
        max_len = max(max_len, len(values))

    # 填寫每一秒的資料
    for sec in range(max_len):
        one_row = {'秒數': sec + 1}
        for col in split_columns:
            # 如果某欄在這個秒數沒有資料，就填空或 0
            one_row[col] = split_data[col][sec] if sec < len(split_data[col]) else np.nan
        all_rows.append(one_row)

# 建立 DataFrame 並儲存
result_df = pd.DataFrame(all_rows)
result_df.to_excel("轉換後的資料.xlsx", index=False)

print("轉換完成 ✅")
