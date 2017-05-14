import parser

p = parser.Parser("this 1243+1 is 'a' thing, \"have\" some")
p.parse()

i = 0
for x in p.tokens:
    print(p.text[x.start:x.end] + " :: " + str(len(p.text[x.start:x.end])))
