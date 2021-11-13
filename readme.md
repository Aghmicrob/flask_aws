Instrucciones de instalacion:
A.1 Instalamos visual studio code:
    Utilizando visual studio code: 
    Comencemos instalando visualstudiocode desde su pagina
    instalamos python, igualmente desde su pagina web

B.Crea el entorno vitrual: 
    Introduce el siguiente comando en la consola: 
    <<< python -m venv venv >>>
    Para activarlo, introduce: 
    (sistema operativo windows): <<< venv\Scripts\activate >>>

    RECUERDA QUE DEBES TENER ACTIVADO EL ENTORNO VIRTUAL ANTES DE INSTALAR LAS DEPENDENCIAS:
    aparecera en la consola un mensaje   <<<  (venv)  >>> antes de la linea en que escribimos comandos en la consola.        

C. desde la consola de comandos, instalamos las librerias necesarias, tenemos 2 opciones: 
    podemos introducir en la consola los siguientes comandos:
    pip install flask
    pip install flask_wtf
    pip install python-dotenv
    pip install requests 

    
    aunque es más recomendable instalar todas las dependencias con el siguiente comando:
        pip install -r requirements.txt

    RECORDAMOS QUE CADA SISTEMA OPERATIVO PUEDE VARIAR SUS COMANDOS DE INSTALACION por ejemplo:
        EN WINDOWS: python -m pip install 
        EN LINUX: sudo apt-get install 

D. creacion de la base de datos:

    En la consola de comandos escriba: 
    sqlite3 base.db 
    (hemos puesto ese nombre a la base de datos, si lo prefiere puede ponerle otro nombre, pero cambie tambien el nombre del archivo en la variable fichero que luego mencionaremos)

    Si quieres que la ruta de la base de datos sea la misma que proponemos, mueve la base a una carpeta llamada data (debes crearla) dentro de la carpeta crypto.
    ahora creamos las tablas con esta sentencia
    .read migrations/Tablas.sql


crea un fichero llamado: .env

    y dentro tiene que tener las siguientes sentencias:  
        FLASK_ENV = development
        FLASK_APP = run.py

a continuacion crea un fichero denominado: config.py

    y dentro pondremos las variables FICHERO = (con la ruta en que hayamos creado la base de datos) 

    SECRET_KEY  contendrá la clave privada de tu conexion, es una cadena aleatoria, crea una propia e introducela aqui como una cadena
    pueder crear una cadena aleatoria facilmente en la siguiente pagina: https://randomkeygen.com/

    api_key contendrá la clave para acceder a la api, la obtendremos de la pagina: https://coinmarketcap.com/api/




