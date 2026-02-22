def reverse_string(text):
    for i in range(len(text)-1,-1,-1):
        yield text[i]
for ch in reverse_string("PYTHON"):
    print(ch)