# La Inteligencia Aritificial en Microsoft Azure

## Introducción

¡Bienvenid@! 👋 esta es la documentación de mi proyecto personal sobre reconocimiento de imagenes utilizando los servicios de inteligencia artificial de Microsoft Azure, en él, se describe en detalle el código escrito mediante comentarios y ejemplos prácticos que se podrán ejecutar directamente en este cuaderno de [Python](https://www.python.org/psf-landing/).

Se ha decidido crear esta documentación en español ya que esto mismo se encuentra explicado en inglés con mayor cantidad de detalle en la documentación oficial de Microsoft en GitHub.

+ Documentación Microsoft: [Click aquí](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/overview-image-analysis?tabs=4-0)

+ Cuaderno de Colab: [Click aquí](https://colab.research.google.com/drive/1tQ1ebKbxK0BhLUiDoIbv2nvHlXqNqxil#scrollTo=Pgdz-5wIMh-M)

¡Espero que disfrutéis de este proyecto! 😃

## Configuración del Entorno

Antes de empezar a probar nuestro código, hay que tener en cuenta la configuración del entorno de trabajo, cabe recalcar que yo he estado usando tanto un entorno local en el SO Window 10 para programar el código, como un entorno en la nube como es Google Colab para crear la documentación de este proyecto, por lo que la configuración del entorno que contemplo en este apartado, puede cambiar para ti si usan otros sistemas diferentes, por lo pronto lo que veremos acontinuación será:

+ Instalación de paquetes
+ Variables de entorno
+ Archivos y directorios

### Instalación de paquetes de Azure

Para que nuestro código funcione correctamente, necesitaremos instalar previamente los paquetes que vamos a utilizar en nuestro código, serán los siguientes:

+ [Azure ai vision imageanalysis](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/overview-image-analysis?tabs=4-0)
+ [google translate](https://cloud.google.com/translate/?hl=es)

Para instalar cada uno de ellos debemos hacerlo desde la consola de comandas `cmd` en nuestro sistema operativo en caso de que queramos trabajar localmente, lo haremos con `pip` 
