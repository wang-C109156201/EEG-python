# EEG-python

## 功能說明
- 從原始腦波數據 Excel 檔案中拆解每一欄的資料為獨立的每秒紀錄。
- 整合所有欄位為統一格式，輸出為新的 Excel 檔案。
- 輸出 Excel 檔示意圖在 `output excel preview.png`

## 使用方式
1. 安裝必要的 Python 套件（第一次執行才需要）：

   ```bash
   pip install pandas openpyxl numpy
   ```

2. 複製 `EEG.py` 中的程式碼後執行。

## 注意事項
- 你需要有一個可以執行 Python 的開發環境（IDE），例如 [Visual Studio Code](https://code.visualstudio.com/)、PyCharm 或 Jupyter Notebook。  
   - 如果你沒有這類開發環境或是執行 Python 的經驗，並想嘗試在你的電腦上安裝 Python 環境，可以參考以下文章或是自己上網蒐關鍵字：

     - [Windows 使用者](https://ithelp.ithome.com.tw/articles/10212365) (個人淺見:只需要做到"新增檔案settings.json"前就好)
     - [macOS 使用者](https://www.youtube.com/watch?v=MpPne7NT_HI)

   - 如果你覺得這些步驟太麻煩，其實也可以直接把檔案給我，我可以幫你處理XD
- Excel 中的資料欄位**格式必須設為「文字」**，不要選擇數字，否則資料會被自動格式化喔～
---
