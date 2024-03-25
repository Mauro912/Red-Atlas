Scraping de Propiedades en ZonaProp

Este script en Python utiliza Selenium para realizar scraping en el sitio web de ZonaProp y obtener información sobre departamentos en alquiler en Moreno. En este caso, ordenados por precio ascendente. Para conseguir otros filtros o paginas, sólo hay que cambiar la url que se pasa como prámetro.

Requisitos

    Python 
    Selenium
    Pandas

Para instalar las dependencias se puede utilizar el siguiente comando:

pip install selenium pandas

Además, necesitarás descargar el controlador de Chrome WebDriver y asegurarte de que esté en tu PATH. 

Uso

    Clona este repositorio o descarga el script ZonaProp_Scraper.py.
   
    El script abrirá una ventana del navegador Chrome y comenzará a recopilar la información de los departamentos en alquiler en Moreno. Una vez completado, generará un archivo CSV llamado ZonaProp_Data.csv con los datos recopilados.
    El archivo CSV contendrá información sobre el precio mensual, gastos, dirección, área, cantidad de habitaciones y detalles de la unidad de cada propiedad.
 

Métodos Utilizados
Método find_element

El método find_element se utiliza para encontrar un elemento dentro del DOM (Documento de Objeto del Modelo) de una página web. Toma dos argumentos:

    El primer argumento especifica la estrategia de búsqueda, que puede ser por identificador de clase, identificador de nombre, selector CSS, XPath, etc.
    El segundo argumento especifica el valor que se está buscando.

Por ejemplo:


price_element = posteo.find_element(By.CLASS_NAME, 'sc-12dh9kl-3.iqNJlX')

En este caso, estamos buscando un elemento que tenga la clase 'sc-12dh9kl-3.iqNJlX'.
Método presence_of_all_elements_located

Este método espera a que se encuentren todos los elementos que cumplan con ciertas condiciones en la página. Toma una tupla como argumento, donde el primer elemento de la tupla especifica la estrategia de búsqueda y el segundo elemento especifica el valor que se está buscando.

Por ejemplo:


posts_container = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'sc-1tt2vbg-5.GcsXo')))

En este caso, estamos esperando a que se encuentren todos los elementos que tengan la clase 'sc-1tt2vbg-5.GcsXo'.
Otros Métodos de Selenium

    text: Este método se utiliza para obtener el texto contenido dentro de un elemento.
    get: Este método se utiliza para navegar a una URL específica.
    quit: Este método se utiliza para cerrar el navegador WebDriver.
    WebDriverWait: Este método se utiliza para esperar hasta que se cumplan ciertas condiciones antes de realizar una acción en el navegador. Se puede utilizar junto con otros métodos de espera, como presence_of_element_located, visibility_of_element_located, etc.

Estos son solo algunos de los métodos utilizados en el script. Selenium ofrece una gran cantidad de métodos para interactuar con elementos de una página web.

