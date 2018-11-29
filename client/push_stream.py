import subprocess
cmd = 'ffmpeg -f dshow -i video="EasyCamera":audio="麦克风 (Realtek High Definition Audio)" -vcodec libx264  -tune:v zerolatency -f flv rtmp://59.110.140.100:1935/live/123'
p = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
p.wait()

