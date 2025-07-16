<!-- ECOSYSTEM_DOCTRINE: genesis-agents -->
# 🤖 Ecosystem Doctrine — Genesis-Agents (Registro y Base de Agentes)

Este repositorio forma parte del ecosistema **Genesis Engine**.  
Su rol es el de **hub central de agentes y registro de capacidades**.

## 🧠 Rol Declarado

- Tipo: **Hub de Agentes**
- Nombre: `genesis-agents`
- Dominio: Registro y gestión de agentes
- Función: Proveer clase base y registro para todos los agentes

## 🔒 Mandamientos del Proyecto

### 1. **No implementarás lógica de negocio específica**
NO contiene lógica de FastAPI, Next.js, Docker, etc.  
Solo la clase base y registro de agentes.

### 2. **No generarás código de aplicación**
NO contiene generadores ni templates.  
Solo infraestructura para que otros agentes funcionen.

### 3. **No interactuarás con el usuario final**
NO tiene CLI ni interfaz gráfica.  
Es infraestructura silenciosa para otros repositorios.

### 4. **Serás la base común para todos los agentes**
Todos los agentes especializados deben heredar de tu clase base.  
Defines la interfaz estándar para comunicación MCPturbo.

### 5. **No conocerás dominios específicos**
Agnóstico a SaaS, e-commerce, arquitecturas específicas.  
Solo infraestructura de agentes pura.

### 6. **Proveerás discovery automático**
Sistema de registro para que genesis-core encuentre agentes.  
Auto-discovery de capacidades instaladas.

### 7. **Serás extensible pero estable**
Interfaz estable para que agentes especializados no se rompan.  
Extensible para nuevos tipos de agentes.

---

## 🧩 Interfaz esperada por consumidores

Los repositorios especializados deben usar:

- `GenesisAgent` (clase base)
- `AgentRegistry.register(agent)`
- `AgentCapabilities` (definición de capacidades)
- `TaskResult` (resultado estándar)

---

## 📦 Separación de capas (importante)

| Capa | Puede importar desde | No puede importar desde |
|------|----------------------|--------------------------|
| genesis-agents | mcpturbo | genesis-core, genesis-backend, genesis-frontend, genesis-devops, genesis-ai |
| genesis-backend | genesis-agents, mcpturbo | genesis-core |
| genesis-frontend | genesis-agents, mcpturbo | genesis-core |

---

## 🤖 AI Agents, please read:

Este repositorio es la fundación de todos los agentes.

Si estás revisando código, escribiendo tests o generando lógica nueva:
- ❌ No implementes lógica de generación específica.
- ❌ No agregues conocimiento de dominios específicos.
- ❌ No crees dependencias hacia repos especializados.
- ✅ Mantén la clase base simple y extensible.
- ✅ Enfócate en la interfaz MCPturbo.

Toda excepción debe documentarse en `DOCTRINE_CHANGE_REQUEST.md`.

---

## 📎 Referencias

- MCPturbo Core → [https://github.com/fmonfasani/mcpturbo](https://github.com/fmonfasani/mcpturbo)
- Genesis Core → [https://github.com/fmonfasani/genesis-core](https://github.com/fmonfasani/genesis-core)
