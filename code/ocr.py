import os
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential

# EN - Set the values of your computer vision endpoint and computer vision key as environment variables:
# SP - Configura las variables de entorno como las variables "endpoint" y "key" a utilizar por el probrama:
try:
    endpoint = os.environ['VISION_ENDPOINT']
    key = os.environ['VISION_KEY']
except KeyError:
    print('No se encuentran las variables de entorno "VISION_ENDPOINT" or "VISION_KEY".')
    print('Asegurese de estar en el entorno de desarrolo correcto y de que las variables de entorno están configuradas.')
    exit()

# EN - Create the image analysis client
# SP - Crea el cliente para el análisis usando las variables de entorno 
client = ImageAnalysisClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(key),
)

# EN - Get a caption for the image. This will be a synchronously call.
# SP - Obtenemos el subtítulo de la imagen me diante una llamada sincrónica
result = client.analyze_from_url(
    image_url='https://img.freepik.com/psd-premium/mockup-cartel-ciudad-noche_23-2147912092.jpg',
    visual_features=[VisualFeatures.CAPTION, VisualFeatures.READ],
    gender_neutral_caption=True,  # Optional (default is False)
    language='en'
)

# EN - Print OCR analysis results
# SP - Imprime el resultado del analisis OCR por consola
print('\n- Lectura:')
if result.read is not None and result.read.blocks:
    for line in result.read.blocks[0].lines:
        print(f'Linea: "{line.text}", Polígono delimitador {line.bounding_polygon}')
        for word in line.words:
            print(f'Palabra: "{word.text}", Polígono delimitador {word.bounding_polygon}, /Confianza {word.confidence:.3f}/\n')
else:
    print('No existe.\n')
