# Web
1. app.py: 執行檔
2. recognition資料夾: 包含所有.py程式、xgboost model(壓縮檔)
3. static資料夾:
  - bootstrap: template, 此處沒有成功套用
  - inalcsv: 資料集3s特徵、30秒特徵(有空值)、30秒特徵(無空值)數據
  - mg: 頁首icon
  - query: template, 此處沒有成功套用
  - musicfile: 收使用者上傳的URL mp4影片、wav、30s wav、3s wav、30s特徵、3s特徵
4. templates: 
  - parts: *下面檔案名稱前都有底線*
      -- nav.html、page_header.html、scripts.html、styles.html: base模板中的不同區域
      -- base.html: 每一個網頁的基礎架構
  - file.html: 使用者輸入url
5. 各.py底下" if __name__ == "__main__"程式: 表示如果直接在該html中跑程式執行才會取用的參數, 供debug用, 否則會從app.py中傳入參數 

