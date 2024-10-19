@echo off
:: Ejecutar el comando de MkDocs para desplegar en GitHub
mkdocs gh-deploy

:: Añadir todos los cambios al índice de Git
git add .

:: Realizar el commit con un mensaje predefinido
git commit -m "commit"

:: Enviar los cambios al repositorio remoto (GitHub)
git push

:: Pausar para que puedas ver el resultado en la terminal antes de que se cierre
pause
