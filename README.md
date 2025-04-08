# QZSS L6 Downloader GUI Tools
Each section is written in the order: Japanese → English.

このリポジトリには、日本の準天頂衛星システム（QZSS）が提供するL6信号の航法データのアーカイブをダウンロードするための、2種類のGUIアプリケーション（Windows用実行ファイル）が含まれています：  
**L6D Downloader**: QZSS L6D（CLAS）データを日付範囲指定で取得  
**L6E Downloader**: QZSS L6E（MADOCA）データを衛星ごと・日付範囲指定で取得 

This repository contains two types of GUI applications (Windows executables) for downloading navigation data archives from the Quasi-Zenith Satellite System (QZSS) L6 signals provided by Japan:  
**L6D Downloader**: Downloads QZSS L6D (CLAS) data by specifying a date range  
**L6E Downloader**: Downloads QZSS L6E (MADOCA) data by specifying a satellite and date range  

---

📦 **ダウンロードファイル**  
- `l6d_downloader.exe`  
- `l6e_downloader.exe`  
（※ .py ファイルからexe化されています）  
📦 **Downloadable Files**  
- `l6d_downloader.exe`  
- `l6e_downloader.exe`  
(*These are converted from .py files into .exe executables*)  

---

## 🖥 L6D Downloader の使い方  
1. `l6d_downloader.exe` を実行  
2. 開いたウィンドウで以下を入力：  
　・取得したい開始日・終了日（YYYY-MM-DD形式）  
　・保存先のフォルダ  
3. **Start Download** をクリック  
4. 指定された期間の `.l6` ファイル（L6Dデータ）が1日ごとに1ファイル出力されます  
## 🖥 How to Use L6D Downloader  
1. Run `l6d_downloader.exe`  
2. In the window that opens, enter:  
　・Start date and end date (in `YYYY-MM-DD` format)  
　・Destination folder to save the files  
3. Click **Start Download**  
4. A `.l6` file (L6D data) will be downloaded for each day in the specified date range  

---

## 🛰 L6E Downloader の使い方  
1. `l6e_downloader.exe` を実行  
2. 以下の項目を入力または選択：  
　・対象の衛星（例：J07）  
　・取得したい開始日・終了日（YYYY-MM-DD形式）  
　・保存先のフォルダ  
3. **Start Download** をクリック  
4. 指定衛星のPRNに対応した `.l6` ファイルが出力されます（1日ごと）  
## 🛰 How to Use L6E Downloader  
1. Run `l6e_downloader.exe`  
2. Enter or select the following:  
　・Target satellite (e.g., `J07`)  
　・Start date and end date (in `YYYY-MM-DD` format)  
　・Destination folder to save the files  
3. Click **Start Download**  
4. A `.l6` file corresponding to the selected satellite’s PRN will be downloaded for each day  

---

## 💡 補足  
**ダウンロード元URL:**  
- L6D: https://sys.qzss.go.jp/dod/archives/clas.html （https://sys.qzss.go.jp/archives/l6/）  
- L6E: https://l6msg.go.gnss.go.jp/ （https://l6msg.go.gnss.go.jp/archives/）  
## 💡 Additional Information  
**Download URLs:**  
- L6D: https://sys.qzss.go.jp/dod/archives/clas.html (https://sys.qzss.go.jp/archives/l6/)  
- L6E: https://l6msg.go.gnss.go.jp/ (https://l6msg.go.gnss.go.jp/archives/)  

`.py` ファイルは CUI 版です。URL 変更等によるバグ修正や Linux・macOS 等で利用してください。  
The original `.py` files are command-line interface (CUI) versions. Please use them on Linux/macOS or when fixing issues such as URL changes.
