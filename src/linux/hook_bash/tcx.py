from wdf import anyControl
def reset():
    r = anyControl("9999",None,False)
    print("reply:",r)
def scommand(s):
    r = anyControl("9999",s,True)
    print("reply:",r)
