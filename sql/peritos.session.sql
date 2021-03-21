-- @block listar
-- @conn pjecz_plataforma_web
SELECT distritos.nombre,
    peritos.tipo,
    peritos.nombre,
    peritos.renovacion
FROM peritos
    INNER JOIN distritos ON peritos.distrito = distritos.id
WHERE peritos.distrito = 6
ORDER BY peritos.nombre
LIMIT 25
