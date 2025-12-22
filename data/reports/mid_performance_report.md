# Performance report for mid []

## Summary of Critical Events
| Event Name | Frame Time (ms) | Budget (ms) | Over Budget (ms) |
| :--- | :---: | :---: | :---: |
| BeginFrame | 38.80 | 22.22 | 16.58 |
| FEngineLoop::Tick | 38.67 | 22.22 | 16.45 |
| Tick Time | 15.56 | 7.78 | 7.78 |
| Frame Sync Time | 6.65 | 3.33 | 3.32 |
| RedrawViewports | 3.85 | 1.55 | 2.30 |
| Slate::Tick (Time and Widgets) | 3.38 | 3.33 | 0.05 |
| Net Tick Time | 0.88 | 2.22 | -1.34 |
| STAT_FEngineLoop_Tick_SlateInput | 0.31 | 1.11 | -0.80 |

## Summary of Tick Related Events
| Event Name | Frame Time (ms) |
| :--- | :---: |
| AnimGameThreadTime | 4.52 |
| USkinnedMeshComponent_TickComponent | 4.51 |
| FStartPhysicsTickFunction_ExecuteTick | 1.53 |
| Game TaskGraph Stalls | 1.10 |
| Char Movement Total | 1.01 |
| PlayerController Tick | 0.75 |
