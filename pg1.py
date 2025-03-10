from googletrans import Translator

# Initialize Translator
translator = Translator()
def translate_text(text, dest_language):
    translated = translator.translate(text, dest=dest_language)
    return translated.text

text = input("Enter text to translate: ")
lang = input("Enter target language code (e.g., 'fr' for French): ")

translated_text = translate_text(text, lang)
print(f"Translated Text: {translated_text}")


from flask import Flask, request, render_template
from googletrans import Translator

app = Flask(_name_)
translator = Translator()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form["text"]
        lang = request.form["lang"]
        translated_text = translator.translate(text, dest=lang).text
        return render_template("index.html", text=text, translated=translated_text, lang=lang)
    return render_template("index.html")

if _name_ == "_main_":
    app.run(debug=True)
    from googletrans import Translator

# Initialize Translator
translator=translator()
def translate_text(text,dest_language):
def translate_text(text, dest_language):
    translated = translator.translate(text, dest=dest_language)
    return translated.text
    text = input("Enter text to translate: ")
lang = input("Enter target language code (e.g., 'fr' for French): ")

translated_text = translate_text(text, lang)
print(f"Translated Text: {translated_text}")
from flask import Flask, request, render_template
from googletrans import Translator

app = Flask(_name_)
translator = Translator()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form["text"]
        lang = request.form["lang"]
        translated_text = translator.translate(text, dest=lang).text
        return render_template("index.html", text=text, translated=translated_text, lang=lang)
    return render_template("index.html")

if _name_ == "_main_":
    app.run(debug=True)
