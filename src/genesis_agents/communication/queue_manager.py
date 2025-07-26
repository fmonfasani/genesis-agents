# src/genesis_agents/communication/queue_manager.py
"""
Gestor de colas para comunicación entre agentes.

Este módulo proporciona una forma de comunicación asíncrona y desacoplada
entre los diferentes agentes del ecosistema Genesis.
"""

import asyncio
from typing import Dict, Any

class QueueManager:
    """
    Gestiona múltiples colas de mensajes para la comunicación entre agentes.
    """
    def __init__(self):
        self.queues: Dict[str, asyncio.Queue] = {}
        self.logger = self._get_logger()

    def _get_logger(self):
        import logging
        return logging.getLogger("genesis.queue_manager")

    def create_queue(self, queue_name: str, max_size: int = 0):
        """
        Crea una nueva cola de mensajes.

        Args:
            queue_name: El nombre de la cola.
            max_size: El tamaño máximo de la cola. 0 para ilimitado.
        """
        if queue_name in self.queues:
            self.logger.warning(f"Queue '{queue_name}' already exists.")
            return
        self.queues[queue_name] = asyncio.Queue(maxsize=max_size)
        self.logger.info(f"Queue '{queue_name}' created.")

    def get_queue(self, queue_name: str) -> asyncio.Queue:
        """
        Obtiene una cola de mensajes existente.

        Args:
            queue_name: El nombre de la cola.

        Returns:
            La instancia de la cola.

        Raises:
            KeyError: Si la cola no existe.
        """
        if queue_name not in self.queues:
            raise KeyError(f"Queue '{queue_name}' not found.")
        return self.queues[queue_name]

    async def publish(self, queue_name: str, message: Any):
        """
        Publica un mensaje en una cola.

        Args:
            queue_name: El nombre de la cola.
            message: El mensaje a publicar.
        """
        try:
            queue = self.get_queue(queue_name)
            await queue.put(message)
            self.logger.debug(f"Message published to queue '{queue_name}'.")
        except KeyError:
            self.logger.error(f"Failed to publish to non-existent queue '{queue_name}'.")
        except asyncio.QueueFull:
            self.logger.error(f"Queue '{queue_name}' is full. Message discarded.")

    async def subscribe(self, queue_name: str) -> Any:
        """
        Se suscribe a una cola y espera un mensaje.

        Args:
            queue_name: El nombre de la cola.

        Returns:
            El mensaje recibido.
        """
        try:
            queue = self.get_queue(queue_name)
            message = await queue.get()
            self.logger.debug(f"Message received from queue '{queue_name}'.")
            return message
        except KeyError:
            self.logger.error(f"Failed to subscribe to non-existent queue '{queue_name}'.")
            return None

# Instancia global del gestor de colas
queue_manager = QueueManager()
