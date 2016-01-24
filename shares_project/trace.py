import traceback

try:
    a = 1/0
# except Exception, e:
#     print e
except:
    print traceback.print_exc()