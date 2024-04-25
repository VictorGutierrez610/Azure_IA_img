# La Inteligencia Aritificial en Microsoft Azure

## Introducción

¡Bienvenid@! 👋 esta es la documentación de mi proyecto personal sobre reconocimiento de imagenes utilizando los servicios de inteligencia artificial de **Microsoft Azure**, en él, se describe en detalle el código escrito mediante comentarios y ejemplos prácticos que se podrán ejecutar directamente en el cuaderno de [Python](https://www.python.org/psf-landing/) que te dejaré a continuación, el cual he creado para que puedas probar por ti mismo el código sin que tengas que hacer nada mas que tener una simple cuenta de correo gmail 😉.

Se ha decidido crear esta documentación en español ya que esto mismo se encuentra explicado en inglés con mayor cantidad de detalle en la **documentación oficial de Microsoft** en GitHub. Ante todo quiero dejar claro que no soy ningún experto en materia ni de programación, ni inteligencia artificial, ni en nigún ambito relacionado con el código, de hecho, esta documentación la escribo a modo de práctica y hobby cuando todavía soy estudiante de Desarrollo de Aplicaciones Web, mientras mi propósito es desarrollarme profesionalmente en **Big Data e IA**. 

+ Documentación Microsoft: [Click aquí](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/overview-image-analysis?tabs=4-0)

+ Cuaderno de Colab: [Click aquí](https://colab.research.google.com/drive/1tQ1ebKbxK0BhLUiDoIbv2nvHlXqNqxil#scrollTo=Pgdz-5wIMh-M)

¡Espero que disfrutéis de este proyecto! 😃

## Configuración del Entorno

Antes de empezar a probar nuestro código, hay que tener en cuenta la configuración del entorno de trabajo, cabe recalcar que yo he estado usando tanto un entorno local en el **SO Window 10** trabajando en **visual studio code**, como a su vez, un entorno en la nube como es **Google Colab** para crear el cuarderno de Python con cada uno de los códigos de este proyecto, por lo que la configuración del entorno que contemplo en este apartado, puede cambiar para ti si usas otros sistemas diferentes, por lo pronto lo que veremos a continuación será:

+ Instalación de paquetes
+ Variables de entorno
+ Archivos y directorios

### Instalación de paquetes de Azure

Para que nuestro código funcione correctamente, necesitaremos instalar previamente los paquetes que vamos a utilizar en nuestro código, serán los siguientes:

+ [Azure ai vision imagean alysis](https://pypi.org/project/azure-ai-vision-imageanalysis/)
+ [google translate](https://pypi.org/project/googletrans/)

Para instalar cada uno de ellos debemos hacerlo desde la consola de comandas `cmd` en nuestro sistema operativo en caso de que queramos trabajar localmente, lo haremos con `pip install`:

+ Instalar el paquete de vision imagean alysis:
  ```bash
  pip install azure-ai-vision-imageanalysis
  ```
+ Instalar el paquete de google translate:
  ```bash
  pip install googletrans
  ```
Ten presente que en en el cuarderno de colab antes de probar la inteligencia artificial de Azure, debes ejecutar las dos primeras celdas de código para instalar estos paquetes en este entorno virtual.

### Variables de entorno

He decidido usar variables de entorno para preservar la seguridad e integridad de los datos proporcionados por el recurso de [Computer Vision](https://portal.vision.cognitive.azure.com/gallery/featured) creado en Azure, así proteger tanto las credeciales del recurso como la URL de extremo. Con esto te quiero decir que el código debería ser modificado en tal caso de que quieras usarlo en cualquier otro entorno con un recuerso propio. **¡RECUERDA!** Es muy importante mantener siempre la mayor **seguridad en nuestro código**.

Para crear las variables de entorno en **Window 10** la forma más sencilla es acudir a nuestra gran amiga, la consola de comandos `cmd`, en ella usaremos: `SET [variable=[cadena]]` donde `variable` es el nombre que le queremos dar y `cadena` es el valor que queremos que reciba.

También podemos trabajar desde **visual studio code**, lo que nos permitirá crear variables de entorno para cualquiera de los entornos locales en los que estemos trabajando sin salir del programa, para ello debemos abrir una terminal de `powershell`  

>### Importante
>Puedes revisar las variables de entorno que tienes declaradas desde el `cmd` usando:
>```bash
>set
>```
>Con este comando te aparecerá una lista de todas las variables de entorno que están en tu entorno local de Window.
>
>También puedes conocer las variables de entorno que están declaradas para un entorno de desarrollo en concreto desde visual studio code usando: 
>```bash
>Get-ChildItem Env:
>```
>Lo cual personalmente me resulta más cómodo ya que podemos ir moviendonos entre diferentes entornos locales directamente desde visual studio code.

Como podrás ver en el cuarderno de **Google Colab** las variables de entorno se deben declarar y llamar de formas diferentes, la verdad es que resulta todo muy intuitivo como para explicarlo pero por si acaso, te comntaré que haciendo click en el icono de la llave de la barra lateral izquierda de nuestro cuaderno de colab se nos abrirá el apartado para nombrar y darle valor a nuestra variable de entorno. 







