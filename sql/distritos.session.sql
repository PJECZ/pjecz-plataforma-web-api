-- @block listar activos
SELECT id,
    nombre,
    es_distrito_judicial
FROM distritos
WHERE es_distrito_judicial = TRUE
    AND estatus = 'A'
ORDER BY nombre;
