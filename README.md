# Music_20221026_sa.7z.001/002/003 >> 需要三個一起解壓縮

1. final csv: 最終版csv-after_select_ft_final30s
2. recognition資料夾: 
  - 存放.py程式、DL model
  - __pycache__資料夾: 此為Python解釋器編譯的字節碼, 在主程式 app.py中引用模組，並且執行後自動建立，下一次執行主程式時，Python編譯器會直接載入該模組，省略編譯，藉此來加速載入模組(Module)的速度。
3. static資料夾: 
  - assets: 存放網頁使用的圖片、影片
  - css: css檔
  - js: js檔
  - pca_jpn: 存放使用者PCA圖檔(上傳15分鐘後刪除)
  - musicfile: 收使用者上傳的URL mp4影片、wav、30s wav、3s wav、30s特徵、3s特徵
4. templates: 存放html檔案 
  - about: 團隊介紹頁面
  - analysis: user輸入url頁面
  - index: 首頁
  - result: 分析完成頁面
5. userfile: 存放user url影片、mp4、wav、csv
6. app.py: 執行檔
7. 待修改: 筆記用, 請忽略
8. 補充: 
  - 各.py底下" if __name__ == "__main__"程式: 表示如果直接在該html中跑程式執行才會取用的參數, 供debug用, 否則會從app.py中傳入參數
