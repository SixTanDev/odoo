# Odoo Technical Test

This repository contains code and configuration files for setting up Odoo using Docker Compose and creating a checklist management module.

## Makefile
| Objetivo               | Comando                                       | Descripción                                                      |
|------------------------|----------------------------------------------|------------------------------------------------------------------|
| build_image            | `make build_image`                            | Construye la imagen Docker de Odoo.                               |
| build                  | `make build`                                  | Construye los contenedores definidos en el archivo `docker-compose.yml`. |
| run_odoo               | `make run_odoo`                               | Inicia los contenedores en modo daemon para ejecutar Odoo.       |
| interactive_odoo       | `make interactive_odoo`                       | Permite ingresar al contenedor de Odoo en un entorno interactivo. |
| interactive_development | `make interactive_development`                 | Permite ingresar al contenedor de desarrollo en un entorno interactivo. |
| create_module          | `make create_module`                          | Crea un nuevo módulo de Odoo utilizando el comando `odoo scaffold`. |
| pre_commit             | `make pre_commit`                             | Ejecuta pre-commit para realizar verificaciones en todos los archivos. |

The above commands allow you to build images, run containers, access containers in interactive mode, create Odoo modules, and perform verifications on files before committing changes.


## Part 1: Odoo Configuration with Docker

### Prerequisites

Docker should be installed on your machine.

### Setup
Create a `docker-compose.yml` file to configure the Odoo container. Make sure the file includes the following components:
- Odoo container with necessary environment variables.
- PostgreSQL container for the Odoo database.
- Port mapping to access Odoo from a web browser.
- Container development

Use Docker Compose to start the containers.

`# Run Docker Compose
docker-compose up -d
`
## Part 2: Checklist Module Creation

### Create the Module

1. Create a new Odoo module named checklist_management. You can do this using the Odoo web interface or the command odoo scaffold in the command line.
2. Define an Odoo model checklist.checklist with the following fields:
  - Checklist Title (text field).
  - Checklist Description (text field).
  - Assigned User (selection/dropdown field for assigning users to checklist items).
3. Define another Odoo model checklist.item with the following fields:
  - Item Title (text field).
  - Item State (selection/dropdown field with options such as "Pending," "In Progress," and "Completed").
  - Checklist to Which It Belongs (relation to the checklist.checklist model).
4. Create a view for the checklist form (form view) that includes fields from the checklist.checklist model.
5. Create a view for the checklist list (tree view) that displays records from checklist.checklist.
6. Create a view for the item form (form view) that includes fields from the checklist.item model.
7. Create a view for the item list (tree view) that displays records from checklist.item.

## Part 3: Testing

Create a new checklist and add several items to it, assigning different users to the items.
Verify that you can edit and update checklist items by changing their status and assigning users.
