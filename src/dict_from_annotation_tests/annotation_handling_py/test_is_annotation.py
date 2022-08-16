from dict_from_annotation.annotation_handling import is_annotation


def test_empty_X__is_false():
  result = is_annotation("", "X")
  assert not result
