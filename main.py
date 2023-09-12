import lark

my_grammar = '''
start: mixed_string | a_string | b_string
a_string: A | A a_string 
b_string: B | B b_string 
mixed_string: a_string CHAR | b_string CHAR 
A: "a" | "A"
B: "b" | "B"
CHAR: "a".."z" | "B".."Z"
'''

parser = lark.Lark(my_grammar, ambiguity="explicit")

tree = parser.parse('aaaaaaAZ')

print(tree.pretty())

