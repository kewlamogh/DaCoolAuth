def to_json(dictionary):
  return str(dictionary).replace("None", "null").replace("True", "true").replace("False", "false")