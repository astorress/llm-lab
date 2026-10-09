# Colab y Hardware — Limitaciones y Presupuestos

> Pasos concretos de ejecución: [06 · Guía de ejecución](06_guia_ejecucion.md). Este documento explica el *porqué* de los límites de hardware.

## Perfiles de GPU en Google Colab

| | T4 (Free) | L4 (Pro) | A100 40GB (Pro/Pro+) |
|---|---|---|---|
| VRAM | 16 GB | 24 GB | 40 GB |
| Arquitectura | Turing (2018) | Ada (2023) | Ampere (2020) |
| bf16 | ❌ (solo fp16) | ✅ | ✅ |
| TF32 | ❌ | ✅ | ✅ |
| FP16 TFLOPS | ~65 | ~121 | ~312 |
| Flash Attention | ⚠️ limitado | ✅ | ✅ |
| Perfil del pipeline | `small` | `large` (batch 16 + accum 16) | `large` |
| Perfil de los notebooks | SMALL | SMALL o LARGE (según VRAM) | LARGE |

## Limitaciones de Colab que afectan al laboratorio

1. **Desconexiones**: las sesiones Free duran como máximo unas horas (sin garantía) y se cortan antes por inactividad. **Mitigación:** el pipeline guarda `last.pt` cada `checkpoint_every_steps` (250 en `small`) en Drive y reanuda solo; el notebook 06 copia su checkpoint de demo a Drive.
2. **Sin persistencia de disco**: el filesystem se borra al cerrar. **Mitigación:** `drive.mount()` para checkpoints y corpus procesado.
3. **fp16 en T4, no bf16**: fp16 tiene rango dinámico pequeño (~6e-5 a 65 504) → riesgo de overflow en gradientes. **Mitigación:** `GradScaler` (loss scaling dinámico), explicado en F6.
4. **RAM de sistema limitada (~12 GB Free)**: cargar corpus grandes en memoria falla. **Mitigación:** `datasets` con Arrow memory-mapped + streaming.
5. **Cuotas de GPU opacas**: el uso intensivo agota la cuota Free. **Mitigación:** los notebooks SMALL entrenan pocos pasos; el `small` del pipeline (~1.5–2 h estimadas) es más cómodo en Kaggle, que tiene cuota semanal fija.
6. **Versiones preinstaladas**: Colab trae torch/numpy fijados; instalar versiones incompatibles rompe el runtime. **Mitigación:** los notebooks instalan solo lo faltante (`pip install -q`); el notebook 09 instala `requirements.txt`, cuyo `torch>=2.4` ya está satisfecho en Colab y no se reinstala.

## Presupuesto de VRAM (regla práctica)

Para entrenar con AdamW en precisión mixta, por cada parámetro se necesita aproximadamente:

| Componente | Bytes/parám | Comentario |
|------------|-------------|------------|
| Pesos (fp16/bf16) | 2 | copia de cómputo |
| Pesos master (fp32) | 4 | mantenida por el optimizador |
| Gradientes | 2 | en la precisión de cómputo |
| AdamW: momento m | 4 | fp32 |
| AdamW: varianza v | 4 | fp32 |
| **Total** | **~16** | + activaciones (depende de B·T) |

→ Modelo de **~100 M params ≈ 1.6 GB** de estados de entrenamiento + activaciones. Por eso el `large` del pipeline (~101 M) cabe holgado en 24–40 GB y lo que limita el batch son las activaciones (~O(B·T·d·capas) y los logits B·T·vocab); y con QLoRA (pesos base en 4-bit congelados, solo adaptadores entrenables) se puede fine-tunear un modelo de 7 B en 16 GB.

**Memoria de activaciones** (lo que realmente mata en secuencias largas): crece como $O(B \cdot T \cdot d)$ por capa, y la matriz de attention como $O(B \cdot h \cdot T^2)$ — la motivación de Flash Attention (F5 §13).

## Detección automática

- **Notebooks 00–08:** su celda de setup detecta CUDA > MPS > CPU y elige SMALL/LARGE por VRAM con código
  inline (forzable con `PROFILE = "small" | "large"`). No importan `llm_lab`.
- **Pipeline:** `scripts/pretrain.py` llama a `llm_lab.utils.hardware.detect_hardware()` para informar el
  hardware; el perfil lo eliges tú (`--profile small`). Si pides bf16 en una GPU sin soporte, cambia a fp16;
  en CPU usa fp32.
