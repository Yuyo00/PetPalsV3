from .models import Categoria, Producto, Bodega

def eliminar_registro(modelo, clave_primaria):
    eliminado, mensaje = verificar_eliminar_registro(modelo, clave_primaria, True)
    return mensaje

def verificar_eliminar_registro(modelo, clave_primaria, debe_eliminar_registro):
    accion_eliminar = modelo.acciones()['accion_eliminar']


    if not modelo.objects.filter(pk=clave_primaria).exists():
        return False, f'¡No se puede {accion_eliminar} {clave_primaria}, ya que no existe en la Base de Datos! Revise si el registro de la tabla de {modelo._meta.verbose_name} ya fue eliminado por otro usuario.'
    

    registro = modelo.objects.get(pk=clave_primaria)
    info_registro = str(registro)
    tablas_relacionadas = modelo._meta.related_objects

    for tabla_relacionada in tablas_relacionadas:

        modelo_relacionado = tabla_relacionada.related_model
        nombre_campo_relacionado = tabla_relacionada.field.name

        nombre_tabla_relacionada = modelo_relacionado._meta.verbose_name
        nombre_tabla_relacionada_plural = modelo_relacionado._meta.verbose_name_plural

        if modelo_relacionado.objects.filter(**{nombre_campo_relacionado: clave_primaria}).exists():
            return False, f'¡No se puede {accion_eliminar} "{info_registro}", ya que está presente en {nombre_tabla_relacionada_plural}!'

    try:
        if debe_eliminar_registro:
            registro.delete()
        return True, f'¡El {modelo._meta.verbose_name} "{info_registro}" fue eliminado correctamente!'
    except Exception as error:
        return False, f'Comuníquese con el Administrador del sistema. ¡No se pudo eliminar el {modelo._meta.verbose_name} "{info_registro}", pues se presentó el siguiente problema: {error}!'
