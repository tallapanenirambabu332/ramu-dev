from ruamel.yaml import YAML
def parseYaml():
  yaml = YAML()
  input_file = 'repos.yml'
  repos_list = []
  i = 0
  for key, value in yaml.load(open(input_file)).items():
    print(str(value))
    i+=1
    repos_list.insert(i,value)
    print(repos_list)
    return repos_list
repositories = parseYaml()
print(repositories)
