import re

pattern = r"\Spam"

if re.match(pattern, "spamspamspam"):
   print("Match")
else:
   print("No match")
