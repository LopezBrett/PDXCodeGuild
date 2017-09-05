import datetime
# start time
sta_tim_var=f"{datetime.time.now():0-0-0}"
# decorator
class my_decorator(object):

    def __init__(self, f):
        print("inside my_decorator.__init__()")
        f() # Prove that function definition has completed

    def __call__(self):
        print("inside my_decorator.__call__()")

@my_decorator
def aFunction():
    print("inside aFunction()")

print("Finished decorating aFunction()")

aFunction()
# end time
end_tim_var=f"{datetime.time.now():0-0-0}"
# calculate time
print(sta_tim_var)
print(end_tim_var)
#cal_tim_var= sta_tim_var - end_tim_var