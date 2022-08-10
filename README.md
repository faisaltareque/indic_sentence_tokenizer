# Indic Sentence Tokenizer

This repo reduced from [indic_nlp_library](https://github.com/anoopkunchukuttan/indic_nlp_library) to be olny used for indic sentence tokenize.
  

## Setup from Clone
```bash
python setup.py bdist_wheel
pip install -e .
```

## Setup from Git
```bash
pip install git+https://github.com/faisaltareque/multi_lingual_rouge_BPE_tokenizer
```


* **Default usage**


```python
from indic_sentence_tokenizer import sentence_tokenize
sentences = sentence_tokenize.sentence_split('''ਪਰ ਦੋਵੇਂ ਭਾਈਚਾਰਿਆਂ ਵਿਚਕਾਰ ਤਰੇੜ ਪਹਿਲਾਂ ਤੋਂ ਜ਼ਿਆਦਾ ਗਹਿਰੀ ਹੁੰਦੀ ਦਿਖ ਰਹੀ ਹੈ, ਜਿਸ ਦੇ ਪਿੱਛੇ ਰੋਜ਼-ਰੋਜ਼ ਉਛਾਲੇ ਜਾਣ ਵਾਲੇ ਅਜਿਹੇ ਮੁੱਦੇ ਹਨ ਜਿਨ੍ਹਾਂ ਦਾ ਸਿੱਧਾ ਸਬੰਧ ਦੇਸ਼ ਦੇ ਮੁਸਲਮਾਨਾਂ ਨਾਲ ਹੈ। ਇੱਥੇ ਅਸੀਂ ਉਨ੍ਹਾਂ ਮੁੱਦਿਆਂ 'ਤੇ ਨਜ਼ਰ ਮਾਰ ਰਹੇ ਹਾਂ ਜੋ ਦਰਾੜ ਨੂੰ ਭਰਨ ਦੀ ਜਗ੍ਹਾ ਉਸ ਨੂੰ ਹੋਰ ਗਹਿਰਾ ਕਰਦੇ ਜਾ ਰਹੇ ਹਨ। ਅਜਿਹਾ ਨਹੀਂ ਹੈ ਕਿ ਇਹ ਸਾਰੇ ਬਿਆਨ ਕੇਵਲ ਸਿਆਸੀ ਤਬਕੇ ਤੋਂ ਆ ਰਹੇ ਹਨ, ਬਲਕਿ ਸਮਾਜ ਦੇ ਹਰ ਹਿੱਸੇ ਵਿੱਚੋਂ ਆ ਰਹੇ ਹਨ। ਸੋਸ਼ਲ ਮੀਡੀਆ 'ਤੇ, ਪਾਰਟੀਆਂ ਦੇ ਬੁਲਾਰਿਆਂ ਤੋਂ ਲੈ ਕੇ ਵੱਟਸਐਪ ਗਰੁੱਪ ਦੇ ਰਿਸ਼ਤੇਦਾਰਾਂ ਵਿਚਕਾਰ ਹਿੰਦੂ-ਮੁਸਲਮਾਨ ਤਕਰਾਰ ਨਾਲ ਜੁੜੇ ਮੁੱਦਿਆਂ 'ਤੇ ਬਹਿਸ ਅਤੇ ਵਿਵਾਦ ਲਗਾਤਾਰ ਜਾਰੀ ਹੈ। ਕਦੇ ਧਰਮ-ਸੰਸਦ ਦੇ ਨਾਮ 'ਤੇ, ਤਾਂ ਕਦੇ ਭੜਕਾਊ ਭਾਸ਼ਣ ਦੇ ਕੇ, ਕਦੇ ਮਾਸ ਦੀਆਂ ਦੁਕਾਨਾਂ ਨੂੰ ਲੈ ਕੇ, ਕਦੇ ਪਾਰਕ-ਮਾਲ ਵਿੱਚ ਨਮਾਜ਼ ਪੜ੍ਹਨ ਨੂੰ ਲੈ ਕੇ।''', lang='pa', delim_pat='auto')
#text (str): text to split into sentence
#lang (str): ISO 639-2 language code
#delim_pat (str): regular expression to identify sentence delimiter characters. If set to 'auto', the delimiter pattern is chosen automatically based on the language and text.
```
