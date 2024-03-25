Scraping de Propiedades en ZonaProp

Este script en Python utiliza Selenium para realizar scraping en el sitio web de ZonaProp y obtener información sobre departamentos en alquiler en Moreno. En este caso, ordenados por precio ascendente. Para conseguir otros filtros o paginas, sólo hay que cambiar la url que se pasa como parámetro.

Requisitos

    Python 
    Selenium
    Pandas

Para instalar las dependencias se puede utilizar el siguiente comando:

    pip install selenium pandas

Además, se necesitará descargar el controlador de Chrome WebDriver y asegurarte de que esté en tu PATH. 

Uso
   
    El script abrirá una ventana del navegador Chrome y comenzará a recopilar la información de los departamentos en alquiler en Moreno. Una vez completado, generará un archivo CSV llamado ZonaProp_Data.csv con los datos recopilados.
    El archivo CSV contendrá información sobre el precio mensual, gastos, dirección, área, cantidad de habitaciones y detalles de la unidad de cada propiedad.
 


