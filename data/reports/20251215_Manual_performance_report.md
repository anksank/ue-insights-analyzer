# Performance Report for 20251215_Manual

## Critical Events - Frame Time (ms)
| Device Profile | Device Name | BeginFrame | FEngineLoop::Tick | Tick Time | Frame Sync Time | RedrawViewports | Slate::Tick (Time and Widgets) | STAT_FEngineLoop_Tick_SlateInput | Net Tick Time |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Low1 | Moto_G85_XT2427-3 | <span style="color:red">27.21</span> | <span style="color:red">27.12</span> | <span style="color:red">10.01</span> | <span style="color:red">4.29</span> | <span style="color:red">1.98</span> | <span style="color:green">1.68</span> | <span style="color:red">1.28</span> | <span style="color:green">0.89</span> |
| Low0 | POCO_M6 Pro_23076PC4BI | <span style="color:red">39.72</span> | <span style="color:red">39.61</span> | <span style="color:red">12.37</span> | <span style="color:red">7.01</span> | <span style="color:red">2.44</span> | <span style="color:green">1.96</span> | <span style="color:green">1.63</span> | <span style="color:green">1.45</span> |
| Low1 | Redmi_Note8_Pro_M19067l | <span style="color:red">50.50</span> | <span style="color:red">50.31</span> | <span style="color:red">17.27</span> | <span style="color:red">15.73</span> | <span style="color:red">4.22</span> | <span style="color:green">2.77</span> | <span style="color:red">1.16</span> | <span style="color:green">1.63</span> |
| Low0 | Vivo_Y33S_V2109 | <span style="color:red">55.20</span> | <span style="color:red">54.88</span> | <span style="color:red">17.73</span> | <span style="color:red">13.59</span> | <span style="color:red">3.65</span> | <span style="color:green">3.17</span> | <span style="color:red">2.45</span> | <span style="color:green">2.92</span> |

## Critical Events - Over Budget (ms)
| Device Profile | Device Name | BeginFrame | FEngineLoop::Tick | Tick Time | Frame Sync Time | RedrawViewports | Slate::Tick (Time and Widgets) | STAT_FEngineLoop_Tick_SlateInput | Net Tick Time |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Low1 | Moto_G85_XT2427-3 | <span style="color:red">4.99</span> | <span style="color:red">4.90</span> | <span style="color:red">2.23</span> | <span style="color:red">0.96</span> | <span style="color:red">0.43</span> | <span style="color:green">-1.65</span> | <span style="color:red">0.17</span> | <span style="color:green">-1.33</span> |
| Low0 | POCO_M6 Pro_23076PC4BI | <span style="color:red">6.39</span> | <span style="color:red">6.28</span> | <span style="color:red">0.70</span> | <span style="color:red">2.01</span> | <span style="color:red">0.11</span> | <span style="color:green">-3.04</span> | <span style="color:green">-0.04</span> | <span style="color:green">-1.88</span> |
| Low1 | Redmi_Note8_Pro_M19067l | <span style="color:red">28.28</span> | <span style="color:red">28.09</span> | <span style="color:red">9.49</span> | <span style="color:red">12.40</span> | <span style="color:red">2.67</span> | <span style="color:green">-0.56</span> | <span style="color:red">0.05</span> | <span style="color:green">-0.59</span> |
| Low0 | Vivo_Y33S_V2109 | <span style="color:red">21.87</span> | <span style="color:red">21.55</span> | <span style="color:red">6.06</span> | <span style="color:red">8.59</span> | <span style="color:red">1.32</span> | <span style="color:green">-1.83</span> | <span style="color:red">0.78</span> | <span style="color:green">-0.41</span> |

## Tick Related Events - Frame Time (ms)
| Device Profile | Device Name | AnimGameThreadTime | Game TaskGraph Stalls | USkinnedMeshComponent_TickComponent | Char Movement Total | FStartPhysicsTickFunction_ExecuteTick | PlayerController Tick |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Low1 | Moto_G85_XT2427-3 | 1.65 | 1.58 | 1.46 | 0.93 | 0.58 | 0.36 |
| Low0 | POCO_M6 Pro_23076PC4BI | 2.36 | 1.25 | 2.48 | 1.07 | 0.91 | 0.46 |
| Low1 | Redmi_Note8_Pro_M19067l | 3.54 | 0.23 | 4.49 | 1.15 | 2.75 | 0.42 |
| Low0 | Vivo_Y33S_V2109 | 3.57 | 1.06 | 3.31 | 1.68 | 1.15 | 0.64 |
