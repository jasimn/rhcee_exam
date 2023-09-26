def named(**kwargs):
        print(kwargs)

def nice_value(**kwargs):
        named(**kwargs)
        for arg,value in kwargs.items():
                print(f"{arg}:{value}")

nice_value(name="bob",age=34)
              