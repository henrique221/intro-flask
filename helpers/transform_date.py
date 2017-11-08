from datetime import datetime

class TransformDate:

    @staticmethod
    def transform_date_to_br(date):
        return date.strftime("%d/%m/%y %H:%M")