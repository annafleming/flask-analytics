import pandas as pd
import numpy as np
import datetime

def get_summary(site_name):
    return {
        'today': {
            'reviews': 30,
            'promoters': 44,
            'passives': 4,
            'detractors': 94
        },
        'month': {
            'reviews': 30,
            'promoters': 44,
            'passives': 4,
            'detractors': 94
        },
    }

