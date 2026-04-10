
const token = "b0b1eeb6380643b1c4dc8cbc39bb24dee67fd2aa1406ea95f4a310cc4c7684a8";
;
import "dotenv/config";
import { WebflowClient } from "b0b1eeb6380643b1c4dc8cbc39bb24dee67fd2aa1406ea95f4a310cc4c7684a8";

// 1. Verificamos que el token existe en el .env
const token = process.env.WEBFLOW_API_TOKEN;

if (!token) {
    console.error("❌ Error: No se encontró WEBFLOW_API_TOKEN en el archivo .env");
    process.exit(1);
}

// 2. Inicializamos el cliente
const webflow = new WebflowClient({ accessToken: token.trim() });

// ─── FUNCIONES DE LECTURA ────────────────────────────────────────────────────

async function listarSitios() {
    const sites = await webflow.sites.list();
    console.log("\n📋 Sitios disponibles:");
    sites.forEach(site => {
        console.log(`  ➡️  ${site.displayName} | ID: ${site.id}`);
    });
    return sites;
}

async function listarColecciones(siteId) {
    const collections = await webflow.collections.list(siteId);
    console.log(`\n📁 Colecciones del sitio ${siteId}:`);
    collections.collections.forEach(col => {
        console.log(`  ➡️  ${col.displayName} | ID: ${col.id}`);
    });
    return collections.collections;
}

async function listarItems(collectionId) {
    const items = await webflow.collections.items.list(collectionId);
    console.log(`\n📄 Items de la colección ${collectionId}:`);
    items.items.forEach(item => {
        console.log(`  ➡️  ${item.fieldData?.name || item.id} | ID: ${item.id}`);
    });
    return items.items;
}

// ─── FUNCIONES DE ESCRITURA ──────────────────────────────────────────────────

async function crearItem(collectionId, datos) {
    const item = await webflow.collections.items.create(collectionId, {
        fieldData: datos,
    });
    console.log(`\n✅ Item creado: ${item.id}`);
    return item;
}

async function actualizarItem(collectionId, itemId, datos) {
    const item = await webflow.collections.items.update(collectionId, itemId, {
        fieldData: datos,
    });
    console.log(`\n✅ Item actualizado: ${item.id}`);
    return item;
}

async function eliminarItem(collectionId, itemId) {
    await webflow.collections.items.delete(collectionId, itemId);
    console.log(`\n✅ Item eliminado: ${itemId}`);
}

async function publicarSitio(siteId) {
    await webflow.sites.publish(siteId, { publishToWebflowSubdomain: true });
    console.log(`\n🚀 Sitio publicado: ${siteId}`);
}

// ─── FUNCIÓN PRINCIPAL ───────────────────────────────────────────────────────

async function ejecutar() {
    const comando = process.argv[2];

    try {
        switch (comando) {
            case "info": {
                console.log("🔗 Probando conexión con Webflow...");
                const sites = await listarSitios();
                console.log(`\n✅ Conexión exitosa. ${sites.length} sitio(s) encontrado(s).`);
                break;
            }

            case "colecciones": {
                const siteId = process.argv[3];
                if (!siteId) {
                    console.error("❌ Uso: node index.js colecciones <siteId>");
                    process.exit(1);
                }
                await listarColecciones(siteId);
                break;
            }

            case "items": {
                const collectionId = process.argv[3];
                if (!collectionId) {
                    console.error("❌ Uso: node index.js items <collectionId>");
                    process.exit(1);
                }
                await listarItems(collectionId);
                break;
            }

            case "crear": {
                // Ejemplo: node index.js crear <collectionId> '{"name":"Título","slug":"titulo"}'
                const collectionId = process.argv[3];
                const datos = JSON.parse(process.argv[4] || "{}");
                if (!collectionId) {
                    console.error("❌ Uso: node index.js crear <collectionId> '{\"name\":\"Título\"}'");
                    process.exit(1);
                }
                await crearItem(collectionId, datos);
                break;
            }

            case "actualizar": {
                // Ejemplo: node index.js actualizar <collectionId> <itemId> '{"name":"Nuevo título"}'
                const collectionId = process.argv[3];
                const itemId = process.argv[4];
                const datos = JSON.parse(process.argv[5] || "{}");
                if (!collectionId || !itemId) {
                    console.error("❌ Uso: node index.js actualizar <collectionId> <itemId> '{\"name\":\"Nuevo\"}'");
                    process.exit(1);
                }
                await actualizarItem(collectionId, itemId, datos);
                break;
            }

            case "publicar": {
                const siteId = process.argv[3];
                if (!siteId) {
                    console.error("❌ Uso: node index.js publicar <siteId>");
                    process.exit(1);
                }
                await publicarSitio(siteId);
                break;
            }

            default: {
                console.log(`
📖 Comandos disponibles:
  node index.js info                                        → Verificar conexión y listar sitios
  node index.js colecciones <siteId>                       → Listar colecciones CMS
  node index.js items <collectionId>                       → Listar items de una colección
  node index.js crear <collectionId> '<json>'              → Crear nuevo item
  node index.js actualizar <collectionId> <itemId> '<json>'→ Actualizar item existente
  node index.js publicar <siteId>                          → Publicar el sitio
                `);
            }
        }

    } catch (error) {
        console.error("❌ Error:");
        if (error.body) {
            console.error(JSON.stringify(error.body, null, 2));
        } else {
            console.error(error.message);
        }
        process.exit(1);
    }
}

ejecutar();