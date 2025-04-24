class Test:
    def thisisatest(me, you):
        print(f"called with {you}")

test = Test()

test_val = 1

if test_val != 1:
    test.thisisatest(False)
elif test_val == 1:
    test.thisisatest(True)

x = 5
y = 4

if test_val > 0:
    print(x * y)
