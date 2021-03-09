-- @block listar
-- @conn pjecz_plataforma_web
SELECT id,
    nombre
FROM distritos
ORDER BY nombre;
-- @block listar activos
-- @conn pjecz_plataforma_web
SELECT id,
    nombre
FROM distritos
WHERE estatus = 'A'
ORDER BY nombre;
