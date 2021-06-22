-- @block materias
SELECT nombre
FROM materias -- @block juzgados civiles
SELECT autoridades.clave,
    autoridades.descripcion
FROM autoridades
    JOIN materias ON autoridades.materia_id = materias.id
WHERE materias.nombre = 'CIVIL'
ORDER BY clave ASC
