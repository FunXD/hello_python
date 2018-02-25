""" make stdout environment cp494 to utf-8 [WINDOWS-7]
  1.BEFORE: 안녕세계 = �ȳ缼��
    - sys.getdefaultencoding() = utf-8
    - sys.stdout.encoding = cp949        ---> change to 'utf-8'

  2.AFTER: 안녕세계 = 안녕세계
    - sys.getdefaultencoding() = utf-8
    - sys.stdout.encoding = 'utf-8'
 """
import io
import sys

def main():
    sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

if __name__ == '__main__':
    main()
