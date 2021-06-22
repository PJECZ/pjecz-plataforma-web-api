-- @block listar autoridades activas
SELECT distritos.nombre AS departamento,
    autoridades.clave,
    autoridades.descripcion
FROM distritos
    INNER JOIN autoridades ON autoridades.distrito_id = distritos.id
WHERE autoridades.estatus = 'A'
ORDER BY departamento,
    descripcion;
-- @block listar juzgados y materias
SELECT autoridades.organo_jurisdiccional,
    materias.nombre AS materia,
    distritos.nombre AS departamento,
    autoridades.clave,
    autoridades.descripcion AS juzgado
FROM autoridades
    INNER JOIN distritos ON autoridades.distrito_id = distritos.id
    INNER JOIN materias ON autoridades.materia_id = materias.id
WHERE distritos.es_distrito_judicial = True
    AND autoridades.es_jurisdiccional = True
    AND autoridades.es_notaria = False
    AND autoridades.estatus = 'A'
ORDER BY organo_jurisdiccional,
    materia,
    departamento,
    clave ASC
