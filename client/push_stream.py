import subprocess
cmd = 'ffmpeg -f dshow -i video="EasyCamera":audio="麦克风 (Realtek High Definition Audio)" -vcodec libx264  -tune:v zerolatency -f flv rtmp://59.110.140.100:1935/live/123'
# 上面的123是一个推流和拉流的id,当推流是地址是123时,拉流地址也是123;推流地址是456,拉流地址也是456;可以通过设置id来开启多个直播
p = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
p.wait()

