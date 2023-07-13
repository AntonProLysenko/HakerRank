def matchingStrings(strings, queries):
    out = []

    for i in queries:
        if i in strings:
            out.append(strings.count(i))
        else:
            out.append(0)
    return out






string=["aba","baba","aba","xzxb"]
querie = ["aba","xzxb","ab"]

print(matchingStrings(string,querie))
