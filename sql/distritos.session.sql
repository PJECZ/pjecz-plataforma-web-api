-- @block listar
-- @conn pjecz_plataforma_web
SELECT id,
    nombre
FROM distritos
ORDER BY nombre;
-- @block listar activos
-- @conn pjecz_plataforma_web
SELECT id,
    nombre,
    es_distrito_judicial
FROM distritos
WHERE estatus = 'A'
ORDER BY nombre;
