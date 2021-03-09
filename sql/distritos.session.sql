-- @block listar
SELECT id,
    nombre
FROM distritos
ORDER BY nombre;
-- @block listar activos
SELECT id,
    nombre
FROM distritos
WHERE estatus = 'A'
ORDER BY nombre;
