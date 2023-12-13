import emoji
# не думал что есть даже такая библиотека
# добавление эмодзи к строке
text = "Hello, World!"
emoji_text = emoji.emojize(":thumbs_up: " + text + " :thumbs_up:")
print(emoji_text)

