BIENVENIDO A LAS INTRUCCIONES DE INSTALACION,  EMPECEMOS INSTALANDO

Asegurate de tener instalado python, para comprobarlo puedes introducir: pip freeze 
deveria darte una lista con las librerias de python instaladas, al final de las instalaciones de librerias comprueba que estan todas las que salen en el fichero requirements.txt 

instala las librerias con los siguientes codigos:

pip install flask

pip install flask_wtf


pip install python-dotenv

creacion de la base de datos:

En la consola de comandos escriba: 
sqlite3 base.db 
(hemos puesto ese nombre a la base de datos, si lo prefiere puede ponerle otro nombre, pero cambie tambien el nombre del archivo en la variable fichero que luego mencionaremos)

Si quieres que la ruta de la base de datos sea la misma que proponemos, mueve la base a una carpeta llamada data en el fichero crypto

ahora creamos las tablas con esta sentencia
.read migrations/tablas.sql




CSS: 
miligram??

comandos para repositorio git:

git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Aghmicrob/Proyecto-Flask_classic.git
git push -u origin main

