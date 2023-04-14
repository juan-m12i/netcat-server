set CONTAINER_NAME=cont-netcat-web
set IMAGE_NAME=img-netcat-web

docker build -t %IMAGE_NAME% .

:: Remove the container if it already exists
docker ps -a --format "{{.Names}}" | findstr /B /C:"%CONTAINER_NAME%" >nul
if %errorlevel% equ 0 (
  docker stop %CONTAINER_NAME%
  docker rm %CONTAINER_NAME%
)

docker run -d --name %CONTAINER_NAME% -p 5000:5000 %IMAGE_NAME%
