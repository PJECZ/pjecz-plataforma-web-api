-- @block listar
-- @conn pjecz_plataforma_web
SELECT listas_de_acuerdos.id,
    distritos.nombre,
    autoridades.descripcion,
    listas_de_acuerdos.fecha,
    listas_de_acuerdos.descripcion,
    listas_de_acuerdos.archivo,
    listas_de_acuerdos.url
FROM listas_de_acuerdos
    INNER JOIN autoridades ON listas_de_acuerdos.autoridad = autoridades.id
    INNER JOIN distritos ON autoridades.distrito = distritos.id
ORDER BY listas_de_acuerdos.fecha DESC
LIMIT 25;
