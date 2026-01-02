#exception handling
#exception1
try:
    a=10
    b=0
    print(a/b)

except(ZeroDivisionError):
    print("Zero Division Error Exception...")
except Exception:
    print("This is exception block")
#finally:
print("Hello World")