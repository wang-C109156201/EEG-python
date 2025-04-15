# EEG-python

## 功能說明
- `EEG_second.py` 從原始腦波數據 Excel 檔案中拆解每一欄的資料為獨立的每秒紀錄。整合所有欄位為統一格式，輸出為新的 Excel 檔案。
- `EEG_case.py` 是根據時間序列先檢查是否有連續至少 20 秒的穩定數據，並將對應的腦波指標資料提取 6 段影片數據出來並儲存成新的 Excel。(這裡的"六段影片數據"是因為我的專案需要才加進去，如果你不需要把專案分段檔案，可以把程式碼註解掉。)
- code 對應輸出 Excel 檔示意圖在 `EGG_second output excel preview.png` 跟 `EGG_case output excel preview.png`

## 使用方式
1. 安裝必要的 Python 套件（第一次執行才需要）：

   ```bash
   pip install pandas openpyxl numpy
   ```

2. 複製 `EEG_second.py` 或是 `EEG_case.py` 中的程式碼後執行。

## 注意事項
- 你需要有一個可以執行 Python 的開發環境（IDE），例如 [Visual Studio Code](https://code.visualstudio.com/)、PyCharm 或 Jupyter Notebook。  
   - 如果你沒有這類開發環境或是執行 Python 的經驗，並想嘗試在你的電腦上安裝 Python 環境，可以參考以下文章或是自己上網蒐關鍵字：

     - [Windows 使用者](https://ithelp.ithome.com.tw/articles/10212365) (個人淺見:只需要做到"新增檔案settings.json"前就好)
     - [macOS 使用者](https://www.youtube.com/watch?v=MpPne7NT_HI)

   - 如果你覺得這些步驟太麻煩，其實也可以直接把檔案給我，我可以幫你處理XD
- Excel 中的資料欄位**格式必須設為「文字」**，不要選擇數字，否則資料會被自動格式化喔～
---
