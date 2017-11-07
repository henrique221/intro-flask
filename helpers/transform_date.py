from datetime import datetime

class TransformDate:

    def transform_date_to_br(self, date):
        return date.strftime("%d/%m/%y %H:%M")