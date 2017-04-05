import os
import time
import random
from django.core.files.storage import FileSystemStorage


class ImageStorage(FileSystemStorage):
    def save(self, name, content, max_length=None):
        # 文件拓展名
        ext = os.path.splitext(name)[1]
        # 文件目录
        d = os.path.dirname(name)
        # 自定义文件名，年月日时分秒随机数
        current_time = time.strftime('%Y%m%d-%H%M%S-')
        fn = current_time + '%d' % random.randint(0, 100)
        # 合成文件名
        name = os.path.join(d, fn + ext)
        return super(ImageStorage, self).save(name, content)

    def delete(self, name):
        if os.path.basename(name) == 'default.png' or \
                os.path.basename(name) == 'default_male.png' or \
                os.path.basename(name) == 'default_female.png':
            pass
        else:
            if os.path.exists(self.path(name)):
                os.remove(self.path(name))
