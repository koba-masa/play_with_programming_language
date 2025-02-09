import textwrap

def here_document1():
    doc = """
      タイトル: ヒアドキュメント1

      メッセージ:
        1行目
        2行目
    """

    return doc

def here_document2():
    doc = """
    タイトル: ヒアドキュメント2

    メッセージ:
      1行目
      2行目
    """

    return doc

def here_document3():
    doc = """タイトル: ヒアドキュメント3

    メッセージ:
      1行目
      2行目"""

    return doc

print(here_document1())
print('---')
print(here_document2())
print('---')
print(here_document3())

print('')
print('=== textwrap.dedent ========================')

print(textwrap.dedent(here_document1()))
print('---')
print(textwrap.dedent(here_document2()))
print('---')
print(textwrap.dedent(here_document3()))

print('')
print('=== textwrap.dedent & strip() ========================')

print(textwrap.dedent(here_document1()).strip())
print('---')
print(textwrap.dedent(here_document2()).strip())
print('---')
print(textwrap.dedent(here_document3()).strip())
