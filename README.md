# QZSS L6 Downloader GUI Tools

このリポジトリには、日本の準天頂衛星システム（QZSS）が提供するL6信号の航法データのアーカイブをダウンロードするための、2種類のGUIアプリケーション（Windows用実行ファイル）が含まれています：

- **L6D Downloader**: QZSS L6D（CLAS）データを日付範囲指定で取得  
- **L6E Downloader**: QZSS L6E（MADOCA）データを衛星ごと・日付範囲指定で取得

## 📦 ダウンロードファイル

- `l6d_downloader.exe`
- `l6e_downloader.exe`

（※ `.py` ファイルからexe化されています）

---

## 🖥 L6D Downloader の使い方

1. `l6d_downloader.exe` を実行  
2. 開いたウィンドウで以下を入力：
   - 取得したい開始日・終了日（YYYY-MM-DD形式）
   - 保存先のフォルダ
3. `Start Download` をクリック  
4. 指定された期間の `.l6` ファイル（L6Dデータ）が1日ごとに1ファイル出力されます

---

## 🛰 L6E Downloader の使い方

1. `l6e_downloader.exe` を実行  
2. 以下の項目を入力または選択：
   - 対象の衛星（例：J07）
   - 取得したい開始日・終了日（YYYY-MM-DD形式）
   - 保存先のフォルダ
3. `Start Download` をクリック  
4. 指定衛星のPRNに対応した `.l6` ファイルが出力されます（1日ごと）

---

## 💡 補足

ダウンロード元URL:
  - L6D: https://sys.qzss.go.jp/archives/l6/
  - L6E: https://l6msg.go.gnss.go.jp/archives/

.pyファイルはCUI版です。URL変更等によるバグ対応やLinux,MacOS等で利用してください。
