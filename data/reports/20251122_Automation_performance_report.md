# Performance Report for 20251122_Automation

## Critical Events - Frame Time (ms)
| Device Profile | BeginFrame | FEngineLoop::Tick | Tick Time | Frame Sync Time | RedrawViewports | Slate::Tick (Time and Widgets) | Net Tick Time | STAT_FEngineLoop_Tick_SlateInput |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| mid | <span style="color:red">38.80</span> | <span style="color:red">38.67</span> | <span style="color:red">15.56</span> | <span style="color:red">6.65</span> | <span style="color:red">3.85</span> | <span style="color:red">3.38</span> | <span style="color:green">0.88</span> | <span style="color:green">0.31</span> |

## Critical Events - Over Budget (ms)
| Device Profile | BeginFrame | FEngineLoop::Tick | Tick Time | Frame Sync Time | RedrawViewports | Slate::Tick (Time and Widgets) | Net Tick Time | STAT_FEngineLoop_Tick_SlateInput |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| mid | <span style="color:red">16.58</span> | <span style="color:red">16.45</span> | <span style="color:red">7.78</span> | <span style="color:red">3.32</span> | <span style="color:red">2.30</span> | <span style="color:red">0.05</span> | <span style="color:green">-1.34</span> | <span style="color:green">-0.80</span> |

## Tick Related Events - Frame Time (ms)
| Device Profile | AnimGameThreadTime | USkinnedMeshComponent_TickComponent | FStartPhysicsTickFunction_ExecuteTick | Game TaskGraph Stalls | Char Movement Total | PlayerController Tick |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| mid | 4.52 | 4.51 | 1.53 | 1.10 | 1.01 | 0.75 |
