
from keywords_Extraction import Keywords_frequency
import os
import time 
# os.environ['JAVA_HOME'] =r'/Users/codestates/Downloads/jdk-20.0.1/bin'

def main():
    # 데이터 경로 받아오기 > 이 부분은 유저의 '기록'데이터를 가져와 읽도록 하면됨
    data_path = 'testdata.txt'
    data = []
    with open(data_path) as f:
        data_all = f.readlines()
        for row in data_all:
            data.append(row)
    data = ','.join(data)
    keyword_func = Keywords_frequency()
    top_keywords = keyword_func.token_counter(data, 3)
    print(top_keywords)

if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(f'{end-start:.5f}초 소요') 