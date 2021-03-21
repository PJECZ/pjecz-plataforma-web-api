-- @block listar
-- @conn pjecz_plataforma_web
SELECT fecha,
    nombre,
    numero,
    libro
FROM abogados
ORDER BY fecha DESC;
LIMIT 25;
-- @block listar
-- @conn pjecz_plataforma_web
SELECT fecha,
    nombre,
    numero,
    libro
FROM abogados
WHERE nombre ILIKE '%ROSALBA%'
ORDER BY fecha DESC
LIMIT 25;
