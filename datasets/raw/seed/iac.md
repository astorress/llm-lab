# Corpus semilla — dominio: iac

## Infraestructura como código con Terraform
<!-- subcategoria: terraform | dificultad: intermedio | idioma: es -->
La infraestructura como código (IaC) gestiona recursos de cómputo, red y almacenamiento mediante archivos versionados en lugar de configuración manual. Terraform usa un lenguaje declarativo (HCL): se describe el estado deseado y Terraform calcula el plan de cambios (terraform plan) para alcanzarlo, aplicándolo de forma idempotente (terraform apply). Mantiene un archivo de estado que mapea los recursos reales con la configuración. Los módulos encapsulan y reutilizan componentes; los proveedores abstraen las APIs de AWS, Azure, GCP y otros. El estado remoto compartido y el bloqueo evitan conflictos en equipos.
