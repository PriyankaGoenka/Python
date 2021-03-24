def decorator_f(func):
    def inner():
        x="ConsultantAdd Training"
        print(x[::-1])
        return func
    return inner

def revs():
    print("The reveres string is printed.")

rev=decorator_f(revs)
rev()