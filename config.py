default_city = 'passau'
warning_levels_upper = {'keine Meldestufe': 700, 'Meldestufe1': 740, 'Meldestufe2': 770, 'Meldestufe3': 850,
                        'Meldestufe4': float('inf')}
url = 'https://www.pegelonline.wsv.de/webservices/rest-api/v2/stations.json?includeTimeseries=true' \
      '&includeCurrentMeasurement=true'

emojis = {'keine Meldestufe': '✔',
          'Meldestufe1': '❕',
          'Meldestufe2': '❗',
          'Meldestufe3': '❗❗',
          'Meldestufe4': '❗❗❗',
          'steigend': '↗',
          'gleichbleibend': '➡',
          'fallend': '↘'}

trends = {-1: 'fallend', 0: 'gleichbleibend', 1: 'steigend'}