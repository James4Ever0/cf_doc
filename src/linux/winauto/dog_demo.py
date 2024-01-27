from dogtail import tree

root=tree.root

def walker(a):
    a.childrenLimit = 1000
    for x in a.children:
        print(x,type(x))
#        x.dump()
        try:
            x.typeText("random string")
        except:
            print("unable to type")
        try:
            print(x.get_process_id())
        except:
            print("error id here")
        try:
            print(x.get_text())
        except:
            print("error text here")
#        if len(a.children)!=0:
        for y in x.children:
            walker(y)

#        print(dir(x))
#lisx=[]
walker(root)
"""
for x in root.children:
    for y in x.children:
        walker(y)
"""
