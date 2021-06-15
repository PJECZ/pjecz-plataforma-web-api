-- @block listar
SELECT autoridades.id,
    distritos.nombre,
    autoridades.descripcion
FROM distritos
    INNER JOIN autoridades ON autoridades.distrito = distritos.id
WHERE autoridades.estatus = 'A'
ORDER BY distritos.nombre,
    autoridades.descripcion;
-- @block autoridades y materias
SELECT distritos.nombre AS distrito,
    autoridades.clave,
    autoridades.descripcion
FROM autoridades
    INNER JOIN distritos ON autoridades.distrito_id = distritos.id
WHERE distritos.es_distrito_judicial = True
    AND autoridades.es_jurisdiccional = True
    AND autoridades.es_notaria = False
    AND autoridades.estatus = 'A'
ORDER BY distrito,
    clave ASC -- @block materias
SELECT nombre
FROM materias
ORDER BY id ASC
