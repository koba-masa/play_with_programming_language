def here_document1
  <<~EOS
    タイトル: ヒアドキュメント1

    メッセージ:
      1行目
      2行目
  EOS
end

def here_document2
  <<~EOS
  タイトル: ヒアドキュメント2

  メッセージ:
    1行目
    2行目
  EOS
end

puts here_document1
puts '---'
puts here_document2
