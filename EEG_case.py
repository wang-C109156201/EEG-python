import pandas as pd

# 根據時間欄位中的整數序列，找出相鄰時間差距不超過 2 且連續長度 ≥ 20 的段落。
def find_continuous_segments(time_list, min_len=20):
    segments = []
    current_segment = [time_list[0]]

    for i in range(1, len(time_list)):
        if time_list[i] - time_list[i - 1] <= 2:
            current_segment.append(time_list[i])
        else:
            if len(current_segment) >= min_len:
                segments.append(current_segment)
            current_segment = [time_list[i]]

    if len(current_segment) >= min_len:
        segments.append(current_segment)

    return segments

# 讀取 Excel 並強制所有欄位為字串
df = pd.read_excel("腦波數據.xlsx", dtype=str)# 記得改成自己的檔名

data_columns = [
    'Attention/注意力', 'Relaxation/放松度', 'Delta/δ波', 'Theta/θ波',
    'Low-Alpha/低α波', 'High-Alpha/高α波', 'Low-Beta/低β波', 'High-Beta/高β波',
    'Low-Gamma/低γ波', 'Mid-Gamma/高γ波', 'Appreciation/喜好度',
    'Pitch/俯仰角', 'Yaw/偏航角', 'Roll/滚转角', 'SyncRate/同步率'
]

results = []

for _, row in df.iterrows():
    # 處理時間欄位 → 整數列表（僅此欄轉 int）
    time_raw = str(row['Time-set/时间集合']).split(',')
    time_list = [int(t.strip()) for t in time_raw if t.strip().isdigit()]

    segments = find_continuous_segments(time_list, min_len=20)

    # 若找不到足夠的連續區段（至少6段），跳過此筆資料
    if len(segments) < 6:
        print("⚠️ 無法切出六段有效影片資料！")
        continue

    # 將每欄字串用逗號切開，保留原樣數字（不轉 int）
    parsed_data = {
        col: [x.strip() for x in str(row[col]).split(',')]
        for col in data_columns
    }

     # 只取前六段區段，逐段儲存到 results 中
    for i, segment in enumerate(segments[:6]):
        indices = [time_list.index(t) for t in segment if t in time_list]

        row_result = {'影片': i + 1} # 可以改成你要欄位名稱
        for col in data_columns:
            values = [parsed_data[col][j] for j in indices if j < len(parsed_data[col])]
            row_result[col] = ",".join(values)
        results.append(row_result)

# 輸出結果（數值以純字串方式儲存）
result_df = pd.DataFrame(results)
result_df.to_excel("分段結果.xlsx", index=False)
print("輸出成功✅")
