import pandas as pd

'''url = 'https://finance.naver.com/item/main.nhn?code=035720'
table_df_list = pd.read_html(url, encoding='euc-kr')
table_df = table_df_list[3]
table_df = pd.DataFrame(table_df)'''
'''print(table_df)'''

# 코스피에 상장된 주요 종목의 주요재무정보를 가져오기

import FinanceDataReader

kospi = FinanceDataReader.StockListing("KOSPI")
'''print(kospi)'''

kospi_info_list = []
for code in kospi['Code'][:10]:
    url = f'https://finance.naver.com/item/main.nhn?code={code}'
    table_df_list = pd.read_html(url, encoding='euc-kr')
    table_df = table_df_list[3]
    kospi_info_dic = {}
    kospi_info_dic['code'] = code
    kospi_info_dic['table'] = table_df
    kospi_info_list.append(kospi_info_dic)

print(kospi_info_list)

print(kospi_info_list[0]['code'])
'''display(kospi_info_list[0]['table'])'''