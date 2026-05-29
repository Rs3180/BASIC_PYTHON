def remove_and_split(string, word):
          newstr = string.replace(word, "")
          return newstr.strip()

this = "     Harry is a good      "
n = remove_and_split(this, "Harry")
print(n)
# print(this)
# print(this.strip())