# dict-from-annotation

[![PyPI](https://img.shields.io/pypi/v/dict-from-annotation.svg)](https://pypi.python.org/pypi/dict-from-annotation)
[![PyPI](https://img.shields.io/pypi/pyversions/dict-from-annotation.svg)](https://pypi.python.org/pypi/dict-from-annotation)
[![MIT](https://img.shields.io/github/license/stefantaubert/dict-from-annotation.svg)](LICENSE)

Command-line interface to create pronunciation dictionaries based on manual annotations.

## Installation

```sh
pip install dict-from-annotation
```

## Usage

```sh
# Create example vocabulary
cat > /tmp/vocabulary.txt << EOF
Test?
abc,
/X|MM|L/
/X|MM||L/
EOF

dict-from-annotation-cli \
  /tmp/vocabulary.txt \
  /tmp/dictionary.dict \
  --rest-out /tmp/rest_vocabulary.txt

cat /tmp/dictionary.dict
# -------
# Output:
# -------
# /X|MM|L/  X MM L
# -------

cat /tmp/rest_vocabulary.txt
# -------
# Output:
# -------
# Test?
# abc,
# /X|MM||L/
# -------
```
