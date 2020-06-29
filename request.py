
import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'fixedacidity':2,'volatileacidity':9,'citricacid':6,'residualsugar':2,'chlorides':9,'freesulfurdioxide':6,
                            'totalsulfurdioxide':9,'density':6,'pH':2,'sulphates':9,
                            'alcohol':6})

print(r.json())