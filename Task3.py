import nltk
import matplotlib.pyplot as plt
import string
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords

# Розкоментувати при першому запуску:
# nltk.download('punkt')
# nltk.download('punkt_tab') # Іноді потрібен для новіших версій NLTK
# nltk.download('stopwords')

# Зчитування файлу
with open('caroll-alice.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Токенізація
tokens = word_tokenize(text)
total_words = len(tokens)
print(f"Кількість токенів у тексті: {total_words}\n")

# Аналіз сирого тексту
fdist_raw = FreqDist(tokens)
top_10_raw = fdist_raw.most_common(10)
print("10 найчастіших токенів:")
for word, count in top_10_raw:
    print(f"{word}: {count}")

# Побудова першої діаграми
words_raw, counts_raw = zip(*top_10_raw)
plt.figure(figsize=(10, 6))
plt.bar(words_raw, counts_raw, color='skyblue')
plt.title("10 найчастіших токенів")
plt.xlabel("Слово або символ")
plt.ylabel("Кількість")
plt.show()

# Список непотрібних стоп-слів, пунктуації, специфічних символів
stop_words = set(stopwords.words('english'))
custom_punctuation = set(string.punctuation)
custom_punctuation.update(['“', '”', '’', '‘', '—', '...'])

# Виділення змістовних слів
clean_tokens = []
for word in tokens:
    word_lower = word.lower()
    if (word_lower not in stop_words and word_lower not in custom_punctuation and word_lower.isalpha()):
        clean_tokens.append(word_lower)
fdist_clean = FreqDist(clean_tokens)
top_10_clean = fdist_clean.most_common(10)
print("\n10 найчастіших змістовних слів:")
for word, count in top_10_clean:
    print(f"{word}: {count}")

# Побудова другої діаграми
words_clean, counts_clean = zip(*top_10_clean)
plt.figure(figsize=(10, 6))
plt.bar(words_clean, counts_clean, color='lightgreen')
plt.title("10 найчастіших змістовних слів")
plt.xlabel("Слово")
plt.ylabel("Кількість")
plt.show()