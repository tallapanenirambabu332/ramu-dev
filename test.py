import yaml
with open(‘repos_yaml', 'r') as f:
   doc = yaml.load(f)
print doc 
txt = doc[“repo1”]
print txt
