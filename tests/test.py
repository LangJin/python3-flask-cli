import re

exp ="^([0-9]+-)*[0-9]+$"
res = re.match(exp,"6232-8323-")
print(res)