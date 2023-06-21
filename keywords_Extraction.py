
import numpy as np
import pandas as pd
import re
from collections import Counter
from konlpy.tag import Okt
import time
from tqdm.notebook import tqdm
okt = Okt()
class Keywords_frequency():
    def __init__(self):
        # self.text = text
      
        self.con = re.compile(r'[^ A-Za-z0-9가-힣+]')

    def token_counter(self, text, num, stopword=None,text_pos='Noun'):
        """
        토큰의 개수를 세어주는 함수
        text: 문자열 데이터
        text_pos(default == Noun): 찾고자 하는 품사  
        num: frequency rank
        stopword = 불용어
        """

        sentence_tag = []
        result = []
        start = time.time()
        cleaned = self.con.sub('', text).lower()                # 특수문자제거
        print(f'cleaned 실행결과 : {time.time()-start:.5f}초')
        start = time.time()
        morphs = okt.pos(cleaned)                               # 토큰 / 품사 tuple list 추출 ex> ('설명', 'Noun')
        print(f'morphs 실행결과 : {time.time()-start:.5f}초')
        sentence_tag.append(morphs)                             # 토큰 리스트 저장  ex> [('설명', 'Noun'),('해보세요', 'Verb'),...]

        for sentence in tqdm(sentence_tag):
            for word, tag in sentence:
                if (tag == text_pos)and (len(word) > 1):        # 요청한 품사이고, 길이가 한글자 이상인 경우 추출 해당 단어 추출
                    result.append(word)
        counts = Counter(result)                                # 빈도수 계산을 위한 Counter 적용
        keyword_freq = counts.most_common(num)                  # 진해 품사 빈도수 확인
        keywords = [keyword[0] for keyword in keyword_freq]     # 상위 빈도 키워드 추출
        return keyword_freq, keywords                           

    # def keyword_lookup(self, df, variable, pos="Noun"):
    #     """
    #     키워드와 빈도 관련하여 column을 추가해주는 함수
    #     df: 데이터 테이블
    #     variable: 추출을 원하는 변수
    #     pos: 키워드 추출을 원하는 품사 -> default는 명사
    #     """
    #     keyword_frequency=[]
    #     keywords = []
    #     for index in (range(len(df))):
    #         keyword_frequency.append(token_counter(df[variable][index], pos, 3)[0])
    #         keywords.append(token_counter(df[variable][index], pos, 3)[1])
    #     df[variable+'키워드빈도'] = keyword_frequency
    #     df[variable+'키워드'] = keywords
    #     return df