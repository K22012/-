# 🧾 README

## プロジェクト名  
**三段論法風 ランダム理由ジェネレーター**

## 概要  
このPythonスクリプトは、三段階の句（壱の句、弐の句、参の句）から構成される“理由”をランダムに生成する簡易ツールです。句を自由に追加・編集することで、面白い・ユニークな理由文を作ることができます。

## 特徴
- 三段構成（誰が・何を・なぜ）による文章生成
- 任意の句リストに基づいたランダム生成
- 複数回出力も簡単に変更可能
- 空リストへの対策も実装済み

## ファイル構成
- `reason_generator.py`（例: `55ca1c0c-fa0f-4f71-b74b-e772d2c0a513.py`）: メインスクリプト

## 使用方法

1. Python 3 をインストールしておく。
2. スクリプト内の以下のリストに自由にフレーズを追加：

```python
first_phrases = [ "妹が", "先輩が", ... ]      # 壱の句（主語）
second_phrases = [ "眼鏡が", "こんなに可愛い", ... ]  # 弐の句（述語）
third_phrases = [ "嫌いだから。", "出ないから。", ... ]  # 参の句（理由）
```

3. ターミナルで実行：

```bash
python reason_generator.py
```

4. 実行結果例：

```
ランダム理由: 妹が こんなに可愛い 嫌いだから。
```

## 注意
- リストが1つでも空だと理由を生成できません。エラーメッセージが表示されます。
- `range(1)` の数字を変更することで複数の理由を一度に生成可能です。
