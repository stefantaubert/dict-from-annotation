# dict-from-annotation

[![PyPI](https://img.shields.io/pypi/v/dict-from-annotation.svg)](https://pypi.python.org/pypi/dict-from-annotation)
[![PyPI](https://img.shields.io/pypi/pyversions/dict-from-annotation.svg)](https://pypi.python.org/pypi/dict-from-annotation)
[![MIT](https://img.shields.io/github/license/stefantaubert/dict-from-annotation.svg)](LICENSE)
[![PyPI](https://img.shields.io/pypi/wheel/dict-from-annotation.svg)](https://pypi.python.org/pypi/dict-from-annotation/#files)
![PyPI](https://img.shields.io/pypi/implementation/dict-from-annotation.svg)
[![PyPI](https://img.shields.io/github/commits-since/stefantaubert/dict-from-annotation/latest/main.svg)](https://github.com/stefantaubert/dict-from-annotation/compare/v0.0.2...master)

Command-line interface (CLI) to create pronunciation dictionaries based on manual annotations.

## Installation

```sh
pip install dict-from-annotation --user
```

## Usage

```sh
dict-from-annotation-cli
```

## Example

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

## Dependencies

- `iterable-serialization>=0.0.1`
- `pronunciation_dictionary>=0.0.4`
- `ordered_set>=4.1.0`
- `tqdm`

## License

MIT License

## Acknowledgments

Funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – Project-ID 416228727 – CRC 1410

## Citation

If you want to cite this repo, you can use this BibTeX-entry:

```bibtex
@misc{tsdfa22,
  author = {Taubert, Stefan},
  title = {dict-from-annotation},
  year = {2022},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/stefantaubert/dict-from-annotation}}
}
```
