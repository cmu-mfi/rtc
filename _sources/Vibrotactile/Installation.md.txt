# Vibrotactile System - Installation

![vbt-setup](../files/vbt-setup.png)

```{contents}
```

## Pre-requisites

### Hardware 

| Name | Suggested Order Link | Quantity | Price | Total Cost|
|-------|-------------|-------------|-------------|-------------|
| Behringer UMC 404HD | [Sweetwater](https://www.sweetwater.com/store/detail/UMC404HD--behringer-u-phoria-umc404hd-usb-audio-interface) | 1 | $109.00 | $109.00 |
| 5 Pack of Piezoelectric Contact Microphones | [Amazon](https://www.amazon.com/TIMESETL-Microphone-Self-Adhesive-Instrument-Mandolin/dp/B07ZTBVKRD/ref=sr_1_5?crid=1OHNBI7Y4OM4U&dib=eyJ2IjoiMSJ9.-PibDNlinRz79bIpdumGJHAAdW3PdumsNrUWTrBZB4hYry4WdTr78zPfu4ZnYQWFlwNLi0yY8THnebiukewvbaDljZXfaSdQ0njt5TC4QlHQUbw-4_M51b1tVUYlgZl6bLj9okH0wZqaFYOOhAo4upt3WI4d1Tj6ApClqPZNZep-iIMk3dItQ0ypgfMbxqWdPuSmfoJVkW-mXZQSGQE25jBOfYMTwTv_7UsH_2RJuBoABTUdnXDijXNkBa1PxqxMXAsXIjy9HopNVacSJfhPereGmHMmK3gLGBOpPmN7eJc.JVs0GaesD3pa5oN6mlhvDtEM4Jdsj8TEvta9yf8iEBU&dib_tag=se&keywords=contact+microphone&qid=1728404098&sprefix=contact+microphone%2Caps%2C116&sr=8-5) | 1 | $14.99 | $14.99 |
| 5 Pack of Piezoelectric Contact Microphones | [Amazon](https://www.amazon.com/TIMESETL-Microphone-Self-Adhesive-Instrument-Mandolin/dp/B07ZTBVKRD/ref=sr_1_5?crid=1OHNBI7Y4OM4U&dib=eyJ2IjoiMSJ9.-PibDNlinRz79bIpdumGJHAAdW3PdumsNrUWTrBZB4hYry4WdTr78zPfu4ZnYQWFlwNLi0yY8THnebiukewvbaDljZXfaSdQ0njt5TC4QlHQUbw-4_M51b1tVUYlgZl6bLj9okH0wZqaFYOOhAo4upt3WI4d1Tj6ApClqPZNZep-iIMk3dItQ0ypgfMbxqWdPuSmfoJVkW-mXZQSGQE25jBOfYMTwTv_7UsH_2RJuBoABTUdnXDijXNkBa1PxqxMXAsXIjy9HopNVacSJfhPereGmHMmK3gLGBOpPmN7eJc.JVs0GaesD3pa5oN6mlhvDtEM4Jdsj8TEvta9yf8iEBU&dib_tag=se&keywords=contact+microphone&qid=1728404098&sprefix=contact+microphone%2Caps%2C116&sr=8-5) | 1 | $14.99 | $14.99 |
| Cable Matters 2-Pack 1/4 Inch Cable 6 Feet | [Amazon](https://www.amazon.com/Cable-Matters-2-Pack-Straight-Instrument/dp/B073RMQKYG/ref=sr_1_5?crid=3CAXQV30GAW34&dib=eyJ2IjoiMSJ9.Kt4WgCJJxKgRCeq0DAJKS-hNN4erYY2vaNujsRJ79_VO1tDk5Lk_iwploE1cLZ84vf7-BUaTykY2GWsQ-ok3Cxo31LQ-_hUiD-dSBHQGE66CwqGDRkAYst0p9N8vxKShFFfwDUwgWAv5Zr7fwUBfH6WKmorjgqEohj5LpuAUZSFXZHCbsmui-RZapHChPC0qWVZIvvXxeVhLABGOOtuXiKXuITo_nMy1gSxIlrr5y5yHl3O_oRLR_WkkS9XHgQiJUMZWROeesGbWotCmyGCRZQ21p-_ISN1SPshgiikzoZc.UjQgkGwOghuAMmPTfaykA48QvzMRfXTSK0Cc3Xy4KKg&dib_tag=se&keywords=1%2F4%2Bto%2B1%2F4%2Baudio%2Bcable&qid=1728404189&sprefix=1%2F4%2Bto%2B1%2F4%2Baudio%2Bcabl%2Caps%2C112&sr=8-5&th=1) | 2 | $9.99 | $18.98 | 

*insert diagram of how things need to be connected*

*insert few key notes*

### Software

There are two levels of software installation required for the vision system.

<a href="https://github.com/cmu-mfi/vibro_tactile_toolbox" class="inline-button"><i class="fab fa-github"></i>vibro_tactile_toolbox</a>

**1. Device Interfaces**\
This includes the installation of the software required to interface with the hardware components like robots, cameras, grippers, etc.

ROS Nodes for the devices can be launched using docker-compose.yml in `docker/` directory. It will need modification if using other hardware, like a different camera or force torque sensor.

**2. Vibrotactile System**\
This includes the installation of the software required to run the vibrotactile system which involves teach, learn and execute tasks described in the [overview](Vibrotactile.md) section.

## Installation Steps

1. **Step 1: Device Interfaces**
    - Make sure the devices are connected and working properly.
    - Pre-requisite for the vision system is one robot arm, 2-4 contact microphones, one force torque sensor, once side camera and one gripper.

        ```shell

        $ cd docker
        $ docker compose up --build

        ```
    > Note: If using different hardware, modify the `docker-compose.yml` file accordingly.
<br>

2. **Step 2: Systems Check**

    - Run test docker compose ....
    ....

3. **Step 3: Create Config Files**

    - `<create / modify config files>`


4. **Step 4: TEACH - Collect training data**
    ...

5. **Step 5: LEARN - Train the models**
    ...

6. **Step 6: EXECUTE - Validate the system**
    ...