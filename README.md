# Festival DevOps Music Fest 2026 🎸🐳

Proyecto final de la Semana 06 enfocado en la aplicación de flujo de trabajo colaborativo (Git Flow) y la contenerización de una arquitectura web (Frontend + Backend).

## Tecnologías Utilizadas
* **Frontend:** HTML5, CSS3, servido a través de Nginx.
* **Backend:** API REST desarrollada con Python y Flask.
* **Contenedores:** Docker y Docker Compose para la orquestación, redes y volúmenes.
* **Control de Versiones:** Git y GitHub.

## Instrucciones de Ejecución
1. Clonar el repositorio: `git clone <URL_DEL_REPO>`
2. Ingresar a la carpeta: `cd festival-devops`
3. Levantar los contenedores: `docker-compose up -d --build`
4. Accesos:
   - Frontend: [http://localhost:8080](http://localhost:8080)
   - Backend API: [http://localhost:5000](http://localhost:5000)