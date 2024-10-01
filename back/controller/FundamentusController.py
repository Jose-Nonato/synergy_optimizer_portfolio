import fundamentus as fund


class FundamentusController:
    @staticmethod
    def get_all_papers():
        data = fund.get_resultado_raw()
        return data.to_dict()
