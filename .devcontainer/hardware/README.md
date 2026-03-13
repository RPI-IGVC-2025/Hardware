# Running the hardware development container

## Requirements

### ZED camera & utilites
- USB 3.0+ port(s)
- 8GB+ RAM
- NVIDIA RTX GPU with compute capability ≥ 7.5 
- Linux host filesystem: 
    - NOT WSL, as it doesn't have webcam drivers and has to use usb-ip to do usb passthrough
        - WSL may be used if you're not actually connecting to a webcam  
- Latest NVIDIA drivers on the host
- [Nivida container toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html) on the 
