t = input('請問你的身高是:')
k = input('請問你的體重是:')
t = float(t)
k = float(k)
g = float(t / 100)
BMI = k / g**2  
if BMI < 18.5:
    input('你好瘦')
elif BMI >=18.5 and BMI < 24 :
    input('還不錯喔')
elif BMI >= 24 and BMI < 27:
    input('有點像工哥')
elif BMI >=27 and BMI <30:
    input('越來越像工哥了')
elif BMI >= 30 and BMI < 35:
    input('你簡直是工哥')
else :
    input('你就是工哥吧')