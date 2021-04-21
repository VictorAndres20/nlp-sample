from bs4 import BeautifulSoup
import urllib.request
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
from src.utils.frequency import build_freq
import seaborn as sns


def get_data():
    # Obtener HTML de la web
    # https://librefinanciero.com
    url = "https://librefinanciero.com"
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, "html5lib")
    text = soup.get_text(strip=True)
    return text


def build_tokens(text):
    tokens = word_tokenize(text, "spanish")

    # Remove punctuation marks
    tokens = [word.lower() for word in tokens if word.isalpha()]
    return tokens


def plot_freq(freq):
    # sns.set()
    # freq.plot(30, cumulative=False)
    plt.hist(freq)
    plt.savefig("f.png")


def tokenize():
    text = get_data()
    tokens = build_tokens(text)
    freq = build_freq(tokens)
    # plot_freq(freq)
    return tokens
