import os
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential
from googletrans import Translator 

def traslate_to_spanish(texto):
    translator = Translator()
    return translator.translate(texto, src='en', dest='es').text

# EN - Set the values of your computer vision endpoint and computer vision key as environment variables:
# SP - Configura las variables de entorno como las variables "endpoint" y "key" a utilizar por el probrama: 
try:
    endpoint = os.environ['VISION_ENDPOINT']
    key = os.environ['VISION_KEY']
except KeyError:
    print('No se encuentran las variables de entorno "VISION_ENDPOINT" or "VISION_KEY".')
    print('Asegurese de estar en el entorno de desarrolo correcto y de que las variables de entorno están configuradas.')
    exit()

# EN - Create an Image Analysis client
# SP - Crea el cliente para el análisis usando las variables de entorno 
client = ImageAnalysisClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(key),
)

# EN - Get a caption for the image. This will be a synchronously (blocking) call.
# SP - Obtenemos el subtítulo de la imagen me diante una llamada sincrónica
result = client.analyze_from_url(
    image_url='https://cloudfront-us-east-1.images.arcpublishing.com/elespectador/SQT6VSTKY5ALBBK4QFI22JCWNY.jpg',
    visual_features=[VisualFeatures.CAPTION, VisualFeatures.READ],
    gender_neutral_caption=True,  # Optional (default is False)
    language='en'
)

# EN - Print caption results to the console
# SP - Imprime la descripción de la imagen por consola
print('\nResultados del análisis:')
print('- Descripción:')
if result.caption is not None:
    traslate_description = traslate_to_spanish(result.caption.text)
    #print(f'{result.caption.text}, /Confianza = {result.caption.confidence:.3f}/\n') #--> English
    print(f'{traslate_description}, /Confianza = {result.caption.confidence:.3f}/\n') #--> Español
