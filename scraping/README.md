# fetch the delay of the train

## 概要
　[yahoo路線の運行状況](https://transit.yahoo.co.jp/diainfo)をスクレイピングして任意の路線の遅延状況を取得する。

## 環境
- wsl2 on ubuntu20.04
- python 3.10.2

## 環境構築手順
1. python仮想環境の作成※pipをまとめるため
  ```bash
    python -m venv smart-speaker
  ```
2. 仮想環境に入る
  ```bash
    . smart-speaker/bin/activate
  ```
3. ライブラリのインストール
  ```bash
    pip install requests beautifulsoup4
  ```
4. (作業終了時)仮想環境を終了する
   ```bash
    deactivate
   ```

## 参考
- [yahoo路線の運行情報を取得したい
](https://qiita.com/hirohiroto522/items/6ff29be1344be805ecb0)