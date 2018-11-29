import re
import os
import mimetypes
from wsgiref.util import FileWrapper
from django.http import StreamingHttpResponse

def file_iterator(file_name, chunk_size=8192, offset=0, length=None):
  with open(file_name, "rb") as f:
    f.seek(offset, os.SEEK_SET)
    remaining = length
    while True:
      bytes_length = chunk_size if remaining is None else min(remaining, chunk_size)
      data = f.read(bytes_length)
      if not data:
        break
      if remaining:
        remaining -= len(data)
      yield data

def stream_video(request, path):   # path视频路径
  """将视频文件以流媒体的方式响应"""
  range_header = request.META.get('HTTP_RANGE', '').strip()
  range_re = re.compile(r'bytes\s*=\s*(\d+)\s*-\s*(\d*)', re.I)
  range_match = range_re.match(range_header)
  size = os.path.getsize(path)
  content_type, encoding = mimetypes.guess_type(path)  # 根据由url给出的文件名或URL猜测文件的类型。返回值是一个元组(type, encoding)
  content_type = content_type or 'application/octet-stream'
  if range_match:
    first_byte, last_byte = range_match.groups()
    first_byte = int(first_byte) if first_byte else 0
    last_byte = first_byte + 1024 * 1024 * 8    # 8M 每片,响应体最大体积
    if last_byte >= size:
      last_byte = size - 1
    length = last_byte - first_byte + 1
    resp = StreamingHttpResponse(file_iterator(path, offset=first_byte, length=length), status=206, content_type=content_type)
    resp['Content-Length'] = str(length)
    resp['Content-Range'] = 'bytes %s-%s/%s' % (first_byte, last_byte, size)
    # print(111)  通过打印可以看到走的是视频流
  else:
    # 不是以视频流方式的获取时，以生成器方式返回整个文件，节省内存
    resp = StreamingHttpResponse(FileWrapper(open(path, 'rb')), content_type=content_type)
    resp['Content-Length'] = str(size)
    # print(2222)
  resp['Accept-Ranges'] = 'bytes'
  return resp
