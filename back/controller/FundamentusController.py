import fundamentus as fund
import json


class FundamentusController:
    @staticmethod
    def df_to_array(df):
        result_array = []
        for index, row in df.iterrows():
            result_array.append({
                'papel': index,
                'cotacao': row['cotacao'],
                'pl': row['pl'],
                'pvp': row['pvp'],
                'psr': row['psr'],
                'dy': row['dy'],
                'pa': row['pa'],
                'pcg': row['pcg'],
                'pebit': row['pebit'],
                'pacl': row['pacl'],
                'evebit': row['evebit'],
                'evebitda': row['evebitda'],
                'mrgebit': row['mrgebit'],
                'mrgliq': row['mrgliq'],
                'roic': row['roic'],
                'roe': row['roe'],
                'liqc': row['liqc'],
                'liq2m': row['liq2m'],
                'patrliq': row['patrliq'],
                'divbpatr': row['divbpatr'],
                'c5y': row['c5y']
            })
        return result_array


    @staticmethod
    def get_all_papers():
        data = fund.get_resultado()
        data = data[data['pl'] > 0]
        array_data = FundamentusController.df_to_array(data)
        return array_data
    

    @staticmethod
    def get_paper(ticker):
        df = fund.get_papel(ticker)
        json_str = df.to_json(orient='records')
        return json.loads(json_str)
