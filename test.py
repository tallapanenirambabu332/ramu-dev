import yaml
with open('repos.yml', 'r') as f:
   doc = yaml.load(f)
print(doc)
print(doc.repo1)
#txt = doc[“repo1”]
#print(txt)
