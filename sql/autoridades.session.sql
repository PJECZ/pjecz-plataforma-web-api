-- @block listar
-- @conn pjecz_plataforma_web
SELECT autoridades.id,
    distritos.nombre,
    autoridades.descripcion
FROM distritos
    INNER JOIN autoridades ON autoridades.distrito = distritos.id
WHERE autoridades.estatus = 'A'
ORDER BY distritos.nombre,
    autoridades.descripcion
