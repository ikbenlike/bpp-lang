import parser

p = parser.Parser("this + is 'a' thing, \"have\" some")
p.parse()

i = 0
for x in p.tokens:
    print(p.text[x.start:x.end] + " :: " + str(len(p.text[x.start:x.end])))
