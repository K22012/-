import random

# 壱の句リスト（誰が・何が）
first_phrases = [
    # "ファッションデザイナーが",
    # "妹が",
    # "ガチャで",
    # "コンタクトレンズ",
    # "先輩が",
]

# 弐の句リスト（何を・どうして）
second_phrases = [
    # "めがねってぇなんかぁださくね？",
    # "こんなに可愛い",
    # "眼鏡が",
    # "アイドルとして",
    # "乗ると",
]

# 参の句リスト（なぜか・だから）
third_phrases = [
    # "と言ったから。",
    # "わけがないから。",
    # "出ないから。",
    # "嫌いだから。",
    # "使えないから。",
]

# ランダムに理由を生成
def generate_reason():
    if not first_phrases or not second_phrases or not third_phrases:
        return "⚠ 壱の句・弐の句・参の句のいずれかが空です。句を追加してください。"
    
    first = random.choice(first_phrases)
    second = random.choice(second_phrases)
    third = random.choice(third_phrases)
    return f"{first} {second} {third}"

# 実行して表示（複数回出力したいときは rangeの数字を増やす）
for i in range(1):
    print(f"ランダム理由: {generate_reason()}")
