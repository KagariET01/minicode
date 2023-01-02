Vp=float(input("請輸入P波速率(m/s):"))     #設Vp為P波速率
Vs=float(input("請輸入S波速率(m/s):"))     #設Vs為S波速率
Tp=float(input("請輸入P波到達時間(s):"))   #設Tp為P波到達時間
Ts=float(input("請輸入S波到達時間(s):"))   #設Ts為S波到達時間
#設T0為震央發生地震的時間
#設ans為測站和震央距離
#Tp-T0=ans*(1/Vp)---1---P波到達時間
#Ts-T0=ans*(1/Vs)---2---S波到達時間
#由1,2兩式可得
#Tp-Ts=ans*(1/Vp)-ans*(1/Vs)=ans*(1/Vp-1/Vs)
#(Tp-Ts)/(1/Vp-1/Vs)=ans
ans=(Tp-Ts)/(1/Vp-1/Vs)                   #計算ans
print("震央距離此測站",ans,"公尺")
print("made by ET01(蔡奕章)")
#made by ET01