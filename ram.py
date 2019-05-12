from ruamel.yaml import YAML
yaml = YAML()
input_file = 'repos.yml'
for key, value in yaml.load(open(input_file)).items():
  print(str(value))
