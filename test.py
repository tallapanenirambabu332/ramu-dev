import yaml
with open('repos.yml', 'r') as f:
   doc = yaml.load(f)
print(doc)
for repo_name in doc[‘repos’]:   
   name = doc[‘repos’][repo_name]
   print(name) 
