import { WebflowClient } from "webflow-api";

const client = new WebflowClient({ accessToken: 'ws46356bb0189743cb4c4719ffcf8a6dd4c72ac19fa4d2461e562d8940a1e125b7' });

async function test() {
    try {
        const authenticatedUser = await client.authenticatedUser();
        console.log("Usuario autenticado:", authenticatedUser);
        
        const sites = await client.sites.list();
        console.log("Sitios disponibles:", sites);
    } catch (e) {
        console.error("Error detallado:", e.body);
    }
}

test();