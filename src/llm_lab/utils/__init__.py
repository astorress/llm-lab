"""Utilidades transversales: reproducibilidad, hardware, logging y configuración.

Las exportaciones se cargan de forma PEREZOSA (PEP 562): importar este paquete
—o un submódulo como ``llm_lab.utils.config``— NO arrastra ``torch``. Así el
pipeline de datos (``llm_lab.data``), que solo necesita ``config``, es
importable en entornos sin PyTorch instalado. ``torch`` solo se importa al
acceder realmente a ``set_seed``, ``detect_hardware`` o ``get_device``.
"""

from __future__ import annotations

__all__ = [
    "load_config",
    "load_yaml",
    "detect_hardware",
    "get_device",
    "get_logger",
    "MetricsLogger",
    "set_seed",
]

# Mapa nombre exportado -> (submódulo, atributo). La carga ocurre en __getattr__.
_LAZY = {
    "load_config": ("config", "load_config"),
    "load_yaml": ("config", "load_yaml"),
    "get_logger": ("logging", "get_logger"),
    "MetricsLogger": ("logging", "MetricsLogger"),
    "set_seed": ("seed", "set_seed"),                 # importa torch al usarse
    "detect_hardware": ("hardware", "detect_hardware"),  # importa torch al usarse
    "get_device": ("hardware", "get_device"),            # importa torch al usarse
}


def __getattr__(name: str):
    """Importa el submódulo correspondiente solo cuando se accede al símbolo."""
    if name in _LAZY:
        import importlib
        module_name, attr = _LAZY[name]
        module = importlib.import_module(f"llm_lab.utils.{module_name}")
        return getattr(module, attr)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__() -> list[str]:
    return sorted(__all__)
