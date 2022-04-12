# dict-from-annotation

Creates a pronunciation dictionary based on annotations.

```sh
cat > /tmp/test.txt << EOF
Test?
abc,
/X|MM|L/
/X|MM||L/
EOF

pipenv run python -m dict_from_annotation.cli \
  /tmp/test.txt \
  /tmp/test_out.dict
  
cat /tmp/test_out.dict
# Output:
# /X|MM|L/  X MM L

cat /tmp/rest.txt
# Output:
# Test?
# abc,
# /X|MM||L/

```
