# Pythonのヒアドキュメント

## 書き方

### ヒアドキュメント内にインデントあり

```python
"""
  タイトル: ヒアドキュメント1

  メッセージ:
    1行目
    2行目
"""
```

### ヒアドキュメント内にインデントなし

```python
"""
タイトル: ヒアドキュメント2

メッセージ:
  1行目
  2行目
"""
```

### ヒアドキュメントの開始終了と同じ行から開始終了する

```python
"""タイトル: ヒアドキュメント3

メッセージ:
  1行目
  2行目"""
```

## 問題点

1. ヒアドキュメントのインデント開始位置がファイルの先頭になる
2. ヒアドキュメントの開始終了行にも改行が含まれる

## 対応方法

1. `textwrap.dedent(text)`を使用して、共通的に存在する先頭の空白を削除する
2. `string.strip()`を使用して、文字列の先頭および末尾部分の文字を除去する

## 結論

```python
import textwrap

def create_message():
    return textwrap.dedent(
      """
        タイトル: ヒアドキュメント1

        メッセージ:
          1行目
          2行目
      """
    ).strip()
```

## 参考資料

- [textwrap.dedent](https://docs.python.org/ja/3.12/library/textwrap.html#textwrap.dedent)
- [str.strip()](https://docs.python.org/ja/3.12/library/stdtypes.html#str.strip)
