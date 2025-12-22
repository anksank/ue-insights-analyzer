# Performance Report for 20251122_Automation

## Critical Events - Frame Time (ms)
| Device Profile | BeginFrame | FEngineLoop::Tick | Tick Time | Frame Sync Time | RedrawViewports | Slate::Tick (Time and Widgets) | Net Tick Time | STAT_FEngineLoop_Tick_SlateInput |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| mid | 38.80 | 38.67 | 15.56 | 6.65 | 3.85 | 3.38 | 0.88 | 0.31 |

## Critical Events - Over Budget (ms)
| Device Profile | BeginFrame | FEngineLoop::Tick | Tick Time | Frame Sync Time | RedrawViewports | Slate::Tick (Time and Widgets) | Net Tick Time | STAT_FEngineLoop_Tick_SlateInput |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| mid | 16.58 | 16.45 | 7.78 | 3.32 | 2.30 | 0.05 | -1.34 | -0.80 |

## Tick Related Events - Frame Time (ms)
| Device Profile | AnimGameThreadTime | USkinnedMeshComponent_TickComponent | FStartPhysicsTickFunction_ExecuteTick | Game TaskGraph Stalls | Char Movement Total | PlayerController Tick |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| mid | 4.52 | 4.51 | 1.53 | 1.10 | 1.01 | 0.75 |
